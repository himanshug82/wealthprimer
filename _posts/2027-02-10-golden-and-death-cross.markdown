---
layout: post
title: "Golden cross and death cross: what the Nifty did next"
seo_title: "Golden cross and death cross, tested on the Nifty"
description: "A golden cross is the 50-day average rising above the 200-day. We tested every golden and death cross on 18 years of Nifty data against the base rate."
image: /assets/og/golden-and-death-cross.png
date: 2027-02-10 09:00:00 +0530
series: technical-analysis
term: "Golden cross and death cross"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign g = t4.golden_cross %}
{% assign base = t4.base_rate %}

## What are a golden cross and a death cross?

A **golden cross** happens when a short-term moving average rises above a long-term one. The usual pair is the {{ g.fast }}-day and {{ g.slow }}-day SMA ([simple moving average]({% post_url 2026-10-06-moving-averages %})). A **death cross** is the mirror image: the {{ g.fast }}-day average falls below the {{ g.slow }}-day. Headlines like to announce them as signals. This post asks the question the headlines skip: what happened *after* each one, compared with what happens after an ordinary day?

It follows the method from the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}): a fixed forward horizon, a base rate, and every event reported. It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

```
SMA(n)        = average of the last n closing prices
Golden cross  = day when SMA(50) moves from at-or-below to above SMA(200)
Death cross   = day when SMA(50) moves from at-or-above to below SMA(200)

Outcome       = Close(t + 63 sessions) / Close(t) − 1      (63 sessions ≈ 3 months)
Base rate     = the same outcome measured from every day
```

## The test

The data is the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}). It is a price index, so dividends are left out. A 200-day average needs 200 days of history, so the first usable day is {{ g.first_valid_day | date: "%-d %B %Y" }}. Parameters were fixed before looking: 50 and 200, no other pairs tried.

| After… | Crosses | With a full 63-session window | Average next-63-session change | Median | Share higher |
|---|---:|---:|---:|---:|---:|
| Golden cross | {{ g.golden.events }} | {{ g.golden.n }} | {{ g.golden.avg_pct }}% | {{ g.golden.median_pct }}% | {{ g.golden.share_positive_pct }}% |
| Death cross | {{ g.death.events }} | {{ g.death.n }} | {{ g.death.avg_pct }}% | {{ g.death.median_pct }}% | {{ g.death.share_positive_pct }}% |
| **Every day (base rate)** | | {{ base.n }} | {{ base.avg_pct }}% | {{ base.median_pct }}% | {{ base.share_positive_pct }}% |

{{ g.death.dropped_no_window }} death cross (the most recent, {{ g.last_death | date: "%-d %B %Y" }}) was dropped because 63 sessions had not passed before the data ends. The Nifty's golden crosses ran from {{ g.first_golden | date: "%-d %B %Y" }} to {{ g.last_golden | date: "%-d %B %Y" }}.

Three things to notice:

1. **Both signals were followed by gains on average.** The death cross was followed by a *larger* average gain than the golden cross, which is the opposite of the headline. A death cross arrives after a fall, so one possible reading is that falls were often followed by rebounds in this sample. With this few events we can't tell that from chance.
2. **Neither is far from the base rate.** The base rate across every day is {{ base.avg_pct }}%, because the index rose over the period. A signal needs to beat that, not zero.
3. **The sample is tiny.** {{ g.golden.n }} golden crosses and {{ g.death.n }} death crosses, each its own episode. A change of one or two events moves the averages a lot.

## The whipsaw problem

A moving-average cross is a lagging event by construction. Across the {{ g.all_crosses }} crosses of either kind, {{ g.reversed_within_63 }} were undone by an opposite cross within 63 sessions ({{ g.reversed_share_pct }}% of the gaps between consecutive crosses). Someone acting on each cross would have bought and sold on a signal that reversed inside a quarter.

## What if you traded the rule?

As an illustration, not a recommendation: hold the index while the 50-day is above the 200-day, sit in cash otherwise (assumed to earn nothing), trade at the next session's close, and pay 0.1% a side. Over {{ g.strategy.years }} years from {{ g.first_valid_day | date: "%-d %B %Y" }}:

| | Rule | Buy and hold |
|---|---:|---:|
| Compound annual growth rate (CAGR) | {{ g.strategy.strategy_cagr_pct }}% | {{ g.strategy.buy_hold_cagr_pct }}% |
{% assign d1 = g.strategy.strategy_max_drawdown_pct %}{% assign d2 = g.strategy.buy_hold_max_drawdown_pct %}| Deepest fall from a peak | {% include inr.html n=d1 %}% | {% include inr.html n=d2 %}% |
| Share of time invested | {{ g.strategy.share_time_invested_pct }}% | 100% |
| Trades | {{ g.strategy.trades }} | 0 |

The rule spent about {{ g.strategy.share_time_invested_pct }}% of the time invested and earned a lower CAGR. Its deepest fall was only slightly smaller than buy-and-hold's. Two assumptions matter: cash earning nothing penalises the rule, and ignoring dividends understates both lines. The point is narrower: on this index, the cross did not deliver a clear advantage after costs.

## Common mistakes

- **Treating the name as evidence.** "Golden" and "death" are branding. The only thing that matters is what happened afterwards, and here the "death" cross was followed by the better average.
- **Ignoring the base rate.** Roughly {{ base.share_positive_pct }}% of all 63-session windows ended higher. A signal that is "right" {{ g.golden.share_positive_pct }}% of the time is not far from "any day".
- **Counting 12 events as a pattern.** Each cross is a separate market episode. Twelve data points can show you a story and can't show you a rule.
- **Forgetting it is a lagging indicator.** An average of 200 days moves slowly, so a cross confirms a change that is already well under way.

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
fast, slow = s.rolling(50).mean(), s.rolling(200).mean()
above = fast > slow
valid = slow.notna()
golden = valid & above & ~above.shift(fill_value=False)
fwd = s.shift(-63) / s - 1                    # NaN where the window is incomplete
print(fwd[golden].dropna().describe().round(3))
print("base rate:", fwd.dropna().mean().round(3))
```

The `valid` mask is there so that the first day the 200-day average exists isn't counted as a "cross".

**Takeaway:** On 18 years of the Nifty, golden and death crosses were both followed by gains on average, with the death cross followed by the bigger one, and neither stood clear of the base rate on so few events. Treat a moving-average cross as a description of the past, not a forecast.
