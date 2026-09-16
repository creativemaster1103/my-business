# Templates

Fill the brackets. Delete nothing — if a slot is genuinely irrelevant, cut it deliberately rather
than leaving it blank. Every template assumes the rules in `prompt-anatomy.md`.

---

## T1 — Studio packshot

**Model:** `cinematic_studio_2_5` or `nano_banana_pro` · **Media:** product photo as
`image_references`

```
[PRODUCT], centred on a [SURFACE / seamless backdrop] in [COLOUR],
85mm macro on a static tripod at product height,
[single soft key from camera left with a subtle rim from behind / broad even softbox],
[PALETTE] palette, gentle falloff to the backdrop edges,
crisp material detail on [MATERIAL], no dust, no fingerprints,
[RATIO], generous negative space [WHERE]
```

---

## T2 — Lifestyle product still

**Model:** `soul_2` (person in frame) or `cinematic_studio_2_5` (no person) · **Media:** product
as `image_references`

```
[PERSON, age and specific wardrobe] [ACTION with the product],
in [ROOM with two concrete props],
35mm at chest height, three-quarter front, shallow depth of field,
[LIGHT: source, direction, quality, temperature],
[PALETTE], low contrast,
visible skin texture, imperfect framing, faint sensor grain,
[RATIO], clean [UPPER THIRD / LEFT THIRD] for copy
```

---

## T3 — UGC frame (phone-shot look)

**Model:** `soul_2` · optional `soul_id` to hold the face across a set

```
[PERSON] holding a front-facing phone at arm's length, [EXPRESSION], [ACTION],
in [EVERYDAY LOCATION — a real one, unstyled],
front-facing phone camera, slight lens distortion, eye level, vertical,
[available light: window / overhead domestic / car window],
slightly blown highlights, no colour grade,
visible pores, flyaway hair, no beauty retouching,
9:16
```

---

## T4 — Hero banner with room for type

**Model:** `nano_banana_pro` (text on frame) or `cinematic_studio_2_5` (type set later)

```
[SUBJECT] [ACTION], [ENVIRONMENT],
24mm wide, low angle, deep focus,
[LIGHT],
[PALETTE] with [ACCENT COLOUR] as the only saturated element,
16:9, subject in the right third, clean uncluttered left half for headline text
```

Rendering the headline on the frame: append
`headline text reading "[EXACT COPY]" in a clean grotesque sans, [COLOUR], upper left` — and
only on a text-rendering model.

---

## T5 — Single-beat video clip

**Model:** `seedance_2_0` (product must hold) / `cinematic_studio_3_0` (cinematic) ·
**Media:** product as `image_references`, opening frame as `start_image`

```
[SUBJECT] [ONE ACTION, present participle], in [ENVIRONMENT],
[ONE CAMERA MOVE: slow push in / locked off with faint handheld breathing / slow orbit right],
[LIGHT],
[PALETTE],
the shot ends on [END STATE],
[DURATION]s, [RATIO], audio [on: what it is / off]
```

---

## T6 — Start frame → end frame

**Model:** `flux_3_video` or `minimax_h3` · **Media:** `start_image` + `end_image`

```
Begins on [WHAT IS IN THE START FRAME]. [WHAT CHANGES, one transformation].
Ends on [WHAT IS IN THE END FRAME].
[ONE CAMERA MOVE], [LIGHT holds / shifts to X],
[DURATION]s, [RATIO]
```

The two frames do the heavy lifting. Keep the prompt to the transition between them — do not
re-describe what the images already show.

---

## T7 — Talking-head opener (hook frame)

**Model:** `soul_2` for the frame, then the `ugc-review-video` workflow for the clip

```
[PERSON] mid-sentence looking straight into the lens, [EXPRESSION — specific, not "happy"],
[LOCATION], [ONE PROP that says what this is about],
front-facing phone camera at arm's length, eye level,
[LIGHT],
natural, ungraded,
visible skin texture, slightly off-centre framing,
9:16, head in the upper middle, clean space at the bottom for captions
```

---

## T8 — Variant sweep

One slot varies, everything else is byte-identical. This is how you learn what a slot does, and
how you get a usable test set for paid social.

```
BASE = [a working prompt from above]
VARY = [exactly one slot: environment | light | wardrobe | camera distance | palette]
```

Run with `generate_image_batch` / `generate_video_batch` → `jobs_wait` → one
`show_generation_by_ids`. Confirm the base on a single generation first.
