---
layout: post
title: "Net Debt/EBITDA: how many years of profit it would take to pay off the debt"
description: "How many years of operating profit it would take to clear the debt. The ratio credit rating agencies watch, and what a negative reading actually means."
image: /assets/og/net-debt-ebitda.png
date: 2026-09-18 09:00:00 +0530
series: jargon
term: "Net debt/EBITDA"
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign db_net_debt = db_bs25.term_loan | minus: db_bs25.cash %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign bi_cash_total = bi_bs25.cash_and_bank | plus: bi_bs25.current_investments %}
{% assign bi_net_debt = bi_bs25.total_borrowings | minus: bi_cash_total %}

## What net debt/EBITDA means

This rounds off the leverage posts with a ratio lenders and credit rating
agencies commonly use: **net debt/EBITDA** — roughly, how many years of the
company's current operating profit would it take to pay off all its debt,
if every rupee of [EBITDA]({% post_url 2026-08-28-ebitda-margin %}) went straight to debt repayment?

Treat that "years" reading as a floor, not an estimate. EBITDA comes before
interest, tax and capital spending, so the cash genuinely free to repay debt
is smaller — the real payback would take longer.

**Net debt** nets a company's borrowings against the cash and liquid
investments it's sitting on — because cash on hand could, in principle, be
used to pay debt down immediately.

## The formula

```
Net Debt = Total Borrowings − (Cash & Bank + Liquid Investments)
Net Debt / EBITDA = Net Debt / EBITDA
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Term Loan | {{ db_bs25.term_loan }} |
| − Cash | {{ db_bs25.cash }} |
| **Net Debt** | **{{ db_net_debt }}** |
| EBITDA | {{ db_is25.ebitda }} |
| **Net Debt / EBITDA** | **{{ site.data.case_study.ratios.FY25.net_debt_ebitda }}x** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). Cash here includes both cash
& bank balances and current investments (treasury holdings classified as
current assets), since both could realistically be used to pay down debt.
For illustration only.

| | ₹ Crore |
|---|---:|
| Total Borrowings | {{ bi_bs25.total_borrowings }} |
| − (Cash & Bank + Current Investments) | {{ bi_cash_total }} |
| **Net Debt** | **{{ bi_net_debt }}** |
| EBITDA | {{ bi_is25.ebitda }} |
| **Net Debt / EBITDA** | **{% include inr.html n=site.data.real_company.ratios.FY25.net_debt_ebitda %}x** |

Britannia's net debt is *negative* — it holds more cash and liquid
investments than it owes in borrowings. It's in a net cash position, not a
net debt one — so read the negative ratio as "no net debt", not as a
negative number of years. That rounds off what the last few posts have shown
for Britannia: a current ratio and quick ratio that looked tight in
isolation, a low debt-to-equity, an equity multiplier explained by supplier
financing rather than borrowing, comfortable interest coverage — and now,
a balance sheet with more cash than debt on it. None of these ratios told
the whole story alone; read together, they tell a much fuller one.

## Common mistakes

- **Misreading negative net debt (net cash) as automatically wasted
  capital.** It can mean a company is sitting on cash it should be
  deploying — or it can mean genuine financial strength and optionality.
  Worth asking why, not assuming either answer.
- **Using different "cash" definitions without checking.** Some sources use
  cash & equivalents only; this post also includes liquid current
  investments, since Britannia holds meaningful treasury balances there —
  always check which definition a given number is using before comparing
  across sources.
- **Using a single year's EBITDA in a cyclical downturn.** EBITDA can swing
  faster than debt levels — a company's net debt/EBITDA can look
  artificially high or low in an unusual year, even if its debt itself
  hasn't changed much.
- **Ignoring debt maturity.** A low net debt/EBITDA doesn't tell you when
  the debt is actually due — a company could have a small, low ratio but a
  large single repayment due next year, which is still a real liquidity
  question this ratio doesn't answer.

**Takeaway:** net debt/EBITDA roughly measures how many years of operating
profit it would take to clear a company's debt after netting off its cash.
Like every leverage ratio, it's most useful read alongside the others, not
on its own.
