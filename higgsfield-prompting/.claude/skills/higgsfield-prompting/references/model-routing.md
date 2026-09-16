# Model routing

A snapshot taken 2026-09-16 from `models_explore`. **Treat it as a map, not a spec sheet.** The
roster and the parameters move; before you depend on an aspect ratio, a duration, or a parameter
name, call:

```
models_explore { action: "get", model_id: "<id>" }
```

and use what comes back — especially `medias[].roles`, which is where routing mistakes actually
bite. `models_explore { action: "recommend", query: "...", input: "image" }`
is the fast path when nothing below obviously fits.

## Images

| Job | Model | Why |
|---|---|---|
| Realistic person, UGC, creator frame — **no product in hand** | `soul_2` | Built for UGC / editorial realism. Optional `soul_id` locks a recurring face. Up to 2k. **Takes one media at role `image` only — it has no `image_references` role, so it cannot hold a product photo.** |
| Person **plus** a product that must stay itself | `nano_banana_pro`, `seedream_v4_5`, `kling_omni_image`, `flux_2` | These take `image_references`. This is the row people get wrong — see the `soul_2` caveat above. |
| Cinematic still, concept art | `soul_cinematic`, `cinematic_studio_2_5` | Dramatic light and lensing. `cinematic_studio_2_5` goes to 4k. |
| **Legible on-image text**, diagrams, packaging copy | `nano_banana_pro`, `gpt_image_2_5`, `openai_hazel` | The only reliable text renderers. Realism models will hand you gibberish letterforms. |
| General photoreal, versatile | `nano_banana_2`, `kling_omni_image`, `flux_2` | Good defaults. `flux_2` has the tightest prompt adherence when the prompt is long and specific. |
| Edit / restyle an existing image | `seedream_v4_5`, `nano_banana_2` (`is_inpaint` + mask), `flux_kontext` | `seedream_v4_5` for precise transformation at 4k; `flux_kontext` for style transfer. |
| Expand a frame past its borders | `flux_2_pro_outpaint` | Per-side pixel expansion. Negative values crop instead. |
| Cheap look-see | `z_image`, `nano_banana` | Compose and test the idea before spending on a quality model. |
| DTC ad image with a brand kit | `ms_image` | **`style_id` is required** — call `show_marketing_studio` with `type='image_style'` and have the user pick first. Supports `brand_kit_id`, up to 4 `product_ids`, `batch_size` up to 20. |
| One-click product ad | `marketing_studio_image` | Lower ceremony than `ms_image`, no style pick. |
| Environment / background plate | `soul_location` | |
| Recurring character identity | `soul_cast`, or `soul_2` with a `soul_id` | |
| Don't know | `image_auto` | Routes by prompt intent. Fine for exploration, not for a deliverable. |

## Video

| Job | Model | Why |
|---|---|---|
| Cinematic clip, best quality | `cinematic_studio_3_0` | 4–15s, up to 4k, `genre` hint, optional `generate_audio`. |
| Cinematic with shot control | `cinematic_studio_video_v2` | `multi_shots` + `multi_prompt`, `speedramp`, `cfg_scale`, `preset_id`. 3–12s. |
| **Product identity held across the clip** | `seedance_2_0` | Reference-driven, built for product and multi-SKU. Pass the product as `image_references`. 4–15s, to 4k. |
| Edit / extend an existing clip | `seedance_2_5` | `mode`: `t2v`, `omni_reference`, `video_edit`, `video_extension`. 4–30s. |
| Start frame → end frame | `flux_3_video`, `minimax_h3`, `minimax_hailuo` | All take `start_image` + `end_image`. `flux_3_video` does 5–20s with synchronized audio. |
| Product / UGC ad, TikTok-Reels ready | `marketing_studio_video` | 12–15s. Composes from `hook_id` + `setting_id`, **or** from `ad_reference_id` — never both. `avatar_ids` and `product_ids` are not auto-pulled from an ad reference; pass them explicitly. |
| Viral template on a still | `higgsfield_preset` | `preset_id` from `presets_show`. Image-to-video only. |
| Natural physics and facial emotion | `minimax_hailuo` | 6 or 10s. |
| Stylized / experimental | `wan2_6` | |
| Many edited versions of one supplied ad | `ad_multiplier` | Load the `ad-multiplier` workflow first. |
| Lip-sync a clip to audio | `sync_so` | `sync_mode` decides how a duration mismatch is reconciled. |
| Upscale / finish | `topaz_video`, `bytedance_video_upscale` | Last step, after the cut is locked. |
| Drop the background | `video_background_remover` | |

### Genjutsu edits

Both route through `generate_video`, not the legacy `motion_control` tool:

- Copy / transfer movement from a driving video → `hf_mult_motion_control`
- Replace or swap an object in a source video → `hf_mult_replace_object`

## Media roles

Getting the role right matters more than the model choice in reference work:

| Role | Means |
|---|---|
| `image` / `start_image` | The first frame. The clip begins here. |
| `end_image` | The last frame. The model interpolates toward it. |
| `image_references` | "Keep this thing consistent" — identity, product, style. Not a frame. |
| `video_references` | Source clip for edit / extend / motion transfer. |
| `audio_references` | Drives timing or voice. |
| `mask` | Restricts the edit (`is_inpaint: true`). |

A product passed as `start_image` is a frame the model will move away from. The same product
passed as `image_references` is a constraint it holds. For product work you usually want the
second, or both.

## The id you ask for is not always the id that runs

A `nano_banana_pro` request came back as a completed `nano_banana_2` job on 2026-09-16. The
server re-routes. When the exact model matters — a text render, a 4k finish — read the `model`
field on the returned job rather than assuming, and re-run on an explicit id if it matters.

## Cost discipline

- `balance` and `show_plans_and_credits` before a large batch.
- `run_cost` / `charged_cost` are **USD**, not credits (`0.009` = $0.009). Quote USD.
- Resolution and quality tiers scale cost roughly linearly. Compose at 1k, finish at 4k.
- Reference point: one 2k 9:16 image on `nano_banana_pro` with one reference image cost
  **2 credits** (2026-09-16).
- On `insufficient_credits` / `BILLING_*`: stop. Do not retry — send the upgrade link from the
  error.
