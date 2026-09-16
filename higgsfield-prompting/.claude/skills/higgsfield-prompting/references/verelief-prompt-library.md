# VeRelief Prime — prompt library

Everything Hoolest-specific. The written rules — voice, approved claims, the compliance gate —
live in `creativemaster1103/my-business` →
`.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md`. This file is the visual
half of the same discipline and defers to that brief wherever the two touch.

## 1. Product lock

**Never describe the device in words when a photograph is available.** Pull the current product
image from Shopify (or the Marketing Studio product record) and pass it as `image_references` on
every generation the device appears in. For video, that means `seedance_2_0` — it is the model
that holds a product identity across a clip.

Words drift. A word-described device is a different device in frame two, and an ad with an
inconsistent product is unusable no matter how good the light is.

When a photograph genuinely is not available — a concept frame, a silhouette, a shot where the
device is out of focus in the background — this is the only permitted verbal description:

> a small matte handheld device, palm-sized, held like a remote, with a rounded contact tip
> pressed to the side of the neck

Do not add colours, screens, logos, buttons, or brand marks from imagination. A hallucinated
logo on our own product is worse than no product in frame.

## 2. Visual compliance

The brief's compliance gate is written for script copy. It applies identically to what the frame
*shows*, because a set dresses a claim without a word being said.

**Do not generate:**

- Clinical or hospital settings — exam tables, curtained bays, monitors, EKG traces, IV poles.
- A person in a white coat, scrubs, a stethoscope, or anything reading as a clinician
  administering the device.
- Pill bottles, blister packs, or prescription labels being pushed aside, refused, or replaced.
  That is the "replaces a medication" claim, staged.
- Alcohol being poured away or a wine glass set down as the device comes out. Same claim,
  different substance. (The Off-ramper angle lives in *copy*, not in a staged renunciation.)
- Anatomical overlays, nerve-pathway diagrams, glowing neural graphics, or brain imagery
  implying a demonstrated mechanism of action.
- On-frame text containing a numeric outcome (`83%`, `-40% cortisol`, `HRV +12`), `clinically
  proven`, `FDA approved`, or any named condition — anxiety, insomnia, PTSD, migraine, POTS.
- Literal before/after panels of a *person's state*. Before/after of a **situation** — a cluttered
  desk at 3pm vs. the same desk, same person, two minutes later — carries the feeling without
  making a treatment claim. Use that instead.

**Do generate:**

- Real domestic and work settings — a home office, a kitchen at night, a car before a meeting,
  a bedside table.
- The device in the person's own hand, self-applied. Always self-applied.
- Wellness-register calm: shoulders dropping, a slow exhale, eyes closing for a beat.
- Gel tips visible as a consumable — the repeat-purchase story is a legitimate visual.

> **Open item, same as the brief:** the regulatory posture of VeRelief Prime (general wellness
> device vs. an FDA clearance and its indication) is unconfirmed. These visual rules are written
> conservatively on that basis. Do not widen them on inference — have Mark confirm the status
> first, then update this section and the brief together.

## 3. House look

One recognisable frame, across every avatar:

- **Palette:** muted, desaturated, warm skin against cool environment. One accent colour at most.
- **Light:** soft and directional, usually a window. Low fill, real falloff. Never flat and
  even; never dramatic beauty light.
- **Lens:** 35mm at chest height for lifestyle, 50mm close for the hand-on-neck moment, phone
  camera for UGC.
- **Register:** the grown-up in a hype category. No grinning, no arms-out relief, no lens flares,
  no glow.

## 4. Prompts by avatar

Each is a starting block, not a finished prompt. Pass the product photo as `image_references`,
set the aspect ratio for the placement, and add realism levers from `prompt-anatomy.md`.

### Wired Lifer — "tired but wired", relief in seconds, mid-day

**Model:** `soul_2` · 9:16

```
A man in his late thirties in a plain charcoal t-shirt, pressing the handheld device to the
side of his neck with his eyes half-closed, at a home office desk with an open laptop, a second
monitor, and a cold coffee, mid-afternoon,
35mm at chest height, three-quarter front, shallow depth of field,
hard overcast window light from frame left, no fill,
muted desaturated palette, warm skin against a cool grey room,
visible skin texture, slightly off-centre framing, faint sensor grain,
9:16, clean upper third for headline text
```

Clip version — **`seedance_2_0`, 5s**: `...lifting the device to his neck and letting his
shoulders drop on the exhale, locked off with faint handheld breathing, the shot ends on his
eyes closed and his jaw unclenched, audio off`

### Off-ramper — drug-free, non-habit-forming, in your control

**Model:** `soul_2` · 4:5 or 9:16

```
A woman in her forties in a linen shirt, sitting on the edge of a sofa holding the handheld
device in both hands and looking at it, an ordinary living room at dusk with a single lamp on,
50mm, eye level, close-up, shallow depth of field,
one warm practical lamp behind her at 2700K, hard rim, deep falloff,
muted palette, warm pool of light in a cool room,
visible pores, no beauty retouching, natural asymmetry,
4:5
```

Nothing is being renounced in frame. No bottles, no glass, no ashtray — the angle is in the
copy.

### Sleep Struggler — wind-down ritual, no morning hangover

**Model:** `soul_2` · 9:16

```
A woman in her thirties in a grey sleep tee, sitting on the edge of the bed pressing the
handheld device to the side of her neck, a dim bedroom with a bedside lamp, a paperback, and a
phone face-down,
35mm at chest height, three-quarter back so the room reads,
single warm bedside lamp at 2700K, everything else falling to black,
deep shadows, warm amber against blue-black,
visible skin texture, slight motion blur on the hand,
9:16, clean space above her for headline text
```

### HRV Hunter — mechanism, measurable, stackable

**Model:** `soul_2` · 1:1 or 16:9

```
A man in his early thirties in technical fabric, the handheld device in one hand and a wrist
wearable visible on the other, at a clean but lived-in desk with a notebook of handwritten
numbers, early morning,
35mm, eye level, three-quarter front,
cool north-facing window light from frame right, one-stop fill,
neutral desaturated palette, one accent colour,
visible skin texture, unstyled desk,
1:1
```

No screens showing readouts, no graphs, no arrows. The wearable establishes the person; a
displayed number would be a claim.

## 5. Recurring assets

| Asset | Route |
|---|---|
| PDP packshot, gel tips, in-box | `product-photoshoot` workflow → T1 |
| Static ad pack for Meta | `ms_image` (pick `style_id` via `show_marketing_studio`) or T2 + T4 |
| UGC creator video | `ugc-review-video` workflow, house look above |
| Product-only video ad, voiceover | `ugc-product-video` workflow |
| Variants of an ad that already works | `ad-multiplier` workflow |
| Hero banner for the site | T4 on `nano_banana_pro`, 16:9 |

## 6. Before anything ships

1. Product lock applied — real photo as `image_references`, no invented logo or mark.
2. Nothing on the visual don't-list is in frame.
3. Any on-frame text passes the brief's written compliance gate, and the price, if shown, came
   from Shopify at run time.
4. The device is self-applied, in the person's own hand.
5. Aspect ratio matches the placement it was made for.
