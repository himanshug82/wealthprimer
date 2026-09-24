---
layout: post
title: "Cement: EBITDA per tonne and capacity utilisation"
description: "In cement, percentage margins hide what matters: profit per tonne and how full the plants are. Both explained, and rebuilt from UltraTech Cement's FY26 release."
image: /assets/og/cement-ebitda-per-tonne-capacity-utilisation.png
date: 2026-10-19 09:00:00 +0530
series: fundamental-analysis
term: "EBITDA per tonne"
---

{% assign u = site.data.sectors.ultratech %}
{% assign rp = u.reported %}
{% assign d = u.derived %}

## Why cement is read per tonne

Cement is about as close to a commodity as a manufactured product gets. One
company's 50 kg bag is much like another's, it's too heavy to ship far
cheaply, and its price in any region moves with that region's supply and
demand. The costs — power and fuel, freight, limestone — are also counted
in tonnes.

So cement analysts don't start from margins in percent. They start from
**rupees per tonne**: how much the company realised on each tonne, what each
tonne cost, and what was left — **EBITDA per tonne** (earnings before
interest, tax, depreciation and amortisation, divided by tonnes sold).
Percentage margins move whenever cement *prices* move, even if nothing
about the business changed. Per-tonne profit strips that out.

The second number is **capacity utilisation**: how full the plants are. A
cement plant is a big fixed cost. Once it's built, every extra tonne it
sells carries most of its price straight to profit — the
[operating leverage]({% post_url 2026-10-09-operating-leverage %}) mechanism
at industrial scale. Steel and aluminium makers are read the same way,
per tonne and per unit of capacity.

## The formulas

```
EBITDA per tonne        =  EBITDA  /  tonnes sold

Realisation per tonne   =  net sales  /  tonnes sold
Cost per tonne          =  realisation per tonne − EBITDA per tonne

Capacity utilisation    =  volume produced (or sold)  /  installed capacity
                           (for a quarter, annualise the volume — × 4 —
                            or use a quarter's worth of capacity)

Units:  ₹ crore = 10,000,000 rupees;  MTPA = million tonnes per annum
```

The whole trick is to keep the numerator and denominator on the same base:
the same businesses, the same geography, the same period.

## Worked example: UltraTech Cement, FY26

From UltraTech's [results press release]({{ u.source_url }}) of
{{ u.release_date }}, covering the quarter and year to 31 March 2026
(consolidated). UltraTech calls EBITDA "PBIDT" — profit before interest,
depreciation and tax. Historical, for illustration only.

| | Q4 FY26 | Q4 FY25 | FY26 | FY25 |
|---|---:|---:|---:|---:|
| Net sales, ₹ crore | {{ rp.net_sales_cr.Q4FY26 }} | {{ rp.net_sales_cr.Q4FY25 }} | {{ rp.net_sales_cr.FY26 }} | {{ rp.net_sales_cr.FY25 }} |
| PBIDT, ₹ crore | {{ rp.pbidt_cr.Q4FY26 }} | {{ rp.pbidt_cr.Q4FY25 }} | {{ rp.pbidt_cr.FY26 }} | {{ rp.pbidt_cr.FY25 }} |
| India grey cement sold, million tonnes | {{ rp.india_grey_volume_mt.Q4FY26 }} | — | {% include inr.html n=rp.india_grey_volume_mt.FY26 %} | — |

### Step 1: the company's own number

1. The release reports an **operating PBIDT per tonne** of
   ₹{% include inr.html n=rp.operating_pbidt_per_tonne_q4 %} for the March 2026 quarter,
   {{ rp.operating_pbidt_per_tonne_q4_growth_pct }}% higher than a year
   earlier, and says total cost per tonne fell
   {{ rp.total_cost_per_tonne_change_q4_pct | abs }}% year on year.

### Step 2: rebuild it yourself — and see why it doesn't match

2. Divide the quarter's consolidated PBIDT by its India grey cement tonnes:
   ₹{% include inr.html n=rp.pbidt_cr.Q4FY26 %} crore ÷ {{ rp.india_grey_volume_mt.Q4FY26 }} million
   tonnes ≈ **₹{% include inr.html n=d.homemade_pbidt_per_tonne_q4 %} per tonne**.
3. For the full year: ₹{% include inr.html n=rp.pbidt_cr.FY26 %} crore ÷
   {% include inr.html n=rp.india_grey_volume_mt.FY26 %} million tonnes ≈
   **₹{% include inr.html n=d.homemade_pbidt_per_tonne_fy26 %} per tonne**.
4. The homemade quarterly figure is about ₹{{ d.homemade_vs_reported_q4_gap }}
   higher than the company's. That's not an error on either side; the bases
   differ. The numerator here is *all* of consolidated PBIDT — white cement
   and value-added products, overseas plants and, depending on how the
   company defines PBIDT, other income — while the denominator is only India
   grey cement tonnes. The company's
   figure is labelled "operating", and the release doesn't set out exactly
   which lines and tonnes go into it.

The lesson: use a company's own per-tonne series to follow its trend, use
your own to cross-check, and never compare your version for one company with
the reported version for another.

### Step 3: how full are the plants?

5. The release gives **capacity utilisation of {{ rp.capacity_utilisation_q4_pct }}%**
   for the quarter.
6. Rebuild it roughly. Domestic grey capacity was
   {{ rp.domestic_capacity_after_apr2026_mtpa }} MTPA *after*
   {{ rp.capacity_commissioned_apr2026_mtpa }} MTPA was added in April 2026,
   so about {{ d.capacity_end_fy26_mtpa }} MTPA at 31 March 2026. The
   quarter's {{ rp.india_grey_volume_mt.Q4FY26 }} million tonnes × 4 ≈
   {{ d.q4_annualised_volume_mt }} million tonnes a year, and
   {{ d.q4_annualised_volume_mt }} ÷ {{ d.capacity_end_fy26_mtpa }} ≈
   **{{ d.q4_utilisation_check_pct }}%** — close to the reported figure.
7. Annualising one quarter is rough: construction activity varies through
   the year, so a strong quarter overstates the year, and the company may
   measure capacity on a slightly different base (for example, averaging
   capacity added mid-quarter).

### Step 4: what volume and utilisation did to margins

| | FY26 | FY25 |
|---|---:|---:|
| Net sales growth | {{ d.net_sales_growth_pct }}% | |
| PBIDT growth | {{ d.pbidt_growth_pct }}% | |
| PBIDT margin (PBIDT ÷ net sales) | {{ d.pbidt_margin_fy26_pct }}% | {{ d.pbidt_margin_fy25_pct }}% |
| Capex, ₹ crore (share of net sales) | {% include inr.html n=rp.capex_fy26_cr %} ({% include inr.html n=d.capex_intensity_fy26_pct %}%) | |

8. PBIDT grew about twice as fast as net sales, and the margin rose — the
   operating-leverage pattern. The release credits "strong volume growth,
   cost discipline, and the progressive integration of acquired assets".
9. That last phrase matters: FY26 isn't a clean like-for-like year. Part of
   the growth came from integrating acquired plants, so not all of it is
   organic, and the release doesn't split the two.
10. Growth in cement is built in steps: the company commissioned
    {{ rp.capacity_commissioned_fy26_mtpa }} MTPA during FY26 and spent
    ₹{% include inr.html n=rp.capex_fy26_cr %} crore on capex — about
    {% include inr.html n=d.capex_intensity_fy26_pct %}% of net sales, against
    Britannia's {{ site.data.real_company.ratios.FY25.capex_intensity }}% in
    FY25 (see [capex intensity]({% post_url 2026-09-21-capex-intensity %})).
    New capacity usually runs below full rate at first, which pulls
    utilisation down until demand fills it.

None of this is a view on UltraTech. It's one year's release, read per
tonne.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A bakery has one big oven. Paying for the oven, the rent and the baker costs
the same whether it bakes 100 loaves a day or 400.

If the oven is only a quarter full, each loaf has to carry a big share of
those costs, and the bakery barely makes money. If the oven is nearly full,
each loaf carries only a small share, and most of the price is profit.

"How full is the oven?" is capacity utilisation. "How much profit on each
loaf?" is profit per tonne. A cement company is a bakery with a very, very
big oven.

</details>

## Common mistakes

- **Mixing bases in a per-tonne number.** Consolidated profit divided by
  one segment's tonnes (as in Step 2) gives a number that looks precise and
  isn't comparable with anything. Match the profit to the tonnes that earned
  it, or use the company's own series.
- **Comparing per-tonne profit across companies without asking why it
  differs.** Distance to market, the fuel mix, captive power and the regions
  a company sells in all move cost per tonne. A gap between two companies is
  a question, not an answer.
- **Treating new capacity as new sales.** Capacity is the ceiling, not the
  volume. Utilisation often falls when big capacity arrives, and rising
  capacity with flat utilisation means more tonnes sold, not a fuller plant.
- **Ignoring acquisitions in year-on-year growth.** When a company buys
  plants, volumes and profits jump without any change in the underlying
  business. Look for the company's own note on acquired assets before
  reading growth as organic.

**Takeaway:** Read a cement company per tonne, not per rupee of sales: profit
per tonne strips out price swings, and capacity utilisation shows how hard
the fixed plant is working. Keep the numerator and denominator on the same
base, or the per-tonne number means nothing.
