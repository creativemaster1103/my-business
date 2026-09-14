---
name: video-brief-scriptwriting
description: Originate new VeRelief video ad concepts from scratch — no competitor ad — grounded in customer reviews, post-purchase surveys, ad comments and our own Motion performance data, then write the script and file it as a Video Brief in Notion with four hook variants. Use when the user asks to write new video briefs, come up with new ad concepts, script a video ad, fill a gap in the creative library, or run a scriptwriting session.
---

# Video Brief Scriptwriting — originate from scratch

Write new VeRelief video concepts that nobody's ad suggested, and file them as Video Briefs.

The sibling skill, `competitor-ad-swipe`, mines proven competitor ads. This one starts with
nothing, which means it has no borrowed validation and is therefore the easier of the two to do
badly. The whole discipline is in one line:

> **A swipe borrows its validation from ad longevity. Origination has to earn it from evidence.**

Anything written without evidence behind it is a guess in a brief's clothes. It will look exactly
like a good brief, cost the same to produce, and teach us nothing when it loses.

**What origination buys us that swiping cannot:** freedom from what the category happens to be
running. Every vagus-nerve competitor runs the same three angles at the same avatar, so a swipe
can only ever deepen the library's existing skew. Originating is the only way to write for the
avatars and stages the library is starving — `HRV Hunter` has one brief out of 92.

## Required connectors

Check before starting. If one is off, say which — do not work around it.

| Connector | Used for |
|---|---|
| **Parker** | Evidence: customer reviews, post-purchase survey, ad comments, swipe file |
| **Notion** | Destination: the Video Brief database |
| **Shopify** | Live price / offer / product facts |
| **Motion Creative Analytics** | Supporting evidence: what already works on our own account |

Parker, Notion and Shopify are required. Motion is strongly preferred — without it you are
writing blind to our own results. Nothing else is needed to file: file names are built from the
brief's own Notion properties.

## Read before writing

Four files, in this order, and none of them are optional:

1. `references/modular-framework.md` — **the four gates**, the Hook/Body/CTA spine, the blocks,
   and how awareness decides structure. This governs how every script is assembled.
2. `.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md` — product, the four
   approved personas, voice, **approved claim set, compliance gate**. One product, one claim
   set; it is not duplicated here.
3. `references/concept-sources.md` — where evidence comes from and how to search it
4. `references/origination-rules.md` — picking from the gap, framework, dedupe

And for filing: `references/notion-deltas.md`, plus the sibling's
`references/notion-map.md` and `references/naming-convention.md`.

---

## Run the pipeline

### 1. Load config and the library's current state

Read `config/scriptwriting.yml` for volume, evidence requirements and the property defaults. If
the user named an avatar, product or theme, that scopes the run.

Then read what is already there — you cannot fill a gap you have not measured:

```sql
SELECT "Avatar", COUNT(*) AS n
FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
GROUP BY "Avatar" ORDER BY n DESC
```

Do the same for `TEEP Stage`, and pull the last 40 `Concept Name`s for the dedupe check in
`origination-rules.md`. **The gaps you find here decide what you go looking for evidence about**
— not the other way round.

### 2. Gather evidence

Follow `references/concept-sources.md`. Search reviews, the post-purchase survey and ad comments
for the avatar and stage you are trying to serve, then Motion for what our own account has proved
(`insightType="SPEND"` first, always — the rule and the reason are in that file).

Per `config/scriptwriting.yml`: **at least two independent evidence items per concept, at least
one of which is a real customer in their own words.**

Gather across the whole run before writing anything. Evidence found while searching for one
concept routinely turns out to be the better case for a different one.

### 3. Set the four gates — per concept

**Nothing gets written until all four are set.** If the user has not named them and the evidence
does not settle one, **ask**. Never guess a gate and never start writing with one missing.

| Gate | Where it comes from |
|---|---|
| **Core desire** (Life Force 8) | the evidence — what the customer is actually reaching for |
| **Awareness stage** | who you are trying to reach, and what they already know |
| **Ad angle** | the argument the evidence supports |
| **Persona** | the gap in the library (step 1), not where evidence is thickest |

`references/modular-framework.md` has all four lists and the rules. Two that catch people:

- **Awareness decides where the product enters the script**, so it is a structural choice, not a
  label. The same concept at two stages is two different scripts.
- **Desire and persona are not interchangeable.** Wired Lifer's real driver is Life Force 1
  (self-preservation — chronic stress damaging them), not 3. Read the persona before assuming.

Then, per `references/origination-rules.md`: framework from `ugc-video-frameworks`, then the
block list.

Write each concept's case in one sentence before going further:

> Someone said _X_, which means _Y_ about what they believe, and no brief in the library has
> built on that yet.

A concept that cannot fill all three slots is a topic, not a concept. Go back to step 2.

Then check the batch against itself: no two concepts in a run may share an angle + avatar
pairing, and none may repeat a framework from the last `framework_lookback` briefs.

### 4. Pull live product facts

Shopify, every run: current price, current offer, what is in the box, the guarantee window.
**Never hardcode a price.**

### 5. Write the script

Per concept: **four hook variants** (four distinct mechanisms), one body, one CTA. Same persona,
same HPT number.

**All four hooks sit at the brief's awareness level.** Audit each one against the alignment test
in `modular-framework.md` §5 before filing — a Problem Aware hook that gestures at a solution has
drifted to Solution Aware, and one that never names the problem has drifted to Unaware. Both are
disqualified. The awareness letter is in every file name, so a mismatch is visible downstream.

**Product and Person blocks go inside the Body.** The Hook and the CTA are structural units, not
assemblies of blocks — a hook may draw on the same material as a Problem Statement, but it is
not one and is never mapped as one.

Write the `Visual` column as a **direction the editor can shoot**, not a description of a mood.
The `Note` column carries pacing and delivery. One table row per beat, and apply the 1-3 second
rule — if a beat cannot change the visual within three seconds, it is two beats.

### 6. Run the compliance gate

The gate in `verelief-prime-brief.md`, in full, on every script **and on all four hooks**. The
hook is where an unapproved claim hides best, because it is the line written last and read first.

A script that fails the gate does not get filed. Fix it or drop the concept — and if a concept
cannot pass, raise it with the user rather than filing a watered-down version of it.

Originating drifts toward overclaiming in a way swiping does not: a swipe puts the competitor's
claim in front of you and makes you consciously replace it. Here there is no such prompt.

Run the gate; do **not** print it into the brief. It is a check you run, not a section the editor
reads.

### 7. Generate the file names

Build all three strings from the page's own properties, per the sibling's
`references/naming-convention.md`. No spreadsheet, no Zapier.

The variant token is `<hook number><awareness letter>`: `A` Unaware · `B` Problem Aware ·
`C` Solution Aware · `D` Product Aware · `E` Most Aware. **All four hooks carry the same
letter**, because a brief sits at one awareness level. `Self Targeting`, `TEEP Stage` and
`Valence Zone` are no longer part of any name — still set them on the page, but they do not
travel with the asset.

### 8. File in Notion

**Video Brief database only.** Never create an Ad Creative Pipeline row — the team promotes
briefs themselves.

Follow the sibling's `references/notion-map.md` for the page body and the two naming tables at
the top, and `references/notion-deltas.md` for what an originated brief does differently:
`Category: New`, **no AD INSPO section**, `Landing Page` set, and the verified property options.

1. Derive the next `Creative ID` from the live maximum (`HPT091` on 2026-09-11 — re-derive it,
   never assume).
2. Create the page with the two naming tables first, then the Hook/Body/CTA tables.
3. Fill every strategy field — `Avatar`, `TEEP Stage`, `Self Targeting`, `Valence Zone`,
   `Landing Page`. These are what the team filters on, and an unfilled brief is an invisible one.
   23 briefs have no avatar and 39 no TEEP stage; do not add to that.
4. Four hook variants, four file-name rows. They must match exactly.
5. Page icon **⚡**, every brief, no exceptions.

### 9. Report

A short table: Creative ID, concept name, avatar, TEEP stage, framework, angle, brief link.

Then, and only then:

- **The evidence, per concept** — the anchor quote verbatim, its source, the second item, and the
  one-sentence case. This is the part of the report that matters; it is how Mark judges whether
  the concept is real, and it is the only place it appears.
- The avatar and TEEP spread after this run, so the skew stays visible.
- Anything dropped and why — failed the gate, too close to an existing brief, would not carry
  four hooks.

Evidence belongs in the report, **never in the brief**. The editor cannot act on a survey
response.

---

## Guardrails

- **Never invent a customer quote, statistic, or testimonial.** Not as a placeholder, not as an
  illustration, not "in the style of" real reviews. A fabricated quote in a brief becomes a
  fabricated quote in an ad and is not recoverable after it ships. Paraphrase for compliance if
  you must, mark it as a paraphrase, and keep the original beside it in the report.
- **No evidence, no brief.** Two sources, one of them a customer's own words. Falling short is a
  research failure — go back to the sources. It is never a reason to file anyway and flag it.
- **Four distinct hook mechanisms, four file rows, every brief.** A concept that cannot carry
  four openings is the wrong concept. Drop it and take the next one.
- **Fill the gap, do not deepen the groove.** At most one brief per run for `Wired Lifer`, and
  never label an avatar `Multi` because the decision was hard.
- **`Multi` is not an avatar.** It is the label for an undecided brief, and it is already 27 of
  92 rows.
- **Live price from Shopify, every run.**
- **This skill only creates.** Never edit or delete an existing brief. If one looks wrong, say so
  in the report.
- **Icon is always ⚡.** No thematic emoji, however apt.
- **The brief is for the editor.** Naming tables, general instruction, glossary, Hook/Body/CTA.
  No evidence section, no strategy rationale, no compliance table. Anything the editor cannot act
  on is noise.
- **Never fill the missing AD INSPO with a competitor's ad.** That makes it a swipe filed as an
  original. If a competitor ad is genuinely the seed, run `/competitor-ad-swipe` instead.
