---
layout: post
title: "P/E: how many years of earnings you're paying for"
date: 2026-10-11 09:00:00 +0530
series: jargon
---

{% assign listing = site.data.case_study.listing %}
{% assign bi_market = site.data.real_company.market %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign db_wrong_pe = listing.ipo_price | divided_by: listing.eps_undiluted | round: 1 %}
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

This series always uses **diluted** EPS — the [last post]({% post_url 2026-10-09-eps %}) showed exactly why
that matters.

## Worked example: Desi Bites Foods Ltd

| | |
|---|---:|
| IPO Price | ₹{% include inr.html n=listing.ipo_price %} |
| ÷ Diluted EPS | ₹{% include inr.html n=listing.eps_diluted %} |
| **P/E** | **{{ db_pe }}x** |

Worth seeing the mistake explicitly: had we used *undiluted* EPS (₹{% include inr.html n=listing.eps_undiluted %})
instead, P/E would come out to {{ db_wrong_pe }}x — a materially different, and
wrong, number for a stock that just diluted its share count via a fresh
issue.

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
its FY25 earnings. That's a rich multiple — but not an irrational one for a
company that, across this whole series, has shown [ROE above 50%]({% post_url 2026-09-01-roe %}),
[negative net debt]({% post_url 2026-09-29-net-debt-ebitda %}), and [a negative cash conversion cycle]({% post_url 2026-09-13-cash-conversion-cycle %}). A high
P/E is what a market paying up for genuine, demonstrated quality looks
like — whether {{ bi_pe }}x specifically is a *good price* to pay for that quality is
a separate question this series deliberately doesn't answer.

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
  checking [OCF/PAT]({% post_url 2026-10-03-ocf-pat %}) before trusting a P/E at face value.

**Takeaway:** P/E measures how many years of current earnings the market is
charging for a share — useful as a starting comparison, but it only means
something once it's read alongside the quality and growth of the earnings
underneath it, not as a number that's simply "high" or "low" in isolation.
