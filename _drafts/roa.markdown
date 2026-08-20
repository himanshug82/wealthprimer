---
layout: post
title: "ROA (Return on Assets): how hard everything the company owns is working"
series: jargon
---

{% assign db_bs24 = site.data.case_study.balance_sheet.FY24 %}
{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs24 = site.data.real_company.balance_sheet.FY24 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What ROA means

We've now looked at return on shareholders' money ([ROE]({% post_url 2026-09-01-roe %})) and return
on all invested capital, equity plus debt ([ROCE]({% post_url 2026-09-03-roce %})). **ROA — Return on
Assets** — asks a third, related question: how much profit did the company
generate on *everything it owns* — its total assets from the [balance
sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}) — regardless of whether that asset base was funded by
shareholders, lenders, or suppliers?

It's the broadest of the three, because total assets include things ROCE
doesn't directly capture, like short-term liabilities (payables) that also
fund part of what a company owns.

## The formula

```
ROA (%) = PAT / Average Total Assets × 100
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| PAT (FY25) | {{ db_is25.pat }} |
| Total assets, start of year (FY24) | {{ db_bs24.total_assets }} |
| Total assets, end of year (FY25) | {{ db_bs25.total_assets }} |
| Average total assets | {{ db_bs24.total_assets | plus: db_bs25.total_assets | divided_by: 2.0 }} |
| **ROA** | **{{ site.data.case_study.ratios.FY25.roa }}%** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| PAT (FY25) | {{ bi_is25.pat }} |
| Total assets, start of year (FY24) | {{ bi_bs24.total_assets }} |
| Total assets, end of year (FY25) | {{ bi_bs25.total_assets }} |
| Average total assets | {{ bi_bs24.total_assets | plus: bi_bs25.total_assets | divided_by: 2.0 }} |
| **ROA** | **{{ site.data.real_company.ratios.FY25.roa }}%** |

## ROE vs ROCE vs ROA, side by side

Three "return" ratios in a row is a lot to hold in your head at once — here's
what each one actually divides by, and Britannia's FY25 numbers for all
three together:

| Ratio | Numerator | Denominator | Whose capital? | Britannia FY25 |
|---|---|---|---|---:|
| ROE | PAT | Average equity | Shareholders' only | {{ site.data.real_company.ratios.FY25.roe }}% |
| ROCE | EBIT | Average (equity + debt) | Shareholders' + lenders' | {{ site.data.real_company.ratios.FY25.roce }}% |
| ROA | PAT | Average total assets | Everyone financing the asset base, incl. suppliers | {{ site.data.real_company.ratios.FY25.roa }}% |

ROA comes out lowest of the three here, and that's typical, not a mistake —
the denominator (total assets) is the largest of the three, since it
includes short-term supplier credit and other current liabilities on top of
equity and borrowings.

## Common mistakes

- **Comparing ROA across asset-light vs asset-heavy industries.** An IT
  services company with almost no fixed assets will show a very different
  ROA from a cement or steel manufacturer, even if both are excellent
  businesses in their own right — the asset base itself is structurally
  different.
- **Confusing ROA with ROE or ROCE.** All three sound similar and use
  overlapping inputs, but they answer different questions — see the table
  above. A company can rank differently on each depending on how it's
  financed.
- **Treating a high ROA as automatically low-risk.** ROA measures how
  efficiently assets are used, not financial risk — an asset-light company
  can still carry real operational or competitive risk that ROA won't show.
- **Not adjusting for one-off asset sales or write-downs.** A big one-time
  gain or a large impairment can swing the total-assets denominator or the
  PAT numerator in a way that doesn't reflect the ongoing business — check
  the trend, not one year.

**Takeaway:** ROA measures how much profit a company squeezes out of
everything it owns, regardless of who financed it — the broadest of the
three "return" ratios, and the natural complement to ROE and ROCE rather
than a replacement for either.
