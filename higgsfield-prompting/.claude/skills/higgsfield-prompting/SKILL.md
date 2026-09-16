---
name: higgsfield-prompting
description: Route a visual request to the right Higgsfield model or bundled workflow and write the prompt to house structure. Use whenever the user asks for an image, video, product shot, ad creative, thumbnail, UGC clip, or any generated visual through the Higgsfield connector — including "make me a product photo", "generate a video ad", "a bedside shot of the device", or any VeRelief Prime asset.
---

# Higgsfield prompting

Four gates, in order. Do not skip to the prompt.

## Gate 1 — Does a bundled workflow own this deliverable?

Higgsfield ships workflows that own whole categories. When one owns the ask, calling
`generate_image` / `generate_video` directly produces a worse result than the workflow would,
and the connector's own instructions require loading it first.

Call `get_workflow_instructions` **with no argument** to list the catalog, then load the match:

| Ask | Workflow |
|---|---|
| Product photography, packshot, hero banner, static ad pack, catalog image | `product-photoshoot` |
| UGC creator talking to camera | `ugc-review-video` |
| UGC, product only, voiceover, no creator on camera | `ugc-product-video` |
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

The catalog is the source of truth — check it rather than trusting this table, which is a
snapshot. If a workflow matches, load it and follow it; the rest of this skill still governs how
the prompt text inside it is written.

No workflow matches → Gate 2.

## Gate 2 — Pick the model

`references/model-routing.md`. The short version:

- **Realistic person / UGC frame** → `soul_2`
- **Legible on-image text or a diagram** → `nano_banana_pro`, `gpt_image_2_5`, or `openai_hazel`.
  Never a realism model.
- **Edit or restyle an existing image** → `seedream_v4_5`, `nano_banana_2`, `flux_kontext`
- **Cinematic still** → `soul_cinematic`, `cinematic_studio_2_5`
- **Cheap look-see before committing** → `z_image`, `nano_banana`
- **Product identity held across a clip** → `seedance_2_0` with the product as `image_references`
- **Cinematic clip** → `cinematic_studio_3_0`
- **Start frame → end frame** → `flux_3_video`, `minimax_h3`
- **Extend or edit an existing clip** → `seedance_2_5` with the matching `mode`

Verify before you rely on a parameter: `models_explore` with `action: "get"` and the `model_id`
returns that model's real aspect ratios, durations, and parameters. The roster changes.

## Gate 3 — Write the prompt to house structure

`references/prompt-anatomy.md`, and `references/templates.md` for a starting block.

Non-negotiable:

- **One subject, one action, one camera move per clip.** A second action needs a second clip.
- **Camera and light are named, not implied.** "Shot on a 35mm at chest height, window light
  from frame left" beats "nice lighting" every time.
- **Never describe a product in words when you can pass it as a reference image.** Words drift;
  references do not.
- **Never ask for cuts inside a single generation.** Generate the shots and assemble.
- **State the aspect ratio explicitly**, matched to the destination (9:16 paid social, 1:1 feed,
  16:9 site/YouTube).

## Gate 4 — VeRelief Prime / Hoolest work

Load `references/verelief-prompt-library.md` and apply the **product lock** and the **visual
compliance rules** before generating. The written claim rules in the brand brief
(`my-business` → `competitor-ad-swipe/references/verelief-prime-brief.md`) apply to on-screen
text and implied setting exactly as they apply to script copy — a clinic set and a white coat
make a medical claim without a single word being said.

## Running the generation

- Local or attached media with no confirmed `media_id` → call `media_upload_widget` as the only
  tool in that turn. Do not go looking in the filesystem for it.
- More than one independent generation of the same type → `generate_image_batch` /
  `generate_video_batch`, then `jobs_wait`, then a single `show_generation_by_ids`.
- Quote cost in USD from `run_cost` / `charged_cost` before spending on a batch.
- Generate **one** frame first, confirm it, then batch the variants. A batch of twelve wrong
  frames costs twelve times as much as one wrong frame.
