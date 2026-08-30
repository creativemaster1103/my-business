---
name: inspo-harvest
description: Daily top-up of the TrendTrack Inspo Bank. Sweeps the tracked competitor watchlist for ads still actively running past the longevity threshold (default 30 days), vets them, and files the keepers into the Inspo Bank favorites folder in TrendTrack. Use when the user asks to harvest competitor creatives, top up the inspo bank, run the daily competitor check, or stock the swipe queue. Does not write briefs — that is /competitor-ad-swipe.
---

# Inspo Harvest → TrendTrack Inspo Bank

Keep the **Inspo Bank** stocked with competitor ads that have proven themselves, so the weekly
swipe always has vetted candidates to draw from.

This is the **front half** of the creative pipeline, split out to run daily:

```
/inspo-harvest   (daily)   competitors → vet → Inspo Bank         ← this skill
/competitor-ad-swipe (weekly)  Inspo Bank → rewrite → Notion brief
```

The two never overlap. **This skill only ever ADDS to the bank.** It never briefs, never writes
to Notion, and never removes anything — draining the bank is the swipe's job.

## Why daily, and why it is usually cheap

The bank has to run about four weeks ahead of a five-a-week briefing target. Topping it up once
a week means a quiet fortnight from the competitors starves the pipeline with no warning.

But a daily sweep of nine brands would burn the TrendTrack quota for no reason. So this skill is
**demand-driven, not schedule-driven**: it reads the bank first, and if the bank is already at
target it exits having spent almost nothing. Most days should be a no-op. The cost is only paid
on the days the bank actually needs filling.

## Required connectors

| Connector | Used for |
|---|---|
| **Trend Track MCP** | Everything — discovery, dedupe, and the favorites write |

That is the only one. If it is not enabled, **stop and say so.** Do not scrape `trendtrack.io`
as a workaround — direct HTTPS to it is blocked by the egress proxy by design, and all access
goes through the MCP connector on a different path.

## Run the pipeline

### 0. Credit guard

```
usage_get()
```

Use `usage_get` as the canonical number — the `credits.creditsRemaining` field returned inline
on other calls reports a different figure and is not the quota that matters.

Read `harvest.credit_reserve` from `config/competitors.yml`. **If `includedQuota.remaining` is
below the reserve, stop immediately** and report the balance. The reserve exists to protect the
weekly swipe: a harvest that drains the quota on a Saturday leaves Sunday's swipe unable to run,
which trades a nice-to-have for the thing that actually ships briefs.

Note the billing period rolls over on the 3rd. A run late in the period has less headroom than
the same run on the 5th.

### 1. Load the watchlist

Read `config/competitors.yml`:

- `competitors` — sweep in `priority` order: **high, then medium, then low**
- `min_days_running` / `max_days_running` — the longevity window
- `inspo_bank_folder_id`, `inspo_bank_target_size`
- `harvest.*` — the daily-run controls
- `excluded_angles` — angles that never transfer

If the user named a specific competitor, that overrides the watchlist for this run.

### 2. Measure the bank — and stop early if it is full

The three state folders, all **`scope: "personal"`** (Mark's own favorites, a separate namespace
from the workspace — omitting `scope` returns "this resource isn't in TrendTrack"):

| Folder | id | Role here |
|---|---|---|
| `Inspo Bank → To Remake` | `6985225d-84f3-4e72-b831-96938ac00b9a` | **Destination.** |
| `★ Mark's Picks (any vertical)` | `4c9e5267-210a-464e-99d0-1fc4ec25efe5` | Subfolder of the bank. Read-only here — counts toward the total, never written to. |
| `Swiped → VeRelief Briefs` | `a608a57a-d8fc-47cb-87a6-f3d1b08076b1` | Already briefed. Exclusion set. |

```
list_favorites(type="ads", scope="personal",
               folder="6985225d-84f3-4e72-b831-96938ac00b9a", limit=25)
```

Listing the bank returns **only its own items, not the subfolder's** — count `★ Mark's Picks`
with its own call and add the two.

```
deficit = inspo_bank_target_size − (bank_count + picks_count)
```

**If `deficit` is zero or less, stop here.** Report the bank level and exit. This is a
successful run, not a skipped one — say so plainly so a string of quiet days does not read as a
broken automation.

Otherwise cap the run: `to_add = min(deficit, harvest.max_adds_per_run)`.

### 3. Build the exclusion set

Page through `pagination.totalPages` on **all three** folders and collect, for every ad:

- `ad.id`
- `content.body`, normalized (trim, collapse whitespace, lowercase)
- `collationId` where present

The id check alone is not enough, and this bank proves it: three of its five entries are the
same Pulsetto creative re-uploaded under different ad ids, with byte-identical `content.body`.
Brands re-upload constantly — Pulsetto had 80 copies of one ad. **An ad whose normalized body
or `collationId` matches something already banked or swiped is the same ad**, whatever its id
says. Drop it.

### 4. Sweep, in priority order, stopping as soon as the bank is filled

Per brand, highest priority first:

```
get_brandtracker_scaling_ads(
  brandtracker_id  = <uuid from config>,
  min_days_running = <min_days_running from config>,
  max_days_running = <max_days_running from config>,
  status           = "active",
  media_type       = "video",
  ad_rank_sort     = "current_rank",
  limit            = <harvest.sweep_limit>
)
```

**Check the count after each brand and stop the moment you have `to_add` keepers.** Every extra
brand call is spent quota. Do not sweep all nine out of tidiness.

Four things that are easy to get wrong:

- **`status: "active"` is not optional.** The whole premise is an ad *still running* past the
  threshold — a competitor still paying for it today. `status: "all"` silently admits dead ads,
  and a dead ad is not a validated ad, it is one they killed. The bank currently holds five
  inactive entries for exactly this reason; do not add to them.
- **`min_days_running` does the 30-day filter server-side.** Never filter by hand and never
  lower it. Recently-ended ads are a deliberate escalation rung in the *weekly* swipe, not
  something the daily harvest reaches for.
- **`main_countries` only matches EU/UK** (Meta transparency reporting). For US ads use
  `ad_countries`, or leave country unset and read `audience.targetedCountries`.
- Each call costs credits — roughly 12 units at `limit: 8`. That is the whole reason for the
  early exits in steps 0, 2 and here.

**Do not trust `daysRunning` from this endpoint on its own.** The scaling endpoint returns
`lastSeenAt: null` and appears to compute `daysRunning` as first-seen-to-today, which
*overstates* any ad that has already stopped. Pinning `status: "active"` is most of the defence,
but it is not all of it — verify true run length against the enriched favorites record before
banking, and drop anything whose genuine run is under `min_days_running`.

This is almost certainly how the bank ended up holding entries that ran 22, 5 and 23 days. An
overstated `daysRunning` is invisible at the point of banking and only shows up weeks later, in
the swipe, as a candidate that never deserved the queue slot.

### 5. Rank the survivors

**Longevity × duplicates, not `daysRunning` alone.** `metrics.duplicates` is how many times the
brand re-uploaded the creative: a 272-day ad with 80 duplicates is a brand shouting about a
winner; a 392-day ad with 10 is one they forgot to switch off. `metrics.reach` and
`estimatedSpend` break ties.

### 6. Vet before banking

The bank is a queue of things *worth remaking*, not a dump of everything that cleared 30 days.
A too-generous harvest just moves the judgement work into the swipe, where it costs more. Drop
a candidate if:

- Its primary angle matches one in `excluded_angles` — prescription/medication replacement,
  named-condition treatment claims, ingestible dosing, subscription-only mechanics. None of
  those transfer to a $399 non-prescription wellness device, so banking one guarantees the
  swipe throws it away later.
- It is a near-duplicate of anything in the exclusion set (step 3) **or of anything else picked
  this same run**.
- Its angle could not honestly carry a VeRelief Prime rewrite. When unsure, skip it — the cost
  of a thin bank is visible and the cost of a padded one is not.

Prefer candidates mapping to the under-served avatars in `prefer_avatars` (HRV Hunter, Sleep
Struggler, Off-Ramper) when two are otherwise close. The Video Brief library is heavily skewed
toward Wired Lifer, and the bank is where that gets corrected cheaply.

### 7. Bank them

```
add_favorite_item(type="ads", scope="personal", item_id="<ad.id>",
                  folder_id="6985225d-84f3-4e72-b831-96938ac00b9a")
```

Add to the **bank root**, never to `★ Mark's Picks` — that subfolder means "a human chose this"
and an automation writing into it destroys the distinction the swipe relies on to prioritize.

**These folders are Mark's private working state.** Never call
`set_favorite_folder_visibility` with `organization` on them, and never call
`create_favorite_folder_share_link` on them — a folder share link is a public URL with **no
API to revoke it**, so creating one is a one-way door. (Ad-level `create_ad_share_link` is
different and is fine; the swipe uses it for the AD INSPO embed.)

Note that visibility and scope are the same axis in TrendTrack: setting a workspace folder
`private` moves it into personal scope and silently changes which `scope` argument every later
call needs.

### 8. Report

Short. A table of what was banked — brand, days running, duplicates, angle, ad id — then:

- bank level before → after, against target
- one line for skips, as counts by reason, not one line each
- credits consumed and remaining

If the bank came up short of target after sweeping every brand, **say so plainly.** That is the
signal that matters: it means the competitors are not producing enough keepers, and the weekly
target is outrunning supply. It is real information about the market. Do not lower
`min_days_running`, widen to inactive ads, or pad with mediocre candidates to make the number
look right.

## Guardrails

- **Only ever adds.** Never removes from the bank, never writes Notion, never files a brief.
  If the bank looks wrong, report it — do not clean it up.
- **`status: "active"` and `min_days_running` never relax.** They are the entire signal. An ad
  that is not still running has not proven anything.
- **Never write into `★ Mark's Picks`.** Bank root only.
- **`scope: "personal"` on every favorites call.** Workspace and personal are separate
  namespaces and the workspace one is the wrong bank.
- **Keep the folders private.** No organization visibility, no folder share links, ever.
- **Respect the credit reserve.** The weekly swipe outranks the daily top-up; if the quota is
  tight, the harvest is what gets skipped.
- **A full bank is a successful run.** Exiting at step 2 having done nothing is the design
  working, not a failure to report.
