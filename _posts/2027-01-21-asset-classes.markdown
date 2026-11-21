---
layout: post
title: "Asset classes: what equity, debt, gold and cash each do"
description: "An asset class is a group of investments that behave alike. 18 years of Indian equity, government bonds, gold and cash, year by year, and what each did."
image: /assets/og/asset-classes.png
date: 2027-01-21 09:00:00 +0530
series: money-before-markets
term: "Asset class"
---

{% assign m = site.data.mbm2 %}
{% assign ds = m.dataset %}
{% assign ac = m.asset_classes %}
{% assign se = ac.summary.equity %}
{% assign sg = ac.summary.gilt %}
{% assign sl = ac.summary.liquid %}
{% assign sa = ac.summary.gold %}

## What an asset class is

An **asset class** is a group of investments that earn their return the same
way and so tend to move together. Shares earn from company profits. Bonds
earn interest and move with interest rates. Gold earns nothing; its price is
all there is. Cash earns a short-term interest rate and barely moves.

Picking an asset class is a bigger decision than picking a fund inside it,
because two funds in the same class usually rise and fall together. This post
puts four Indian asset classes side by side over the same
{{ ds.fy_count }} financial years, so you can see what each one did, and
didn't do, before the asset allocation post later in this series asks how to
combine them. The earlier posts in
[Money Before Markets]({{ '/series/money-before-markets/' | relative_url }})
covered where safe money sits.

## The four series

Each asset class needs a long, public price history. These four are not
recommendations; they are long series this blog already uses:

| Asset class | Series used | Source |
|---|---|---|
| Equity | Nifty 50 TRI (Total Returns Index, dividends reinvested) | [NSE Indices]({{ ds.tri_source_url }}), the index arm of the National Stock Exchange |
| Government bonds | UTI Gilt Fund, regular plan, growth | AMFI (Association of Mutual Funds in India) via [mfapi.in]({{ ds.gilt_source_url }}) |
| Cash-like | UTI Liquid Fund, regular plan, growth | AMFI via [mfapi.in]({{ ds.liquid_source_url }}) |
| Gold | UTI Gold ETF (exchange-traded fund) | AMFI via [mfapi.in]({{ ds.gold_source_url }}) |

Two things make this less than perfectly like-with-like. The three funds'
NAVs (net asset values) have their costs taken out; the index has none. And
the gold ETF's NAV drops by a factor of about {{ ds.gold_split_factor }} on
{{ ds.gold_split_date }}, which looks like a unit split; we divide the earlier
NAVs by {{ ds.gold_split_factor }} so the series is continuous. Data from
{{ ds.start }} to {{ ds.end }}, past data for illustration only, pre-tax.

## The formulas

```
Yearly return (FY)    =  value on 31 March / value a year earlier  −  1
CAGR                  =  (end value / start value) ^ (1 / years)  −  1
Volatility            =  standard deviation of daily returns × √252
Maximum drawdown      =  largest fall from a peak to a later low
```

CAGR is the compound annual growth rate, from the
[point-to-point returns post]({% post_url 2026-09-26-point-to-point-returns %}).
Volatility and drawdown are explained in the
[volatility]({% post_url 2026-09-30-volatility-and-sharpe %}) and
[drawdown]({% post_url 2026-09-29-drawdown %}) posts.

## Worked example: {{ ds.fy_first }} to {{ ds.fy_last }}

### Year by year

Each financial year (FY) runs from April to March. Bold marks the best of the
four that year.

| Year | Equity | Gov. bonds | Cash-like | Gold |
|---|---:|---:|---:|---:|
{% for r in ac.fy_rows -%}
| {{ r.fy }} | {% if r.best == "equity" %}**{{ r.equity }}%**{% else %}{{ r.equity }}%{% endif %} | {% if r.best == "gilt" %}**{{ r.gilt }}%**{% else %}{{ r.gilt }}%{% endif %} | {% if r.best == "liquid" %}**{{ r.liquid }}%**{% else %}{{ r.liquid }}%{% endif %} | {% if r.best == "gold" %}**{{ r.gold }}%**{% else %}{{ r.gold }}%{% endif %} |
{% endfor %}

### Over the whole period

| {{ ds.fy_first }}–{{ ds.fy_last }} | Equity | Gov. bonds | Cash-like | Gold |
|---|---:|---:|---:|---:|
| CAGR | {{ se.cagr_pct }}% | {{ sg.cagr_pct }}% | {{ sl.cagr_pct }}% | {{ sa.cagr_pct }}% |
| ₹1 lakh became (₹) | {{ se.lakh_became }} | {{ sg.lakh_became }} | {{ sl.lakh_became }} | {{ sa.lakh_became }} |
| Volatility, a year | {{ se.vol_pct }}% | {{ sg.vol_pct }}% | {{ sl.vol_pct }}% | {{ sa.vol_pct }}% |
| Worst year | {{ se.worst_fy_pct }}% ({{ se.worst_fy }}) | {{ sg.worst_fy_pct }}% ({{ sg.worst_fy }}) | {{ sl.worst_fy_pct }}% ({{ sl.worst_fy }}) | {{ sa.worst_fy_pct }}% ({{ sa.worst_fy }}) |
| Best year | {{ se.best_fy_pct }}% ({{ se.best_fy }}) | {{ sg.best_fy_pct }}% ({{ sg.best_fy }}) | {{ sl.best_fy_pct }}% ({{ sl.best_fy }}) | {{ sa.best_fy_pct }}% ({{ sa.best_fy }}) |
| Negative years, of {{ ds.fy_count }} | {{ se.negative_fys }} | {{ sg.negative_fys }} | {{ sl.negative_fys }} | {{ sa.negative_fys }} |
| Maximum drawdown | {{ se.max_dd_pct }}% | {{ sg.max_dd_pct }}% | {{ sl.max_dd_pct }}% | {{ sa.max_dd_pct }}% |
| Years it was the best | {{ ac.best_counts.equity }} | {{ ac.best_counts.gilt }} | {{ ac.best_counts.liquid }} | {{ ac.best_counts.gold }} |

And after inflation, over the shorter span the CPI (Consumer Price Index)
series allows, {{ ac.real_first_fy }} to {{ ac.real_last_fy }}, when prices
rose {{ ac.cpi_cagr_pct }}% a year (method as in the
[real returns post]({% post_url 2026-10-20-inflation-and-real-returns %})):

| {{ ac.real_first_fy }}–{{ ac.real_last_fy }} | Equity | Gov. bonds | Cash-like | Gold |
|---|---:|---:|---:|---:|
| Nominal CAGR | {{ ac.real.equity.nominal_cagr_pct }}% | {{ ac.real.gilt.nominal_cagr_pct }}% | {{ ac.real.liquid.nominal_cagr_pct }}% | {{ ac.real.gold.nominal_cagr_pct }}% |
| Real CAGR | {{ ac.real.equity.real_cagr_pct }}% | {{ ac.real.gilt.real_cagr_pct }}% | {{ ac.real.liquid.real_cagr_pct }}% | {{ ac.real.gold.real_cagr_pct }}% |

### What the tables show

1. **Each class has its own character.** Cash-like money never had a
   negative year and its worst drawdown was {{ sl.max_dd_pct }}%. Equity's
   worst year was {{ se.worst_fy_pct }}% and its worst drawdown
   {{ se.max_dd_pct }}%, from {{ se.dd_peak }} to {{ se.dd_trough }}.
   Government bonds sat in between on volatility, with no negative
   financial year here but a {{ sg.max_dd_pct }}% fall inside one
   ({{ sg.dd_peak }} to {{ sg.dd_trough }}).
2. **Gold behaved like neither.** Its volatility ({{ sa.vol_pct }}%) was
   close to equity's ({{ se.vol_pct }}%), it had {{ sa.negative_fys }}
   negative years, and its drawdown that began on {{ sa.dd_peak }} took until
   {{ sa.dd_recovered }} to recover. It also had the highest CAGR of the four
   over this window, helped by a {{ sa.best_fy_pct }}% final year. Change the
   end date and that ranking can change; the limits post later in this
   series tests exactly that.
3. **No class won every year.** Equity was best in
   {{ ac.best_counts.equity }} years, gold in {{ ac.best_counts.gold }},
   government bonds in {{ ac.best_counts.gilt }}. The best class one year was
   often not the best the next.
4. **They moved differently.** The correlation of yearly returns (from +1,
   moving together, to −1, moving opposite; see the
   [correlation post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %}))
   was {{ ac.corr_fy.equity_gilt }} between equity and bonds and
   {{ ac.corr_fy.equity_gold }} between equity and gold. On daily returns
   both were close to zero ({{ ac.corr_daily.equity_gilt }} and
   {{ ac.corr_daily.equity_gold }}). {{ ds.fy_count }} yearly points is a small
   sample, so treat the yearly figures as a description of this period, not
   a constant.

## Common mistakes

1. **Counting funds instead of classes.** Five equity funds are still one
   asset class. Spreading money across funds that hold similar shares doesn't
   add the different behaviour you see between columns above; the
   [overlap post]({% post_url 2026-10-15-portfolio-overlap %}) measures this.
2. **Ranking classes by one period's CAGR.** The ranking in the second table
   depends on where the window starts and ends. Gold's lead here owes a lot to
   its last year; equity's CAGR from a different start would look different.
3. **Calling cash or bonds "safe" without saying from what.** Cash-like money
   avoided falls but earned {{ ac.real.liquid.real_cagr_pct }}% a year after
   inflation. Bonds avoided negative years here, yet fell
   {{ sg.max_dd_pct }}% at one point. Each class trades one risk for another.
4. **Comparing a price index with a fund.** The equity line is a total-return
   index with no costs; a fund tracking it would show slightly less. The
   [price vs total-return index post]({% post_url 2026-12-24-price-vs-total-return-index %})
   covers the other half of that trap.

**Takeaway:** An asset class is a way of earning a return, and each one
brings its own kind of bumpiness: cash barely moves, bonds wobble, equity and
gold can fall hard. In this period no single class led every year, which is
why choosing the mix between them comes before choosing a fund within each.
