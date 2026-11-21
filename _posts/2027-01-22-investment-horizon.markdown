---
layout: post
title: "Investment horizon: how often each asset lost money"
description: "Investment horizon is how long money can be left before it is needed. How often Indian equity, bonds, gold and cash lost money over 1 to 10-year windows."
image: /assets/og/investment-horizon.png
date: 2027-01-22 09:00:00 +0530
series: money-before-markets
term: "Investment horizon"
---

{% assign m = site.data.mbm2 %}
{% assign ds = m.dataset %}
{% assign h = m.horizon %}
{% assign h1 = h.y1 %}
{% assign h3 = h.y3 %}
{% assign h5 = h.y5 %}
{% assign h10 = h.y10 %}

## What an investment horizon is

Your **investment horizon** is how long a sum of money can be left
invested before you need it back. Money for next year's fees has a one-year horizon.
Money for a retirement twenty years away has a long one, even if some of it
will be spent earlier.

The horizon matters because an asset's risk looks different depending on how
long it's held. A single bad year is common for some assets; a bad decade
is much rarer. This post measures one side of risk, how often an asset lost
money, on Indian data, using the same four
series as the [asset classes post]({% post_url 2027-01-21-asset-classes %}),
part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

## The method

Instead of one start date, we use every start date. For each trading day
from {{ h1.first_start }}, we look at what the asset returned over the next
1, 3, 5 and 10 years, a method the [rolling returns post]({% post_url 2026-09-27-rolling-returns %})
explains:

```
Window return, a year  =  (value n years later / value at start) ^ (1 / n)  −  1

Share of windows that lost money  =  windows with a return below 0  /  all windows
```

A window counts only if its full n years fit inside the data, which
ends on {{ ds.end }}. So the last 10-year window starts on
{{ h10.last_start }}; later start dates are dropped because their 10 years
haven't finished. That's why the longer horizons have fewer windows.

The four series are the Nifty 50 TRI (Total Returns Index, dividends
reinvested) for equity, and three funds' NAVs (net asset values) from UTI
Mutual Fund, via
AMFI (the Association of Mutual Funds in India): the Gilt Fund for government
bonds, the Liquid Fund for cash-like money and the Gold ETF
(exchange-traded fund). Sources and the gold ETF's unit-split adjustment are
in the [asset classes post]({% post_url 2027-01-21-asset-classes %}). The
bond and cash-like series are regular plans net of their costs and the index
has none, so the equity-versus-cash comparisons below lean towards equity.
Past data, {{ ds.start }} to {{ ds.end }}, pre-tax, for illustration only.

## Worked example: every window, four assets

### How often each one lost money

| Horizon | Windows | Equity | Gov. bonds | Cash-like | Gold |
|---|---:|---:|---:|---:|---:|
| 1 year | {{ h1.windows }} | {{ h1.equity.neg_pct | replace: "-", "−" }}% | {{ h1.gilt.neg_pct | replace: "-", "−" }}% | {{ h1.liquid.neg_pct | replace: "-", "−" }}% | {{ h1.gold.neg_pct | replace: "-", "−" }}% |
| 3 years | {{ h3.windows }} | {{ h3.equity.neg_pct | replace: "-", "−" }}% | {{ h3.gilt.neg_pct | replace: "-", "−" }}% | {{ h3.liquid.neg_pct | replace: "-", "−" }}% | {{ h3.gold.neg_pct | replace: "-", "−" }}% |
| 5 years | {{ h5.windows }} | {{ h5.equity.neg_pct | replace: "-", "−" }}% | {{ h5.gilt.neg_pct | replace: "-", "−" }}% | {{ h5.liquid.neg_pct | replace: "-", "−" }}% | {{ h5.gold.neg_pct | replace: "-", "−" }}% |
| 10 years | {{ h10.windows }} | {{ h10.equity.neg_pct | replace: "-", "−" }}% | {{ h10.gilt.neg_pct | replace: "-", "−" }}% | {{ h10.liquid.neg_pct | replace: "-", "−" }}% | {{ h10.gold.neg_pct | replace: "-", "−" }}% |

### The worst, middle and best window, a year

| Horizon | Equity: worst / median / best | Gov. bonds | Cash-like | Gold |
|---|---|---|---|---|
{% assign hkeys = "y1,y3,y5,y10" | split: "," -%}
{% for k in hkeys -%}
{% assign r = h[k] -%}
| {{ k | remove: "y" }} yr | {{ r.equity.worst_pct | replace: "-", "−" }}% / {{ r.equity.median_pct | replace: "-", "−" }}% / {{ r.equity.best_pct | replace: "-", "−" }}% | {{ r.gilt.worst_pct | replace: "-", "−" }}% / {{ r.gilt.median_pct | replace: "-", "−" }}% / {{ r.gilt.best_pct | replace: "-", "−" }}% | {{ r.liquid.worst_pct | replace: "-", "−" }}% / {{ r.liquid.median_pct | replace: "-", "−" }}% / {{ r.liquid.best_pct | replace: "-", "−" }}% | {{ r.gold.worst_pct | replace: "-", "−" }}% / {{ r.gold.median_pct | replace: "-", "−" }}% / {{ r.gold.best_pct | replace: "-", "−" }}% |
{% endfor %}

### How often equity and gold trailed cash

| Horizon | Equity below cash-like | Gold below cash-like |
|---|---:|---:|
| 1 year | {{ h1.equity_below_liquid_pct | replace: "-", "−" }}% | {{ h1.gold_below_liquid_pct | replace: "-", "−" }}% |
| 3 years | {{ h3.equity_below_liquid_pct | replace: "-", "−" }}% | {{ h3.gold_below_liquid_pct | replace: "-", "−" }}% |
| 5 years | {{ h5.equity_below_liquid_pct | replace: "-", "−" }}% | {{ h5.gold_below_liquid_pct | replace: "-", "−" }}% |
| 10 years | {{ h10.equity_below_liquid_pct | replace: "-", "−" }}% | {{ h10.gold_below_liquid_pct | replace: "-", "−" }}% |

### What the tables show

1. **Equity's loss rate fell sharply with time.** {{ h1.equity.neg_pct | replace: "-", "−" }}%
   of 1-year windows lost money, {{ h3.equity.neg_pct | replace: "-", "−" }}% of 3-year windows,
   and none of the 10-year windows. The worst 1-year window was
   {{ h1.equity.worst_pct | replace: "-", "−" }}%; the worst 10-year window still grew
   {{ h10.equity.worst_pct | replace: "-", "−" }}% a year.
2. **Gold's did not fall as fast.** {{ h3.gold.neg_pct | replace: "-", "−" }}% of its 3-year
   windows and {{ h5.gold.neg_pct | replace: "-", "−" }}% of its 5-year windows lost money,
   against {{ h3.equity.neg_pct | replace: "-", "−" }}% and {{ h5.equity.neg_pct | replace: "-", "−" }}% for equity.
   And it trailed cash-like money in {{ h10.gold_below_liquid_pct | replace: "-", "−" }}% of
   10-year windows, about as often as in 1-year windows.
3. **A positive window isn't the same as a good one.** Equity beat cash-like
   money in most long windows, but not all: it trailed in
   {{ h10.equity_below_liquid_pct | replace: "-", "−" }}% of 10-year windows. A longer horizon
   narrowed the range of yearly returns; it didn't remove the bottom of it.
4. **Bonds and cash rarely lost money at any horizon here,** but their
   middle outcomes were lower too. The horizon question for them is mostly
   about inflation, not losses.

So a horizon is a property of the money, not of the asset. The same equity
index was riskier for a 1-year goal than for a 10-year one in this data,
because of how often its short windows went negative.

## Common mistakes

1. **Reading the percentages as odds for the future.** These are counts of
   what happened in one period of Indian history, {{ ds.start }} to
   {{ ds.end }}. A future decade can be worse than any window in the table.
2. **Treating the windows as independent.** Neighbouring windows share almost
   all of their days, so the 10-year column's windows contain far fewer
   separate experiences than their count suggests. The 10-year windows here all
   start between {{ h10.first_start }} and {{ h10.last_start }}, so any two
   of them share at least two years.
3. **Giving all your money one horizon.** A household usually has several:
   an [emergency fund]({% post_url 2026-12-23-emergency-fund-sizing %}) needed
   any day, a goal in five years, retirement in twenty. Each sum has its own.
4. **Forgetting that the horizon shrinks.** Money for a goal ten years away
   becomes money for a goal one year away. What suited it at the start may
   not suit it at the end; the glide path post later in this series covers
   that shift.

**Takeaway:** The same asset can be risky for short money and much less so
for long money, because short windows go negative far more often than long
ones. That's why each sum's horizon is worth thinking about separately, and
why a long horizon narrows the range of yearly returns without promising any of them.
