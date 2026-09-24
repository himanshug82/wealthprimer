---
layout: post
title: "Capex Intensity: how capital-hungry the business actually is"
description: "What share of revenue a company must plough back into plant and equipment just to keep going, and how capital-hungry business models show up in the numbers."
image: /assets/og/capex-intensity.png
date: 2026-09-21 09:00:00 +0530
series: jargon
term: "Capex intensity"
---

{% assign db_cf25 = site.data.case_study.cash_flow.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_cf25 = site.data.real_company.cash_flow.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign bi_cf24 = site.data.real_company.cash_flow.FY24 %}
{% assign bi_is24 = site.data.real_company.income_statement.FY24 %}

## What capex intensity means

The last post noted that Britannia's [free cash flow]({% post_url 2026-09-19-free-cash-flow %}) rose year on year
partly because capex fell. **Capex intensity** turns that observation into
its own ratio: what share of revenue does a company have to plough back
into fixed assets — plant, equipment, capacity — just to sustain or grow
the business?

It's a read on how capital-hungry a business model is. A telecom or steel
company needs to keep spending heavily relative to revenue just to stand
still; a strong consumer brand with existing capacity can often grow
revenue with comparatively little additional capex.

## The formula

```
Capex Intensity (%) = Capex / Revenue × 100
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Capex | {{ db_cf25.cfi | abs }} |
| Revenue | {{ db_is25.revenue }} |
| **Capex Intensity** | **{{ site.data.case_study.ratios.FY25.capex_intensity }}%** |

Desi Bites' capex intensity was {{ site.data.case_study.ratios.FY23.capex_intensity }}% in FY23, peaked at
{{ site.data.case_study.ratios.FY24.capex_intensity }}% in FY24, then dropped to {{ site.data.case_study.ratios.FY25.capex_intensity }}% in FY25 — consistent with a company that
front-loaded plant capacity in its earlier years and is now growing revenue
without needing to spend as heavily to support it.

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Capex | {{ bi_cf25.capex }} |
| Revenue | {{ bi_is25.revenue }} |
| **Capex Intensity** | **{{ site.data.real_company.ratios.FY25.capex_intensity }}%** |

That's down from {{ bi_cf24.capex | times: 100.0 | divided_by: bi_is24.revenue | round: 1 }}% in FY24 — a real, meaningful drop, and now we
have the full explanation for last post's finding: Britannia's FCF rose
year on year mainly because it spent less on capex, not because its
underlying operating cash generation improved. Whether that's a genuinely
efficient business needing less reinvestment, or a company simply pausing
between expansion cycles, is exactly the kind of question worth watching
over the next couple of years rather than settling from one data point.

## Common mistakes

- **Comparing capex intensity across industries.** A capital-heavy business
  (telecom, cement, steel) will structurally run a much higher capex
  intensity than an asset-light one (FMCG, services) — this ratio is most
  meaningful within an industry or against a company's own history.
- **Assuming low capex intensity is always a sign of efficiency.** It can
  also mean underinvestment — an ageing plant, a capacity ceiling coming up,
  or delayed maintenance that eventually becomes an urgent, larger expense.
- **Not separating maintenance capex from growth capex.** The same rupee
  amount means something very different depending on whether it's replacing
  worn-out equipment (needed just to stand still) or building new capacity
  (funding future growth) — a distinction the raw capex figure alone
  doesn't make, as flagged already in the [cash flow statement post]({% post_url 2026-08-24-reading-a-cash-flow-statement %}).
- **Reading one year's dip or spike as a trend.** Capex is naturally lumpy —
  a single large plant project can distort one or two years' numbers
  without signalling anything permanent about the business.

**Takeaway:** capex intensity is how much of each rupee of revenue gets
ploughed back into plant. A falling number can mean efficiency — or just a
pause between investment cycles.
