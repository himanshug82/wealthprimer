---
layout: post
title: "Net Margin: what actually makes it to the bottom line"
series: jargon
---

{% assign db25 = site.data.case_study.income_statement.FY25 %}
{% assign bi25 = site.data.real_company.income_statement.FY25 %}
{% assign bi24 = site.data.real_company.income_statement.FY24 %}

## What net margin means

**Net margin** is the last checkpoint in the income-statement waterfall —
after COGS, operating expenses, depreciation, interest, and tax have all
been subtracted. It's **PAT** (Profit After Tax, sometimes called net profit)
as a percentage of revenue: out of every rupee of sales, how much does the
company actually get to keep, after every single cost?

If gross margin and [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) tell you how the core business is doing,
net margin tells you what's left for shareholders once financing, tax, and
everything else has taken its share.

## The formula

```
Net Margin (%) = PAT / Revenue × 100
```

## Worked example: Desi Bites Foods, FY25

| | ₹ Lakh |
|---|---:|
| Revenue | {{ db25.revenue }} |
| PAT (Net Profit) | {{ db25.pat }} |
| **Net Margin** | **{{ db25.pat | times: 100.0 | divided_by: db25.revenue | round: 1 }}%** |

Out of every ₹100 Desi Bites sells, roughly ₹{{ db25.pat | times: 100.0 | divided_by: db25.revenue | round: 0 }} makes it all the way
to the bottom line as profit for shareholders.

## Worked example: Britannia Industries, FY25

From Britannia Industries' [audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025, filed 8 May 2025). PAT here is profit
attributable to owners of the company. For illustration only, not a
recommendation.

| | ₹ Crore |
|---|---:|
| Revenue from operations | {{ bi25.revenue }} |
| PAT (Net Profit) | {{ bi25.pat }} |
| **Net Margin** | **{{ site.data.real_company.ratios.FY25.net_margin }}%** |

Worth noticing what *didn't* happen here: [gross margin]({% post_url 2026-08-26-gross-margin %}) and EBITDA margin
both compressed from FY24 to FY25 at Britannia, but net margin only dipped
slightly — from {{ bi24.pat | times: 100.0 | divided_by: bi24.revenue | round: 1 }}% in FY24 to {{ site.data.real_company.ratios.FY25.net_margin }}% in FY25. Below-the-line
items (other income, interest, tax) don't always move in the same direction
as operating costs, so margins at different checkpoints in the waterfall
can tell slightly different stories in the same year.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You sold ₹500 of lemonade. After lemons and sugar (₹200), paying your
brother to help (₹100), and giving ₹50 to your parents because they lent you
the jug, you have ₹150 left — but you still owe ₹15 in "tax" (your parents'
rule: 10% of whatever's left goes to the family savings jar). What's
actually yours to keep is ₹135. Net margin is that final ₹135, as a share of
the original ₹500 — everyone else's cut has already been paid.

</details>

## Common mistakes

- **Treating net margin as the single number that matters.** It's the last
  checkpoint, not the only one. Two companies can have identical net margins
  for completely different reasons — one from a genuinely efficient
  operation, another because a one-off gain (like an asset sale) padded the
  bottom line for a single year.
- **Ignoring one-off/exceptional items.** A company's reported PAT can
  include gains or losses that have nothing to do with its ongoing business
  (an asset sale, a legal settlement, a write-down). A spike or dip in net
  margin is worth checking against the notes to the financials before
  drawing a conclusion.
- **Comparing net margins across industries or tax regimes.** An asset-light
  IT services company and a capital-heavy manufacturer will have
  structurally different net margins even if both are run equally well —
  and effective tax rates vary by company and year too.
- **Assuming a high net margin means low risk.** Net margin describes
  profitability, not financial risk. A company can have a healthy net margin
  and still carry a debt load that makes it fragile — that's a separate
  question, covered later in the Leverage module.

**Takeaway:** net margin is what's actually left for shareholders after
every cost — the last word on a given year's profitability, but not the
whole story on whether that profit is durable, high-quality, or fairly
priced.
