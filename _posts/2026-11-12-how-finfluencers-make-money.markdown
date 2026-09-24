---
layout: post
title: "How finfluencers make money (and why it isn't from the tips)"
description: "Referral fees, paid courses, sponsored posts and the pump: the incentives behind financial content, what SEBI did about them, and this blog's own disclosure."
image: /assets/og/how-finfluencers-make-money.png
date: 2026-11-12 09:00:00 +0530
series: risk
---

{% assign f = site.data.fno %}
{% assign u = f.fy26_unverified %}

## The question to ask about every piece of financial content

Including this one: *how does the person telling me this get paid?*

Not because paid content is automatically wrong — most of it isn't — but
because the answer predicts what the content will push you toward. A
**finfluencer** (financial influencer: someone producing investment content
for an audience, usually on social media, usually without a SEBI
registration) is running a business. The product is rarely the advice. The
advice is the funnel. This closing post of the risk series walks through the
funnel's plumbing, the rules SEBI has put around it, and — since the same
question applies here — how this blog is and isn't paid.

No individuals are named. The structures are the point; the people change.

## The five revenue models

**1. Referral commissions.** The largest one, historically. A broker,
trading app or investment platform pays a fee for every account opened
through a link — often a flat amount per account, sometimes a share of the
brokerage the referred client goes on to generate. Notice what that second
kind rewards: not the client's returns, but the client's *activity*. The
[F&O post]({% post_url 2026-11-05-what-the-fo-numbers-actually-say %}) put
individual traders' transaction costs at roughly
₹{% include inr.html n=u.transaction_costs_cr_fy26 %} crore in FY26 alone. A
slice of that flows back to whoever brought the traders in. Content that
makes derivatives look accessible, exciting and frequently profitable is
worth more under this model than content that quotes the loss rate.

**2. Paid courses and communities.** A free feed of confident, simplified
market commentary; a paid course, Telegram channel or "mentorship" behind it.
The economics are excellent — near-zero marginal cost per student — and the
incentive is to make the *skill* look learnable and the *results* look
routine. Testimonials are selected. Losses aren't screenshot.

**3. Sponsored content and brand deals.** A fund house, a fintech, an
insurance seller or an NFO (new fund offer) pays for a mention, a review or an
"explainer." Sometimes disclosed with a small #ad; often not. The tell is
content that reviews a product without ever finding a reason not to buy it.

**4. Platform monetisation.** Ad revenue and creator payouts scale with
views. Views scale with certainty, urgency and drama — "this stock will
double," "sell everything before Monday." Measured, hedged content is
correct more often and watched far less. This is the mildest incentive on
the list and still bends everything toward hype.

**5. The pump.** Buy a thinly traded small-cap, talk it up to a large
audience, sell into the buying you created. Illegal under SEBI's fraudulent
and unfair trade practices regulations, and regularly the subject of SEBI
orders. It's rarer than the other four and far more damaging when it
happens, because the audience is the exit liquidity by design.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a kid at school who gives everyone tips on which cricket cards to
buy. He's very confident and very popular.

What you don't see: the card shop pays him ₹5 every time someone he sent
buys a pack. So he wants you to buy *lots* of packs, often. Whether the cards
turn out to be good doesn't change his ₹5.

He's not lying about liking cricket. He's just not paid for being right.
He's paid for you buying.

</details>

## What each model rewards

| Model | Paid for | Content it favours | Content it punishes |
|---|---|---|---|
| Referral commission | Accounts opened, trades made | "Anyone can trade," derivatives, frequent activity | Base rates, "do less" |
| Courses / communities | Sign-ups | Certainty, screenshots of wins, a learnable "system" | Honest win/loss records |
| Sponsored content | The sponsor's product | Product reviews with no downside | Comparisons that favour a competitor, or nothing |
| Platform revenue | Views | Predictions, urgency, drama | Hedged, slow, boring |
| The pump | The exit | A specific small stock, right now | Anything after they've sold |

Read the right-hand column. Almost everything this blog has spent seventy
posts on — base rates, recovery times, why volatility is expensive, what
ratios can't tell you — sits there. That isn't a coincidence and it isn't a
virtue. It's that none of those things are monetisable through the models
above, so nobody with those incentives produces them.

## What SEBI has done

The regulator has moved on this in stages. The rules below are stated only at
the level I'm confident of; a compliance professional would add detail.

- **Registration is the line.** Giving investment advice or research
  recommendations for a fee requires registration as an Investment Adviser
  or Research Analyst. Unregistered persons doing so are in breach, and SEBI
  has passed orders against several, including disgorgement of fees.
- **Regulated entities can't associate with them.** From 2024, SEBI
  prohibited its regulated intermediaries — brokers, fund houses, registered
  advisers — from having any association, including paying referral fees,
  with persons who give unregistered advice or make performance claims. This
  is the rule aimed at revenue model one. It cut off the largest funding
  source for tip-based content at the intermediary end rather than trying to
  police every creator.
- **Education is carved out — with conditions.** SEBI subsequently clarified
  that regulated entities *may* associate with persons engaged purely in
  investor education, provided the content makes no recommendations and no
  claims about returns. In the same clarification, educational content was
  told not to use recent live market data — which is where this blog's rule
  that every real figure is at least three months old comes from. That
  three-month lag is not a house style. It's the regulator's definition of
  the boundary between education and a call.
- **Disclosure norms exist alongside.** The Advertising Standards Council of
  India's guidelines require influencers giving financial content to disclose
  material connections and, for advice, their registration. Enforcement is
  softer than SEBI's, but the norm is on the record.

Two limits of all this. First, the rules govern what *regulated* entities
may do; a creator funded by course sales and platform revenue is outside
that perimeter, and both models remain fully legal. Second, the line between
"education" and "recommendation" is a judgment. A post that explains a ratio
using a named company's numbers is education. The same post ending "and
that's why it's a buy" is not. This blog lives on the first side of that line
on purpose, and the line is the reason the disclaimer at the bottom of every
post is identical.

## This blog's incentives

The same question, asked of Wealth Primer.

- **No referral links, no brokerage or platform partnerships.** Nothing here
  earns money from you opening an account or making a trade.
- **No courses, no paid community, no sponsored posts.**
- **No ads.**
- **Analytics** run on this site (Google Analytics), so I can see which posts
  are read. That's disclosed on the privacy page.
- **A newsletter signup** appears on posts. It's free, and the only thing it
  earns is a reader who comes back. If that ever changes, it'll be written
  here first.
- **Registration:** I'm not a SEBI-registered Investment Adviser or Research
  Analyst, which is why nothing on this site is a recommendation and every
  real figure is lagged.

That's the honest position: the blog's incentive, today, is to be read and
trusted, which is a real incentive and not a neutral one. It rewards being
right over time and punishes being caught wrong. Given the alternatives in
the table above, it's the one I'd choose to be judged by — but you should
know it's there.

## Common mistakes

- **Judging content by confidence.** Confidence is what the revenue models
  reward. Hedging is what accuracy requires. They point opposite ways.
- **Treating "I'm not paid to say this" as the whole disclosure.** Ask what
  they *are* paid for. Course sales and referral fees don't need a sponsor.
- **Assuming a large audience is a track record.** Audience measures
  distribution. Only a verifiable, complete record of calls — losses
  included — measures accuracy, and almost nobody publishes one.
- **Mistaking a screenshot for a statement.** A P&L screenshot shows one
  account, one period, selected by the person who benefits from your seeing
  it.
- **Concluding that all financial content is compromised.** Plenty of it is
  useful. The point is to know the incentive before weighing the content, not
  to dismiss the content because an incentive exists.
- **Not asking the question of this blog.** You should. The answer is above.

**Takeaway:** Financial content is mostly a funnel, and the funnel is paid by
accounts opened, courses sold, sponsors served or views won — none of which
reward being right, and all of which reward certainty, activity and drama.
SEBI has cut off the referral pipe for unregistered advice and drawn a
three-month line between education and a call. Before weighing any tip,
including anything here, ask how the person telling you gets paid.
