# Prompt anatomy

## The slots

Write every image prompt as these slots, in this order, comma-joined. The order matters: models
weight the front of the prompt more heavily, so the subject and the action go first and the
format housekeeping goes last.

```
SUBJECT — who or what, specific
ACTION — one verb, present participle
ENVIRONMENT — where, and what is in the near background
CAMERA — lens, height, distance, angle
LIGHT — source, direction, quality, temperature
GRADE — palette and contrast
TEXTURE — the realism levers (below)
FORMAT — aspect ratio, and any deliberate empty space
```

Worked example:

> A woman in her late thirties in a grey merino sweater, pressing a small handheld device to the
> side of her neck, at a home office desk with a laptop half-closed and a cold coffee, shot on a
> 35mm at chest height from three-quarter front, soft overcast window light from frame left with
> no fill, muted desaturated palette with warm skin tones, visible skin texture and fine flyaway
> hair, slight sensor grain, 9:16 with clean space in the upper third

Not: *"a calm woman using a wellness device, beautiful lighting, high quality, 8k"*. Quality
adjectives (`8k`, `masterpiece`, `award-winning`) do nothing on current models except dilute the
tokens that would have worked.

## Video adds four slots

```
MOTION — what moves, one primary action
CAMERA MOVE — one move: push in, pull back, slow pan left, static handheld, orbit
TIMING — where the beat lands inside the duration
AUDIO — on or off; if on, what it is
```

Hard rules for clips:

- **One action, one camera move.** "She presses the device to her neck and then smiles and then
  puts it down while the camera pushes in and orbits" is four clips, not one.
- **Never ask for a cut.** A generation is one continuous shot. Cuts are assembly.
- **Say what the shot ends on.** Models resolve ambiguity at the tail badly; naming the end state
  fixes most of the mush in the last second.
- **Match duration to the beat.** A single gesture is 4–5s. A gesture plus a reaction is 8–10s.
  Padding a 5s idea to 15s gives the model room to invent something you did not ask for.

## Camera vocabulary that actually changes the output

| Want | Say |
|---|---|
| Intimate, close | `50mm, close-up, chest height, shallow depth of field` |
| Documentary, honest | `35mm, handheld with slight drift, eye level` |
| Phone-shot / UGC | `front-facing phone camera, arm's length, slight lens distortion, vertical` |
| Product hero | `85mm macro, product centred, seamless backdrop, static tripod` |
| Scale, environment | `24mm wide, low angle, deep focus` |
| Movement toward | `slow push in` (not "zoom" — zoom reads as a lens artefact) |
| Movement around | `slow orbit right` |
| Stillness that is not dead | `locked off with faint handheld breathing` |

## Light vocabulary

Name **source, direction, quality, temperature**. Four words gets you a look; "good lighting"
gets you a default.

- `soft overcast window light from frame left, no fill, cool 5600K`
- `single warm practical lamp behind the subject, hard rim, 2700K, deep falloff`
- `bounced key from a white wall camera right, one-stop fill, neutral`
- `late golden hour backlight through a window, visible haze`

## Realism levers (the anti-AI kit)

AI output looks like AI mostly because it is too clean, too symmetrical, and too evenly lit.
Fix it by asking for the flaws:

- `visible skin texture, pores, no beauty retouching`
- `fine flyaway hairs, slightly uneven skin tone`
- `imperfect framing, subject slightly off-centre`
- `natural asymmetry in the face`
- `mixed colour temperature between window and lamp`
- `slight motion blur on the hand`
- `faint sensor grain / phone camera noise in the shadows`
- `unstyled background — a real desk, not a set`

Use three or four, not all of them. Loaded together they start reading as a filter.

## Negative space for text

If a designer or Meta will put copy on the frame, ask for the hole:

> `9:16, clean uncluttered upper third for headline text, subject in the lower two thirds`

Do not ask a realism model to render the headline itself. Generate the plate clean, then either
set the type in design, or render text-carrying variants on `nano_banana_pro` /
`gpt_image_2_5` / `openai_hazel`.

## Failure modes and their fixes

| Symptom | Cause | Fix |
|---|---|---|
| Garbled letters on packaging or a sign | Realism model asked to render text | Re-route to `nano_banana_pro` / `gpt_image_2_5` / `openai_hazel`, or generate clean and set type after |
| Product changes shape between frames | Product described in words | Pass a real product photo as `image_references`; for video use `seedance_2_0` |
| Mangled hands | Hands doing something fiddly at distance | Bring the hand closer and simplify the action, or crop it out of frame |
| Clip goes soft / invents motion in the last second | Duration longer than the idea | Shorten, and name the end state |
| Face changes across a set | No identity anchor | `soul_id` with `soul_2`, `soul_cast`, or the `character-sheet` workflow |
| Output ignores half the prompt | Prompt too long, or contradictory | Cut the quality adjectives first; then resolve the contradiction (you cannot have `shallow depth of field` and `deep focus`) |
| Right idea, wrong crop | Aspect ratio left to default | State it, and confirm the model supports it via `models_explore action:"get"` |
| Looks like stock photography | No realism levers, everything lit evenly | Add three from the anti-AI kit, kill the fill light |

## Iterating without burning budget

1. Compose on a cheap model (`z_image`, `nano_banana`) at low resolution until the framing is
   right.
2. Move the working prompt to the quality model, **one frame**.
3. Only then batch variants — `generate_image_batch` + `jobs_wait` + one
   `show_generation_by_ids`.
4. Change **one slot at a time** between attempts. Changing three and getting a better result
   teaches you nothing about which one did it.
