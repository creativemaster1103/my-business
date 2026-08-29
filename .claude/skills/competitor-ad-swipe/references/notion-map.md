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
| `Concept Name` | title — `<Angle> — <Avatar>` e.g. `Failed Alternative — Off-ramper` |
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
| `Content Type` | short text — the UGC framework used, e.g. `Why I Switched` |
| Leave unset | `Editor`, `Assign`, `Performance`, `Winning version`, `Delivery link` |

## Video Brief page body

Mirror the existing template so editors read a familiar shape.

No source attribution block, no swipe analysis, no compliance table. The brief is for the
editor — everything in it should be something they can act on.

```
### AD INSPO
<video src="https://medias.trendtrack.io/video/facebook/<id>.mp4"></video>

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

Use the `media.mediaUrl` from the scaling-ads response for the AD INSPO embed — the `<video>`
tag makes it preview inline. `thumbnailUrl` is the fallback when there is no media URL.

The swipe analysis (source structure, angle, why it ran, what changed) still gets **done** — it
is what makes the rewrite good — but it goes in the chat report, not the page.
