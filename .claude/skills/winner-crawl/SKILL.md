---
name: winner-crawl
description: Crawl the Hoolest Meta ad account for winner creatives (ad-level spend and ROAS over the bar), match them to their Video Brief row in Notion by Creative ID, and set Performance to Winner. Use when the user asks to check for winners, find winning creatives, run the weekly winner crawl, or tag winners in Notion.
---

# Winner crawl

Automates: **crawl the ad account at ad level → keep creatives over the spend and ROAS bar
→ match to the Notion Video Brief row → set `Performance` = `Winner`.**

Thresholds, the account id and the Notion destination all live in
`config/winner-criteria.yml`. Read that file first, every run. Never hardcode the numbers.

## The bar

A creative is a winner when, **at ad level** over the configured window, it has both:

- spend ≥ `min_spend_usd` (default $1,000 USD), and
- `purchase_roas` ≥ `min_roas` (default 1.8)

Ad level means one hook variant, not the campaign and not the ad set. A campaign that
averages 1.9 is not a winner; the individual ad has to clear the bar on its own.

## Why the format token is not optional

**The HPT namespace collides across formats.** Statics run their own HPT sequence that
reuses numbers already spent on videos, for entirely different concepts:

| HPT | Notion Video Brief says | Meta static ad says |
|---|---|---|
| HPT033 | Stuck on Fight or Flight – AI UGC | PEMF Statics *(Mini Max PEMF)* |
| HPT034 | Worth of investment | Hero Product *(Mini Max PEMF)* |
| HPT038 | Gel Tip Vs Gel Paste 3 | US vs THEM |
| HPT039 | Gel Tip Vs Gel Paste 4 | B2G1 Bundles |
| HPT045 | Ronak UGC | Back to School Sale |

Matching on the number alone tags *"HPT034 – Worth of investment"*, a VeRelief Prime video,
as a winner off a **Mini Max PEMF static's** ROAS. The write succeeds, looks plausible, and
is wrong. So:

1. Parse the ad name. Accept it only if the second token is **`VID`**.
2. Cross-check the concept slug against the Notion `Concept Name`.
3. Below `concept_match_min_overlap`, **report it, do not write it.**

The Video Brief database is VID-only (`Format` has exactly one option). Statics have no row
in it — a winning static is a reporting line, never a write.

**Two Notion rows can share a Creative ID.** HPT022 is both "Hard to sleep" and "Top 5
Objection"; HPT031 is "Stuck on Fight or Flight" and "…2". The concept-name check is what
picks the right one. If it cannot, report the ambiguity and leave both rows alone.

## Run it

```
/winner-crawl
```

Scope it: `/winner-crawl last 90 days`, or `/winner-crawl dry run` to report without writing.

## Pipeline

### 1. Read config
`config/winner-criteria.yml`. Thresholds, window, account id, Notion data source.

### 2. Pull ad-level performance

`ads_get_ad_entities` with `level: "ad"`, `date_preset` from config, and
`fields: ["name", "spend", "purchase_roas", "effective_status"]`.

> **Do not trust the `filtering` parameter.** It is silently ignored on this account —
> a `amount_spent >= 1000` filter still returns $638 rows, and `purchase_roas` is rejected
> outright as unfilterable at ad level. **`sort` is reliable.** So:
>
> - sort `spend_descending`, `limit: 100`
> - page with `next_cursor`, resending every other parameter unchanged
> - **stop paging** as soon as a row falls below `min_spend_usd` — the sort guarantees
>   everything after it is smaller
> - apply both thresholds yourself, in code, on the returned rows
>
> Also avoid `date_preset: "maximum"` — it silently drops both filtering *and* sorting and
> returns rows in arbitrary order. Use `last_90d` if a wide window is wanted.

`spend` is an alias for `amount_spent` and **is** scoped to the window. Values come back as
display strings (`"$2,231.65 USD"`) — strip the currency and commas before comparing.
`purchase_roas` can be `null` (no attributed purchases); treat null as 0, never as a pass.

### 3. Parse each ad name

House convention, underscore-delimited:

```
HPT044_VID_Top 5 Q&A - Listicle (HPT025)_3B_VeRelief Prime_AI VO_...
└─┬──┘ └┬┘ └────────────┬─────────────┘ └┬┘
Creative Format      Concept          Variant
```

- **Creative ID** — leading `HPT` + digits. Zero-pad to three (`HPT44` → `HPT044`).
- **Format** — token 2. Must be `VID`.
- **Concept** — token 3.
- **Variant** — token 4, the hook variant (`3B`, `1Ac-Z1`). This goes in `Winning version`.

Real names are messier than the spec. Handle:

- **Trailing suffixes** — ` -  7/28/26`, ` - Copy`. Strip before parsing. A ` - Copy` is a
  duplicate of an existing ad; keep whichever row has the higher spend, do not double-count.
- **Space-delimited names** — `HPT034 IMG Hero Product 6D Mini Max PEMF …` uses spaces, not
  underscores. Split on whitespace when there are no underscores.
- **Truncated names** — Meta cuts long names (`HPT041_VID_Price Objection 2_3C_VeRelief Prime_Fou`).
  The first four tokens survive, which is all this needs.
- **No HPT prefix at all** — creator/whitelist ads (`WillBurger_VeReliefPrime_20260812_trybe=…`),
  legacy PDP statics (`Prime _ PDP_BOFU _ …`), one-offs (`Longform - Nov 26th`). These have no
  Video Brief row. Report them, never write.

### 4. Collapse variants to concepts

Several ads share one Creative ID (HPT052 runs `5B`, `2B`, and copies of `2B`). One Notion row
covers all of them. **Any single variant clearing the bar makes the concept a winner** — that
is what "ad level" means. Record the *highest-ROAS qualifying variant* as `Winning version`.

### 5. Match to Notion

Query the Video Brief data source for `Creative ID`, `Concept Name`, `Performance`,
`Winning version`, `url`. Match on Creative ID, then confirm with the concept name per
**Why the format token is not optional** above.

### 6. Write

For each confirmed match where `Performance` is **empty**:

```
notion-update-page  command: update_properties
  properties: { "Performance": "Winner", "Winning version": "<variant>" }
```

**Promote only.** If `Performance` already holds any value, leave it — do not overwrite, and
never write `Loser`. Report it as "already tagged" instead. Same for `Winning version`: if the
row already names a variant, keep it and note the difference rather than clobbering it.

### 7. Report

In chat, four sections:

1. **Tagged** — Creative ID, concept, variant, spend, ROAS, Notion link.
2. **Already tagged** — cleared the bar, row already had a Performance value.
3. **No Notion row** — winners that are statics, creator ads, or legacy one-offs. This is where
   a winning static surfaces; it is real signal even though nothing can be written.
4. **Near misses** — within 10% of either threshold. These are next week's candidates.

Then state the window and both thresholds, so the numbers are never read without their basis.

## What it deliberately does not do

- Never creates a Video Brief row — it only updates existing ones.
- Never writes `Loser` or `High Potential`, and never overwrites a Performance value a human set.
- Never writes to a row whose concept name does not corroborate the Creative ID.
- Never matches a non-`VID` ad to a Video Brief row.
- Never touches any ad account other than the one in config.
