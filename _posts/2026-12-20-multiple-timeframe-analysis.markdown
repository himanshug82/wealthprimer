---
layout: post
title: "Multiple timeframes: the weekly chart is not a second opinion"
description: "Weekly trend, daily signal — the classic recipe. Six real oversold readings on one chart, sorted by weekly trend, and why the one in the 'uptrend' fell the most."
image: /assets/og/multiple-timeframe-analysis.png
date: 2026-12-20 09:00:00 +0530
series: technical-analysis
term: "Timeframe (multiple-timeframe analysis)"
---

{% assign ta2 = site.data.ta2 %}
{% assign mt = ta2.multi_timeframe %}
{% assign bad_up = mt.example_uptrend_failed %}
{% assign kept_falling = mt.example_downtrend_kept_falling %}
{% assign bounced = mt.example_downtrend_bounced %}

## The recipe everyone is taught

Somewhere in every technical-analysis course is the same advice: **trade in
the direction of the higher timeframe.** Find the trend on the weekly chart,
then use the daily chart to time your entry. A daily "oversold" reading inside
a weekly uptrend is a dip worth buying; the same reading inside a weekly
downtrend is a falling knife.

It's sensible-sounding advice, and it contains a real idea — a signal means
different things in different contexts. It also has a problem that the
tutorials never show you, because they never run the numbers. This post does.

Same data as the whole series: Britannia (NSE: BRITANNIA), daily,
{{ ta2.dataset.as_of }}, resampled to weekly bars — {{ mt.weekly_bars }} of
them.

## What "resampling" means

A weekly bar is built from five daily bars:

```
Weekly open   = Monday's open
Weekly high   = highest high of the week
Weekly low    = lowest low of the week
Weekly close  = Friday's close
Weekly volume = sum of the five days
```

Nothing new is added. The weekly chart contains strictly *less* information
than the daily one — it's the same data with four-fifths of the detail thrown
away. That's the point: less detail, less noise, and a trend that's easier to
see. It's the [moving-average trade-off]({% post_url 2026-10-12-moving-averages %})
again in a different costume: smoother, but later.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine your temperature is taken every hour for a month. The hourly chart is
a mess — you're warmer after lunch, cooler at night.

Now take just one reading a day. The chart is much smoother, and if you're
slowly getting a fever, you'll see it clearly.

But here's the catch: if you *started* getting a fever this afternoon, the
daily chart won't show it until tomorrow. The smoother chart is the slower
chart. That's not a flaw you can fix — it's what smoothing *is*.

</details>

## The chart

![Weekly trend on top, daily RSI underneath]({{ '/assets/charts/ta2-multi-timeframe.svg' | relative_url }})

Britannia (NSE: BRITANNIA), daily and weekly, {{ ta2.dataset.as_of }}. Source:
[Yahoo Finance]({{ ta2.dataset.source_url }}). Historical data, for illustration only.

Top: weekly closes with a {{ mt.weekly_ma_period }}-week simple moving average
(roughly 100 trading days) as the "weekly trend" — up when the weekly close is
above it, down when below. Bottom: the daily 14-period
[RSI]({% post_url 2026-10-14-rsi %}). The weekly average needs 20 weeks of
history, so the trend reading begins on {{ mt.weekly_ma_first_date }}; before
that there is no weekly trend to speak of.

Over the period where it exists, the weekly trend read "up" for
{{ mt.weeks_in_uptrend }} weeks and "down" for {{ mt.weeks_in_downtrend }}.

## Every daily oversold reading, sorted by the weekly trend

Here is the test the tutorials skip. Take every day on which the daily RSI
first dropped below 30 — a fresh "oversold" reading — and record what the
weekly trend said *as of the previous completed week* (so no peeking at a
week that hadn't finished). Then look 20 sessions ahead.

There were **{{ mt.daily_oversold_events }}** such events in two years:

| Date | Daily RSI | Close | Weekly trend | 20 sessions later | Lowest low in between |
|---|---:|---:|---|---:|---:|{% for e in mt.events %}
| {{ e.date }} | {{ e.rsi }} | ₹{% include inr.html n=e.close %} | {{ e.weekly_trend }} | **{% if e.fwd_20_bars_pct > 0 %}+{% endif %}{{ e.fwd_20_bars_pct }}%** | ₹{% include inr.html n=e.lowest_low_next_20_bars %} |{% endfor %}

Summarised:

| Weekly trend at the time | Events | Average 20-session return | Share positive |
|---|---:|---:|---:|
| Up ("buy the dip") | {{ mt.in_weekly_uptrend.count }} | **{{ mt.in_weekly_uptrend.avg_fwd_20_bars_pct }}%** | {{ mt.in_weekly_uptrend.share_positive_pct }}% |
| Down ("falling knife") | {{ mt.in_weekly_downtrend.count }} | **+{{ mt.in_weekly_downtrend.avg_fwd_20_bars_pct }}%** | {{ mt.in_weekly_downtrend.share_positive_pct }}% |

The recipe says the top row should be the good one. In this dataset it is the
*only* losing row.

## Why the "uptrend" dip was the worst one

The single oversold reading inside a weekly uptrend came on {{ bad_up.date }},
with RSI at {{ bad_up.rsi }} and the stock at ₹{% include inr.html n=bad_up.close %}.
Twenty sessions later it was **{{ bad_up.fwd_20_bars_pct }}%** lower, and the
lowest low along the way was ₹{% include inr.html n=bad_up.lowest_low_next_20_bars %}.

Look at where that date sits: three weeks after the {{ site.data.ta.major_decline.peak_date }}
peak that the [trend lines post]({% post_url 2026-10-11-trend-lines %})
built its examples on. The stock had already turned. The daily chart knew it —
that's why RSI was under 30. The *weekly* chart did not know it yet, because a
20-week average takes weeks to roll over after a top. The "higher timeframe
uptrend" was a lagging description of a rally that had ended.

This is the structural problem with the recipe, and it isn't specific to this
stock. The higher timeframe is smoother *because* it is slower. So at exactly
the moment it matters most — right after a top or a bottom — the weekly trend
is the last thing to notice. The daily signal fires; the weekly context says
"still fine"; the recipe says buy.

## The two downtrend examples

The mirror image is in the bottom row. Of the five oversold readings inside a
weekly downtrend — the ones the recipe says to ignore — three were followed by
gains.

{{ kept_falling.date }} is the one that behaved as advertised: RSI
{{ kept_falling.rsi }}, weekly trend down, and the stock fell another
**{{ kept_falling.fwd_20_bars_pct }}%** over the next 20 sessions. The RSI
post used this exact date as its "oversold but kept falling" example.

{{ bounced.date }} is the opposite: RSI {{ bounced.rsi }}, weekly trend firmly
down, four sessions before the {{ site.data.ta.major_decline.trough_date }}
low that ended the whole decline — and the stock rose
**+{{ bounced.fwd_20_bars_pct }}%** over the next 20 sessions. The weekly
trend was still "down" for weeks afterwards, for the same lag reason: it took
that long for the average to catch up with the turn.

Same signal, same weekly context, opposite outcomes. Three months apart, on
the same stock.

## What multiple timeframes are actually good for

None of this means the weekly chart is useless. It means the weekly chart is a
**description of the recent past at a coarser resolution** — not an
independent second opinion, and certainly not a filter that makes daily
signals reliable. Used honestly, it does two things well:

1. **It stops you mistaking noise for structure.** The [chart-patterns post]({% post_url 2026-10-16-chart-patterns %})
   found six swing highs in a 3% band that a daily chart could be talked into
   calling a double top. On the weekly chart they collapse into one flat
   ceiling — the more accurate reading.
2. **It sets the scale for everything else.** Where the [support and resistance]({% post_url 2026-10-10-support-and-resistance %})
   zones come from, how far an [ATR-based stop]({% post_url 2026-12-18-bollinger-bands-and-atr %})
   should sit — these depend on the timeframe you're actually operating on,
   and looking at one chart above yours keeps that honest.

What it can't do is turn a signal that's unreliable on the daily chart into a
reliable one. Agreement between timeframes feels like confirmation. Since the
weekly is built from the daily, it's closer to hearing the same thing twice.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

# daily -> weekly bars (weeks ending Friday)
wk = df.resample("W-FRI").agg({"open": "first", "high": "max",
                               "low": "min", "close": "last",
                               "volume": "sum"}).dropna()
wk["trend_up"] = wk.close > wk.close.rolling(20).mean()

# weekly trend as known on each DAILY bar: use the PREVIOUS completed week
trend_on_day = wk.trend_up.shift(1).reindex(df.index, method="ffill")

delta = df.close.diff()
rsi = 100 - 100 / (1 + delta.clip(lower=0).ewm(alpha=1/14, adjust=False).mean()
                   / (-delta.clip(upper=0)).ewm(alpha=1/14, adjust=False).mean())
oversold = (rsi < 30) & (rsi.shift() >= 30)          # first day of each episode
fwd = df.close.shift(-20) / df.close - 1

print(pd.DataFrame({"weekly_up": trend_on_day, "fwd20": fwd})[oversold]
        .groupby("weekly_up").fwd20.agg(["count", "mean"]).round(3))
```

The `.shift(1)` on the weekly trend is the line that keeps this honest. Without
it, a Wednesday's signal would be judged against a weekly bar that includes
Thursday and Friday — prices that hadn't happened yet. The next post is
entirely about that kind of mistake.

## Common mistakes

- **Treating the higher timeframe as an independent opinion.** It's the same
  prices, aggregated. Agreement is not confirmation.
- **Forgetting that smoother means slower.** The weekly trend is last to turn
  at tops and bottoms — precisely when a daily signal is most tempting.
- **Judging a daily signal against the current, unfinished week.** That week's
  close is in the future. Use the last completed bar.
- **Adding timeframes until they agree.** With daily, weekly, monthly and
  four-hourly charts to choose from, some pair will always line up. That's a
  search, not a signal.
- **Quoting a weekly average before it exists.** Twenty weeks of history means
  twenty weeks of nothing. The first trend reading here is
  {{ mt.weekly_ma_first_date }}, four and a half months into the data.

**Takeaway:** A weekly chart is the daily chart with the detail thrown away —
smoother, and therefore slower — not an independent second opinion. On two
years of Britannia, the only daily oversold reading that arrived inside a
weekly "uptrend" was followed by a 12.6% fall, because the weekly trend hadn't
yet noticed the top, while three of the five readings in a weekly "downtrend"
were followed by gains. Use the higher timeframe to set scale and kill noise.
Don't use it to launder a daily signal.
