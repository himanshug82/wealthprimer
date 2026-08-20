---
layout: post
title: "Gross Margin: how much survives the cost of making the thing"
date: 2026-08-26 09:00:00 +0530
series: jargon
---

{% assign db25 = site.data.case_study.income_statement.FY25 %}
{% assign bi25 = site.data.real_company.income_statement.FY25 %}
{% assign bi24 = site.data.real_company.income_statement.FY24 %}

## What gross margin means

**Gross margin** answers one question: out of every rupee a company sells, how
much is left after paying for the direct cost of making or sourcing what it
sold — before touching salaries, rent, marketing, interest, or tax?

That direct cost is called **COGS** (Cost of Goods Sold) — raw materials for a
manufacturer, or the wholesale cost of goods bought for resale, for a
retailer. Gross margin is the first checkpoint in the income-statement
waterfall we walked through in [Reading an Income Statement]({% post_url 2026-08-22-reading-an-income-statement %}) — it's the very first
subtraction, before any of the rest of the business's costs show up.

## The formula

```
Gross Profit = Revenue − COGS
Gross Margin (%) = Gross Profit / Revenue × 100
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Revenue | {{ db25.revenue }} |
| COGS | {{ db25.cogs }} |
| **Gross Profit** | **{{ db25.gross_profit }}** |
| **Gross Margin** | **{{ db25.gross_profit | times: 100.0 | divided_by: db25.revenue | round: 1 }}%** |

Desi Bites keeps about ₹{{ db25.gross_profit | times: 100.0 | divided_by: db25.revenue | round: 0 }} out of every ₹100 of snacks it
sells, before it has paid a single rupee of salaries, distribution cost, or
interest.

## Worked example: Britannia Industries, FY25

Britannia Industries (NSE: BRITANNIA) — a real, listed packaged-foods maker —
reported these figures for the year ended 31 March 2025, filed with NSE/BSE
on 8 May 2025 ([source
filing](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)).
Used here only to illustrate the calculation, not as a signal to act on.

| | ₹ Crore |
|---|---:|
| Revenue from operations | {{ bi25.revenue }} |
| COGS (materials + traded goods − inventory change) | {{ bi25.cogs }} |
| **Gross Profit** | **{{ bi25.gross_profit }}** |
| **Gross Margin** | **{{ site.data.real_company.ratios.FY25.gross_margin }}%** |

For context, the same math on FY24 (year ended 31 March 2024, same filing)
gives a gross margin of {{ bi24.gross_profit | times: 100.0 | divided_by: bi24.revenue | round: 1 }}%
— a noticeably richer margin than FY25's {{ site.data.real_company.ratios.FY25.gross_margin }}%. That
compression in a single year is a real, reportable event (rising input costs,
in Britannia's case) — exactly the kind of thing gross margin is good at
surfacing early, well before it necessarily shows up in the bottom line.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say you run a lemonade stand. You sell a glass for ₹20. The lemons, sugar,
and water cost you ₹8. Your gross margin is (₹20 − ₹8) / ₹20 = 60%. It
doesn't matter yet whether you paid your little brother to help sell it, or
whether you spent ₹500 on a fancy sign — gross margin only cares about the
ingredients in the glass you just sold.

</details>

## Common mistakes

- **Comparing gross margins across very different industries.** A software
  company's "COGS" (mostly server costs) looks nothing like a snack
  manufacturer's (mostly raw material). A 70% gross margin means something
  completely different for each. Compare gross margin within an industry, or
  against the same company's own history — not across unrelated sectors.
- **Treating a rising gross margin as automatically good.** It can come from
  raising prices customers are happy to pay (great), or from quietly using
  cheaper inputs (a real risk to product quality and brand, especially for a
  packaged-foods company). The number alone won't tell you which.
- **Confusing gross margin with actual profitability.** A business can have a
  healthy gross margin and still lose money overall, if operating expenses,
  interest, or tax eat everything gross profit built. Gross margin is the
  first checkpoint, not the final verdict.
- **Reading one year in isolation.** A single year's gross margin doesn't
  tell you if it's a stable business characteristic or a one-year commodity-
  price blip — that's why Britannia's FY24 number above is worth glancing at
  alongside FY25's.

**Takeaway:** gross margin tells you what's left after only the direct cost
of what a company sold — it's the first and cleanest checkpoint in the
income statement, but it's a starting point for judging a business, not the
whole verdict.
