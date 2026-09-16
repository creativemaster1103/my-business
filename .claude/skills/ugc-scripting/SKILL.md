---
name: ugc-scripting
description: Write creator-ready UGC video scripts for Hoolest — two scripts of five hooks each plus a ten-clip iPhone-shootable B-roll shotlist per brief, for a named content creator or as a general unassigned brief, sourced from customer language and gated on persona, awareness level, core desire and ad angle — and file them in the Notion UGC Brief Database. Use when the user asks for a UGC script, a creator script, a script for a specific creator, a talking-head ad, a testimonial ad, to script a creator shoot, or to run the UGC batch.
---

# UGC Scripting → UGC Brief Database

Write scripts a **creator can shoot on a phone**, from **our own customers' words**, and file them
in the Notion **UGC Brief Database** off the team's own template.

> ## Every brief ships 2 scripts and 10 general clips
>
> **2 scripts**, genuinely different — different framework, different persona+angle pairing. Both
> live on **one** brief page, in the `Script 1` and `Script 2` sections the template already
> carries. Each gets **5 hooks** and a main body — so **10 hook takes and 2 body takes**.
>
> **10 general clips**, one per `B-ROLLS | SHOTLIST` row, captured once and cuttable into
> **either** script. **Shot alone on an iPhone in fifteen minutes** — there is no production
> shoot. Spec in `references/general-clips.md`.
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

> ### All four are the user's to set. If one is missing, ASK.
>
> **Do not choose a gate the user did not give you, and do not proceed on your own pick.** This
> applies to **all four**, Ad Angle included. Naming a persona is not implicitly answering the
> other three.
>
> **Recommending is not deciding.** Come to the question prepared: offer two to four options
> drawn from the persona's pain, desire and fear, say which you would pick and why, and make it
> one easy answer. Then **wait**. What you may not do is pick one, start writing, and report the
> choice afterwards — by then the script is built on it and the user is reviewing a decision
> instead of making one.
>
> These four decide who the ad talks to and what it argues. Getting one wrong does not produce
> a slightly-off script; it produces a script aimed at the wrong person. That is the user's call
> to make, not a detail to infer from a persona page.

Do not confuse these with the **two compliance gates** (brand + endorsement) in step 8. The four
gates decide *what to write*. The compliance gates decide *whether it can ship*.

## What this is not

This is the sibling of `/competitor-ad-swipe`, and the two differ in almost every particular:

| | `/competitor-ad-swipe` | `/ugc-scripting` |
|---|---|---|
| Source | Competitor ads running 30d+ | Customer reviews, surveys, support tickets, ad comments |
| Destination | **Video Brief** database | **UGC Brief Database** page |
| Output | Editor cut sheet | **Creator shoot brief** — spoken lines + shotlist |
| Per brief | 1 concept, 4 hooks | **2 scripts, 5 hooks each, 10 clips** |
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
| ~~Shopify~~ | **ON HOLD — do not connect or query.** See below |
| **Gorgias** | Optional — support tickets are the best source of unspoken objections |

If one is off, stop and name it. Do not substitute invented customer quotes for a connector you
could not reach — a fabricated review is the one failure this pipeline cannot recover from.

> ### 🚫 Shopify is on hold
>
> **Do not query Shopify from this pipeline** — not for price, not for offers, not for product
> status. Standing instruction from Mark, 2026-09-16. It is a hold, not a removal: lift it only
> when Mark says so.
>
> What that changes:
>
> - **Take the `Offer` value from the user, or leave the template's default.** Never invent one,
>   and never infer a discount from an order value.
> - **No price in the scripts.** This was already the better call — good UGC does not quote a
>   price — and with no live source it is now the only defensible one. If a script genuinely
>   needs a price, ask Mark for the figure rather than reaching for a number.
> - The brand brief's *"always pull the live price and current offer from Shopify at run time"*
>   is suspended for the same period. Its point stands: **never hardcode a price.** With the
>   connector on hold, the way to honour that is to not state one.

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

Read `config/ugc-scripting.yml` for `scripts_per_brief` (2), `hooks_per_script` (5),
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
4. **Ad Angle** — **ask.** Derive candidates from the persona's pain / desire / fear, present
   them with a recommendation, and let the user choose. Check the chosen angle against
   `excluded_angles` in `config/competitors.yml`.

**If the user supplied only some of the four, ask for the rest before writing** — in one go, with
options, so it is a single exchange rather than four. A persona on its own is one gate answered
and three still open.

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

### 7. Five hooks per script

> **2 scripts × 5 hooks = 10 hook takes + 2 body takes**, on one page.

Five genuinely different **mechanisms**, not five rewordings of one opening. A reworded hook tests
nothing — the whole reason for five is to find out which *way in* works, and two hooks that differ
only in adjectives give you one data point at twice the cost.

| Mechanism | Opens with |
|---|---|
| **In medias res** | Mid-sentence, mid-action, already using it |
| **Direct callout** | Names the viewer's situation in the first four words |
| **Objection-first** | Leads with the reason not to buy, then dismantles it |
| **Reframe** | Says the thing the category never says out loud |
| **Confession** | Admits something slightly unflattering about themselves |
| **Demonstration-first** | Does the thing on camera before saying anything about it |
| **Contrast** | "Everyone says X" → the actual answer |
| **Failed-alternative** | Opens on the thing that did not work, in frame |

Pick **five of the eight** per script. **The two scripts may share at most two mechanisms**, so
the ten hooks across the page stay genuinely varied rather than converging.

If a concept cannot carry five distinct openings, it is the wrong concept — take the next one
rather than padding with rewordings.

**The naming block must list five**, `Talkinghead_S1_hook1` … `Talkinghead_S1_hook5`. The
template's standing text says three; that number is now wrong and gets corrected on every brief.
A brief asking for three hooks while five are written is how a creator delivers the wrong number
of takes.

### 8. Build the clip bank

**10 general clips, shared by both scripts.** Read `references/general-clips.md` — the standing
ten, their section names, which need the phone propped, and the capture notes.

**The hard constraint is execution, not concept.** The creators shoot on an iPhone, alone, in
their own home, in about fifteen minutes. There is no crew and no production shoot. Every clip
must survive this test:

> Could they shoot it, **alone, in their kitchen, in under a minute**, without moving furniture
> or asking anyone for help?

Which means, on every clip:

- **One person, one iPhone.** No second operator, no second phone, no tripod, no gimbal, no
  lighting kit, no macro lens.
- **Say whether the phone is handheld or propped.** If the clip needs both of the creator's
  hands, the phone gets propped against books, a mug or a wall — and the brief says so. This is
  the single most common reason a clip comes back missing.
- **Nothing to buy.** Only the device, the gel tips, and things already in their home.
- **One take, 6–8 seconds, no choreography.** No timing to hit, no second angle within a take.
- **Nothing shot on a phone screen** — they are filming *with* the phone. A screen means a laptop,
  a TV, or a wall calendar.
- **Write each row as an instruction in the second person.** "Prop the phone and sit how you
  actually sit at 4pm" is shootable. "Evocative shot conveying low-grade tension" is not.

The standing ten are the default and already obey all of this. Swap one only for a clip that
passes both tests — the execution test above, and:

> **If it cannot be cut into both scripts, it is not a general clip.** It is script b-roll, and it
> does not count toward the ten.

- **No spoken lines in any clip.** The moment a clip carries dialogue it belongs to one script.
- **Same room, same clothes** as the talking-head footage, or it will not cut in.
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
   - **Confirm the product with the user** — the template and all four live briefs say
     `Hoolest Mini`, not VeRelief Prime.
   - `Offer` comes from the user or stays at the template's default. **Shopify is on hold** —
     do not query it, and do not guess a discount.
3. **`Script 1` and `Script 2`** — hooks then main body, under the headings already there.
4. **`B-ROLLS | SHOTLIST`** — extend the template's 8 rows to **10**, one clip each, section name
   in bold at the front of the `Visual description` cell. `INSPO` takes a link or stays empty.
5. **File Naming Convention** — the template's standing text says three hooks. **Correct it to
   five and scope the names to the script**: `Talkinghead_S1_hook1` … `Talkinghead_S2_hook5`,
   plus `Talkinghead_S1_body` / `Talkinghead_S2_body`. B-roll stays `BRoll_<section>`, ten of
   them.

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
- **The four gates are blocking, and all four are the user's to set.** If the user did not give
  you an awareness level, a core desire or an ad angle, **ask** — with options and a
  recommendation, then wait. Never pick one yourself and report it afterwards.
- **Persona comes from the live `Official Persona` page**, never from memory or from this repo.
  Default to the four approved; ask before using the other four.
- **Off-Ramper needs Nick's sign-off** and never runs anti-medication framing in paid. The
  persona is drawn to exactly the framing that carries the risk.
- **Never invent a customer quote, review, or statistic.** If the connectors returned nothing,
  report that and stop.
- **Do not touch Shopify.** On hold as of 2026-09-16. No price in scripts; `Offer` comes from the
  user or the template default.
- **Never put a review verbatim into a creator's mouth as their own experience.** Mine the
  phrasing; write the line.
- **Two scripts and ten clips, every brief.** One script is half a brief. Ten clips shot for only
  one of the two is not a clip bank.
- **The two scripts must differ in framework and in persona+angle.**
- **Five hooks per script**, five distinct mechanisms, at most two shared between the two
  scripts. The naming block must be corrected to five — the template's standing text says three.
- **Every clip must be shootable alone on an iPhone in under a minute.** No crew, no tripod, no
  second phone, no props they do not own. State handheld or propped on every row.
- **Wrong database is the loudest failure here.** UGC briefs go in the UGC Brief Database, as
  child pages of the template, with icon ✏️ and no properties.
- **Do not edit the standing callouts** — Shooting Specifications and HOW TO UPLOAD CONTENT are
  identical on every brief.
- **Do not touch existing briefs.** This skill only creates.
- **The brief is for the creator.** Direction they can act on, and nothing else.
