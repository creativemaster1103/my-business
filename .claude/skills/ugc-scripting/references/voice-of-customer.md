# Voice of customer — mining guide

How to build the quote bank a UGC script is written from, and how to tell a usable quote from a
nice one.

## Where the good material actually is

| Source | Tool | What it uniquely gives |
|---|---|---|
| Reviews, 3–4★ | `reviews_search` (Okendo) | Expectation vs. reality, and the thing that nearly stopped them buying |
| Reviews, semantic | `search_customer_reviews_semantic` (Parker) | Emotional states in their own words, across the whole corpus |
| Post-purchase survey | `semantic_search_post_purchase_survey` (Parker) | **The trigger moment** — what was happening when they decided |
| Ad comments | `search_facebook_ad_comments_semantic` (Parker) | Public objections, i.e. the ones the script must pre-empt |
| Support tickets | `list_tickets` / `search_tickets` (Gorgias) | Private objections, and misuse patterns worth directing around |
| Review questions | `questions_list` (Okendo) | What people needed to know before buying — straight CTA material |

**Read the 3- and 4-star reviews first.** Five-star reviews are congratulation, not information:
"love it, works great" cannot be built on. The middling review is the one that says *I thought it
would be gimmicky, it isn't, but the gel tips run out faster than I expected* — which is a hook,
a proof beat and an objection in one paragraph.

## What to search for

Search the **state**, not the product. Nobody writes "vagus nerve stimulation device" in a review
about how they feel. They write:

```
couldn't switch off · tired but wired · brain wouldn't shut up · sceptical
tried everything · wasted money on · my wife noticed · didn't expect
gave up on · 3am · before a presentation · instead of a drink
```

Run several narrow semantic queries rather than one broad one. "Stress" returns everything and
therefore nothing.

## Judging a quote

A quote earns a place in the bank if it does one of three jobs. Tag which:

- **Hook** — names a situation specifically enough that the right viewer recognises themselves
  in four words. `"I'd be exhausted and still lying there at 2am"`
- **Objection** — the reason they nearly did not buy. `"another gadget to put in a drawer"`
- **Proof** — what changed, stated concretely and without hyperbole. `"I stopped needing the
  second glass of wine to wind down"`

Reject a quote if:

- It is generic praise. "Amazing product" is not material.
- It names a **diagnosed condition** as the thing that improved. You cannot build a script on it
  — the brand compliance gate will kill the line, so do not start there.
- It states a number you cannot substantiate. "Dropped my resting heart rate 12 points" is one
  person's device reading, not a claim we can make.
- It is the only one of its kind. One person saying something striking is an anecdote; three
  people circling the same phrasing is an insight. **Prefer the pattern.**

## Building the bank

Keep it as a flat list until you have enough to see repetition:

```
"[verbatim quote]"  · source · avatar · hook | objection | proof
```

Aim for 15–25 usable quotes before writing. Then cluster by **what the person was trying to
do**, not by sentiment. The cluster with the most independent voices is the script.

## The line you cannot cross

Everything in the bank is **raw material for writing**, never a line to hand a creator as their
own experience. Mine the phrasing, the objection and the rhythm; write the sentence.

If the actual customer words are too good to lose, that is a **quote card** — on screen,
attributed, presented as a review — and the creator reacts to it rather than claiming it. See the
endorsement gate in `ugc-creator-brief.md`.

**Never invent a quote.** Not to fill a gap, not as a placeholder, not "in the style of" the ones
you found. A fabricated review in a brief becomes a fabricated claim in an ad, and nobody
downstream has any way to tell it was synthetic. If the connectors returned nothing usable,
report that and stop.
