---
name: higgsfield-prompting
description: Craft a Higgsfield prompt — pick the model the prompt is written for, write it to house structure, and hand back a copy-paste-ready block. Use whenever the user wants a prompt for an image, video, product shot, ad creative, thumbnail, UGC clip, or any VeRelief Prime visual. The deliverable is the prompt, not a generation.
---

# Higgsfield prompting

**The deliverable is a prompt.** Write it, hand it over, stop. Do not call `generate_image` /
`generate_video` unless the user asks for a generation in so many words — and even then, quote
the cost first.

Four gates, in order.

## Gate 1 — Which model is this prompt written for?

A prompt is not model-agnostic. Reference roles, aspect ratios, durations, and how much
prose the model will actually read all differ. Pick the model before writing a word, and name it
in the output. `references/model-routing.md` has the full table; the short version:

- **Realistic person, UGC, no product in hand** → `soul_2`
- **Person *and* a product that must stay itself** → `nano_banana_pro`, `seedream_v4_5`,
  `kling_omni_image`, or `flux_2`. **Not `soul_2`** — it takes a single media at role `image`
  and has no `image_references` role, so it cannot hold a product photo. (Confirmed against
  `models_explore action:"get"`, 2026-09-16.)
- **Legible on-image text or a diagram** → `nano_banana_pro`, `gpt_image_2_5`, `openai_hazel`
- **Edit or restyle an existing image** → `seedream_v4_5`, `nano_banana_2`, `flux_kontext`
- **Cinematic still** → `soul_cinematic`, `cinematic_studio_2_5`
- **Product identity held across a clip** → `seedance_2_0`, product as `image_references`
- **Cinematic clip** → `cinematic_studio_3_0`
- **Start frame → end frame** → `flux_3_video`, `minimax_h3`
- **Extend or edit an existing clip** → `seedance_2_5` with the matching `mode`

Verify anything you are about to put in the settings line:
`models_explore { action: "get", model_id: "<id>" }` returns that model's real aspect ratios,
durations, parameters, and media roles. The roster moves.

## Gate 2 — Does a bundled workflow own this deliverable?

Some deliverables are owned by a Higgsfield workflow that carries its own prompt architecture —
a hand-written prompt is the wrong shape for them. Call `get_workflow_instructions` with **no
argument** to list the catalog, then load the match and write inside its structure:

| Ask | Workflow |
|---|---|
| Product photography, packshot, hero banner, static ad pack | `product-photoshoot` |
| UGC creator talking to camera | `ugc-review-video` |
| UGC, product only, no creator on camera | `ugc-product-video` |
| Unboxing / first reaction | `ugc-unboxing-video` |
| Step-by-step how-to with on-screen steps | `ugc-tutorial-video` |
| Wearing / fit check | `ugc-try-on-video` |
| The website or product page shown on screen | `ugc-website-video` |
| Many edited versions of one supplied 4–30s ad | `ad-multiplier` |
| YouTube / Instagram thumbnail or cover | `thumbnail-generation` |
| Logo, brand kit, packaging, merch, branded deck | `brand-asset-creation` |
| Narrated explainer / faceless channel video | `faceless-video` |
| Consistent character across views | `character-sheet` |
| Burned-in captions on a finished cut | `subtitles` |

The catalog is the source of truth — this table is a dated snapshot.

## Gate 3 — Write it

`references/prompt-anatomy.md` for the slot structure and vocabulary,
`references/templates.md` for a starting block.

Non-negotiable:

- **One subject, one action, one camera move per clip.** A second action is a second prompt.
- **Camera and light are named, not implied.** "35mm at chest height, window light from frame
  left, no fill" beats "nice lighting" every time.
- **A product that must stay itself is a reference image, not a sentence.** Say so in the
  settings line rather than describing the product in prose.
- **Never ask for a cut inside one generation.** One prompt is one continuous shot.
- **State the aspect ratio**, matched to the destination (9:16 paid social, 1:1 feed, 16:9 site).
- **No quality adjectives.** `8k`, `masterpiece`, `award-winning` do nothing but dilute the
  tokens that work.

## Gate 4 — VeRelief Prime / Hoolest work

Load `references/verelief-prompt-library.md` and apply the **product lock** and **visual
compliance rules**. The written claim rules in the brand brief (`my-business` →
`competitor-ad-swipe/references/verelief-prime-brief.md`) govern on-screen text and implied
setting exactly as they govern script copy — a clinic set and a white coat make a medical claim
without a word being said.

## Output contract

Hand back exactly this, nothing padded around it:

````
**Model:** <id>  ·  **Aspect:** <ratio>  ·  **Resolution:** <tier>
**Reference images:** <what to attach, at which role — or "none">

```
<the prompt, ready to paste>
```

**Vary next:** <the one slot worth changing if this misses>
````

Then say in one line what you would change first if it comes back wrong. Do not narrate the slot
structure back at the user — they have this file.

## If the user does ask you to generate

Only then:

1. `get_cost: true` first, and quote the number before spending.
2. Local or attached media with no confirmed `media_id` → `media_upload_widget`, as the only
   tool in that turn. Do not go hunting in the filesystem.
3. One generation, confirmed, *then* batch variants — `generate_image_batch` /
   `generate_video_batch` → `jobs_wait` → a single `show_generation_by_ids`.
4. Check the model the job reports back. A requested id is not always the id that runs
   (a `nano_banana_pro` request came back as `nano_banana_2` on 2026-09-16).
