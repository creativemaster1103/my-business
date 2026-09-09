---
brand: hoolest-performance-technologies
doc: voc-corpus-profile
generated_on: 2026-09-08
refresh_by: 2027-03-07
raw_records_received: 6721
normalized_records: 6216
deduplicated_records_removed: 0
date_range: 2024-08-09 to 2026-09-08 (ad comments only; the 139 reviews carry no original date)
sources_read:
  - "Parker customer reviews (search_customer_reviews_sql, search_customer_reviews_semantic) - 139 records, all read"
  - "Parker Facebook ad comments (search_facebook_ad_comments_sql) - 6,562 records, all 6,562 paged and counted"
  - "Parker post-purchase surveys (semantic_search_post_purchase_survey) - collection exists, 0 responses"
  - "Parker TikTok video library (search_tiktok_videos) - 20 videos, all read; no customer text in them"
expected_sources_missing:
  - "Post-purchase surveys - 0 responses. The highest-intent VoC surface is completely dark."
  - "Amazon reviews - a customer says in an ad comment they bought on Amazon, so the listing exists, but no Amazon review is in Parker"
  - "Original review dates - every review collapsed to the 2026-09-07 CSV import timestamp"
  - "Review source platform - all 139 carry type csv_import; no Shopify vs Yotpo vs Amazon split"
  - "Organic social comments (Instagram, TikTok, YouTube) - not reachable through Parker for this brand"
  - "Support tickets, email, and Reddit or forum pulls - not connected"
  - "Any demographic field anywhere in the corpus - age, gender, region, first-time-buyer status all absent"
structured_fields_available:
  - "reviews: row id, star score (1-5), title, body text, reviewer display name, product title, import timestamp"
  - "ad comments: comment id, message text, real created_time, like_count, reply count, permalink URL, ad_ids, ad_names, post_ids, parent_comment_ids, comment_length, snapshot_date"
  - "ad comments: author_name populated for Facebook Pages only (457 of 6,562, 7.0%); author_id null on every row"
model_applied_tags:
  - "sentiment band on reviews (derived from the structured star score, so this one is a structured fact)"
  - "record-level read of all 139 reviews: non-delivery vs product-experience, junk or test row, support ticket posing as a review"
  - "keyword theme tags on reviews, computed by the Parker SQL tool against all 139 (exact keyword lists printed in Classification method)"
  - "regex theme tags on 6,077 customer-language ad comments (exact patterns printed in Classification method)"
  - "lexicon sentiment attempt on ad comments - reported as a failure, not a finding"
data_limitations:
  - "0 post-purchase survey responses. No purchase-motivation, NPS, attribution, or first-time-buyer read is possible."
  - "139 reviews is a thin corpus, and 17 of them (12.2%) are from people who never received the product."
  - "No review dates, so no trend, no era tagging, no what-is-emerging read on the review side."
  - "No demographic or identity field anywhere. Any age, gender, or income claim downstream is inferred from writing style only."
  - "Ad comments have no rating field and a 49-character median, so no sentiment split can be computed from them."
  - "The ad comment corpus mixes two product lines (VeRelief nerve stimulators and MiniMax/Flex PEMF), so a comment is not automatically about VeRelief."
  - "TikTok library holds zero customer language. It is a competitor and creator swipe file, not a VoC surface."
---

> # ⚠ THIS DOCUMENT IS INCOMPLETE
>
> It was cut off mid-sentence when the build hit an API spend limit on 2026-09-08. The
> open-loops tail is present, but the final section ends partway through a sentence about
> clinician and practitioner language in the review corpus.
>
> The corpus measurements above are real and were verified against live pulls — they are safe to
> use as denominators. The last section's conclusions are not finished.
>
> Re-run: `parker-system/prompts/voice-of-customer/voc-corpus-profile.md`

# VoC corpus profile - Hoolest Performance Technologies

## Executive summary

**1. The highest-value customer surface is empty, and that is the headline.** `semantic_search_post_purchase_survey` returns 0 responses for this brand against a collection that exists and is queryable (**verified**, pulled 2026-09-08). Zero. Not thin, not sparse. Post-purchase surveys are the one place a real buyer tells you why and when they bought, and Hoolest has none. Every purchase-motivation, final-straw-trigger, and first-time-buyer claim that any downstream VoC or persona doc makes has to come from reviews and ad comments instead, which means every one of those claims is a step weaker than it looks. **This is the single most important sentence in this document.**

**2. The review pile is small and a chunk of it is not about the product.** 139 reviews total, 4.11 average score (**verified**, structured field). Of those, 17 (12.2% of 139) are written by people who say plainly they never received the device. Another 4 (2.9% of 139) are keyboard mash or off-topic. So the reviews that actually describe using the product number **118 of 139 (84.9%)**. On the negative side the split is brutal: of the 29 reviews scored 1 or 2 stars, **17 (58.6% of 29) are fulfillment complaints, not product complaints**. Only 12 of 139 reviews (8.6%) are a customer saying the device itself let them down.

**3. Ad comments are the deep corpus, and they are a question surface, not a satisfaction surface.** 6,562 comment records exist, current through today (**verified**, latest `created_time` 2026-09-08). After removing 415 brand replies and 70 blank rows, **6,077 rows are customer language**. But the median comment is 49 characters, and 1,593 of 6,077 (26.2%) contain a question mark. People are not reviewing here. They are asking how it works, what it costs, whether it is safe with their condition, and whether the science is real. That is a different creative job than a review corpus implies.

**4. The loudest single line in the whole corpus is a demand for proof.** The most-liked customer comment in 6,077 is "I'd like to see the clinical studies that show the safety and efficacy of this device." (214 likes, 2026-02-23, comment `e97c5f9e`). It sits on PEMF creative, not VeRelief. Across the customer comments, 159 of 6,077 (2.6%) name FDA, clinical, study, research, or evidence, and 241 of 6,077 (4.0%) use scam, snake oil, BS, placebo, or fake. Skepticism is the biggest single objection cluster in the corpus, bigger than price. **The most important creative lever the corpus points at is proof, delivered plainly.**

**5. Price is the second wall, and it has a specific shape: the recurring cost, not the sticker.** 432 of 6,077 customer comments (7.1%) touch price or cost. 129 of 6,077 (2.1%) name the gel tips, electrodes, or activators. In the reviews, 16 of 139 (11.5%) mention price and 17 of 139 (12.2%) mention the consumables. The complaint is rarely "$399 is too much" on its own. It is "$399 and then $50 a month forever." One commenter, 2026-01-12: "Jerry Nesseler it costs $50 a month for electrodes. Every month.  That's why i returned mine."

**Overall sentiment split (reviews, structured star field, n=139):** 107 positive (4-5 stars, 77.0%), 3 neutral (3 stars, 2.2%), 29 negative (1-2 stars, 20.9%). **Ad comment sentiment: data-limited.** There is no rating field, and a lexicon pass classified only 621 of 6,077 rows (10.2%), leaving 5,456 (89.8%) with no verdict language at all. Do not let a downstream doc quote a Facebook sentiment percentage. There isn't one.

**Largest data limitation:** the zero surveys, followed closely by the missing review dates. Every one of the 139 reviews carries `created_at` 2026-09-07, which is the CSV import timestamp, not when the customer wrote it. Grouping all 139 by month returns a single bucket. So the review corpus cannot answer "is this getting better or worse," and any downstream doc that wants a trend has to use ad comments, which do carry real dates.

---

## Source and data profile

### What was pulled, and how

| Surface | Tool | Raw records | Customer-language records | Date field usable? |
|---|---|---|---|---|
| Customer reviews | `search_customer_reviews_sql`, `search_customer_reviews_semantic` | 139 | 139 | No |
| Facebook ad comments | `search_facebook_ad_comments_sql` | 6,562 | 6,077 | Yes |
| Post-purchase surveys | `semantic_search_post_purchase_survey` | 0 | 0 | n/a |
| TikTok video library | `search_tiktok_videos` | 20 | 0 | Video post dates only |
| **Total** | | **6,721** | **6,216** | |

**How the ad comment count was actually measured, because the tool lies about it.** An unfiltered call to `search_facebook_ad_comments_sql` sorted descending returned `total: 0` while handing back 500 real rows (**verified**, reproduced 2026-09-08). Ascending calls returned `total: 6562`. So the total field is not trustworthy on its own. The size here was derived by paging: fourteen calls at `limit: 500`, offsets 0 through 6000 ascending plus one descending page to catch the tail, then deduplicating on `comment_id`. That produced **6,562 unique comment ids**, which matches the ascending total exactly. Offset 6500 returned exactly 62 rows, confirming the end of the collection. **Any downstream slice that trusts the `total` field on a single call may get zero. Page it.**

### Review corpus (n=139)

**Fields present:** `id`, `created_at`, `score`, `title`, `content`, `reviewer_name`, `product_title`. The semantic index adds `type`, which reads `csv_import` on every record checked.

**Fields absent:** review date, source platform, verified-buyer flag, review URL, order id, helpful votes, images, reviewer location, age, gender, and any purchase or repeat-purchase field.

**Populated share:**

| Field | Populated | Share of 139 |
|---|---|---|
| `score` | 139 | 100% |
| `content` (any text) | 139 | 100% |
| `content` (substantive product text) | 118 | 84.9% |
| `product_title` | 139 | 100% |
| `reviewer_name` | 139 | 100% |
| Original review date | 0 | 0% |
| Source platform (distinguishable) | 0 | 0% |
| Any demographic field | 0 | 0% |

**Rating distribution (structured field, verified):**

| Score | Count | Share of 139 |
|---|---|---|
| 5 | 98 | 70.5% |
| 4 | 9 | 6.5% |
| 3 | 3 | 2.2% |
| 2 | 7 | 5.0% |
| 1 | 22 | 15.8% |

That shape is worth pausing on. It is not a bell curve, it is a barbell: 107 of 139 (77.0%) at 4-5 stars and 22 of 139 (15.8%) at a flat 1 star. Weighted average checks out to 571/139 = 4.108, which matches the 4.11 the tool reports.

**Reviews by product (structured field, verified against the tool for the top three):**

| Product title | Reviews | Share of 139 | Avg score |
|---|---|---|---|
| VeRelief Prime - Lasting Relief Bundle | 45 | 32.4% | 3.40 |
| VeRelief Mini | 39 | 28.1% | 4.51 |
| VeRelief Prime Gen 2 | 17 | 12.2% | 4.88 |
| VeRelief Prime | 7 | 5.0% | not pulled |
| VeRelief Pro | 6 | 4.3% | not pulled |
| Hoolest Pro | 6 | 4.3% | not pulled |
| Hoolest Sleep | 5 | 3.6% | not pulled |
| Vagus Nerve Activator Gels | 4 | 2.9% | not pulled |
| The Replacement Gel Tip Subscription | 4 | 2.9% | not pulled |
| VeRelief Prime, Pro & Reset Gel Tips - 30 Day Supply | 2 | 1.4% | not pulled |
| Small VeRelief Electrodes | 1 | 0.7% | not pulled |
| VeRelief RESET | 1 | 0.7% | not pulled |
| Route Package Protection | 1 | 0.7% | not pulled |
| MiniMax GO | 1 | 0.7% | not pulled |

**The Bundle's 3.40 average is a shipping artifact, not a product verdict (verified by reading all 45).** 13 of the 45 Bundle reviews (28.9%) are from people who never received the order. Strip those 13 and the remaining 32 Bundle reviews are overwhelmingly positive. Any downstream doc that reads "the Bundle is the weakest SKU" from that 3.40 has misread the data. Say the real thing: the Bundle was the SKU that got backordered.

**Data-quality issues found in the reviews, by reading all 139:**

- **4 junk or off-topic rows (2.9% of 139).** `0811cdd0` "fdsf edet sef fs e se ee e" scored 4. `fe99a06f` "yfuhjyfytht" scored 4. `4094228c` "hjkjhk" scored 5. `ba19e403` an Arabic line of affection with no product content, scored 5. All four inflate the average.
- **17 non-delivery reviews (12.2% of 139).** People rating a company they never bought from in practice. Listed in Objections below.
- **3 rows are customer service tickets, not reviews.** `f57c33a4` "How do I get it shipped overnight?" scored 5. `2d91c9d1` from a person who says they cannot afford one and never bought it, scored 5. `12ad9190` is a complaint that a review request arrived before the product shipped, scored 1.
- **3 reviewer names appear twice.** peter balestrieri (twice on Hoolest Pro), daniel (twice on the Bundle), Kathleen Lestition (once on Hoolest Pro, once on the Gel Tip Subscription). All six are distinct reviews with different text. **0 merged.**
- **The export is not the brand's complete review history (inferred).** Row `3374e231` opens "Already left a 5 star review but as of today it has been 10 days," and there is no other row by that reviewer in the 139. So at least one earlier review exists outside this corpus.
- **No encoding cleanup was applied upstream.** Several rows carry mojibake such as "I‚Äôve" and "üòä" where curly quotes and emoji should be. Preserve verbatim; do not silently fix.

### Ad comment corpus (n=6,562 raw, 6,077 customer language)

**Fields present by default:** `comment_id`, `author_name`, `message`, `created_time`, `like_count`, `comment_count`, `permalink_url`. Available on request via `fieldsToInclude`: `ad_ids`, `ad_names`, `post_ids`, `parent_comment_ids`, `facebook_comment_ids`, `snapshot_date`, `author_id`, `comment_length`. **The ad attribution is real and it works** — a comment can be tied to the exact ad name that drew it, which is a gift for a hook or objection read. It just is not in the default response, so ask for it.

**Populated share (n=6,562):**

| Field | Populated | Share |
|---|---|---|
| `comment_id` | 6,562 | 100% |
| `created_time` (real date) | 6,562 | 100% |
| `message` with any text | 6,492 | 98.9% |
| `permalink_url` | 6,180 | 94.2% |
| `like_count`, `comment_count` | 6,562 | 100% |
| `author_name` | 457 | 7.0% |
| `author_id` | 0 | 0% |

`author_name` fills in only for Facebook Pages. Personal profiles come back null. That means **no repeat-commenter detection and no per-person deduplication is possible** on 6,105 of 6,562 rows (93.0%).

**Who wrote them (verified):** 415 of 6,562 (6.3%) are the Hoolest page replying to customers. 42 more are named business pages, of which the largest is "Nicole x UGC" at 6 comments. The remaining 6,105 are anonymous individuals.

**Normalization decisions:**
- Removed 415 brand replies. Brand text is not customer voice. It is useful separately as a record of what the brand tells people, and several of those replies are the clearest plain-English explanations of the mechanism anywhere in the corpus.
- Removed 70 blank-message rows (1.1% of 6,562). None of them were brand rows.
- **Result: 6,077 customer-language rows. This is the denominator every ad comment percentage in this document uses.**

**Deduplication:** 2 rows share both message text and permalink with another row ("I need one" and "Fixin to put 2 thc gummies on a 9 volt"). Both carry distinct `comment_id` values and, with `author_id` null, there is no way to prove they are the same person rather than two people typing the same short thing on the same post. **0 rows merged.** Beyond those two, 6,282 distinct message strings cover 6,492 non-blank rows; the repeats are short generics like "Reset" (30 rows) and "All of them" (12 rows), which are genuine separate comments.

**Shape of the text:** median length 49 characters, mean 96, longest 3,612. 1,123 of 6,077 (18.5%) are 20 characters or shorter. 588 of 6,077 (9.7%) run 200 characters or longer. **The long tail is where the usable language lives, and it is under a tenth of the corpus.**

**Thread structure:** 4,064 of 6,077 (66.9%) are top-level comments, 1,634 (26.9%) are replies, and 379 (6.2%) cannot be classified because the permalink is null. The reply share matters: a quarter of this corpus is customers arguing with each other, answering each other's questions, and vouching for the product to a stranger. That is peer-to-peer proof, and it reads differently than a review.

**Volume over time (verified, real `created_time`):**

| Period | Comments |
|---|---|
| 2024 (Aug-Nov) | 211 |
| 2025 | 1,770 |
| 2026 (Jan 1 - Sep 8) | 4,581 |

| Month | Comments | Month | Comments |
|---|---|---|---|
| 2025-09 | 172 | 2026-03 | 1,084 |
| 2025-10 | 95 | 2026-04 | 479 |
| 2025-11 | 123 | 2026-05 | 522 |
| 2025-12 | 269 | 2026-06 | 394 |
| 2026-01 | 353 | 2026-07 | 694 |
| 2026-02 | 474 | 2026-08 | 512 |
| | | 2026-09 (8 days) | 69 |

March 2026 is a real spike, 1,084 comments in one month against a 2026 monthly average of roughly 540. That is more than double. **Something happened in March 2026** — a scaled campaign, a viral placement, or a creative that drew argument. Worth a look from the ad account side.

### Post-purchase surveys (n=0)

Called `semantic_search_post_purchase_survey` in lookup mode with no query, `topK: 50`, brand filter only. Response: `results: []`, `count: 0`, `uniqueResponses: 0`, `totalResponsesForBrand: 0`, `collectionExists: true`. The tool's own message: "This brand has no post-purchase survey responses yet."

**This is not a query problem or an access problem. The collection is live and it is empty for Hoolest.** It matches what `running-notes/missing-context.md` already logged on 2026-09-08. To fill it the brand needs a KnoCommerce or Zigpoll connection, or a CSV upload of an existing survey.

**What the zero forbids downstream, said plainly:**
- No NPS, no promoter or detractor segments, and no NPS-segmented language.
- No "how did you hear about us," so no first-party attribution and no read of whether purchases come from ads, word of mouth, a clinician, or search.
- No purchase trigger tied to a real buyer at the moment of purchase.
- No first-time vs returning buyer split.
- No pre-purchase consideration set, so "who else did you look at" stays a guess.
- Persona confidence is capped. Per the persona method, survey data is the top evidence tier and reviews sit a tier below it. **Every Hoolest persona built from this corpus is one confidence band lower than it would otherwise be, and should say so.**

### TikTok library (n=20 videos, 0 customer-language records)

20 videos, confirmed by `total: 20` across two pages of 10 (**verified**). All 20 were ingested on 2026-09-07. Video post dates run 2021-09-09 to 2026-08-08.

**None of the 20 are Hoolest's own content and none are from Hoolest customers.** They come from 19 distinct creator handles (only `@drjoe_md` appears twice). The mix:

- **16 of 20 (80%)** are unaffiliated educational or creator content about the vagus nerve, panic, racing thoughts, and nervous system regulation. Examples: `@drjoe_md` on panic attacks (1.1M plays), `@fascialmaneuvers` on a manual vagus nerve release (444K), `@taytrace` on nervous system exercises (373K).
- **4 of 20 (20%)** are competitor-owned or competitor-sponsored: `@apolloneuro`'s own account, `@henry.ugc` running an Apollo Neuro affiliate post, `@jodie_lynnofficial` on a gifted Pulsetto post, and `@alispagnola` testing Pulsetto against her HRV.

Those 20 videos carry **1,625 comments between them** (sum of `comment_count`), and **not one comment body is retrievable through `search_tiktok_videos`**. The tool returns the caption, the engagement counts, an AI relevancy note, and media URLs. No comment text.

**Characterise it honestly for downstream: this is a competitor and format swipe file, not a voice-of-customer surface.** It belongs to the creative-strategy and competitor work. **No VoC slice should count a TikTok record toward any language denominator.** If Hoolest wants customer language off TikTok, the 1,625 comments sitting on those 20 videos are the obvious first pull, and Parker cannot reach them today.

---

## Normalized schema

Everything above was mapped into one record model so downstream slices read one shape. Fields marked **structured** came straight from a source field. Fields marked **model-inferred** were assigned by reading the text and must never be quoted as something the customer supplied.

| Normalized field | Reviews | Ad comments | Type |
|---|---|---|---|
| `row_id` | `id` (uuid) | `comment_id` (uuid) | structured |
| `source_type` | `review` | `ad_comment` | structured |
| `platform` | unknown; `type` reads `csv_import` on all 139 | Facebook | structured, but reviews are unresolved |
| `source_native_id` | none | `facebook_comment_ids[]` | structured |
| `date` | **absent.** `created_at` is the 2026-09-07 import stamp | `created_time`, real, 2024-08-09 to 2026-09-08 | structured |
| `rating` | `score`, 1-5, all 139 | none | structured (reviews only) |
| `product_sku` | `product_title`, all 139 | **absent** at row level; `ad_names` is the nearest handle | structured (reviews only) |
| `text` | `title` + `content` | `message` | structured |
| `url` | none | `permalink_url`, 6,180 of 6,562 | structured |
| `author_display` | `reviewer_name`, all 139 | `author_name`, 457 of 6,562 | structured |
| `author_stable_id` | none | none (`author_id` null everywhere) | absent |
| `engagement` | none | `like_count`, `comment_count` | structured |
| `campaign_ref` | none | `ad_ids[]`, `ad_names[]`, `post_ids[]` | structured (ad comments only) |
| `thread_position` | none | derived from `parent_comment_ids` / permalink | structured |
| `sentiment_band` | derived from `score` | **not derivable** | structured (reviews only) |
| `theme_tags` | keyword and record-level read | regex | **model-inferred** |
| `record_class` | product review / non-delivery / support ticket / junk | n/a | **model-inferred** |
| `age`, `gender`, `region`, `first_time_buyer`, `occasion`, `channel`, `device` | **absent** | **absent** | absent on every record |

**The most consequential line in that table is `product_sku` on ad comments.** A comment cannot be tied to a SKU. It can be tied to an ad, and the ad name usually implies a SKU (`HPT009_VID_Authority Mash Up_3C_VeRelief Prime_...` clearly points at VeRelief Prime; `PEMF_Product-Demo_V1_Mar-29th 2026` points at the PEMF line). But that is an inference off a name, and per the method a name is an inventory handle, not proof. **If a downstream slice needs a SKU-level read of ad comments, it must pull the creative itself, not read the ad name.**

---

## Classification method

Three passes ran. Each is named here so a downstream doc knows exactly what it can lean on.

**Pass 1 - structured facts.** Star score, product title, comment date, like count, reply count, ad ids and names, permalink. These came from source fields. Nothing was inferred. Sentiment bands on reviews (positive 4-5, neutral 3, negative 1-2) come straight off the score, so they count as structured too.

**Pass 2 - record-level reading of all 139 reviews.** Every review was read in full, body and all, not just the title. That is where the non-delivery count, the junk count, the support tickets, and the twelve real product complaints come from. These are **model judgments made against the full text of every record**, which is the strongest form of model tag available here because the corpus was small enough to read whole.

**Pass 3 - keyword and regex theme tags.** On reviews, the Parker SQL tool ran ILIKE matching across title and content for all 139, returning both a match count and the average score of the matching set. On ad comments, case-insensitive regex ran across all 6,077 customer rows. **These are model-applied tags. They are recall-biased and they will over-count.** For example, an early attempt to count work and focus mentions in reviews using the token `work` returned 41 of 139 because it caught every "it works." Tightened to `focus, focused, meeting, presentation, golf, workout, productive, concentrate, desk, at work, before work, my job`, the real count is 14 of 139 (10.1%). **The lesson generalises: check the pattern against the text before quoting the number.**

The exact keyword lists and regex patterns used are printed alongside each count in the sections below, so any slice can reproduce or tighten them.

**Pass 4 - the one that failed, reported as a failure.** A lexicon sentiment pass on the 6,077 customer ad comments classified 326 rows (5.4%) positive and 310 (5.1%) negative, with 15 rows hitting both lists. That leaves **5,456 of 6,077 rows (89.8%) unclassified**. A tag that cannot reach nine rows in ten is not a measurement. **There is no ad comment sentiment split in this corpus, and no downstream doc may report one.** What ad comments do support is objection and question counting, which is what the sections below do.

**Tags that are unavailable at any confidence:** gift vs self-purchase on ad comments, recipient relationship, occasion, buyer type, region, device, channel, age, gender, first-time vs returning, and lifetime value. No source field carries them and the text almost never volunteers them.

---

## Sentiment and rating profile

### Reviews (structured, n=139)

| Band | Count | Share of 139 | Avg score |
|---|---|---|---|
| Positive (4-5) | 107 | 77.0% | 4.92 |
| Neutral (3) | 3 | 2.2% | 3.00 |
| Negative (1-2) | 29 | 20.9% | 1.24 |

**By SKU, top three only (the rest are thin and marked as such):**

| SKU | n | Avg | Read |
|---|---|---|---|
| VeRelief Prime Gen 2 | 17 | 4.88 | Highest-rated SKU with meaningful support. Zero non-delivery reviews in the set. |
| VeRelief Mini | 39 | 4.51 | The volume SKU on the review side. |
| VeRelief Prime - Lasting Relief Bundle | 45 | 3.40 | 13 of 45 (28.9%) never received the order. The score is a fulfillment score. |

**Every other SKU is thin: 7 or fewer reviews each.** VeRelief Prime (7), VeRelief Pro (6), Hoolest Pro (6), Hoolest Sleep (5), Vagus Nerve Activator Gels (4), Gel Tip Subscription (4), the 30-day gel supply (2), Small Electrodes (1), VeRelief RESET (1), Route Package Protection (1), MiniMax GO (1). **Do not write a SKU-level pattern off any of those.** Individual quotes from them are still usable.

**Sentiment by time period: data-limited.** All 139 reviews group into one month bucket, 2026-09, because the date field is the import stamp. There is no trajectory read available on reviews. **If a downstream doc needs "is sentiment improving," it must use ad comments or wait for dated reviews.**

**Sentiment by source: data-limited on reviews.** All 139 carry `type: csv_import` with no platform split, so owned-site reviews cannot be separated from marketplace or retail reviews. Given that a commenter says on 2026-08-02 "I got mine from Amazon, BTW," Amazon reviews exist somewhere and are not here.

### Ad comments

**Data-limited.** See Pass 4 above. No rating field, and 5,456 of 6,077 rows (89.8%) carry no verdict language. What can be said with evidence: 190 of 6,077 (3.1%) explicitly say they own it and it works, and 241 of 6,077 (4.0%) use scam, snake oil, BS, placebo, fake, gimmick, or nonsense. Those are two floors, not a split.

### Strongest positive theme

Speed of felt effect, and it recurs across both surfaces. In reviews the language is consistently about minutes, not weeks. From `2d7a92e0`, 5 stars, VeRelief Prime Bundle: "I've had mine for 3 months and I am astounded that it actually works. For some reason I have a lot of anxiety in the early mornings. I can calm myself down, feeling immediate relief in seconds." From `8b2cb4a6`, 5 stars, Prime Gen 2: "I love this device because it takes me to a calm state within 2 minutes :-)"

### Strongest negative theme

Fulfillment, by a wide margin, and it is a company problem rather than a product problem. 19 of 139 reviews (13.7%) hit the shipping keyword set (`shipping, ship, never received, haven't received, back order, backorder, tracking, delivery, not received`), and that matching set averages **2.16 stars against a corpus average of 4.11** (**verified**, tool-computed). No other theme in the corpus drags the score like that.

---

## Motivation and trigger profile

**Read this section knowing the strongest evidence tier is missing.** With 0 post-purchase surveys, nobody in this corpus was ever asked why they bought. Everything below is what people volunteered on their own, which skews toward the dramatic and the recent.

### What people say brought them (reviews, n=139)

| Motivation cluster | Keywords used | Count | Share of 139 | Avg score of matches |
|---|---|---|---|---|
| Anxiety and panic | anxiety, anxious, panic, anxiety attack | 35 | 25.2% | 4.71 |
| Sleep | sleep, insomnia, asleep, bedtime, before bed | 38 | 27.3% | 4.87 |
| Avoiding or getting off medication | medication, meds, benzo, Xanax, Ativan, antidepressant, drugs, pharmaceutical, without drugs, prescription | 16 | 11.5% | 4.94 |
| Clinician or practitioner in the story | doctor, physician, chiropractor, therapist, clinician, my provider, clinic, patients, counseling, practice, practitioner | 14 | 10.1% | 4.29 |
| Serious diagnosis named | PTSD, trauma, veteran, Long Covid, fibro, ME/CFS, chronic fatigue, Lyme, Crohn, seizure, brain injury, concussion, stroke, dysautonomia | 14 | 10.1% | 4.43 |
| Wearable or HRV data | HRV, heart rate variability, Oura, Whoop, wearable, Apple health, Welltory, Pixel watch | 9 | 6.5% | 4.44 |
| Comparison shopping against another device | Truvaga, Pulsetto, Sensate, Apollo, Neuvana, Nurosym, gammaCore, TENS, Xen | 11 | 7.9% | 4.64 |
| Focus, work, or performance | focus, focused, meeting, presentation, golf, workout, productive, concentrate, desk, at work, before work, my job | 14 | 10.1% | 4.71 |

The medication cluster deserves attention out of proportion to its size. 16 of 139 is not huge, but it averages **4.94 stars**, the highest of any cluster measured. These are the most satisfied customers in the corpus, and the thing they have in common is that the device let them avoid a pill. From `0bf05a14`, 5 stars, VeRelief Mini: "I purchased Hoolest VeRelief Mini and it's been life changing... I've been able to wean off of anxiety medication and I have a peace that I've never experienced before."

### The final-straw trigger

**Data-limited but visible in the long reviews.** The corpus does not let this be counted, because a trigger is a story and most reviews do not tell one. Where it does appear, it is an acute episode, not a slow decision. Three examples, all verbatim:

- `b2edd196`, 5 stars, Prime Bundle, titled "Don't Be That Guy": "I was the victim of some horrible road rage.  I was so emotionally shaken I was looking for anything to re-balance my nervous system.  I could not sleep or even focus."
- `e97a283a`, 5 stars, VeRelief Mini: "I purchased this device in total desperation, having suffered from the effects of a souped up sympathetic nervous system for years."
- `7163c172`, 5 stars, Prime Bundle: "I did a bunch of research, and ffinally bought the Hoolest VeRelief Prime because I've got some experience with manual stimulation of Vagus nerve ( chanting, humming, breathwork), very much believe in the science, but I needed a hack to make it more convenient and accessible and effective to affect real change in my life. And lemme tell ya... I am DESPERATE for something to change for the better."

The word desperate shows up unprompted in two of those three. **Marked thin** — this is a pattern of three, not a counted theme. **Flag it for the trigger-moment slice to hunt properly.**

### Referral and word of mouth

28 of 139 reviews (20.1%) hit the recommendation keyword set (`recommend, tell everyone, told my, telling others, share this, everyone I know`), averaging 4.61. The interesting sub-pattern is that referral in this category runs through professionals as often as friends. From `18ff2df0`, 5 stars, Mini: "A friend of mine got a VeRelief Mini and after I tried it I immediately ordered one for myself." From `3aff05af`, 5 stars, VeRelief Pro: "I first used a VRelief mini at my chiropractor's office. After a minute I knew that I had to get one!" From `cc7031b0`, 5 stars, Prime Bundle: "My mental healthcare provider lent me this to see if it would help me."

**The try-it-once-then-buy loop is the clearest purchase mechanic in the corpus (inferred from those three plus `2da0cba4`, "I can't believe this little device actually works. I tried it a couple times and had to buy my own.").** Four records. **Thin, but consistent, and it points at a demo or trial play.**

### Ad comment motivation signals (n=6,077)

| Signal | Regex | Count | Share of 6,077 |
|---|---|---|---|
| Anxiety, panic, stress, fight or flight | `anxiet\|anxious\|panic\|nervous system\|fight.?or.?flight\|stress` | 488 | 8.0% |
| Sleep | `sleep\|insomnia\|fall asleep\|wake up\|bedtime\|rest` | 114 | 1.9% |
| Purchase intent | `where (can\|do) i (buy\|get)\|link\|ordering\|just ordered\|i want one\|need one\|buying\|order(ed)? (one\|mine)\|sign me up` | 106 | 1.7% |
| Medication context | `medication\|meds\|benzo\|xanax\|ativan\|klonopin\|ssri\|antidepressant\|prescription\|pharmaceutical\|drugs` | 86 | 1.4% |
| PTSD, trauma, veteran | `ptsd\|trauma\|veteran\|combat` | 74 | 1.2% |
| Kids, ADHD, autism | `adhd\|autis\|asd\|my (son\|daughter\|kid\|child)\|kids?\|teen` | 74 | 1.2% |
| Long Covid, ME/CFS, fibro, chronic illness | `long ?covid\|me/?cfs\|chronic fatigue\|fibro\|dysautonomia\|pots\|lyme\|autoimmune\|crohn\|ibs\|ibd` | 69 | 1.1% |
| Migraine or headache | `migraine\|headache` | 38 | 0.6% |
| Tinnitus | `tinnitus\|ringing in (my\|the) ears` | 34 | 0.6% |

**Tinnitus is the interesting one.** 34 mentions is small against 6,077, but Hoolest does not advertise tinnitus, and people keep bringing it up unprompted, including "Can you make some for tinnitus sufferers please?" (`77f48286`, 2025-04-02) and "Great idea. Keep going and fix my tinnitus that is not from my ears." (`67646358`, 2025-04-08). **Marked thin at 34 of 6,077 (0.6%), and worth a look as an unserved use case.**

---

## Gifting, usage, and occasion profile

**This is not a gifting category, and the data says so clearly.**

**Reviews:** 1 of 139 (0.7%) hits the gift-occasion keyword set (`gift, Christmas, birthday, holiday, present for, stocking`). One. **Ad comments:** 7 of 6,077 (0.1%) hit `gift|christmas|birthday|stocking stuffer|present for`. **Verified across both surfaces.** No downstream doc should build a gifting angle off this corpus, and no seasonal creative plan should claim customer-language support from it. If the brand believes gifting matters, that belief has to be tested against order data, not asserted from VoC.

**What does happen instead is buying for a specific person with a specific problem.** 19 of 139 reviews (13.7%) hit the buying-for-someone keyword set (`my son, my daughter, my husband, my wife, my boss, for my, gift, bought for, my child, my kid, my family, my partner, my mom, my boyfriend`), averaging 4.68. In ad comments, 13 of 6,077 (0.2%) match a tighter version of the same idea. **The review-side count is the usable one.**

The recipients that recur, read at record level:

- **A child.** `a5b154e5` on a young son with daily anxiety, `8d74d857` on an 8-year-old who takes it to school for anxiety attacks, `51a68e6b` on a son with severe sports anxiety, `85694751` on a son with a brain injury, `fda243fc` on a son whose clinician recommended it.
- **A partner or spouse.** `7881441f`, 5 stars, VeRelief Pro: "I was able to purchase the VeRelief Pro for my high-stress husband.  G A M E -C H A N G E R!!! ... He came home in full Hulk Mode and 15 minutes later was Bruce Banner!"
- **A colleague or boss.** `f5046631`, 4 stars, Prime Gen 2: "I bought this for my boss, she gets migraines and is not functional during a HA."
- **Clients or patients.** Six reviews come from practitioners buying for professional use, including a clinic, a counseling practice, and a company that makes an HRV system.

**Recipient reactions: thin.** Only a handful of reviews report what the recipient said, and the Hulk to Bruce Banner line is the one worth keeping.

### Where and when it gets used

| Setting or occasion | Evidence |
|---|---|
| Before bed | 38 of 139 reviews (27.3%) hit the sleep keyword set |
| At a desk, at work, before a meeting | 14 of 139 (10.1%) hit the tightened focus set |
| In public, without anyone noticing | `9f312bc3`: "Especially when out in public and you are not able to 'close your eyes and do your breathing exercises' to calm down ( example: out to dinner with friends at a restaurant ) you can just whip this puppy out and continue to be at the table ( or office mtg...)" |
| Travel | `55401851`: "I was able to take VeRelief Mini through TSA with no issues whatsoever." |
| Around workouts and sport | `eb5f0276` uses it around workouts; `42083493` is a golfer on chipping and putting |
| During an acute episode | `95bda524`, `cc7031b0`, `809efeb7` all describe use mid-panic |

**Portability is the most-praised physical attribute.** 20 of 139 reviews (14.4%) hit `pocket, purse, portable, take it with me, everywhere, discreet, travel, on the go, compact, small`, averaging 4.75.

**Repeat purchase:** 10 of 139 (7.2%) hit `bought a second, second one, another one, bought two, 3 units, purchased 3, subscription, reorder, buy another, life long customer`, averaging 4.20. **Marked thin, and note that the average is dragged by gel tip subscription complaints landing in the same keyword net.** No LTV or true repeat-rate read is possible without order data.

---

## Objections and barriers profile

This is the richest section in the corpus, because ad comments are where objections live.

### 1. Skepticism and demand for proof (the biggest one)

**241 of 6,077 ad comments (4.0%)** use `scam|snake oil|BS|bullsh|placebo|fake|gimmick|hoax|nonsense|doesn't work|no benefit|waste of money|rip-off|grift`. Separately, **159 of 6,077 (2.6%)** name `FDA|clinical|study|studies|research|peer-review|evidence|approved`. In reviews, 10 of 139 (7.2%) hit the skepticism set, averaging 3.10.

The proof demand is the most-liked comment in the entire corpus:

> "I'd like to see the clinical studies that show the safety and efficacy of this device."
> `e97c5f9e` | 214 likes | 2026-02-23 | on ads named "Flex PEMF", "Minimax post id - 3", "PEMF_Product-Demo_V1_Mar-29th 2026"

And the sharper versions:

> "Why has your research not been submitted for peer review? It could make great strides in the veteran community but without the correct research, data, and backing, it would not be funded."
> `fa028e74` | 7 likes | 2026-07-08

> "Save your money, folks. Externally applied devices lack efficacy. Implanted devices are more effective, but still limited to a few areas where they can help. If he thought it was effective, he would have sought FDA approval."
> `6e17e703` | 3 likes | 2026-01-04

> "💯 BS Junk Science"
> `d8b7399f` | 57 likes | 2026-03-16

> "Essential Oils 2.0"
> `1eab748a` | 80 likes | 2026-01-27

**The founder story is itself being attacked**, which is a specific and actionable finding:

> "\"I was a competitive golfer with bad performance anxiety and all they would do is prescribe me benzodiazepines, so I got my PHD in biomedical engineering.\" / / Ok, sure pal. That's how it all happened."
> `02c95378` | 47 likes | 2026-05-30

### 2. Price, and specifically the recurring cost

**432 of 6,077 ad comments (7.1%)** touch price. **129 of 6,077 (2.1%)** name gel tips, electrodes, or activators. In reviews, 16 of 139 (11.5%) mention price and 17 of 139 (12.2%) mention the consumables, the latter averaging 3.76.

The sticker objection:

> "First of all most people can't afford this! So it's a no for me. Thanks for making it hard to try something that might help… next"
> `b68e989d` | 37 likes | 2025-05-16

> "I have had panic attacks and anxiety attacks for yrs.. the only thing they give me are antidepressants which if im still getting the attacks their not working.. after 34 yrs of them I'd love some relief .. but can't afford 400 bucks.."
> `8e1706ac` | 7 likes | 2025-09-12

The recurring-cost objection, which is the sharper one:

> "Jerry Nesseler it costs $50 a month for electrodes. Every month.  That's why i returned mine."
> `cc820df4` | 2 likes | 2026-01-12

> "Naw dude, chill with that. Yes, your ve relief stimulator is absolutely the best. But you can't say that your gel tips are 11 dollars a month and the other companies gel tube is 10 a month because that gel tube lasts a whole damn 3 years lmao"
> `fdce53d5` | 4 likes | 2026-07-21

> "Jeff Maina I totally agree with you,  I like my devise but the gel tips need to be replaced too often, and they are expensive"
> `49a798f7` | 2 likes | 2026-06-26

And from the reviews, `1c51eda0`, 2 stars: "I purchased the Mini Hoolest & am VERY disappointed in how long the gel tips last. You say up to 20 uses?  I barely get 2 uses out of them & they are so expensive!  I love how it works when I put a new pair in & would love to use it daily but the 2nd time I try to use them the unit barely works.  Would not recommend for the price!"

**The gel tip lifespan claim is being publicly contradicted by customers, and the brand's own reply in the corpus states the claim: "Each pair lasts up to 7 days or after 20 uses, whichever comes first."** That gap is a live claims risk. Per the review-mining governors, any nugget resting on gel tip longevity is **gated**, not clear.

### 3. HSA, FSA, and insurance friction

**96 of 6,077 ad comments (1.6%)** name `hsa|fsa|insurance|truemed|medicare|medicaid|reimburs`. This is a price objection wearing a different hat: people want the device and want someone else to pay.

> "I was so interested and had a panic attack when I saw the price 😅 Do you accept insurance?"
> `e0c53cde` | 18 likes | 2026-08-21

> "Fix your Truemed link so I can use my HSA/FSA Card"
> `07314610` | 2 likes | 2026-07-27 (this exact sentence appears 4 times in the corpus)

> "Bro this is FSA ELIGIBLE but the one I got don't accept it and it's a NBS FSA card DO BETTER MAN"
> `8ee76da7` | 0 likes | 2026-09-02

**There is a working answer in the corpus that the brand is not amplifying.** From review `7163c172`: "You may even be able to use HSA/FSA funds. I just applied for a \"Boost\" Letter of Medical Necessity online, which took less time than writing this monster review, cost $25...  et voila! No $ out of pocket, reimbursed, and saved about 30% usung pre-tax monies."

### 4. Fulfillment and delivery (the review-side killer)

**17 of 139 reviews (12.2%) are from people who never received the product**, and all 17 sit in the 1-2 star band. That is **58.6% of all 29 negative reviews**. In ad comments the same complaint is rare, 35 of 6,077 (0.6%), because ad comments come from people who have not bought yet.

The full non-delivery set, by row id: `e24646a0` (2★), `ede1a99e` (1★), `56304cd9` (1★), `10b05523` (1★), `4b879c8f` (1★), `05ada83a` (1★), `9f3bb264` (2★), `9b6a2a2e` (1★), `1d84bec0` (2★), `5e3f2b38` (1★), `d4f45942` (1★), `ec5246db` (1★), `11329b2e` (1★), `06473e1b` (1★), `23181ec0` (1★), `12ad9190` (1★), `ecd3e81c` (1★).

The most damaging one is the longest, and it names a competitor as the alternative:

> "This is not a legitimate company. Their office address is a house in Arizona, and they operate out of a garage, as indicated in their annual report filed this year. Last year, they were sued for patent infringement. / I ordered this device over 45 days ago... After making me wait 45+ days—during which time I could have obtained and used a Truvaga device—they canceled my order... P.S. I have been suffering from Long COVID for over a year. Vagus nerve stimulation is the only thing that gives me relief. My doctor recommended this device."
> `11329b2e` | 1 star | VeRelief Prime - Lasting Relief Bundle

And the process complaint that shows up repeatedly, which is being asked for a review before the product arrives:

> "Haven't received the product yet because of shipping issues and already wanting a review very interesting tactic"
> `1d84bec0` | 2 stars

**Treat this as a review-request timing problem as much as a shipping problem.** The brand is generating its own 1-star reviews by soliciting them before delivery.

### 5. Competitor comparison, especially Pulsetto and hands-free

**73 of 6,077 ad comments (1.2%)** name a competitor. **88 of 6,077 (1.4%)** compare it to a TENS unit. In reviews, 11 of 139 (7.9%) name a competitor, averaging 4.64.

The comparison request is unusually specific and it lands on the same feature every time, which is having to hold the device:

> "What are the differences or similarities between your product and Pulsetto? ￼ The one feature that I may like is that  Pulsetto allows hands-free treatment which to me would seem a little bit more relaxing than having to hold the device for 10 minutes, etc. But besides that what are the differences"
> `14cb68d5` | 14 likes | 2026-07-16

> "I really want more information, and I want a study or at least an honest comparison between this and pulsetto"
> `39349847` | 6 likes | 2026-01-11

> "I wonder why he designed it that you have to hold it? It would be more relaxing if you did not have to hold it. Pulsetto's is worn around the neck, but I am trying to figure out which one has the best results. Anyone?"
> `9ad1c12d` | 2 likes | 2026-07-24

**33 of 6,077 (0.5%)** raise the hands-free wish directly (`hands.?free|hold it|wear it|around (the|your) neck|while (i|you) (work|sleep|drive)`). **Marked thin as a count, but it recurs inside the competitor comparisons, which is where it does damage.**

When Hoolest wins the comparison in customer words, the reason is price and session limits:

> "Amazing product, using 8hz frequency to heal my IBD (Crohns) and 25hz frequency for sleep and anxiety. It works really good. Just be consistent. A 100% better option than Truvaga as it is affordable and allow unlimited session. And the stimulation is felt better than Truvaga as well."
> `7d57ad51` | 5 stars | VeRelief Prime Gen 2

### 6. Safety and contraindication questions

**197 of 6,077 ad comments (3.2%)** raise `pacemaker|safe|safety|seizure|epilep|pregnan|contraindicat|side effect|heart condition|afib|stent|implant`. These are almost all sincere questions from people who want to buy, not attacks. Two of the three most-liked comments in the entire corpus are in this cluster, and both are people with implanted VNS devices:

> "I have epilepsy so I have a vagus nerve stimulator implant and it doesn't help my seizures unfortunately, but it has been great for helping my anxiety! So I think this would be helpful for people who don't qualify for a VNS."
> `e06689c5` | 93 likes | 2026-08-23 | on ad "HPT052_VID_Nick Trial Reels_2B_VeRelief Prime_AI VO_Wired Lifter"

> "This genuinely sounds phenomenal, my daughter has a VNS device implanted for her seizures and it works wonders for her. I have done a lot of research on the VNS and mental health and its benefits, however, it is nearly impossible to get one for that sole purpose. This seems like a very attainable way for anyone who may need this for mental health purposes and they are unable to get a VNS implant."
> `ed29dfcb` | 87 likes | 2026-05-28 | on ad "HPT009_VID_Authority Mash Up_3C_VeRelief Prime_Mashup_CSuite Operator"

**The single highest-engagement positive framing in this corpus is "the implant you cannot get, in a form you can."** That is a customer's framing, not the brand's, and it is sitting there earning 87 and 93 likes.

### 7. Product confusion and how-to questions

**129 of 6,077 (2.1%)** ask how it works. **232 of 6,077 (3.8%)** ask about ear or neck placement, which side, or where to put it. **1,593 of 6,077 (26.2%)** contain a question mark at all.

Recurring confusions worth naming: how often to change the tips, whether it needs gel when the ads say it does not ("Why do you sell gel when you advertise it doesn't need it?", `b749d65b`, 2026-09-05), and left side versus right side ("I thought clinical advice was to use the left side of the neck, not the right side.", `27a7aa5b`, 2026-09-06).

### 8. Device reliability

**5 of 139 reviews (3.6%)** hit the defect keyword set, averaging 3.00. **Marked thin.** But the failures described are the same failure: `ea09a330` "Stopped working after 10 uses," `32b875fc` "my buttons don't work without lots of pushing and holding and now it doesn't seem to work at all, but the lights come on," `ef9eeecc` "The equipment does not work." And from ad comments, the warranty jab: "\"built to last\"...\"2 year warranty\". Built to last 2 years then best of luck!" (`154a28d3`, 60 likes, 2026-04-03).

**Balance it honestly.** The corpus also contains the opposite: "I love mine! The company is legit too. My first one stopped working and they sent another out! They back their product!!" (`b1ccb40d`, 20 likes, 2026-01-27).

---

## Product experience and outcome profile

### What gets praised (reviews, record-level read)

**Speed of effect.** The most consistent praise in the corpus, and it comes with numbers. From `2d0cba4`-adjacent record `2da0cba4`, 5 stars, Mini: "Every hour or so I bust it out for a 4 minutes session (2 minutes, or 6 cycles on each side of my neck)." From `e97a283a`, 5 stars, Mini: "I administered on both sides for about 2 minutes each (too tired to incorporate the breathing) and when I put it down, the pounding was GONE... That's generally the effect from a good 15 minutes of box breathing. All done in less than 5, and no effort by me."

**Size and discretion.** 20 of 139 (14.4%). Covered above.

**No gel required, versus the older way.** From `8d80814a`, 5 stars, Prime Gen 2: "It comes with removeable electrodes as opposed to the ultrasound gel which is required for other VNS devices. For the last several years I had been using the GammaCore VNS which is VERY expensive (5K) and requires using the goopy gel. In contrast the Hoolest is much easier and I have actually been using it several times a day since it is more convenient."

**Mode and frequency range.** From `f693da14`, 5 stars, Prime Gen 2: "This is by far the best engineered device so far. It works. I especially like the gel nubs that are already hydrated so you don't have to use messy gels. The 5 different intensity levels, and ability to trigger different nerves is also a superior feature."

**Customer service, when it goes right.** From `6597fcfa`, 5 stars: "the customer service i have received from Ve Relief has been extraordinary. fast efficient and nothing is a problem for them. the mark of a great company."

### What gets criticised

The 12 product-experience negative reviews, read in full. This is the complete list, which is worth stating plainly because it is small:

| Row | Score | SKU | The complaint, in their words |
|---|---|---|---|
| `ae5453ab` | 2 | Mini | "Hard to actually get it to work correctly , and when you do their is no noticeable difference . You're just more stressed because you are sitting there shocking yourself for no reason . Cool idea , the video is compelling, the reality is underwhelming." |
| `4ac6452a` | 1 | Mini | "This device has no effect on me." |
| `2bfaeb63` | 1 | Mini | "I have Long Covid and there is a lot of talk about vagus nerve stimulation. Using this product didn't help me in any way... Also the electrodes wear down super fast. They didn't last a day with 2 uses, let alone a week." |
| `474c279c` | 1 | Mini | "Very, very, very unpleasant sensation. Engages instant fight or flight, opposite to its purpose," |
| `1c51eda0` | 2 | Bundle | Gel tip lifespan and cost, quoted in full above |
| `c35fcf12` | 1 | Bundle | "The build quality of the device is cheap and the gel, accessory tips, and accessories are far overpriced. Customer service has been terrible, shipments come in late." |
| `ea09a330` | 1 | Bundle | Battery failed after 10 uses; charged a repair fee |
| `fda243fc` | 1 | Bundle | "the soft tips are a hazard... After sales is what sets companies apart imo" |
| `cef8bd58` | 1 | Gel Tip Subscription | "The gel tips themselves work fairly well thought they have a limited life span. The cost of the tips and the cost of shipping feels extreme." |
| `bcd00121` | 1 | Hoolest Sleep | "Gives me a very disturbed night of sleep. Sleep metrics as measured by my wearable confirm." |
| `32b875fc` | 2 | Bundle | Buttons stopped responding |
| `ef9eeecc` | 2 | VeRelief Prime | "The equipment does not work ." |

**Two patterns run through that list.** First, when the device fails, it fails silently for that person: it just does nothing. Four of the twelve say a version of "no effect." Second, the gel tips are named in three of twelve. **Marked thin at 12 records, and treat it as a set of examples rather than a rate.**

### Expectations missed in a specific way: the learning curve

Several positive reviews contain a hidden complaint, which is that the device takes practice. From `a85c51fc`, 4 stars, Mini: "After an initial adjustment period during which I had to learn how to use it and get used to the way it feels, I am finding the VeRelief Mini to be helpful." From `8619190d`, 5 stars, Bundle: "It does take some learning on placement, intensity and mode." From `0bf05a14`, 5 stars, Mini: "I have to admit, sometimes finding the right spot to place it can take a second." From `f2912e97`, 3 stars, Mini: "I am having half of an experience as i can't activate my left vagus only the right side. I did reach out to customer support but they only email me the very basic instructions you find on the intro videos etc."

**That is 4 records naming placement difficulty, and it lines up with the 232 of 6,077 ad comments (3.8%) asking placement questions.** The onboarding is the gap, and it shows on both surfaces. **This is one of the few themes with support on both sides of the corpus.**

### Comfort is not universal

From `3b0f8132`, 5 stars, Prime Gen 2, in the longest comfort account in the corpus: "my boyfriend did NOT find the device useable for the most part: we tested it the day it arrived, and he complained of an unbearable stinging sensation every time he touched it to his skin, no matter where he put it, even at the lowest intensity... So comfort might depend on your skin type."

---

## Transformation and impact profile

### The counted piece

**15 of 139 reviews (10.8%)** hit the transformation keyword set (`life changing, life-changing, changed my life, game changer, game-changer, miracle, gave me my life back, blessing`). Those 15 average **5.00 stars**, the only cluster in the corpus that is a clean sweep.

**But apply the method's own warning here.** Per the review-mining discipline, "life-changing" and "would recommend" are generic positive sentiment, not golden nuggets. They describe the brand's promise coming back at it. **The count is real; the language is mostly unusable.** What is usable is the small number of reviews that show the change instead of naming it.

### The before and after stories that actually carry

These are the whole-review concept candidates. Each one has an arc, a specific number or scene, and a named starting state.

**`7163c172` | 5 stars | VeRelief Prime - Lasting Relief Bundle | Rachel Verdi**
Titled "Spoonies! Take Note! Life-Changing Results in 5 Days for 21 Year Disabled Woman, ME/CFS, Fibro, Sleep Disorders!!!" 21-year history, tried everything including an $8,000 rife machine, five days of use. She counts: "Ive gone down 2+ points on pain scale at least 20x in last five days, from a 7/10 down to 5, within 5 mins of using device for 3-5 mins." Her doctor noticed her blood pressure drop. She asks for a lanyard slot and a holster. **This is the single richest record in the corpus and it should be treated as a concept, not a quote.**

**`74e0d82c` | 5 stars | Bundle | Thomas Martin | titled "This changed my life. I have data to back that up."**
"I have a Pixel 2 watch, and use Welltory to measure heart rate variability, SNS:PSNS and stress markers. I was nearly 100% in the SNS before finding VeRelief Prime. Now I see either a balance, or an excess of PSNS. / Literally 2 sessions of using it, and my partner mentioned they could feel my vibe change. I used to have panic attacks that led to excessive sweating. I haven't had an excessive sweating event since I started using the VeRelief Prime a few weeks ago."

**`3dd96d2e` | 5 stars | VeRelief Prime Gen 2 | Ruthkeyoko**
"I'd been suffering from severe PTSD, hyper vigilance, nightmares, emotional deregulation, withdrawn with suicidal thoughts, the whole 9 yards. I didn't want to go the antidepressant route so tried many things including Ketamine infusions with no lasting or measurable difference... As for the results, I'm smiling and talking again, my brain fog has lifted and I'm getting my life back after 2 years of suffering after 3 weeks of regular use morning and night."

**`9a07557f` | 5 stars | Bundle | Ryan Kratt**
"At first, I was very skeptical of this device. But after using it for a short period of time, you can feel the tightness in your chest release and anxiety fade away... I had a hemorrhagic stroke a little over a year ago, and it caused me to develop GAD. With this tool, I don't need to take antidepressant medications or Ativan for emergency situations when panic attacks happen."

**`3374e231` | 5 stars | Bundle | Ryan | titled "1 Week Update"**
"as of today it has been 10 days of using Verelief and I just had my highest HRV recording in several years… I was shocked when I saw my HRV reading this morning. Over 100….my average is usually 30... As you can see in my Apple health data. Average over the last year is in the 20's. Day 10 I wake up to 108."

**`b05b6221` | 4 stars | Bundle | Julian Pisciotta**
"I've been tapering off Xanax and it's been the most difficult season of my life and there's not much that helps and my nervous system has been absolutely decimated. With this I notice a difference in my ability to unwind. I've gotta keep using it daily as it's only been a month and I wanna see where I'm at by the 4-6 month mark."

### The measurable-result pattern

**9 of 139 reviews (6.5%)** name HRV or a wearable. **Marked thin, but it is the highest-credibility proof shape in the corpus** because the customer brings third-party data the brand did not supply. Three of the six transformation stories above lean on it. **The proof demand in the ad comments and the wearable data in the reviews are two halves of the same opportunity.**

### Behavior change, said in customer words

- Weaning off medication: `0bf05a14` "I've been able to wean off of anxiety medication."
- Replacing a coping ritual that needed privacy: `582937fd` "Normally I have to go running or escape into nature to lower my stress and anxiety, which a lot of times that is not possible but using this allows me to take a step away from my desk and laptop, close my eyes and calm myself!"
- Doing things previously avoided: `74e0d82c` "Including a public speaking event, and lots of other activities that I would have avoided due to anxiety before."
- Faster recovery from a spike: `90843b0e` "i could get my work done without 30+ minutes of recuperation in conditions that aren't easily obtainable."

### Won't-buy-again statements

Small and worth naming: `cc820df4` "That's why i returned mine" (ad comment), `2bfaeb63` "Overall I am really disappointed and returned it" (review), `0a1cc1ba` "Over priced weak tens device. Bought two and absolutely regret it" (ad comment), `1fe176e6` "my kid did, but after 30 days he would just feel pain... We were able to return it, no problems. It was worth trying" (ad comment). **27 of 6,077 ad comments (0.4%) mention refund or return.** Thin, and notably the return experience itself is described as easy.

---

## Language and creative-asset index

Every quote below is verbatim, including spelling, punctuation, casing, and typos. Each carries its row id, source, date where a real one exists, product where known, and rating where one exists. **Reviews have no real date. Do not attach one downstream.**

### Golden nuggets - liftable close to as-written

| Quote | Row | Source | Date | SKU | Rating |
|---|---|---|---|---|---|
| "The simplest description of VeRelief is that \"It's an OFF switch for your nervous system.\"" | `83454ab4` | review | none | VeRelief Prime Gen 2 | 5 |
| "I can't believe this little device actually works." | `2da0cba4` | review | none | VeRelief Mini | 5 |
| "This device is like turning the walls into foam." | `90843b0e` | review | none | VeRelief Prime Gen 2 | 5 |
| "He came home in full Hulk Mode and 15 minutes later was Bruce Banner!" | `7881441f` | review | none | VeRelief Pro | 5 |
| "I felt like I was on the medication they put in your IV before putting you to sleep" | `95bda524` | review | none | Prime Bundle | 5 |
| "it \"keeps the hounds at bay\", so to speak" | `52605a0d` | ad comment | 2026-08-02 | unknown | n/a |
| "I'm officially a Hoolest Human" | `7163c172` | review | none | Prime Bundle | 5 |
| "Legends, Hoolest. Legends." | `e97a283a` | review | none | VeRelief Mini | 5 |
| "This changed my life. I have data to back that up." | `74e0d82c` | review | none | Prime Bundle | 5 |
| "you can just whip this puppy out and continue to be at the table" | `9f312bc3` | review | none | VeRelief Mini | 5 |

### Headline-worthy phrases

| Quote | Row | Source | Date | Rating |
|---|---|---|---|---|
| "Don't Be That Guy" (review title) | `b2edd196` | review | none | 5 |
| "It's an OFF switch for your nervous system." | `83454ab4` | review | none | 5 |
| "Not paid to say this! I promise!" (review title) | `95bda524` | review | none | 5 |
| "This tool is amazing" / "At first, I was very skeptical of this device." | `9a07557f` | review | none | 5 |
| "It Just Works!" (review title) | `2d7a92e0` | review | none | 5 |
| "This device is giving me more spoons!!!" | `7163c172` | review | none | 5 |
| "a very attainable way for anyone who may need this... and they are unable to get a VNS implant" | `ed29dfcb` | ad comment | 2026-05-28 | n/a |

### Pain phrases

| Quote | Row | Source | Date |
|---|---|---|---|
| "I purchased this device in total desperation, having suffered from the effects of a souped up sympathetic nervous system for years." | `e97a283a` | review | none |
| "spiraling anxiety with my thoughts all over the place in essentially an echo chamber that leads to a meltdown" | `90843b0e` | review | none |
| "I awoke 2 hours after falling asleep with a racing, pounding heart" | `e97a283a` | review | none |
| "Im am literally retraining my vagus nerve and 60 yrs of survival \" stuck\" hypervigilance ." | `df1be2ad` | ad comment | 2026-09-05 |
| "my nervous system has been absolutely decimated" | `b05b6221` | review | none |
| "I was in an accident that locked my nervous system into fight or flight." | `c3f8ce02` | ad comment | 2026-01-01 |
| "I would absolutely love to get my hands on something like this for my nonverbal autistic son. Anything to get him untrapped from his brain." | `2ed50bef` | ad comment | 2026-01-29 |
| "Stress is a huge problem. Can't relax! No matter what I do!" | `def3f762` | review | none |

### Outcome phrases

| Quote | Row | Source | Date |
|---|---|---|---|
| "when I put it down, the pounding was GONE" | `e97a283a` | review | none |
| "It un-tensed all my muscles and I felt myself just melt away" | `95bda524` | review | none |
| "my heart rate slows, my body relaxes, my sweating ceases... all of which leads to my thoughts mellowing" | `3b0f8132` | review | none |
| "my face will feel like it \"thawed out,\" and I usually feel sense of freedom in my expressions" | `73d2d52b` | review | none |
| "it brings me back to a state of calm where I can be rational instead of reactional" | `3b0f8132` | review | none |
| "Day 10 I wake up to 108." (HRV) | `3374e231` | review | none |
| "I'm smiling and talking again, my brain fog has lifted" | `3dd96d2e` | review | none |
| "It's an enjoyable 4 minutes due to the pleasurable sensation experienced around my ear" | `2da0cba4` | review | none |

### Objections

| Quote | Row | Source | Date | Likes |
|---|---|---|---|---|
| "I'd like to see the clinical studies that show the safety and efficacy of this device." | `e97c5f9e` | ad comment | 2026-02-23 | 214 |
| "💯 BS Junk Science" | `d8b7399f` | ad comment | 2026-03-16 | 57 |
| "Essential Oils 2.0" | `1eab748a` | ad comment | 2026-01-27 | 80 |
| "\"built to last\"...\"2 year warranty\". Built to last 2 years then best of luck!" | `154a28d3` | ad comment | 2026-04-03 | 60 |
| "First of all most people can't afford this! So it's a no for me." | `b68e989d` | ad comment | 2025-05-16 | 37 |
| "it costs $50 a month for electrodes. Every month.  That's why i returned mine." | `cc820df4` | ad comment | 2026-01-12 | 2 |
| "I think people with anxiety are in a different state of mind, living terrified 24/7, so they're willing to try scams like this." | `48c7a76a` | ad comment | 2026-01-27 | 6 |
| "Ok, sure pal. That's how it all happened." (on the founder story) | `02c95378` | ad comment | 2026-05-30 | 47 |
| "the reality is underwhelming" | `ae5453ab` | review (2★) | none | n/a |
| "Very, very, very unpleasant sensation. Engages instant fight or flight, opposite to its purpose," | `474c279c` | review (1★) | none | n/a |
| "Too bad it has to be held. I would love to use this while sitting at my desk but I can't just sit and hold it on my neck." | `25f9e1e2` | ad comment | 2026-09-02 | 1 |
| "Haven't received the product yet because of shipping issues and already wanting a review very interesting tactic" | `1d84bec0` | review (2★) | none | n/a |

### Trigger moments

| Quote | Row | Source | Date |
|---|---|---|---|
| "I was the victim of some horrible road rage.  I was so emotionally shaken I was looking for anything to re-balance my nervous system." | `b2edd196` | review | none |
| "I first used a VRelief mini at my chiropractor's office. After a minute I knew that I had to get one!" | `3aff05af` | review | none |
| "A friend of mine got a VeRelief Mini and after I tried it I immediately ordered one for myself." | `18ff2df0` | review | none |
| "My mental healthcare provider lent me this to see if it would help me." | `cc7031b0` | review | none |
| "I was visiting my Dr. and he had a pair of these that he allowed me to demo for about 20 minutes." | `52b8801c` | review | none |
| "I got it after I found that my seizures were resulting from anxiety and stress." | `f8e12e1c` | review | none |
| "I have been plagued with chronic throat clearing for no apparent reason for two years. No doctor or med has been able to help, and I began to suspect it was a vagus nerve issue." | `21518b69` | review | none |

### Metaphors and similes

**This is the highest-priority signal in the review-mining method and most passes skip it, so it gets its own list.**

| Metaphor | Row | Source |
|---|---|---|
| "It's an OFF switch for your nervous system." | `83454ab4` | review |
| "this device is like turning the walls into foam" | `90843b0e` | review |
| "full Hulk Mode... 15 minutes later was Bruce Banner" | `7881441f` | review |
| "like the medication they put in your IV before putting you to sleep" | `95bda524` | review |
| "my face will feel like it \"thawed out\"" | `73d2d52b` | review |
| "it \"keeps the hounds at bay\"" | `52605a0d` | ad comment |
| "the vagus nerve, the \"wanderer\", winds throughout the body" | `3aff05af` | review |
| "This device is giving me more spoons!!!" (spoon theory) | `7163c172` | review |
| "the master reset line between your brain and body" | TikTok caption, `@kinezioadvancedmassage` | not customer language |

### Category jargon customers actually use

vagus nerve / VNS, fight or flight, rest and digest, parasympathetic, sympathetic, nervous system regulation, dysregulation, vagal tone and "low vagal tonicity", HRV, hypervigilance, somatic, box breathing, TENS unit, auricular, spoonie and spoons, GAD, POTS, dysautonomia, Long Covid, ME/CFS, benzo taper.

**Note the split.** Words like "vagal tonicity," "auricular," and "parasympathetic" come from the most engaged and most educated customers. Words like "shocking yourself" and "handheld version of a tens unit" come from skeptics. **The same product has two vocabularies, and which one a piece of creative speaks decides who it recruits.**

### Anti-language - what the corpus says not to say

- **"Life-changing" and "game changer."** 15 of 139 reviews use them, and they carry no information. They read as brand promise repeated back.
- **Warranty-flavored durability claims.** The "built to last / 2 year warranty" line earned 60 likes as a joke at the brand's expense.
- **Gel tip lifespan claims as stated.** The brand's own reply says "up to 7 days or after 20 uses." Customers publicly contradict it. **Gated, not clear.**
- **Anything implying regulatory approval.** 159 of 6,077 comments already probe FDA and clinical status; overclaiming here walks into the loudest objection in the corpus.
- **The founder-origin story told as a tidy arc.** It is being mocked at 47 likes.

### Outliers and unserved use cases

Each of these is a single record or a handful. **All are marked thin. They are use-case findings, not patterns.**

- Chronic throat clearing, cut roughly 50% on first use (`21518b69`).
- Golf touch shots, chipping and putting (`42083493`).
- Migraine and vestibular migraine (`4dcb6f3f`, `f5046631`).
- Stress-induced eczema (`912044fa`).
- Medication-induced nausea (`a1617f64`).
- Bloating and digestion (`2d7a92e0`, `8d80814a`).
- Benzodiazepine tapering (`b05b6221`).
- Hiccups and temperature regulation (`90843b0e`).
- Tinnitus, requested repeatedly in ad comments but never a review outcome.
- Lyme disease nervous system flares, mother and son (`8d74d857`).
- Wanting a version for dogs (`4e3fc076`).
- Clinician and clinic use as a demo tool, which shows up in at least 6 of 139 reviews.

### Whole-review concept candidates

Five records where the entire review is the asset: `7163c172` (the spoonie five-day log), `74e0d82c` (the HRV data story), `3dd96d2e` (PTSD, after ketamine failed), `3b0f8132` (the researcher who read the studies, plus the honest note that it did not work for her boyfriend), `95bda524` ("Not paid to say this! I promise!").

**Product requests that appear inside positive reviews and should reach the product team:** a lanyard slot and a holster (`7163c172`), a keychain case (`aad77296`), a carrying case that holds the tips and solution (`b2c8f372`), a session-tracking app for clinicians (`9ec638db`), and battery level visible over Bluetooth (`b3c1087f`).

---

## Data limitations

**1. Post-purchase surveys: 0 responses.** The single largest hole. Named in full above. It caps persona confidence, removes first-party attribution, removes the first-time versus returning split, and removes NPS entirely. **Fixing this is the highest-value data move available to this brand.**

**2. The review corpus has no dates.** All 139 collapse to the 2026-09-07 import stamp. No trend, no era tagging, no emerging-versus-fading read. This matters more than it sounds for a hardware brand: the Prime Gen 2 and the original Prime are different products, and there is no way to tell which era a complaint belongs to.

**3. 139 reviews is thin, and 21 of them are not product feedback.** 17 non-delivery plus 4 junk. The usable product-experience corpus is 118 records. **Any review theme with fewer than 10 supporting records is thin and is marked as such throughout this doc.**

**4. Only 12 reviews describe a product failure.** That is not enough to rate anything. It is enough to name examples. **Do not compute a defect rate from this corpus.**

**5. No review source platform.** All 139 read `csv_import`. Owned-site reviews cannot be separated from marketplace reviews, and the corpus is almost certainly partial: one commenter bought on Amazon (`52605a0d`, 2026-08-02) and one reviewer references an earlier review of theirs that is not in the 139 (`3374e231`).

**6. No demographic field anywhere.** Age, gender, region, income, first-time-buyer status: absent on all 6,216 normalized records. **Any demographic claim downstream is inferred from writing style and must be labeled inferred every single time.** Per the persona method, an inferred demographic must never harden into a claim in the retelling.

**7. Ad comments carry no rating, so there is no sentiment split.** 89.8% of rows resist lexicon classification. Ad comments answer "what do people object to and ask about," not "how satisfied are people."

**8. Ad comment authors are anonymous.** `author_id` is null on 100% of rows and `author_name` is populated on 7.0%. No repeat-commenter detection, no per-person deduplication, no way to tell a customer from a bystander except by what they say.

**9. Ad comments mix two product lines.** The most-liked comment in the corpus sits on PEMF creative (`Flex PEMF`, `PEMF_Product-Demo_V1`), not VeRelief. **A slice reading ad comments for VeRelief must filter by `ad_ids` and then verify the creative, not trust the ad name.**

**10. `search_facebook_ad_comments_sql` reports `total: 0` on some unfiltered calls.** Reproduced on 2026-09-08 with a descending sort. **Page the collection to size it. Do not trust a single call's total.**

**11. TikTok holds zero customer language.** 20 videos, 1,625 comments on them, 0 comment bodies retrievable. It is a competitor and format library. **Never count it toward a VoC denominator.**

**12. Missing sources not connected at all:** organic social comments on Instagram, TikTok and YouTube; support tickets and email; Reddit and forum discussion; Amazon and any retail review surface; the brand's own site analytics. Per the review-mining method's source coverage rule, **this pass is partial and should be labeled directional, not statistically representative, in every doc that reads it.**

**13. No LTV, repeat-purchase rate, or order data.** 10 of 139 reviews mention buying again, but that is language, not behavior. The gel tip subscription is the obvious repeat-revenue line and this corpus cannot size it.

**14. Two sources of intake bias worth naming.** First, the brand appears to solicit reviews before delivery, which manufactures 1-star reviews from people with no product opinion. Second, ad comments come overwhelmingly from people who have not bought, so the corpus over-represents pre-purchase objection and under-represents post-purchase experience. **The two surfaces are biased in opposite directions, which is actually useful if a downstream doc reads them as a pair rather than pooling them.**

---

## Open loops

Five loops came out of this census. Each carries the observation, the pull, the question, why it matters, and its territory. Grading and routing happen in the roll-up, not here.

**Loop 1 - Why is proof the loudest objection, and what proof would actually land?**
The most-liked customer comment in 6,077 asks for clinical studies (214 likes), 159 of 6,077 (2.6%) name FDA or research, and 241 of 6,077 (4.0%) reach for scam or snake oil. Meanwhile the most credible proof in the whole corpus is customers posting their own HRV screenshots, which appears in 9 of 139 reviews (6.5%). **Pull: tension.** It fired because the brand's own strongest evidence in customer hands is wearable data a customer brought, while the objection people voice is for institutional evidence the brand does not have. **Question: what kind of proof actually moves a skeptic in this category?** If the answer is customer wearable data rather than clinical citation, the whole proof strategy and the creative built on it changes. *Territory: messaging.*

**Loop 2 - Who is the buyer who says "I can't get a VNS implant"?**
The two highest-liked positive comments in the corpus, at 93 and 87 likes, are both from people connected to implanted vagus nerve stimulators for epilepsy, framing VeRelief as the version you can actually get. Hoolest's creative does not appear to speak to them. **Pull: gap.** It fired because the single most engaged positive framing in 6,077 comments came from customers, not from the brand, and nothing in the corpus suggests the brand has ever run it. **Question: how many people are looking for a home version of a clinical device they cannot access?** If this is a real population, it is a persona nobody in the category is speaking to. *Territory: personas.*

**Loop 3 - What happened in March 2026?**
Ad comments jumped to 1,084 in March 2026 against a 2026 monthly average near 540. **Pull: surprise.** It fired because nothing else in 25 months of comment history comes close to double the average, and the census cannot see what caused it. **Question: what drove the March 2026 comment spike?** If it was a creative or placement that generated argument rather than demand, that changes how comment volume is read as a signal at all. *Territory: messaging.*

**Loop 4 - Does the gel tip cost actually kill repeat purchase, or just annoy people?**
129 of 6,077 ad comments (2.1%) and 17 of 139 reviews (12.2%) name the consumables, the review set averaging 3.76 against a 4.11 corpus average, and at least one commenter says the recurring cost is why they returned the device. **Pull: pattern.** It fired because the same objection surfaces independently on both surfaces and the brand's own stated tip lifespan is being publicly contradicted. **Question: how much of the churn is the recurring cost versus the tips wearing out faster than promised?** The two problems have completely different fixes, one is pricing and one is product. *Territory: product.*

**Loop 5 - Why do so many buyers arrive through a clinician, and is that lane being fed?**
14 of 139 reviews (10.1%) mention a doctor, chiropractor, therapist, or clinic, and at least 6 of 139 come from practitioners buying for clients or patients. The clearest purchase mechanic in the corpus is trying it once in a professional's office and then buying. **Pull: resonance.** It fired because the try-then-buy story kept repeating in reviews with a warmth that the paid creative does not seem to have noticed. **Question: how much of Hoolest's demand starts in a practitioner's hands rather than in the feed?** If a meaningful share does, the strongest growth lever might be a practitioner program rather than more prospecting spend. *Territory: personas.*
