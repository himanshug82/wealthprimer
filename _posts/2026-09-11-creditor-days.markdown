---
layout: post
title: "Creditor Days: how long a company takes to pay its own suppliers"
date: 2026-09-11 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What creditor days means

We've covered how long stock sits before it sells ([Inventory Days]({% post_url 2026-09-07-inventory-days %})) and
how long customers take to pay ([Debtor Days]({% post_url 2026-09-09-debtor-days %})). **Creditor Days** — also called
Days Payable Outstanding (DPO), or payable days — flips the debtor-days
question around: how many days does the company itself take to pay *its*
suppliers?

Trade payables — money the company owes suppliers but hasn't paid yet — is a
liability on the [balance sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}). It's effectively free, short-term
financing: the longer a company can hold onto that cash before paying
suppliers, the less of its own working capital it needs.

## The formula

```
Creditor Days = Trade Payables / COGS × 365
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Trade payables (FY25 closing) | {{ db_bs25.payables }} |
| COGS (FY25) | {{ db_is25.cogs }} |
| **Creditor Days** | **{{ site.data.case_study.ratios.FY25.payable_days }} days** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Trade payables (FY25 closing) | {{ bi_bs25.trade_payables }} |
| COGS (FY25) | {{ bi_is25.cogs }} |
| **Creditor Days** | **{{ site.data.real_company.ratios.FY25.payable_days }} days** |

Britannia holds onto supplier cash for {{ site.data.real_company.ratios.FY25.payable_days }} days, versus Desi Bites'
{{ site.data.case_study.ratios.FY25.payable_days }}. Paired with what we just saw on debtor days — Britannia collects
from customers in under 10 days but pays suppliers in 60 — that gap is the
whole story the next post, Cash Conversion Cycle, is built to measure.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

If your local kirana store buys biscuits from a distributor on credit and
doesn't have to pay for 60 days, but sells those same biscuits to customers
for cash on day one — the store gets to use the distributor's money,
interest-free, for almost two months before it has to pay it back. That's
exactly what a company with high creditor days is doing, just at a much
bigger scale.

</details>

## Common mistakes

- **Assuming high creditor days is always a sign of negotiating strength.**
  It usually is, for a large, established company with real leverage over
  its suppliers. But for a smaller or struggling company, unusually high (or
  suddenly rising) creditor days can instead mean it's *delaying* payments
  because it's short on cash — the same number, two very different stories.
- **Ignoring the impact on supplier relationships.** Stretching payment
  terms too aggressively can strain supplier relationships over time, even
  if it looks efficient on a single year's balance sheet.
- **Mixing trade payables with other current liabilities.** Only money owed
  specifically to suppliers for goods/services belongs in this ratio —
  lumping in other short-term liabilities (like accrued expenses) distorts
  it.
- **Comparing creditor days across industries with very different supplier
  relationships.** A manufacturer buying raw materials on 60-day terms and a
  services business with almost no physical suppliers aren't comparable on
  this ratio at all.

**Takeaway:** creditor days measures how long a company effectively borrows
from its own suppliers for free — a high number for an established company
with real bargaining power is a genuine strength, but the same number for a
cash-strapped company can be a warning sign instead.
