---
layout: post
title: "ADX explained: how strong is the trend, not which way"
seo_title: "ADX (average directional index) explained"
description: "ADX measures how strong a trend is, not which way it points. How +DI and −DI build it, and what 435 days of Britannia show about ADX bands and later moves."
image: /assets/og/adx-trend-strength.png
date: 2027-01-29 09:00:00 +0530
series: technical-analysis
term: "ADX (average directional index)"
---

{% assign t4 = site.data.ta4 %}
{% assign ds = t4.dataset %}
{% assign ax = t4.adx %}

## What does ADX measure?

The **ADX (average directional index)** is a number between 0 and 100 that says how strongly a price has been trending over roughly the last few weeks, whichever way it has been going. A high ADX means the recent moves were mostly in one direction. A low ADX means the price has been wandering sideways. It does **not** say whether the trend is up or down, and it does not say what comes next.

J. Welles Wilder Jr. introduced it in his 1978 book *New Concepts in Technical Trading Systems*, alongside the RSI ([relative strength index]({% post_url 2026-10-08-rsi %})) and the ATR ([average true range]({% post_url 2026-10-12-bollinger-bands-and-atr %})). All three use the same smoothing, so if you have read those posts, the arithmetic here will feel familiar. This post is part of the [Technical Analysis]({{ '/series/technical-analysis/' | relative_url }}) series.

## The formula

ADX is built in four steps from each day's high, low and close:

```
Up move    = today's high − yesterday's high
Down move  = yesterday's low − today's low
+DM = Up move    if Up move > Down move and Up move > 0, else 0
−DM = Down move  if Down move > Up move and Down move > 0, else 0

+DI = 100 × Wilder average of +DM (14 days) / ATR (14 days)
−DI = 100 × Wilder average of −DM (14 days) / ATR (14 days)

DX  = 100 × |+DI − −DI| / (+DI + −DI)
ADX = Wilder average of DX (14 days)
```

"DI" is directional indicator and "DM" is directional movement. "Wilder average" is the exponential smoothing with α = 1/14 used in the RSI post. The two DIs say how much of the recent range was upward or downward push. DX says how lopsided they are. ADX smooths DX, which is why it moves slowly and only gets going about {{ ax.warmup_dropped }} bars after the start of the data (we drop those).

## Worked example: three days of Britannia's chart

Britannia Industries (NSE: BRITANNIA), daily bars from {{ ds.stock_start | date: "%-d %B %Y" }} to {{ ds.stock_end | date: "%-d %B %Y" }} ({{ ds.stock_bars }} bars), from [Yahoo Finance]({{ ds.stock_source_url }}). This is one stock over two years, used to show how the indicator behaves. It is not a test of anything, and it is historical data for illustration only. Here are the days with the lowest, middle and highest ADX once it had settled:

| | Lowest ADX | Middle ADX | Highest ADX |
|---|---:|---:|---:|
| Date | {{ ax.worked[0].date }} | {{ ax.worked[2].date }} | {{ ax.worked[1].date }} |
| Close (₹) | {{ ax.worked[0].close }} | {{ ax.worked[2].close }} | {{ ax.worked[1].close }} |
| +DI | {{ ax.worked[0].plus_di }} | {{ ax.worked[2].plus_di }} | {{ ax.worked[1].plus_di }} |
| −DI | {{ ax.worked[0].minus_di }} | {{ ax.worked[2].minus_di }} | {{ ax.worked[1].minus_di }} |
| **ADX** | **{{ ax.worked[0].adx }}** | **{{ ax.worked[2].adx }}** | **{{ ax.worked[1].adx }}** |

Read the columns, not the dates. On the lowest-ADX day the two DIs were almost equal ({{ ax.worked[0].plus_di }} and {{ ax.worked[0].minus_di }}): upward and downward pushes cancelled, so ADX was {{ ax.worked[0].adx }}. On the highest-ADX day +DI ({{ ax.worked[1].plus_di }}) was far above −DI ({{ ax.worked[1].minus_di }}): one-sided, so ADX was {{ ax.worked[1].adx }}. On the middle day −DI was well above +DI, yet ADX was {{ ax.worked[2].adx }}, the same side of the coin: ADX would read similarly for a falling trend as for a rising one. The direction is in which DI is higher, not in the ADX.

Across the {{ ax.bars_used }} usable bars the ADX ranged from {{ ax.adx_min }} to {{ ax.adx_max }}.

## Does a high ADX say anything about what happens next?

The conventional reading is "above 25 means a trend worth following, below 20 means no trend". Those cut-offs are conventions, not laws, so the table shows all three bands and not a favourite. For each day we measured the size of the move over the **next {{ ax.horizon_sessions }} sessions**, up or down, and the share of those windows that ended higher. {{ ax.windows_dropped_no_forward }} days at the end of the data had no full window and were dropped.

| ADX band | Days with a full window | Average size of next-{{ ax.horizon_sessions }}-session move | Share ending higher |
|---|---:|---:|---:|
{% for b in ax.bands %}| {{ b.band }} | {{ b.n }} | {{ b.avg_abs_move_pct }}% | {{ b.share_up_pct }}% |
{% endfor %}| **All days (base rate)** | {{ ax.all.n }} | {{ ax.all.avg_abs_move_pct }}% | {{ ax.all.share_up_pct }}% |

ADX of 25 or more covered {{ ax.share_days_adx_25_plus_pct }}% of days. The band that was supposed to mean "strong trend" was followed by the **smallest** average move, not the largest. That is not surprising once you remember what ADX is: it summarises the trend that has *already* happened. It can be high at the end of a long run, just before the run stalls.

The direction signal fares no better. When +DI was above −DI, {{ ax.di_up.share_up_pct }}% of the next windows ended higher ({{ ax.di_up.n }} days). When −DI was above +DI, {{ ax.di_down.share_up_pct }}% did ({{ ax.di_down.n }} days). If anything the "down" side was higher, which is the opposite of what the indicator implies. With one stock and two years, we would not read anything into that either way.

## Common mistakes

- **Reading ADX as direction.** A rising ADX in a falling market is a strengthening *downtrend*. Check +DI and −DI to see which side is driving it.
- **Treating 25 as a threshold that triggers something.** It is a convention from a 1978 book. The table above shows how little the bands separated outcomes here. If an article says "above 25, trade the trend", ask for the base rate.
- **Expecting it to lead.** ADX is a smoothed average of smoothed numbers, so it confirms after the fact. A reading of 40 describes the past weeks, not the coming ones.
- **Generalising from a short sample.** {{ ax.bars_used }} bars of one stock is a handful of trending and non-trending stretches. Nothing in this post shows what ADX does on other stocks or in other years.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")
up, dn = df.high.diff(), -df.low.diff()
plus_dm = up.where((up > dn) & (up > 0), 0.0)
minus_dm = dn.where((dn > up) & (dn > 0), 0.0)
prev = df.close.shift()
tr = pd.concat([df.high - df.low, (df.high - prev).abs(),
                (df.low - prev).abs()], axis=1).max(axis=1)

w = lambda s: s.ewm(alpha=1/14, adjust=False).mean()    # Wilder smoothing
atr = w(tr)
pdi, mdi = 100 * w(plus_dm) / atr, 100 * w(minus_dm) / atr
adx = w(100 * (pdi - mdi).abs() / (pdi + mdi))
print(adx.iloc[60:].describe().round(1))                # skip the warm-up
```

**Takeaway:** ADX tells you how one-sided the recent price action has been, not which way it will go next. On two years of Britannia, days with ADX of 25 or more were followed by the smallest average moves of the three bands, so treat it as a description of the past weeks.
