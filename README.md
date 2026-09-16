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

Enable these in the chat's connector settings before the first run:

- **Trend Track MCP** — discovery
- **Notion** — destination
- **Higgsfield** — video transcription
- ~~Shopify~~ — **on hold**, do not connect ([see below](#-shopify-is-on-hold))

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
> Notion, Zapier, Higgsfield** before the first fire — **not Shopify**, which is on hold. Its
> prompt tells it to stop and
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

## 🚫 Shopify is on hold

**Do not query Shopify from either pipeline** — not for price, not for offers, not for product
status. Standing instruction from Mark, 2026-09-16. A hold, not a removal: lift it only when Mark
says so.

Both skills previously said *"pull live price/offer from Shopify, never hardcode a price."* The
principle stands; the method is suspended. With no live source, the way to honour it is to **keep
a price out of the script** — which is the better call anyway, since good UGC does not quote one.
If a price is genuinely required, ask Mark for the figure. Never infer a discount from an order
value, and never reuse a stale number from this repo.

The `Offer` field on a UGC brief comes from the user, or stays at the Notion template's default.

## UGC Scripting

Automates: **mine what our customers actually said → clear four strategy gates → write two
creator-shootable scripts and a ten-clip shotlist → file it in the UGC Brief Database.**

### Every brief ships 2 scripts and 10 general clips

One page, one creator, two scripts, ten clips.

The two scripts live in the `Script 1` / `Script 2` sections the team's Notion template already
carries, and must differ in framework **and** in persona+angle — two angles onto one persona is
one script with extra steps. Each gets **5 hooks** and a body, so **10 hook takes and 2 body
takes** per page.

Five genuinely different *mechanisms*, not five rewordings — a reworded hook tests nothing. The
pipeline picks five from eight (in medias res, direct callout, objection-first, reframe,
confession, demonstration-first, contrast, failed-alternative) and the two scripts may share at
most two, so the ten hooks stay varied instead of converging.

### The clips are shot alone, on an iPhone, in fifteen minutes

There is no production shoot. Every one of the ten has to survive one test:

> Could they shoot it **alone, in their kitchen, in under a minute**, without moving furniture or
> asking anyone for help?

So: one person, one iPhone. No second operator, no second phone, no tripod, no gimbal, no
lighting kit, no macro lens. Nothing to buy — only the device and things already in their home.
One take, 6–8 seconds. Nothing shot on a phone screen, because they're filming *with* the phone —
a screen means a laptop, a TV or a wall calendar.

**Every row says whether the phone is handheld or propped.** Five of the ten need both of the
creator's hands, which means the phone goes against a stack of books or a mug. Leaving that unsaid
is the single most common reason a clip comes back missing.

Each row is written as an instruction in the second person — *"prop the phone and sit how you
actually sit at 4pm"*, not *"evocative shot conveying low-grade tension"*. The test for "general"
is blunt: **if it cannot be cut into both scripts, it is not a general clip** — it is script
b-roll, and it does not count toward the ten. Each row carries a section name, because the creator
names the file `BRoll_<section>`.

### First question: specific creator, or general?

**The pipeline asks before it does anything else**, and never infers the answer. It is first
because it decides *which personas are even available*:

| | **Creator-specific** | **General** |
|---|---|---|
| Persona | Constrained — one **this creator can carry** without acting | Free — chosen on the evidence, then the casting is specified |
| Page title | `<Creator Name>-<Concept>` | `General-<Concept>` |
| `Content Creator` cell | Their name | `General — unassigned` + a one-line casting spec |
| Personal-outcome lines | Only if they have genuinely used it — **the pipeline asks** | All marked `[REQUIRES GENUINE USE]`; it cannot know |
| Clip bank | Staged in their actual space | Location-agnostic, so anyone can shoot it |

You cannot cast someone who is already cast. Get it wrong in the creator-specific direction and
you write a Lights-Out Loser script for someone who reads wired and 24 — unusable, and nobody
notices until the footage comes back. Get it wrong the other way and you ship a brief that only
works in one person's kitchen.

### The four gates

**Nothing gets written until all four are resolved, per script.**

| Gate | Set by | Reference |
|---|---|---|
| **Persona** | **The user** | The `Official Persona` toggle on Notion's `👤 Buying Persona` page — read live, never from a copy |
| **Awareness level** | **The user** | Unaware → Most-Aware |
| **Core Desire** | **The user** | One of the Life Force 8, from the toggle on the same page |
| **Ad Angle** | **The user** | Candidates derived from the persona's pain / desire / fear |

**All four are the user's to set. If one is missing, the pipeline asks — it does not choose.**
That includes the ad angle. Naming a persona answers one gate and leaves three open.

Recommending is not deciding: it arrives with two to four options, a recommendation and the
reason, then waits. What it must not do is pick one, write the script, and report the choice
afterwards — by then the user is reviewing a decision instead of making one.

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
ASK                        →  specific creator, or general? (never inferred)
      ↓  decides which personas are available
Okendo + Parker + Gorgias  →  quote bank (15-25 verbatim lines, tagged hook/objection/proof)
      ↓
ASK THE USER            →  FOUR GATES: persona · awareness · core desire · angle
      ↓  blocking — all four are theirs to set, never inferred
ugc-video-frameworks skill →  two frameworks, one per script, paired to share one clip bank
      ↓
2 scripts × 5 hooks        →  Spoken / Shot-Action / Note
10 general clips           →  one shotlist, iPhone-only, serving both
      ↓  brand compliance gate + endorsement gate
      ↓
Notion MCP                 →  duplicate ✏️ TEMPLATE, fill, file as `<Creator>-<Concept>`
```

### Run it

```
/ugc-scripting
```

It will ask whether the brief is for a specific creator or general. Answer up front to skip the
question: `/ugc-scripting for Hayden Bender`, or `/ugc-scripting general brief, Lights-Out
Loser`, or `/ugc-scripting general, from the post-purchase survey`.

### Required connectors

- **Notion** — persona source, destination, and the record of what has been scripted
- **Okendo** — product reviews
- **Parker** — semantic review search, post-purchase survey, ad comments
- ~~Shopify~~ — **on hold**, see below
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

- **Never assumes who the script is for.** Specific creator or general is asked, not inferred.
- **Never writes before the four gates are clear**, and never sets one itself. If the user did
  not give an awareness level, core desire or ad angle, it asks and waits.
- **Never files a general brief without a casting spec** — that is not general, it is unfinished.
- **Never invents a customer quote, review or statistic.** If the connectors return nothing, the
  run reports that and stops.
- Never puts a review verbatim into a creator's mouth as their own experience.
- Never files a UGC script in the Video Brief database, and never runs the `HPT` naming sheet for
  one — that database has no properties, no creative ID and its own creator-facing naming.
- Never edits the standing `Shooting Specifications` or `HOW TO UPLOAD CONTENT` callouts.
- Never edits an existing brief.

### Flagged, not decided

**Hook count — three conventions in play.** The UGC template's standing naming block says
**three** hooks, the Video Brief pipeline uses **four**, and this pipeline now writes **five**.
Five is what it follows, and the naming block gets corrected on every brief — but the template
should be updated at source so the fix is not made by hand each time.

**`Category` in the Video Brief database** has only two options, `New` and `Iteration`. There is
no `Adaptation`, despite what `competitor-ad-swipe/references/notion-map.md` instructs — verified
against the live schema 2026-09-16. That pipeline's mapping needs Mark's call on which value
competitor-derived briefs should carry. It does not affect UGC briefs, which have no properties
at all.

**Product.** The UGC template and all four existing briefs say `Hoolest Mini`, not
`VeRelief Prime`. The pipeline confirms the product before filing rather than assuming.

**`General-<Concept>` is a new title convention.** Every existing brief is creator-named, so
there is no precedent for an unassigned one. It keeps them sorting together and makes it obvious
which briefs still need a creator — but it is a proposal, not a settled convention.
