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

---

## Video Brief Scriptwriting

Automates: **find the gap in the creative library → gather customer evidence → originate a
concept → write the script → file it as a Video Brief in Notion.**

The sibling of Competitor Ad Swipe, working from the other end. That pipeline mines ads someone
else already proved; this one writes concepts nobody's ad suggested.

### Why evidence

A swiped ad arrives pre-validated — 30 days of someone else's spend says the angle works.
Originating has no such borrowed signal, which makes it the easier of the two to do badly: a
guess and a good concept look identical on the page. So evidence takes longevity's place. Every
concept has to rest on at least two independent sources, one of which is a real customer in their
own words — a review, a survey answer, an ad comment.

What that buys is freedom from the category. Every vagus-nerve competitor runs the same three
angles at the same avatar, so a swipe can only deepen the library's existing skew. Of 92 briefs,
`Wired Lifer` has 34 and `HRV Hunter` has 1. Originating is the only way to write for the
avatars and funnel stages that are starving.

### How it runs

```
Notion (library state)  →  where the gaps are: avatar, TEEP stage, concept
      ↓
Parker MCP              →  reviews, post-purchase survey, ad comments, swipe file
Motion MCP              →  what already works on our own account (SPEND call first)
      ↓  two evidence items per concept, one in a customer's own words
ugc-video-frameworks    →  pick the structure a swipe would have inherited
brook-adblock-analyzer  →  choose the Hook/Body/CTA and Person/Product blocks
      ↓
Shopify                 →  live price + offer
      ↓  write 4 hooks + body + CTA, then the compliance gate
      ↓  set the four gates: desire . awareness . angle . persona
      ↓  4 hooks, all at the brief's awareness level
Notion                  →  Video Brief page, names built from its own properties
```

### Run it

```
/video-brief-scriptwriting
```

Or scope it: `/video-brief-scriptwriting two for HRV Hunter, purchase stage`.

### Required connectors

- **Parker** — evidence (required)
- **Notion** — destination (required)
- **Shopify** — live price and offer (required)
- **Motion Creative Analytics** — our own performance data (strongly preferred)

### Files

| Path | What |
|---|---|
| `.claude/skills/video-brief-scriptwriting/SKILL.md` | The pipeline |
| `.claude/skills/video-brief-scriptwriting/references/modular-framework.md` | **The four gates, the Hook/Body/CTA spine, the blocks, awareness → structure** |
| `.claude/skills/video-brief-scriptwriting/references/concept-sources.md` | Where evidence comes from and how to search it |
| `.claude/skills/video-brief-scriptwriting/references/origination-rules.md` | Avatar, angle, framework, blocks, four hooks, dedupe |
| `.claude/skills/video-brief-scriptwriting/references/notion-deltas.md` | What an originated brief files differently, plus live property options |
| `config/scriptwriting.yml` | Volume, evidence rules, diversity guards, property defaults |

Brand voice, the approved claim set, the compliance gate, the Notion page layout and the naming
procedure are **not duplicated** — one product means one claim set, so this skill reads
`verelief-prime-brief.md`, `notion-map.md` and `naming-convention.md` from
`.claude/skills/competitor-ad-swipe/references/`. Change them in one place.

`modular-framework.md` runs the other way: it lives with this skill but governs both, because a
swiped structure and an originated concept are assembled identically once the raw idea exists.

### No schedule

Deliberately on-demand. The competitor sweep carries the weekly volume on a Routine; originating
is slower per concept because each one has to be argued from evidence rather than inherited, and
running it on a timer would produce briefs to meet a number. Run it when the library has a gap
worth filling.

### What it deliberately does not do

- Never invents a customer quote, statistic, or testimonial — not even as a placeholder.
- Never files a concept with less evidence than `config/scriptwriting.yml` requires.
- Never fills the empty AD INSPO slot with a competitor's ad. That is a swipe filed as an
  original; use `/competitor-ad-swipe` instead.
- Never edits or deletes an existing Notion row — it only creates.
- Never files a script that fails the compliance gate.

### Naming convention — changed 2026-09-14

File names are now built **from each brief's own Notion properties**. Mark's Naming Convention
Generator spreadsheet is retired and must not be used; it emits a different, now-wrong format.
Spec: `.claude/skills/competitor-ad-swipe/references/naming-convention.md`.

```
HPT089_VID_Twenty Two Years Running Hot_1B_VeRelief Prime_AI VO_Wired Lifer_NA_New_Mark_JM_Stress to Control_091426
```

The variant token is **hook number + awareness letter** — `A` Unaware · `B` Problem Aware ·
`C` Solution Aware · `D` Product Aware · `E` Most Aware. All four hooks on a brief share the
letter, because a brief sits at one awareness level.

Two consequences worth knowing:

- **`Self Targeting`, `TEEP Stage` and `Valence Zone` are no longer in file names.** The old
  token `1Aa-Z3` packed all three; `1B` does not. Keep setting them — they are useful for
  filtering — but they no longer travel with the asset. `Landing Page` now does.
- **Briefs written before 2026-09-14 use the old scheme**, where that letter meant Self
  Targeting. `HPT089_..._1Aa-Z1_...` and `HPT090_..._1B_...` mean different things in the same
  folder. Old names are not wrong, they are a different scheme — do not "fix" them.

Making awareness load-bearing on the filename is the point: you can read a file's awareness level
off its name and check whether the hook actually matches it.

### Three things to settle

**`Category: Adaptation` does not exist.** The Video Brief `Category` property has exactly two
options, `New` and `Iteration`, and no row in the database carries `Adaptation` — but
`competitor-ad-swipe/references/notion-map.md` instructs that every swiped brief be filed as
`Adaptation`. Whether a competitor-derived brief should be `New` or `Iteration` is a call for
Mark, so this skill does not change it. Originated briefs are `New`.

**`Lights-Out Loser` has nowhere to go in Notion.** The approved persona doc calls the sleep
persona *Lights-Out Loser*; the `Avatar` property still offers `Sleep Struggler`. Same person.
Until the database options are updated, set `Sleep Struggler` — and note the property spells the
other one `Off-Ramper`, capital R, where the persona doc does not.
