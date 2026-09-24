---
name: sb7-framework
description: "ASK THE USER FIRST — never invoke this skill on your own initiative. Even when a task obviously fits, say what you would use it for and wait for a yes. Build and apply StoryBrand (SB7) messaging — Donald Miller's 7-part framework where the customer is the hero and the brand is the guide. Use this skill to create a BrandScript for a product, write a one-liner, turn a BrandScript into ad scripts, VSLs, landing pages, emails, or hooks, or audit existing copy against the 7 elements. Trigger whenever the user mentions StoryBrand, SB7, BrandScript, one-liner, 'customer as hero', 'brand as guide', or asks to clarify a product's messaging, fix confusing copy, find the internal problem, write stakes/success sections, or structure an ad or page around a story — even if they don't name the framework."
---

# SB7 Framework (StoryBrand)

> **Invoke only when asked.** Mark's standing instruction, 2026-09-24: always ask before
> using this framework. Do not auto-trigger it because a task looks like a story problem, and
> do not apply its structure quietly without naming it. If SB7 would help, say so in a line and
> wait for a yes. This overrides the trigger wording in the description above.

This skill turns a product into a clear hero story the customer can see themselves in, then turns that story into copy.

The core rule is that **the customer is the hero and the brand is the guide.** When a brand makes itself the hero ("we're innovative, we're award-winning"), the customer has no role in the story and tunes out. Every output from this skill should pass that test.

---

## The 7 Elements

| # | Element | What it answers | Common failure |
|---|---|---|---|
| 1 | **Character** | What does the customer want? | Wants too many things, or something vague ("a better life") |
| 2 | **Problem** | What's in the way? (external, internal, philosophical, villain) | Only the external problem is named |
| 3 | **Guide** | Why should they trust us? (empathy + authority) | All authority, no empathy, or brand bragging |
| 4 | **Plan** | What exactly do they do? (process plan + agreement plan) | No plan, or a plan with 7 steps |
| 5 | **Call to Action** | What's the ask? (direct + transitional) | Soft, hidden, or only one CTA for all readiness levels |
| 6 | **Failure** | What's at stake if they don't act? | No stakes at all, or fear-mongering |
| 7 | **Success** | What does life look like after? | Abstract ("feel your best") instead of concrete |

### Element detail

**1. Character — one clear want.** Pick a single desire tied to survival-level needs: conserving time or energy, feeling safe, feeling at ease in their own body, belonging, status, relief. The want should be specific enough to picture. "Wind down at night without scrolling for two hours" works. "Wellness" doesn't.

**2. Problem — three levels plus a villain.**
- *External:* the tangible, physical issue.
- *Internal:* how the external problem makes them feel. **This is what people actually buy to resolve.** Spend the most time here.
- *Philosophical:* why it's wrong that they have to deal with this at all ("You shouldn't need a prescription just to feel calm").
- *Villain:* a personified root cause. It can be a condition of modern life, a system, a habit loop, or an old way of doing things. Keep it to one villain, and make it not a named competitor.

**3. Guide — empathy first, then authority.** Empathy is a line that proves you understand the internal problem ("We know what it's like to lie awake with your mind racing"). Authority is proof in the form of review counts, star ratings, testimonials, expert involvement, press, or units sold. Keep authority brief, because the guide's job is to point at the hero rather than at itself.

**4. Plan — make buying feel easy.**
- *Process plan:* 3 steps (4 max) from purchase to result. For example: order → use it X minutes a day → feel the shift.
- *Agreement plan:* promises that remove fear, like the guarantee, free returns, shipping, or support.

**5. Call to Action — two lanes.**
- *Direct:* buy now / shop / get yours. It should be repeated and visible.
- *Transitional:* for people not ready yet, like a quiz, guide, comparison chart, webinar, or email offer.

**6. Failure — just enough stakes.** Describe the cost of inaction in the customer's terms: the problem continues, the feeling persists, the moments get missed. Use a pinch rather than a pound. Stakes create urgency, while too much fear creates avoidance and, in health categories, compliance risk.

**7. Success — the concrete after.** Paint the resolved state with sensory detail and identity. Who do they become? ("The calm one in the room.") Success can land on three levels: *winning power/position*, *unification/wholeness* (feeling complete or at peace), and *self-realization* (becoming who they want to be).

---

## Modes

Figure out which mode the user needs. If it's unclear, default to **Mode 1**, since every other mode depends on having a BrandScript.

### Mode 1 — Build a BrandScript

**Inputs to gather.** Pull these from the conversation, memory, or files first, and ask only for what's missing: the product, the target persona, the core mechanism/benefit, the proof available (reviews, stats, experts), the offer and guarantee, and the price point.

**Process.**
1. Draft all 7 elements.
2. For the Problem section, write 3 options for the internal problem and pick the strongest. The internal problem is the highest-leverage choice in the whole script.
3. Write the one-liner (see format below).
4. Run the Quality Checks and the Compliance Layer.
5. Flag your assumptions and the 2–3 choices most worth the user's review.

**Output format:**

```
# BrandScript — [Product] × [Persona]

## One-liner
[Problem] → [Solution/plan] → [Result]

## 1. Character — wants
## 2. Problem
- Villain:
- External:
- Internal:  (options A / B / C → chosen: X, why)
- Philosophical:
## 3. Guide
- Empathy line:
- Authority proof:
## 4. Plan
- Process: 1. / 2. / 3.
- Agreement:
## 5. Call to Action
- Direct:
- Transitional:
## 6. Failure (stakes)
## 7. Success (the after)

## Compliance flags
## Assumptions & review points
```

**One-liner format:** 1–2 sentences. It opens with the problem (the hook), names the solution as the plan, and closes with the result. For example: "Most people's nervous systems never get a chance to power down. [Product] gives you a few minutes a day to reset, so you can fall asleep feeling like yourself again."

### Mode 2 — Turn a BrandScript into assets

Map the SB7 elements onto the asset's structure. If no BrandScript exists yet, build a compact one first (you can show it briefly) and then write the asset.

| Asset | SB7 mapping |
|---|---|
| **Short video ad (15–30s)** | Hook = Problem (internal-led) → Guide (empathy beat) → Plan (1-line demo) → Success glimpse → Direct CTA |
| **Long video / VSL (60s+)** | Hook = Problem → Villain reveal → Failed alternatives (stakes) → Guide (empathy + authority) → Plan (3 steps + demo) → Success story → Agreement plan (guarantee) → Direct CTA → Transitional CTA if the platform allows |
| **UGC script** | The creator *is* the hero telling their own story: Character → Problem → found the Guide → followed the Plan → Success. The brand stays in the guide role. Hand off to Chopper for full UGC formatting if needed. |
| **Static ad** | One element carries the whole ad. Pick Problem (internal), Success (the after), or Plan (it's this easy) and make it the single idea. |
| **Landing page** | Header (Character want + Success + Direct CTA) → Stakes → Value/Success → Guide (empathy + authority) → Plan → Explanatory paragraph → Transitional CTA → Direct CTA repeated |
| **Email / nurture sequence** | Use the transitional CTA as the entry. Email 1 names the Problem, Email 2 introduces the Guide, Email 3 lays out the Plan, Email 4 paints Success, Email 5 is the direct CTA with stakes |
| **Hooks batch** | Write hooks from each of: external problem, internal problem, philosophical problem, villain, stakes, and success |

**Awareness-level emphasis (Schwartz).** Adjust which elements lead based on the audience's awareness level.
- *Unaware:* lead with Character/Problem (internal or philosophical) and introduce the villain. The product appears late.
- *Problem aware:* lead with the internal problem and the villain, then the Guide.
- *Solution aware:* lead with the Guide (why this, why us) and the Plan.
- *Product aware:* lead with the Agreement plan, Success, and the Direct CTA.

When the user is building variations, note the awareness level and angle for each piece so it can slot into a Nami matrix.

### Mode 3 — Audit existing copy

When the user shares a script, page, ad, or email:
1. Score each of the 7 elements from 0 to 2 (0 = missing, 1 = present but weak, 2 = strong), with a one-line reason for each.
2. Run the **Hero Test**: count the sentences about the brand versus the sentences about the customer, and quote the worst offender.
3. Name the single biggest gap, which is usually a missing internal problem, a missing plan, or brand-as-hero framing.
4. Rewrite the weakest 1–2 sections. Do not rewrite everything unless asked.
5. Run the Compliance Layer on both the original and the rewrite.

---

## Quality Checks (run on every output)

- **Hero test:** Is the customer the subject of most sentences? If the brand is the grammatical subject too often, flip it ("We built X to…" → "You get…").
- **One want:** Is there exactly one desire driving the story?
- **Internal problem named:** Is the feeling explicit, not just the symptom?
- **Plan is ≤4 steps** and each step is doable.
- **Both CTAs exist** (a direct and a transitional) wherever the format allows.
- **Stakes are a pinch:** Is there any fear or shame language that crosses a line?
- **Success is concrete:** Can you picture it? Does it describe a moment rather than an adjective?
- **The grunt test (for headers/hooks):** Could someone glancing for 5 seconds tell what's offered, how it improves their life, and what to do next?

---

## Compliance Layer (health/wellness DTC)

The Problem, Failure, and Success sections are where health claims slip in. Apply these defaults unless the user's own compliance rules say otherwise. If the user has standing rules on file, those override these defaults.

- **Body-state language over condition language.** Write "feel wound up," "a racing mind at night," or "a body that won't settle" rather than naming diagnoses or promising to treat, cure, or prevent conditions.
- **No time-to-effect claims** ("results in 5 minutes," "sleep tonight") without explicit sign-off from whoever owns compliance. Flag them instead of writing them.
- **No competitor brand names**, including in the villain or failed-alternatives sections. Use categories ("pills," "apps," "another supplement").
- **Success = experience, not outcome guarantee.** Write "Wake up feeling more like yourself" rather than "eliminate your anxiety." Testimonials describe personal experience.
- **Stakes without shame.** Avoid body-shaming, fear of illness, or implying something is wrong with the viewer personally. Meta's health/personal-attributes policies penalize "you" + condition phrasing ("Do you suffer from…?"), so frame the problem around situations and feelings instead.
- **Authority accuracy.** Only cite proof the user has actually provided. Never invent review counts, studies, or expert quotes. Leave placeholders like `[# reviews]` instead.

List every flag under **Compliance flags** with the line, the issue, and a safer alternative.

---

## Crew handoffs

- **Nami:** a BrandScript's persona × awareness × angle options can feed a combination matrix.
- **Sanji:** a finished BrandScript becomes the messaging section of a creative brief.
- **Chopper:** hand off SB7-structured UGC beats for full script formatting.
- **Brook:** Brook breaks down how an ad is built, and SB7 checks whether its story holds together. For audits, the two lenses complement each other.

Mention a handoff only when it's the natural next step, not on every output.
