# Filing an originated brief — what differs

The destination, the `HPT` numbering rule, the naming-table format, the page body structure and
the ⚡ icon are all shared with the competitor pipeline. **Read
`.claude/skills/competitor-ad-swipe/references/notion-map.md` for those** — it is the source of
truth and is not duplicated here.

This file carries only what an originated brief does differently, plus the property options as
read live from the workspace on **2026-09-11**.

---

## 1. `Category` is `New`, never `Adaptation`

The property has exactly two options: **`New`** and **`Iteration`**. Originated concepts are
`New`. A deliberate variation on an existing brief is `Iteration`, and the report says which
`HPT` number it varies.

> **Note for whoever maintains the sibling skill:** `notion-map.md` instructs
> "`Category` = `Adaptation` (always)". No such option exists on the property, and no row in the
> database carries that value — the 92 well-formed briefs are `New` 75, `Iteration` 12, unset 5.
> Whether a competitor-derived brief should be `New` or `Iteration` is Mark's call, so this skill
> does not change it. Do not copy `Adaptation` into an originated brief.

## 2. There is no AD INSPO embed

`AD INSPO` on a swiped brief is the TrendTrack share link for the source ad. An originated brief
has no source ad, so there is nothing to embed. **Omit the section.** Do not substitute a
competitor's ad to fill the space — that would make it a swipe, filed as if it were not.

The one exception: when a concept is deliberately anchored on one of **our own** winners found in
Motion, open with a `### REFERENCE` section naming that creative and what is being carried
forward (the hook mechanism, the pacing) in one line. Anything longer belongs in the chat report.

## 3. Set `Landing Page`

86 of 92 briefs leave it unset, which is why nobody can tell which concepts were built to sell
against which page. An originated concept is written toward a destination, so set it:

```
Fight-or-Flight Founder Story · Fight-or-Flight Listicle · Racing mind to Asleep
Stress to Control · Sleep Listicle · Home Page
```

Pick the page whose argument the script is setting up. If none fits, `Home Page` — but say so in
the report, because it usually means the concept has not decided what it is asking for.

## 4. Property options, verified live

| Property | Type | Options |
|---|---|---|
| `Concept Name` | title | House style. **No em-dashes, no avatar suffix** — it goes into filenames. |
| `Creative ID` | text | `HPT<nnn>`. Max was **`HPT091`** on 2026-09-11 — always re-derive, never assume. |
| `Category` | select | `New` · `Iteration` |
| `Product` | select | `VeRelief Prime` · `PEMF Mini Max` |
| `Format` | select | `VID` only |
| `Status` | status | `Conceptualizing` → `Brief In progress` → `Ready for Visuals` → `Need Revisions` → `Assigned to Editor` → `Ready to Upload` → `Uploaded to Drive` · `Failed to Upload` |
| `Avatar` | select | `Wired Lifer` · `Sleep Struggler` · `HRV Hunter` · **`Off-Ramper`** · `Multi` |
| `TEEP Stage` | select | `a - Trigger` · `b - Exploration` · `c - Evaluation` · `d - Purchase` |
| `Self Targeting` | select | `A - Actual Self` · `B - Ideal Self` · `C - Ought Self` |
| `Valence Zone` | select | see below — the full strings are long |
| `Event` | select | `Evergreen` · `BFCM` |
| `Offer` | select | `20OFF` · `NA` · `15%OFF` |
| `Content Type` | **text** | free text, not a select. Defaults to `AI VO`. |
| `Strategist` | select | `Mark` · `Nick` · `Ronak` |
| `Editor` | select | `JM` · `Jovanna` · `Diego` · `Ronak` · `Nick` |
| `Landing Page` | select | the six above |
| Leave unset | | `Assign`, `Performance`, `Winning version`, `Delivery link`, `🛣️ Ad Creative Pipeline` |

**`Avatar` is `Off-Ramper` with a capital R.** The brand brief writes it `Off-ramper`; the
database does not. Use the database's casing when setting the property.

**`Valence Zone` option names are the full strings**, not `Zone 3`:

```
Zone 1 — Cozy/Calm/Supportive (Positive + Low Intensity)
Zone 2 — Joy/Hype/Excitement (Positive + High Intensity)
Zone 3 — Frustration/Fatigue/Irritation (Negative + Low Intensity)
Zone 4 — Fear/Panic/Loss (Negative + High Intensity)
```

The filename token is just the number — `Z3`. Pick the zone the **hook** opens in, not the one
the ad resolves to; most of ours open in 3 and land in 1.

## 5. The naming sheet runs once per brief

`references/naming-generator.md` in the sibling skill has the full procedure and its two traps
(the date needs a leading apostrophe; empty strings do not clear cells). One thing it does not
spell out, which matters more here because this skill files several briefs in a run:

**Never batch two concepts into the sheet.** Output rows 20-24 hold at most five file names, and
the Batch name (row 29) and Folder name (row 30) cells hold exactly one brief's values. Two
concepts in the sheet at once produces one brief's batch name applied to both.

Per brief, in order: clear rows 6-16 → write rows 2-5, one per hook variant → read rows 20-24 and
29-30 → paste verbatim → move to the next concept and clear again.

## 6. `Status`

File at `Conceptualizing` if the script is a concept and hooks only. Use `Brief In progress` once
the Hook/Body/CTA tables are complete and an editor could work from the page — which, for this
skill, should be every brief. Originating and then filing a stub is just moving the work.
