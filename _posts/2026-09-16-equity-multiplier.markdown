---
layout: post
title: "Equity Multiplier: how many times equity is levered up into total assets"
description: "Total assets divided by equity: how far an asset base is levered above the equity backing it, once every liability is counted, not just the loans."
image: /assets/og/equity-multiplier.png
date: 2026-09-16 09:00:00 +0530
series: jargon
term: "Equity multiplier"
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}

## What equity multiplier means

[Debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) only counts interest-bearing borrowings. But a company can
also be "levered up" by liabilities that aren't loans at all — trade
payables, for instance. **Equity multiplier** captures the full picture: how
many times bigger is the total asset base than the equity backing it, once
*every* liability — debt or otherwise — is counted?

## The formula

```
Equity Multiplier = Total Assets / Total Equity
```

Since Total Assets = Total Equity + Total Liabilities, a higher equity
multiplier means a larger share of the asset base is funded by liabilities
of some kind, not necessarily debt specifically.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Total Assets | {{ db_bs25.total_assets }} |
| Equity | {{ db_bs25.equity }} |
| **Equity Multiplier** | **{{ site.data.case_study.ratios.FY25.equity_multiplier }}x** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only. Equity here
is *total* equity, including the small minority (non-controlling) interest, to
match total assets. (The book value per share post later in this series uses
owners' equity only.)

| | ₹ Crore |
|---|---:|
| Total Assets | {{ bi_bs25.total_assets }} |
| Total equity (incl. minority interest) | {{ bi_bs25.total_equity }} |
| **Equity Multiplier** | **{{ site.data.real_company.ratios.FY25.equity_multiplier }}x** |

Here's the puzzle this post exists to solve: Britannia's D/E was a low
{{ site.data.real_company.ratios.FY25.debt_equity }} last post, yet its equity multiplier ({{ site.data.real_company.ratios.FY25.equity_multiplier }}x) is almost
identical to Desi Bites' ({{ site.data.case_study.ratios.FY25.equity_multiplier }}x). If Britannia barely uses debt, what's
doing the "levering" here? Britannia's non-equity liabilities come to about
₹{% assign bi_liab = bi_bs25.total_assets | minus: bi_bs25.total_equity | round: 0 %}{% include inr.html n=bi_liab %} crore, and only ₹{% assign bi_debt = bi_bs25.total_borrowings | round: 0 %}{% include inr.html n=bi_debt %} crore of that is borrowings. The
single biggest item is the one the [cash conversion
cycle post]({% post_url 2026-09-10-cash-conversion-cycle %}) uncovered: trade payables of ₹{% assign bi_tp = bi_bs25.trade_payables | round: 0 %}{% include inr.html n=bi_tp %} crore. So Britannia's
suppliers are financing a large part of its asset base — with no interest,
no covenants, and far less of the repayment risk that comes with borrowed debt.
(The rest is a mix of provisions, other payables and similar items.)

## Common mistakes

- **Confusing equity multiplier with debt-to-equity.** They look similar and
  move together, but they measure different things — D/E counts only
  interest-bearing borrowings, equity multiplier counts *every* liability.
  A company can score very differently on the two, as Britannia does here.
- **Assuming a high equity multiplier always signals financial risk.** It
  depends entirely on *what* is doing the levering. Interest-bearing debt
  carries repayment risk if things go wrong; free supplier financing, backed
  by genuine negotiating strength, doesn't carry the same risk.
- **Reading equity multiplier without D/E alongside it.** Neither ratio
  alone tells the full leverage story — the gap between the two is often
  more informative than either number by itself.
- **Forgetting this is one-third of the DuPont formula.** Equity multiplier,
  paired with [net margin]({% post_url 2026-08-30-net-margin %}) and [asset turnover]({% post_url 2026-09-11-asset-turnover %}), is one of the three
  levers that together explain ROE ([return on equity]({% post_url 2026-09-01-roe %})) — a topic this series will return to in
  the Fundamental Analysis track once all three pieces are in place.

**Takeaway:** equity multiplier shows how much of a company's asset base is
funded by liabilities of any kind, not just debt. Read it next to
debt-to-equity to see whether the leverage comes from borrowed money or from
something gentler, like supplier credit.
