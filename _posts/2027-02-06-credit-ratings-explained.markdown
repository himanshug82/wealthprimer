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

A **credit rating** is a credit rating agency's opinion on how likely a borrower is to repay a particular debt on time. It is published as a short symbol: letters such as AAA at the top and D (default) at the bottom, with plus and minus modifiers in between. It is usually attached to a specific instrument, such as one bond or one debenture, so one company can have different ratings on different debt. Rating agencies in India operate under the [SEBI (Securities and Exchange Board of India) (Credit Rating Agencies) Regulations, 1999](https://www.sebi.gov.in/acts/creditratingamend.pdf); the consolidated copy we read shows amendments up to March 2010, and later changes weren't traced. Each agency publishes its own scale and definitions. Check the agency's current rating scale for the exact wording.

Ratings matter to a reader of debt funds and bonds because the extra yield over a government bond of the same maturity is what a bond pays for taking credit risk. A weaker rating usually means more of that extra yield, and it isn't free money: it is, in large part, the market's price for the chance of not being repaid. This post uses **hypothetical** numbers throughout and names no issuer. It follows the post on [yield to maturity (YTM)]({% post_url 2026-10-05-yield-to-maturity %}) and is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

Two ideas link a rating to a yield:

```
Expected loss  ≈  probability of default × (1 − recovery rate)

Yield spread   =  yield on the borrower's bond  −  yield on a government bond of the same maturity
```

The **recovery rate** is the share of the money you get back after a default. Lenders normally want the spread to cover the expected loss, and then some. A rating is an opinion about credit risk, and it isn't a measure of the spread; what it says about recovery varies, so check the agency's definition.

## Worked example: an invented ladder

This table is **hypothetical**: the default probabilities, recovery and spreads are invented to show the arithmetic. They are not the rates of any agency or any issuer, and no rating scale is being quoted. A fixed recovery of {{ rt.grid[0].recovery_pct }}% is assumed in each row.

| Bucket | Assumed annual probability of default | Expected loss a year | Assumed spread | Spread left after expected loss |
|---|---:|---:|---:|---:|
{% for g in rt.grid %}| {{ g.bucket }} | {{ g.annual_default_prob_pct }}% | {{ g.expected_loss_pct }}% | {{ g.spread_pct }}% | {{ g.spread_minus_loss_pp }} points |
{% endfor %}
The table assumes spreads above expected loss, on the idea that a lender wants to be paid for risk, not just reimbursed for it. The part of the spread above expected loss is a premium for bearing uncertainty, and it isn't guaranteed: if defaults come in higher than assumed, it disappears.

Now the effect on price. Take a {{ rt.years }}-year bond paying a {{ rt.coupon_pct }}% coupon once a year, and a [government bond]({% post_url 2027-01-31-g-secs-and-t-bills %}) yield of {{ rt.base_yield_pct }}%. A borrower priced {{ rt.issuer_spread_pp }} points above it yields {{ rt.issuer_yield_pct }}%:

| | Yield | Price of a ₹1,000 bond (₹) |
|---|---:|---:|
| Priced off the government yield | {{ rt.base_yield_pct }}% | {{ rt.price_at_base }} |
| Priced with the {{ rt.issuer_spread_pp }}-point spread | {{ rt.issuer_yield_pct }}% | {{ rt.price_at_issuer }} |

A {{ rt.issuer_spread_pp }}-point spread is a ₹{{ rt.price_gap }} lower price for the same coupons, {{ rt.price_gap_pct }}% below the first. If the market later decides the borrower is riskier, the spread widens beyond {{ rt.issuer_spread_pp }} points and the price falls below ₹{{ rt.price_at_issuer }}, even if no default happens.

## What a rating doesn't tell you

- **It is an opinion at a point in time.** Ratings are reviewed and can be changed up or down.
- **It says nothing about price risk.** A top-rated long bond can lose value when yields rise ([modified duration]({% post_url 2026-10-06-modified-duration %})). The rating covers repayment, not market price.
- **It isn't a guarantee.** A high rating is a view on a low probability, not a zero one. The [riskometer post]({% post_url 2026-10-22-the-riskometer %}) shows how a fund-level measure uses credit quality as one input.

## Common mistakes

- **Reading the highest rating as "no risk".** It is the lowest credit risk on that agency's scale, still not nil, and it carries interest-rate risk.
- **Chasing the extra yield without asking what it pays for.** A higher yield usually pays for some risk (credit, liquidity or maturity), so ask which.
- **Treating a fund's average rating as the rating of each holding.** An average hides the spread between its best and worst bonds.
- **Ignoring liquidity.** A lower-rated bond can be hard to sell exactly when you want to ([liquidity risk]({% post_url 2026-10-17-liquidity-risk %})).

**Takeaway:** A credit rating is an agency's opinion on whether a specific debt will be repaid on time, and the extra yield on weaker-rated bonds is largely payment for that risk, not a bonus. A top rating still leaves interest-rate and liquidity risk on the table.
