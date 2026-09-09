---
brand: hoolest-performance-technologies
doc: ad-comments
generated_on: 2026-09-08
refresh_by: 2026-11-07
sources_read:
  - Parker MCP `search_facebook_ad_comments_sql`, brand-wide, six pages of 300 sorted newest first, covering 2026-05-30 to 2026-09-08
  - Parker MCP `search_facebook_ad_comments_sql`, two pages of 300 with an upper bound of 2026-05-30, reaching back to 2024-08-09
  - Parker MCP `search_facebook_ad_comments_sql`, one page of 300 sorted by like count, to surface the comments the audience itself upvoted across the full corpus
  - Parker MCP `search_facebook_ad_comments_semantic`, two recognition queries against all 6,562 embedded comments
  - Parker MCP `search_facebook_ads_sql`, adIds and grouped lookups on the ads carrying the heaviest comment volume, so each thread could be read against the creative it sits under rather than against its ad name
  - Parker MCP `get_brand_persona` for the brand's stated ICPs, so the showed-up read had a targeted read to sit against
comments_read: 2,617 unique comments out of 6,562 in the corpus, which is 39.9%. 1,797 are top-level and 820 are replies. They sit across 254 distinct ad names. The window runs 2024-08-09 to 2026-09-08, and the recent slice, 2026-05-30 to 2026-09-08, is read completely at 1,800 comments over 101 days.
data_limitations:
  - Every `author_name` in the corpus is null. There is no way to tell a repeat commenter from a new one, no way to separate the brand's own replies from a customer's except by voice, and no way to check whether one loud person is producing many of the comments in a thread. Every count below is a count of comments, never of people.
  - Roughly 66 of the 2,617 comments read, 2.5%, are written in a customer-service voice and appear to be the brand answering. They are left in the denominator because they cannot be separated with confidence, which means the customer share of every theme is slightly understated.
  - The comment tool's `total` field returns 0 on date-sorted calls and 6,562 on a like-sorted call. 6,562 is used as the corpus size. It could not be confirmed a second way.
  - Comments carry no platform field. Facebook permalinks appear on most rows, so the corpus reads as mostly Facebook, but the Instagram share cannot be measured. Since Instagram carried 55.3% of the last 90 days of ad spend, the comment corpus is probably tilted toward the Facebook audience rather than the whole served audience.
  - No comment can be tied to a purchase. Nothing here verifies who bought.
  - Post-purchase surveys hold zero responses for this brand, so the strongest corroboration source for anything found here does not exist yet.
---

# Ad comments — persona signal — Hoolest Performance Technologies

## Identity signals observed

How I worked, so you can weigh what follows. I pulled the comment corpus in nine passes: six pages walking backward from today, two pages reaching back past May, and one page sorted by likes so the comments the audience itself voted up came in regardless of date. That gave 2,617 unique comments, 39.9% of the 6,562 Parker holds, across 254 ad names. Then I read each recurring theme back against the ad it sits under, using the creative fields rather than the ad name, so I could tell who the ad was built for before judging who showed up. Counts below are shares of the 2,617 unless I say otherwise.

The caution that governs this whole doc: a commenter is not a buyer. These are the reactions of whoever Meta served. Some of the loudest voices here will never buy anything.

**The person who has already tried everything and is still not okay. Strong signal.**

The largest identity in the corpus, and the one the ads are built for. 167 comments, 6.4%, name anxiety or panic directly. They do not write like people shopping. They write like people reporting a condition. From "Longform - Nov 26th" on 2026-02-09: *"I've been wishing I could try this out just once so I could make sure it works. I have panic attacks every single day and it's awful. But I can't just pay $250 and hope that it is helpful for me!"* From "Longform - Nov 26th - Copy" on 2026-08-18: *"I suffer from severe anxiety. It is pretty much crippled me. I am a solo father and I have a lot resting on my shoulders."* From a whitelisted creator ad on 2026-04-02: *"Feel like im going to die every day, and no one understands it's truely terrible."*

The identity these reveal, my inference: someone who has stopped treating this as a mood and started treating it as a body that is broken. They talk in physical terms and they talk about the cost of the failed attempts before them. That lines up closely with the brand's stated Wired Lifer ICP, and the agreement is worth naming because it means the biggest ads are reaching the person they were written for. Confidence strong on the identity, unknown on whether they convert.

**The neurological patient with an implanted device. Strong signal, and the account never asked for it.**

This is the most surprising identity in the corpus. 47 comments, 1.8%, mention a vagus nerve stimulator implant or the letters VNS, and 27 mention seizures or epilepsy. More telling than the count is the engagement. The two most-liked comments in the entire corpus after the top one are both from this group. On "HPT009_VID_Authority Mash Up," 2026-05-28, at 87 likes and 26 replies: *"This genuinely sounds phenomenal, my daughter has a VNS device implanted for her seizures and it works wonders for her. I have done a lot of research on the VNS and mental health and its benefits, however, it is nearly impossible to get one for that sole purpose. This seems like a very attainable way for anyone who may need this for mental health purposes and they are unable to get a VNS implant."* On "HPT052_VID_Nick Trial Reels," 2026-08-23, at 93 likes: *"I have epilepsy so I have a vagus nerve stimulator implant and it doesn't help my seizures unfortunately, but it has been great for helping my anxiety! So I think this would be helpful for people who don't qualify for a VNS."*

These threads run long. The 2026-04-14 comment on "Partnership ad Dr Ryan Test" is a several-hundred-word first-person account of living with an implant since 2011, ending *"I would have welcomed death at one point in my life. Today because of stimulating my vagus nerve I have a life beyond my wildest dreams."*

The identity, my inference: a person or a caregiver who already believes in the mechanism completely, because they have lived inside it. They are not the skeptic the ads are written to convert. They arrive pre-sold on vagus nerve stimulation and are asking a narrower question, which is whether this specific device is for them. The account has no creative for that question. Confidence strong that the group is showing up, unknown whether they buy, and complicated by the fact that an implant appears on the brand's own contraindication list.

**The chronic illness community. Strong signal, and it is being turned away.**

45 comments, 1.7%, name POTS, dysautonomia, long covid, fibromyalgia, or an autoimmune condition. They ask a very specific question and they ask it over and over. From "Dr Ryan VeRelief #2," 2026-07-06: *"Would this help pots syndrome?"* From "HPT030_VID_Founder Golf Story," 2026-07-16: *"I wonder if it will help with Hyper POTS and adrenaline spikes."* From "HPT025_VID_Top5_Q&A," 2026-07-11, a long and careful answer from an owner: *"For me, a primary symptom of my POTS is that my sympathetic nervous system is always way overactive. My parasympathetic nervous system is barely active at all it seems like most days. This device helps my autonomic nervous system become more balanced."*

And then the friction. From "HPT025_VID_Top5_Q&A," 2026-07-09: *"It scared off my Mom who was diagnosed with pots, so I'm pretty upset with the way it was written. No care for ill people just CYA at all costs."* From a Hoolest Pro ad, 2026-04-21: *"Why would you say it's contraindicated for POTS; when the person doing the review states she was diagnosed with it? So the contraindications don't matter?"*

The identity, my inference: a person whose whole life is nervous system dysregulation, who is the most motivated buyer in the entire comment section, and who keeps running into a contraindication notice written by a lawyer. Confidence strong that the pattern is real, because it recurs across at least six different ads.

**The category comparison shopper who already owns a rival. Moderate signal, and it is almost all one rival.**

44 comments, 1.7%, name Pulsetto. Truvaga appears 6 times, gammaCore 4, Apollo 3. That ratio is lopsided enough to be a finding on its own: in the open comment sections, Hoolest has one competitor.

The comparisons are specific and they consistently land on the same axis. From "HPT025_VID_Top5_Q&A," 2026-07-15: *"Not liking that you have to hold in place!!! Would rather wear it around the neck. I like Pulsetto better!"* From "HPT022_VID_Top 5 Objection," 2026-07-18: *"Cherie Clare I didn't like the placement or the neck pressure for the pulsetto. I want to try this one."* From "HPT038_IMG_US vs THEM," 2026-08-10: *"I love my pulsetto fit, and have used it in a tiny village in Nepal, as well as on an airplane. I'd rather wipe off gel than replace gel tips, personally."* And from "HPT022," 2026-07-22, a person who owns both: *"I love both Pulsetto and VRelief. Pulsetto at home…VRelief away from home. Both are great."*

The identity, my inference: an experienced category user, further along than the ads assume, who is not choosing between a device and nothing but between two devices they can name. Confidence moderate.

**The engineer who calls it a TENS unit. Moderate signal, and it is the sharpest attack the brand faces.**

44 comments, 1.7%, invoke a TENS or EMS unit. From "LaurenDeCicco" whitelist ad, 2026-09-08: *"I feel like this is just a handheld version of a tens unit."* From "BACK IN STOCK RET," 2026-09-05: *"Over priced weak tens device. Bought two and absolutely regret it."* From "HPT037_VID_Gel Tip Vs Gel Paste," 2026-08-04: *"I mean this is an overpriced EMS-TENS unit."* From "Flex PEMF - 3," 2026-03-04: *"Get a 10's unit off amazon for 20 bucks..you'll thank me later."* From "HPT001_VID_Dr. Ryan #2 Iteration," 2026-07-16: *"Not for $200 lol cheaper to build one."*

Worth noting that this identity also defends the brand. From "HPT052," 2026-08-28: *"No you would not want to use a TENS unit to stimulate the vagus nerve on the neck. Not safe."*

The identity, my inference: someone with enough technical literacy to recognize the hardware category and enough confidence to price it. They are exactly the buyer the account's Authority Figure and Educational spend is aimed at, and roughly half of them arrive hostile. Confidence moderate on the identity, strong that the objection recurs across many ads.

**The person who wants it and cannot pay for it. Strong signal, and it is not a haggle.**

Inside the 243 price comments, 16 explicitly say they cannot afford it and want it anyway. From "Nick Founder_Ad_Nov 12," 2025-09-12: *"I wish I could afford this i have Vasel vagel ptsd potta depression n anxiety. God please have a charity program."* From "WillBurger" whitelist ad, 2026-08-08: *"I need this but can't afford it."* From "HPT052," 2026-08-21: *"Jesus. If only people who really need this could afford it."* From "4x Flex Nick Mar 11th," 2026-04-21: *"I'm sorry, did you say first responders? Paramedic here, and my husband is an ex-dispatcher with cptsd.... So, ya know... we're below the federal poverty line. $199 plus all the doo-dads still sounds too expensive."*

The identity, my inference: a person whose need is severe and whose income is not. They are not negotiating. They are describing a wall. Confidence strong that the pattern recurs, unknown how big the group is relative to buyers.

**The caregiver. Thin signal, and thinner than it should be.**

19 comments, 0.7%, describe buying for someone else or wishing they could. From "BACK IN STOCK RET," 2026-08-10: *"I got my husband one and it helps with panic attacks but definitely doesn't stop them. Unfortunately Xanax is the only thing that stops my husbands. He has PTSD from the military."* From "Longform - Nov 26th," 2026-05-04: *"I will chime in, I bought myself one and a year later I bought my husband one as well."* From "Hoolest pro - baby hand Jan 20th," 2026-01-29: *"I would absolutely love to get my hands on something like this for my nonverbal autistic son. Anything to get him untrapped from his brain."*

Confidence thin on size. Real as a signal, since it recurs across five different ads over eight months, but 0.7% is not a base to plan on.

**Who is almost absent.** First responders, military and veterans account for 14 comments, 0.5%, and several of those are jokes about tasers rather than people identifying as first responders. HRV and wearable talk accounts for 6 comments, 0.2%. Menopause accounts for 3. These are the identities the brand's own ICP list leans on, and in the open reactions to its ads they barely exist.

## Recurring objections, with the identity behind each

Ranked by how widely each recurs across ads, not just by count.

**1. The gel tip subscription. 152 comments, 5.8%. Recurs across at least 14 different ads. The most distinctive objection this brand has.**

This is not a price complaint dressed up. It is a checkout complaint, and several commenters say plainly that it stopped a purchase. From "HPT009_VID_Authority Mash Up," 2026-06-01: *"Almost purchased. Then I saw you can't take off the monthly support in the cart. So you sneakily tried to make this a subscription based scam."* From "HPT014_VID_Winner Video Memorial Day," 2026-05-23: *"I would buy this product and others if it weren't for everyone pushing a subscription!!!! So, you lost another sale because of the $11 a month!!!!"* From "HPT025_VID_Top5_Q&A," 2026-07-26: *"Sneaky way to hide monthly subscription fee with no opt out. Sorry, product looks good but won't do subs."* From "WillBurger," 2026-07-28: *"I was going to order, but it was trying to set up my monthly subscription with a $50 shipping charge with no other shipping options."* From a 2025-12-31 comment on "BLACK FRIDAY 2024": *"When you go to check out there is Mandatory reoccurring charge... That makes me doubt all the products they make when they do shady business like that."*

There is a second layer underneath it, from people who already own the device and find the tips do not last. From "HPT061_VID_College Student," 2026-09-01: *"I just received mine. I like it as a ADHD high performing anxiety individual. I'm a bit frustrated as to how fast my gel tips have dried out! I purchased a years worth ……. 1 set hasn't lasted 4-5 days."* From "HPT026_VID_Fight or Flight," 2026-07-28: *"Be aware of the cost of continuing to have to buy the tips! Way over priced!"*

And a third layer, people routing around it. From "BACK IN STOCK RET," 2026-06-21: *"The one thing I don't like is the rubber prongs wear out rather fast and they try to get you on a subscription to keep you paying forever. Claude told me I can use ultrasound gel to apply to it to get around that and it cost me $6 a tube."*

The identity behind it, my inference: a careful buyer who reads a cart before submitting and treats a mandatory recurring charge as a character test the brand failed. Notably, this is the same person the account's whole friction message is aimed at, the one who was promised no app, no gel, no subscription. The account sells freedom from friction and then meets them with a subscription at checkout. That is not a price objection. It is a trust objection.

**2. Price. 243 comments, 9.3%. Recurs across nearly every ad with meaningful volume.**

Highest count, but ranked second because it is less specific and less actionable than the subscription. It splits three ways. There is sticker shock: *"Holy hek it's pricey !"* on "BLACK FRIDAY 2024," 2025-12-31. There is value contempt from the TENS crowd: *"imagine spending $200 for a 'it feels good'"* on the "ClaytonStakelbeck" whitelist ad, 2026-07-22, and *"$299 for a TENS unit?"* on "HPT052," 2026-08-22. And there is the affordability wall described above.

There is also one long comment that argues the other way and is worth carrying because it is the most complete price defense anyone in the corpus wrote, from "BLACK FRIDAY 2024," 2024-11-18: *"Is it too expensive? For what it does, no. One trip to a psychiatrist would cost similar, and I spent 2 decades burning that money with absolutely no results."*

The identity behind it: not one identity. Price is voiced by the affordability-blocked sufferer, by the hostile technical skeptic, and by ordinary comparison shoppers. Treat it as an overlay, not a persona.

**3. Prove it. 87 comments, 3.3%, plus 70 more, 2.7%, that go further and call it a scam.**

The proof demand is polite and specific. The single most-liked comment in the entire corpus, at 214 likes and 21 replies, sits on the PEMF ads from 2026-02-23 and reads in full: *"I'd like to see the clinical studies that show the safety and efficacy of this device."* From "Dr Ryan VeRelief #2," 2026-06-17: *"Can anyone confirm that it's not snake oil?"* From "HPT027_VID_Founder Story," 2026-07-08: *"Why has your research not been submitted for peer review? It could make great strides in the veteran community but without the correct research, data, and backing, it would not be funded."*

The scam version is blunter. *"That add sounds bogus…."* and *"Quackery"* both on "HPT009_VID_Authority Mash Up," 2026-06-01. From "HPT030_VID_Founder Golf Story," 2026-07-02: *"Quack."* From "Longform - Nov 26th," 2026-05-03: *"Ever since the discovery of electricity there have been constant scams involving 'miracle' electrical devices."*

And a targeted attack on the partnership talent, from "HPT001_VID_Dr. Ryan #2 Iteration," 2026-07-19: *"'Functional neurologist' that's a weird way to spell 'chiropractor' Always grifter either useless gimmick or supplements... or both."*

The identity behind it, my inference: the mechanism skeptic the account already courts, arriving unconverted. The proof stack the ads carry, three placebo-controlled studies, 94% of 1,300 first responders, a 31% HRV lift, is not landing as proof for this group, because what they are asking for is peer review and a device-specific trial, which is exactly the gap the brand context already flags as a weakness against Truvaga.

**4. Is it safe with my condition. 86 comments, 3.3%. Recurs across at least ten ads and it is asked, not argued.**

This is the highest-intent objection in the corpus, because everyone asking it wants to buy. From "HPT022_VID_Top 5 Objection," 2026-08-31: *"Safe with heart pacemaker devices?"* From "BACK IN STOCK RET," 2026-07-26: *"myhusband has a neck fusion I dont think this would be a ood idea for him."* From "HPT028_VID_Unique Mechanism," 2026-07-01: *"Is this safe for kids?"* From "Longform - Nov 26th," 2026-05-03: *"Sounds great, but is it safe to use if you have CRPS?"* From "HPT001_VID_Dr. Ryan #2 Iteration," 2026-07-18: *"I have a vagus nerve stimulator implant to help control seizures... found that you can't use if you have an implant or tinnitus. I have both. 😩"*

The identity behind it: the neurological and chronic illness communities above, plus older buyers with cardiac hardware. They are not skeptics. They are people trying to give the brand money and being blocked by an unanswered question.

**5. You have to hold it. 22 comments, 0.8%, but concentrated and consistent.**

Small count, sharp signal, and it recurs across at least six ads. From "ClaytonStakelbeck," 2026-07-24: *"I wonder why he designed it that you have to hold it? It would be more relaxing if you did not have to hold it."* From "HPT022," 2026-07-19: *"How long do you have to hold it on your neck for? I have bad shoulders."* From "TaylorByrne" whitelist ad, 2026-08-10: *"it's annoying to hold it on your neck for 10 minutes."*

The identity behind it, my inference: the comparison shopper who has seen the neck-worn rival and reads holding as work rather than as portability. The account's own creative frames handheld as the advantage. In the comments it reads as the drawback about a third of the time it comes up.

**6. The founder's benzodiazepine line is not believable. 9 comments, 0.3%, but clustered on high-spending ads and worth flagging above its count.**

From "HPT009_VID_Authority Mash Up," 2026-05-30: *"'I was a competitive golfer with bad performance anxiety and all they would do is prescribe me benzodiazepines, so I got my PHD in biomedical engineering.' Ok, sure pal. That's how it all happened."* From "HPT004_VID_Nick Invention," 2026-05-26: *"Where are these doctors you only want to prescribe benzodiazepines? Asking for a friend 😅"* From "HPT009," 2026-05-31: *"Literally never met a psychiatrist that just wants to prescribe benzos. They just want to prescribe ssri's and keep you on them til the end of time."* From "HPT009," 2026-05-30: *"Yeah right doctors dont write benzos anymore they'll give you antidepressants."*

This matters more than 0.3% suggests. The founder origin story is the account's single most-funded message. One line inside it is being read as a lie by people who take medication, and it is the line meant to earn their trust. Note the same ad also drew *"This is n excellent ad... The possibility of getting off benzos or never starting them is a big deal,"* on the long-form founder cut, 2026-06-02, so the line splits the audience rather than uniformly failing.

**7. Shipping and service. 32 comments, 1.2%.**

From "HPT059_VID_FAQs," 2026-08-21: *"It works great but they take forever to ship anything."* From "HPT022_VID_Top 5 Objection," 2026-06-29: *"I just ordered a bunch of replacement gel tips and they are the wrong size. And it took a month to get those. Not going to even bother to try and return them."* From "Longform - Nov 26th," 2026-06-08: *"I just bought it and received last week but there were no gel tips, just the device and charger in a nice box."*

Small share, and it corroborates the 3.2 Trustpilot rating already named in the brand context.

**8. It did not work for me. 17 comments, 0.6%.**

Worth logging honestly. From "HPT049_VID_Feel it working," 2026-08-05: *"You can feel the stimulation, but I have not noticed any effect beyond that. Seems like more snake oil. Returning."* From "HPT009," 2026-06-02: *"I know I sent it back too. After being shocked for several minutes I felt like it made my anxiety worse."* From a whitelist ad, 2026-09-07: *"Got one, did not like it at all and made my anxiety worse unfortunately."*

Against that, 63 comments, 2.4%, report that it does work for them, and 90 comments, 3.4%, are written from the position of already owning it. So the owner voice in this corpus runs roughly four to one positive. That ratio is a comment-section ratio, not a return rate, and should not be read as one.

## Moments of recognition

These are the places a commenter handed over an identity without being asked. They are the strongest persona signal a noisy source can produce.

**Recognition of the mechanism as the missing explanation.** From "HP new ads mar 15th," 2026-03-18: *"So thats what wrong with me. My brain isnt connected to my body."* From the PEMF demo ad, 2026-03-18: *"im stuck in that mode."* From the PEMF demo ad, 2026-03-30: *"I definitely need something like this! I am definitely stuck."* And from the same ad the same day: *"Whaaat?! I am always talking about this brain body disconnect that I deal with and the only mild relief and reconnection is small 420 doses but it's not enough."*

What these hand over: the vagus nerve explanation is doing identity work, not just science work. It gives a name to something the person had already noticed about themselves and could not label. That is the Trigger phase of TEEP working exactly as it should, mirroring the internal state back with precision before offering anything.

**Recognition at the exact hour the product is for.** From "Longform - Nov 26th," 2026-04-07: *"I think I need this/ as I write at 1:22am."* Two likes. One line, and it is the entire sleep persona the brand's ICP list describes and the account never advertises to.

**Recognition of a life, not a symptom.** From "Longform - Nov 26th," 2026-05-01: *"Very interesting. My husband has ptsd from nearly being killed on the job in a fire. We have veteran friends who struggle. I struggle. My daughter is highly intelligent and has test anxiety performance anxiety needs constant things for her hands to do to get mindless reset. This might be something we can all use. I could not afford it but thank you for working on something to help such a huge facet of life needing great awareness."*

Read that one twice. In a single comment a woman names a firefighter with PTSD, a veteran community, herself, and a daughter with test anxiety. That is four of the identities in this doc, three of them unserved by the account, and it ends on the affordability wall.

**Recognition through humor, which is its own tell.** From "Kenzie Williams" whitelist ad, 2026-07-09: *"tbh at this point I'd be fully willing to taze myself if it fixes my anxiety 😂😭"* From "Nick_Not a Taser_Feb 9th," 2026-03-08: *"Ope… the anxieties are happening, better taze myself 🤣🙌🏻 yes."* The taser joke recurs, and it is affectionate rather than hostile. It is people saying they are desperate enough to try something that looks alarming.

**Recognition from the owner side.** From "HPT022_VID_Top 5 Objection," 2026-07-24: *"100% love device , best the best$150 I have ever spent. Its good for before fight or flight, after fight or flight ... amazing....and Reccommended before sleep and I use it anytime my thoughts start racing...wow 30 sec on each side... I even used it during a job phone interview to keep me calm."* From "Longform - Nov 26th," 2026-05-04: *"I use mine with hemi sync Alpha tracks in my earbuds... I do this five days a week when I pull into the parking lot at my job. Earbuds in, five minutes on each side."*

Both describe use cases the ads never show: before a phone interview, in the parking lot before a shift, layered with binaural audio. The second one in particular is a ritual the brand did not design and does not advertise.

## Targeted-versus-showed-up gap

**The ad that drew the most comments is the one that converted worst.** "HPT009_VID_Authority Mash Up" carries 276 comments in my sample, the most of any ad by a wide margin, and it is the ad the benzo disbelief, the quackery calls and the tasing jokes cluster on. In the ad account it spent $52,318 lifetime at a 0.85 ROAS and a $255.21 cost per purchase, the worst cost per purchase of any ad above $50,000 in spend. It was built for what the naming convention calls a C-suite operator and the creative is a stack of three authority figures. Who showed up was an argument. Comment volume and conversion moved in opposite directions here, which is the plainest possible warning against reading engagement as performance.

**The account targets skeptics and gets believers it cannot serve.** The Authority Figure and Educational creative carries 52.7% of lifetime ad spend and is built to convert someone who does not believe vagus nerve stimulation works. The comment section keeps delivering the opposite person: 47 comments from people who already have an implanted stimulator and 45 from people managing dysautonomia, who need no convincing about the mechanism at all. The ads answer "does this work." These commenters are asking "will this work for me, specifically, with my condition." Those are different questions and only one of them is being answered.

**The brand's own trust channel does not show up in its own comments.** First responder, military and veteran mentions total 14 comments, 0.5%, and the ad account spends $513,932 lifetime on ads that carry the first responder statistic. When they do appear, it is often to point out the mismatch, as the paramedic did on 2026-04-21. The account tells the world that 1,000 first responders trust this device. The world's reply, in the comments, is mostly silence and one paramedic saying she is below the poverty line.

**Instagram is where the money goes and Facebook is where the talk is.** Instagram carried 55.3% of the last 90 days of ad spend, but nearly every permalink in the corpus is a Facebook URL. So this doc describes the reaction of the Facebook half of the served audience. Given that Facebook delivery skews older, the identities here are probably older than the identities the Instagram half would surface. Marked as a real blank rather than a finding.

**The comment prompt works and nobody has looked at what it caught.** "HPT052_VID_Nick Trial Reels" ends with *"Comment the word RESET if you're willing to try this."* 25 comments in the corpus, 1.0%, are the single word reset. That is a small, self-selected list of people who publicly raised their hand and, as far as this doc can see, were never followed up with.

## Behavioral-signal states observed

Overlays, not identities. Attach these to personas rather than promoting any of them.

**Mid-episode.** People commenting while it is happening. The 1:22am comment is the clearest example. So is *"I just got mine and I'm excited to use it when my anxiety and panic symptoms trigger from when I drive around traffic or congested areas,"* from "BACK IN STOCK RET," 2026-07-28.

**Actively comparison shopping.** 44 Pulsetto mentions plus the how-is-this-different questions. From "Longform - Nov 26th," 2026-04-28: *"How is this different than gammacore and Truvaga?"* This is the Evaluation phase of TEEP, and what these people need is the specific difference named, not more benefit.

**Blocked at the cart.** The subscription objection is a state, not a trait: a person who had decided to buy and stopped in checkout. Distinct from price, and far more fixable.

**Post-purchase confusion.** 25 comments, 1.0%, ask how to use it, where exactly to place it, or how long to hold it. From "HPT022," 2026-07-31: *"I can't tell if I'm using it correctly and the descriptions aren't very helpful. I am trying to use it when I have panic episodes."* A person who bought and cannot get it to work is a refund and a bad review waiting to happen.

**Advocating on the brand's behalf.** Owners answering skeptics unprompted, repeatedly. From "Longform - Nov 26th," 2026-06-06: *"Bobby Boucher I can say it does actually work it's not a scam I actually have it and use it."* From "HPT001," 2026-07-12: *"there's legitimate science backed studies for vagus nerve simulators... its definelty not snake oil."* This is free defense the brand is getting and not organizing.

**Stacking it with something else.** A recurring pattern where the device is used alongside another practice: binaural audio in the parking lot, an ice pack at the start of a migraine aura, a Whoop band to check the effect. From "WillBurger," 2026-07-28: *"I wear a whoop band and if I use the Hoolest before bed, my whoop will register lower heart rate and higher HRV. I also get migraines with aura and if I can get into bed with an ice pack and my Hoolest when the aura starts, it'll blunt the migraine a ton."*

## Corroboration and noise

**Scope.** 2,617 unique comments read out of 6,562, 39.9% of the corpus, across 254 ad names, from 2024-08-09 to 2026-09-08. The recent slice is complete: every comment from 2026-05-30 to 2026-09-08, 1,800 of them over 101 days, roughly 17.8 a day. 1,797 are top-level and 820 are replies, so 31.3% of what is logged is people replying to each other rather than to the brand.

**Where the comments actually live.** Nine ads carry 60% of the volume in my sample. "HPT009_VID_Authority Mash Up" 276, "Longform - Nov 26th" and its relaunch names 209, the "Prime PDP BOFU" static and its aliases 179, "HPT025_VID_Top5_Q&A" 113, the "WillBurger" whitelist ad 107, "PEMF_PDP_Demo_TRex" 102, "HPT052_VID_Nick Trial Reels" 89, "HPT022_VID_Top 5 Objection" 75, and "HPT001_VID_Dr. Ryan #2 Iteration" 70. Note that "PEMF_PDP_Demo_TRex" is for the $6,000 PEMF unit, not VeRelief, and it drew 102 comments including the single most-liked comment in the corpus. Some of the loudest reaction in this doc is to a product almost nobody is being asked to buy.

**Signals I trust, because they recur across many different ads.** The gel tip subscription objection, across at least 14 ads. The safety question, across at least 10. Price, across nearly all. The Pulsetto comparison, across at least 8. The proof demand, across at least 6. The chronic illness question, across at least 6. Each of these is a pattern in the sense the open-loops rubric means it, the same thing appearing independently in places that do not touch.

**Signals I do not trust yet.** The benzodiazepine disbelief is 9 comments and clusters heavily on two ads from May and June 2026, so it could be one thread's crowd rather than a real audience reaction. The caregiver identity is 19 comments and needs the reviews to corroborate it. The hands-free objection is 22 comments. The reset list is 25 comments on one concept. Treat all four as leads, not findings.

**Reaction-noise I logged and am discounting.** The tasing jokes, which are numerous and mostly affectionate. A stray thread about horses. Several comments that are just a tagged name with no content. The 66 comments in a customer-service voice that are probably the brand.

**What corroborates what.** The chronic illness and neurological identities are the strongest cross-source candidates in this doc, because they appear in the comments, they appear in the highest-liked comments, and they map onto nothing in the brand's stated ICP list. The affordability wall corroborates the brand context's own note that price is a real barrier above the impulse threshold. The shipping and service complaints corroborate the 3.2 Trustpilot rating. The first responder identity does the opposite of corroborating: the brand's context leans on it hard and the comment corpus does not carry it. Every one of these needs the reviews doc and the reputation doc to confirm, and none of it can be checked against post-purchase surveys, because there are none.

## Open loops

**1. The implanted-stimulator community keeps showing up and nobody knows why**

47 comments, 1.8% of the corpus, come from people with an implanted vagus nerve stimulator or a family member who has one, and two of the three most-liked comments in the whole corpus are theirs. They arrive already believing the mechanism works, because they have lived with it. The account has never made an ad for them, and an implant appears on the brand's own contraindication list.

*Pull: Gap.* It fired when I sorted the corpus by likes to find what the audience itself upvoted, and the top of that list turned out to be a conversation about surgical implants rather than about the product being advertised.

*Question: Who are the people arriving from the implanted-stimulator world, and what do they want from a handheld device?*

They are the only group in the comments that needs no convincing about the science, which is where the account spends most of its money. If they are a real buyer group, the most expensive part of the creative is unnecessary for them. If they are all contraindicated, the brand is drawing an engaged audience it cannot legally sell to and should know that.

*Territory: Personas.*

**2. The subscription is stopping sales at the cart**

152 comments, 5.8%, are about the gel tip subscription, and several say in plain words that it ended the purchase: *"So, you lost another sale because of the $11 a month!!!!"* and *"product looks good but won't do subs."* This is the brand whose whole creative promise is no app, no gel, no friction.

*Pull: Tension.* It fired when the friction message the ads sell hardest turned out to be the exact thing the comments accuse the checkout of doing.

*Question: How many people reach the cart and leave when the subscription appears?*

This is the only objection in the corpus that names a specific moment in a specific funnel step, which makes it the cheapest thing on this list to check and possibly the cheapest to fix. It sits with the brand, since only they can see the cart data.

*Territory: Product. Routes to the brand.*

**3. People with POTS and dysautonomia are the most motivated askers and the safety copy pushes them away**

45 comments, 1.7%, come from people managing POTS, dysautonomia, long covid, fibromyalgia or an autoimmune condition, asking whether it will help. One reply names the outcome directly: *"It scared off my Mom who was diagnosed with pots, so I'm pretty upset with the way it was written."*

*Pull: Pattern.* It fired when the same condition question came back on six different ads over four months, always phrased as somebody hoping rather than doubting.

*Question: How large is the chronic illness group inside this brand's actual buyer base?*

They have the deepest need and the highest intent of anyone in the comments. If they already make up a real share of buyers, the safety language is turning away customers the brand already has. If they do not, the brand is absorbing a lot of unanswerable questions with no revenue behind them.

*Territory: Personas.*

**4. One line in the founder story reads as a lie to people on medication**

Nine comments push back on the same sentence in the account's most-funded message, the claim that doctors would only prescribe benzodiazepines. One reads: *"Literally never met a psychiatrist that just wants to prescribe benzos. They just want to prescribe ssri's and keep you on them til the end of time."*

*Pull: Surprise.* It fired because the founder origin story is the most-repeated message in the account and I expected the pushback to be about the product, not about a detail of the backstory.

*Question: Why does the medication part of the founder story land as untrue for people who take medication?*

The whole point of that line is to earn trust with the buyer who wants an alternative to pills, which is the brand's own Off-Ramper ICP. If it is doing the opposite for that exact group, it is the highest-leverage sentence to fix in the account.

*Territory: Messaging.*

**5. Pulsetto owns the comparison and nobody else is in it**

Pulsetto appears in 44 comments. Truvaga appears in 6, gammaCore in 4, Apollo in 3. In the open, this is a two-brand category, and the axis people compare on is almost always the same one: whether you wear it or hold it.

*Pull: Curiosity.* It fired when the competitor counts came back nine to one in favor of a brand the Hoolest context describes as having credibility problems.

*Question: What makes Pulsetto the only rival that customers actually name?*

The account runs comparison creative and it converts better than almost anything else it runs, at a $101.51 cost per purchase on "HPT025." Knowing which rival the buyer already has in mind decides what that creative should actually compare against.

*Territory: Messaging.*

**6. Holding the device reads as a chore, not a feature**

22 comments, 0.8%, across at least six ads, treat the handheld form as a downside. *"I wonder why he designed it that you have to hold it?"* and *"it's annoying to hold it on your neck for 10 minutes"* and *"Not liking that you have to hold in place!!!"* Every ad in the account frames handheld as portability and freedom.

*Pull: Tension.* It fired because the brand's stated advantage and the commenters' stated complaint are the same physical fact.

*Question: For whom is holding the device a problem?*

If it is mostly people comparing against a neck-worn rival, it is a messaging fix. If it is people with shoulder pain, arthritis or long sessions, it is a product and a persona finding. The comments cannot tell those apart.

*Territory: Product.*

**7. The single hour the product is most needed never appears in an ad**

One comment on the biggest ad in the account reads, in full: *"I think I need this/ as I write at 1:22am."* Sleep and insomnia appear in only 29 comments, 1.1%, but the account also never asks about them. The brand's own ICP list calls the sleep buyer the largest and least stigmatized group in the base.

*Pull: Resonance.* It fired because that one line, written at 1:22 in the morning, does more persona work than most of the corpus.

*Question: How many people come to this brand because of the night rather than because of the day?*

Everything the account currently says is about daytime pressure: work, meetings, the first tee, the checkout line. If the real trigger is lying awake, the account is describing the wrong hour of the customer's life.

*Territory: Personas.*

**8. Twenty-five people raised their hand and nothing visible happened**

"HPT052_VID_Nick Trial Reels" asks viewers to comment the word RESET. 25 comments in the corpus are exactly that word. There is no sign in the corpus of a reply, a follow-up, or a next step to any of them.

*Pull: Gap.* It fired when I scanned for single-word comments expecting noise and found a self-selected list of interested people sitting untouched.

*Question: What happens to someone who comments RESET?*

That is the highest-intent, lowest-cost audience the account produces, and only the brand can say whether anything is being done with it.

*Territory: Product. Routes to the brand.*
