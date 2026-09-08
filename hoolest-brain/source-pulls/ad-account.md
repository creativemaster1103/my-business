---
brand: hoolest-performance-technologies
doc: ad-account
generated_on: 2026-09-08
refresh_by: 2026-12-07
sources_read:
  - Parker MCP `search_facebook_ads_sql`, Meta ad account "Hoolest FB Ads" (948100899908170, USD), lifetime window, all statuses, grouped by ad name, top 20 by lifetime spend
  - Parker MCP `search_facebook_ads_sql`, same account, last 90 days (2026-06-10 to 2026-09-07), grouped by ad name, top spenders with per-ad age/gender/platform delivery splits
  - Parker MCP `search_facebook_ads_sql`, same account, last 30 days (2026-08-09 to 2026-09-07), ACTIVE only, grouped by ad name, top 15 by spend
  - Parker MCP `search_facebook_ads_sql`, adIds detail lookups on 14 individual ads with the ad_analysis block for creator demographic, ad summary and scene-level read
  - Parker MCP `search_facebook_ads_sql`, keyword cuts on "first responder" (238 ads) and "sleep" (622 ads), lifetime
  - Parker MCP `search_facebook_ads_sql`, adType cuts: static (988 ads) and video (1,894 ads), lifetime
  - Parker MCP `analyze_video_from_url` on the playable media file for the account's single highest-spending ad, because Parker held no AI analysis or transcript for it
  - Parker MCP `get_brand_persona` for the brand's stated targets, stated ICPs and stated creative history
ads_read: 45 distinct ad-name groups read at the creative level, out of 2,887 ads lifetime. Windows covered: lifetime (Sept 2023 to Sept 2026), last 90 days (766 ads with spend), last 30 days ACTIVE (571 ads with spend). Spend denominators: $3,851,961.87 lifetime, $1,044,087.57 last 90 days, $351,004.34 last 30 days.
data_limitations:
  - Meta exposes spend by age, gender, platform and device, but not purchases by age or gender. Every read of who actually converted on a given ad is inference from delivery, never verified buyer truth. This is the single biggest blank in the doc.
  - Frequency was not returned in the metric sets pulled, so no read is offered on whether the account is reaching new people or re-hitting the same ones. That belongs to the ad-account evaluation doc.
  - Parker holds no AI tags, no transcript and no creative analysis for "Longform - Nov 26th," the account's biggest ad at $456,079 lifetime. Resolved by analyzing the video file directly. Flagging it because the same gap will hit any later run that does not do the same.
  - AI tag coverage is partial. Tagged spend on the awareness dimension totals $2,792,391 of $3,851,962 lifetime, so roughly 72.5% of spend carries an awareness tag and the shares below are shares of total spend, not of tagged spend.
  - Post-purchase surveys hold zero responses for this brand, so the strongest tier of buyer evidence is unavailable to hold this served-audience read against. The synthesis has to lean on reviews and comments instead.
  - Northbeam is not connected, so every number here is Meta-reported under the org default attribution window.
---

# Ad account — persona signal — Hoolest Performance Technologies

## Served-audience signals

The research story first, so you can judge everything that follows. I read the account three ways: lifetime, so durable winners show up; the last 90 days, so I could see who the creative courts now; and the currently active set, so I could see what the team is putting into market this week. Then I dropped into 14 individual ads and pulled the full creative read on each, the creator demographic, the scene-by-scene summary, the verbatim hooks. For the biggest ad in the account Parker held no analysis at all, so I ran the video file itself and got the transcript. That matters, because that one ad is 11.8% of everything this brand has ever spent, and reading it off its name would have told me nothing true.

Here is what the account is actually courting.

**The stretched provider. Strong signal. Inferred from creative, backed by delivery data.**

This is the account's biggest served audience by a wide margin, and it is drawn most sharply in the single ad that carries $456,079 of lifetime spend, "Longform - Nov 26th." Nick Hool sits at a desk in a studio with a boom mic in frame and names the person he is talking to out loud, verbatim at 0:15: *"Chances are you wake up every day, go to work, maybe you have a family you're providing for, you have kids you're raising, you're trying to stay healthy, volunteering at your church, trying to keep up with friends."* Then at 0:29 he writes three words on a sheet of paper and crosses them out: *"Time, energy and space."* The close, at 2:45, puts the device *"in your pocket so you can use it in any environment, no matter how stressful. Your car, the office, the sideline of your kid's soccer game, anywhere."*

That is not a stress sufferer in the abstract. That is a working parent in the middle of a loaded life who has decided the problem is that recovery costs time he does not have. The message is not "you are suffering." It is "you are outnumbered." The Life Force 8 lever underneath it is freedom from fear, pain and danger stacked on top of care and protection of loved ones, and the mindstate it plays to is competence more than relief.

The delivery data backs the read rather than contradicting it, which raises confidence to the top of what this account can offer. Lifetime spend by age lands 30.8% on 35 to 44 and 25.8% on 45 to 54, so 56.6% of every dollar ever spent went to people between 35 and 54, and 73.0% went to 35 to 64. Gender splits almost exactly down the middle at 50.8% male and 48.0% female. Devices are 97.5% mobile. This is a middle-aged audience being reached on a phone.

**The skeptical mechanism buyer. Strong signal. Inferred from creative, backed by format spend.**

The second audience the account courts hard is the person who will not buy until they understand why the thing works. The evidence is in where the format spend sits. Across lifetime spend, ads tagged Authority Figure carry $1,118,222, which is 29.0% of everything, and Educational carries $910,998, another 23.7%. Together that is 52.7% of lifetime spend on creative whose whole job is explanation.

You can see what that looks like in the ads. Dr. Ryan, a functional neurologist in a black Adidas quarter-zip, opens with *"This is the V-Relief Prime"* and then names the anatomy out loud: *"So you place it right here, just below the earlobe at what's called the tympanomastoid fissure."* That pair of ads, "Dr Ryan VeRelief #2" and its iteration, carry $116,502 lifetime between them. The founder cuts do the same work from the inventor's chair. "HPT022_VID_Top 5 Objection" opens *"I invented this device that uses vagus nerve stimulation to stop a panic attack in 30 seconds"* and then walks through named rivals, GammaCore at a $5,000 anchor and Truvaga, before showing a pour of thick green competitor gel onto a palm.

The proof stack is consistent enough across the winners to call it the account's real spine: a PhD, a $700,000 research figure, three placebo-controlled studies, a 31% HRV lift, and 94% relaxation across 1,300-plus first responders. That last number is the important one for the persona read, and I come back to it below.

**The comparison shopper already inside the category. Moderate signal. Inferred from creative, thin spend base.**

A smaller but distinct audience is the person who already owns or has priced a rival device. Comparison-tagged ads carry $116,821 lifetime, 3.0% of spend, but they are climbing: $73,582 in the last 90 days, which is 7.0% of the window. "HPT025_VID_Top5_Q&A" opens *"Should you get the VeRelief or one of these other brands?"* with 3D renders of five competing devices floating around Nick's head. This ad returned a 1.82 ROAS on $35,223 lifetime at a $101.51 cost per purchase, the best cost per purchase of any ad above $30,000 in spend in the entire read.

That is a solution-aware buyer in Schwartz terms, already shopping the category, and the account converts them cheaper than it converts anyone else. Worth naming as its own served audience rather than folding it into the mechanism buyer, because the message that wins them is a head-to-head, not an explanation.

**The price-hesitant near-buyer. Emerging signal, last 30 days only.**

New in the active set and worth flagging early. "HPT072_VID_Price Objection Comment," launched 25 August 2026, opens on a viewer comment rendered on screen: *"The price is the only reason I didn't buy this a year ago, and I'm still annoyed about it."* On $6,335 of spend in the last 30 days it returned a 2.53 ROAS at a $93.16 cost per purchase. That is the highest ROAS of any VeRelief ad in the active set, on a small base. Small base means low confidence on the number. The audience signal is real regardless: the account has started speaking to somebody who already decided they want it and stalled on the price.

**The student. Just appeared, too new to read.**

"HPT061_VID_College Student," live since 19 August 2026, frames the moment as *"Studying in the library before an exam, feeling the stress build?"* At $6,046 over 30 days and a 1.06 ROAS it has not earned a verdict either way. I note it because it is the first time in the corpus I read that the account has built an ad around a life stage rather than a symptom.

## Message-to-buyer map, frequency-ranked

Ranked by how heavily each message recurs across winning creative and how much spend sits behind it. Every buyer attached to a message is my inference from the creative, marked as such, because the account cannot show who converted by segment.

**1. "I built this because it happened to me." Founder origin. Roughly $700,000 of readable lifetime spend, and the biggest real bet in the account.**

This is the account's dominant message by any measure. Founder Ads as a tag carry $477,853 lifetime, 12.4% of spend, but that badly undercounts it, because Nick is also the on-screen figure in a large share of the Authority Figure and Educational spend. Of the 20 highest-spending ad-name groups lifetime, 13 have Nick on camera as the primary voice. The verbatim opener recurs almost word for word across cuts spanning three years: *"I invented this device that uses vagus nerve stimulation to stop a panic attack in 30 seconds"* in June 2026, *"I created a new technology to calm your nerves fast"* in November 2025, *"This substance-free tool stimulates your brain and helps you calm down fast"* in September 2023.

The buyer this wins, inferred: the skeptical mechanism buyer, and the stretched provider when the origin story is attached to the time argument rather than to the golf story. Confidence is high on the first, moderate on the second.

**2. "Your nervous system is broken and it is not your fault." Problem naming. $871,330 lifetime spend on Problem Aware tagged creative, 22.6% of total, rising to 32.9% in the last 90 days and 41.0% of active spend in the last 30.**

The body copy that runs under the account's two biggest video assets carries this message in the customer's own register: *"You're not mentally weak. You're not being dramatic. Your vagus nerve — the one that's supposed to keep you calm — just isn't working."* And: *"While everyone tells you to 'just breathe,' your body thinks everything is an emergency."*

This is the TEEP Trigger message. It mirrors the internal state back before it introduces anything to buy, which is exactly the move `emotional-delivery-and-timing.md` says outperforms at that phase. The account is doing more of it now than it ever has, which is the clearest directional shift in the whole read.

The buyer this wins, inferred: the person who has been told to relax and resents it. That is the Wired Lifer in the brand's own ICP language, and the read is consistent with the ICP, which is worth naming out loud because agreement between the account and the brand's stated ICP is not the same as verification.

**3. "It works in 30 seconds and you can feel it." Speed and felt sensation. Present in nearly every winner in the read.**

"Reset panic in 30 seconds" is the account's most repeated single phrase, running as the ad title on the $111,158 BOFU static and inside a dozen video cuts. The version that lands hardest is the one that names the sensation rather than the clock. In "HPT052_VID_Nick Trial Reels," Nick says at 0:26 that unlike breathwork or medication *"you can actually feel it working,"* then at 0:33 that his *"face is just kind of floating away,"* and at 0:36 that *"your shoulders drop, your breathing slows, and everything just feels still."*

That ad holds attention better than anything else in the account. Hold rate 27.84% on the 5B cut and 37.34% on the 2B copy, against an account where most video sits under 10%. By the bar in `ad-account-analysis.md`, where 12% to 15% is the floor and anything under 12% is a problem, those two cuts are outliers by a factor of three.

The buyer this wins, inferred: the person who has already bought and been let down by a wellness device that did nothing. The felt sensation is the answer to "another gadget that won't work."

**4. "No app, no Bluetooth, no messy gel." Friction and rival contrast. $116,821 lifetime on Comparison, plus the friction argument threaded through most founder cuts.**

"HPT059_VID_FAQs," live now, is built entirely on it: *"No app. No Bluetooth. No wires. Just clip VeRelief Prime to your ear."* "HPT027_VID_Founder Story" ends on a shot of green competitor gel being poured onto a hand and a man wiping his neck in frustration.

The buyer this wins, inferred: the comparison shopper. Narrow audience, cheap conversions. This is the message that hits a small pool efficiently.

**5. "Buy it now, it is on sale." Offer. The message the account leans on hardest right now, and the one whose buyer I trust least.**

This is the mismatch worth flagging as high-value signal. Across lifetime, ads tagged with a promotion carry $977,580, or 25.4% of spend. Across the last 90 days that jumps to $637,281, or 61.0%. Across the last 30 days of active spend it is 63.7%. The account has swung from roughly a quarter promotional to roughly two-thirds promotional inside one quarter.

`persona-research-and-creative-strategy-process.md` is blunt about what that does: strip sale creative before the buyer read, because deal-motivated is a behavioral overlay every persona exhibits and treating it as a persona both invents a customer and hides that promo skewed the read. So the honest statement is this. The account's recent buyer file is majority promotional. Any persona read the synthesis builds from recent reviews or recent comments inherits that skew, and the synthesis should hold it at arm's length rather than treat it as a picture of who wants this product at full price.

**6. "It helps you sleep." Present everywhere in body copy, led on almost nowhere.**

The word sleep appears in the text of 622 of 2,887 ads, 21.5% of the account. But every one of the top spenders that carries it carries it as an item in a benefit list, not as the thing the ad is about. The highest-spending ad whose headline actually leads on sleep is "Longer Conversion Vid with Nick, Dr. Teames, and others 1:04," titled *"More Sleep - More Calm - More Life,"* at $39,610 lifetime, which is 1.0% of all spend, and it launched in November 2023. Nothing in the last 90 days leads on sleep at all.

That is a message the account mentions constantly and bets on never. More on it under unserved audiences, because the buyer behind it is the one the account is missing.

## Spend concentration and what it serves

The account is far more concentrated than its ad count suggests. There are 2,887 ads lifetime, but the top 19 ad-name groups carry $1,394,364, which is 36.2% of all spend ever. One creative file carries more than any brand should be comfortable with. The video at `e9e3ece1...mp4` ran under the name "Longform - Nov 26th" for $456,079 and again under "Prime_ Home_TOF_Panic_BulbFX_Mar 26th 2026" for $124,328. Those two alone are $580,408, or 15.1% of lifetime spend, on one asset. At least two further relaunches of the same file appear in the recent windows under "- Copy" names.

What that concentration serves is the stretched provider, because that is the ad. Fifteen percent of everything Hoolest has spent went behind a three-minute studio monologue aimed at a 35-to-54-year-old with a job, kids, a church and no half hour to himself. That is the account's real bet, whether the team framed it that way or not.

The rest of the allocation sorts like this.

**Video over static, roughly three to one.** Video carries $2,846,943 across 1,894 ads, 73.9% of spend, returning a 1.32 ROAS at a $173.70 cost per purchase. Static carries $1,004,907 across 988 ads, 26.1% of spend, returning a 1.58 ROAS at a $160.53 cost per purchase. The static ads return better on both measures, which is the read `ad-account-analysis.md` warns you to caveat rather than act on: statics skew bottom of funnel, so they are scooping people who were already close. The right comparison is not static against video, it is TOF video against TOF video.

**Facebook and Instagram, near even overall, but split hard by format.** Lifetime, Facebook takes 49.4% of spend and Instagram 50.0%. Underneath that even top line, static spend is 64.0% Facebook and video spend is 55.4% Instagram. And the split is starker per ad. The $111,158 BOFU static delivered 99.6% on Facebook. "HPT052_VID_Nick Trial Reels" delivered 91.3% on Instagram. Reading that through the placement logic in `ad-account-analysis.md`, the account's demand capture is happening on Facebook feed in front of an older, lean-back audience, and its discovery is happening in Instagram Reels in front of a younger one. Those are two different served audiences reached by two different halves of the account, and nothing in the creative treats them differently.

**The audience is getting younger, fast.** Lifetime, 25 to 34 takes 15.8% of spend and 55-plus takes 25.3%. Over the last 90 days, 25 to 34 rose to 20.8% and 55-plus fell to 18.2%. That is a meaningful shift inside one quarter, and it tracks with the Instagram lean in the recent creative. Verified from delivery data. What it means for who buys is inference, and I would not push it further than "the account is now paying to reach a younger person than it used to."

**A second product is quietly earning.** "HPT034 IMG Hero Product 6D Mini Max PEMF," a static for the $6,000 PEMF unit, spent $4,798 in the last 30 days and returned a 5.28 ROAS at a $704.19 average order value and an $11.39 CPM. It is 1.4% of active spend. I flag it because it is the only ad in the entire read serving a professional or clinical buyer rather than a consumer, and it is doing so at a return no VeRelief ad approaches. Small base, so the number is thin, but the audience signal is not.

**What the allocation starves.** Every persona the brand names outside the stretched provider and the mechanism skeptic gets almost nothing. Ads tagged with the Life Force 8 desire "care and protection of loved ones," which is where a gifting or spouse-led message would sit, carry $13,226 lifetime across 8 ads. That is 0.3% of spend. Ads tagged "social approval" carry $310 across 3 ads. UGC Single, the format most likely to put an ordinary buyer rather than the founder on screen, carries 293 ads and $148,991, which is 3.9% of spend against 10.2% of the ad count. The account makes plenty of ordinary-person creative. It does not fund it.

## Unserved audiences

These are absences, and by the standard in `analyzing-public-ad-accounts.md` the absence is the finding.

**The first responder as a person on screen.** This is the sharpest gap in the account. The phrase "first responder" appears in the text of 238 ads carrying $513,932 of lifetime spend, 13.3% of everything. In every single one of those I read at the creative level, it is a proof statistic and nothing else: *"94% of over 1,300 first responders felt relaxed after a single session."* Not one ad in the 45 I read casts a firefighter, a cop, a medic or a veteran, puts them in their own setting, or lets them speak. The brand's own ICP 5 is Marcos, a 38-year-old fire captain, described in the brand context as somebody who finds things like this *"through the kind of Instagram ad that shows someone who looks like him instead of a twenty-something in yoga pants."* The account has never made that ad. It has made 238 ads that quote his colleagues as a number.

**The sleep buyer.** Covered above. Sleep is one of the device's five modes, it is named in 21.5% of ad text, and it has led an ad exactly nowhere since 2023. The brand's own ICP 3 calls this segment the largest and least stigmatized desire in the base, and says it is the lowest-friction entry point for cold traffic. The account does not test it.

**Women as a subject rather than a reaction shot.** Female delivery is 48.0% of lifetime spend and 49.6% of the last 90 days, so roughly half of every dollar reaches a woman. Yet across the 45 ads I read at the creative level, women appear as testimonial cutaways and reaction faces inside somebody else's ad. The pattern is visible in the creator demographic fields themselves. In "Flex Home - 322" the primary narrator is a man and the women are *"a Caucasian woman in her 30s-40s sharing a raw, emotional testimonial"* and *"a younger Caucasian woman in her 20s-30s with long brown hair wearing a green sweater."* In "Dr Ryan VeRelief #2" the secondary characters are listed as a mix of *"'high performers' and stressed professionals"* with the doctor doing all the talking. No ad in the read is built from a woman's situation, in her voice, about her life.

**The HRV hunter with a dashboard.** The 31% HRV figure appears as a bar chart inside the Longform ad. No ad in the read is built around a wearable screenshot, a personal experiment, or a before-and-after from an Oura or Whoop. Before & After as a format tag carries $4,134 lifetime across 3 ads, 0.1% of spend. For a buyer the brand describes as generating free UGC unprompted because they screenshot and post, that is a lane the account has never entered.

**The person buying it for someone else.** One ad in the active set speaks to gifting at all, "HPT039_IMG_B20G1 Bundles," and it is a price mechanic rather than a story: *"The Family Circle Pack gets you 3 VeRelief Primes for the price of 2 — one for you, two to share."* The brand context describes a spouse who *"can see the stress but can't get their person to seek help."* No ad in the read is that ad. With Christmas and Father's Day both on the brand's own promotional calendar and a stated three-month lead time on seasonal creative, this absence has a deadline attached to it.

**Anyone over 60.** Buyers 65 and older take 8.9% of lifetime spend and 10.0% of static spend specifically, which is real money at this account size. Nothing in the read is cast, paced or written for them. Every winning video runs fast cuts and dense on-screen graphics.

**The practitioner as the buyer.** The BOFU static claims the device is *"RECOMMENDED BY 1,000+ CLINICIANS."* The Dr. Ryan partnership ads use a clinician to speak to patients. Nothing in the account speaks to a clinician about stocking, recommending or using the device in practice, even though the Mini Max PEMF ad shows there is a professional-tier buyer in reach at a $704 average order value.

## Served-versus-stated gap

Four gaps, each named on both sides and left for the synthesis to weigh against the actual-buyer sources.

**On who the brand thinks it serves.** Stated: five ICPs, the Wired Lifer, the Off-Ramper, the Lights-Out Loser, the HRV Hunter and Marcos the fire captain. Verified from the account: two of those five get real creative and real spend. The Wired Lifer is served constantly and well. The Off-Ramper is served obliquely, since anti-medication framing is the ICP's own stated legal guardrail, and the account works around it with lines like *"So I got my PhD in biomedical engineering so I could create something so I wouldn't have to be dependent on medications my whole life,"* which puts the medication objection in the founder's mouth rather than the viewer's. The other three are effectively unserved. The gap is not that the brand is wrong about its personas. It is that the account has only ever funded two of them, so four of the five ICPs remain hypotheses nobody has spent against.

**On the account's own scale.** Stated success definition, from the brand: *"Consistent 2x ROAS at $1K adspent."* Verified: the account spent $1,044,088 in the last 90 days, which is roughly $11,600 a day, at a 1.33 ROAS. Lifetime is $3,851,962 at 1.39. The stated goal is written for an account three orders of magnitude smaller than the one that exists, and the return target has never been hit at any window I pulled. I am not calling the goal wrong. I am calling it stale, and flagging that every downstream judgment about what counts as a winner rests on a target nobody has restated since the account got big.

**On what the brand says works.** Stated: *"Yapper Founder ads."* Verified: the tag Yapper carries $2,323 lifetime across 3 ads, 0.06% of spend, while Founder Ads carries $477,853 and Nick is the primary voice in 13 of the top 20 spenders. The brand's instinct is right and its label does not match the account's vocabulary. Worth resolving with the team, because a strategist reading the tag alone would conclude the format failed.

**On AI creative.** Stated: *"Tried AI ads didn't work."* Verified: ads tagged AI Animation carry $1,253 lifetime, 0.03% of spend, so that verdict rests on nearly no spend. Meanwhile the account is currently running three ad concepts with "AI VO" in the name, HPT052, HPT059 and HPT061, carrying $56,673 across the recent windows, and the HPT052 cuts post the two highest hold rates in the entire account at 27.84% and 37.34%. The stated history and the current account do not agree, and the current account is winning the attention fight with the thing the brand said failed.

## Behavioral-signal states the creative leans on

These are states layered on a buyer, not identities, so the synthesis should attach them as overlays rather than promote any of them into a persona.

**The acute episode.** The single most activated state in the account. "Reset panic in 30 seconds" is the account's most repeated promise, and the creative reaches for the moment itself: the opening frame of "Flex Home - 322" is *"a woman in a grey sweatshirt sitting on a wooden chair, hunched over in intense distress, clenching her fists"* over the verbal hook *"Anyone else feel like they're about to unalive during a panic attack? Like, this is it."* In TEEP terms this is Trigger creative, mirroring the state back before offering anything.

**Time poverty.** The state the biggest ad in the account is built to activate. Time, energy, space, written on paper and crossed out. This is the one behavioral state the account has bet real money on, $456,079 worth.

**Deal motivation.** Now the most heavily funded state in the account at 63.7% of active spend, up from 25.4% lifetime. It is an overlay, not a buyer, and the account should not read its recent conversion mix as a persona finding.

**Skepticism as a posture.** Ads tagged with the Skepticism emotion carry $194,137 lifetime, 5.0% of spend, and the whole Comparison lane is built for a person actively trying not to be fooled. This is Evaluation-phase creative in TEEP terms, and `emotional-delivery-and-timing.md` is right about what it needs: name the specific hesitation rather than restate the benefit. The account's best-performing recent ad by ROAS does exactly that with a price comment on screen.

**Price hesitation as a distinct stall.** New and separable from general skepticism. Two ads in the last 30 days are built on it, and the stronger one, HPT072, returned 2.53 on $6,335.

**Situational performance pressure.** Thin but present, and it is where the founder's own story starts: *"I had bad performance anxiety as an aspiring professional golfer. Any time I would play, my heart would be in my throat. I couldn't breathe. My vision was blurry and that ultimately wrecked my future."* The account uses this as origin, not as a state it activates in the viewer. The one recent attempt to activate it in somebody else is the college exam ad, live three weeks.

**Gifting.** Barely present. One bundle static, framed as a price mechanic.

## Recurrence and spread

**What I read.** 45 distinct ad-name groups at the creative level, out of 2,887 ads lifetime. That is 1.6% of the ad count but it covers the top of the spend curve: the 19 named groups I read from the lifetime cut alone carry $1,394,364, which is 36.2% of the $3,851,961.87 the account has spent. Of the 45, I pulled the full AI creative analysis on 14, including creator demographic and a scene-level summary, and I ran the raw video file on one because Parker held nothing for it.

**Windows covered.** Lifetime runs from the oldest ad in the read, 26 September 2023, to the newest, 27 August 2026. The recent window is 10 June to 7 September 2026, covering 766 ads with spend and $1,044,087.57. The active window is 9 August to 7 September 2026, covering 571 ads with spend and $351,004.34.

**How heavily each message recurs.** Founder origin appears as the lead in 13 of the top 20 lifetime spenders. Speed and felt sensation appears in some form in nearly all 20. Problem naming carries 660 tagged ads and $871,330 lifetime, rising to 41.0% of active spend. Explanation, meaning Authority Figure plus Educational, carries 442 tagged ads and $2,029,220 lifetime, 52.7% of spend. Comparison carries 22 ads and $116,821 lifetime. Sleep-led creative carries one ad from 2023 and 1.0% of spend. First responders as on-screen talent carry zero ads and zero spend.

**How heavily each audience recurs.** The stretched provider is served by the single largest asset in the account and by the family and time framing threaded through most founder cuts. The mechanism skeptic is served by 52.7% of lifetime spend. The comparison shopper is served by 3.0% lifetime and 7.0% in the last 90 days. The price-hesitant near-buyer is served by two ads, both younger than 60 days. Everyone else in the brand's own ICP list is served by nothing I could find.

**What rests on creative alone versus on performance data.** The audience identities are inferred from creative in every case, because Meta does not expose purchases by segment for this account. What the performance data verifies is delivery, not conversion: which age band and which gender Meta spent the money in front of, per ad and per window. Where those two lines agree, and they do for the stretched provider, I have raised confidence to the top of what this account can support, which is still short of verified buyer truth. The one place the delivery data is doing real independent work is the gender split per ad, where identical founder creative in the same quarter delivered 75.4% male on "HPT027_VID_Founder Story" and 67.4% female on "HPT026_VID_Fight or Flight." That is a verified fact about the account with no creative explanation attached to it yet.

**Confidence, by signal.** Stretched provider: strong. Mechanism skeptic: strong. Comparison shopper: mixed, real but small. Price-hesitant near-buyer: thin, one ad above noise. Student: thin, three weeks live. Every unserved audience above: the absence itself is verified against the 45 ads read and the keyword cuts; what the absence costs is unknown.

## Open loops

**1. The first responder proof line versus the first responder on screen**

The phrase "first responder" carries $513,932 of lifetime spend across 238 ads, 13.3% of everything the account has spent, and in every ad I read at the creative level it is a statistic, never a person. The brand's own ICP 5 is a fire captain who the brand says finds products through an ad that shows someone who looks like him. The account has never made that ad.

*Pull: Gap.* It fired when I ran the "first responder" keyword cut expecting to find a first responder audience lane and found instead that all $513,932 of it was one proof sentence repeated inside ads aimed at somebody else.

*Question: How much of the actual buyer base found VeRelief through first responder, military or veteran circles?*

If a real share of buyers already come through those circles, the account is currently converting them despite never speaking to them, and casting one is the cheapest unlock on the board. If almost none do, the 94% statistic is doing borrowed-credibility work for a general audience and should be judged on that job instead.

*Territory: Personas.*

**2. The same founder, two cuts, opposite genders**

Two ads launched within three days of each other in June 2026, both featuring Nick, both about getting out of fight or flight, delivered to almost opposite audiences. "HPT027_VID_Founder Story" put 75.4% of its $51,223 in front of men. "HPT026_VID_Fight or Flight" put 67.4% of its $16,185 in front of women. Same founder, same product, same quarter, same promise.

*Pull: Surprise.* It fired when I lined up the per-ad gender splits expecting them to cluster near the account's even 49 to 50 average and found a 42-point spread between two cuts of the same idea.

*Question: What is it inside these two cuts that makes Meta deliver one almost entirely to men and the other mostly to women?*

If the lever is findable in the creative, the account can aim at the half of its audience it currently under-serves on purpose instead of by accident, and the women-as-subject gap becomes solvable with existing footage rather than a new shoot.

*Territory: Messaging.*

**3. Sleep, mentioned everywhere and bet on nowhere**

Sleep is one of the device's five modes and appears in the text of 622 of 2,887 ads, 21.5% of the account. The highest-spending ad that actually leads on it is from November 2023 and carries 1.0% of lifetime spend. Nothing in the last 90 days leads on sleep at all. The brand's own ICP 3 calls the sleep buyer the largest and least stigmatized desire in the base.

*Pull: Gap.* It fired when the sleep keyword cut returned 622 ads and $1,227,116 of spend, and every top result turned out to be an ad about panic with sleep listed as a side benefit.

*Question: How big is the sleep-first buyer inside this brand's actual customer base?*

Sleep is the one entry point in the brand's own persona set that carries no stigma, which is why it would reach cold traffic the panic message cannot. If the buyer base is already full of people who bought for sleep, the account has been leaving the easiest cold-traffic door shut for three years.

*Territory: Personas.*

**4. A success target written for a $1,000 account**

The brand states its definition of success as a consistent 2x ROAS at $1,000 ad spend. The account spent $1,044,088 in the last 90 days at a 1.33 ROAS, and $3,851,962 lifetime at 1.39. The target has not been met in any window I pulled, and it describes an operation roughly a thousand times smaller than the real one.

*Pull: Tension.* It fired when I put the stated KPI from the brand context next to the account totals and the two could not both be current.

*Question: What return does this business actually need at its current spend level to be healthy?*

Every judgment downstream about which ads are winners, which get iterated and which get killed is graded against this number. If the real bar is 1.3 with repeat purchase behind it, the account is roughly at target and the read is "hold and diversify." If it is genuinely 2.0, most of what is running is underwater and the read is "cut hard." Those are opposite strategies.

*Territory: Product.*

**5. The account went two-thirds promotional in one quarter**

Promotional creative carried 25.4% of lifetime spend. Over the last 90 days it carried 61.0%, and across currently active spend it is 63.7%. Evergreen creative held 69.1% of lifetime spend and now holds 82.3% of active spend by count while promotions take most of the dollars, so the promos are absorbing budget out of proportion to their share of the library.

*Pull: Surprise.* It fired when the promotion tag flipped from a quarter of spend to two-thirds between the lifetime cut and the 30-day cut, which is not a drift, it is a decision.

*Question: How do buyers who come in on a promotion differ from the ones who come in at full price?*

The persona method says to strip sale creative before reading the buyer, because deal motivation is an overlay every persona carries. If most of the recent customer file arrived on a discount, then the reviews and comments the synthesis is about to mine describe a promotional buyer, and the whole persona picture tilts without anyone noticing.

*Territory: Product.*

**6. The AI voiceover cuts that hold attention three times better than anything else**

The brand states AI ads were tried and did not work. The ads tagged AI Animation carry $1,253 lifetime, so that verdict rests on almost no spend. Meanwhile "HPT052_VID_Nick Trial Reels," an AI voiceover concept live since July 2026, posts hold rates of 27.84% and 37.34% across its cuts, against an account where most video sits under 10% and the working floor is 12%.

*Pull: Tension.* It fired when the two highest hold rates in a 2,887-ad account both turned out to belong to the format the brand had written off.

*Question: What is different about these AI voiceover cuts that keeps people watching so much longer?*

Hold rate is the account's weakest metric almost everywhere, and something here has tripled it. Whatever it is, it is portable to the founder ads, the comparison ads and the problem-naming ads that carry the majority of the spend.

*Territory: Messaging.*

**7. One face carries almost the whole account**

Nick is the primary on-screen voice in 13 of the 20 highest-spending ad-name groups. Outside him, only two other faces carry meaningful money: Dr. Ryan the functional neurologist at $116,502 across two ad names, and two whitelisted creators at roughly $56,374 combined. UGC Single, the format most likely to put an ordinary buyer on camera, holds 293 ads, 10.2% of the ad count, but only 3.9% of spend.

*Pull: Gap.* It fired when I collected the creator demographic fields across the top spenders and found the same white man in his early-to-mid thirties in nearly every one, three years running.

*Question: Who else could carry this message on camera with the same credibility Nick has?*

The brand's stated plan is 50-plus net-new concepts a month. That volume cannot come from one person's calendar, and the account has no proven second face. Knowing who else can carry it is the difference between a roadmap that ships and one that queues behind the founder.

*Territory: Creators and talent.*

**8. Ten percent of static spend goes to people over 65 and nothing is made for them**

Buyers 65 and older take 8.9% of lifetime spend and 10.0% of static spend. Facebook takes 64.0% of static spend and the biggest static in the account delivered 99.6% on Facebook. So there is an older audience being reached in volume on Facebook feed, and every ad reaching them was built for a 35-year-old on Instagram Reels, with fast cuts and dense graphic overlays.

*Pull: Curiosity.* It fired when the static and video demographic splits diverged, and the static half turned out to be reaching a materially older audience that no creative in the read acknowledges.

*Question: What do buyers over 55 want from this device that the younger ones do not?*

If that group converts at all, they are converting on creative built for somebody else, which usually means the ceiling is far higher than it looks. Answering it would also tell the account whether its Facebook half deserves its own creative rather than the Instagram cuts poured into it.

*Territory: Personas.*
