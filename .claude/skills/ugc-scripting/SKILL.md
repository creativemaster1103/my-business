---
name: ugc-scripting
description: Write creator-ready UGC video scripts for Hoolest — two scripts plus a ten-clip B-roll shotlist per brief, for a named content creator or as a general unassigned brief, sourced from customer language and gated on persona, awareness level, core desire and ad angle — and file them in the Notion UGC Brief Database. Use when the user asks for a UGC script, a creator script, a script for a specific creator, a talking-head ad, a testimonial ad, to script a creator shoot, or to run the UGC batch.
---

# UGC Scripting → UGC Brief Database

Write scripts a **creator can shoot on a phone**, from **our own customers' words**, and file them
in the Notion **UGC Brief Database** off the team's own template.

> ## Every brief ships 2 scripts and 10 general clips
>
> **2 scripts**, genuinely different — different framework, different persona+angle pairing. Both
> live on **one** brief page, in the `Script 1` and `Script 2` sections the template already
> carries. Each gets **3 hooks** and a main body.
>
> **10 general clips**, one per `B-ROLLS | SHOTLIST` row, captured once and cuttable into
> **either** script. Spec in `references/general-clips.md`.
>
> One page, one creator, two scripts, ten clips. Two scripts without the clip bank is an
> incomplete brief, and so is a clip bank shot for only one of them.

## First, ask who the script is for

**Before anything else — before the gates, before the research — ask:**

> **Is this for a specific content creator, or a general script?**

Do not infer it, and do not default to one. If the user named a creator, confirm that reading
back rather than assuming; if they named none, ask rather than quietly writing a general brief.

It is the first question because it **changes who the persona can be**:

| | **Creator-specific** | **General** |
|---|---|---|
| Persona | Pick one **this creator can credibly carry**. You cannot cast — they are who they are | Pick freely on the evidence, then **specify the casting** |
| Page title | `<Creator Name>-<Concept>` | `General-<Concept>` |
| `Content Creator` row | Their name | `General — unassigned` + the casting spec |
| Personal-outcome lines | Write them only if they have genuinely used it — **ask** | Always mark `[REQUIRES GENUINE USE]`; you cannot know |
| Clip bank | Staged in their actual space | **Location-agnostic** — whoever shoots it must be able to |
| Wardrobe / location | What they own, where they live | Described generically, never specified |

Get it wrong in the creator-specific direction and you write a Lights-Out Loser script for
someone who reads 24 and wired — unusable, and nobody notices until the footage comes back. Get
it wrong in the general direction and you ship a brief that only works in one person's kitchen.

## Nothing gets written until the four gates are clear

**Persona · Awareness Level · Core Desire · Ad Angle.** Resolved explicitly, per script, before
the first line. Full procedure in `references/four-gates.md`; the persona source is the
`Official Persona` toggle on Notion's `👤 Buying Persona` page, read live each run.

Ad Angle is the only one you may **propose** — derive it from the persona's pain, desire and fear
and say which you picked and why. The other three are settled before writing, not discovered
during it.

Do not confuse these with the **two compliance gates** (brand + endorsement) in step 8. The four
gates decide *what to write*. The compliance gates decide *whether it can ship*.

## What this is not

This is the sibling of `/competitor-ad-swipe`, and the two differ in almost every particular:

| | `/competitor-ad-swipe` | `/ugc-scripting` |
|---|---|---|
| Source | Competitor ads running 30d+ | Customer reviews, surveys, support tickets, ad comments |
| Destination | **Video Brief** database | **UGC Brief Database** page |
| Output | Editor cut sheet | **Creator shoot brief** — spoken lines + shotlist |
| Per brief | 1 concept, 4 hooks | **2 scripts, 3 hooks each, 10 clips** |
| Creative ID | `HPT<nnn>` | **none** — no properties in this database |
| File naming | Google Sheets generator | **`Talkinghead_S1_hook1` / `BRoll_<section>`** |
| Page icon | ⚡ | **✏️** |

Do not file a UGC script in the Video Brief database, and do not run the Zapier naming-sheet
procedure for one.

## Required connectors

| Connector | Used for |
|---|---|
| **Notion** | Persona source, destination, and the record of what has already been scripted |
| **Okendo** | Voice of customer — product reviews, review questions |
| **Parker** | Voice of customer at depth — semantic review search, post-purchase survey, ad comments |
| **Shopify** | Live price / offer facts for the header table |
| **Gorgias** | Optional — support tickets are the best source of unspoken objections |

If one is off, stop and name it. Do not substitute invented customer quotes for a connector you
could not reach — a fabricated review is the one failure this pipeline cannot recover from.

## Run the pipeline

### 1. Establish the brief mode

Ask the question above and get an answer before doing anything else.

**Creator-specific** → get the creator's name, and ask two things the brief depends on:

1. **Have they genuinely used the product?** This decides whether a first-person outcome line is
   allowed at all — see the endorsement gate. Do not guess, and do not assume gifted means used.
2. **What is their actual setup?** Where they film, what their space looks like, their register.
   The clip bank gets staged there, so it matters.

If the creator is one of the existing briefs' creators — Hayden Bender, Lauren DeCicco, Clayton
Stakelbeck, Kenzie Williams — check whether they already have a page before creating a second one.

**General** → nothing more is needed to start, but the brief carries an extra obligation: it must
say **who to cast**, because nobody else will. That goes in the `Content Creator` cell.

Record the mode. Every later step branches on it.

### 2. Load the config

Read `config/ugc-scripting.yml` for `scripts_per_brief` (2), `hooks_per_script` (3),
`general_clips_per_brief` (10), `framework_lookback` and the shoot defaults. A user instruction
overrides the file.

### 3. Mine the voice of customer

Read `references/voice-of-customer.md` — it carries the search terms that actually surface
material, and the test for whether a quote is usable or merely nice.

**Do this before the gates and before the framework.** Picking either first makes you go looking
for quotes that fit, which is how you end up with a script that sounds like an ad wearing a
customer's voice.

Pull in this order and keep the raw language:

1. **`reviews_search` / `reviews_aggregate` (Okendo)** — read the 3- and 4-star reviews first.
   Five-star reviews say "love it" and carry no information; the middling ones say *what they
   expected, what they got, and what nearly stopped them buying*.
2. **`search_customer_reviews_semantic` (Parker)** — query emotional states, not the product.
3. **`semantic_search_post_purchase_survey`** — the only source that says *what they were doing
   the moment they decided to buy*. Gold for hooks.
4. **`search_facebook_ad_comments_semantic`** — the objections people voice in public.
5. **Gorgias tickets**, if enabled — the objections people only voice in private.

Collect **verbatim** lines into a quote bank, each tagged hook / objection / proof, before writing
anything. **If the bank is thin, say so and stop** — a UGC script with no customer input is just
an AI-VO script delivered to camera, and it will read like one.

### 4. Clear the four gates

**Blocking.** Work `references/four-gates.md` and state all four, per script.

**In creator-specific mode the persona is constrained**, not free: it has to be one this person
can carry without acting. A creator who reads as a wired 30-something founder is a Wired Lifer or
an HRV Hunter; scripting them as a Lights-Out Loser is casting against type and the footage will
show it. If no persona fits the creator, say so — that is a real finding, not a blocker to route
around.

1. **Persona** — from the `Official Persona` toggle, read live. Default to the four in
   `Final and approved personas`; the other four need Mark's go-ahead, so ask rather than
   quietly picking one. The **Off-Ramper** carries a standing compliance callout — body-state
   language only, Nick's sign-off, no anti-medication framing in paid.
2. **Awareness level** — Unaware → Most-Aware. Read it off the persona's buying behaviour rather
   than guessing. Cold UGC is usually Unaware or Problem-Aware.
3. **Core Desire** — one of the Life Force 8, from the toggle on the same Notion page. Name
   **one**; two means it is not resolved.
4. **Ad Angle** — propose one from the persona's pain / desire / fear if the user did not name
   it, and say which and why. Check it against `excluded_angles` in `config/competitors.yml`.

**The two scripts must not share a Persona + Angle pairing.** Two angles onto the same persona is
one script with extra steps.

### 5. Pick the framework

The 25-framework library lives in the **`ugc-video-frameworks`** skill. Load it — do not reproduce
it here and do not invent a 26th.

Choose on fit, in this order:

1. **The quote bank and the gates decide.** A switching story is `Why I Switched`; scepticism
   overcome is `I Regret Using` or `Problem → Solution`. Let the evidence pick.
2. **Awareness level.** Unaware/Problem-Aware wants native formats (Green Screen, Industry Myths,
   Stop Wasting Your X). Solution/Product-Aware wants proof and comparison (3 Reasons Why,
   Testimonial Mashup, Before/After).
3. **Do not repeat a framework** used in the last `framework_lookback` briefs, or the one picked
   for the other script on this page.

**Pick both frameworks before writing either**, and pair them so one clip bank can serve both.
Two frameworks needing completely disjoint footage will not share ten clips — that is the signal
you have picked badly.

### 6. Write the two scripts

Per beat, three things:

| Spoken | Shot / Action | Note |
|---|---|---|

- **Spoken** is the line, verbatim, as a person talks. Contractions. Fragments. One idea per line.
  If you cannot say it out loud in one breath, it is written, not spoken.
- **Shot / Action** is what the creator physically does — where they are, what is in frame, what
  they pick up.
- **Note** is delivery and pacing.

Rules that hold for every UGC script:

- **Open in the middle of a thought.** No "Hey guys". The first frame is a sentence in progress.
- **The first line carries the whole ad.** If the viewer hears only line one, they should still
  know who this is for.
- **Show the device before you explain it.** Curiosity beats exposition.
- **One claim per script, stated once.** Stacked claims read as an ad.
- **Name the situation, not the condition.** "Ten minutes before a call I've been dreading" is
  ours. "My anxiety" is not.
- **Pay off the Core Desire in the CTA.** A script that opens on LF6 pride and closes on LF3
  relief loses the viewer at the turn.
- **Write in the creator's register, not the brand's.** Keep the substance on-brand; let the
  delivery be theirs.
- **Length**: 30–45s unless the framework says otherwise. Hook inside 3 seconds.

Casting, delivery and energy direction are in `references/ugc-creator-brief.md`. The template's
own **Shooting Specifications** callout governs the technical side — do not contradict it.

### 7. Three hooks per script

The template's naming block asks the creator to *"film the 3 hooks separately to the body"*.

> **2 scripts × 3 hooks = 6 hook takes + 2 body takes**, on one page.

Three genuinely different **mechanisms**, not three rewordings:

| Mechanism | Opens with |
|---|---|
| **In medias res** | Mid-sentence, mid-action, already using it |
| **Direct callout** | Names the viewer's situation in the first four words |
| **Objection-first** | Leads with the reason not to buy, then dismantles it |
| **Reframe** | Says the thing the category never says out loud |

Pick three of the four per script, and do not give both scripts the same three.

> **Flagged:** the Video Brief pipeline standardises on **four** hook variants; this template asks
> for **three**. The UGC pipeline follows the template. Raise it with Mark rather than letting the
> two conventions drift apart by accident.

### 8. Build the clip bank

**10 general clips, shared by both scripts.** Read `references/general-clips.md` — the standing
ten, why each earns its place, their section names, and the capture notes.

The standing ten are the default. Swap one only for a clip that passes the same test:

> **If it cannot be cut into both scripts, it is not a general clip.** It is script b-roll, and it
> does not count toward the ten.

- **No spoken lines in any clip.** The moment a clip carries dialogue it belongs to one script.
- **Same room, same wardrobe, same phone** as the talking-head footage, or it will not cut in.
- **Each row needs a section name**, because the creator names the file `BRoll_<section>`.
- **Run the clips through the compliance gates too.** Footage makes claims — a visible
  prescription bottle implies medication replacement, and a clip showing wrong device placement
  outlives the script it was shot for.

### 9. Run the two compliance gates

**First**, the brand compliance gate in
`.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md` — same product, same
approved claim set, same conditions-vs-feeling-states line. Read it in full.

**Then**, the **endorsement gate** in `references/ugc-creator-brief.md`. A real person on camera
saying "this worked for me" is a testimonial and the brand owns it. It covers personal-outcome
claims, typicality, disclosure, costume authority, and the rule that a customer review is never
handed to a creator as their own experience.

A script that fails either does not get filed. Fix it or drop the concept — never water one down
to hit the count. Run the gates; **do not print them into the brief.**

### 10. File it in the UGC Brief Database

Follow `references/notion-map-ugc.md` exactly. Duplicate the **`✏️ TEMPLATE`** page and fill it —
do not rebuild the layout, and do not edit the standing callouts.

1. **Title**: `<Creator Name>-<Concept>` in creator-specific mode, `General-<Concept>` in
   general mode. Icon **✏️**, parent `3448fb5b-44b0-80b7-a01f-df29eb7dd956`.
2. **Header table**: Content Creator · Product · Event · Inspo link · Offer.
   - `Content Creator` takes the name, or `General — unassigned` plus a one-line casting spec.
   - **Confirm the product** — the template and all four live briefs say `Hoolest Mini`, not
     VeRelief Prime. Pull the offer from Shopify.
3. **`Script 1` and `Script 2`** — hooks then main body, under the headings already there.
4. **`B-ROLLS | SHOTLIST`** — extend the template's 8 rows to **10**, one clip each, section name
   in bold at the front of the `Visual description` cell. `INSPO` takes a link or stays empty.
5. **File Naming Convention** — scope the hook names to the script:
   `Talkinghead_S1_hook1` … `Talkinghead_S2_hook3`, plus `Talkinghead_S1_body` /
   `Talkinghead_S2_body`. B-roll stays `BRoll_<section>`.

**One page per creator.** Four creators shooting the same concept is four pages — which is exactly
what the existing four are. A general brief is one page that any of them could shoot; if it is
later assigned, duplicate it under the creator's name rather than renaming the general one.

### 11. Report

Open with **the brief mode and the creator**, since it framed everything else. Then a short
table, **one row per script**: Concept, framework, persona, awareness, core desire, angle. Then:

- **the four gates as a block per script**, so Mark can check the reasoning
- the customer quote each script was built on, one line each
- **one line confirming the clip bank**: ten clips, and any swap with the reason
- anything dropped and why
- **anything needing sign-off** — an unapproved persona, or an Off-Ramper script for Nick
- in creator-specific mode, **whether genuine use was confirmed**, and which lines are marked
  `[REQUIRES GENUINE USE]` if not

The gates and the research belong in this report, **not** in the brief. The creator cannot act on
an awareness level, and the database has no properties to file one in.

## Guardrails

- **Ask creator-specific or general before anything else.** Never infer it. It decides which
  personas are even available, how the clips are staged, and what the page is called.
- **In creator-specific mode the persona must fit the creator.** You cannot cast someone who is
  already cast. If none of the personas fit them, say so.
- **A general brief must say who to cast.** Otherwise it is not general, it is unfinished.
- **The four gates are blocking.** No persona, awareness level and core desire, no script.
- **Persona comes from the live `Official Persona` page**, never from memory or from this repo.
  Default to the four approved; ask before using the other four.
- **Off-Ramper needs Nick's sign-off** and never runs anti-medication framing in paid. The
  persona is drawn to exactly the framing that carries the risk.
- **Never invent a customer quote, review, or statistic.** If the connectors returned nothing,
  report that and stop.
- **Never put a review verbatim into a creator's mouth as their own experience.** Mine the
  phrasing; write the line.
- **Two scripts and ten clips, every brief.** One script is half a brief. Ten clips shot for only
  one of the two is not a clip bank.
- **The two scripts must differ in framework and in persona+angle.**
- **Three hooks per script**, matching the template's naming block — and the naming block must
  match the number actually written.
- **Wrong database is the loudest failure here.** UGC briefs go in the UGC Brief Database, as
  child pages of the template, with icon ✏️ and no properties.
- **Do not edit the standing callouts** — Shooting Specifications and HOW TO UPLOAD CONTENT are
  identical on every brief.
- **Do not touch existing briefs.** This skill only creates.
- **The brief is for the creator.** Direction they can act on, and nothing else.
