---
layout: post
title: "Operating leverage: why profit grows faster than sales — and shrinks faster too"
description: "Operating leverage: how fast profit moves when sales move, because of fixed costs. Desi Bites turned 20% sales growth into 39% EBIT growth; Britannia 7% into 0."
image: /assets/og/operating-leverage.png
date: 2026-12-03 09:00:00 +0530
series: jargon
term: "Operating leverage"
---

{% assign ol = site.data.jargon_m6.operating_leverage %}
{% assign d1 = ol.desi_fy23_fy24 %}
{% assign d2 = ol.desi_fy24_fy25 %}
{% assign br = ol.britannia_fy24_fy25 %}

## What operating leverage means

Some of a company's costs rise and fall with sales — raw materials, packaging,
freight. Others don't move much whether sales are up or down — rent,
salaries, depreciation on the factory. **Operating leverage** is what that
second group does to profits: because fixed costs don't grow when revenue
grows, every extra rupee of sales above the break-even point drops through to
operating profit at the *contribution margin*, not the net margin. Profit
grows faster than revenue.

The catch is in the title. The same mechanism runs in reverse. When revenue
falls, fixed costs don't fall with it, and profit shrinks faster than sales.
High operating leverage is a description of *amplification*, not of quality.

## The formula

```
Degree of operating leverage (DOL)  =  % change in EBIT / % change in revenue

Equivalently, at a point:

DOL  =  Contribution / EBIT  =  (Revenue − Variable costs) / EBIT
```

A DOL of 2 means a 10% rise in revenue produces roughly a 20% rise in EBIT —
and a 10% fall in revenue, a 20% fall in EBIT. The higher the fixed-cost
share, the higher the DOL.

## Worked example: Desi Bites Foods, two years running

From the [case study](/case-study/), FY23 → FY24 and FY24 → FY25:

| | FY23 → FY24 | FY24 → FY25 |
|---|---:|---:|
| Revenue growth | {{ d1.revenue_growth_pct }}% | {{ d2.revenue_growth_pct }}% |
| EBITDA growth | {{ d1.ebitda_growth_pct }}% | {{ d2.ebitda_growth_pct }}% |
| EBIT growth | {{ d1.ebit_growth_pct }}% | {{ d2.ebit_growth_pct }}% |
| **DOL (on EBIT)** | **{{ d1.dol_ebit }}** | **{{ d2.dol_ebit }}** |

Revenue grew 20% both years; operating profit grew roughly twice as fast. That
is exactly what the [EBITDA margin post]({% post_url 2026-08-28-ebitda-margin %})
recorded as margins expanding from 14% to 15.5% to 17% — operating leverage is
the *mechanism* behind margin expansion on a growing top line.

Now the forward-looking version. Treat Desi Bites' FY25 cost of goods sold
({{ ol.desi_fy25_cogs_pct_revenue }}% of revenue) as variable and its opex plus depreciation
(₹{% include inr.html n=ol.desi_fy25_fixed_costs %} lakh) as fixed:

| | FY25 actual | Revenue +10%, fixed costs flat |
|---|---:|---:|
| Revenue (₹ lakh) | 2,592 | {% include inr.html n=ol.whatif_revenue %} |
| Contribution margin | {{ ol.desi_fy25_contribution_margin_pct }}% | {{ ol.desi_fy25_contribution_margin_pct }}% |
| Fixed costs (₹ lakh) | {% include inr.html n=ol.desi_fy25_fixed_costs %} | {% include inr.html n=ol.desi_fy25_fixed_costs %} |
| EBIT (₹ lakh) | {{ ol.desi_fy25_ebit }} | {{ ol.whatif_ebit }} |
| **EBIT growth** | | **{{ ol.whatif_ebit_growth_pct }}%** |

A 10% revenue rise becomes a {{ ol.whatif_ebit_growth_pct }}% EBIT rise. The point-in-time formula
agrees: contribution / EBIT = {{ ol.dol_from_formula }}. (The historical DOL of ~2 is lower because
Desi Bites' "fixed" costs actually grew each year — real companies hire people
and add capacity. The point-formula assumes they're truly frozen.)

Run it the other way. Revenue −10% with the same fixed costs would take EBIT
down by about the same {{ ol.whatif_ebit_growth_pct }}%. Three years of 20% growth flatter a
high-fixed-cost business; the first flat year does the opposite.

## Worked example: Britannia, FY24 → FY25

From Britannia's [audited FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf)
(year ended 31 March 2025). For illustration only.

| | FY24 → FY25 |
|---|---:|
| Revenue growth | {{ br.revenue_growth_pct }}% |
| EBITDA growth | {{ br.ebitda_growth_pct }}% |
| EBIT growth | {{ br.ebit_growth_pct }}% |
| **DOL (on EBIT)** | **{{ br.dol_ebit }}** |

Revenue up {{ br.revenue_growth_pct }}%, operating profit essentially flat. A DOL of {{ br.dol_ebit }} —
almost no leverage at all. That isn't because Britannia has no fixed costs; it's
because FY25 was the year input costs (wheat, palm oil, cocoa) rose sharply,
so the *variable* cost line jumped and swallowed the operating leverage the
fixed-cost base would otherwise have delivered. The
[gross margin post]({% post_url 2026-08-26-gross-margin %}) recorded the
compression. Operating leverage is one lever among several, and in FY25 the
input-cost lever was pulling harder.

This is the honest caveat on the whole concept: DOL measured from two years'
results captures everything that happened to costs in those years, not just
the fixed/variable structure. Over a single year it can be noise.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You run a lemonade stand. The table rental is ₹100 a day no matter what.
Each glass costs ₹5 to make and sells for ₹10.

Sell 30 glasses: ₹300 in, ₹150 for lemons, ₹100 rent — you keep ₹50. Sell
33 glasses (10% more): ₹330 in, ₹165 lemons, still ₹100 rent — you keep ₹65.
That's 30% more profit from 10% more sales, because the rent didn't grow.

But sell 27 glasses and you keep only ₹35 — 30% *less* profit. The rent
didn't shrink either.

</details>

## Common mistakes

- **Reading margin expansion as management skill when it's operating
  leverage on a growing top line.** The test is what happens in the first
  flat year.
- **Assuming high operating leverage is good.** It's good in growth and bad in
  decline. Ask which one you're expecting.
- **Computing DOL from one year of results and treating it as structural.**
  Britannia's {{ br.dol_ebit }} says more about FY25's commodity prices than about its
  cost structure.
- **Confusing operating with financial leverage.** Operating leverage comes
  from fixed *costs*; financial leverage from fixed *interest*, covered in the
  [debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) and
  [interest coverage]({% post_url 2026-09-17-interest-coverage %}) posts. A
  company with both is doubly amplified in both directions.

**Takeaway:** Operating leverage is fixed costs turning revenue growth into
faster profit growth — Desi Bites' 20% sales growth became 39% EBIT growth —
and it runs in reverse just as hard. Britannia's near-zero DOL in FY25 is the
other lesson: measured over one year, it's a description of that year, not of
the business.
