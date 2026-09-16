# Notion map — UGC Brief Database

**Destination: the `🤳 UGC Brief Database` page.** Read live 2026-09-16.

| What | ID |
|---|---|
| `🤳 UGC Brief Database` (parent page) | `3448fb5b-44b0-80b7-a01f-df29eb7dd956` |
| `✏️ TEMPLATE` (copy this) | `3dc8fb5b-44b0-8025-920d-cdc4e9ac0903` |
| Path | Hoolest Creative Lab → … → UGC Brief Database |

## It is a page of child pages, not a database

This matters more than anything else on this page. The UGC Brief Database has **no Notion
properties at all** — no schema, no select options, no filters. Each brief is a plain child page
whose entire content is the body.

Everything the Video Brief pipeline does around properties therefore **does not apply here**:

| Video Brief convention | In the UGC Brief Database |
|---|---|
| `HPT<nnn>` Creative ID | **None.** No creative ID, no sequence to increment |
| `Avatar` / `TEEP Stage` / `Self Targeting` / `Valence Zone` properties | **None.** Still think them through — they decide how the script is written — but they are reported in chat, not filed |
| `Content Type` = `UGC` | **None.** The database is the content type |
| `Category`, `Status`, `Editor`, `Strategist`, `Offer` properties | **None.** `Offer` exists, but as a row in the header table |
| Naming-convention Google Sheet (`HPT085_VID_…`) | **Not used.** This database has its own creator-facing naming convention — see below |
| Page icon ⚡ | **✏️** |

**Do not file a UGC script in the Video Brief database**, and do not run the Zapier naming-sheet
procedure for one. Those belong to `/competitor-ad-swipe` and the AI-VO pipeline.

## Page title

Depends on the brief mode, which the skill establishes before anything else.

| Mode | Title |
|---|---|
| **Creator-specific** | `<Creator Name>-<Concept>` |
| **General** | `General-<Concept>` |

Live examples: `Hayden Bender-Fight-or-flight`, `Kenzie Williams-Fight-or-flight`,
`Lauren DeCicco-Fight-or-flight`, `Clayton Stakelbeck-Fight-or-flight`.

Hyphen, no spaces around it. Icon **✏️**, matching the template and every existing brief.

> **`General-` is a new convention.** Every existing brief is creator-named, so there is no
> precedent for an unassigned one. `General-<Concept>` keeps them sorting together and makes it
> obvious at a glance which briefs still need a creator. Flag it to Mark the first time one is
> filed rather than assuming it is settled.

**One page per creator.** Four creators shooting the same concept is four pages, which is exactly
what the existing four are. The concept name repeats; the creator name is what makes it unique.

**A general brief that later gets assigned is duplicated, not renamed** — the general version
stays available for the next creator.

## Page body — copy the template

Duplicate `✏️ TEMPLATE` and fill it. Do not rebuild the layout from scratch and do not reorder it
— the standing callouts are the team's instructions to creators and every brief carries them
identically.

Structure, in order:

```
<table header-column>   Content Creator · Product · Event · Inspo link · Offer
# Content Brief          standing paragraph
callout 🎥 gray_bg       Shooting Specifications — standing, do not edit
callout 💡 gray_bg       HOW TO UPLOAD CONTENT — standing, do not edit
# Storyboard / Shot List
## A-ROLL/SCRIPT
## A-Roll (TALKING HEAD)
### Script 1                ← Hooks, then Main Body
### Script 2                ← Hooks, then Main Body
## B-ROLLS | SHOTLIST       ← the 10 general clips
## File Naming Convention   standing, with the hook count corrected
```

### The header table

| Row | Fill with |
|---|---|
| `Content Creator` | **Creator-specific:** their name — the only row filled in on the existing briefs. **General:** `General — unassigned`, then a one-line casting spec on the same cell: `General — unassigned · cast: reads as a wired 30s founder, films at a real desk, low flat energy`. A general brief with no casting spec is unfinished, because nobody downstream knows who to book |
| `Product` | The product this brief is for. **The template and all four live briefs say `Hoolest Mini`** — confirm which product before filing rather than assuming VeRelief Prime |
| `Event` | `Launch` in the live briefs. `Evergreen` otherwise |
| `Inspo link` | A reference ad if the concept came from one. Leave empty otherwise |
| `Offer` | `20% OFF` in the live briefs. Pull the live offer from Shopify |

### Two scripts per page

**`Script 1` and `Script 2` are two sections of one brief page**, not two pages. The template ships
with both headings for exactly this reason: one creator, one shoot, two scripts.

Under each: `#### Hooks`, then `#### Main Body`. The two scripts must differ in framework and in
angle+avatar — see the skill.

### The shotlist is the clip bank

`B-ROLLS | SHOTLIST` is a three-column table, header row `orange_bg`:

| Shotlist | Visual description | INSPO |
|---|---|---|

**The template ships with 8 rows. We file 10** — the ten general clips, one per row. Extend the
table; the row count is not sacred, the ten clips are.

> **Each row needs a section NAME, not just a number.** The file-naming convention at the bottom
> of the page is `BRoll_<section>`, and *"the name of 'section' can be found in the Shotlist
> above"*. A numbered row with no name gives the creator nothing to name the file after. Put the
> name at the front of the `Visual description` cell — `**Struggle** — jaw set, shoulders up…`.
> The template's own examples are `BRoll_Struggle`, `BRoll_Frustration`,
> `BRoll_Physical discomfort`.

Section names for the standing ten are in `general-clips.md`.

## File naming — and the one fix the template needs

The naming block is creator-facing and stays as it is, **except for the hook count and script
scoping.**

The template reads:

```
Please film the 3 hooks separately to the body
- Talkinghead_hook1
- Talkinghead_hook2
- Talkinghead_hook3
```

Two problems once a page carries two scripts:

1. **`Talkinghead_hook1` is ambiguous.** Script 1's first hook and Script 2's first hook get the
   same filename. Scope it: **`Talkinghead_S1_hook1`** … **`Talkinghead_S2_hook3`**, plus
   `Talkinghead_S1_body` and `Talkinghead_S2_body`.
2. **The count must match what is actually written.** `hooks_per_script` in
   `config/ugc-scripting.yml` is **3**, matching this template. If that ever changes, the naming
   block changes with it — a brief asking for three hooks and listing four is how a creator
   delivers the wrong number of takes.

> **Flagged for Mark:** the Video Brief pipeline standardises on **four** hook variants per
> concept; this template asks for **three**. Both are defensible, but they should not disagree by
> accident. The UGC pipeline follows this template until told otherwise.

B-roll naming is unchanged: `BRoll_<section>`, one per shotlist row, ten of them.
