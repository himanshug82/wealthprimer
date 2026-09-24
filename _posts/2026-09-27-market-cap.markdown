---
layout: post
title: "Market Cap: what the market values the whole company at"
description: "Price times shares outstanding: the number behind every large-cap, mid-cap and small-cap label, and why it is not what buying the company would cost."
image: /assets/og/market-cap.png
date: 2026-09-27 09:00:00 +0530
series: jargon
term: "Market cap (market capitalisation)"
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign db_market_cap_cr = listing.market_cap | divided_by: 100.0 %}
{% assign cap_ratio = bi_market.market_cap_cr | divided_by: db_market_cap_cr | divided_by: 10 | round: 0 | times: 10 %}
{% assign bi_mc_lakh_cr = bi_market.market_cap_cr | divided_by: 100000.0 | round: 1 %}

## What market cap means

**Market capitalisation ("market cap")** is the number behind every
"large-cap," "mid-cap," and "small-cap" label you'll see attached to a
stock: the total value the market places on all of a company's shares put
together.

In India those labels have an official, rank-based meaning. SEBI (the
Securities and Exchange Board of India, the markets regulator) set them in its
[categorisation circular of 6 October 2017](https://www.sebi.gov.in/legal/circulars/oct-2017/categorization-and-rationalization-of-mutual-fund-schemes_36199.html)
(SEBI/HO/IMD/DF3/CIR/P/2017/114), which ranks listed companies by full market cap:

| Bucket | Rank by full market cap |
|---|---|
| Large cap | 1st to 100th |
| Mid cap | 101st to 250th |
| Small cap | 251st onwards |

It's a ranking, not a rupee cut-off. AMFI (the Association of Mutual Funds
in India) publishes the ranked list every six months on its
[stock categorisation page](https://www.amfiindia.com/otherdata/categorisation-of-stocks),
based on average market cap over the previous six months, and mutual funds
use it to decide what counts as "large-cap" in their portfolios.

## The formula

```
Market Cap = Price per Share × Shares Outstanding
```

## Worked example: Desi Bites Foods Ltd

| | |
|---|---:|
| IPO Price | ₹{% include inr.html n=listing.ipo_price %} |
| × Shares Outstanding (Lakh) | {{ listing.post_ipo_shares_lakh }} |
| **Market Cap** | **₹{% include inr.html n=listing.market_cap %} Lakh (₹{% include inr.html n=db_market_cap_cr %} Crore)** |

At ₹{% include inr.html n=db_market_cap_cr %} crore, Desi Bites Foods Ltd is a genuinely tiny listing. Ranked
against thousands of listed companies, it would land far down the small-cap
bucket — often informally called "micro-cap" at this size (that word has no
official SEBI definition).

## Worked example: Britannia Industries

Price is the {{ bi_market.price_date }} NSE closing price used throughout this module.
For illustration only.

| | |
|---|---:|
| Price ({{ bi_market.price_date }}) | ₹{% include inr.html n=bi_market.price %} |
| × Shares Outstanding (Crore) | {{ bi_market.shares_outstanding_cr }} |
| **Market Cap** | **₹{% assign _mc = bi_market.market_cap_cr | round: 0 %}{% include inr.html n=_mc %} Crore** |

At roughly ₹{{ bi_mc_lakh_cr }} lakh crore, Britannia is about {% include inr.html n=cap_ratio %} times Desi Bites'
market cap. Its official bucket isn't set by that rupee figure, though —
it comes from where it ranks on AMFI's half-yearly list for the period in
question. The gap between the two
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
- **Mixing up full and free-float market cap.** Index providers such as NSE
  weight stocks by free-float market cap, which leaves out shares that
  rarely trade (like promoter holdings). SEBI's size buckets use full market
  cap, so the two can differ a lot for a closely held company.

**Takeaway:** market cap is simply price times shares outstanding — the
market's running verdict on what a company's equity is worth. It's useful
for gauging size, but silent on debt, cash, or whether that price makes
sense.
