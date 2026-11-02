---
layout: post
title: "Rebalancing: what the arithmetic does and doesn't give you"
seo_title: "Portfolio rebalancing explained, with 20 years of data"
description: "Rebalancing resets a portfolio to its target mix. What it does to risk and returns, on a 60/40 mix of the Nifty 50 TRI and a gilt fund, over two windows."
image: /assets/og/rebalancing-arithmetic.png
date: 2027-03-02 09:00:00 +0530
series: risk
term: "Rebalancing"
---

{% assign r4 = site.data.risk4 %}
{% assign rb = r4.rebalance %}
{% assign f = rb.full %}
{% assign g = rb.from_2010 %}
{% assign a = rb.arith %}

## What is rebalancing?

A portfolio drifts. If you start with 60% in equity and 40% in bonds and equity rises faster, equity becomes a bigger share than you chose. **Rebalancing** means selling some of what has grown and buying some of what has lagged to return to the original mix. This post shows the arithmetic and a worked history. The 60/40 mix is a convention used to illustrate the mechanics, not a recommended allocation, and nothing here says what mix or schedule anyone should use. It follows [diversification is a correlation problem]({% post_url 2026-10-12-diversification-is-a-correlation-problem %}) and is part of the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series.

## The formula

```
Weight of asset i    =  value of asset i / total portfolio value
Trade to rebalance   =  (target weight − current weight) × total value
                        (positive: buy; negative: sell)
```

A one-step example. Start at 60% equity and 40% gilt. Equity rises {{ a.equity_up_pct }}% and gilt {{ a.gilt_up_pct }}% in a year. The equity weight becomes 60 × 1.{{ a.equity_up_pct }} / (60 × 1.{{ a.equity_up_pct }} + 40 × 1.0{{ a.gilt_up_pct }}) = {{ a.new_equity_weight_pct }}%. To return to 60%, you would sell {{ a.sell_to_reset_pct_of_portfolio }}% of the portfolio's value in equity and put it into gilt. In a single year the drift is small. Its effect builds over years.

## Worked example: 60/40 with the Nifty 50 TRI and a gilt fund

Equity is the Nifty 50 Total Returns Index (TRI, which includes dividends) from [NSE Indices](https://www.niftyindices.com/). The bond leg is the UTI Gilt Fund, regular plan, growth option, NAV (net asset value) from AMFI via mfapi.in. Neither is a recommendation; they are two long public series. Both end 30 March 2026. Past data, for illustration only; fund costs are already in the NAV, and tax and trading costs are ignored. Two rules, both starting at 60/40:

- **Never rebalance:** let the weights drift.
- **Annual rebalance:** at the first trading day of each calendar year, reset to 60/40.

| | {{ f.start | date: "%B %Y" }} to {{ f.end | date: "%B %Y" }} | | {{ g.start | date: "%B %Y" }} to {{ g.end | date: "%B %Y" }} | |
|---|---:|---:|---:|---:|
| | Never | Annual | Never | Annual |
| Compound annual growth rate (CAGR) | {{ f.none.cagr_pct }}% | {{ f.annual.cagr_pct }}% | {{ g.none.cagr_pct }}% | {{ g.annual.cagr_pct }}% |
{% assign d1 = f.none.max_drawdown_pct %}{% assign d2 = f.annual.max_drawdown_pct %}{% assign d3 = g.none.max_drawdown_pct %}{% assign d4 = g.annual.max_drawdown_pct %}| Deepest fall from a peak | {% include inr.html n=d1 %}% | {% include inr.html n=d2 %}% | {% include inr.html n=d3 %}% | {% include inr.html n=d4 %}% |
| Equity share at the end | {{ f.none.end_equity_weight_pct }}% | {{ f.annual.end_equity_weight_pct }}% | {{ g.none.end_equity_weight_pct }}% | {{ g.annual.end_equity_weight_pct }}% |
| ₹100 became | ₹{% assign x = f.none.growth_of_100 %}{% include inr.html n=x %} | ₹{% assign x = f.annual.growth_of_100 %}{% include inr.html n=x %} | ₹{% assign x = g.none.growth_of_100 %}{% include inr.html n=x %} | ₹{% assign x = g.annual.growth_of_100 %}{% include inr.html n=x %} |

For reference, the equity series alone compounded at {{ f.equity_cagr_pct }}% and the gilt fund at {{ f.gilt_cagr_pct }}% over the longer window ({{ g.equity_cagr_pct }}% and {{ g.gilt_cagr_pct }}% from {{ g.start | date: "%B %Y" }}).

Three honest observations:

1. **Drift is real.** Never rebalancing left the portfolio {{ f.none.end_equity_weight_pct }}% in equity by the end of the longer window, a very different risk from the 60% it started with. Across the years the year-end equity weight ranged from {{ f.min_equity_weight_pct }}% to {{ f.max_equity_weight_pct }}% without rebalancing.
2. **Rebalancing mainly changed the risk.** In both windows the deepest fall was smaller for the annually rebalanced version, because it held less equity going into falls.
3. **The return gain depends on the window.** From {{ f.start | date: "%B %Y" }}, annual rebalancing beat never rebalancing by about a percentage point a year. From {{ g.start | date: "%B %Y" }}, the two were within a fraction of a point. The longer window includes 2008, when equity fell and gilts rose. Rebalancing then meant buying equity near the low, and the likeliest reason for the gap is the rebound that followed (we didn't isolate it). That is one episode, and it won't recur on schedule. Don't read the longer-window gap as a property of rebalancing.

## Common mistakes

- **Treating rebalancing as a return booster.** Its main job is to hold the risk you chose. Any return gain here came from a particular stretch of history.
- **Rebalancing too often without counting costs.** This example ignores brokerage, taxes and exit loads. Each sale can trigger tax; the Tax series covers how gains are taxed.
- **Calling a drifted portfolio "the same portfolio".** A 60/40 mix that has drifted to {{ f.none.end_equity_weight_pct }}/{{ f.none.end_equity_weight_pct | minus: 100 | abs }} behaves differently in a fall.
- **Reading one backtest as a rule.** Two windows already disagree on the size of the gap.

## Doing it in Python

```python
import pandas as pd

eq = pd.read_csv("nifty50-tri.csv", parse_dates=["date"]).set_index("date").iloc[:, 0]
gl = pd.read_csv("uti-gilt-fund-nav.csv", parse_dates=["date"]
                 ).set_index("date")["nav_regular_growth"].dropna()
idx = eq.index.intersection(gl.index)
re_, rg = eq.reindex(idx).pct_change().fillna(0), gl.reindex(idx).pct_change().fillna(0)

def run(rebalance, target=0.6):
    we, wg, last, path = target, 1 - target, idx[0].year, []
    for t, a, b in zip(idx, re_, rg):
        if rebalance and t.year != last:            # first session of a new year
            tot = we + wg
            we, wg = tot * target, tot * (1 - target)
        last = t.year
        we, wg = we * (1 + a), wg * (1 + b)
        path.append(we + wg)
    return pd.Series(path, index=idx), we / (we + wg)

for flag in (False, True):
    s, w = run(flag)
    yrs = (idx[-1] - idx[0]).days / 365.25
    print("rebalance" if flag else "never", round(s.iloc[-1] ** (1 / yrs) - 1, 3), round(w, 2))
```

**Takeaway:** Rebalancing resets a portfolio to the risk level you chose after the winners have pulled it away. On a 60/40 Nifty and gilt mix it mainly reduced the depth of the falls, while the return difference depended on which years you looked at.
