---
layout: post
title: "P/E: how many years of earnings you're paying for"
description: "How many years of current earnings the market is charging for. The P/E formula, why high is not automatically expensive, and the earnings quality behind the E."
image: /assets/og/price-to-earnings.png
date: 2026-09-24 09:00:00 +0530
series: jargon
term: "P/E (price-to-earnings)"
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign db_pre_pe = listing.ipo_price | divided_by: listing.eps_undiluted | round: 1 %}
{% assign db_pe = listing.ipo_price | divided_by: listing.eps_diluted | round: 1 %}
{% assign bi_pe = bi_market.price | divided_by: bi_is25.eps | round: 1 %}

## What P/E means

**P/E — Price-to-Earnings** — is the most quoted valuation ratio there is:
how many rupees is the market charging for every rupee of a company's
annual earnings? Framed differently, it's roughly how many years of current
profit an investor is paying for at today's price.

## The formula

```
P/E = Price per Share / EPS
```

For a company that has just issued fresh shares, this series uses
**post-issue** EPS — profit divided by the share count after the issue. The
[last post]({% post_url 2026-09-23-eps %}) showed exactly why that matters.

## Worked example: Desi Bites Foods Ltd

| | |
|---|---:|
| IPO Price | ₹{% include inr.html n=listing.ipo_price %} |
| ÷ Post-issue EPS | ₹{% include inr.html n=listing.eps_diluted %} |
| **P/E** | **{{ db_pe }}x** |

Worth seeing the gap explicitly: on *pre-issue* EPS (₹{% include inr.html n=listing.eps_undiluted %}),
P/E would come out to {{ db_pre_pe }}x. That's not an error as such — Indian IPO
offer documents often quote P/E on pre-issue EPS — but it's a materially
lower number. The post-issue P/E better reflects what a listing-day buyer
is actually paying, because the fresh shares are real and share the same
profit from day one.

## Worked example: Britannia Industries

Price is Britannia's NSE closing price on {{ bi_market.price_date }} (source: Yahoo Finance
historical data), paired with the FY25 EPS from the [audited consolidated
results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
— i.e. roughly what the market was paying for Britannia's FY25 earnings
shortly after those results were digested. For illustration only, not a
signal to act on.

| | |
|---|---:|
| Price ({{ bi_market.price_date }}) | ₹{% include inr.html n=bi_market.price %} |
| ÷ EPS | ₹{% include inr.html n=bi_is25.eps %} |
| **P/E** | **{{ bi_pe }}x** |

A P/E of {{ bi_pe }}x means the market was pricing Britannia at roughly {{ bi_pe }} years of
its FY25 earnings. Across this series, the same company has shown [ROE above 50%]({% post_url 2026-09-01-roe %}),
[negative net debt]({% post_url 2026-09-18-net-debt-ebitda %}), and [a negative cash conversion cycle]({% post_url 2026-09-10-cash-conversion-cycle %}). Mechanically,
a high multiple means the market is paying for expected quality or growth —
whether {{ bi_pe }}x is justified isn't assessed here, and this series
deliberately doesn't answer that question.

## Common mistakes

- **Treating high P/E as automatically overvalued, or low P/E as
  automatically cheap.** Both readings skip the actual question: is the
  multiple justified by the quality and durability of the earnings behind
  it? A "cheap" P/E on a deteriorating business can be far riskier than an
  "expensive" one on a genuinely strong one.
- **Mixing trailing and forward EPS without checking which is being used.**
  This series always uses trailing (historical, already-reported) EPS —
  some sources quote forward (analyst-estimated) EPS instead, which
  produces a different P/E for the same price.
- **Comparing P/E across industries or growth profiles without context.** A
  slow-growing utility and a fast-growing FMCG brand can both have
  "reasonable" P/Es that mean completely different things.
- **Ignoring earnings quality behind the E.** A great P/E on paper means
  little if the earnings themselves aren't backed by real cash — worth
  checking [OCF/PAT]({% post_url 2026-09-20-ocf-pat %}) before trusting a P/E at face value.

**Takeaway:** P/E measures how many years of current earnings the market is
charging for a share — useful as a starting comparison, but it only means
something once it's read alongside the quality and growth of the earnings
underneath it, not as a number that's simply "high" or "low" in isolation.
