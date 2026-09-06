---
layout: post
title: "Market Cap: what the market values the whole company at"
description: "Price times shares outstanding: the number behind every large-cap, mid-cap and small-cap label, and why it is not what buying the company would cost."
image: /assets/og/market-cap.png
date: 2026-09-27 09:00:00 +0530
series: jargon
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign db_market_cap_cr = listing.market_cap | divided_by: 100.0 %}
{% assign cap_ratio = bi_market.market_cap_cr | divided_by: db_market_cap_cr | round: 0 %}

## What market cap means

**Market Capitalisation ("market cap")** is the number behind every
"large-cap," "mid-cap," and "small-cap" label you'll see attached to a
stock: the total value the market places on all of a company's shares put
together.

## The formula

```
Market Cap = Price per Share × Shares Outstanding
```

## Worked example: Desi Bites Foods Ltd

| | |
|---|---:|
| IPO Price | ₹{% include inr.html n=listing.ipo_price %} |
| × Shares Outstanding (Lakh) | {{ listing.post_ipo_shares_lakh }} |
| **Market Cap** | **₹{% include inr.html n=listing.market_cap %} Lakh (₹80 Crore)** |

At ₹80 crore, Desi Bites Foods Ltd is a genuinely tiny listing —
small/micro-cap territory, exactly what you'd expect for a company that
just listed on an SME platform.

## Worked example: Britannia Industries

Price is the {{ bi_market.price_date }} NSE closing price used throughout this module.
For illustration only.

| | |
|---|---:|
| Price ({{ bi_market.price_date }}) | ₹{% include inr.html n=bi_market.price %} |
| × Shares Outstanding (Crore) | {{ bi_market.shares_outstanding_cr }} |
| **Market Cap** | **₹{% assign _mc = bi_market.market_cap_cr | round: 0 %}{% include inr.html n=_mc %} Crore** |

At roughly ₹1.4 lakh crore, Britannia sits firmly in large-cap territory —
about {{ cap_ratio }} times Desi Bites' market cap. The gap between the two
companies' *size* (revenue, assets, market cap) is enormous, even where —
as several earlier posts showed — some of their underlying ratios landed
surprisingly close together.

## Common mistakes

- **Confusing market cap with enterprise value.** Market cap only prices the
  equity — it ignores debt and cash entirely, which is exactly why [EV]({% post_url 2026-09-26-ev-ebitda %})
  exists as a separate, fuller measure of what it would cost to buy the
  whole business.
- **Confusing market cap with revenue or total assets.** These are
  completely different things measured on different statements — market
  cap is purely the market's opinion of what the equity is worth, not a
  figure that appears anywhere on the company's own financials.
- **Assuming a bigger market cap always means a safer investment.** Size
  and safety aren't the same thing — a large-cap company can still carry
  real risk, and a small-cap can be genuinely well-run.
- **Treating market cap as fixed.** It moves every single trading day as
  the share price moves, without anything about the underlying business
  necessarily changing — it's a live market opinion, not a stable
  characteristic of the company.

**Takeaway:** market cap is simply price times shares outstanding — the
market's running verdict on what a company's equity is worth as a whole,
useful for gauging size but silent on debt, cash, or whether that price is
actually a good one to pay.
