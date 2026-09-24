---
layout: post
title: "Dividend Yield: how much cash you're paid back, relative to what you paid"
description: "The cash a share pays back each year as a percentage of its price. How dividend yield is computed, and why an unusually high yield is often a falling price."
image: /assets/og/dividend-yield.png
date: 2026-09-28 09:00:00 +0530
series: jargon
term: "Dividend yield"
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign db_yield = listing.dividend_per_share_fy25 | times: 100.0 | divided_by: listing.ipo_price | round: 2 %}
{% assign db_div25 = site.data.case_study.income_statement.FY25.dividend %}
{% assign db_dps_post = db_div25 | times: 1.0 | divided_by: listing.post_ipo_shares_lakh | round: 2 %}
{% assign db_yield_post = db_dps_post | times: 100.0 | divided_by: listing.ipo_price | round: 2 %}
{% assign bi_yield = bi_market.dividend_per_share_fy25 | times: 100.0 | divided_by: bi_market.price | round: 2 %}

## What dividend yield means

Not every rupee of profit gets reinvested — some companies pay part of it
straight back to shareholders as a **dividend**. **Dividend yield**
expresses that payout relative to the price paid for the stock: how much
cash income does a share generate each year, as a percentage of what it
cost?

## The formula

```
Dividend Yield (%) = Dividend per Share / Price × 100
```

## Worked example: Desi Bites Foods Ltd

Desi Bites' FY25 dividend (₹84 Lakh) was paid before the IPO, to the
{{ listing.pre_ipo_shares_lakh }} lakh pre-IPO shares that existed at the time.

| | |
|---|---:|
| Dividend per share (FY25, pre-issue shares) | ₹{% include inr.html n=listing.dividend_per_share_fy25 %} |
| ÷ IPO price | ₹{% include inr.html n=listing.ipo_price %} |
| **Dividend yield** | **{{ db_yield }}%** |

One catch, the same one the [EPS post]({% post_url 2026-09-23-eps %}) flagged: that
₹{% include inr.html n=listing.dividend_per_share_fy25 %} is per *pre-issue* share. Someone buying at the IPO wasn't paid it, and
there are now {{ listing.post_ipo_shares_lakh }} lakh shares, not {{ listing.pre_ipo_shares_lakh }}. If Desi Bites paid the same ₹{{ db_div25 }} lakh
across the post-issue share count, that's ₹{{ db_dps_post }} a share — a yield of
{{ db_yield_post }}% at the IPO price. That post-issue figure is the fairer one for a new
investor; the pre-issue one mixes an old share count with a new price.

## Worked example: Britannia Industries

Dividend per share is the trailing 12-month figure: the single dividend
Britannia paid during FY25 (ex-date 5 August 2024). That payment was the
final dividend for FY24, paid in August 2024 — there was no interim
dividend during FY25. Sourced from [stockanalysis.com's dividend
history](https://stockanalysis.com/quote/nse/BRITANNIA/dividend/). Price is
the {{ bi_market.price_date }} NSE close used throughout this module. For illustration
only.

| | |
|---|---:|
| Dividend per share (trailing 12 months, paid Aug 2024) | ₹{% include inr.html n=bi_market.dividend_per_share_fy25 %} |
| ÷ Price ({{ bi_market.price_date }}) | ₹{% include inr.html n=bi_market.price %} |
| **Dividend yield** | **{{ bi_yield }}%** |

Another coincidence worth flagging rather than reading too much into: on
the pre-issue figure, both companies land close to {{ db_yield }}%. That's not a pattern this series is claiming
means anything — dividend yield depends heavily on each company's own
payout choices and where its price happens to sit, not on some underlying
law that similar businesses converge here.

## Common mistakes

- **Chasing high yield without checking sustainability.** A falling share
  price mechanically raises yield even if the dividend itself is at real
  risk of being cut — a very high yield is sometimes a warning sign
  dressed up as an opportunity, not always a genuine one.
- **Assuming a low or zero yield is a red flag.** A younger, growing
  company choosing to reinvest profit instead of paying it out isn't doing
  anything wrong — it's often the more value-accretive choice at that stage,
  not evidence of weakness.
- **Ignoring the payout ratio.** A company paying out more in dividends than
  it earns in profit is spending down its own reserves, which isn't
  sustainable — dividend yield alone doesn't reveal this, but comparing the
  dividend to PAT does.
- **Treating dividend yield as the whole return story.** It's cash income
  only — price appreciation (or decline) is a separate, often larger,
  component of total return that yield alone says nothing about.

**Takeaway:** dividend yield measures the cash income a share pays back
relative to its price — informative on its own, but only one part of total
return, and a high yield deserves a check on sustainability before it's
read as a straightforward positive.
