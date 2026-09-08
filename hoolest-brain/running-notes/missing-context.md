---
brand: Hoolest Performance Technologies
doc: missing-context
last_updated: 2026-09-08
sources: Phase 0 operability check + competitive-set decision
---

# Missing context — what the brand has not yet told us

## Data sources not connected

- **Post-purchase surveys — dark.** `semantic_search_post_purchase_survey` confirms the Qdrant
  collection exists but holds **0 responses** for this brand. Needs a KnoCommerce/Zigpoll connection
  or a CSV upload. Until then every purchase-motivation and objection claim leans on reviews and ad
  comments alone, and the VoC corpus is missing its highest-intent surface. `data-limited`
- **Website / landing-page tracking — off** for every tracked competitor (`tracking.website: false`).
  Competitor offer and LP claims cannot be read directly.
- **Own-brand Meta Ad Library tracking — off** (`tracking.metaAds: false` on the own_brand record).
  Internal performance comes through `search_facebook_ads_sql` instead, so this is not a hole for
  the audit — but self-audit against the public library is unavailable.

## Competitors not in Parker's database

Both were confirmed by Mark in `config/competitors.yml` but returned **no match** from
`search_brand_by_name`, so they are absent from the competitive set this build produced:

- **ZenoWell** (zenowell.ai) — noted as "54 active ads, and runs vagusnervecommunity.org. Squarely our category." `priority: high`
- **Vagustim Health** (vagustim.io) — noted as "33 active ads. Direct vagus-nerve device competitor." `priority: medium`

To add: `brand_discovery` with `operation: 'ingest'` and each brand's Facebook page URL (~15 min
each), then subscribe. **This is the single highest-value gap to close** — ZenoWell is flagged high
priority and is missing from every external audit cut in this build.

## Intake questions — ordered by what they unblock

The Phase-0 brand intake was **not run** in this build (the session was scoped to Phase 0 + Phase 1
and the intake is optional, never a gate). Every item below is still open and only the brand can
answer it. Answering the first three changes how every performance read is graded.

1. **North-star metric, and whether hitting its goal is the whole definition of success** — ROAS, CPA, MER, CVR, AOV, or another. → `running-notes/brand-rules.md`
2. **Main business objective right now** — scale acquisition, improve efficiency, launch, revenue target, or retention. → `running-notes/success-definition.md`
3. **Where performance is read** — in-platform, or a third-party tool (Northbeam, Triple Whale). Parker found no Northbeam connection on this brand.
4. **Spend-vs-efficiency tiebreak** — when two ads in one ad set diverge on spend, does higher spend win, or is efficiency weighed too?
5. **Secondary metrics still weighed.**
6. **Ad naming convention** — walk it through or paste the sheet. The account's names (e.g. `Prime_ Home_TOF_Panic_BulbFX_Mar 26th 2026`) imply a convention that has not been confirmed.
7. **Brief template** — share it, saved verbatim to `briefs/_brief-template.md`.
8. **Unit economics** — customer worth, gross margin, LTV/payback window, max tolerable CPA.
9. **Aspirational / inspo brands** — the tracked set is all `competitor`; no `inspo` or `affinity` brands are subscribed.
10. **The gap question** — what does the team feel Parker is still missing, and what does a smart outsider always get wrong about this brand?

## Tools not connected

The runner's "get their own tools connected before the build" step was not run. Notion, Slack, Google
Drive and Gmail are live in the build session's own connector set but were **not** read into this
build. Anything the team keeps in those (briefs, taste, decisions) is unread context.
