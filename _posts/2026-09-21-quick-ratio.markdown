---
layout: post
title: "Quick Ratio: coverage without counting on inventory"
date: 2026-09-21 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign db_ca = db_bs25.inventory | plus: db_bs25.receivables | plus: db_bs25.cash %}
{% assign db_cl = db_bs25.payables | plus: db_bs25.other_current_liabilities %}
{% assign db_quick_assets = db_ca | minus: db_bs25.inventory %}
{% assign bi_quick_assets = bi_bs25.total_current_assets | minus: bi_bs25.inventory %}

## What the quick ratio means

[Current Ratio]({% post_url 2026-09-19-current-ratio %}) treats every current asset as equally able to cover a
bill — but inventory is the least liquid one. It has to actually be sold,
and sold at the expected price, before it turns into cash. **Quick Ratio**
(also called the acid-test ratio) strips inventory out entirely, leaving
only the current assets a company could realistically convert to cash
quickly: cash itself, receivables, and short-term investments.

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
it's a case where the number needs company: paired with its 20-day-faster
collection cycle than payment cycle ([negative CCC]({% post_url 2026-09-13-cash-conversion-cycle %})), a sub-1 quick
ratio isn't the same warning sign it would be at a company that actually
waits on customers to pay before it can pay its own bills. That said — this
is genuinely the exception, not the rule. For most companies, a quick ratio
comfortably under 1 is worth investigating, not explaining away.

## Common mistakes

- **Treating a sub-1 quick ratio as automatically a problem, or automatically
  fine.** Neither extreme is right. It's a real signal that deserves a look
  at *why* — and Britannia's negative CCC is a legitimate why, but it's not
  the default explanation for every company that shows up this way.
- **Using inconsistent definitions of "quick" assets.** Some versions of
  this ratio also strip out prepaid expenses; this series keeps it simple
  (current assets minus inventory only) for consistency across posts —
  worth checking which version a given source is using before comparing
  numbers across sites.
- **Comparing quick ratios across industries with very different inventory
  intensity.** A software company (almost no inventory) will show a quick
  ratio close to its current ratio by default — the gap between the two
  ratios matters more than either number alone.
- **Ignoring the trend.** A quick ratio steadily declining over several
  years, even if still technically above 1, is worth more attention than a
  single low reading at an otherwise fast-cycling business.

**Takeaway:** quick ratio is the stricter cousin of current ratio, showing
coverage without leaning on inventory — a low number is usually worth
investigating, but as Britannia shows, it has to be read alongside the
company's actual cash conversion cycle before jumping to a conclusion.
