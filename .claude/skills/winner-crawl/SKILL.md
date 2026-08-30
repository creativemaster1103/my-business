---
name: winner-crawl
description: Pull ad-level performance from the Hoolest Meta ad account over a rolling window, find every VIDEO creative that clears both the spend and ROAS floors, and tag its matching Notion Video Brief row as a Winner with the winning hook variant. Use when the user asks to crawl for winners, tag winning ads, run the weekly winner crawl, or find which creatives are winning.
---

# Winner Crawl → Notion Video Brief

Close the loop on the creative pipeline. Briefs go out to editors, ads go live on Meta, and
this is the step that walks the results back into Notion so the team can see which concepts
actually won.

The premise: **the brief database is the creative memory, and it is only useful if it knows
what worked.** An untagged library tells you what was made, not what to make more of.

Read `config/winner-criteria.yml` first, every run. Thresholds, window, scope, ad account and
Notion destination all live there. Never hardcode a number from this document — the numbers
below are illustrative of the shape of the data, not the criteria.

## Required connectors

| Connector | Used for |
|---|---|
| **Meta Ads** | Ad-level spend and purchase ROAS from the Hoolest account |
| **Notion** | Destination: the Video Brief database |

If either is missing, **stop and name it.** Do not scrape, do not substitute another data
source, do not file partial results. A run that tags half the winners is worse than a run that
tags none, because nobody can tell which half.

## The pipeline

```
Meta Ads: ad-level insights, window from config, sort by spend desc, page
      ↓  DROP every ad with no VID token  ← load-bearing, see below
      ↓  aggregate duplicates by (Creative ID, variant)
      ↓  keep ads clearing BOTH min_spend AND min_roas
Notion: match Creative ID → cross-check Concept Name
      ↓  skip any row whose Performance is already set
Notion: set Performance = Winner, Winning version = the variant token
```

## Step 1 — Pull the ads

```
ads_get_ad_entities(
  ad_account_id = <from config>,
  level         = "ad",
  date_preset   = <window from config>,
  fields        = ["name", "amount_spent", "purchase_roas", "impressions"],
  sort          = "amount_spent_descending",
)
```

Page until the spend column drops below `min_spend` — everything past that point fails the
floor by construction, so there is no reason to keep reading.

### API quirks on this account — all three are real

1. **`filtering` is silently ignored.** It does not error. It returns an unfiltered result set
   that looks filtered, which is the worst possible failure. Sort by spend descending, page,
   and apply both thresholds yourself in the client.
2. **`date_preset: maximum` breaks sorting.** Use the rolling window from config.
3. **`amount_spent` comes back as a formatted string**, e.g. `"$26,726.78 USD"` — with a
   non-breaking space before the currency code. Strip `$`, `,`, ` ` and the code before
   comparing. `purchase_roas` is a plain decimal string.

## Step 2 — Drop everything that is not a video

**This is a correctness control, not a scope preference.** Do it before evaluating anything.

An ad is in scope only if its name carries a `VID` token in the format position. Everything
else is out: statics (`IMG`), creator/whitelist ads, and legacy one-offs. They are not winners
and they are **not near misses** — they never enter the evaluation at all. Report only a count.

### Why the VID filter is load-bearing

The HPT numbering namespace **collides across formats.** Statics reuse HPT numbers that already
belong to entirely different video concepts in Notion. This is not hypothetical — as of
2026-08-30:

| HPT | In Meta (static) | In Notion (video) |
|---|---|---|
| HPT034 | `IMG Hero Product` — Mini Max PEMF, **ROAS 3.32** | "Worth of investment" |
| HPT039 | `IMG B2G1 Bundles` — ROAS 1.56 | "Gel Tip Vs Gel Paste 4" |
| HPT045 | `IMG Back to School Sale` — ROAS 1.53 | "Ronak UGC" |
| HPT038 | `IMG US vs THEM` | "Gel Tip Vs Gel Paste 3" |

HPT034 is the case that should make this concrete. It is a **static, for a different product**,
and it is the single highest-ROAS ad in the account — it clears any threshold you could set.
Match it on Creative ID alone and you stamp "Winner" on a video concept called "Worth of
investment" that had nothing to do with that result. The Notion `Format` property has exactly
one option, `VID`, so the database cannot even represent the static that actually won.

**After filtering to VID, still cross-check the concept name before any write.** The VID filter
removes the systematic collision; the concept check catches the rest.

### Parsing the ad name

The house convention is
`<CreativeID>_<Format>_<Concept>_<Variant>_<Product>_<ContentType>_<Avatar>_...`, but the live
account does not honour it cleanly. Depend on the **first four fields only** and be tolerant:

- **Names are truncated by Meta.** `HPT041_VID_Price Objection 2_3C_VeRelief Prime_Fou -  7/21/26`
  stops mid-word. Anything after the variant token may simply not be there.
- **Some ads are space-delimited, not underscore-delimited.**
  `HPT034 IMG Hero Product 6D Mini Max PEMF Wired Lifter NA New Mark Mark 062426`.
  Match on `HPT(\d+)[ _](VID|IMG)[ _]` rather than splitting on `_`.
- **A trailing ` - M/D/YY` date and/or ` - Copy` suffix is common.** Strip both.
- **The variant token is two characters in practice** (`1B`, `5B`, `3C`, `8D`) even though the
  naming generator documents a four-part `1Ab-Z3` form. Take the token as written.

Names that do not match the pattern at all are out of scope. Real examples:
`WillBurger_VeReliefPrime_20260623_trybe=ee9ff2ba` (creator whitelist),
`Longform - Nov 26th - Copy` and `Prime _ PDP_BOFU _ Product-in-Hand _IMG _ V1 _ 3-02-2026`
(legacy one-offs).

## Step 3 — Aggregate duplicates

The same creative runs under multiple ad IDs, usually via a ` - Copy` suffix — `HPT052_VID_Nick
Trial Reels_2B` exists twice with separate spend. Sum spend across the duplicates and compute a
spend-weighted ROAS for the group before applying the thresholds. Evaluating the copies
separately splits the spend and can push a genuine winner below `min_spend`.

## Step 4 — Apply the thresholds

Keep an ad only if it clears **both** `min_spend` and `min_roas`. Anything clearing `min_spend`
but landing within `near_miss_roas_margin` of `min_roas` is a **near miss** — report it, never
write it. The `Performance` property offers "High Potential", and this automation does not use
it; promoting a near miss is a human decision.

## Step 5 — Match to Notion

```sql
SELECT "Creative ID", "Concept Name", "Format", "Performance", "Winning version", "Product"
FROM "<video_brief_data_source>"
WHERE "Creative ID" LIKE 'HPT%'
```

Match on Creative ID, then **confirm the Concept Name is the same concept** as the one in the
ad name. They will not be character-identical — the ad name carries the concept as typed into
the naming sheet, Notion carries the canonical title.

**Two rows can share a Creative ID.** Both HPT022 and HPT031 do:

| Creative ID | Concept Name | Performance |
|---|---|---|
| HPT022 | Hard to sleep | Winner |
| HPT022 | Top 5 Objection | — |
| HPT031 | Stuck on Fight or Flight | — |
| HPT031 | Stuck on Fight or Flight 2 | — |

The live ad `HPT022_VID_Top 5 Objection_1B_...` resolves cleanly to the second row on concept
name. HPT031's two rows would not resolve on concept alone if an ad named just "Stuck on Fight
or Flight" appeared — **report it and write nothing.** `Product` is a tiebreaker of last resort
(HPT023 is Mini Max PEMF, most rows are VeRelief Prime). Guessing here writes a permanent wrong
answer into the team's creative memory.

Numbering is sparse and non-dense — HPT036 does not exist. Never infer a row from a number.

## Step 6 — Write

For each confirmed match with `Performance` unset:

| Property | Value |
|---|---|
| `Performance` | `Winner` |
| `Winning version` | the variant token exactly as it appears in the ad name, e.g. `1B` |

Write nothing else. Do not touch `Status`, `Avatar`, `Delivery link`, or the page body.

**Promote only.** Never write `Loser`. Never write `High Potential`. Never overwrite a
`Performance` that already holds a value.

On `Winning version` format: existing rows are mostly the short token (`1B`, `3B`, `4B`, `4C`,
`1D`), with one outlier carrying the long form (HPT072 = `4Bc-Z1`). Match the short form — it
is what the ad names carry and what 7 of the 8 tagged rows use.

### When a tagged row disagrees with current data

If `Performance` is already `Winner` but a *different* variant is now winning, **leave the row
alone and say so in the report.** This is live right now: HPT044 records `3B`, but in the last
30 days variant `1B` outspent it nearly 3:1 at a higher ROAS. That is a real signal and Mark
should see it — but silently rewriting a human-set value is how an automation loses trust.
Report the disagreement; let him decide.

## Step 7 — Report

Four sections, then a footer:

- **Tagged** — Creative ID, concept, variant written, spend, ROAS, Notion link.
- **Already tagged** — cleared the floors but `Performance` was set. Flag any variant
  disagreement here.
- **Near misses** — cleared spend, missed ROAS by less than the margin.
- **Unmatched** — cleared both floors but no confident Notion row. Say why: no such Creative ID,
  or ambiguous and which candidates.

Close with: the count of out-of-scope ads skipped, the window used, and both thresholds. Always
state the thresholds — a reader needs to know what bar this run applied.

## What this skill deliberately does not do

- Never creates a Notion row. It only tags rows that already exist.
- Never writes `Loser` or `High Potential`, in any circumstance.
- Never overwrites an existing `Performance` value.
- Never edits a brief's page body, status, or assignment.
- Never evaluates statics, creator whitelist ads, or anything without a VID token.
- Never guesses which row a Creative ID means.
