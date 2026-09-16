# Hoolest Mini — Will Burger B-roll, shots 1–7

Source: Notion → Hoolest Creative Lab / UGC Brief Database / **Will Burger-Fight-or-flight**
(fetched 2026-09-16). Product: **Hoolest Mini**. Persona: The Self-Rescuer (Panic & Acute
Anxiety), Solution-Aware. Angle: Fight-or-Flight.

Each shot is an **image prompt** (the still) and then a **video prompt** that animates that
still as `start_image`.

## Constraints taken from the brief

| Brief line | What it does to the prompt |
|---|---|
| "Film all content vertically, 9:16" | every aspect ratio is 9:16 |
| "do NOT add any FILTERS or COLOR GRADING" | **no grade slot.** `ungraded, straight off a phone camera, no filter` instead |
| "Must film in good lighting" | one clean daylight key, no moody underexposure |
| "Handheld" / "Prop the phone" | handheld = `handheld with slight drift`; propped = `locked off on a static phone` |
| "Hold each clip 6–8 seconds" | video durations set to 7–8s |
| "No voiceover on B-rolls" | `generate_audio: false` on every clip |
| "Avoid clothing with logos" | `plain unbranded` in the wardrobe slot |
| "keep medication and anything clinical-looking out of frame" | matches the library's visual compliance rules — nothing clinical anywhere |

## World lock

Paste this **byte-identical** into every prompt below. It is what makes seven separately
generated shots read as one afternoon in one room.

```
a man in his early thirties, short dark hair, light stubble, plain unbranded charcoal crew-neck
t-shirt, in a small home office with a pale oak desk against a white wall and a half-open window
with a sheer curtain at frame left, late-afternoon overcast daylight from that window,
ungraded, straight off a phone camera, no filter, visible skin texture, faint sensor noise
```

## Shot 0 — casting frame (not in the shotlist; generate it first)

The shotlist has no establishing shot, but shots 2–7 need the same person, wardrobe, and room.
Render one casting frame and attach it at `image_references` on every later shot.

**Model:** `soul_2` · **Aspect:** 9:16 · **Quality:** 2k
**Reference images:** none

```
A man in his early thirties, short dark hair, light stubble, plain unbranded charcoal crew-neck
t-shirt, sitting at a pale oak desk against a white wall, looking just off-lens, a small home
office with a half-open window and a sheer curtain at frame left, late-afternoon overcast
daylight from that window, 35mm at chest height, three-quarter front, ungraded, straight off a
phone camera, no filter, visible skin texture, fine flyaway hair, no beauty retouching, faint
sensor noise, 9:16
```

**Vary next:** wardrobe — charcoal reads flat against a white wall; a mid-grey marl holds more
texture under overcast light.

---

## Shot 1 — Product Intro · handheld

> *Brief: "Hold the Hoolest Mini in one hand over a plain table. Turn it over slowly. Handheld."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** Hoolest Mini product photo → `image_references`

```
Close on a man's open hand holding the small handheld device from the reference image, palm up,
over a bare pale oak table, forearm entering from the bottom of the frame, plain unbranded
charcoal sleeve at the wrist, 50mm close-up at hand height, shallow depth of field, soft
overcast daylight from a window at frame left with no fill, ungraded, straight off a phone
camera, no filter, visible skin texture on the hand, faint sensor noise, 9:16, device centred
with clean table above it
```

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 7s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 1 still → `start_image`; Hoolest Mini product photo →
`image_references`

```
The hand rotates the device slowly through a half turn to show its other face, handheld camera
with slight natural drift, the light holds, the shot ends with the device flat in the open palm
and still
```

**Vary next:** camera distance — pull to a wider hand-and-forearm frame if the device reads too
abstract at 50mm.

---

## Shot 2 — Product Demo · propped phone

> *Brief: "Use the Hoolest Mini just under your ear, face out of frame. Prop the phone."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** Hoolest Mini product photo + Shot 0 casting frame → `image_references`

```
A man framed from the jaw down — chin, jawline, neck and one shoulder only, face above the top
edge of frame — holding the small handheld device from the reference image against the side of
his neck just below the earlobe, plain unbranded charcoal crew-neck t-shirt, a pale oak desk and
white wall behind him, 50mm at neck height from three-quarter side, soft overcast daylight from
a window at frame left, ungraded, straight off a phone camera, no filter, visible skin texture
and stubble at the jaw, faint sensor noise, 9:16
```

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 8s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 2 still → `start_image`; Hoolest Mini product photo →
`image_references`

```
He presses the device gently into the skin below the ear and holds it there, the tendon in his
neck softens and his shoulder drops a little, locked off on a static propped phone with no
camera movement, the shot ends with the device still held in place and his shoulder settled
```

**Vary next:** the head angle — if the jaw crops awkwardly, tilt him slightly away from lens so
the placement under the ear reads clearly.

---

## Shot 3 — Product Feature · handheld

> *Brief: "Reach into a bag on the table and pull the Hoolest Mini out. One motion. Handheld."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** Hoolest Mini product photo → `image_references`

```
A man's hand reaching into the open mouth of a plain unbranded canvas tote bag slumped on a pale
oak desk, the small handheld device from the reference image just visible inside among a
notebook and keys, plain unbranded charcoal sleeve at the wrist, 35mm at desk height angled
down, soft overcast daylight from a window at frame left, ungraded, straight off a phone camera,
no filter, visible weave in the canvas, faint sensor noise, 9:16
```

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 7s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 3 still → `start_image`; Hoolest Mini product photo →
`image_references`

```
The hand closes around the device and lifts it out of the bag in one unbroken motion, handheld
camera with slight natural drift following the hand up, the shot ends with the device held clear
of the bag in the open palm
```

**Vary next:** environment — swap the tote for a jacket pocket if the bag interior renders as
mush.

---

## Shot 4 — Person Problem · propped phone

> *Brief: "Sit how you actually sit at 4pm — shoulders up, jaw tight. Do nothing for 8 seconds.
> No device in frame. Prop the phone."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** Shot 0 casting frame → `image_references`

```
The man from the reference image sitting at a pale oak desk in a plain unbranded charcoal
crew-neck t-shirt, shoulders raised toward his ears, jaw set, staring past a half-open laptop at
nothing, a white wall behind him and a half-open window with a sheer curtain at frame left,
mid-shot, 35mm at chest height from three-quarter front, late-afternoon overcast daylight from
the window with no fill, ungraded, straight off a phone camera, no filter, visible skin texture,
no beauty retouching, faint sensor noise, 9:16
```

No device anywhere in frame. Nothing clinical, no medication, no mug of pills on the desk.

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 8s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 4 still → `start_image`

```
Almost nothing happens: he holds the same tight posture, his jaw flexes once, he blinks slowly
and his eyes stay unfocused, no gesture and no change of expression, locked off on a static
propped phone with no camera movement, the shot ends exactly as it began with his shoulders
still raised
```

**Vary next:** nothing in the prompt — this shot lives or dies on how little the model invents.
If it adds a gesture, shorten to 6s before you touch the wording.

**Alternative model:** `minimax_hailuo` at 6s — its facial micro-emotion is stronger, at the cost
of the 8-second hold the brief asks for.

---

## Shot 5 — Person Failed Alternative · handheld

> *Brief: "Point the phone at what you tried before — cold tea, a meditation app, a yoga mat.
> Handheld."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** none

```
A corner of a pale oak desk seen from above at a slight angle: a mug of cold tea with a dull film
on the surface, a phone lying face-up beside it showing a plain circular breathing timer on a
dark screen with no readable words or brand marks, and a rolled yoga mat leaning against the
white wall behind, 35mm angled down from standing height, soft overcast daylight from a window at
frame left, ungraded, straight off a phone camera, no filter, dust visible on the desk, faint
sensor noise, 9:16
```

Deliberately no logos and no readable app name — a recognisable third-party UI in a paid ad is a
problem the shot does not need.

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 7s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 5 still → `start_image`

```
The camera drifts slowly across the desk from the cold tea to the phone to the rolled mat,
handheld with slight natural shake, nothing in the scene moves, the shot ends resting on the
rolled yoga mat
```

**Vary next:** the prop set — a stale glass of water and a foam roller if the tea and mat read
too styled.

---

## Shot 6 — Person Desired Result · propped phone

> *Brief: "Same setup as Person Problem. Let one long breath out, shoulders drop. Prop the
> phone."*

### Image

**Reuse the Shot 4 still.** "Same setup" means the framing must match, and the cheapest way to
guarantee that is to feed Shot 4's render straight in as `start_image` rather than generate a
near-identical second frame. If you do want a separate still, run the Shot 4 image prompt again
unchanged.

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 8s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the **Shot 4** still → `start_image`

```
He lets one long breath out, his shoulders drop away from his ears, his jaw unclenches and his
eyes close for a beat before opening softly, locked off on a static propped phone with no camera
movement, the shot ends with his shoulders low and his face settled
```

**Vary next:** duration — 8s gives the exhale room, but if the model fills the tail with a second
gesture, drop to 6s.

**Alternative model:** `minimax_hailuo` at 6s — this is the one shot where facial micro-emotion
is the whole point.

---

## Shot 7 — Person Before & After · propped phone

> *Brief: "Walk back to the desk or get into bed, settled. No device in frame. Prop the phone."*

### Image

**Model:** `nano_banana_pro` · **Aspect:** 9:16 · **Resolution:** 2k
**Reference images:** Shot 0 casting frame → `image_references`

```
Wide of the same small home office: the man from the reference image stepping back into the room
toward an empty desk chair, one hand on the back of the chair, relaxed shoulders and an easy
posture, pale oak desk against a white wall, half-open window with a sheer curtain at frame left,
24mm wide at chest height, deep focus, late-afternoon overcast daylight from the window,
ungraded, straight off a phone camera, no filter, unstyled room, faint sensor noise, 9:16
```

### Video

**Model:** `seedance_2_0` · **Aspect:** 9:16 · **Duration:** 8s · **Resolution:** 1080p ·
`generate_audio: false`
**Reference images:** the Shot 7 still → `start_image`

```
He steps forward, pulls the chair out, sits down and settles into it without hurry, locked off on
a static propped phone with no camera movement, the shot ends with him seated and still, facing
the desk
```

**Vary next:** the action — the brief offers "or get into bed" as an alternative; the bedroom
version reads warmer and needs a second world lock.

---

## Open item — the product reference

Shots 1, 2 and 3 are blocked on a real **Hoolest Mini** photo. Shopify has no product under that
name: the closest record is **VeRelief Mini** ($199.95), which is ARCHIVED, and the brief calls
the Mini Hoolest's "newest" stimulator — so it may be a new device rather than a rename.

Do not generate 1–3 until that is settled. A guessed device in a launch ad is worse than no
B-roll, and the library's product lock forbids inventing form factors, logos, or buttons.
Shots 4–7 have no product in frame and can run now.
