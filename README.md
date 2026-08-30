# Hoolest — business automations

## Routines and connectors — read this first

All three automations here run as Routines, and **a Routine's connectors can only be attached from
the claude.ai Routines UI.** This is an org-level policy, not a gap in how the Routines were
set up.

Verified 2026-08-30, not assumed. `create_trigger` does expose a `connectors` parameter; calling
it with the five the swipe needs fails outright:

```
create_trigger: the connectors parameter is not available for this organization.
Omit the connectors parameter.
```

`update_trigger` has no `connectors` parameter at all, so an existing Routine cannot be granted
them either. There is no API path. Deleting and recreating a Routine does not help — the
recreate hits the same policy.

**Consequence:** a Routine created through the API fires a session holding built-in tools only
(`Bash`, `Read`, `Edit`, `Skill`, `WebFetch` …) and no MCP connectors. All three prompts here
are written to stop and name the missing connector rather than improvise, so a misconfigured
run fails loudly instead of filing something wrong — but it still does no work.

This is exactly what happened on **2026-08-30 16:10 UTC**: the swipe Routine fired on schedule,
ran 48 seconds, exited at its step-1 connector gate, and recorded `SUCCEEDED`. The run status
means "reported the blocker correctly", not "did the job".

**The fix, per Routine:** open it in the claude.ai Routines UI and attach its connectors.

| Routine | Connectors to attach |
|---|---|
| Weekly competitor ad swipe | Trend Track MCP, Notion, Zapier, Shopify, Higgsfield |
| Weekly winner crawl | Meta Ads, Notion |
| Daily inspo harvest | Trend Track MCP |

Until that is done, any of the pipelines can still be run by hand in a chat session that has
the connectors enabled — `/inspo-harvest`, `/competitor-ad-swipe` or `/winner-crawl`. That is a
stopgap, not a fix: it needs a human to start it.

## Inspo Harvest

Automates: **sweep the competitor watchlist daily for video ads still actively running past 30
days → vet them → file the keepers in the TrendTrack Inspo Bank.**

This is the front half of the creative pipeline, split out so it can run on its own cadence:

```
/inspo-harvest        (daily)    competitors → vet → Inspo Bank
/competitor-ad-swipe  (weekly)   Inspo Bank  → rewrite → Notion brief
```

The harvest **only ever adds** to the bank. It never briefs, never touches Notion, and never
removes anything — draining the bank is the swipe's job. The two cannot collide.

### Why split it out, and why daily is not expensive

The bank has to run about four weeks ahead of a five-a-week briefing target. Topping it up only
on swipe day means a quiet fortnight from the competitors starves the pipeline with no warning —
and the warning is the valuable part.

A daily sweep of nine brands would burn the TrendTrack quota for nothing, so the harvest is
**demand-driven rather than schedule-driven**: it reads the bank first and exits almost free if
the bank is at target. Most days are a no-op by design. A run that does nothing because the bank
is full is a *successful* run, and both the skill and the Routine prompt say so explicitly — a
string of quiet days should not read as a broken automation.

Cost is bounded three ways: the `credit_reserve` floor (step 0), the early exit on a full bank
(step 2), and stopping the brand sweep the moment the deficit is filled (step 4). The monthly
quota is 10,000 units and the billing period rolls over on the 3rd.

### Run it

```
/inspo-harvest
```

### Required connectors

- **Trend Track MCP** — the only one. Discovery, dedupe, and the favorites write all go through it.

### Files

| Path | What |
|---|---|
| `.claude/skills/inspo-harvest/SKILL.md` | The pipeline |
| `config/competitors.yml` | Watchlist and thresholds (shared with the swipe), plus the `harvest:` block |

### Schedule

A Routine fires a fresh session **every day at 01:00 UTC — 09:00 Philippine time**. Trigger id
`trig_01LUEXWWkXhojHkeZUWtd4ho`. Push and email notifications on. First run 2026-08-31.

The cron is `0 1 * * *`. Because it is daily, day-of-week is `*` and **the timezone day-shift
trap that bit both weekly Routines does not apply here** — there is no day field to get wrong.
The hour avoids the 16:00 UTC slot both weekly Routines share, and on swipe day the harvest lands
15 hours ahead of the swipe, so the bank is topped up before it is drained.

> **Blocker: no connectors attached.** Needs **Trend Track MCP** attached from the claude.ai
> Routines UI — see *Routines and connectors* above. Re-verified 2026-08-30: `create_trigger`
> still rejects the `connectors` parameter for this org outright, so there is no API path.
> Until it is attached, every fire stops at the connector gate having banked nothing.

### The bank was audited on 2026-08-30, and it has two problems

Read live from TrendTrack while building this. Both are pre-existing, neither is caused by the
harvest, and the harvest is written not to repeat them:

**1. The bank is at 5 of 20, and every entry fails the filter it was supposedly built with.**
All five are `status: "inactive"`, and three ran for 22, 5 and 23 days — well under the 30-day
threshold that is the entire premise. Whatever populated it did not apply the longevity or
active filter. The harvest pins `status: "active"` and `min_days_running` server-side and treats
both as non-negotiable, so it will not add more like these. **It also will not clean these out** —
the skill only ever adds. Removing them is a human call, and worth making: they are the queue the
weekly swipe draws from first.

**2. Three of the five entries are the same creative.** The three Pulsetto ads carry
byte-identical `content.body` under different ad ids — the brand re-uploading, which they do
constantly (80 copies of one ad at peak). So the real bank depth is about 3 distinct creatives,
not 5. Deduping on `ad.id` alone does not catch this, so the harvest also compares normalized
`content.body` and `collationId` against everything already banked or swiped, and against
everything picked in the same run.

### What it deliberately does not do

- Never writes to Notion or files a brief — that is `/competitor-ad-swipe`.
- Never removes anything from any folder, including the stale entries above.
- Never relaxes `status: "active"` or `min_days_running` to hit a number. Recently-ended ads are
  an escalation rung in the weekly swipe, reached deliberately, not a shortcut the daily top-up
  takes on its own.
- Never writes into `★ Mark's Picks` — that subfolder means "a human chose this", and an
  automation writing into it destroys the priority signal the swipe depends on.
- Never makes a favorites folder organization-visible and never creates a folder share link.
  A folder share link is a public URL with no API to revoke it — a one-way door.
- Never pads a short sweep. A bank below target is reported as what it is: the competitors are
  not producing enough keepers.

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

> **Blocker: no connectors attached.** Needs **Trend Track MCP, Notion, Zapier, Shopify,
> Higgsfield** attached from the claude.ai Routines UI — see *Routines and connectors* above.
> Until then every fire stops at step 1, as the 2026-08-30 run did.

Watchlist confirmed 2026-08-29. **Corrected 2026-08-30:** ZenoWell, Vagustim Health and
MindSpire — the three brands added on 2026-08-29 specifically to support the five-a-week floor —
were indented under `excluded_angles:` rather than `competitors:`, so YAML parsed them as
excluded-angle entries and the sweep never saw them. The watchlist read six brands, not nine,
and `excluded_angles` carried three objects where it should hold four strings. Both keys now
parse correctly.

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

> **Blocker: no connectors attached.** Needs **Meta Ads** and **Notion** attached from the
> claude.ai Routines UI — see *Routines and connectors* above. Until then every fire stops at
> step 1 rather than tagging anything.

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
