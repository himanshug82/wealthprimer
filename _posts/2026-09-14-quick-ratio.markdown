---
layout: post
title: "Quick Ratio: coverage without counting on inventory"
description: "The acid test: coverage once inventory is stripped out entirely. Why the quick ratio is the stricter cousin of the current ratio, and when the gap matters."
image: /assets/og/quick-ratio.png
date: 2026-09-14 09:00:00 +0530
series: jargon
term: "Quick ratio"
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign db_ca = db_bs25.inventory | plus: db_bs25.receivables | plus: db_bs25.cash %}
{% assign db_cl = db_bs25.payables | plus: db_bs25.other_current_liabilities %}
{% assign db_quick_assets = db_ca | minus: db_bs25.inventory %}
{% assign bi_quick_assets = bi_bs25.total_current_assets | minus: bi_bs25.inventory %}

## What the quick ratio means

The [current ratio]({% post_url 2026-09-13-current-ratio %}) treats every current asset as equally able to cover a
bill — but inventory is the least liquid one. It has to actually be sold,
and sold at the expected price, before it turns into cash. The **quick
ratio** (also called the acid-test ratio) strips inventory out entirely, leaving
only the current assets a company could realistically convert to cash
quickly: cash itself, receivables, and short-term investments. In practice,
this series computes it as current assets minus inventory only, so smaller
items such as prepaid expenses stay in; some sources strip those out too.

## The formula

```
Quick Ratio = (Current Assets − Inventory) / Current Liabilities
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Current Assets − Inventory | {{ db_quick_assets }} |
| Current Liabilities | {{ db_cl }} |
| **Quick Ratio** | **{{ site.data.case_study.ratios.FY25.quick_ratio }}** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Current Assets − Inventory | {{ bi_quick_assets }} |
| Current Liabilities | {{ bi_bs25.total_current_liabilities }} |
| **Quick Ratio** | **{{ site.data.real_company.ratios.FY25.quick_ratio }}** |

Strip out inventory, and Britannia's coverage looks tighter still —
{{ site.data.real_company.ratios.FY25.quick_ratio }}, below 1. On paper, that's the kind of number that would
normally deserve real scrutiny at most companies. For Britannia specifically,
it's a case where the number needs company: paired with its [cash conversion cycle]({% post_url 2026-09-10-cash-conversion-cycle %})
of −{{ site.data.real_company.ratios.FY25.ccc | abs }} days (it collects from customers in about
{{ site.data.real_company.ratios.FY25.receivable_days }} days but pays suppliers in about {{ site.data.real_company.ratios.FY25.payable_days }}), a sub-1 quick
ratio isn't the same warning sign it would be at a company that actually
waits on customers to pay before it can pay its own bills. That said — this
is genuinely the exception, not the rule. For most companies, a quick ratio
comfortably under 1 is worth investigating, not explaining away.

## Common mistakes

- **Treating a sub-1 quick ratio as automatically a problem, or automatically
  fine.** Neither extreme is right. It's a real signal that deserves a look
  at *why* — and Britannia's negative CCC is a legitimate why, but it's not
  the default explanation for every company that shows up this way.
- **Using inconsistent definitions of "quick" assets.** Because some
  versions also strip out prepaid expenses (see above), check which version
  a given source is using before comparing numbers across sites.
- **Comparing quick ratios across industries with very different inventory
  intensity.** A software company (almost no inventory) will show a quick
  ratio close to its current ratio by default — the gap between the two
  ratios matters more than either number alone.
- **Ignoring the trend.** A quick ratio steadily declining over several
  years, even if still technically above 1, is worth more attention than a
  single low reading at an otherwise fast-cycling business.

**Takeaway:** the quick ratio is the stricter cousin of the current ratio,
showing coverage without leaning on inventory. A low number is usually worth
investigating — but, as Britannia shows, read it alongside the company's cash
conversion cycle before jumping to a conclusion.
