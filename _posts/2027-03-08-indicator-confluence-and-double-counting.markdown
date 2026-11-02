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
{% assign base = cf.base_common %}
{% assign ts = cf.tests %}

## What is confluence, and what is redundancy?

**Confluence** is chart-reading jargon for several indicators pointing the same way at the same time. "RSI (relative strength index) is oversold, the price is below the lower Bollinger Band and the momentum is negative" sounds like three independent witnesses. **Indicator redundancy** is the problem with that: if the three are all computed from the same closing prices, they are three views of the same fact, and agreement between them is closer to one witness repeating themselves.

This post measures how much of each indicator is shared, and then checks whether stacking them changed what followed. It uses the [RSI (relative strength index)]({% post_url 2026-10-08-rsi %}), the [MACD (moving average convergence divergence)]({% post_url 2026-10-09-macd %}) and the [Bollinger Bands]({% post_url 2026-10-12-bollinger-bands-and-atr %}), and the fixed-horizon method from the [backtesting post]({% post_url 2026-10-15-how-to-backtest-honestly %}). It is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

Four numbers computed daily from closing prices, plus the outcome:

```
RSI(14)      = relative strength index, Wilder smoothing
MACD hist    = (EMA12 − EMA26) − 9-day EMA of (EMA12 − EMA26)
%B           = (Close − lower band) / (upper band − lower band)       (20-day, 2 standard deviations)
20-day move  = Close(t) / Close(t − 20) − 1

Oversold-type conditions (conventions, not tuned; C was first written with a full-sample cut-off, reported below):
  A: RSI(14) < 30
  B: Close below the lower Bollinger Band  (%B < 0)
  C: 20-day move in the worst tenth of earlier days (needs at least a year
     of history, and uses nothing from that day or later)

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

RSI and %B are close relatives: a correlation of {{ cf.corr_rsi_pctb }} means they move almost together across all days. Their extremes overlap less. Of the {{ cf.overlap.rsi_days }} days when RSI was below 30, {{ cf.overlap.rsi_and_band_pct }}% also had the close under the lower band; of the {{ cf.overlap.band_days }} days under the band, {{ cf.overlap.band_and_rsi_pct }}% also had RSI under 30. That's far more than chance, but of the {{ cf.overlap.either_days }} days when at least one held, both held on only {{ cf.overlap.both_days }} ({{ cf.overlap.both_share_of_either_pct }}%). So the second one adds much less than an independent witness would, not nothing.

## Does stacking them change what followed?

Each row is a condition, the number of days it held, and the 63-session outcome, with the base rate from every day at the bottom. All rows run from {{ cf.common_start | date: "%-d %B %Y" }}, the first day condition C can exist, so they cover the same period. That leaves out most of the 2008 fall: before that date, A's {{ cf.before_common_start.rsi_below_30.n }} days averaged {% assign x = cf.before_common_start.rsi_below_30.avg_pct %}{% include inr.html n=x %}% and B's {{ cf.before_common_start.below_lower_band.n }} days {% assign x = cf.before_common_start.below_lower_band.avg_pct %}{% include inr.html n=x %}%. "Separate episodes" counts days at least 63 sessions apart.

| Condition | Days | With a 63-session window | Average next-63-session change | Median | Share higher | Separate episodes |
|---|---:|---:|---:|---:|---:|---:|
| A: RSI below 30 | {{ ts.rsi_below_30.events }} | {{ ts.rsi_below_30.n }} | {{ ts.rsi_below_30.avg_pct }}% | {{ ts.rsi_below_30.median_pct }}% | {{ ts.rsi_below_30.share_positive_pct }}% | {{ ts.rsi_below_30.episodes }} |
| B: below lower band | {{ ts.below_lower_band.events }} | {{ ts.below_lower_band.n }} | {{ ts.below_lower_band.avg_pct }}% | {{ ts.below_lower_band.median_pct }}% | {{ ts.below_lower_band.share_positive_pct }}% | {{ ts.below_lower_band.episodes }} |
| C: worst tenth of 20-day moves, using earlier days only | {{ ts.worst_tenth_20d.events }} | {{ ts.worst_tenth_20d.n }} | {{ ts.worst_tenth_20d.avg_pct }}% | {{ ts.worst_tenth_20d.median_pct }}% | {{ ts.worst_tenth_20d.share_positive_pct }}% | {{ ts.worst_tenth_20d.episodes }} |
| At least two of A, B, C | {{ ts.at_least_2.events }} | {{ ts.at_least_2.n }} | {{ ts.at_least_2.avg_pct }}% | {{ ts.at_least_2.median_pct }}% | {{ ts.at_least_2.share_positive_pct }}% | {{ ts.at_least_2.episodes }} |
| All three | {{ ts.all_3.events }} | {{ ts.all_3.n }} | {{ ts.all_3.avg_pct }}% | {{ ts.all_3.median_pct }}% | {{ ts.all_3.share_positive_pct }}% | {{ ts.all_3.episodes }} |
| **Every day (base rate)** | | {{ base.n }} | {{ base.avg_pct }}% | {{ base.median_pct }}% | {{ base.share_positive_pct }}% | |

The conditions were followed by an average above the base rate. Stacking fell between the single conditions: the average with all three ({{ ts.all_3.avg_pct }}%) beats A ({{ ts.rsi_below_30.avg_pct }}%) and B ({{ ts.below_lower_band.avg_pct }}%) but not C ({{ ts.worst_tenth_20d.avg_pct }}%), and its share ending higher ({{ ts.all_3.share_positive_pct }}%) is below A's ({{ ts.rsi_below_30.share_positive_pct }}%) and C's ({{ ts.worst_tenth_20d.share_positive_pct }}%). Meanwhile the evidence shrinks: "all three" rests on {{ ts.all_3.episodes }} separate episodes.

The period matters more than the setting. C held on just {{ ts.worst_tenth_20d.events }} days, because the 2008 fall set a low bar early on (the cut-off was {% assign x = cf.trailing_cutoff_end_2008_pct %}{% include inr.html n=x %}% at the end of 2008). A full-sample cut-off of {% assign x = cf.worst_tenth_cutoff_hindsight_pct %}{% include inr.html n=x %}%, which needs hindsight, holds on {{ cf.tests_hindsight.worst_tenth_20d.events }} days, {{ cf.hindsight_days_before_start }} of them before the start date. With it, all-three averaged {{ cf.hindsight_all3_after_start.avg_pct }}% from the start date, close to the {{ ts.all_3.avg_pct }}% above, but {% assign x = cf.hindsight_all3_before_start.avg_pct %}{% include inr.html n=x %}% on the {{ cf.hindsight_all3_before_start.n }} days before it. Whether these signals look good depends heavily on whether the 2008 fall is in the sample.

Two limits. Days with at least two conditions spanned {{ cf.at_least_2_years_spanned }} calendar years, but {{ cf.at_least_2_top3_share_pct }}% of them fell in just three ({{ cf.at_least_2_top3_years | join: ", " }}), so these numbers lean on a few market-wide falls. And the table says nothing about acting on any of this: it shows that agreement between price-derived indicators is easy to get and that it did not clearly add information here.

## Common mistakes

- **Counting agreement between related indicators as independent confirmation.** RSI, Bollinger %B and the recent price change are built from the same closes. In our view, more independence needs a different type of information, such as [volume]({% post_url 2026-10-07-volume %}) or a different asset.
- **Adding filters until the history looks clean.** Every added condition shrinks the sample. Fewer events with a prettier average is a warning sign, not a feature.
- **Reporting the average without the number of episodes.** {{ ts.at_least_2.n }} days with two or more conditions come from {{ ts.at_least_2.episodes }} episodes, and {{ ts.all_3.n }} days with all three from {{ ts.all_3.episodes }}.
- **Skipping the base rate.** If most 63-session windows end higher anyway ({{ base.share_positive_pct }}% here), a signal "followed by a gain" has to be compared with that.

## Doing it in Python

The data is [this CSV]({{ ds.index_csv_path | relative_url }}). Historical data, for illustration only.

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

cut = x.roc20.expanding(252).quantile(0.10).shift(1)   # earlier days only
a, b, c = x.rsi < 30, x.pctb < 0, x.roc20 < cut
keep = cut.notna()                                     # same start for every row
fwd = (s.shift(-63) / s - 1).reindex(x.index)
for name, m in [("A", a & keep), ("A+B+C", a & b & c & keep)]:
    print(name, m.sum(), fwd[m].dropna().mean().round(3))
```

**Takeaway:** Indicators computed from the same closing prices tend to say the same thing, so their agreement is closer to one witness than three. On {{ ds.index_years }} years of Nifty data, stacking oversold signals fell between the single signals, shrank the number of independent episodes, and looked much worse once the 2008 fall was included.
