# Notion map

Exact destinations and property mappings. These IDs were read live from the workspace — if a
call rejects one, re-`fetch` the database rather than guessing a replacement.

## Databases

| What | ID |
|---|---|
| Video Brief (data source) | `collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f` |
| Ad Creative Pipeline (data source) | `collection://9ed8fb5b-44b0-8214-ba3f-87e0b7d225f7` |
| Video Brief page template | `3528fb5b-44b0-80d6-85c5-cfd2c41793df` |

Both live under **Hoolest Creative Lab**.

## Write order

Create the Video Brief first, then the Pipeline row, then relate them. The relation is
two-sided — setting it from the Pipeline row's `Video Brief` property is enough.

## Video Brief — property mapping

| Property | Value |
|---|---|
| `Concept Name` | title — `<Angle> — <Avatar>` e.g. `Failed Alternative — Off-ramper` |
| `Creative ID` | **`TT-<trendtrack_ad_id>`** — the dedupe key. Always set it. |
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

## Ad Creative Pipeline — property mapping

| Property | Value |
|---|---|
| `Ad Name` | title — same as the Video Brief `Concept Name` |
| `Video Brief` | relation → the page just created |
| `Product` | `VeRelief Prime` |
| `Status` | `💡 Idea` |
| `Medium` | `VID` |
| `Format` | `UGC` / `Talking Head` / `VSL` / `Mashup` — match the source ad's form |
| `Avatar`, `TEEP Stage`, `Valence Zone` | same values as the Video Brief |
| `Self-Concept Anchor` | `Actual Self (who they are now)` / `Ideal Self (…)` / `Ought Self (…)` |
| `Story Framework` | from analysis — `Problem-Agitate-Solve`, `Before-After-Bridge`, `SCQA`, … or `NA` |
| `Language Intensity` | `Low — Organic-feeling` or `High — Direct response` |
| `Emotion Present` | short text — the dominant emotion the ad works on |
| `Sprint Week` | the current week's Monday |
| Leave unset | `Owner`, `Worked?`, `CX Generation`, `Static Brief`, `Insight Bank` |

> Note the two databases spell the same concepts differently — `TEEP Stage` is
> `A - Trigger` in the Pipeline but `a - Trigger` in the Video Brief, and the Pipeline's
> `Self-Concept Anchor` options are worded differently from the Video Brief's `Self Targeting`.
> Use each database's own option strings exactly or the write silently drops the value.

## Video Brief page body

Mirror the existing template so editors read a familiar shape.

```
## Source
Competitor · Days running · TrendTrack ad ID + link · Swept on <date>
Compliance gate: passed <date>

### AD INSPO
<video src="competitor creative url">

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

## Structural analysis block

Append below the brief so the strategy is auditable later:

```
### Swipe analysis
- Source structure: <hook type → body blocks → CTA type>
- Primary angle: <angle>
- Person Blocks present: <list>
- Why it ran <N> days: <one sentence>
- What we changed and why: <one sentence>
```
