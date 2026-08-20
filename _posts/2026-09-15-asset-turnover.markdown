---
layout: post
title: "Asset Turnover: how much revenue a company squeezes out of what it owns"
date: 2026-09-15 09:00:00 +0530
series: jargon
---

{% assign db_bs24 = site.data.case_study.balance_sheet.FY24 %}
{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs24 = site.data.real_company.balance_sheet.FY24 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What asset turnover means

We closed the Profitability module with [ROA]({% post_url 2026-09-05-roa %}), which asks how much
*profit* a company earns on everything it owns. **Asset Turnover** asks a
related but different question, using the same total-assets denominator:
how much *revenue* does a company generate per rupee of assets?

It's a pure efficiency measure — it says nothing about margins at all. A
company can post a strong asset turnover while barely making any profit per
sale, or a modest asset turnover while keeping a huge chunk of every rupee
sold. Put together with the margins from the Profitability module, it starts
to explain *how* a company arrives at its ROA — two very different paths can
lead to the same destination.

## The formula

```
Asset Turnover = Revenue / Average Total Assets
```

Expressed as a multiple (times), not a percentage — "2.0x" means the
company generates ₹2 of revenue for every ₹1 of assets it holds, on
average, over the year.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Revenue (FY25) | {{ db_is25.revenue }} |
| Total assets, start of year (FY24) | {{ db_bs24.total_assets }} |
| Total assets, end of year (FY25) | {{ db_bs25.total_assets }} |
| Average total assets | {{ db_bs24.total_assets | plus: db_bs25.total_assets | divided_by: 2.0 }} |
| **Asset Turnover** | **{{ site.data.case_study.ratios.FY25.asset_turnover }}x** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Revenue (FY25) | {{ bi_is25.revenue }} |
| Total assets, start of year (FY24) | {{ bi_bs24.total_assets }} |
| Total assets, end of year (FY25) | {{ bi_bs25.total_assets }} |
| Average total assets | {{ bi_bs24.total_assets | plus: bi_bs25.total_assets | divided_by: 2.0 }} |
| **Asset Turnover** | **{{ site.data.real_company.ratios.FY25.asset_turnover }}x** |

Here's the interesting part: Desi Bites ({{ site.data.case_study.ratios.FY25.asset_turnover }}x) and Britannia
({{ site.data.real_company.ratios.FY25.asset_turnover }}x) turn over their assets at almost the *same* rate — despite Britannia's
[net margin]({% post_url 2026-08-30-net-margin %}) being roughly half again as high as Desi Bites'. Two
businesses can reach a similar ROA through very different combinations of
margin and turnover — a thin-margin, high-turnover retailer and a
high-margin, low-turnover luxury brand can land on the same ROA for
completely different reasons. That margin-times-turnover relationship has a
name — the DuPont decomposition — which we'll come back to once the
remaining pieces are in place.

## Common mistakes

- **Comparing asset turnover across industries with very different asset
  intensity.** A capital-heavy manufacturer or utility will naturally show a
  lower asset turnover than an asset-light retailer or services business,
  regardless of how well either is run.
- **Assuming higher asset turnover always means a better business.** A
  company can also post a high asset turnover because it's under-invested in
  its asset base (old, fully depreciated equipment still in use) — not
  because it's genuinely more efficient.
- **Reading asset turnover in isolation from margin.** A low asset turnover
  isn't automatically a problem if it's paired with a high margin (and vice
  versa) — the two need to be read together, not separately, to judge a
  business.
- **Using closing assets instead of average.** As with ROE, ROCE, and ROA, a
  large mid-year addition to the asset base (a new plant, an acquisition)
  will distort a closing-only calculation.

**Takeaway:** asset turnover measures how much revenue a company generates
per rupee of assets — a pure efficiency number that says nothing about
margin on its own, but combined with margin, starts to explain *how* a
company earns its return, not just how much.
