---
layout: post
title: "Stacking indicators: confluence or double counting?"
seo_title: "Indicator confluence: do more signals add information?"
description: "RSI, Bollinger %B and a falling price all say 'oversold'. We checked how correlated they are on 18 years of Nifty data and what stacking them changed."
image: /assets/og/indicator-confluence-and-double-counting.png
date: 2027-03-08 09:00:00 +0530
series: technical-analysis
term: "Indicator redundancy (confluence)"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign cf = t4.confluence %}
{% assign base = t4.base_rate %}
{% assign ts = cf.tests %}

## What is confluence, and what is redundancy?

**Confluence** is chart-reading jargon for several indicators pointing the same way at the same time. "RSI is oversold, the price is below the lower Bollinger Band and the momentum is negative" sounds like three independent witnesses. **Indicator redundancy** is the problem with that: if the three are all computed from the same closing prices, they are three views of the same fact, and agreement between them is closer to one witness repeating themselves.

This post measures how much of each indicator is shared, and then checks whether stacking them changed what followed. It uses the [RSI]({% post_url 2026-10-08-rsi %}), the [MACD]({% post_url 2026-10-09-macd %}) and the [Bollinger Bands]({% post_url 2026-10-12-bollinger-bands-and-atr %}), and the fixed-horizon method from the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}). It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

Four numbers computed daily from closing prices, plus the outcome:

```
RSI(14)      = relative strength index, Wilder smoothing
MACD hist    = (EMA12 − EMA26) − 9-day EMA of (EMA12 − EMA26)
%B           = (Close − lower band) / (upper band − lower band)       (20-day, 2 standard deviations)
20-day move  = Close(t) / Close(t − 20) − 1

Oversold-type conditions, fixed in advance:
  A: RSI(14) < 30
  B: Close below the lower Bollinger Band  (%B < 0)
  C: 20-day move in the worst tenth of all days

Outcome = Close(t + 63 sessions) / Close(t) − 1
```

EMA is an exponential moving average. The data is the Nifty 50 price index, {{ ds.index_start | date: "%-d %B %Y" }} to {{ ds.index_end | date: "%-d %B %Y" }}, from [Yahoo Finance]({{ ds.index_source_url }}); price index, so dividends are left out. The first {{ cf.warmup_dropped }} days are dropped while the indicators warm up, leaving {{ cf.days }} days.

## How much do they overlap?

If two indicators were independent, their correlation would be near 0. If one were a copy of the other, it would be 1.

| Pair | Correlation |
|---|---:|
| RSI and %B | {{ cf.corr_rsi_pctb }} |
| RSI and the 20-day move | {{ cf.corr_rsi_roc20 }} |
| %B and the 20-day move | {{ cf.corr_pctb_roc20 }} |
| %B and the MACD histogram | {{ cf.corr_pctb_macdhist }} |
| RSI and the MACD histogram | {{ cf.corr_rsi_macdhist }} |

RSI and %B are close to the same thing: a correlation of {{ cf.corr_rsi_pctb }} means they move almost together. Of the {{ cf.overlap.rsi_days }} days when RSI was below 30, {{ cf.overlap.rsi_and_band_pct }}% also had the close under the lower band; of the {{ cf.overlap.band_days }} days under the band, {{ cf.overlap.band_and_rsi_pct }}% also had RSI under 30. So when both say "oversold", you have learned much less than when one does.

## Does stacking them change what followed?

Each row is a condition, the number of days it held, and the 63-session outcome, with the base rate from every day at the bottom. "Separate episodes" counts days at least 63 sessions apart.

| Condition | Days | With a 63-session window | Average next-63-session change | Median | Share higher | Separate episodes |
|---|---:|---:|---:|---:|---:|---:|
| A: RSI below 30 | {{ ts.rsi_below_30.events }} | {{ ts.rsi_below_30.n }} | {{ ts.rsi_below_30.avg_pct }}% | {{ ts.rsi_below_30.median_pct }}% | {{ ts.rsi_below_30.share_positive_pct }}% | {{ ts.rsi_below_30.episodes }} |
| B: below lower band | {{ ts.below_lower_band.events }} | {{ ts.below_lower_band.n }} | {{ ts.below_lower_band.avg_pct }}% | {{ ts.below_lower_band.median_pct }}% | {{ ts.below_lower_band.share_positive_pct }}% | {{ ts.below_lower_band.episodes }} |
| C: worst tenth of 20-day moves (below {{ cf.worst_tenth_cutoff_pct }}%) | {{ ts.worst_tenth_20d.events }} | {{ ts.worst_tenth_20d.n }} | {{ ts.worst_tenth_20d.avg_pct }}% | {{ ts.worst_tenth_20d.median_pct }}% | {{ ts.worst_tenth_20d.share_positive_pct }}% | {{ ts.worst_tenth_20d.episodes }} |
| At least two of A, B, C | {{ ts.at_least_2.events }} | {{ ts.at_least_2.n }} | {{ ts.at_least_2.avg_pct }}% | {{ ts.at_least_2.median_pct }}% | {{ ts.at_least_2.share_positive_pct }}% | {{ ts.at_least_2.episodes }} |
| All three | {{ ts.all_3.events }} | {{ ts.all_3.n }} | {{ ts.all_3.avg_pct }}% | {{ ts.all_3.median_pct }}% | {{ ts.all_3.share_positive_pct }}% | {{ ts.all_3.episodes }} |
| **Every day (base rate)** | | {{ base.n }} | {{ base.avg_pct }}% | {{ base.median_pct }}% | {{ base.share_positive_pct }}% | |

The conditions were followed by an average above the base rate, but stacking added nothing in a consistent direction. The average with all three ({{ ts.all_3.avg_pct }}%) is not higher than with RSI alone ({{ ts.rsi_below_30.avg_pct }}%), and the share ending higher with two or more ({{ ts.at_least_2.share_positive_pct }}%) is lower than with RSI alone ({{ ts.rsi_below_30.share_positive_pct }}%). Meanwhile the evidence shrinks: "all three" rests on {{ ts.all_3.episodes }} separate episodes.

Two honest limits. Those episodes are dominated by a few market-wide falls, so these numbers describe what followed a handful of crashes, not many independent dips. And the table says nothing about acting on any of this: it shows that agreement between price-derived indicators is easy to get and that it did not clearly add information here.

## Common mistakes

- **Counting agreement between related indicators as independent confirmation.** RSI, Bollinger %B and the recent price change are built from the same closes. Real independence needs a different type of information, such as [volume]({% post_url 2026-10-07-volume %}) or a different asset.
- **Adding filters until the history looks clean.** Every added condition shrinks the sample. Fewer events with a prettier average is a warning sign, not a feature.
- **Reporting the average without the number of episodes.** {{ ts.all_3.n }} days seem like a lot, but they come from {{ ts.all_3.episodes }} episodes.
- **Skipping the base rate.** If most 63-session windows end higher anyway ({{ base.share_positive_pct }}% here), a signal "followed by a gain" has to be compared with that.

## Doing it in Python

```python
import pandas as pd

s = pd.read_csv("nifty50-price-index.csv", parse_dates=["date"]
                ).set_index("date").nifty50_pri_close
w = lambda x: x.ewm(alpha=1/14, adjust=False).mean()
d = s.diff()
rsi = 100 - 100 / (1 + w(d.clip(lower=0)) / w(-d.clip(upper=0)))
ma, sd = s.rolling(20).mean(), s.rolling(20).std()
pctb = (s - (ma - 2 * sd)) / (4 * sd)
roc20 = s.pct_change(20)

x = pd.DataFrame({"rsi": rsi, "pctb": pctb, "roc20": roc20}).iloc[60:]
print(x.corr().round(2))                      # how much do they share?

a, b = x.rsi < 30, x.pctb < 0
c = x.roc20 < x.roc20.quantile(0.10)
fwd = (s.shift(-63) / s - 1).reindex(x.index)
for name, m in [("A", a), ("A+B+C", a & b & c)]:
    print(name, m.sum(), fwd[m].dropna().mean().round(3))
```

**Takeaway:** Indicators computed from the same closing prices tend to say the same thing, so their agreement is closer to one witness than three. On 18 years of Nifty data, stacking oversold signals did not add a consistent edge over the first one and shrank the number of independent episodes.
