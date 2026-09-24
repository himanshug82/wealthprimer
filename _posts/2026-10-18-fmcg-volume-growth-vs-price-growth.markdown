---
layout: post
title: "FMCG: volume growth vs price growth, and why revenue alone misleads"
description: "A consumer company's revenue can jump 20% while it sells barely more. How to split growth into volume and price, with Marico's FY26 update as the example."
image: /assets/og/fmcg-volume-growth-vs-price-growth.png
date: 2026-10-18 09:00:00 +0530
series: fundamental-analysis
term: "Underlying volume growth (UVG)"
---

{% assign m = site.data.sectors.marico %}
{% assign fy = m.reported.fy26 %}
{% assign q = m.reported.q4 %}
{% assign pr = q.parachute_rigids %}
{% assign d = m.derived %}

## Two ways to grow, one number on the page

An FMCG (fast-moving consumer goods) company — soaps, oils, biscuits, tea —
can grow revenue in two ways. It can sell **more units**, or it can get
**more per unit**, by raising prices or by selling more of its expensive
products (a change in *mix*). The income statement shows only the total.

The two kinds of growth behave very differently. Volume growth means more
households buying, more often — it usually builds on itself. Price growth
often just passes on a rise in raw-material costs, and it can reverse when
those costs fall. That's why FMCG companies report **volume growth**
separately, and why the sector lens starts by splitting revenue growth in
two.

Most report **underlying volume growth (UVG)**: volume adjusted by the
company for things that would distort it — acquisitions, one-offs, or a
change in pack size. The adjustment is the company's own, so the definition
matters.

## The formula

```
Revenue growth  ≈  (1 + volume growth) × (1 + price-and-mix growth) − 1

so

Implied price-and-mix growth  =  (1 + revenue growth) / (1 + volume growth) − 1
```

For small numbers you can nearly add them (8% volume and 5% price ≈ 13%
revenue), but multiply when the numbers get large.

## Worked example: Marico, quarter and year to March 2026

All figures from Marico's [Information Update for Q4 FY26]({{ m.source_url }}),
filed with the stock exchanges on {{ m.release_date }}. Growth rates are as
printed, rounded to whole percentages by the company. Historical, for
illustration only. Marico sells hair oils (Parachute), edible oils
(Saffola), foods and personal care in India and abroad.

### Step 1: the India business, one quarter

The March 2026 quarter's India business — about {{ d.india_share_of_q4_revenue_pct }}% of revenue
that quarter:

| | Q4 FY26 vs Q4 FY25 |
|---|---:|
| India revenue growth | {{ q.india_revenue_growth_pct }}% |
| Underlying volume growth (India) | {{ q.domestic_volume_growth_pct }}% |
| **Implied price-and-mix growth** | **{% include inr.html n=d.q4_india_implied_price_mix_pct %}%** |

1. Revenue grew {{ q.india_revenue_growth_pct }}%, but volume only
   {{ q.domestic_volume_growth_pct }}%. Using the formula:
   {{ d.q4_rev_factor }} ÷ {{ d.q4_vol_factor }} − 1 ≈ {% include inr.html n=d.q4_india_implied_price_mix_pct %}%.
2. So roughly half of the rupee growth came from getting more per unit,
   not from selling more units. Both are real revenue — they just have different
   causes and different staying power.

The implied figure is a rough split, not a disclosed one: it treats UVG as
the volume of the whole India business and lumps price and mix together.

### Step 2: one brand, where the gap is extreme

Parachute Rigids (coconut oil in rigid packs), same quarter:

| | Q4 FY26 vs Q4 FY25 |
|---|---:|
| Reported volume growth | −{{ d.parachute_volume_decline_pct }}% |
| Revenue growth | {{ pr.revenue_growth_pct }}% |
| **Implied revenue per unit** | **+{{ d.parachute_implied_realisation_growth_pct }}%** |

3. Volume fell slightly; revenue rose {{ pr.revenue_growth_pct }}%. Almost
   all the growth was price (and mix). The backdrop, in the update: copra
   (dried coconut, the raw material) had been expensive — it describes
   "significant input cost pressures" through the year. It also says copra
   prices have since fallen about
   {{ q.copra_off_peak_pct_approx }}% from their peak, and that the brand has
   taken "selective pricing actions to pass on value to consumers". When
   prices come down, the price part of growth works in reverse.
4. The update adds that the *underlying* volume, after adjusting for
   "ml-age reductions" — less oil per pack — grew in low single digits.
   Shrinking the pack changes the measured volume: if the same number of
   packs is sold but each holds less oil, volume in litres falls. When the
   price per pack stays put, a smaller pack is also a price increase per
   millilitre.

### Step 3: what price-led growth did to margins

| | FY26 | Change vs FY25 |
|---|---:|---:|
| Revenue from operations, ₹ crore | {{ fy.revenue_cr }} | +{{ fy.revenue_growth_pct }}% |
| EBITDA, ₹ crore | {{ fy.ebitda_cr }} | +{{ fy.ebitda_growth_pct }}% |
| EBITDA margin | {{ fy.ebitda_margin_pct }}% | −{{ d.ebitda_margin_fy_bps_abs }} basis points |

5. Revenue grew {{ fy.revenue_growth_pct }}% but EBITDA (earnings before
   interest, tax, depreciation and amortisation) only
   {{ fy.ebitda_growth_pct }}%, so the
   [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}) fell from about
   {{ d.fy26_ebitda_margin_prev_pct }}% to {{ fy.ebitda_margin_pct }}%.
6. In the March quarter, [gross margin]({% post_url 2026-08-26-gross-margin %})
   was down about {{ d.gross_margin_yoy_bps_abs }} basis points year on year
   (a basis point is 0.01 percentage point). Price increases can protect
   the rupee profit per pack without protecting the percentage: if an input
   doubles and you raise the price just enough to keep the same rupee profit
   per pack, your margin *percentage* still falls, because the same profit
   now sits on a bigger price.

That's a common pattern in a raw-material-heavy consumer company during a
commodity spike: revenue up sharply, volume modest, margin down. When the
commodity falls, the mirror image is possible — prices cut, revenue growth
slower, margin recovering — though it isn't guaranteed. Neither is a verdict on the company — it's how a
raw-material-heavy business passes costs through.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your favourite chocolate bar cost ₹10 last year. This year it costs ₹12. The
shop sold 100 bars both years.

The shop's chocolate money went from ₹1,000 to ₹1,200 — up 20%! But it
didn't sell one extra bar. That's price growth.

Now imagine the company keeps the price at ₹10 but quietly makes the bar a
bit smaller. The shop still sells 100 bars for ₹1,000, but the company is
selling less chocolate. That's the "smaller pack" trick, and it's why
companies say what they mean by volume.

</details>

## Common mistakes

- **Reading revenue growth as demand.** A {{ fy.revenue_growth_pct }}%
  revenue year with {{ fy.domestic_volume_growth_pct }}% India volume growth
  (and a separate international business growing in its own currencies) is
  not "{{ fy.revenue_growth_pct }}% more product sold". Find the volume
  number first.
- **Extrapolating price-led growth.** Price increases that pass on a
  commodity spike tend to be reversed when the commodity falls, as the
  Parachute example shows. Volume growth is the part that tends to persist.
- **Missing pack-size changes.** Smaller packs at the same price raise the
  price per gram and lower reported volume. Companies that adjust for this
  call the result "underlying" volume — check what's been adjusted.
- **Comparing volume growth across companies as if it were one measure.**
  One company counts tonnes, another packs, a third an index it builds
  itself; some exclude acquisitions, some don't. Compare a company with its
  own history first.

**Takeaway:** For a consumer company, split revenue growth into volume and
price before believing it. Volume tells you whether more people are buying
more; price often just passes on raw-material costs and can reverse when
those costs fall.
