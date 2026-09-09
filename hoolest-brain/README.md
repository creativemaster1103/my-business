# Hoolest Performance Technologies — brand brain

Parker's memory and method for Hoolest. Built 2026-09-08/09 against the live Parker MCP —
the Meta ad account, customer reviews, ad comments, the TikTok library and the competitor ad
library. Pinned to factory release **v15**.

**Start here: open this folder and run `/get-started`** for a guided walkthrough of what's here
and what to do first. Everything below is the map.

> ## This build is incomplete — read `BUILD-STATUS.md` first
>
> The build stopped partway through Phase 1 when the API spend limit was reached. Six documents
> are complete, three are truncated mid-write, and Phases 2 and 3 were never run.
> `BUILD-STATUS.md` is the authoritative ledger of exactly what exists.
> Resume with `/set-up-brain`, which reads it and picks up from the first unresolved item.

## What was pulled, and what stayed dark

| Surface | Status |
|---|---|
| Meta ads | **Live** — 2,887 ads, $3.85M lifetime spend, 22,650 purchases |
| Customer reviews | **Live** — 139 reviews, 4.11 avg (no real dates; all share the CSV ingest timestamp) |
| Facebook ad comments | **Live** — current through 2026-09-08 |
| TikTok / organic | **Live** — 20 videos |
| Competitor ad library | **Live** — 7 rivals subscribed, 1,341 ads, 568 AI-analyzed |
| Post-purchase surveys | **Dark** — zero responses ingested |
| Northbeam | **Not connected** — everything is Meta-reported at default attribution |
| Parker web chat history | **None** — no prior threads to read in |

## Where to start reading

1. **`BUILD-STATUS.md`** — what exists, what is truncated, what was never run.
2. **`audits/2026-Q3/90-day-performance-audit.md`** — the headline read of the account. ROAS
   trends down inside the quarter (1.44 → 1.15) while spend grew 42.5%.
3. **`audits/2026-Q3/customer-review-audit.md`** — the sharpest doc in the build. The 4.11 star
   average is a shipping story, not a product story, and three unnamed personas surface in it.
4. **`audits/2026-Q3/90-day-diversity-audit.md`** — where spend concentrates and what it starves.
5. **`brand-lens.md`** — the brand's own tribal knowledge, including two stated beliefs the data
   contradicts.
6. **`running-notes/missing-context.md`** — the ten things only Hoolest can answer.
7. **`audits/INDEX.md`** and **`competitors/INDEX.md`** — the generated maps of those folders.

`CLAUDE.md` is the operating contract; it leads with the brand's hard claim rules and carries an
honest account of what is thin, so Parker does not answer from a doc that isn't there.

## The three things most worth fixing

1. **Connect post-purchase surveys.** The highest-intent voice-of-customer surface is empty.
2. **Set a north-star metric.** The one stated bar — "2x ROAS at $1K adspend" — cannot grade an
   account running ~$11,491/day, so every performance doc currently grades against Meta defaults.
3. **Ingest ZenoWell and Vagustim Health.** Both are confirmed competitors absent from Parker's
   database, so both are missing from every competitor read here.

## How this brain travels

- **The skills come with it.** `.claude/skills/` holds 26 skills — the craft set (scriptwriting,
  hooks, headlines, iterations, ad-account-analysis, ai-ad-generation, the open-loops pipeline)
  and the routine set (dream, self-improve, refresh-context, research-loops, harvest-ideas,
  evaluate-ideas, update-brain, save-brain, setup-routines, get-started, disconnect-factory).
  They load on clone, after the one-time workspace-trust prompt.
- **The method comes with it.** `parker-system/` is the public `parker-brain` factory mounted as
  a read-only submodule pinned to **v15**, so every prompt that generated a doc here can be
  re-run exactly. `/update-brain` offers newer releases; the team decides.
- **Updates are offered, never imposed.** What you decline stays declined; what you modify stays
  yours.

> **The routines are stamped but not armed.** `schedules/` holds all six recipes and the skills
> are in place, but no scheduled agents were registered — the build environment had no scheduler.
> Run `/setup-routines` to arm them.

> **This brain is self-managed, not Parker Desktop-synced.** It lives inside the
> `creativemaster1103/my-business` repo rather than its own, because the session that built it
> could not reach `parker-brain/hoolest-hoolest-performance-technologies`.
> `running-notes/standard-sync.md` explains how to move it, and note that `/save-brain` and the
> git-guard hook both assume Desktop sync — read them before relying on either.
