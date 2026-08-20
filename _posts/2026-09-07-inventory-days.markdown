---
layout: post
title: "Inventory Days: how long stock sits on the shelf before it sells"
date: 2026-09-07 09:00:00 +0530
series: jargon
---

{% assign db_bs25 = site.data.case_study.balance_sheet.FY25 %}
{% assign db_is25 = site.data.case_study.income_statement.FY25 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}

## What inventory days means

We've spent the last few posts on profitability — how much of every rupee of
sales a company keeps. **Inventory Days** (also called Days Inventory
Outstanding, or DIO) is the first of a different family of ratios:
efficiency, or how well a company manages the cash tied up in running the
business day to day.

Inventory Days answers a simple operational question: on average, how many
days does stock sit around — as raw material, work in progress, or finished
goods — before it's sold? A snacks company holding 60 days of inventory is
carrying two months of unsold stock at any given time; one holding 20 days
turns its shelves much faster.

## The formula

```
Inventory Days = Inventory / COGS × 365
```

We divide by [COGS]({% post_url 2026-08-26-gross-margin %}) rather than revenue, because inventory is carried
at its cost to the company, not at what it'll eventually sell for.

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Inventory (FY25 closing) | {{ db_bs25.inventory }} |
| COGS (FY25) | {{ db_is25.cogs }} |
| **Inventory Days** | **{{ site.data.case_study.ratios.FY25.inventory_days }} days** |

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). For illustration only, not a
signal to act on.

| | ₹ Crore |
|---|---:|
| Inventory (FY25 closing) | {{ bi_bs25.inventory }} |
| COGS (FY25) | {{ bi_is25.cogs }} |
| **Inventory Days** | **{{ site.data.real_company.ratios.FY25.inventory_days }} days** |

Britannia turns its inventory faster than Desi Bites — {{ site.data.real_company.ratios.FY25.inventory_days }} days versus
{{ site.data.case_study.ratios.FY25.inventory_days }}. That's a real, structural advantage of scale and distribution reach
in packaged foods: a bigger, more efficient distribution network moves stock
off shelves faster than a smaller manufacturer can manage.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a fruit stall. If a crate of mangoes sits unsold for 10 days, that's
10 days the stall owner's money is stuck in mangoes instead of in cash. A
stall that sells its mangoes in 3 days gets its money back — and can buy the
next crate — much faster than one that takes 10. Inventory days measures
exactly that: how long money is "stuck" in stock before it turns back into
cash.

</details>

## Common mistakes

- **Comparing inventory days across very different industries.** A jewellery
  retailer and a bakery have completely different natural inventory cycles —
  one sells through slowly by design, the other has to move stock daily.
  Compare within the same industry, or against the same company's own
  history.
- **Assuming falling inventory days is always good.** It can mean genuinely
  better efficiency — or it can mean the company is running low on stock and
  risking stockouts, which shows up later as lost sales.
- **Assuming rising inventory days is always bad.** A company stocking up
  ahead of a big seasonal push (festive season for an Indian FMCG company,
  for instance) will show temporarily higher inventory days without
  anything being wrong.
- **Reading one year-end snapshot without checking seasonality.** Inventory
  levels can swing a lot within a year — a single balance-sheet date doesn't
  always represent the average.

**Takeaway:** inventory days measures how long a company's cash stays tied
up in unsold stock — lower is generally more efficient, but the number only
means something when read against the company's own industry and history,
not in isolation.
