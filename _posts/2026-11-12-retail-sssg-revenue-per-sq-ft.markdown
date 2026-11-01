---
layout: post
title: "Retail: same-store growth and sales per sq ft"
description: "Retail growth comes from new stores and from older ones selling more. SSSG and revenue per sq ft explained, with Avenue Supermarts' FY26 figures."
image: /assets/og/retail-sssg-revenue-per-sq-ft.png
date: 2026-11-12 09:00:00 +0530
series: fundamental-analysis
term: "SSSG (same-store sales growth)"
---

{% assign m = site.data.sectors2.dmart %}
{% assign d = m.derived %}

## What same-store growth means

A retailer's sales can rise simply because it opened more shops. That tells you about expansion, not about whether each shop is selling more. Same-store sales growth (SSSG) — also called like-for-like (LFL) growth — strips out the new shops by measuring only stores that were already open in both periods being compared.

Two numbers answer two questions:

- **Same-store growth:** are the older shops selling more than before?
- **Sales per square foot:** how hard is each foot of selling space working?

## The formulas

```
SSSG  =  sales of comparable stores this period  /  same stores' sales last period  −  1
         (comparable = open for the whole of both periods; each company sets its own cut-off)

Sales per sq ft  =  sales for the year  /  retail area
                    (company-defined: year-end area, or the average of opening and closing area?)

Revenue growth  ≈  (growth from older stores)  +  (contribution of stores opened since)
```

The definitions matter. Avenue Supermarts (DMart) defines like-for-like growth as growth in sales from stores operational for at least 24 months at the end of the fiscal year. It computes sales per square foot by dividing annualised sales by the retail business area at the *end* of the year, not the average.

## Worked example: Avenue Supermarts, year to March 2026

From the company's [press release]({{ m.source_url }}) and investor presentation of {{ m.release_date }}. Standalone figures, as the company's headline numbers are. FY26 is the year ended 31 March 2026. Historical, for illustration only.

| | FY26 | FY25 |
|---|---:|---:|
| Revenue from operations (₹ crore) | {{ m.revenue_cr.FY26 }} | {{ m.revenue_cr.FY25 }} |
| Stores at year end | {{ m.stores.FY26 }} | {{ m.stores.FY25 }} |
| Retail area at year end (million sq ft) | {{ m.area_mn_sqft.FY26 }} | {{ m.area_mn_sqft.FY25 }} |
| Sales per sq ft, as printed (₹) | {{ m.sales_per_sqft.FY26 }} | {{ m.sales_per_sqft.FY25 }} |
| Like-for-like growth (24-month stores) | {{ m.lfl_pct.FY26 }}% | {{ m.lfl_pct.FY25 }}% |
| Bills cut (crore) | {{ m.bills_cr.FY26 }} | {{ m.bills_cr.FY25 }} |

1. Revenue rose {{ d.revenue_growth_pct }}%. Stores rose {{ d.store_growth_pct }}% (the company added {{ m.stores_added.FY26 }}) and retail area rose {{ d.area_growth_pct }}%. Older stores — the like-for-like set — grew {{ m.lfl_pct.FY26 }}%. Revenue grew faster than the older stores did, so the gap is stores opened or ramping up since. The release doesn't split the growth between the two, so we can't say by how much.
2. Printed sales per square foot moved {{ d.sales_per_sqft_change_fmt }}%, while like-for-like growth was positive. That isn't a contradiction. The release gives no breakdown of why. One general mechanism: when area is counted at year end, stores opened during the year add their full area to the denominator but only part of a year's sales to the numerator, so a fast-expanding retailer's sales per sq ft can dip even when each older store sells more. That mechanism fits the recomputed figures below better than the printed ones. The printed figure won't reproduce from the table above. Revenue from operations divided by year-end area gives ₹{% include inr.html n=d.sales_per_sqft_recomputed.FY26 %} and ₹{% include inr.html n=d.sales_per_sqft_recomputed.FY25 %}, a change of {{ d.sales_per_sqft_recomputed_change_pct }}%. The company's number uses annualised revenue from sales (not revenue from operations), so use its printed figures, with its definition, rather than rebuilding it.
3. The like-for-like set is narrower than it sounds. It counts only stores open at least 24 months at year end, so it covers part of the estate; the company's other stores are younger than 24 months and are left out.
4. Average sales per bill: ₹{% include inr.html n=d.revenue_per_bill %} in FY26 against ₹{% include inr.html n=d.revenue_per_bill_fy25 %} in FY25 (revenue divided by bills cut — our arithmetic, not a company metric). Bills rose {{ d.bills_growth_pct }}%, so growth was mostly more bills, plus a slightly larger bill.
5. EBITDA — earnings before interest, tax, depreciation and amortisation — margin was {{ d.ebitda_margin_fy26 }}% against {{ d.ebitda_margin_fy25 }}%, on the company's definition of EBITDA. In our view, thin retail margins are why sales productivity matters: small shifts in sales per foot carry through to profit. See [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) for the measure itself.

The company's chief executive's Q4 comment gives a different, quarter-only like-for-like figure. Don't put that beside the full-year number.

This is one lens from the [Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}) series, and see [capex intensity]({% post_url 2026-09-21-capex-intensity %}) for what store openings cost. It's not a view on Avenue Supermarts.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You run lemonade stands. Last year you had ten; this year you have twelve, and your total sales went up a lot.

But did that happen because the twelve stands are better, or just because you built two more? To find out, look only at the ten stands that were open both years. If *those* sold more, the older stands really improved. That's same-store growth.

</details>

## Common mistakes

- **Reading total sales growth as shop-level growth.** A growing chain can show strong total growth with flat same-store sales. Ask which part came from new space.
- **Comparing SSSG across companies with different cut-offs.** One company counts stores open 12 months, another 24. The older cut-off gives a smaller, more settled set. Check the definition.
- **Judging sales per sq ft on year-end area.** When the area base is year-end, a year of heavy openings drags the ratio down for a reason that has nothing to do with each store.
- **Ignoring the mix of what's sold.** Same-store growth can come from more bills or from bigger bills, or from price inflation in the basket. The headline doesn't say which.

## What this lens can't tell you

- **It says nothing about profit per store.** A shop can sell more and earn less after rent and wages. Pair the sales lens with margins.
- **It's company-defined.** The cut-off, the area definition and what counts as sales vary.
- **One year, backward-looking.** It describes FY26 only, and it's silent on price.

**Takeaway:** Retail growth is part new space and part older stores selling more, and same-store growth is the number that separates the two. Sales per square foot only means something once you know whether area is counted at year end or on average.
