---
layout: post
title: "Interest Coverage: can operating profit comfortably pay the interest bill"
description: "Whatever the debt load, can operating profit comfortably pay the interest bill? EBIT over interest, and why lenders reach for this ratio first."
image: /assets/og/interest-coverage.png
date: 2026-09-17 09:00:00 +0530
series: jargon
term: "Interest coverage"
---

{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What interest coverage means

[Debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) and the [equity multiplier]({% post_url 2026-09-16-equity-multiplier %}) both look at how much debt
and leverage sit on the balance sheet. **Interest coverage** asks a more
immediate question: whatever the debt load, can the company comfortably
afford the interest payments on it out of its regular operating profit?

## The formula

```
Interest Coverage = EBIT / Interest
```

We use [EBIT]({% post_url 2026-08-22-reading-an-income-statement %}) — operating profit after depreciation, but before interest
and tax — because that's the profit actually available to pay lenders,
before anything is set aside for the government or for shareholders.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| EBIT | {{ db_is25.ebit }} |
| Interest | {{ db_is25.interest }} |
| **Interest Coverage** | **{{ site.data.case_study.ratios.FY25.interest_coverage }}x** |

Desi Bites earns enough operating profit to cover its interest bill about
{{ site.data.case_study.ratios.FY25.interest_coverage }} times over — comfortable, though not enormous headroom for a
smaller manufacturer still carrying a meaningful term loan.

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| EBIT | {{ bi_is25.ebit }} |
| Interest | {{ bi_is25.interest }} |
| **Interest Coverage** | **{{ site.data.real_company.ratios.FY25.interest_coverage }}x** |

At {{ site.data.real_company.ratios.FY25.interest_coverage }}x, Britannia's operating profit covers its interest bill roughly
three times as comfortably as Desi Bites' does — consistent with everything
the last two posts already showed: a company carrying light debt.

## Common mistakes

- **Not knowing which version you're looking at.** Many lenders compute
  coverage as EBITDA ÷ interest — a standard variant, but it comes out
  higher, because EBITDA hasn't yet accounted for the plant ageing. This
  series uses EBIT, the stricter version; check which one a source uses
  before comparing numbers.
- **Reading one year's coverage without checking the trend.** A single
  strong year's EBIT can flatter interest coverage even if the underlying
  business is inconsistent — several years tell a more honest story than
  one.
- **Ignoring the type of debt behind the interest figure.** A company paying
  a low fixed rate on long-tenure debt has a very different risk profile
  from one paying a similar rate on floating-rate, short-tenure debt that
  could reset higher — interest coverage doesn't distinguish between them.
- **Treating comfortable coverage as proof the debt itself is small.**
  Coverage measures serviceability, not size — a company can have very
  comfortable interest coverage and still carry a large absolute debt
  load. That's what [debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) and net debt/EBITDA,
  covered in the next post, are for.

**Takeaway:** interest coverage tells you whether a company's operating
profit can comfortably pay its interest bill. It answers "can it pay?", not
"how much does it owe?" — so read it alongside the leverage ratios.
