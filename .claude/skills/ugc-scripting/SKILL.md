---
name: ugc-scripting
description: Write creator-ready UGC video scripts for VeRelief Prime — spoken lines, shot direction, on-screen text and four hook variants — sourced from customer language rather than competitor ads, and file them as Video Briefs in Notion. Use when the user asks for a UGC script, a creator script, a talking-head ad, a testimonial ad, to script a creator shoot, or to run the UGC batch.
---

# UGC Scripting → VeRelief Prime Brief

Write scripts a **creator can shoot on a phone**, from **our own customers' words**, and file
them in the same Video Brief database the rest of the pipeline uses.

This is the sibling of `/competitor-ad-swipe` and deliberately the opposite end of the funnel of
ideas. That skill mines what *competitors* proved in the auction. This one mines what *our
buyers* already said, in their own language, and puts it in a real person's mouth.

**The premise: the best UGC line is a sentence a customer already wrote.** Copywriters invent
objections; customers state them. A review that says "I was sceptical because I'd already wasted
money on a breathing app" is a hook, an objection and a proof beat in one, and it is pre-validated
in a way no amount of ideation is.

## What makes this different from an AI-VO brief

| | `/competitor-ad-swipe` | `/ugc-scripting` |
|---|---|---|
| Source | Competitor ads running 30d+ | Customer reviews, surveys, support tickets, ad comments |
| Output | Editor cut sheet (`Visual / Copy / Note`) | **Creator shoot script** — verbatim spoken lines + shot direction |
| Reads as | Produced | A person talking to their phone |
| `Content Type` | `AI VO` | **`UGC`** |
| Extra gate | — | **Endorsement gate** (a real person is making the claim) |

A creator cannot act on "SUPER: two minutes on the vagus nerve". They need the sentence to say,
where to stand, and what to do with their hands. Write for that.

## Required connectors

| Connector | Used for |
|---|---|
| **Notion** | Destination: Video Brief. Also the source of what has already been scripted |
| **Okendo** | Voice of customer — product reviews, review questions |
| **Parker** | Voice of customer at depth — semantic review search, post-purchase survey, ad comments |
| **Shopify** | Live price / offer facts |
| **Zapier** | Writes to the naming-convention sheet (Drive connector is read-only) |
| **Gorgias** | Optional — support tickets are the best source of unspoken objections |

If one is off, stop and name it. Do not substitute invented customer quotes for a connector you
could not reach — a fabricated review is the one failure this pipeline cannot recover from.

## Run the pipeline

### 1. Load the config

Read `config/ugc-scripting.yml` for `scripts_per_run`, `hooks_per_script`, `framework_lookback`
and the creator roster. A user instruction overrides the file.

### 2. Mine the voice of customer

Read `references/voice-of-customer.md` — it carries the search terms that actually surface
material, and the test for whether a quote is usable or merely nice.

**Do this before choosing a framework.** Picking the framework first makes you go looking for
quotes that fit it, which is how you end up with a script that sounds like an ad wearing a
customer's voice.

Pull in this order and keep the raw language:

1. **`reviews_search` / `reviews_aggregate` (Okendo)** — filter to VeRelief. Read the 3- and
   4-star reviews first. Five-star reviews say "love it" and carry no information; the middling
   ones say *what they expected, what they got, and what nearly stopped them buying*.
2. **`search_customer_reviews_semantic` (Parker)** — query the emotional states, not the product:
   "couldn't switch off", "tried everything", "sceptical at first", "wife noticed".
3. **`semantic_search_post_purchase_survey` / `lookup_post_purchase_survey`** — this is the only
   source that tells you *what they were doing the moment they decided to buy*. Gold for hooks.
4. **`search_facebook_ad_comments_semantic`** — the objections people voice in public, which are
   the ones the script has to pre-empt.
5. **Gorgias tickets**, if enabled — the objections people only voice in private.

Collect **verbatim** lines into a quote bank before writing anything. For each, note the avatar it
belongs to and whether it is a hook, an objection, or a proof beat.

> **Quotes are raw material, not script.** Never paste a review into a script and call it a
> testimonial — see the endorsement gate in step 7. You are mining the *phrasing and the
> objection*, then writing a line a creator can honestly say.

**If the quote bank is thin, say so and stop.** A UGC script written with no customer input is
just an AI-VO script delivered to camera, and it will read like one.

### 3. Pick the framework

The 25-framework library lives in the **`ugc-video-frameworks`** skill. Load it — do not
reproduce it here and do not invent a 26th.

Choose on fit, in this order:

1. **The quote bank decides.** If the strongest material is a switching story, that is
   `Why I Switched`. If it is scepticism overcome, that is `I Regret Using` or `Problem →
   Solution`. Let the evidence pick, not the roster.
2. **TEEP stage.** Trigger/Exploration wants awareness and native formats (Green Screen, Industry
   Myths, Stop Wasting Your X). Evaluation/Purchase wants proof and comparison (3 Reasons Why,
   Testimonial Mashup, Before/After).
3. **Do not repeat a framework** used in the last `framework_lookback` briefs, or one already
   used earlier in this run.

Check the recent framework history before choosing:

```sql
SELECT "Creative ID", "Content Type", "Avatar", "Concept Name", createdTime
FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
ORDER BY createdTime DESC LIMIT 20
```

### 4. Set the strategy fields

Pick from the **live** option sets — these are the fields the team filters on, and an unfilled
brief is an invisible one. `references/notion-map-ugc.md` carries the verified values; the ones
that bite are noted there.

- **Avatar** — prefer an under-served one when two candidates are close. Re-read the live counts
  each run rather than trusting a list.
- **TEEP Stage**, **Self Targeting**, **Valence Zone** — from the emotional register of the
  quote you built the script on, not from what would be convenient.
- **Landing Page** — UGC usually points somewhere specific. Match the script's argument to the
  page (a sleep script goes to `Racing mind to Asleep`, not `Home Page`).

### 5. Write the script

Structure is **Hook / Body / CTA**, same as every brief. What changes is the column set — a
creator needs to be told what to *say* and what to *do*, in that order.

Per beat, three things:

| Spoken | Shot / Action | Note |
|---|---|---|

- **Spoken** is the line, verbatim, as a person talks. Contractions. Sentence fragments. One
  idea per line. If you cannot say it out loud in one breath, it is written, not spoken.
- **Shot / Action** is what the creator physically does — where they are, what is in frame, what
  they pick up. `Hand-held, kitchen, morning light. Holds device up to camera, doesn't explain
  it yet.`
- **Note** is delivery and pacing: energy, where to pause, what to cut on.

Rules that hold for every UGC script:

- **Open in the middle of a thought.** No "Hey guys". The first frame is already a sentence in
  progress.
- **The first line carries the whole ad.** If the viewer only hears line one, they should still
  know who this is for.
- **Show the device before you explain it.** Curiosity beats exposition.
- **One claim per script, stated once.** UGC that stacks claims reads as an ad.
- **Name the situation, not the condition.** "Ten minutes before a call I've been dreading" is
  ours. "My anxiety" is not — see the compliance gate.
- **Write in the creator's register, not the brand's.** The brand voice is calm and
  mechanism-forward; a 26-year-old on their kitchen floor is not. Keep the *substance* on-brand
  and let the *delivery* be theirs.
- **Length**: 30–45s unless the framework says otherwise. Hook inside 3 seconds.

Casting, shoot defaults, b-roll and the creator direction block are all in
`references/ugc-creator-brief.md`. Fill the direction block from it — a creator left to guess
will guess toward "polished", which is the one thing UGC cannot be.

### 6. Four hook variants, always

Same arithmetic as every other brief:

> **1 concept = 1 brief = 1 `HPT` number, carrying exactly 4 hooks.** Same body, same CTA,
> same avatar, four different openings — and four file-name rows.

Four genuinely different **mechanisms**, not four rewordings. For UGC the mechanisms that work:

| Mechanism | Opens with |
|---|---|
| **In medias res** | Mid-sentence, mid-action, already using it |
| **Direct callout** | Names the viewer's situation in the first four words |
| **Objection-first** | Leads with the reason not to buy, then dismantles it |
| **Reframe** | Says the thing the category never says out loud |

If a concept cannot carry four distinct openings, it is the wrong concept. Take the next one.

### 7. Run both gates

**First**, the brand compliance gate in
`.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md`. It is the same product,
the same approved claim set and the same conditions-vs-feeling-states line. Read it in full.

**Then**, the **endorsement gate** in `references/ugc-creator-brief.md`. This one is specific to
UGC and exists because a real person on camera saying "this worked for me" is a testimonial, and
the brand owns it. It covers what a creator may state as personal experience, disclosure, and
the difference between a script and a claim.

A script that fails either gate does not get filed. Fix it or drop the concept — never file a
watered-down script to hit the count.

Run the gates; **do not print them into the brief.** They are checks, not sections the creator
needs to read.

### 8. Generate the file names

Follow `.claude/skills/competitor-ad-swipe/references/naming-generator.md` exactly — clear rows
6-16, write one input row per hook variant, read the computed output back, paste it verbatim.
The traps in that file (the leading-zero date, empty strings not clearing cells) apply here
unchanged.

**The only delta is `Content Type` = `UGC`**, and it must be set identically in the sheet and in
the Notion property or the filename disagrees with the database.

### 9. File it in Notion

**Video Brief database only.** Never an Ad Creative Pipeline row — the team promotes briefs
themselves. Property mapping in `references/notion-map-ugc.md`.

1. Next `Creative ID`: highest well-formed `HPT<nnn>` + 1, zero-padded.
2. Page body, in order: the two naming tables → creator direction block → glossary →
   Hook/Body/CTA tables. One file-name row per hook variant.
3. Page **icon ⚡**. Template default, every brief, no exceptions.
4. **No AD INSPO embed** unless the script was built off a specific reference ad. There is no
   TrendTrack share link for an original script, and an empty AD INSPO heading is worse than none.

### 10. Report

A short table: Concept Name, framework, avatar, TEEP stage, Creative ID, brief link. Then:

- the customer quote each script was built on, one line each, so Mark can sanity-check the
  sourcing
- anything dropped and why
- the current avatar spread

Nothing else. The voice-of-customer research belongs in this report, not in the brief.

## Guardrails

- **Never invent a customer quote, review, or statistic.** If the connectors returned nothing,
  report that. A fabricated review in a brief becomes a fabricated claim in an ad.
- **Never put a review verbatim into a creator's mouth as their own experience.** Mine the
  phrasing; write the line. The endorsement gate covers this.
- **Four hook variants, four file rows, every brief.** A hook with no row means the creator
  delivers the wrong number of cuts.
- **Never drop the naming tables.** They are how deliverables get named.
- **Content Type is `UGC`** in both Notion and the sheet, or the filename lies.
- **Do not touch existing rows.** This skill only creates.
- **The brief is for the creator.** Direction they can act on, and nothing else — no framework
  theory, no research dump, no compliance table.
