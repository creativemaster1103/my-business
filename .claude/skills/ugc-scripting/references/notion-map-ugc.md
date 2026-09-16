# Notion map — UGC deltas

Same database, same `HPT` sequence, same page icon as every other Video Brief. This file records
only what differs for a UGC script, plus the option values **read live from the workspace on
2026-09-16**.

Base map: `.claude/skills/competitor-ad-swipe/references/notion-map.md`. Everything not
contradicted below still applies.

| What | ID |
|---|---|
| Video Brief (data source) | `collection://34b8fb5b-44b0-8029-8b87-000b98d7a19f` |
| Video Brief page template | `3528fb5b-44b0-80d6-85c5-cfd2c41793df` |

## Property mapping — UGC

| Property | Value | Delta |
|---|---|---|
| `Concept Name` | title, house style, no em-dashes, no avatar suffix — it goes into filenames | — |
| `Creative ID` | `HPT<nnn>`, next in sequence | — |
| `Content Type` | **`UGC`** | **differs** — `AI VO` is the AI-voiceover default |
| `Category` | `New`, or `Iteration` when reworking an existing concept | **see the warning below** |
| `Product` | `VeRelief Prime` | — |
| `Format` | `VID` | — |
| `Status` | `Conceptualizing`, or `Brief In progress` once the script is complete | — |
| `Strategist` | `Mark` | — |
| `Editor` | `JM` | — |
| `Avatar` | `Wired Lifer` / `Sleep Struggler` / `HRV Hunter` / **`Off-Ramper`** / `Multi` | — |
| `TEEP Stage` | `a - Trigger` / `b - Exploration` / `c - Evaluation` / `d - Purchase` | — |
| `Self Targeting` | `A - Actual Self` / `B - Ideal Self` / `C - Ought Self` | — |
| `Valence Zone` | full option string — see below | — |
| `Landing Page` | set it — UGC points somewhere specific | **differs**: worth filling here |
| `Event` | `Evergreen` unless seasonal | — |
| `Offer` | `NA` / `20OFF` / `15%OFF` | — |
| Leave unset | `Assign`, `Performance`, `Winning version`, `Delivery link` | — |

## Values that bite

**`Category` has only two options: `New` and `Iteration`.** There is no `Adaptation` option in
this database, despite what the competitor-ad-swipe map says — that was verified against the live
schema and the swipe map is wrong on this one field. Writing an option that does not exist either
fails the call or silently adds a new option to the team's database. Use `New` for an original
UGC concept and `Iteration` for a rework of an existing one. **Raise the `Adaptation` discrepancy
with Mark rather than adding the option.**

**`Content Type` is a free-text property, not a select.** `UGC` needs no schema change, but
nothing validates it either — a typo lands silently and then propagates into every filename.
Write it exactly `UGC`.

**`Avatar` is `Off-Ramper`, with a capital R.** The brand brief and `config/competitors.yml`
both write `Off-ramper`. The Notion select option is `Off-Ramper`; that spelling wins for writes.

**`Valence Zone` options are the full descriptive strings**, not `Zone 1`:

```
Zone 1 — Cozy/Calm/Supportive (Positive + Low Intensity)
Zone 2 — Joy/Hype/Excitement (Positive + High Intensity)
Zone 3 — Frustration/Fatigue/Irritation (Negative + Low Intensity)
Zone 4 — Fear/Panic/Loss (Negative + High Intensity)
```

The naming sheet takes only the zone **number** (`Z3`). The Notion property takes the whole
string. They are the same field in two formats.

**`Format` has exactly one option, `VID`.** Statics do not live in this database.

**`Landing Page` options**, undocumented in the base map:

```
Fight-or-Flight Founder Story · Fight-or-Flight Listicle · Racing mind to Asleep
Stress to Control · Sleep Listicle · Home Page
```

**`Editor` options**: `JM`, `Jovanna`, `Diego`, `Ronak`, `Nick`. **`Strategist`**: `Mark`,
`Nick`, `Ronak`.

## Page body — UGC layout

Same top as every brief. The script tables are where it diverges: a creator is told what to
**say** and what to **do**, in that order, so `Spoken` leads.

```
<table>  ← Batch name / Folder name
File naming
<table>  ← one row per hook variant (four)

### CREATOR DIRECTION
Avatar · Location · Wardrobe · Camera · Energy · Disclosure · Must capture

### B-ROLL
- device in hand, close
- device applied, second angle
- the moment before, no device in frame
- hands doing something ordinary nearby

### GLOSSARY
Super = Black text on white box · Caption = White text on black box · VO = off-camera line

---
## Creative Brief Instruction

**HOOK ×4**
| Spoken | Shot / Action | Note |

**BODY**
| Spoken | Shot / Action | Note |

**CTA**
| Spoken | Shot / Action | Note |
```

Header rows keep the house colours: HOOK `green_bg`, BODY `orange_bg`, CTA `blue_bg`. `<br>` for
line breaks inside a cell, `SUPER:` to prefix on-screen text.

**The four hooks go in one HOOK table**, one row per variant, numbered to match the file-name
rows. Four hooks, four file rows, four takes — if those three numbers disagree the creator shoots
the wrong thing.

**No AD INSPO section** unless the script was built from a specific reference ad. There is no
TrendTrack share link for an original concept, and an empty heading is worse than none.

Page icon: **⚡**, template default, every brief.
