# higgsfield-prompting

How Hoolest prompts Higgsfield. Model routing, prompt structure, reusable templates, and the
VeRelief Prime prompt library — everything needed to get a usable frame or clip on the first or
second generation instead of the sixth.

**The deliverable is a prompt, not a generation.** The skill hands back a copy-paste-ready block
plus the model and settings it was written for. It generates only when asked outright, and
quotes the cost first.

Higgsfield is reached through its **MCP connector**, not an HTTP API. Nothing here is a script;
it is the prompting layer a Claude session loads before it calls `generate_image` /
`generate_video`.

## Why this exists

Higgsfield exposes ~40 models and ~16 bundled workflows behind three generic tools. Most bad
output is not a model problem — it is one of four things:

1. **Wrong model.** Asking a realism model for legible on-image text. Asking a text-renderer for
   UGC skin.
2. **Wrong entry point.** Calling `generate_video` directly for a UGC ad when a bundled workflow
   owns that deliverable and would have produced a structured one.
3. **Overloaded prompt.** Three actions and two camera moves in a 5-second clip.
4. **No product lock.** The device drifts shape between frames because it was described in words
   rather than attached as a reference image — or because the prompt was written for a model
   that has no `image_references` role to attach it to.

Each of those has a rule in here.

## Files

| Path | What |
|---|---|
| `.claude/skills/higgsfield-prompting/SKILL.md` | The routing skill — load this first |
| `references/model-routing.md` | Which model for which job, and how to verify the roster is current |
| `references/prompt-anatomy.md` | Slot structure, camera/light vocabulary, realism levers, failure modes |
| `references/templates.md` | Fill-in-the-blank prompts per shot type |
| `references/verelief-prompt-library.md` | VeRelief Prime: product lock, visual compliance, ready prompts by avatar |

(`references/` sits under `.claude/skills/higgsfield-prompting/`.)

## Use it

```
/higgsfield-prompting a bedside shot of VeRelief Prime for the Sleep Struggler, 9:16
```

Or just have the skill loaded and ask for the asset in plain language — the skill routes.

## Required connector

**Higgsfield** must be enabled in the chat's connector settings. Everything else in here is
inert without it. Cost checks use `balance` / `show_plans_and_credits`; run costs are quoted in
USD before anything is generated.

## Related

Brand voice, approved claims, and the written compliance gate live in
`creativemaster1103/my-business` →
`.claude/skills/competitor-ad-swipe/references/verelief-prime-brief.md`. This repo covers the
*visual* side of the same rules and defers to that brief wherever they touch.
