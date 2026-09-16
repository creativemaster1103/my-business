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

## Fill the pre-made pages — do not create new ones

**Mark keeps a pre-made page per content creator in this database.** They are copies of the
template with the creator's name already in the header, waiting for a script.

> **Fill those. Do not create a new page.** Standing instruction from Mark, 2026-09-16, and it
> holds for every batch from here on: the roster of pages is his, not something the pipeline
> grows. A new page is only ever created if Mark says there is no pre-made one for that creator.

At time of writing: `Hayden Bender`, `Lauren DeCicco`, `Clayton Stakelbeck`, `Kenzie Williams`,
all suffixed `-Fight-or-flight`. **Read the parent page each run** rather than trusting this list
— the roster changes, and Mark edits the pages live.

**Their headers are not identical.** Hayden's carries `Persona` and `Angle` rows the others do
not. Fill what is there; do not add rows to the pages that lack them, and do not strip rows from
the ones that have them. Read the page before editing it — a `content_updates` call fails whole
if one `old_str` does not match, which is the cheap way to find out a page has drifted.

**Keep their titles.** The concept in the title is Mark's. Do not rename a pre-made page to match
a concept you picked.

## Page title

For the rare case Mark asks for a new page. Depends on the brief mode, which the skill
establishes before anything else.

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

## Page body — the template, filled in

Duplicate `✏️ TEMPLATE` and fill it. **Do not rebuild the layout, do not re-order it, and do not
add blocks it does not have.** Every brief in this database should look like every other one.

The only two structural changes the work requires:

| Change | Why |
|---|---|
| Shotlist table **8 rows → 10** | Ten general clips |
| Naming block **3 hooks → 5**, scoped per script | Five hooks per script, two scripts per page |

Everything else is filled in, not altered. **Nothing else gets added** — no extra callouts, no
extra headings, no `Spoken / Shot / Note` tables. If direction feels like it needs its own block,
it does not: it goes inline in yellow, which is what the template already does.

Structure, exactly as it ships:

```
<table header-column>   Content Creator · Product · Event · Inspo link · Offer
# Content Brief          standing paragraph — verbatim
callout 🎥 gray_bg       Shooting Specifications — standing, verbatim
callout 💡 gray_bg       HOW TO UPLOAD CONTENT — standing, verbatim
# Storyboard / Shot List
## A-ROLL/SCRIPT         the two lines about yellow text — verbatim
## A-Roll (TALKING HEAD)
### Script 1
#### Hooks                 ← numbered list, 5 items
#### Main Body
---                        ← body script sits between the dividers
---
### Script 2               ← same again
## B-ROLLS | SHOTLIST      ← the two standing bullets, then the table (10 rows)
## File Naming Convention  ← standing, with the hook count corrected to 5
```

### Direction goes inline, in yellow

The template states its own convention at the top of the A-ROLL section:

> *"Talking head shots showing face and any gestures as noted in **yellow text**"*
> *"Only some parts of the A-roll will require holding the product this will be outlined in
> yellow text"*

So spoken lines are plain and **every direction is `<span color="yellow">…</span>` inline** —
what they do, where the phone goes, how to deliver it, and `HOLD THE PRODUCT` on the product
beats. `\[REQUIRES GENUINE USE\]` markers ride in yellow too.

This is the one to get right: the AI-VO pipeline's `Spoken / Shot / Note` cut-sheet table looks
like an upgrade and is not. It is a different database's format, and using it here makes a brief
that does not match the four already in the folder.

### The header table

| Row | Fill with |
|---|---|
| `Content Creator` | **Creator-specific:** their name — the only row filled in on the existing briefs. **General:** `General — unassigned`, then a one-line casting spec on the same cell: `General — unassigned · cast: reads as a wired 30s founder, films at a real desk, low flat energy`. A general brief with no casting spec is unfinished, because nobody downstream knows who to book |
| `Product` | The product this brief is for. **The template and all four live briefs say `Hoolest Mini`** — confirm which product before filing rather than assuming VeRelief Prime |
| `Event` | `Launch` in the live briefs. `Evergreen` otherwise |
| `Inspo link` | A reference ad if the concept came from one. Leave empty otherwise |
| `Offer` | `20% OFF` in the live briefs. **Shopify is on hold** — take this from the user or leave the template default. Never infer a discount |

### Two scripts per page

**`Script 1` and `Script 2` are two sections of one brief page**, not two pages. The template ships
with both headings for exactly this reason: one creator, one shoot, two scripts.

Under each: `#### Hooks`, then `#### Main Body`. The two scripts must differ in framework and in
angle+avatar — see the skill.

### The upload link — fill the `[LINK]` placeholder

The `💡 HOW TO UPLOAD CONTENT` callout ships with a `[LINK]` placeholder. **It gets filled**, and
that is the one edit the standing callouts take.

Procedure, every batch:

1. Check Dropbox **`Hoolest UGC - 2026`** (`ns:12062740723//Hoolest UGC - 2026`) for a folder
   named after the creator.
2. **Folder exists** → create a **Dropbox file request** pointing at that folder and put its URL
   in the callout.
3. **No folder** → **ask Mark** whether to create one for that creator. Do not create it yourself.

**Use a file request, not a shared link.** Two reasons, both learned here:

- The Dropbox MCP **cannot create public or edit-access shared links** — it is locked to
  view-only, audience `no_one`. Only the web UI can make an editor link.
- A folder edit-link would let every creator browse, edit and delete every other creator's raw
  footage. A file request gives them an upload URL into their own folder and nothing else. It is
  the right mechanism regardless of the tool limit.

> **`update_content` cannot reach text inside a callout.** Search-and-replace silently finds no
> match, however the string is escaped. To fill `[LINK]` you must use `replace_content` and
> rewrite the whole page. Budget for that rather than burning calls discovering it again.

Live file requests, created 2026-09-16:

| Creator | Upload URL |
|---|---|
| Hayden Bender | `https://www.dropbox.com/request/nmvu4q98u2axb3qxfzmn` |
| Clayton Stakelbeck | `https://www.dropbox.com/request/6oo8txkqa84dmbaek05h` |
| Kenzie Williams | `https://www.dropbox.com/request/1l6l8puxq3n2hr9w2hed` |

### The shotlist is the clip bank

`B-ROLLS | SHOTLIST` is a three-column table, header row `orange_bg`:

| Shotlist | Visual description | INSPO |
|---|---|---|

**The template ships with 8 rows. We file 10** — the ten general clips, one per row. Extend the
table; the row count is not sacred, the ten clips are.

**Each cell is an instruction the creator can act on alone with an iPhone**, and states whether
the phone is handheld or propped. There is no crew and no production shoot — see
`general-clips.md` for the execution rules every row obeys.

> **The `Shotlist` column holds the NAME, not a number.** `Device`, `Application`, `Struggle`,
> `Relief`… That column is what the creator names the file after — `BRoll_Struggle` — and the
> template says so: *"the name of 'section' can be found in the Shotlist above"*. A numbered row
> gives them nothing to name the file from.
>
> **Keep the description short.** One or two plain sentences: what to point the phone at, and
> whether to prop it. `Sit how you actually sit at 4pm — shoulders up, jaw tight. Do nothing for
> 8 seconds. Prop the phone.` A creator skims this on set; a paragraph does not get read.

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

Two things are wrong with it now:

1. **The count is three; we write five.** `hooks_per_script` is **5**. Rewrite the block on every
   brief to list five. A brief asking for three hooks while five are written is how a creator
   delivers the wrong number of takes.
2. **`Talkinghead_hook1` is ambiguous** once a page carries two scripts — Script 1's first hook
   and Script 2's first hook get the same filename.

So the block each brief carries is:

```
Please film the 5 hooks separately to the body, for each script
- Talkinghead_S1_hook1 … Talkinghead_S1_hook5
- Talkinghead_S1_body
- Talkinghead_S2_hook1 … Talkinghead_S2_hook5
- Talkinghead_S2_body
```

> **Flagged for Mark:** three conventions are now in play — this template's standing text says
> **three** hooks, the Video Brief pipeline uses **four**, and the UGC pipeline writes **five**.
> Five is what Mark asked for and what the pipeline follows; the template's standing text should
> be updated at source so the correction is not made by hand on every brief.

B-roll naming is unchanged: `BRoll_<section>`, one per shotlist row, ten of them.
