---
layout: post
title: "Sortino and information ratio: two Sharpe variants"
description: "Sortino counts only the falls; the information ratio measures against a benchmark, not cash. How each is built, worked on a real index fund and hybrid fund."
image: /assets/og/sortino-and-information-ratio.png
date: 2026-10-28 09:00:00 +0530
series: mutual-funds
term: "Sortino ratio and information ratio"
---

{% assign m = site.data.mf4 %}
{% assign r = m.risk_ratios %}
{% assign ix = r.index_fund_vs_tri %}
{% assign hy = r.hybrid_vs_tri %}
{% assign src = m.sources %}
{% capture ir_ix %}{% include inr.html n=ix.information_ratio %}{% endcapture %}

## Two questions Sharpe can't answer

The [Sharpe ratio]({% post_url 2026-09-30-volatility-and-sharpe %}) divides a fund's return above a risk-free rate by its volatility. It has two well-known blind spots.

First, volatility counts a +15% month and a −15% month the same. Most investors don't feel them the same. The **Sortino ratio** fixes that by counting only the falls.

Second, Sharpe measures return against cash, not against what the fund was supposed to track. The **information ratio** asks a different question: how much did the fund earn above its own benchmark, per unit of wandering away from it?

Both are cousins of Sharpe, not replacements. Each answers a narrower question, and each has its own ways to mislead. This post is part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).

## The Sortino ratio

```
                  Return − Minimum acceptable return (MAR)
Sortino  =  ───────────────────────────────────────────────
                          Downside deviation

Downside deviation = square root of the average of
                     (the shortfall below MAR, squared)
                     over ALL days, counting 0 on days at or above MAR,
                     then × √252 to annualise
```

**MAR** is the minimum acceptable return: the bar below which a day counts as a shortfall. We set it equal to the {{ r.risk_free_pct }}% risk-free rate the Sharpe post used, so the two ratios share a numerator. Other choices (zero, an inflation figure) are common, and they change the answer. **CAGR** below is the compound annual growth rate.

## Worked example: two funds, one window

The same funds as in the [capture ratio post]({% post_url 2026-10-26-up-and-down-capture-ratios %}): {{ src.funds.index_fund.name }} and {{ src.funds.hybrid.name }}, direct growth plans, daily NAVs (net asset values, the price per unit) from the Association of Mutual Funds in India (AMFI) via [mfapi.in](https://api.mfapi.in/mf/{{ src.funds.index_fund.code }}), from {{ ix.start | date: "%-d %B %Y" }} to {{ ix.end | date: "%-d %B %Y" }}. The data is as of {{ ix.end | date: "%-d %B %Y" }}, more than three months before this post; it is historical and shown for illustration only. The yardstick for both is the Nifty 50 **TRI** (total return index, which counts dividends as reinvested) from NSE (the National Stock Exchange) Indices.

| | Index fund | Hybrid fund |
|---|---:|---:|
| CAGR | {{ ix.cagr_pct }}% | {{ hy.cagr_pct }}% |
| Less: MAR (risk-free rate) | {{ r.risk_free_pct }}% | {{ r.risk_free_pct }}% |
| Excess return | {{ ix.cagr_pct | minus: r.risk_free_pct | round: 2 }}% | {{ hy.cagr_pct | minus: r.risk_free_pct | round: 2 }}% |
| Volatility (annualised) | {{ ix.vol_pct }}% | {{ hy.vol_pct }}% |
| **Sharpe** = excess ÷ volatility | **{{ ix.sharpe }}** | **{{ hy.sharpe }}** |
| Downside deviation (annualised) | {{ ix.downside_dev_pct }}% | {{ hy.downside_dev_pct }}% |
| **Sortino** = excess ÷ downside deviation | **{{ ix.sortino }}** | **{{ hy.sortino }}** |

Two things stand out.

Sortino is higher than Sharpe for both funds. That isn't the fund doing better. Downside deviation is smaller than volatility because it ignores the days above the bar, so dividing by it gives a bigger number. A Sortino can't be compared with a Sharpe. Compare Sortino with Sortino, on the same bar and the same dates.

The hybrid fund has the lower volatility ({{ hy.vol_pct }}% against {{ ix.vol_pct }}%), which is what a fund with part of its money outside equities would show. Its Sharpe and Sortino are the higher pair in this window. That describes this window and this mix of assets. It doesn't say which fund is better, and the [point-to-point post]({% post_url 2026-09-26-point-to-point-returns %}) shows how much a different ten years could change it.

### In Python

```python
import pandas as pd, numpy as np

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv", parse_dates=["date"]).set_index("date").nav_direct_growth.dropna()
nav = nav.loc["2016-03-31":"2026-03-30"]
rf = 0.065

daily = nav.pct_change().dropna()
years = (nav.index[-1] - nav.index[0]).days / 365.25
cagr = (nav.iloc[-1] / nav.iloc[0]) ** (1 / years) - 1

mar_d = (1 + rf) ** (1 / 252) - 1                       # the daily equivalent of 6.5% a year
downside = np.sqrt((np.minimum(daily - mar_d, 0) ** 2).mean()) * np.sqrt(252)
print(f"Sortino {(cagr - rf) / downside:.2f}")
```

## The information ratio

```
                  Fund CAGR − Benchmark CAGR       Active return
Information  =  ─────────────────────────────  =  ───────────────
ratio              Tracking error                 Tracking error
```

The top line is the **active return**: how far the fund's growth rate sat from its benchmark's. The bottom line is **tracking error**, the annualised standard deviation of the daily gap between the fund and the benchmark. The [tracking error post]({% post_url 2026-10-04-tracking-error-and-tracking-difference %}) covers it in full. The information ratio is Sharpe with the risk-free rate swapped for the benchmark.

It only makes sense with the right benchmark, and for a fund that is trying to differ from it. Two examples show what happens otherwise.

| Against the Nifty 50 TRI, same window | Index fund | Hybrid fund |
|---|---:|---:|
| Fund CAGR | {{ ix.cagr_pct }}% | {{ hy.cagr_pct }}% |
| Benchmark CAGR | {{ ix.bm_cagr_pct }}% | {{ hy.bm_cagr_pct }}% |
| Active return | {{ ix.active_return_pct }}% | {{ hy.active_return_pct }}% |
| Tracking error | {{ ix.tracking_error_pct }}% | {{ hy.tracking_error_pct }}% |
| **Information ratio** | **{{ ix.information_ratio }}** | **{{ hy.information_ratio }}** |

**The index fund.** Its benchmark is the Nifty 50 TRI, from [NSE Indices]({{ src.tri.url }}). It trails by {{ ix.active_return_pct | abs }} points a year, which is the cost of running the fund, and it wanders from the index by only {{ ix.tracking_error_pct }} points. Dividing a small gap by an even smaller wander gives {{ ir_ix }}, a dramatic number that says nothing about skill. Nobody was trying to beat the index. It's the tracking difference divided by the tracking error, and nothing else.

**The hybrid fund.** The Nifty 50 TRI is not its benchmark, and the fund was never trying to match it. The active return is {{ hy.active_return_pct }} points and the tracking error is {{ hy.tracking_error_pct }} points, so the ratio is {{ hy.information_ratio }}. That reads as "matched the index while wandering a long way from it", and it describes nothing useful. Use the index the fund's own documents name, or don't use the ratio.

## Common mistakes

- **Comparing a Sortino with a Sharpe, or quoting one without its bar.** Different denominators give different scales, and setting MAR to zero instead of {{ r.risk_free_pct }}% changes the Sortino. Compare like with like and quote the bar.
- **Using the information ratio against the wrong benchmark.** The hybrid example above is the standard way to get a meaningless number.
- **Reading a passive fund's information ratio as skill or the lack of it.** It is mostly cost divided by a very small wander. The figure looks large because the denominator is tiny.
- **Trusting one window.** Both ratios here come from one ten-year stretch of daily returns. Another stretch gives other numbers, for the same reason a single Sharpe does.

**Takeaway:** Sortino counts only the falls, and the information ratio measures a fund against its benchmark instead of cash. Both change with the bar, the benchmark and the window, so a quoted number without them tells you very little.
