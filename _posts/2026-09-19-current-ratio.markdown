---
layout: post
title: "Current Ratio: can short-term assets cover short-term bills"
date: 2026-09-19 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign db_ca = db_bs25.inventory | plus: db_bs25.receivables | plus: db_bs25.cash %}
{% assign db_cl = db_bs25.payables | plus: db_bs25.other_current_liabilities %}

## What the current ratio means

[Net Working Capital]({% post_url 2026-09-17-net-working-capital %}) gave us a rupee cushion, but a rupee cushion only means
something relative to the size of the bills it needs to cover. **Current
Ratio** fixes that by turning the same two numbers into a ratio instead of a
difference: for every rupee of current liabilities, how many rupees of
current assets does the company have on hand?

## The formula

```
Current Ratio = Current Assets / Current Liabilities
```

A ratio above 1 means current assets exceed current liabilities — on paper,
enough to cover near-term obligations. Below 1 means the opposite.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Current Assets | {{ db_ca }} |
| Current Liabilities | {{ db_cl }} |
| **Current Ratio** | **{{ site.data.case_study.ratios.FY25.current_ratio }}** |

Desi Bites has {{ site.data.case_study.ratios.FY25.current_ratio }}x its current liabilities in current assets — a
comfortable cushion for a smaller manufacturer that doesn't collect from
customers or turn inventory especially fast.

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only.

| | ₹ Crore |
|---|---:|
| Current Assets | {{ bi_bs25.total_current_assets }} |
| Current Liabilities | {{ bi_bs25.total_current_liabilities }} |
| **Current Ratio** | **{{ site.data.real_company.ratios.FY25.current_ratio }}** |

At {{ site.data.real_company.ratios.FY25.current_ratio }}, Britannia's current ratio is barely above 1 — far tighter than
Desi Bites'. Read on its own, that might look like a warning sign. But
remember Britannia's [cash conversion cycle]({% post_url 2026-09-13-cash-conversion-cycle %}) is *negative* — it collects
from customers and moves inventory faster than it pays its own suppliers. A
company that fast doesn't need to sit on a large buffer of current assets to
stay safe; the cash keeps arriving quickly enough on its own. This is
exactly why current ratio should never be read in isolation from the
working-capital cycle behind it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two families, both with ₹1,000 of bills due this month. Family A
keeps ₹2,500 in a jar just in case. Family B keeps only ₹1,080 in the jar —
but Family B gets paid every single day and always has fresh cash coming in
before their bills are due. Family B doesn't need as big a jar, because
money keeps flowing in fast enough on its own. The jar size alone doesn't
tell you which family is actually in better shape — you also need to know
how fast money moves in and out.

</details>

## Common mistakes

- **Assuming a higher current ratio is always better.** A very high current
  ratio can mean idle cash or excess inventory sitting around instead of
  being put to productive use — it isn't automatically a sign of strength.
- **Reading a ratio near or below 1 as automatically risky, without checking
  the operating cycle behind it.** As Britannia shows here, a fast-cycling,
  strong-bargaining-power business can run safely on a thin current ratio.
- **Comparing current ratios across industries.** A capital-project business
  with a long cash cycle needs a very different current ratio than a
  fast-turning FMCG company to be equally safe.
- **Treating one balance-sheet date as the full picture.** Current ratio can
  shift meaningfully around a company's seasonal peaks — check the trend,
  not one snapshot.

**Takeaway:** current ratio measures whether short-term assets can cover
short-term bills, but the "right" number depends entirely on how fast a
company's cash actually moves — a thin current ratio paired with a negative
cash conversion cycle can be perfectly safe, while the same ratio at a
slower-cycling company might not be.
