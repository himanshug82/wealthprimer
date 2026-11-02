---
layout: post
title: "Depreciation and amortisation (D&A): the cost you don't write a cheque for"
seo_title: "Depreciation and amortisation (D&A) explained"
description: "Depreciation spreads an asset's cost over its life; amortisation does it for intangibles. Straight-line vs written-down value, and D&A below EBITDA."
image: /assets/og/depreciation-and-amortisation.png
date: 2027-02-14 09:00:00 +0530
series: jargon
term: "Depreciation and amortisation (D&A)"
---

{% assign dp = site.data.jargon_m9.depreciation %}
{% assign db = dp.db %}

## What are depreciation and amortisation?

When a company buys a machine, it pays the whole price on day one, but the machine earns revenue for years. Accounting spreads the cost over those years so each year's profit carries its share of the machine. **Depreciation** is that yearly share for physical assets (machines, buildings, vehicles). **Amortisation** is the same idea for intangible assets (software, licences, acquired brands). Together they are written **D&A**.

D&A is a real accounting cost but not a cash payment in the year it is charged: the cash left the business when the asset was bought, which you see as [capex (capital expenditure)]({% post_url 2026-09-21-capex-intensity %}) in the [cash flow statement]({% post_url 2026-08-24-reading-a-cash-flow-statement %}). That is why [EBITDA (earnings before interest, tax, depreciation and amortisation)]({% post_url 2026-08-28-ebitda-margin %}) adds it back. This post is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

Two common methods:

```
Straight-line method (SLM):  yearly charge = (cost − salvage value) / useful life
Written-down value (WDV):  yearly charge = opening book value × rate
```

**Book value** is cost minus the depreciation charged so far. SLM charges the same amount each year. WDV charges a fixed percentage of what is left, so the charge is highest early and shrinks. The method and the life are choices the company makes within accounting standards and company law, and they are disclosed in the notes to the accounts.

## Worked example: a ₹{{ dp.cost | round }} lakh machine

All figures in ₹ lakh, a hypothetical machine with no salvage value, a {{ dp.life }}-year life under SLM, and a {{ dp.wdv_rate_pct | round }}% WDV rate:

| Year | SLM charge | SLM book value at year end | WDV charge | WDV book value at year end |
|---:|---:|---:|---:|---:|
{% for s in dp.schedule %}| {{ s.year }} | {{ s.slm_dep }} | {{ s.slm_book_end }} | {{ s.wdv_dep }} | {{ s.wdv_book_end }} |
{% endfor %}
After five years SLM has charged ₹{{ dp.five_year_slm_total }} lakh in total, WDV ₹{{ dp.five_year_wdv_total }} lakh. By year {{ dp.life }}, SLM has charged the full ₹{{ dp.ten_year_slm_total }} lakh, while WDV has charged ₹{{ dp.ten_year_wdv_total }} lakh and still has ₹{{ dp.ten_year_wdv_left }} lakh on the books, because a fixed percentage of what's left never reaches zero. That remainder is settled when the asset is sold or scrapped, as a gain or loss. So the bigger difference is *when* the profit takes the hit: WDV loads it into the early years.

An intangible works the same way. Software bought for ₹{{ dp.intangible.cost }} lakh and amortised straight-line over {{ dp.intangible.life }} years is a charge of ₹{{ dp.intangible.per_year }} lakh a year.

## Where D&A sits in a set of accounts

Desi Bites Foods (fictional), {{ db.fy }} (financial year), ₹ lakh:

| | ₹ lakh |
|---|---:|
| EBITDA | {{ db.ebitda }} |
| − Depreciation | {{ db.depreciation }} |
| **= EBIT** (earnings before interest and tax) | **{{ db.ebit }}** |
| − Interest | {{ db.interest }} |
| **= PBT** (profit before tax) | {{ db.pbt }} |
| − Tax | {{ db.tax }} |
| **= PAT** (profit after tax) | **{{ db.pat }}** |

Depreciation took {{ db.dep_share_of_ebitda_pct }}% of Desi Bites' EBITDA, and equalled {{ db.dep_pct_of_opening_nfa }}% of the previous year's net fixed assets. That is a reminder that EBITDA is flattering for a business that has to keep replacing machines: the cash for replacement shows up as capex, not as D&A ([capex intensity]({% post_url 2026-09-21-capex-intensity %})).

## Common mistakes

- **Treating D&A as free because it isn't cash.** The cash was spent earlier and will be spent again when the asset is replaced.
- **Comparing EBITDA across firms without checking capital intensity.** A firm with heavy machinery has large D&A; the same EBITDA means less profit for it.
- **Assuming the depreciation rate equals the asset's real wear.** It follows an accounting policy. An asset can be fully written down and still work, or lose value faster than charged.
- **Mixing up book value and market value.** Book value after depreciation is an accounting number, not what the asset would sell for.

**Takeaway:** Depreciation and amortisation spread the cost of assets over their lives, so profit carries the cost gradually even though the cash left on day one. That is why EBITDA adds it back, and why, for asset-heavy businesses, it pays to look below EBITDA.
