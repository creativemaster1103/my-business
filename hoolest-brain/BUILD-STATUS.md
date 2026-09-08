# BUILD-STATUS — Hoolest Performance Technologies

**Brand:** Hoolest Performance Technologies (`cd6c3e3b-2beb-434a-837e-432a82d79178`)
**Build started:** 2026-09-08
**Method pin:** parker-brain v15 (`b55c441`)
**Run id:** `4c20de24-44c5-404d-bde9-20a2030abda1`
**Current phase:** Phase 1 — audit baseline and foundation
**Right now:** 16 Phase-1 prompts are running in parallel across branches B, C, D and E.

> **Scope decision (Mark, 2026-09-08):** this session builds **Phase 0 + Phase 1 only**.
> Phase 2 (strategy) and Phase 3 (idea bank, sprint plan, briefs) are deliberately not run.
> Resume them later with `/set-up-brain`, which reads this file.

> **A full Phase 1 is ~128 prompt runs** (Branch B alone is 7 rivals x 10 slices = 70).
> That does not fit one session. This build runs the **dependency spine** — the docs every
> other doc is blocked on — at full fidelity, and leaves the rest `pending` with a reason.
> Nothing below is silently skipped: every unrun prompt is listed and marked.

## Scoreboard

| Branch | Done | Planned this session | Full Phase 1 |
|---|---|---|---|
| E — Audit baseline (internal) | 6 running | 6 | 11 |
| E — Audit baseline (external) | 2 running | 2 | 6 |
| A — Brand foundation | 0 | 6 | 14 |
| B — Competitors | 9 running | 9 | 71 |
| C — Personas | 4 running | 7 | 12 |
| D — Voice of customer | 1 running | 6 | 12 |
| Synthesis | 0 | 2 | 2 |

## Needs attention

- **Post-purchase surveys are dark** — 0 responses in Parker. Every persona and VoC doc that
  would read them is `data-limited`. Logged in `running-notes/missing-context.md`.
- **ZenoWell and Vagustim Health are not in Parker's database** — both confirmed competitors in
  `config/competitors.yml`, neither resolvable by `search_brand_by_name`. They are absent from
  every competitor doc in this build. Needs `brand_discovery operation:'ingest'` (~15 min each).
- **The brand intake was not run.** Ten items only Mark can answer are open in
  `running-notes/missing-context.md`. The north-star metric is unset, so performance docs grade
  against Meta defaults rather than Hoolest's own definition of success.
- **This brain is self-managed, not Desktop-synced.** See `running-notes/standard-sync.md`.

## Prompt ledger

Marks: `done` / `running` / `pending` / `blocked`.

### Phase 0 — repo and scaffold
- [x] `done` — flat layout scaffolded
- [x] `done` — factory mounted at `parker-system/`, pinned v15
- [x] `done` — 26 skills shipped to `.claude/skills/` (21 craft + routine bundle; routine `dream` won the collision)
- [x] `done` — review-gate agents + `voice-lint.py` + `grounding-check.py` shipped and verified executable
- [x] `done` — voice layer (`.claude/output-styles/parker.md` + `outputStyle: Parker`)
- [x] `done` — `parker_config.json`, `running-notes/standard-sync.md`, `running-notes/missing-context.md`
- [ ] `pending` — brand intake (optional; deliberately skipped, items logged)
- [ ] `pending` — `/setup-routines` arming (schedules stamped but **not armed** — no scheduler in this environment)

### Branch E — internal audit baseline
- [ ] `running` — audits-quarterly/90-day-creative-strategy-audit  **(anchor)**
- [ ] `running` — audits-quarterly/90-day-performance-audit
- [ ] `running` — audits-quarterly/90-day-diversity-audit
- [ ] `running` — audits-quarterly/customer-review-audit
- [ ] `running` — audits-monthly/monthly-hook-audit
- [ ] `running` — audits-weekly/weekly-performance-snapshot
- [ ] `pending` — audits-quarterly/quarterly-whitespace-analysis *(deferred — not in spine)*
- [ ] `pending` — audits-monthly/monthly-performance-report *(deferred)*
- [ ] `pending` — audits-monthly/monthly-organic-tiktok-audit *(deferred)*
- [ ] `pending` — audits-monthly/monthly-tiktok-mining *(deferred)*
- [ ] `pending` — audits-biweekly/biweekly-iterations-report *(deferred)*

### Branch E — external audit cuts
- [ ] `running` — audits-monthly-external/monthly-creative-landscape
- [ ] `running` — audits-quarterly-external/90-day-creative-strategy-audit-external
- [ ] `pending` — audits-monthly-external/monthly-top-impressions-report *(deferred)*
- [ ] `pending` — audits-quarterly-external/90-day-performance-audit-external *(deferred)*
- [ ] `pending` — audits-quarterly-external/90-day-diversity-audit-external *(deferred)*
- [ ] `pending` — audits-quarterly-external/single-competitor-ad-analysis *(deferred)*

### Branch A — brand foundation
- [ ] `pending` — brand-profile/ad-account-evaluation *(blocked on branch E anchor)*
- [ ] `pending` — brand-profile/performance-targets-and-metrics *(blocked on branch E)*
- [ ] `pending` — brand-profile/organic-channels-inventory *(blocked on branch E)*
- [ ] `pending` — brand-profile/brand-identity-analysis
- [ ] `pending` — brand-profile/website-and-product-audit
- [ ] `pending` — brand-profile/brand-profile-narrative *(blocked on all of A)*
- [ ] `pending` — brand-profile/category-and-market-research *(deferred)*
- [ ] `pending` — brand-profile/community-and-forums *(deferred)*
- [ ] `pending` — brand-profile/competitive-landscape *(deferred)*
- [ ] `pending` — brand-profile/customer-journey-and-persona-discovery *(deferred)*
- [ ] `pending` — brand-profile/marketing-calendar-and-campaigns *(deferred)*
- [ ] `pending` — brand-profile/operations-and-team *(deferred)*
- [ ] `pending` — brand-profile/reputation-analysis *(deferred)*
- [ ] `pending` — brand-profile/visual-vocabulary *(deferred)*

### Branch B — competitors
Tracked set (7 subscribed 2026-09-08): Pulsetto, Truvaga, Sensate, Apollo Neuroscience,
Neuvana, Nurosym, SONA.help. Missing: ZenoWell, Vagustim Health (not in Parker's DB).
- [ ] `running` — `competitors/_competitive-set.md`
- [ ] `running` — competitor-snapshot x 7 (one per rival)
- [ ] `running` — working-thesis-synthesis
- [ ] `pending` — the 9 per-rival deep slices x 7 rivals = 63 runs *(deferred — full-fidelity per-rival profiles are a session of their own)*

### Branch C — personas
- [ ] `running` — personas/ad-account
- [ ] `running` — personas/ad-comments
- [ ] `running` — personas/customer-reviews
- [ ] `running` — personas/brand-reputation
- [ ] `pending` — personas/personas-profile *(blocked on the source pulls)*
- [ ] `pending` — personas/persona-voice-library *(blocked on personas-profile)*
- [ ] `pending` — personas/cross-persona-bias-notes *(blocked on personas-profile)*
- [ ] `blocked` — personas/post-purchase-surveys — **0 survey responses in Parker.** Nothing to read.
- [ ] `pending` — personas/other-reviews *(deferred)*
- [ ] `pending` — personas/reddit *(deferred)*
- [ ] `pending` — personas/brand-self-echo-detection *(deferred)*
- [ ] `pending` — personas/lifecycle-journey-maps *(deferred)*

### Branch D — voice of customer
- [ ] `running` — voice-of-customer/voc-corpus-profile
- [ ] `pending` — voice-of-customer/voc-pain-phrase
- [ ] `pending` — voice-of-customer/voc-outcome-phrase
- [ ] `pending` — voice-of-customer/voc-objection
- [ ] `pending` — voice-of-customer/voc-trigger-moment
- [ ] `pending` — voice-of-customer/voice-of-customer-assembly *(blocked on the slices)*
- [ ] `pending` — voc-anti-language, voc-aspirational, voc-category-jargon, voc-metaphor, voc-surprise-delight *(deferred — 5 runs)*

### Synthesis
- [ ] `pending` — market-synthesis/gaps-opportunities-inspo *(blocked on A + B)*
- [ ] `pending` — open-loops/open-loops-roll-up *(blocked on everything above)*

### Stamp
- [ ] `pending` — `CLAUDE.md` from template
- [ ] `pending` — `README.md`
- [ ] `pending` — `brand-lens.md`
- [ ] `pending` — `running-notes/refresh-schedule.md` + `routine-log.md`
- [ ] `pending` — `competitors/INDEX.md`, `audits/INDEX.md`

## What happens next

Branch E's anchor audit runs first — the account one-pagers in Branch A are defined as syntheses
of it, so nothing in A can be honest until it exists. Branches B, C and D run alongside it.
