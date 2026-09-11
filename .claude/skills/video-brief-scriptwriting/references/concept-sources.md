# Where an originated concept comes from

A competitor sweep gets its validation for free: an ad running 30+ days has already survived a
real auction. Originating has no such borrowed signal. **Evidence is what replaces it.**

So the question this file answers is not "what should we say?" but "what do we already know that
nobody has built an ad out of yet?"

Work top to bottom. The sources are ordered by how close each sits to a real buyer's own words,
and the first three are the only ones that satisfy `require_voice_of_customer_anchor`.

---

## 1. Customer reviews — Parker

The single best source. People who paid describe the problem in language no copywriter invents,
and they volunteer the objection they had to talk themselves past.

```
get_available_brands            → resolve the brand first; everything else needs it
search_customer_reviews_semantic  → thematic: "couldn't switch off", "gave up on melatonin"
search_customer_reviews_sql       → structured: filter by rating, date, product
```

Search for the **shape of a moment**, not for praise. "Works great" is worth nothing. What you
want is the sentence where someone describes the 4pm crash, the third night awake, the thing
they tried before us.

Mine reviews for three different things and keep them separate:

| What you are looking for | What it becomes in the brief |
|---|---|
| The moment the problem bites | The **hook** |
| What they tried first and why it failed | The **failed alternative** block |
| The objection they admit to having had | What the **body** pre-empts |

Low-star reviews are not a problem to skip past. A two-star review naming an expectation we set
badly tells you exactly which promise the next ad should stop making — that is a brief too.

## 2. Post-purchase survey — Parker

```
semantic_search_post_purchase_survey   → thematic search across responses
lookup_post_purchase_survey            → pull specific responses
```

The survey answers the one question reviews do not: **what were they actually trying to fix on
the day they bought?** That is the trigger moment, and a `a - Trigger` brief is only honest if it
is built on one of these rather than on a guess about what a stressed person's Tuesday looks like.

Read the free-text answers, not just the aggregate. The aggregate tells you "stress"; the
free text tells you "my chest was tight before every stand-up".

## 3. Facebook ad comments — Parker

```
search_facebook_ad_comments_semantic
search_facebook_ad_comments_sql
```

Comments are where the objection lives **before** the sale, from people who did not buy. They are
blunter than reviews and considerably more useful for the body of an ad.

Recurring comments on our own ads are a standing instruction about what the next script has to
handle in the first ten seconds — price, "does this actually work", "is this just a TENS unit",
"can I use it with my medication". Never answer that last one on the medication question's own
terms; see the compliance gate.

## 4. Our own performance data — Motion

Supporting evidence, never the whole case. It shows *what* worked, not *why* — and a brief built
only on "this one had a good hook rate" is a brief that copies our own surface the way a bad
swipe copies a competitor's.

**The SPEND-first rule.** Motion's own protocol, and it matters:

```
get_auth_context                                   → workspaces, defaultWorkspaceId
get_creative_insights(insightType="SPEND", …)      → ALWAYS first
```

The `SPEND` response carries `goalMetric`, `spendThreshold` and `customConversions` at the top
level. Everything after it is read against those anchors, so calling `SCALING` or `HOOK` first
gives you numbers with nothing to interpret them against. If `goalMetric.isCustomConversion` is
true, carry `["{id}_cost", "{id}_count"]` in `tableKPIs` on every later call or per-creative
efficiency simply will not appear.

Then:

```
get_creative_insights(insightType="HOOK")    → which openings hold attention
get_creative_insights(insightType="SCALING") → what survived budget
get_creative_transcript(…)                   → the actual words of a winner
get_demographic_breakdown(…)                 → who a concept is landing on vs. who it was for
```

Use it for two jobs and no others:

1. **Hook mechanics.** A hook that holds attention tells you the *mechanism* that works on this
   audience — not the line to reuse. Abstract it, then rebuild it for a different avatar.
2. **The gap.** Cross-reference what is winning against the avatar spread. If everything winning
   speaks to Wired Lifer, the gap is not a better Wired Lifer ad.

**Never lift a number out of Motion into a script.** Performance figures are ours, not claims we
have substantiated for a viewer. See the compliance gate, rule 3.

## 5. Swipe file — Parker

```
search_swipe_file
```

Structures Mark has already flagged as worth having. Overlaps with the competitor pipeline's
`★ Mark's Picks`, but reached from the other end: here you have a concept and want a structure
for it, rather than a structure looking for a concept.

## 6. Product truth — Shopify

```
get-shop-info · search_products · get-product
```

**Live price and current offer, every run. Never hardcode a price.** A stale price in a brief
reaches an editor and then reaches a viewer.

Also the place to check what is actually true about the product before writing a demo beat —
what is in the box, what the gel tips cost, what the guarantee window currently is.

---

## The evidence test

Before a concept goes any further, write its case in one sentence of this shape:

> **Someone said _X_, which means _Y_ about what they believe, and no brief in the library has
> built on that yet.**

If you cannot fill all three slots, it is not a concept yet — it is a topic. Go back to the
sources.

Two failure modes, both of which produce briefs that look fine:

1. **Evidence as decoration.** Finding a review that happens to agree with a concept you already
   had. The review has to *generate* the concept, not ratify it. If you thought of the angle
   first and searched second, say so and treat it as unevidenced.
2. **The aggregate voice.** Building on "customers say they feel calmer" — a true sentence
   nobody has ever said. Specifics are the whole value of these sources; an average of them is
   just the category cliché with a citation attached.

## Recording evidence

Evidence goes in the **chat report**, never in the brief. The brief is for the editor, who cannot
act on a survey response. For each concept the report carries:

- the anchor quote, verbatim, and which source it came from
- the second piece of evidence
- the one-sentence case above

**Never invent, compose, or tidy a customer quote.** If you paraphrase for compliance, mark it as
a paraphrase and keep the original beside it. A fabricated quote in a brief becomes a fabricated
quote in an ad, and it is not recoverable once it has shipped.
