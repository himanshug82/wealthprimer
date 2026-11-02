---
layout: post
title: "Credit ratings: what AAA does and doesn't tell you"
seo_title: "Credit rating explained: AAA, spreads and expected loss"
description: "A credit rating is an agency's opinion on whether a borrower will repay on time. How ratings link to yield spreads and expected loss, on invented numbers."
image: /assets/og/credit-ratings-explained.png
date: 2027-02-06 09:00:00 +0530
series: jargon
term: "Credit rating"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign rt = site.data.jargon_m9.rating %}

## What is a credit rating?

A **credit rating** is a credit rating agency's opinion on how likely a borrower is to repay a particular debt on time. It is published as a short symbol: letters such as AAA at the top and D (default) at the bottom, with plus and minus modifiers in between. It is attached to a specific instrument, such as one bond or one debenture, not to a company in the abstract, so one company can have different ratings on different debt. Rating agencies in India operate under rules from SEBI (the Securities and Exchange Board of India) (we did not open those regulations for this post), and each agency publishes its own scale and definitions. Check the agency's current rating scale for the exact wording.

Ratings matter to a reader of debt funds and bonds because the yield on a bond is the interest rate it pays for taking credit risk. A weaker rating usually means a higher yield, and a higher yield is not free money: it is the market's price for the chance of not being repaid. This post uses **hypothetical** numbers throughout and names no issuer. It follows the [YTM post]({% post_url 2026-10-05-yield-to-maturity %}) and is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

Two ideas link a rating to a yield:

```
Expected loss  ≈  probability of default × (1 − recovery rate)

Yield spread   =  yield on the borrower's bond  −  yield on a government bond of the same maturity
```

The **recovery rate** is the share of the money you get back after a default. The spread has to cover the expected loss, and then some, for lenders to accept the risk. A rating is an opinion about the probability part, and it doesn't measure the recovery or the spread.

## Worked example: an invented ladder

This table is **hypothetical**: the default probabilities, recovery and spreads are invented to show the arithmetic. They are not the rates of any agency or any issuer, and no rating scale is being quoted. A fixed recovery of {{ rt.grid[0].recovery_pct }}% is assumed in each row.

| Bucket | Assumed annual probability of default | Expected loss a year | Assumed spread | Spread left after expected loss |
|---|---:|---:|---:|---:|
{% for g in rt.grid %}| {{ g.bucket }} | {{ g.annual_default_prob_pct }}% | {{ g.expected_loss_pct }}% | {{ g.spread_pct }}% | {{ g.spread_minus_loss_pp }} points |
{% endfor %}
The spread is always larger than the expected loss here, because the lender wants to be paid for risk, not just reimbursed for it. The part of the spread above expected loss is a premium for bearing uncertainty, and it isn't guaranteed: if defaults come in higher than assumed, it disappears.

Now the effect on price. Take a {{ rt.years }}-year bond paying a {{ rt.coupon_pct }}% coupon, and a government yield of {{ rt.base_yield_pct }}%. A borrower priced {{ rt.issuer_spread_pp }} points above it yields {{ rt.issuer_yield_pct }}%:

| | Yield | Price of a ₹1,000 bond (₹) |
|---|---:|---:|
| Priced off the government yield | {{ rt.base_yield_pct }}% | {{ rt.price_at_base }} |
| Priced with the {{ rt.issuer_spread_pp }}-point spread | {{ rt.issuer_yield_pct }}% | {{ rt.price_at_issuer }} |

A {{ rt.issuer_spread_pp }}-point spread is a ₹{{ rt.price_gap }} ({{ rt.price_gap_pct }}%) lower price for the same coupons. If the market later decides the borrower is riskier, the spread widens and the price falls toward the lower figure and beyond, even if no default happens.

## What a rating doesn't tell you

- **It is an opinion at a point in time.** Ratings are reviewed and can be changed up or down.
- **It says nothing about price risk.** A top-rated long bond can lose value when yields rise ([modified duration]({% post_url 2026-10-06-modified-duration %})). The rating covers repayment, not market price.
- **It isn't a guarantee.** A high rating is a view on a low probability, not a zero one. The [riskometer post]({% post_url 2026-10-22-the-riskometer %}) shows how a fund-level measure uses credit quality as one input.

## Common mistakes

- **Reading the highest rating as "no risk".** It is the lowest credit risk on that agency's scale, still not nil, and it carries interest-rate risk.
- **Chasing the extra yield without asking what it pays for.** A higher yield is the market's estimate of risk. If it were free, it would not exist.
- **Treating a fund's average rating as the rating of each holding.** An average hides the spread between its best and worst bonds.
- **Ignoring liquidity.** A lower-rated bond can be hard to sell exactly when you want to ([liquidity risk]({% post_url 2026-10-17-liquidity-risk %})).

**Takeaway:** A credit rating is an agency's opinion on whether a specific debt will be repaid on time, and the extra yield on weaker-rated bonds is payment for that risk, not a bonus. A top rating still leaves interest-rate and liquidity risk on the table.
