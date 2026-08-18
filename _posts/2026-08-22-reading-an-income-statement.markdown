---
layout: post
title: "Reading an Income Statement (P&L), using a snacks company"
date: 2026-08-22 09:00:00 +0530
series: jargon
---

{% assign is = site.data.case_study.income_statement.FY25 %}

## What an income statement is

If the balance sheet is a photograph, the income statement — also called the
**P&L** (profit and loss statement) — is the video. It shows what happened
**over a period** (a quarter, a year), not on one specific day: how much the
company sold, what it cost to sell it, and what was left over as profit.

It's a waterfall — revenue at the top, a series of costs subtracted in a
specific order, profit at the bottom. Each stopping point along the way tells
you something different about the business.

## The waterfall

| Line | What it means |
|---|---|
| Revenue | Total sales |
| − COGS (Cost of Goods Sold) | Cost of the raw material and direct production |
| = **Gross Profit** | What's left after direct production costs |
| − Operating expenses | Selling, distribution, salaries, admin |
| = **EBITDA** | Earnings Before Interest, Tax, Depreciation & Amortisation — profit from core operations, before financing and accounting decisions |
| − Depreciation | The plant wearing out over time, spread across years |
| = **EBIT** | Earnings Before Interest & Tax — operating profit, after accounting for the plant ageing |
| − Interest | Cost of the company's debt |
| = **PBT** | Profit Before Tax |
| − Tax | |
| = **PAT** | Profit After Tax — the actual bottom-line number, "net profit" |

Each subtraction removes a different kind of cost: first the cost of making
the product, then the cost of running the business day-to-day, then the cost
of the plant ageing, then the cost of borrowing, then the government's share.
What's left at each stage is a genuinely different question — "is the product
itself profitable?" (gross profit) is not the same question as "is the whole
company profitable after everything?" (PAT).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say you sell lemonade for ₹20 a glass. The lemons and sugar cost ₹8 — that's
your gross profit, ₹12. But you also paid your little brother ₹3/glass to
help sell it, so real profit is ₹9. If you borrowed money for the lemonade
stand and pay interest on it, subtract that too. What's left after every cost
is the only number that tells you what you actually get to keep.

</details>

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh | % of Revenue |
|---|---:|---:|
| Revenue | {{ is.revenue }} | 100% |
| COGS | {{ is.cogs }} | {{ is.cogs | times: 100.0 | divided_by: is.revenue | round: 1 }}% |
| **Gross Profit** | **{{ is.gross_profit }}** | **{{ is.gross_profit | times: 100.0 | divided_by: is.revenue | round: 1 }}%** |
| Operating expenses | {{ is.opex }} | {{ is.opex | times: 100.0 | divided_by: is.revenue | round: 1 }}% |
| **EBITDA** | **{{ is.ebitda }}** | **{{ is.ebitda | times: 100.0 | divided_by: is.revenue | round: 1 }}%** |
| Depreciation | {{ is.depreciation }} | {{ is.depreciation | times: 100.0 | divided_by: is.revenue | round: 1 }}% |
| **EBIT** | **{{ is.ebit }}** | **{{ is.ebit | times: 100.0 | divided_by: is.revenue | round: 1 }}%** |
| Interest | {{ is.interest }} | {{ is.interest | times: 100.0 | divided_by: is.revenue | round: 1 }}% |
| **PBT** | **{{ is.pbt }}** | **{{ is.pbt | times: 100.0 | divided_by: is.revenue | round: 1 }}%** |
| Tax | {{ is.tax }} | {{ is.tax | times: 100.0 | divided_by: is.revenue | round: 1 }}% |
| **PAT (Net Profit)** | **{{ is.pat }}** | **{{ is.pat | times: 100.0 | divided_by: is.revenue | round: 1 }}%** |

Out of every ₹100 of snacks Desi Bites sells, about
₹{{ is.gross_profit | times: 100.0 | divided_by: is.revenue | round: 0 }}
is left after paying for raw material, but only
₹{{ is.pat | times: 100.0 | divided_by: is.revenue | round: 0 }}
makes it all the way down to actual profit, after running the business,
depreciating the plant, paying interest on the loan, and paying tax. Every
line in between is a real cost that a headline "revenue grew!" number
conveniently skips over.

Full three-year version (FY23–FY25, showing margins improving as the business
scales) is on the [case study page]({{ '/case-study/' | relative_url }}).

## Common mistakes

- **Treating revenue growth as profit growth.** A company can grow revenue
  while margins shrink — meaning it's making *less* money per rupee of sales,
  even as the headline number looks better.
- **Confusing EBITDA with actual profit.** EBITDA ignores depreciation,
  interest, and tax — all real costs. It's useful for comparing operating
  performance between companies with different debt loads or accounting
  choices, but it is not what the company actually keeps.
- **Ignoring where in the waterfall a problem shows up.** A company with
  healthy gross margin but weak PAT margin has a cost, financing, or tax
  problem below the operating line — a completely different issue than a
  company whose gross margin itself is thin.
- **Looking at one year in isolation.** A single year's P&L doesn't tell you
  whether a margin is stable, improving, or one good year in an otherwise
  shaky trend — that's why every ratio post in this series looks at three
  years, not one.

**Takeaway:** an income statement is a waterfall from revenue down to profit,
and every subtraction along the way answers a different question — reading
only the top line (revenue) or the bottom line (PAT) skips the story of where
the money actually went.
