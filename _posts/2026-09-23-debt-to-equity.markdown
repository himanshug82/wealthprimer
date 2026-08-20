---
layout: post
title: "Debt-to-Equity: how much of the business runs on borrowed money"
date: 2026-09-23 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}

## What debt-to-equity means

The last three posts looked at short-term coverage — can the company pay
its bills over the next year? **Debt-to-Equity (D/E)** shifts to the bigger,
longer-term question: how is the business funded at all — by shareholders'
own money, or by borrowed money?

This series defines "debt" as interest-bearing borrowings only (term loans,
bonds, working capital debt) — not every liability on the balance sheet.
Trade payables, for instance, aren't counted here, even though they're
technically a liability too; they showed up in their own right back in
[Creditor Days]({% post_url 2026-09-11-creditor-days %}). Worth checking which definition any given source uses,
since "debt" isn't always defined the same way everywhere.

## The formula

```
Debt-to-Equity = Total Borrowings / Total Equity
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Term Loan (Borrowings) | {{ db_bs25.term_loan }} |
| Equity | {{ db_bs25.equity }} |
| **Debt-to-Equity** | **{{ site.data.case_study.ratios.FY25.debt_equity }}** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Total Borrowings | {{ bi_bs25.total_borrowings }} |
| Total Equity | {{ bi_bs25.total_equity }} |
| **Debt-to-Equity** | **{{ site.data.real_company.ratios.FY25.debt_equity }}** |

Britannia's D/E of {{ site.data.real_company.ratios.FY25.debt_equity }} is genuinely low leverage — far less reliant on
borrowed money than Desi Bites' {{ site.data.case_study.ratios.FY25.debt_equity }}. That matters for one specific reason
worth remembering from the [ROE post]({% post_url 2026-09-01-roe %}): debt is exactly the lever that can
inflate ROE without the underlying business actually improving. Britannia's
[ROE was a strong 52.5%]({% post_url 2026-09-01-roe %}) — and now we know that number wasn't manufactured
by heavy borrowing. It's earned mostly on genuine operating strength.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

If you buy a ₹10,000 bicycle using ₹8,000 of your own savings and a ₹2,000
loan from a friend, your debt-to-equity is ₹2,000 / ₹8,000 = 0.25 — mostly
your own money, a little borrowed. If instead you put in only ₹2,000 and
borrowed ₹8,000, your D/E flips to 4.0 — mostly borrowed. Same bicycle,
very different amount of risk if something goes wrong and you can't repay
the loan.

</details>

## Common mistakes

- **Comparing D/E across industries without adjusting for norms.** Banks
  and NBFCs structurally run on very high D/E as part of their business
  model — comparing them to a manufacturer on this ratio alone is
  meaningless.
- **Treating all debt as equally risky.** A low-interest, long-tenure loan
  is a very different risk from expensive, short-fuse borrowing — D/E
  captures the amount, not the quality, of the debt.
- **Assuming rising D/E is automatically bad.** Taking on debt to fund
  genuinely value-accretive expansion (a new plant that will pay for
  itself) is a very different story from borrowing to cover operating
  losses — the reason behind the change matters more than the change
  itself.
- **Using D/E as the only leverage lens.** As the next post shows, a company
  can carry very little interest-bearing debt and still be significantly
  "levered" through other liabilities — D/E alone doesn't catch that.

**Takeaway:** debt-to-equity measures how much of a business is funded by
borrowed money versus shareholders' own — a low D/E, paired with a strong
ROE like Britannia's here, is a sign that returns are being earned on
genuine business quality, not manufactured through leverage.
