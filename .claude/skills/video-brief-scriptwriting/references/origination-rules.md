# Building the concept

Evidence gives you something true. This file is about turning it into something an editor can
shoot — and about the three ways an originated brief goes wrong that a swiped one cannot.

---

## Pick the avatar first, and pick it from the gap

Not the avatar the evidence is most abundant for. Abundance tracks who we have already been
selling to, so following it deepens the skew that made originating worth doing.

Live spread, read 2026-09-11:

```
Wired Lifer 34 · Multi 27 · (unset) 23 · Sleep Struggler 4 · Off-Ramper 3 · HRV Hunter 1
```

Re-read it each run:

```sql
SELECT "Avatar", COUNT(*) AS n
FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
GROUP BY "Avatar" ORDER BY n DESC
```

A swipe is constrained — you take the avatar the competitor's ad maps to. Origination is not,
and that freedom is most of its value. **One brief per run may serve Wired Lifer; the rest go to
the thin columns.** If the evidence genuinely will not carry a thin avatar this run, say so in
the report rather than filing three more Wired Lifer briefs and calling the spread a known issue.

`Multi` is not an avatar. It is what a brief gets labelled when nobody decided, and it is the
second-largest column in the library. Do not add to it: pick the person, or drop the concept.

## Then the angle

The angle is the argument, and it has to come out of the evidence rather than off a list. Useful
shapes, if you need prompting: Problem-Solution, Comparison, Transformation, Functional Benefit,
Identity, Authority, Social Proof, Curiosity, Gifting.

Two checks before it survives:

1. **Is the category already saturated with it?** Every vagus-nerve brand runs the same three
   arguments. If the angle is one of those, originating has bought us nothing — we have written
   a competitor's ad without the benefit of knowing it worked for them.
2. **Does it need a claim we cannot make?** Run it past the approved claim set in
   `verelief-prime-brief.md` *now*, not after the script is written. An angle that only works
   with a condition claim is a dead angle, and finding that out at the compliance gate costs a
   whole script.

## Then the framework

Read the **`ugc-video-frameworks`** skill and pick from its 25. The framework is the structural
load a swipe would have inherited from the source ad — originating means choosing it
deliberately, which is a real decision and not a formality.

Match it to the TEEP stage:

| TEEP stage | What the viewer needs | Frameworks that fit |
|---|---|---|
| `a - Trigger` | To recognise themselves | Problem → Solution, 3 Signs, Green Screen |
| `b - Exploration` | To understand the mechanism | Industry Secret, Industry Myths, Unboxing |
| `c - Evaluation` | To believe it over the alternative | Why I Switched, Before/After, Testimonial Mashup |
| `d - Purchase` | A reason to act now | Offer formats, 3 Reasons Why, Customer Story |

`d - Purchase` has 5 briefs and `a - Trigger` has 8, against 21 and 19 for the middle two. Prefer
the thin ends when a concept could honestly sit at more than one stage.

**Do not repeat a framework** used in the last `framework_lookback` briefs, or one already used
by another concept in this run.

## Then build the blocks

Use the **`brook-adblock-analyzer`** vocabulary to *construct*, not just to analyse. Decide, per
concept, which blocks are present and in what order:

- **Structure**: Hook → Body → CTA
- **Person blocks**: Problem Statement, Failed Alternative, Desired Result, Before & After,
  Social Proof, Storytelling
- **Product blocks**: Intro, Demo, Features, Buying Experience, Unboxing

An originated script drifts toward **all body and no shape** — a list of true things about the
product. Choosing the blocks up front is what stops that. If the block list for two concepts in
a run is identical, one of them is not a separate concept.

---

## The four hooks

Four ways into **one** concept: same body, same CTA, same avatar, same HPT number, four different
openings. Not four concepts. A concept does not get to ship with one hook and count as one of the
three.

They must be four different **mechanisms**, not four rewordings:

| Mechanism | What it does in the first second |
|---|---|
| Reframe | Tells them the thing they believe is wrong |
| Cost | Names what the problem is costing them |
| In medias res | Drops them mid-moment, no setup |
| Direct callout | Names the person: "If you've ever…" |
| Question | Makes them answer something about themselves |
| Pattern interrupt | Visual or tonal jolt that does not belong on the feed |

Pick four that are genuinely distinct. Rephrasing one line four ways is one hook. **If a concept
cannot carry four distinct openings, it is the wrong concept** — drop it and take the next one
rather than shipping a short brief.

---

## Do not re-file something the library already has

There is no ad ID to dedupe against here, so the check is semantic and you have to do it by
reading. Before writing:

```sql
SELECT "Creative ID", "Concept Name", "Avatar", "TEEP Stage", "Content Type"
FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
WHERE "Creative ID" LIKE 'HPT%'
ORDER BY "Creative ID" DESC LIMIT 40
```

Read the concept names and open anything that sounds close. A new concept must differ from every
recent brief in **at least two** of: angle, avatar, framework, TEEP stage. Differing only in
wording is an iteration, and an iteration is a different thing:

- Genuinely new concept → `Category: New`
- Deliberate variation on an existing brief → `Category: Iteration`, and say in the report which
  HPT number it iterates on

Those are the only two options the property has. Filing an iteration as new is how a library
grows to 92 rows that look varied and test three ideas.

---

## Voice

`verelief-prime-brief.md` carries the voice and the claim set in full, and it is not optional
reading. The three things originating gets wrong that swiping does not:

1. **Writing the product's ad instead of the viewer's.** With no source ad imposing a shape, a
   script slides toward features. Every beat has to be doing something to the viewer.
2. **Reaching for the category cliché.** "Reset your nervous system in 60 seconds" is what you
   write when the evidence ran out. Go back to the sources instead.
3. **Overclaiming, because nobody else's claim is in the way.** A swipe makes you notice the
   competitor's claim and consciously replace it. Originating has no such prompt, so the drift
   is silent. Run the compliance gate honestly, and run it on the hooks too — the hook is where
   an unapproved claim hides best.
