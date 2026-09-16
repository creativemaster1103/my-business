# UGC creator brief — direction, casting and the endorsement gate

Everything a VeRelief Prime script needs on top of the brand brief, because a **real person is
saying it on camera**.

Read `.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md` first. Product,
avatars, voice, approved claims and the compliance gate all live there and are not repeated
here. This file covers only what changes when a human delivers the line.

## The endorsement gate

Run this **after** the brand compliance gate, on every finished script. Any failure blocks
filing.

A scripted creator speaking to camera is an **endorsement**. The brand is responsible for what
they say as if it had said it directly, and "the creator improvised" is not a defence — we wrote
the script.

1. **Does a line state a personal outcome the speaker has not had?**
   → Either the creator has genuinely used the product and can say it, or the line is rewritten
   as something other than personal experience. Never script a first-person result for a creator
   who has not experienced it. If casting is unresolved when the brief is written, mark the line
   `[REQUIRES GENUINE USE]` in the Note column so the producer cannot miss it.

2. **Does a line present an outcome as typical?**
   → "It works in seconds for everyone" is a typicality claim. Keep results individual and
   situational: "it takes the edge off for me before a call."

3. **Is a customer review quoted as the speaker's own words?**
   → Mine the phrasing; do not transplant the sentence. If we genuinely want a customer's words
   on screen, it is a **quote card** — attributed, on screen, as a review — not the creator
   claiming it.

4. **Is a named condition delivered as lived experience?**
   → This is the most common failure, and the brand gate will not always catch it, because it
   reads as a story rather than a claim. "Ever since my anxiety diagnosis" makes the product a
   treatment for a diagnosed condition, whoever is speaking. Rewrite to the situation and the
   feeling state.

5. **Is there a disclosure beat?**
   → Any paid or gifted creator needs a clear, unavoidable disclosure. Script it as a line or an
   on-screen super in the **first few seconds** — not buried in a caption, not at the end. `#ad`
   in the first line of on-screen text is the house default. A creator who is a genuine,
   unpaid customer does not need one, but that has to be true rather than assumed.

6. **Does a white coat, a scrub top, a clipboard or a clinic set imply medical authority?**
   → Cut it, unless the person actually holds that credential and it has been cleared. Costume
   authority is an implied claim.

7. **Does the on-screen text make a claim the spoken line was careful about?**
   → Supers get written last and reviewed least. Run them through the brand gate separately.

8. **Is the device shown being used correctly?**
   → An ad showing wrong placement is worse than no ad. Check the shot direction against the
   actual product, not against how the competitor's device is worn.

## Casting

Cast the **avatar**, not the demographic. Age matters far less than whether the person reads as
someone who would plausibly own the problem.

| Avatar | Reads true when the creator is | Reads false when |
|---|---|---|
| **Wired Lifer** | Visibly mid-day, mid-work, shot in a real workspace | Shot at golden hour looking rested |
| **Off-Ramper** | Matter-of-fact, understated, no redemption-arc energy | Preachy, or dramatising the substance they left |
| **Sleep Struggler** | Filmed at night, low light, low energy delivery | Bright, bouncy, clearly shot at 11am |
| **HRV Hunter** | Fluent in the data without being told to be | Reciting metrics they clearly do not use |

> Avatar strings in Notion are `Wired Lifer`, `Sleep Struggler`, `HRV Hunter`, `Off-Ramper`,
> `Multi`. Note the capital **R** in `Off-Ramper` — other files in this repo write it
> `Off-ramper`, and the select option will not match.

## Production direction

Specify these in the brief's creator direction block. A creator who has to guess will guess
toward "polished", which is the one thing UGC cannot be.

| | Default | Why |
|---|---|---|
| **Camera** | Front-facing phone, hand-held | Tripod-steady reads as produced |
| **Framing** | Chest-up, slightly off-centre, some headroom drift | Perfect framing kills the register |
| **Audio** | Phone mic or earbuds. Room tone audible | Studio audio over a kitchen shot is uncanny |
| **Light** | Whatever the room has, facing a window | Ring light reads as influencer, not customer |
| **Location** | The room where the problem actually happens | A clean neutral wall says nothing |
| **Wardrobe** | What they already own | Styled wardrobe breaks the premise |
| **Takes** | One continuous take per hook, plus b-roll | Cutaways every two seconds signal an edit |

**B-roll to capture on every shoot**, regardless of framework — it is what saves a script in the
edit and costs thirty seconds to grab:

- Device in hand, close, unbranded surface
- Device being applied, clean and correct, from a second angle
- The moment *before* — the actual stressed/tired state, no device in frame
- Hands doing something ordinary nearby: laptop, kettle, phone face-down

## Delivery

- **Talk, do not present.** The read should sound like the middle of a conversation with a
  friend who asked.
- **Keep the stumbles.** A restarted sentence is a credibility signal. Do not direct them out.
- **Do not smile at the claim.** The moment the creator performs enthusiasm, it becomes an ad.
- **Pace down, not up.** The category sells calm; a fast excited read contradicts the product.
- **Never read the super out loud.** Spoken line and on-screen text should do different jobs.

## What the creator direction block contains

Put this near the top of the brief, under the naming tables and before the script. Short, and
only things the creator can act on:

```
CREATOR DIRECTION
Avatar        Wired Lifer — reads as someone mid-workday, not rested
Location      Home desk or office, daylight, real room
Wardrobe      Own clothes, nothing styled
Camera        Front-facing, hand-held, chest-up
Energy        Low and flat. Talking, not presenting
Disclosure    #ad super in the first 2 seconds
Must capture  4 hook takes · full body take · B-roll list below
```

## Two failure modes

1. **The polished UGC.** Well-lit, well-framed, clean audio, confident read. It performs like a
   brand ad because it *is* one, and the format's only advantage — that it does not look like an
   ad — is gone.
2. **The costume UGC.** Deliberate scruffiness over a script that is still brand copy. The
   viewer reads the mismatch instantly: a person in a messy kitchen using the phrase "clinically
   engineered". Authenticity is in the *sentence construction*, not the set dressing.

If the script would be improved by being read by a voice actor over stock footage, it is not a
UGC script — it is an AI-VO script, and it belongs in `/competitor-ad-swipe`'s output instead.
