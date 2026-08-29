---
name: winner-crawl
description: Crawl the Hoolest Meta ad account for winner video creatives (ad-level spend and ROAS over the bar), match them to their Video Brief row in Notion by Creative ID, and set Performance to Winner. Use when the user asks to check for winners, find winning creatives, run the weekly winner crawl, or tag winners in Notion.
---

# Winner crawl

Automates: **crawl the ad account at ad level → keep video creatives over the spend and ROAS
bar → match to the Notion Video Brief row → set `Performance` = `Winner`.**

Thresholds, scope, the account id and the Notion destination all live in
`config/winner-criteria.yml`. Read that file first, every run. Never hardcode the numbers.

## The bar

A creative is a winner when, **at ad level** over the configured window, it has both:

- spend ≥ `min_spend_usd` (default $1,000 USD), and
- `purchase_roas` ≥ `min_roas` (default 1.8)

Ad level means one hook variant, not the campaign and not the ad set. A campaign that
averages 1.9 is not a winner; the individual ad has to clear the bar on its own.

## Video only, and why that also keeps writes correct

**Scope is video.** An ad name carrying a `VID` token is a video. Anything without one is out
of scope and is not evaluated — not a winner, not a near miss, not a line item. That covers:

- **Statics** — `HPT045_IMG_Back to School Sale_…`, `HPT034 IMG Hero Product 6D …`
- **Creator / whitelist ads** — `WillBurger_VeReliefPrime_20260812_trybe=…`. These are videos
  in reality but carry no `VID` token and follow no naming convention, so there is nothing to
  match on. Out of scope until they are named to convention.
- **Legacy one-offs** — `Prime _ PDP_BOFU _ …`, `Longform - Nov 26th`, `Nick in the woods HP Ad`.

Report only a **count** of what was skipped, so nothing is hidden, but do not itemise it.

The same rule is what stops bad writes. **The HPT namespace collides across formats** — statics
run their own HPT sequence that reuses numbers already spent on videos, for different concepts:

| HPT | Notion Video Brief (VID) | Meta static ad (IMG) |
|---|---|---|
| HPT033 | Stuck on Fight or Flight – AI UGC | PEMF Statics *(Mini Max PEMF)* |
| HPT034 | Worth of investment | Hero Product *(Mini Max PEMF)* |
| HPT038 | Gel Tip Vs Gel Paste 3 | US vs THEM |
| HPT039 | Gel Tip Vs Gel Paste 4 | B2G1 Bundles |
| HPT045 | Ronak UGC | Back to School Sale |

Matching on the number alone tags *"HPT034 – Worth of investment"*, a VeRelief Prime video, as
a winner off a **Mini Max PEMF static's** ROAS. The write succeeds, looks plausible, and is
wrong. Filtering to `VID` first removes the whole class of error.

So after the `VID` filter, still cross-check the concept slug against the Notion `Concept Name`.
Below `concept_match_min_overlap`, **report it, do not write it.** **Two Notion rows can share a
Creative ID** — HPT022 is both "Hard to sleep" and "Top 5 Objection"; HPT031 is "Stuck on Fight
or Flight" and "…2". The concept-name check is what picks the right one. If it cannot, report
the ambiguity and leave both rows alone.

## Run it

```
/winner-crawl
```

Scope it: `/winner-crawl last 90 days`, or `/winner-crawl dry run` to report without writing.

## Pipeline

### 1. Read config
`config/winner-criteria.yml`. Thresholds, window, scope, account id, Notion data source.

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

### 3. Filter to video, then parse

**Drop every ad whose name carries no `VID` token.** Keep a count for the report. Then parse
what remains — house convention, underscore-delimited:

```
HPT044_VID_Top 5 Q&A - Listicle (HPT025)_3B_VeRelief Prime_AI VO_...
└─┬──┘ └┬┘ └────────────┬─────────────┘ └┬┘
Creative Format      Concept          Variant
```

- **Creative ID** — leading `HPT` + digits. Zero-pad to three (`HPT44` → `HPT044`).
- **Format** — token 2, `VID` by definition after the filter.
- **Concept** — token 3.
- **Variant** — token 4, the hook variant (`3B`, `1Ac-Z1`). This goes in `Winning version`.

Real names are messier than the spec. Handle:

- **Trailing suffixes** — ` -  7/28/26`, ` - Copy`. Strip before parsing. A ` - Copy` is a
  duplicate of an existing ad; keep whichever row has the higher spend, do not double-count.
- **Truncated names** — Meta cuts long names (`HPT041_VID_Price Objection 2_3C_VeRelief Prime_Fou`).
  The first four tokens survive, which is all this needs.
- **Space-delimited names** — a few older ads use spaces instead of underscores. Split on
  whitespace when there are no underscores. (In practice these are all statics, so they are
  usually gone by this point.)

### 4. Collapse variants to concepts

Several ads share one Creative ID (HPT052 runs `5B`, `2B`, and copies of `2B`). One Notion row
covers all of them. **Any single variant clearing the bar makes the concept a winner** — that
is what "ad level" means. Record the *highest-ROAS qualifying variant* as `Winning version`.

### 5. Match to Notion

Query the Video Brief data source for `Creative ID`, `Concept Name`, `Performance`,
`Winning version`, `url`. Match on Creative ID, then confirm with the concept name per
**Video only, and why that also keeps writes correct** above.

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

In chat:

1. **Tagged** — Creative ID, concept, variant, spend, ROAS, Notion link.
2. **Already tagged** — cleared the bar, row already had a Performance value.
3. **Near misses** — video creatives within 10% of either threshold. Next week's candidates.
4. **Unmatched** — video creatives that cleared the bar but had no confident Notion row
   (missing row, or concept name did not corroborate). Usually empty; when it is not, it means
   a brief was never filed or an ad was misnamed, and both are worth fixing.

Then one line: how many ads were skipped as out of scope (no `VID` token), and the window and
both thresholds — so the numbers are never read without their basis.

## What it deliberately does not do

- **Never evaluates a non-video ad.** No `VID` token, no consideration. Statics and creator ads
  are out of scope, and a winning static is not a finding.
- Never creates a Video Brief row — it only updates existing ones.
- Never writes `Loser` or `High Potential`, and never overwrites a Performance value a human set.
- Never writes to a row whose concept name does not corroborate the Creative ID.
- Never touches any ad account other than the one in config.
