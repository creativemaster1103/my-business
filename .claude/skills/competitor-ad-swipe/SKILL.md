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

### 3. Skip what we already have

`Creative ID` is a sequential house number (`HPT085`), not the source ad ID, so it cannot be
the dedupe key. Instead, query the Video Brief data source and compare the **source ad** against
what is already filed — check `Concept Name` and the AD INSPO media URL on recent rows.

Never create a second brief for an ad already in the database. Report skips as a count, not
one line each.

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
4. **Upload** the competitor creative into AD INSPO — do not hotlink it. Pass the ad's
   `media.mediaUrl` to Notion `create-attachment` as `source_url`; Notion downloads it
   server-side, so this works even though the sandbox cannot reach `medias.trendtrack.io`
   itself. Then embed the returned upload id:

   ```
   ### AD INSPO
   <video src="file-upload://<file_upload_id>"></video>
   ```

   A hotlink to the TrendTrack CDN may not render and will rot when the URL expires; an
   uploaded file plays inline and outlives the source. Name the file
   `<CreativeID>-ad-inspo-<competitor>-<days>d.mp4`.
5. Set the page **icon to ⚡** — the Video Brief template default. Every brief uses it. Do not
   pick a per-brief emoji, however apt: a consistent icon is how the database stays scannable.

### 8. Report

Give the user a short table: competitor, days running, angle, Creative ID, brief link. Then one
line naming anything you skipped and why. Nothing else.

Source details (days running, duplicates, ad ID) belong in this report, **not** in the brief.

## Guardrails

- **Cap the output.** Respect `max_new_briefs_per_run`. Ten mediocre briefs are worse than two
  good ones — the team has to read these.
- **Longevity is necessary, not sufficient.** If a long-running ad's angle cannot legally or
  honestly transfer to a $399 non-prescription wellness device, drop it and say why. A retail
  gummy brand's "eat 2 before bed" angle is not our angle.
- **Do not touch existing rows.** This skill only creates. If something looks wrong in an
  existing brief, tell the user; never edit or delete their work.
- **Icon is always ⚡.** No exceptions, no thematic emoji.
- **The brief is for the editor, not the strategist.** It carries AD INSPO, general instruction,
  glossary, and the Hook/Body/CTA tables — nothing else. No source attribution block, no swipe
  analysis, no compliance table. Anything the editor cannot act on is noise.
