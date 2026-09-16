# Hoolest — business automations

Video briefing strategy. Two pipelines, both ending in the same Notion **Video Brief** database
and the same `HPT` numbering:

| Skill | Sources from | Output reads as |
|---|---|---|
| [`/competitor-ad-swipe`](#competitor-ad-swipe) | Competitor ads running 30+ days | AI-voiceover editor cut sheet |
| [`/ugc-scripting`](#ugc-scripting) | Our own customers' words | Creator shoot script |

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

---

## UGC Scripting

Automates: **mine what our customers actually said → pick a proven UGC framework → write a
creator-shootable script → file it in Notion.**

### Why voice of customer

The sibling pipeline mines what *competitors* proved in the auction. This one mines what *our
buyers* already wrote. A review that says "I was sceptical because I'd already wasted money on a
breathing app" is a hook, an objection and a proof beat in one sentence — pre-validated in a way
ideation never is. Copywriters invent objections; customers state them.

The 3- and 4-star reviews carry the information. Five-star reviews are congratulation.

### How it runs

```
Okendo + Parker + Gorgias  →  quote bank (15-25 verbatim lines, tagged hook/objection/proof)
      ↓  cluster by what the person was trying to do
ugc-video-frameworks skill →  pick the framework the evidence points at
      ↓
script                     →  Spoken / Shot-Action / Note, 4 hook mechanisms
      ↓  brand compliance gate + endorsement gate
Shopify                    →  live price/offer
      ↓
Notion MCP                 →  Video Brief page, Content Type `UGC`
```

### Run it

```
/ugc-scripting
```

Or scope it: `/ugc-scripting two scripts for Sleep Struggler`, `/ugc-scripting from the
post-purchase survey`.

### Required connectors

- **Notion** — destination, and the record of what has already been scripted
- **Okendo** — product reviews
- **Parker** — semantic review search, post-purchase survey, ad comments
- **Shopify** — live price/offer
- **Zapier** — writes the naming-convention sheet (the Drive connector is read-only)
- **Gorgias** — optional, but support tickets are the best source of unspoken objections

### Files

| Path | What |
|---|---|
| `.claude/skills/ugc-scripting/SKILL.md` | The pipeline |
| `.claude/skills/ugc-scripting/references/ugc-creator-brief.md` | Casting, shoot direction, **endorsement gate** |
| `.claude/skills/ugc-scripting/references/voice-of-customer.md` | Where the quotes are and how to judge one |
| `.claude/skills/ugc-scripting/references/notion-map-ugc.md` | Property deltas + live option values |
| `config/ugc-scripting.yml` | Quote-bank floor, framework lookback, shoot defaults |

It reuses the brand brief and the naming generator from `competitor-ad-swipe/references/` rather
than copying them — same product, same claim set, same file-naming sheet.

### The endorsement gate

The one thing this pipeline has that the swipe pipeline does not. A scripted creator speaking to
camera is an **endorsement**: the brand owns what they say, and "the creator improvised" is no
defence when we wrote the script. The gate covers personal-outcome claims, typicality, disclosure
placement, costume authority, and the rule that a customer review is never handed to a creator as
their own experience.

Both gates run on every script. A script that fails either is fixed or dropped — never watered
down to hit the count.

### What it deliberately does not do

- **Never invents a customer quote, review or statistic.** If the connectors return nothing, the
  run reports that and stops.
- Never puts a review verbatim into a creator's mouth as their own experience.
- Never files fewer than four hook variants, or a hook without a matching file-name row.
- Never creates an Ad Creative Pipeline row, and never edits an existing brief.

**Still open:** the Video Brief `Category` property has only two options, `New` and `Iteration` —
there is no `Adaptation`, despite what `competitor-ad-swipe/references/notion-map.md` instructs.
Verified against the live schema 2026-09-16. The UGC pipeline uses `New`; the swipe pipeline's
mapping needs Mark's call on which value competitor-derived briefs should carry.
