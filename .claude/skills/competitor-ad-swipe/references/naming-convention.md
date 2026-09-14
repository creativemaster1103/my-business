# Naming convention

Every file name is built **from the brief's own Notion properties**. Nothing else is needed —
no spreadsheet, no Zapier, no Google Sheets connector.

> Superseded 2026-09-14. This file previously documented a Zapier → Google Sheets procedure
> against Mark's Naming Convention Generator. That sheet is no longer the source of truth and
> must not be used: it emits a different, now-wrong format. Build the strings here instead.

## The three strings

```
Batch name
[Creative ID]_[Format]_[Concept name]_[Product]_[Content Type]_[Persona]_[Offer]_[Category]_[Strategist]_[Editor]_[Date]

Folder name
[Creative ID]_[Concept name]_[Product]

File / Ad name
[Creative ID]_[Format]_[Concept name]_[Variant+Awareness]_[Product]_[Content Type]_[Persona]_[Offer]_[Category]_[Strategist]_[Editor]_[Landing Page]_[Date]
```

Worked example — HPT089, hook variant 1, Problem Aware:

```
HPT089_VID_Twenty Two Years Running Hot_VeRelief Prime_AI VO_Wired Lifer_NA_New_Mark_JM_091426
HPT089_Twenty Two Years Running Hot_VeRelief Prime
HPT089_VID_Twenty Two Years Running Hot_1B_VeRelief Prime_AI VO_Wired Lifer_NA_New_Mark_JM_Stress to Control_091426
```

## Where each part comes from

| Token | Notion property | Note |
|---|---|---|
| Creative ID | `Creative ID` | `HPT<nnn>` |
| Format | `Format` | `VID` |
| Concept name | `Concept Name` | No em-dashes, no avatar suffix — it goes into the filename verbatim |
| **Variant+Awareness** | hook number + **awareness level** | see below |
| Product | `Product` | `VeRelief Prime` / `PEMF Mini Max` |
| Content Type | `Content Type` | defaults `AI VO` |
| Persona | `Avatar` | the persona, e.g. `Wired Lifer` |
| Offer | `Offer` | `NA` unless the script carries one |
| Category | `Category` | `New` / `Iteration` |
| Strategist | `Strategist` | defaults `Mark` |
| Editor | `Editor` | defaults `JM` |
| Landing Page | `Landing Page` | **file name only** — not in the batch name |
| Date | — | `MMDDYY`, the date the brief is written |

## The variant token

A number and a letter, e.g. `1B`.

**Number = hook variant.** 1–4, one per hook. Four hooks, four file rows, always.

**Letter = awareness level of the brief:**

| Letter | Awareness |
|---|---|
| `A` | Unaware |
| `B` | Problem Aware |
| `C` | Solution Aware |
| `D` | Product Aware |
| `E` | Most Aware |

So `1C` is hook variant 1 of a Solution Aware brief. **All four hooks on a brief carry the same
letter** — a brief sits at one awareness level, and every hook must be written for it.

This is the whole reason the token exists: you can read a file's awareness level off its name
and check whether the hook actually matches. A `B` file whose hook mentions the product is
mislabelled, and the name is how you catch it.

## Three properties that are no longer in file names

`Self Targeting`, `TEEP Stage` and `Valence Zone` used to be packed into the old variant token
(`1Aa-Z3` = variant, self, TEEP, zone). **They are not in the current convention.** Keep setting
them on the page — they are useful for filtering — but they do not travel with the asset.

**Briefs written before 2026-09-14 use the old scheme.** In `HPT089_..._1Aa-Z1_...` the `A` is
Self Targeting; in `HPT090_..._1B_...` the `B` is awareness. Same slot, different meaning. Do not
"fix" an old name to match the new shape, and do not read an old letter as an awareness level.

## Two things to get right

**The date keeps its leading zero.** `091426`, never `91426`. It is a plain string here, so the
old spreadsheet coercion trap is gone — but a dropped zero still sorts wrongly.

**Set `Content Type`, `Editor` and `Strategist` once.** They appear in the property and in every
name built from it, so there is only one place to change them now. That is the main thing the
move off the spreadsheet bought: the filename can no longer disagree with the database.
