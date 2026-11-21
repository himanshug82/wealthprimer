---
layout: post
title: "Price-to-sales: valuing revenue, and when that misleads"
seo_title: "Price-to-sales ratio (P/S): formula, meaning and example"
description: "The price-to-sales ratio compares a company's market value with its revenue. The formula, its link to P/E and margins, and why one P/S can mean two prices."
image: /assets/og/price-to-sales.png
date: 2027-04-28 09:00:00 +0530
series: jargon
term: "Price-to-sales ratio (P/S)"
---

{% assign p = site.data.jargon_m10.ps %}
{% assign a = p.years.FY25 %}
{% assign b = p.years.FY26 %}
{% assign ga = p.generic[0] %}
{% assign gb = p.generic[1] %}

## What price-to-sales means

The **price-to-sales ratio (P/S)** is a company's market capitalisation
divided by its revenue for a year. It says how many rupees the market is
paying for each rupee of annual sales. Because revenue is positive for almost
any operating company, P/S can be worked out where the
[P/E ratio]({% post_url 2026-09-24-price-to-earnings %}) (price-to-earnings)
can't, such as a company making a loss.

That's also its weakness. Revenue isn't profit, and a rupee of sales is worth
very different amounts in a high-margin business and a low-margin one. This
post shows the arithmetic that links the two. It's part of
[Jargon, Decoded]({{ '/series/jargon/' | relative_url }}).

## The formula

```
P/S  =  market capitalisation ÷ revenue          (or price per share ÷ revenue per share)

P/S  =  P/E × net margin                          (net margin = profit after tax ÷ revenue)

EV/sales  =  enterprise value ÷ revenue           (EV = market cap + debt − cash)
```

The second line is an identity: market cap ÷ revenue = (market cap ÷ profit)
× (profit ÷ revenue). It's why P/S and P/E can't be read separately from the
[net margin]({% post_url 2026-08-30-net-margin %}). EV/sales, using
[enterprise value]({% post_url 2026-10-13-enterprise-value %}), takes debt
and cash into account.

## Worked example: Desi Bites at its IPO price

[Desi Bites Foods]({{ '/case-study/' | relative_url }}) is fictional. At its
IPO (initial public offering) price of ₹{{ p.price }} on {{ p.shares_lakh }}
lakh shares, its market capitalisation is ₹{% include inr.html n=p.mcap %} lakh.

| ₹ lakh | FY25 revenue | FY26 revenue |
|---|---:|---:|
| Revenue | {{ a.revenue }} | {{ b.revenue }} |
| P/S at ₹{{ p.price }} | {{ a.ps }} | {{ b.ps }} |
| Net margin | {{ a.net_margin_pct }}% | {{ b.net_margin_pct }}% |
| P/E at ₹{{ p.price }} | {{ a.pe }} | {{ b.pe }} |

Check the identity on FY26 with unrounded inputs:
{{ b.pe_exact }} × {{ b.margin_exact_pct }}% ≈ {{ b.ps }}. On enterprise value,
using the 31 March 2026 term loan (₹{{ b.debt }} lakh) and cash
(₹{% include inr.html n=b.cash %} lakh) against the IPO-price market cap, EV
is ₹{% include inr.html n=b.ev %} lakh and EV/sales {{ b.ev_sales }}. The
[enterprise value post]({% post_url 2026-10-13-enterprise-value %}) used
₹{% include inr.html n=b.listing_ev %} lakh, the figure at listing, with the
cash and debt of that date.

**Why one P/S can mean two different prices.** Two made-up companies, both at
a P/S of {{ ga.ps }}:

| | P/S | Net margin | Implied P/E |
|---|---:|---:|---:|
| {{ ga.name }} | {{ ga.ps }} | {{ ga.margin_pct }}% | {{ ga.pe }} |
| {{ gb.name }} | {{ gb.ps }} | {{ gb.margin_pct }}% | {{ gb.pe }} |

Same price per rupee of sales; very different prices per rupee of profit.
Comparing them on P/S alone hides the difference.

## Common mistakes

1. **Comparing P/S across industries.** A retailer and a software company
   keep very different shares of each rupee of sales, so their P/S ratios
   aren't comparable. Compare within an industry, or adjust for margin.
2. **Ignoring debt.** P/S uses market cap, which ignores borrowings. Two
   companies with the same P/S but different debt aren't priced the same for
   the whole business; EV/sales fixes that.
3. **Mixing periods.** Market cap is today's; revenue is a past year's. Say
   which year's revenue, and don't compare one company's trailing P/S with
   another's forward one.

**Takeaway:** Price-to-sales divides market value by revenue, and P/S equals
P/E times net margin. It can be calculated where profits are negative, but a low P/S in
a thin-margin business can still be a high price for its profits.
