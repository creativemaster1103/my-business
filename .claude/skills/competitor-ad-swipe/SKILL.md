---
name: competitor-ad-swipe
description: Find competitor ads that have been running longer than a threshold (default 30 days) on TrendTrack, extract their script, rewrite it for VeRelief Prime, and file it as a Video Brief in Notion. Use when the user asks to check competitor ads, mine long-running ads, build a swipe file, or run the weekly competitor sweep.
---

# Competitor Ad Swipe → VeRelief Prime Brief

Turn a competitor's proven long-running ads into VeRelief Prime scripts, filed in Notion.

The premise: **ad longevity is the only free performance signal we get.** A DTC brand does not
pay to run a creative for 30+ days unless it is profitable. Anything past that threshold is a
validated concept — the angle, the hook, and the structure have already survived a real auction.

## Required connectors

Check these are enabled in-chat before starting. If one is off, stop and tell the user which
one to toggle on — do not attempt to scrape a site as a workaround.

| Connector | Used for |
|---|---|
| **Trend Track MCP** | Discovery: competitor ads + how long each has run |
| **Notion** | Destination: Video Brief + Ad Creative Pipeline |
| **Higgsfield** | Fallback only — transcribing video when TrendTrack returns no transcript |
| **Shopify** | Live VeRelief Prime price / offer facts |

Direct HTTPS to `trendtrack.io` is blocked by the egress proxy in sandboxed sessions. This is
expected and is not a failure to route around — all TrendTrack access goes through the MCP
connector, which uses a different path. Never substitute scraping.

## Run the pipeline

### 1. Load the watchlist

Read `config/competitors.yml` for the brands to sweep, the `min_days_running` threshold, and
`max_new_briefs_per_run`. If the user named a specific competitor, that overrides the file.

### 2. Pull ads from TrendTrack

`list_tracked_brands` → grab the `brandtracker_id` for each watchlist brand. Everything the
watchlist names is already tracked; if the user adds a new one, `add_to_brandtracker` first.

Then per brand:

```
get_brandtracker_scaling_ads(
  brandtracker_id = <uuid>,
  min_days_running = <threshold from config>,
  status           = "active",
  media_type       = "video",
  ad_rank_sort     = "current_rank",
  limit            = 8
)
```

`min_days_running` does the 30-day filter server-side — do not filter by hand.

**Rank survivors by `metrics.duplicates`, not just `daysRunning`.** Duplicates are how many
times the brand has re-uploaded the same creative. A 272-day ad with 80 duplicates is a brand
shouting; a 392-day ad with 10 is one they forgot to switch off. Longevity × duplicates is the
real signal. `metrics.reach` and `estimatedSpend` break ties.

Two gotchas:
- `main_countries` only matches EU/UK (Meta transparency reporting). For US ads use
  `ad_countries`, or leave country unset and read `audience.targetedCountries`.
- Each call costs credits. Check `check_credits` if a sweep is large; a `limit: 8` call runs
  about 12 units.

### 3. Skip what we already swiped

`Creative ID` is a house number (`HPT085`) and carries no link to the source ad, so it cannot
be the dedupe key. The ledger lives in TrendTrack instead:

**Favorites folder `Swiped → VeRelief Briefs`** — id `8e6eb79b-c2b5-467c-bf44-dafc29eb1401`
(workspace scope, ads).

```
list_favorites(type="ads", folder="8e6eb79b-c2b5-467c-bf44-dafc29eb1401", limit=25)
```

Page through `pagination.totalPages` and collect every `ad.id`. Drop any candidate whose id is
already in that set — before spending effort on transcripts or rewriting.

Then, **immediately after filing each brief**, register it:

```
add_favorite_item(type="ads", item_id="<ad.id>",
                  folder_id="8e6eb79b-c2b5-467c-bf44-dafc29eb1401")
```

Register it even if the run is later interrupted — an unregistered brief is one you will swipe
again next week. The ledger lives beside the ads rather than in this repo or a Notion column,
so it survives across sessions and machines and the team can see it in the TrendTrack UI.

Watch for **near-duplicates**, which the id check will not catch. Brands re-upload the same
creative under new ad ids — Pulsetto had 80 copies of one ad. Two ads sharing a
`content.body`, a `collationId`, or an obviously identical transcript are the same ad. Compare
against the folder's existing entries on those fields too, not just id.

Report skips as a count, not one line each.

### 3b. Steer away from sameness

Passing the dedupe check is not enough. Six different ads that all land on the same avatar make
a library that looks varied and behaves identically. Before picking, read what is already there:

```sql
SELECT "Avatar", COUNT(*) AS n
FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
WHERE "Creative ID" LIKE 'HPT%'
GROUP BY "Avatar" ORDER BY n DESC
```

At time of writing that returns Wired Lifer 32, Multi 25, unset 24, Off-ramper 3,
Sleep Struggler 2, HRV Hunter 1. The library is heavily skewed and two avatars are barely
served.

Apply these, in order:

1. **Prefer the under-served avatar.** When two candidate ads are close on longevity and
   duplicates, take the one mapping to the thinner column. A good ad for HRV Hunter is worth
   more right now than a slightly better one for Wired Lifer.
2. **One ad per competitor per run.** Never file two Pulsetto briefs in the same sweep, however
   good both look — you are sampling one brand's strategy, not copying it.
3. **Do not repeat a recent framework.** Check `Content Type` on the last ~10 briefs and skip a
   candidate whose framework is already there.
4. **Say when the well is dry.** If everything left is a rerun of an angle already covered,
   file fewer briefs and say so. Filing to hit `max_new_briefs_per_run` is how the library
   fills with near-copies.

Report the avatar counts in step 8 so the skew stays visible.

### 4. Extract the script

Usually already done for you. `get_brandtracker_scaling_ads` returns `content.transcript` as a
JSON string of timed segments — parse it and you have the full spoken script with timings, which
also gives you the pacing. `content.body` carries the ad copy, `content.ctaDescription` the CTA
headline.

In order of preference:

1. **`content.transcript`** — parse the segments. Timings are the pacing map; use them.
2. **`get_brandtracker_transcripts`** — grouped transcripts for the brand, sorted by
   `longestRunning` or `usageCount`. Useful for sweeping a brand's whole library at once.
3. **Higgsfield** — only if both are empty. Some brands (Truvaga, at time of writing) return
   `transcript: null` on every ad; their `content.body` is long-form and often carries the whole
   argument, so read that before reaching for transcription.
4. **Say so.** If none work, file with what you have, status `Conceptualizing`, noting the script
   needs manual capture. Do not invent a script.

Capture the **visual beats** too, not just the words. A script without its visual pacing is
half a brief, and the editor cannot build from it.

### 5. Analyse the structure

Run the `brook-adblock-analyzer` skill on the extracted script. You need, at minimum:

- The **Hook / Body / CTA** split
- Which **Person Blocks** are present (Problem Statement, Failed Alternative, Desired Result,
  Before & After, Social Proof, Storytelling)
- The **primary angle** (Comparison, Transformation, Problem-Solution, Authority, …)

This analysis is what gets transferred. **We are copying the structure, never the words.**

### 6. Rewrite for VeRelief Prime

Read `references/verelief-prime-brief.md` in full before writing a single line.

Hard rules:

- Keep the competitor's **structure and angle**. Replace **every** word, claim, and story beat.
- Never reuse a competitor's sentence, tagline, or on-screen text verbatim.
- Never carry over a competitor's **claim** — their device is not ours and their substantiation
  is not ours. Re-derive each claim from the approved list in the brand brief.
- Run the compliance gate in the brand brief on the finished script. It is not optional. A
  script that fails the gate does not get filed — fix it or drop the ad. **Do not print the
  gate into the brief** — it is a check you run, not a section editors need to read. If a
  script cannot pass, raise it with the user rather than filing a watered-down brief.
- Pull live price/offer from Shopify. Never hardcode a price.

### 7. File it in Notion

**Video Brief database only.** Do not create an Ad Creative Pipeline row — the team promotes
briefs into the pipeline themselves. Follow `references/notion-map.md` exactly.

1. Get the next `Creative ID`: query the Video Brief data source for the highest existing
   `HPT<n>` and increment it, zero-padded to three digits (`HPT084` → `HPT085`). Numbers are
   sequential house IDs, unrelated to the source ad.
2. Create the page with the Hook/Body/CTA table layout the template uses.
3. Fill the strategy fields (Avatar, TEEP Stage, Self Targeting, Valence Zone) from your step-5
   analysis — these are the fields the team filters on, so an unfilled brief is an invisible one.
4. **Write four hook variants by default.** One body, one CTA, four different ways in. Hooks
   are the highest-leverage thing to test, and four is the house default — HPT079 ships four.
   Make them four genuinely different *mechanisms*, not four rewordings: e.g. reframe, cost,
   in-medias-res, direct callout. If the concept only supports fewer, say so rather than
   padding with near-copies.
5. **Start the page body with the two naming tables** — Batch name / Folder name, then File
   naming. They carry the team's file-naming convention and are the first thing the editor
   reads. `references/notion-map.md` has the exact format. Never omit them. **One file-name row
   per hook variant**, so four by default.
6. Put the TrendTrack share link in **AD INSPO** as an `<embed>`, on its own:

   ```
   ### AD INSPO
   <embed src="https://app.trendtrack.io/share/ads/<slug>"></embed>
   ```

   Call `create_ad_share_link(ad_id)` to get the URL. It renders as a card carrying days
   running, rank movement, advertiser and ad copy. No video block — the embed alone is house
   style.
7. Set the page **icon to ⚡** — the Video Brief template default. Every brief uses it. Do not
   pick a per-brief emoji, however apt: a consistent icon is how the database stays scannable.

### 8. Report

Give the user a short table: competitor, days running, angle, avatar, Creative ID, brief link.
Then:

- one line naming anything skipped and why (already swiped, near-duplicate, angle repeat)
- the current avatar spread, so the skew is visible before it becomes a problem

Nothing else.

Source details (days running, duplicates, ad ID) belong in this report, **not** in the brief.

## Guardrails

- **Cap the output.** Respect `max_new_briefs_per_run` as a ceiling, never a target. Ten
  mediocre briefs are worse than two good ones — the team has to read these.
- **Register every filed brief in the favorites ledger.** A brief that is not registered will
  be swiped again.
- **Longevity is necessary, not sufficient.** If a long-running ad's angle cannot legally or
  honestly transfer to a $399 non-prescription wellness device, drop it and say why. A retail
  gummy brand's "eat 2 before bed" angle is not our angle.
- **Do not touch existing rows.** This skill only creates. If something looks wrong in an
  existing brief, tell the user; never edit or delete their work.
- **Icon is always ⚡.** No exceptions, no thematic emoji.
- **Four hook variants, four file rows.** They must match; a fifth file row with no hook, or a
  hook with no row, means the editor delivers the wrong number of cuts.
- **Never drop the naming tables.** They are not decoration and not source attribution — they
  are how the editor names deliverables. Any brief without them is incomplete.
- **The brief is for the editor, not the strategist.** It carries AD INSPO, general instruction,
  glossary, and the Hook/Body/CTA tables — nothing else. No source attribution block, no swipe
  analysis, no compliance table. Anything the editor cannot act on is noise.
