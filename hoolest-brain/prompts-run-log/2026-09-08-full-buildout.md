# Full buildout — Hoolest Performance Technologies

Permanent provenance record for the 2026-09-08/09 build. `BUILD-STATUS.md` was the live view
while the build ran; this is the durable record of what actually executed.

- **Brand:** Hoolest Performance Technologies (`cd6c3e3b-2beb-434a-837e-432a82d79178`)
- **Run id:** `4c20de24-44c5-404d-bde9-20a2030abda1`
- **Method pin:** parker-brain v15 (`b55c441`; `git describe` resolves it as v14 — same commit)
- **Scope agreed with Mark:** Phase 0 + Phase 1 only. Phases 2 and 3 deliberately not run.
- **Outcome:** interrupted at ~21:40 UTC on 2026-09-08 by an individual API spend limit.

## A note on the review pass

The runner requires a **separate review subagent** per output, checking fidelity to the prompt
before any downstream node consumes the doc. **That pass was never run** — the spend limit was
reached before any review could start, and the session had no budget for it afterwards.

Every verdict below is therefore `not reviewed`. The docs were spot-checked structurally by the
orchestrator (frontmatter present, claim labels present, open-loops tail present, not truncated),
which is a far weaker check than the review pass. Anyone resuming this build should run the
review pass over the six completed docs before treating them as gated.

## Phase 0 — repo and scaffold

| Step | Result |
|---|---|
| `get_available_brands` | One org (Hoolest), one brand. Locked without asking. |
| Operability check — Meta ads | **Live.** 2,887 ads, $3,851,961.87 lifetime spend, 22,650 purchases, 1.39 ROAS. One ad account: Hoolest FB Ads (948100899908170, USD). |
| Operability check — customer reviews | **Live.** 139 reviews, 4.11 avg. |
| Operability check — ad comments | **Live**, current through 2026-09-08. |
| Operability check — TikTok/organic | **Live.** 20 videos. |
| Operability check — post-purchase surveys | **DARK.** Collection exists, 0 responses. |
| Operability check — competitor library | **Empty at first check** — only the own-brand row. |
| `search_chat_history` | No prior threads. No web history to read into the build. |
| `check_northbeam_connection` | `connected: false`. All attribution is Meta default. |
| `setup_parker_brain` | Created `parker-brain/hoolest-hoolest-performance-technologies`. **Could not be cloned or pushed to** — session GitHub scope was limited to `creativemaster1103/my-business`; token clone and repo-attach both denied. Brain delivered to a subfolder of `my-business` per Mark's decision. |
| Competitive set | Mark chose his own confirmed 9 from `config/competitors.yml` over Parker's auto-pick (whose top hits were at-home blood testing and supplements — not category rivals). |
| Competitor subscribe | **7 of 9 subscribed** as `competitor`: Pulsetto, Truvaga, Sensate, Apollo Neuroscience, Neuvana, Nurosym, SONA.help. Library populated immediately: 1,341 ads, 568 AI-analyzed. |
| Competitors not found | **ZenoWell, Vagustim Health** — no match in Parker's brand database. Excluded from every competitor doc. |
| Scaffold, mount, ship | Flat layout created; factory mounted as a pinned submodule; 21 craft + 11 routine skills shipped (routine `dream` won the collision); review-gate agents, checker scripts and voice layer copied and verified executable. |
| Brand intake | **Not run.** Optional per the runner and never a gate. Ten items logged to `running-notes/missing-context.md`. |

## Phase 1 — prompt runs

Every prompt was delegated per the fidelity contract: the subagent received a **pointer to the
prompt file**, never a paraphrase, plus the brand, the `brand_id`, the flat output path, and the
verified denominators it needed.

| Prompt | Output | Sources pulled | Verdict |
|---|---|---|---|
| `audits-quarterly/90-day-performance-audit` | `audits/2026-Q3/90-day-performance-audit.md` | `search_facebook_ads_sql`, `list_custom_metrics`, `check_northbeam_connection`, `get_brand_persona` | **complete**, not reviewed |
| `audits-quarterly/90-day-diversity-audit` | `audits/2026-Q3/90-day-diversity-audit.md` | `search_facebook_ads_sql` (tags, tags_summary, ad_analysis), `search_competitor_facebook_ads` | **complete**, not reviewed |
| `audits-quarterly/customer-review-audit` | `audits/2026-Q3/customer-review-audit.md` | `search_customer_reviews_sql` + `_semantic` (all 139 rows read), `search_facebook_ad_comments_sql` | **complete**, not reviewed |
| `audits-quarterly/90-day-creative-strategy-audit` | `audits/2026-Q3/90-day-creative-strategy-audit.md` | `search_facebook_ads_sql` | **TRUNCATED** — died mid-write; no open-loops tail |
| `competitor-profile/competitor-snapshot` (SONA.help) | `competitors/sona-help/competitor-snapshot.md` | `search_competitor_facebook_ads` (28 ads) | **complete**, not reviewed |
| `competitor-profile/competitor-snapshot` (Neuvana) | `competitors/neuvana/competitor-snapshot.md` | `search_competitor_facebook_ads` (18 ads) | **complete**, not reviewed |
| `competitor-profile/competitor-snapshot` (Sensate) | `competitors/sensate/competitor-snapshot.md` | `search_competitor_facebook_ads` (8 ads) | **TRUNCATED** — died mid-URL; no open-loops tail |
| `personas/ad-account` | `source-pulls/ad-account.md` | `search_facebook_ads_sql`, `get_brand_persona` | **complete**, not reviewed |
| `personas/ad-comments` | `source-pulls/ad-comments.md` | `search_facebook_ad_comments_sql` + `_semantic` | **complete**, not reviewed |
| `voice-of-customer/voc-corpus-profile` | `personas/voice-of-customer/voc-corpus-profile.md` | reviews, ad comments, TikTok library, survey collection (empty) | **TRUNCATED** — final section cut |
| `audits-monthly/monthly-hook-audit` | — | — | **never started** (container restart) |
| `audits-weekly/weekly-performance-snapshot` | — | — | **never started** (container restart) |
| `audits-monthly-external/monthly-creative-landscape` | — | — | **never started** (container restart) |
| `audits-quarterly-external/90-day-creative-strategy-audit-external` | — | — | **never started** (container restart) |
| `personas/customer-reviews` | — | — | **never started** (spend limit) |
| `personas/brand-reputation` | — | — | **never started** (spend limit) |
| `competitors/_competitive-set` | — | — | **never started** (container restart) |
| `competitor-snapshot` — Pulsetto, Nurosym, Apollo, Truvaga | — | — | **never started** (container restart) |
| `competitor-profile/working-thesis-synthesis` | — | — | **never started** (container restart) |
| `personas/post-purchase-surveys` | — | — | **blocked** — 0 survey responses exist |

## Stamp and verify — 2026-09-09

Run directly by the orchestrator, no data pulls required.

| Step | Result |
|---|---|
| `CLAUDE.md` | Stamped from `templates/brand-brain-CLAUDE-template.md`. Hard rules filled from the team's own VeRelief Prime compliance gate; build-status slot filled with an honest account of what is thin, truncated or absent. |
| `README.md` | Brand-facing map, incomplete-build warning first. |
| `brand-lens.md` | Seeded from `config/competitors.yml`, the team's brief, and the Q3 audits. All lines marked `stated` or `verified`. |
| `running-notes/refresh-schedule.md` | Generated from the real frontmatter of the 10 docs that exist, plus an explicit "not yet generated" list. |
| `running-notes/routine-log.md` | Stamped empty, ready for the first routine run. |
| `competitors/INDEX.md`, `audits/INDEX.md` | Generated. |
| Truncation banners | Added in-file to the three cut documents so they cannot be mistaken for finished. |
| Build-completion verification | All structural checks pass **except** routines not armed (no scheduler in the build environment — run `/setup-routines`). |

## What a resume must do first

1. Re-run the **anchor** — `audits-quarterly/90-day-creative-strategy-audit`. Branch A is blocked on it.
2. Re-run `voc-corpus-profile` and the Sensate snapshot.
3. Run the **review pass** over the six completed docs, which never happened.
4. Then continue from the first `pending` item in `BUILD-STATUS.md`.
