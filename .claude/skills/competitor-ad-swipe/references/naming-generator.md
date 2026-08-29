# Naming generator — Zapier → Google Sheets

The file names in every brief are produced by **Mark's Naming Convention Generator**, not by
reconstructing the format by hand. Reconstruction is how you ship a filename that looks right
and is wrong.

| | |
|---|---|
| Spreadsheet | `1LqXRQXs4WyGptVOmvsk1JIH1UnfyBExIC2Ls-rtBhL8` |
| Worksheet (video) | `0` — "Video Naming Convention" |
| Worksheet (static) | `865461764` — "Static Naming Convention" |
| Zapier app | Google Sheets, connection `mark@hoolest.com` |

The Google Drive connector is read-only for content, so all writes go through Zapier.

## Sheet layout

| Range | What |
|---|---|
| Row 1 | Headers |
| Rows 2-16 | **Inputs**, one row per variation |
| Rows 20-24 | **Output** — file/ad names, max 5 |
| Row 29 col A | **Output** — Batch name |
| Row 30 col A | **Output** — Folder name |

Input columns, in order:

```
A Creative ID   B Format      C Date (MMDDYY)  D Concept name  E Variation
F Self Variation  G TEEP Stage  H Valence Zone  I Product      J Content Type
K Avatar        L Offer       M Category       N Strategist    O Editor
```

`O` (Editor) defaults to **`JM`**. `N` (Strategist) is `Mark`.

`F` and `G` take the **letter only** — `A - Actual Self` → `A`, `b - Exploration` → `b`. They
concatenate in the output as `1Ab-Z3`, which is why both matter and why TEEP Stage is easy to
lose: it appears nowhere else in the string.

## Procedure

1. **Clear rows 6-16** with `google_sheets_clear_spreadsheet_row_s`, `row: "6-16"`. Do this
   first, every run. Stale rows from the previous brief will otherwise generate extra file
   names for a concept that no longer exists.
2. **Write rows 2-5** with `google_sheets_update_spreadsheet_row_s`, one row per hook variant,
   `COL$E` = 1..4.
3. **Read rows 20-24 and 29-30** with `google_sheets_get_data_range`.
4. **Paste those strings verbatim** into the brief's naming tables. Do not adjust them, even if
   one looks wrong — if it looks wrong, the inputs were wrong; fix those and re-read.

## The sheet normalises some values

It returned `Off-Ramper` for the `Off-ramper` that Notion's Avatar property uses. The sheet's
casing wins for filenames — paste what it gives you rather than "correcting" it back to match
Notion.

Read the output back **after** the write, never assume it. A read taken while the sheet is being
edited in the browser can catch a half-applied state: one run here briefly returned `New` for a
`Category` that was `Adaptation` moments later.

## Two traps, both learned the hard way

**The date loses its leading zero.** Writing `082926` lets Sheets coerce it to the number
`82926`, and the filename silently ends `_82926`. Write it as `'082926` — the leading apostrophe
forces text. Always re-read row 20 to confirm the zero survived.

**Empty strings do not clear cells.** Passing `""` through `update_row_lines` is ignored, and
the sheet's fill-down then repopulates the row, generating variations you did not ask for. Only
`clear_spreadsheet_row_s` actually clears.

Row 24 reads `___-________` when only four variations are filled. That is the formula running on
an empty row — expected, ignore it.

## Statics

Same sheet, worksheet `865461764`, `IMG` instead of `VID`. Note statics use an **uppercase** TEEP
letter (`1bD-Z2`) where video uses lowercase (`1Ab-Z3`). Take the case from the sheet rather than
assuming.
