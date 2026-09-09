# Refresh schedule — Hoolest Performance Technologies

This is the one place that tracks when every standing doc was last run and when it is due to be
re-run. Each doc's own `generated_on` and `refresh_by` frontmatter is the source of truth; this
file aggregates them so the whole brain's freshness can be read at a glance. The cadence policy
lives in `parker-system/system/refresh-cadence.md`.

> **This brain is partially built.** Only the docs listed below exist. Every other standing doc
> named in the factory's template — the whole of `sub-context-docs/`, `personas-profile.md`, the
> voice-of-customer slices, `strategy/`, the open-loops roll-up — has **never been generated**,
> so it has no line here. See `BUILD-STATUS.md` for what is missing and why.

## How Parker uses this

- When you load this brain or consult a standing doc, read this schedule and compare each `due` date to today from `get_current_time`. A doc whose due date has passed is overdue; one inside roughly two weeks of its due date is due soon.
- Surface what is overdue or due soon plainly, and offer to re-run the generating prompt by name — "your ad-account read is from March and it is now July, want me to refresh it." Do not silently keep using a doc past its due date, and do not re-run without surfacing the recommendation first.
- A refresh is a re-run of the generating prompt. It takes the prior version as context, carries forward what is still true, and re-stamps `generated_on` and `refresh_by`. After a re-run, update that doc's line in this schedule to the new dates.
- The triggers in `parker-system/system/refresh-cadence.md` outrank the calendar. A rebrand, a new SKU, a pricing move, a new competitor, an attribution change, or a validated finding that changes the read makes a doc due early regardless of the date here. When a trigger has fired, flag the doc as due now and note the trigger.
- When two or more sub-context slices have been re-run, `sub-context-docs/brand-profile-narrative.md` is due regardless of its own date, because it is a synthesis of them.

## The schedule — every standing doc that exists

- `audits/2026-Q3/90-day-creative-strategy-audit.md` — last run 2026-09-08 — due 2026-11-10  **TRUNCATED — re-run required**
- `audits/2026-Q3/90-day-diversity-audit.md` — last run 2026-09-08 — due 2026-12-07
- `audits/2026-Q3/90-day-performance-audit.md` — last run 2026-09-08 — due 2026-12-07
- `audits/2026-Q3/customer-review-audit.md` — last run 2026-09-08 — due 2026-12-07
- `competitors/neuvana/competitor-snapshot.md` — last run 2026-09-08 — due 2026-10-08
- `competitors/sensate/competitor-snapshot.md` — last run 2026-09-08 — due 2026-10-08  **TRUNCATED — re-run required**
- `competitors/sona-help/competitor-snapshot.md` — last run 2026-09-08 — due 2026-10-08
- `personas/voice-of-customer/voc-corpus-profile.md` — last run 2026-09-08 — due 2027-03-07  **TRUNCATED — re-run required**
- `source-pulls/ad-account.md` — last run 2026-09-08 — due 2026-12-07
- `source-pulls/ad-comments.md` — last run 2026-09-08 — due 2026-11-07

## Not yet generated

These have no `generated_on` because they were never run. They are not overdue — they are absent.
Running them is a build task, not a refresh task; `/set-up-brain` resumes that build.

- All of `sub-context-docs/` — including `brand-profile-narrative.md`, the always-loaded one-pager
- `personas/personas-profile.md`, `persona-voice-library.md`, `lifecycle-journey-maps.md`, `cross-persona-bias-notes.md`
- All ten `personas/voice-of-customer/voc-*.md` extraction slices and the assembly
- `competitors/_competitive-set.md`, `working-thesis-synthesis.md`, and snapshots for Pulsetto, Nurosym, Apollo Neuroscience and Truvaga
- The monthly hook audit, weekly snapshot, and every external competitor audit cut
- `audits/[quarter]/gaps-opportunities-inspo.md`
- `open-loops/open-loops-roll-up.md`
- Everything in `strategy/`, `idea-bank/`, `briefs/` (Phases 2 and 3 were not run)
