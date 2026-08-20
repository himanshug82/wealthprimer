---
layout: post
title: "Debtor Days: how long customers take to actually pay"
date: 2026-09-09 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What debtor days means

**Debtor Days** — also called Days Sales Outstanding (DSO), or receivable
days — is the [inventory-days]({% post_url 2026-09-07-inventory-days %})-shaped question, applied to the other end of a
sale: once a company sells something on credit, how many days does it take,
on average, to actually collect the cash from the customer?

Trade receivables — money owed to the company by customers who haven't paid
yet — sit on the [balance sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}) as an asset, but they're not cash. Debtor
days measures how long that gap between "sold it" and "got paid for it"
usually lasts.

## The formula

```
Debtor Days = Trade Receivables / Revenue × 365
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Trade receivables (FY25 closing) | {{ db_bs25.receivables }} |
| Revenue (FY25) | {{ db_is25.revenue }} |
| **Debtor Days** | **{{ site.data.case_study.ratios.FY25.receivable_days }} days** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Trade receivables (FY25 closing) | {{ bi_bs25.trade_receivables }} |
| Revenue (FY25) | {{ bi_is25.revenue }} |
| **Debtor Days** | **{{ site.data.real_company.ratios.FY25.receivable_days }} days** |

That's a striking number: Britannia collects from its customers in under 10
days, versus Desi Bites' {{ site.data.case_study.ratios.FY25.receivable_days }} days. A large, established FMCG
company selling mostly through a wide distributor network with tight credit
terms — and real bargaining power over that network — collects cash fast.
That's not a coincidence; it's exactly the kind of structural strength this
ratio is built to surface.

## Common mistakes

- **Treating rising debtor days as automatically a red flag, or falling
  debtor days as automatically good.** Rising debtor days can mean weakening
  collections — or it can mean the company deliberately extended credit
  terms to win a large new customer. Context matters.
- **Comparing across business models.** A company selling mostly to
  consumers (near-zero receivables, cash or instant digital payment) and one
  selling mostly to other businesses on 30-90 day credit terms will show
  very different debtor days for reasons that have nothing to do with
  quality of management.
- **Not checking for bad debt provisions.** Reported receivables are
  sometimes shown net of amounts the company already expects not to
  collect — worth knowing whether a number is gross or net before comparing
  it across companies.
- **Watching debtor days in isolation from revenue growth.** A company that
  grows revenue partly by loosening credit terms to customers who might not
  pay is buying growth with future collection risk — debtor days rising
  alongside a revenue growth spurt is worth a second look.

**Takeaway:** debtor days measures how long a company's cash stays tied up
in unpaid customer invoices — a very low number, like Britannia's here, is
often a sign of real bargaining power over the sales channel, not just good
bookkeeping.
