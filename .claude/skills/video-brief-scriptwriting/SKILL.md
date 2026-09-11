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
| **Zapier** | Writing the naming-generator spreadsheet (Google Drive is read-only for content) |

Parker, Notion and Shopify are required. Motion is strongly preferred — without it you are
writing blind to our own results. Zapier is required to file, because the file names come from
Mark's sheet and are never reconstructed by hand.

## Read before writing

Three files, in this order, and none of them are optional:

1. `.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md` — product, avatars,
   voice, **approved claim set, compliance gate**. One product, one claim set; it is not
   duplicated here.
2. `references/concept-sources.md` — where evidence comes from and how to search it
3. `references/origination-rules.md` — avatar, angle, framework, blocks, four hooks, dedupe

And for filing: `references/notion-deltas.md`, plus the sibling's
`references/notion-map.md` and `references/naming-generator.md`.

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

### 3. Form the concepts

Per `references/origination-rules.md`, in this order — avatar from the gap, angle from the
evidence, framework from `ugc-video-frameworks`, then the block list.

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

Per concept: **four hook variants** (four distinct mechanisms — see `origination-rules.md`), one
body, one CTA. Same avatar, same HPT number.

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

Mark's Naming Convention Generator, via Zapier, per the sibling's
`references/naming-generator.md`. **Once per brief, never batched** — `notion-deltas.md` §5 says
why. Paste the output strings verbatim; if one looks wrong, the inputs were wrong.

Set `Content Type`, `Editor` and `Strategist` in the spreadsheet row **and** the Notion
properties. Changing one without the other leaves the filename disagreeing with the database.

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
