---
layout: post
title: "Net Working Capital: the cushion for day-to-day operations"
date: 2026-09-17 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign db_ca = db_bs25.inventory | plus: db_bs25.receivables | plus: db_bs25.cash %}
{% assign db_cl = db_bs25.payables | plus: db_bs25.other_current_liabilities %}

## What net working capital means

The last module looked at the individual pieces of a company's operating
cycle — [inventory]({% post_url 2026-09-07-inventory-days %}), [receivables]({% post_url 2026-09-09-debtor-days %}), and [payables]({% post_url 2026-09-11-creditor-days %}). This module
asks a different question about the same balance sheet: does the company
have enough short-term resources to comfortably cover its short-term
obligations? **Net Working Capital (NWC)** is the starting point.

**Current assets** are everything expected to turn into cash within a year —
cash itself, receivables, inventory. **Current liabilities** are everything
due within a year — payables, short-term borrowings, other near-term dues.
NWC is simply the gap between the two: the cushion left over after every
near-term bill is accounted for.

## The formula

```
Net Working Capital = Current Assets − Current Liabilities
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Inventory + Receivables + Cash (Current Assets) | {{ db_ca }} |
| Payables + Other Current Liabilities (Current Liabilities) | {{ db_cl }} |
| **Net Working Capital** | **{{ site.data.case_study.ratios.FY25.net_working_capital }}** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Total Current Assets | {{ bi_bs25.total_current_assets }} |
| Total Current Liabilities | {{ bi_bs25.total_current_liabilities }} |
| **Net Working Capital** | **{{ site.data.real_company.ratios.FY25.net_working_capital }}** |

Look at those two numbers next to each other: Britannia is a vastly bigger
company than Desi Bites, yet its net working capital cushion
(₹{{ site.data.real_company.ratios.FY25.net_working_capital }} crore) is proportionally much thinner relative to
its current liabilities than Desi Bites' is. That's not a red flag on its
own — it's the first clue in a story the next two posts (Current Ratio,
Quick Ratio) will unpack properly.

## Common mistakes

- **Judging NWC by its absolute rupee value alone.** ₹295 crore sounds like
  a lot until you see it next to ₹3,618 crore of current liabilities. NWC
  only means something relative to the size of the business — which is
  exactly why the next post normalizes it into the Current Ratio.
- **Assuming a bigger company needs a bigger NWC number.** It needs a bigger
  NWC in absolute terms just to stand still as it scales, but *how much*
  bigger depends entirely on its operating cycle — a company with fast
  collections and slow payments (like the one we're about to see) can run
  safely on far less.
- **Treating negative NWC as automatically alarming.** Some very
  well-run businesses — especially ones with a negative cash conversion
  cycle — operate comfortably with low or even negative NWC, because cash
  keeps flowing in faster than it needs to flow out.
- **Reading one balance-sheet date in isolation.** Like inventory, NWC can
  swing with seasonality — a single snapshot doesn't always represent the
  year.

**Takeaway:** net working capital is the raw rupee cushion between what a
company can turn into cash soon and what it owes soon — useful as a
starting point, but it only becomes a meaningful signal once it's sized
relative to the business, which is what the Current Ratio does next.
