# Notion map

Exact destinations and property mappings. These IDs were read live from the workspace — if a
call rejects one, re-`fetch` the database rather than guessing a replacement.

## Databases

| What | ID |
|---|---|
| Video Brief (data source) | `collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f` |
| Video Brief page template | `3528fb5b-44b0-80d6-85c5-cfd2c41793df` |

Under **Hoolest Creative Lab**.

## Write target

**Video Brief only.** This skill does not create Ad Creative Pipeline rows — the team promotes
briefs into the pipeline themselves. The Pipeline data source
(`collection://9ed8fb5b-44b0-8214-ba3f-87e0b7d225f7`) is listed here only so it is recognisable,
not as a destination.

## Creative ID

Sequential house number, `HPT` + three digits, zero-padded. Not derived from the source ad.

```sql
SELECT "Creative ID" FROM "collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f"
WHERE "Creative ID" LIKE 'HPT%' ORDER BY "Creative ID" DESC LIMIT 5
```

Take the highest well-formed `HPT<nnn>` and add one. Ignore malformed entries — the database
contains a bare `HPT` and an `HPT0` that are not part of the sequence. Numbering is not strictly
dense (gaps and out-of-order creation dates exist); always go off the maximum, never off a count
of rows.

## Video Brief — property mapping

| Property | Value |
|---|---|
| `Concept Name` | title — a short descriptive name for the creative, house style, e.g. `Not Another Sleep Supplement`, `3 Signs Nervous System Never Shut Off`. **No em-dashes, no avatar suffix** — this string goes into filenames. |
| `Creative ID` | **`HPT<nnn>`** — next in sequence. Always set it. |
| `Category` | `Adaptation` (always — this is a competitor-derived brief) |
| `Product` | `VeRelief Prime` |
| `Format` | `VID` |
| `Status` | `Conceptualizing`, or `Brief In progress` if the script is complete |
| `Strategist` | `Mark` |
| `Avatar` | from analysis — `Wired Lifer` / `Sleep Struggler` / `HRV Hunter` / `Off-ramper` / `Multi` |
| `TEEP Stage` | `a - Trigger` / `b - Exploration` / `c - Evaluation` / `d - Purchase` (lowercase letters in this DB) |
| `Self Targeting` | `A - Actual Self` / `B - Ideal Self` / `C - Ought Self` |
| `Valence Zone` | Zone 1–4, matching the emotional register of the swiped ad |
| `Event` | `Evergreen` unless the source ad is clearly seasonal |
| `Offer` | `NA` unless the rewrite carries a specific offer |
| `Content Type` | short text, filename-safe — the framework used, e.g. `Why I Switched`, `AI VO`. Keep it to a few words with no parentheses. |
| Leave unset | `Editor`, `Assign`, `Performance`, `Winning version`, `Delivery link` |

## Video Brief page body

Mirror the existing template exactly. **The two naming tables at the very top are required** —
they carry the team's file-naming convention and the editor works from them. Never omit them.

### Naming convention

**Source of truth:** Mark's [Naming Convention Generator](https://docs.google.com/spreadsheets/d/1LqXRQXs4WyGptVOmvsk1JIH1UnfyBExIC2Ls-rtBhL8/edit),
"Video Naming Convention" tab. File id `1LqXRQXs4WyGptVOmvsk1JIH1UnfyBExIC2Ls-rtBhL8`.

**Generate the strings in that sheet each run** — see `references/naming-generator.md` for the
Zapier procedure. The format below is documentation; the sheet's output is the truth, and if
they ever disagree the sheet wins.

Its input columns, in order:

```
Creative ID, Format, Date, Concept name, Variation, Self Variation,
TEEP Stage, Valence Zone, Product, Content Type, Avatar, Offer,
Category, Strategist, Editor
```

Its three outputs:

```
File/Ad name  <CreativeID>_<Format>_<Concept>_<Var><Self><TEEP>-<Zone>_<Product>_<ContentType>_<Avatar>_<Offer>_<Category>_<Strategist>_<Editor>_<MMDDYY>
Batch name    <CreativeID>_<Concept>_<Product>_<ContentType>_<Avatar>_<Offer>_<Category>_<Strategist>_<Editor>
Folder name   <CreativeID>_<Concept>_<Product>
```

**The variant token is four separate fields, not two.** `1Ab-Z3` reads as:

| Part | From | Note |
|---|---|---|
| `1` | Variation | 1-indexed, one per hook variant |
| `A` | Self Targeting | letter only — `A - Actual Self` → `A` |
| `b` | **TEEP Stage** | letter only, lowercase for video — `b - Exploration` → `b` |
| `Z3` | Valence Zone | zone number |

Do **not** read `Ab` as an abbreviation of the self-targeting name. `A` and `b` are two
different properties jammed together, and TEEP Stage is easy to miss because it appears nowhere
else in the string. Getting this wrong produces a filename that looks plausible and sorts
wrongly.

Live example from the generator:

```
HPT085_VID_Test Zap_1Bd-Z3_VeRelief Prime_AI VO_Multi_NA_New_Mark_JM_082726
HPT085_Test Zap_VeRelief Prime_AI VO_Multi_NA_New_Mark_JM
HPT085_Test Zap_VeRelief Prime
```

Statics use the same shape with `IMG` and an uppercase TEEP letter
(`HPT047_IMG_Labor Day Sale Bundle_1bD-Z2_...`), so do not assume a fixed case — take the
letter as the sheet writes it for that format.

### Body structure


No source attribution block, no swipe analysis, no compliance table. The brief is for the
editor — everything in it should be something they can act on.

Page icon: **⚡** (template default, every brief).

```
<table>  ← Batch name / Folder name
File naming
<table>  ← one row per hook variant

### AD INSPO
<embed src="https://app.trendtrack.io/share/ads/<slug>"></embed>

### GENERAL INSTRUCTION
- Always apply the 1-3 sec rule (change visual every 1-3 sec)
- Avoid awkward moments, remove dead air on the audio

### GLOSSARY
TC = Time Clips · Super = Black text on white box · Caption = White text on black box

---
## Creative Brief Instruction

**HOOK**
| Visual | Copy/ Text Overlay | Note |

**BODY**
| Visual | Copy/ Text Overlay | Note |

**CTA**
| Visual | Copy/ Text Overlay | Note |
```

One table row per beat. The `Visual` column is what the editor shoots or cuts — write it as a
direction, not a description. The `Note` column carries pacing and delivery.

**AD INSPO is the share-link embed alone.** `create_ad_share_link(ad_id)` returns a `shareUrl`
like `https://app.trendtrack.io/share/ads/pulsetto-acWuuw`; put it in an `<embed>`. That is the
house convention — see HPT079. Do not add a video block, and never hotlink
`medias.trendtrack.io` directly.

Header rows are colour-coded: HOOK `green_bg`, BODY `orange_bg`, CTA `blue_bg`. Use `<br>` for
line breaks inside a cell, and `SUPER:` to prefix on-screen text.

The swipe analysis (source structure, angle, why it ran, what changed) still gets **done** — it
is what makes the rewrite good — but it goes in the chat report, not the page.
