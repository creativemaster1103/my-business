# Hoolest — business automations

## Winner Crawl

Automates: **crawl the ad account at ad level → keep video creatives over the bar → tag the
matching Video Brief row in Notion as a Winner.**

### The bar

A creative is a winner when, **at ad level** (one hook variant, not the campaign), over a
rolling **14 days** it clears **both** $1,000 USD spend **and** 1.8 purchase ROAS. Ad level is
the point: a campaign averaging 1.9 tells you nothing about which of its four hooks earned it.

The window is deliberately tight — a creative has to be earning *now*, not coasting on spend
from three weeks ago. The trade-off is that far fewer ads reach $1,000 in 14 days, so expect
lean weeks and read the near-miss list, which is where spend-short/ROAS-strong creatives now
collect. Both the window and the floors live in `config/winner-criteria.yml`; if the crawl
starts returning nothing week after week, lower `min_spend_usd` rather than widening the
window — the shorter window is the point.

### Scope: video only

**An ad name carrying a `VID` token is a video, and video is the whole scope.** Anything
without one is not evaluated — statics (`IMG`), creator/whitelist ads
(`WillBurger_VeReliefPrime_…`, which are videos but follow no naming convention), and legacy
one-offs (`Prime _ PDP_BOFU _ …`). The report gives a count of what was skipped so nothing is
hidden, but does not itemise it.

### How it runs

```
Meta Ads MCP     →  ad-level spend + purchase_roas, last 14d
      ↓  keep VID only — everything else is out of scope
      ↓  keep spend >= $1,000 AND roas >= 1.8
parse ad name    →  Creative ID / Format / Concept / Variant
      ↓  concept-name cross-check
Notion MCP       →  Video Brief row: Performance = Winner, Winning version = <variant>
```

### Run it

```
/winner-crawl
```

Or scope it: `/winner-crawl last 90 days`, `/winner-crawl dry run`.

### The VID filter is also what keeps writes correct

Statics run their own HPT sequence that **reuses numbers already spent on videos**, for
different concepts:

| HPT | Notion Video Brief (VID) | Meta static ad (IMG) |
|---|---|---|
| HPT033 | Stuck on Fight or Flight – AI UGC | PEMF Statics *(Mini Max PEMF)* |
| HPT034 | Worth of investment | Hero Product *(Mini Max PEMF)* |
| HPT038 | Gel Tip Vs Gel Paste 3 | US vs THEM |
| HPT039 | Gel Tip Vs Gel Paste 4 | B2G1 Bundles |
| HPT045 | Ronak UGC | Back to School Sale |

Matching on the number alone tags *"HPT034 – Worth of investment"*, a VeRelief Prime video, as
a winner off a **Mini Max PEMF static's** ROAS — a write that succeeds, looks plausible and is
wrong. Filtering to `VID` first removes the whole class of error. After that, the crawl still
cross-checks the concept name, which is what disambiguates the two Creative IDs owning two
Notion rows each (HPT022, HPT031); when it cannot, it reports instead of writing.

### Meta API quirks this works around

- **`filtering` is silently ignored** on this account. An `amount_spent >= 1000` filter still
  returns $638 rows, and `purchase_roas` is rejected outright as unfilterable at ad level.
- **`sort` is reliable.** So the crawl sorts by spend descending, pages, and applies both
  thresholds itself, stopping once rows drop below the spend floor.
- **`date_preset: maximum` breaks sorting and filtering both** and returns arbitrary order.
  Use `last_90d` when a wide window is wanted, never `maximum`.
- `spend` is an alias for `amount_spent` and **is** window-scoped. Values arrive as display
  strings (`"$2,231.65 USD"`); strip currency and commas before comparing. `purchase_roas` can
  be `null` — treat null as 0, never as a pass.

### Safety rules

- **Video only.** No `VID` token, no consideration.
- **Promote only.** Never writes `Loser`, never overwrites a `Performance` value a human set.
- Never creates a Video Brief row; it only updates existing ones.
- Never writes to a row whose concept name does not corroborate the Creative ID.
- Never touches any ad account other than the one in config.

### Files

| Path | What |
|---|---|
| `.claude/skills/winner-crawl/SKILL.md` | The pipeline |
| `config/winner-criteria.yml` | Thresholds, window, scope, account id, Notion destination |

### Schedule

A Routine fires a fresh session every **Monday 09:00 Philippine time** — nine hours after the
competitor sweep, so the week's briefs and the week's winners land together. Trigger id
`trig_011usqGZbGMcmPwYo1UaALEc`. Push and email notifications on.

The cron is `0 1 * * 1` — **Monday** 01:00 UTC. Philippine time is UTC+8, so 09:00 local is
01:00 UTC the same day; unlike the competitor sweep, no day-of-week shift is needed here.

> **Connectors must be attached from the claude.ai Routines UI.** Same limitation as the
> competitor sweep — this organization rejects the API's `connectors` parameter outright, so
> the Routine as created runs *without* MCP tools and will stop at step 1. Open it in the
> Routines UI and attach **Meta Ads** and **Notion** before the first fire. Its prompt tells it
> to stop and name the missing connector rather than improvise.

## Competitor Ad Swipe

Automates: **find competitor ads running 30+ days → extract the script → rewrite for
VeRelief Prime → file it in Notion.**

### Why longevity

A DTC brand does not keep paying to run a creative for 30 days unless it is profitable. Ad
longevity is the only free performance signal available on a competitor, so "still running
after 30 days" is the filter that separates validated concepts from everything they tested and
killed. The pipeline mines that signal and nothing else.

### How it runs

The whole chain runs through MCP connectors, so it lives as a **Claude Code skill** rather than
a script on a cron box. There is no scraping and no stored competitor login.

```
TrendTrack MCP        →  competitor ads + days-running
      ↓  filter ≥ 30 days, drop already-swiped
Higgsfield MCP        →  transcribe the ad video when no text script exists
      ↓
brook-adblock-analyzer →  Hook/Body/CTA blocks + primary angle
      ↓
VeRelief Prime brief  →  rewrite structure, replace every word + claim, compliance gate
      ↓
Notion MCP            →  Video Brief page + Ad Creative Pipeline row, related
```

### Run it

```
/competitor-ad-swipe
```

Or scope it: `/competitor-ad-swipe Pulsetto only, last 60 days`.

### Required connectors

Enable all four in the chat's connector settings before the first run:

- **Trend Track MCP** — discovery
- **Notion** — destination
- **Higgsfield** — video transcription
- **Shopify** — live price/offer

Direct HTTPS to `trendtrack.io` is blocked by the sandbox egress proxy. That is expected: the
MCP connector reaches TrendTrack over a different path. Do not work around it by scraping.

### Files

| Path | What |
|---|---|
| `.claude/skills/competitor-ad-swipe/SKILL.md` | The pipeline |
| `.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md` | Voice, avatars, approved claims, compliance gate |
| `.claude/skills/competitor-ad-swipe/references/notion-map.md` | Notion IDs + property mapping |
| `config/competitors.yml` | Watchlist, thresholds, excluded angles |

### Schedule

A Routine fires a fresh session every **Monday 00:00 Philippine time** and runs the sweep end
to end. Trigger id `trig_01Awavxwivudwt9MurxicY7y`. Push and email notifications on.

The cron is `0 16 * * 0` — **Sunday** 16:00 UTC. Philippine time is UTC+8 with no daylight
saving, so midnight Monday local falls on Sunday afternoon UTC and the day-of-week shifts back
a day. Editing the hour without also moving the day would silently schedule it a day late.

> **Connectors must be attached from the claude.ai Routines UI.** This organization does not
> allow the API to grant connectors to a trigger, so the Routine as created runs *without*
> MCP tools and will stop at step 1. Open it in the Routines UI and attach **Trend Track MCP,
> Notion, Zapier, Shopify, Higgsfield** before the first fire. Its prompt tells it to stop and
> name the missing connector rather than improvise, so a misconfigured run fails loudly instead
> of filing something wrong.

Watchlist confirmed 2026-08-29 (all six competitors).

**Still open:** the regulatory posture of VeRelief Prime. The claim set in the brand brief is
written conservatively on purpose; whether the device is positioned as a general wellness
device or carries an FDA clearance (and for what indication) decides how far those claims can
stretch. Until that is confirmed, the conservative set stands.

### What it deliberately does not do

- Never edits or deletes an existing Notion row — it only creates.
- Never reuses a competitor's words, claims, or proof; only their structure and angle.
- Never files a script that fails the compliance gate.
- Never exceeds `max_new_briefs_per_run`.
