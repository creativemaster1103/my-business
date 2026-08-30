# Hoolest — business automations

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
## Winner Crawl

Automates: **pull ad-level performance from the Hoolest Meta account → keep every video
creative clearing both the spend and ROAS floors → tag its Notion Video Brief row as a
Winner.** Promote-only; it never writes Loser and never overwrites a Performance value that is
already set. This is the loop-closer — the brief database is the team's creative memory, and it
is only useful if it knows what actually won.

### Run it

```
/winner-crawl
```

### Required connectors

- **Meta Ads** — ad-level spend and purchase ROAS
- **Notion** — destination: the Video Brief database

### Files

| Path | What |
|---|---|
| `.claude/skills/winner-crawl/SKILL.md` | The pipeline |
| `config/winner-criteria.yml` | Ad account, window, thresholds, scope, Notion destination |

### Why the VID filter is load-bearing

The HPT numbering namespace **collides across formats** — statics reuse HPT numbers that already
belong to different video concepts in Notion. `HPT034` is a static for Mini Max PEMF and the
highest-ROAS ad in the account at 3.32; the `HPT034` row in Notion is a video concept called
"Worth of investment". Matching on Creative ID without filtering to video first stamps "Winner"
on the wrong creative. The Notion `Format` property has exactly one option, `VID`, so the
database cannot even represent the static that won.

### Schedule

A Routine fires a fresh session on cron `0 16 * * 1` — **Monday 16:00 UTC**. Trigger id
`trig_011usqGZbGMcmPwYo1UaALEc`. Push and email notifications on. As of 2026-08-30 it has
never fired; its first run is 2026-08-31.

> **Blocker: no connectors are attached.** Same defect as Competitor Ad Swipe above — the
> Routine was created through the API, so it carries no MCP grant and its fired session gets
> built-in tools only. It needs **Meta Ads** and **Notion**, attached from the claude.ai
> Routines UI. Its prompt tells it to stop and name the missing connector rather than
> improvise, so a misconfigured run fails loudly instead of tagging the wrong rows.

> **Check the day-of-week.** `0 16 * * 1` is Monday 16:00 UTC, which is **Tuesday 00:00**
> Philippine time — the local day shifts *forward* one, the mirror of the correction made to
> Competitor Ad Swipe in `7c54c9e`. If the intent was Monday local, the cron should be
> `0 16 * * 0`, which collides with the swipe's slot. Confirm which day is wanted.

> **Thresholds are provisional.** `min_spend: 2000` USD and `min_roas: 1.5` are calibrated
> against what the account actually did in the 30 days to 2026-08-30, not against a stated
> target. Video ROAS in that window ran 0.71–1.68, so a floor of 2.0 would tag nothing and read
> as a broken automation. Mark to confirm the real break-even.

### What it deliberately does not do

- Never creates a Notion row — it only tags rows that already exist.
- Never writes `Loser` or `High Potential`, in any circumstance.
- Never overwrites an existing `Performance` value, even when the current best variant differs
  from the recorded one — it reports the disagreement instead.
- Never evaluates statics, creator whitelist ads, or anything without a VID token.
- Never guesses which row an ambiguous Creative ID means.
