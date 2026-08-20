---
layout: post
title: "Interest Coverage: can operating profit comfortably pay the interest bill"
date: 2026-09-27 09:00:00 +0530
series: jargon
---

{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What interest coverage means

[Debt-to-Equity]({% post_url 2026-09-23-debt-to-equity %}) and the [Equity Multiplier]({% post_url 2026-09-25-equity-multiplier %}) both look at how much debt
and leverage sit on the balance sheet. **Interest Coverage** asks a more
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
the last two posts already showed: a company carrying genuinely light debt.

## Common mistakes

- **Using EBITDA instead of EBIT in the numerator.** EBITDA hasn't yet
  accounted for the plant ageing — using it inflates the ratio and can
  overstate how comfortably a company can actually service its debt.
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
  load. That's what [Debt-to-Equity]({% post_url 2026-09-23-debt-to-equity %}) and [Net Debt/EBITDA]({% post_url 2026-09-29-net-debt-ebitda %}) are for.

**Takeaway:** interest coverage measures whether a company's operating
profit can comfortably afford its interest bill — a high number is
reassuring, but it answers "can it pay?", not "how much does it owe?",
which is a separate question the leverage ratios earlier in this module
already covered.
