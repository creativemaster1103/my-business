# Hoolest — business automations

Video briefing strategy. Two pipelines, two Notion destinations:

| Skill | Sources from | Files into | Output reads as |
|---|---|---|---|
| [`/competitor-ad-swipe`](#competitor-ad-swipe) | Competitor ads running 30+ days | **Video Brief** database | AI-voiceover editor cut sheet |
| [`/ugc-scripting`](#ugc-scripting) | Our own customers' words | **UGC Brief Database** | Creator shoot brief |

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

Automates: **mine what our customers actually said → clear four strategy gates → write two
creator-shootable scripts and a ten-clip shotlist → file it in the UGC Brief Database.**

### Every brief ships 2 scripts and 10 general clips

One page, one creator, two scripts, ten clips.

The two scripts live in the `Script 1` / `Script 2` sections the team's Notion template already
carries, and must differ in framework **and** in persona+angle — two angles onto one persona is
one script with extra steps. Each gets **3 hooks** and a body, matching the template's own naming
block (`film the 3 hooks separately to the body`).

The ten clips go in the `B-ROLLS | SHOTLIST` table, one per row, and are captured once for both
edits. The test for "general" is blunt: **if it cannot be cut into both scripts, it is not a
general clip** — it is script b-roll, and it does not count toward the ten. Each row carries a
section name, because the creator names the file `BRoll_<section>`.

### The four gates

**Nothing gets written until all four are resolved, per script.**

| Gate | Source |
|---|---|
| **Persona** | The `Official Persona` toggle on Notion's `👤 Buying Persona` page — read live, never from a copy |
| **Awareness level** | Unaware → Most-Aware, read off the persona's buying behaviour |
| **Core Desire** | One of the Life Force 8, from the toggle on the same page |
| **Ad Angle** | *Optional to be given* — derived from the persona's pain / desire / fear, and stated |

They are a gate, not a worksheet. A script started before they are settled is written to nobody
in particular, and it reads that way.

The persona page carries eight personas and a second toggle naming four of them as the approved
set for locked creative — Wired Lifer, Lights-Out Loser, HRV Hunter, Off-Ramper. Those four are
the default; the other four need Mark's go-ahead. **The Off-Ramper carries a standing compliance
hold**: body-state language only, Nick's sign-off, and no anti-medication framing in paid — the
persona is drawn to exactly the framing that carries the risk.

### Why voice of customer

The sibling pipeline mines what *competitors* proved in the auction. This one mines what *our
buyers* already wrote. A review that says "I was sceptical because I'd already wasted money on a
breathing app" is a hook, an objection and a proof beat in one sentence. Copywriters invent
objections; customers state them.

The 3- and 4-star reviews carry the information. Five-star reviews are congratulation.

### How it runs

```
Okendo + Parker + Gorgias  →  quote bank (15-25 verbatim lines, tagged hook/objection/proof)
      ↓
Official Persona (Notion)  →  FOUR GATES: persona · awareness · core desire · angle
      ↓  blocking — nothing is written until these are stated
ugc-video-frameworks skill →  two frameworks, one per script, paired to share one clip bank
      ↓
2 scripts × 3 hooks        →  Spoken / Shot-Action / Note
10 general clips           →  one shotlist serving both
      ↓  brand compliance gate + endorsement gate
Shopify                    →  live price/offer for the header table
      ↓
Notion MCP                 →  duplicate ✏️ TEMPLATE, fill, file as `<Creator>-<Concept>`
```

### Run it

```
/ugc-scripting
```

Or scope it: `/ugc-scripting for Hayden Bender, Lights-Out Loser`,
`/ugc-scripting from the post-purchase survey`.

### Required connectors

- **Notion** — persona source, destination, and the record of what has been scripted
- **Okendo** — product reviews
- **Parker** — semantic review search, post-purchase survey, ad comments
- **Shopify** — live price/offer
- **Gorgias** — optional, but support tickets are the best source of unspoken objections

### Files

| Path | What |
|---|---|
| `.claude/skills/ugc-scripting/SKILL.md` | The pipeline |
| `references/four-gates.md` | Persona, awareness, core desire, angle — and how to derive an angle |
| `references/voice-of-customer.md` | Where the quotes are and how to judge one |
| `references/general-clips.md` | The standing ten, their section names, capture notes |
| `references/ugc-creator-brief.md` | Casting, delivery, **endorsement gate** |
| `references/notion-map-ugc.md` | The destination page, the template, and what does *not* apply |
| `config/ugc-scripting.yml` | Gates, quote-bank floor, the ten clips, shoot defaults |

It reuses the brand brief from `competitor-ad-swipe/references/` rather than copying it — same
product, same approved claim set.

### The endorsement gate

The one thing this pipeline has that the swipe pipeline does not. A scripted creator speaking to
camera is an **endorsement**: the brand owns what they say, and "the creator improvised" is no
defence when we wrote the script. The gate covers personal-outcome claims, typicality, disclosure
placement, costume authority, and the rule that a customer review is never handed to a creator as
their own experience.

Both compliance gates run on every script. One that fails either is fixed or dropped — never
watered down to hit the count.

### What it deliberately does not do

- **Never writes before the four gates are clear.** No persona, awareness level and core desire,
  no script.
- **Never invents a customer quote, review or statistic.** If the connectors return nothing, the
  run reports that and stops.
- Never puts a review verbatim into a creator's mouth as their own experience.
- Never files a UGC script in the Video Brief database, and never runs the `HPT` naming sheet for
  one — that database has no properties, no creative ID and its own creator-facing naming.
- Never edits the standing `Shooting Specifications` or `HOW TO UPLOAD CONTENT` callouts.
- Never edits an existing brief.

### Two things flagged, not decided

**Hook count.** The Video Brief pipeline standardises on **four** hook variants per concept; the
UGC template's naming block asks for **three**. The UGC pipeline follows its own template. Both
are defensible — they just should not drift apart by accident.

**`Category` in the Video Brief database** has only two options, `New` and `Iteration`. There is
no `Adaptation`, despite what `competitor-ad-swipe/references/notion-map.md` instructs — verified
against the live schema 2026-09-16. That pipeline's mapping needs Mark's call on which value
competitor-derived briefs should carry. It does not affect UGC briefs, which have no properties
at all.

**Product.** The UGC template and all four existing briefs say `Hoolest Mini`, not
`VeRelief Prime`. The pipeline confirms the product before filing rather than assuming.
