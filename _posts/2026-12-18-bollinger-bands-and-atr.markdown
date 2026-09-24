---
layout: post
title: "Bollinger Bands and ATR: measuring volatility, not direction"
description: "Two tools that measure how much a stock moves, not where. Bollinger Bands, the squeeze, ATR, and two real squeezes on one chart that resolved very differently."
image: /assets/og/bollinger-bands-and-atr.png
date: 2026-12-18 09:00:00 +0530
series: technical-analysis
term: "Bollinger Bands"
---

{% assign ta2 = site.data.ta2 %}
{% assign bb = ta2.bollinger %}
{% assign atr = ta2.atr %}
{% assign sq1 = bb.squeeze_then_big_move %}
{% assign sq2 = bb.squeeze_then_nothing %}
{% assign st = atr.stop_example %}

## A different question

Everything in the [first ten posts]({% post_url 2026-10-08-what-technical-analysis-is %})
of this series asked some version of *which way?* Trend lines, moving
averages, RSI, MACD — all of them are, at bottom, attempts to read direction.

This post asks a different and more answerable question: **how much does this
thing move?** That is volatility, and two of the most common tools for
measuring it — Bollinger Bands and the Average True Range — are useful
precisely because they don't pretend to know direction. They tell you how
wide the road is, not which way the car is going.

Same dataset as the rest of the series: Britannia (NSE: BRITANNIA),
{{ ta2.dataset.as_of }}. The data ends {{ ta2.dataset.end | date: "%-d %B %Y" }}, about
{{ ta2.dataset.lag_months }} months before this post — well past the
three-month lag this blog keeps on every real price series.

## Bollinger Bands: the formula

Take a moving average, then draw a line two
[standard deviations]({% post_url 2026-10-23-volatility-and-sharpe %}) above it and
two below:

```
Middle band  = SMA(20)
Upper band   = SMA(20) + 2 × σ(20)
Lower band   = SMA(20) − 2 × σ(20)

σ(20) = population standard deviation of the last 20 closes

Bandwidth  = (Upper − Lower) / Middle               how wide are they?
```

The standard deviation is the whole idea. When price has been jumping around,
σ is large and the bands are wide; when it has been quiet, σ shrinks and the
bands pinch together. The bands are a **volatility ruler drawn around a
[moving average]({% post_url 2026-10-12-moving-averages %})**.

You'll often read that about 95% of closes should fall inside the bands,
because 95% of random draws from a normal distribution land within two
standard deviations. That rule is for independent draws around a fixed
average. Bollinger's σ is measured on the last 20 closing *prices* — levels,
not daily returns — and prices trend. Each close sits near the one before, so
in a steady move the whole window drifts and the newest close keeps landing
near the edge, or past it. In this dataset **{{ bb.pct_bars_inside_bands }}%**
of closes sat inside the bands. Treat the 95% as a loose analogy, not a
probability.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine walking a dog on a lead that stretches. When the dog is calm, it stays
close and the lead is slack — the "band" around you is narrow. When the dog is
excited, it darts about and the lead stretches to its limit in every direction.

Bollinger Bands are that lead, drawn around the price. Wide bands mean the dog
has been darting. Narrow bands mean it's been calm. Neither tells you which way
the dog will run next — only how far it's *been* running lately.

</details>

## The chart

![Britannia with 20-day Bollinger Bands, bandwidth and ATR]({{ '/assets/charts/ta2-bollinger-atr.svg' | relative_url }})

Britannia (NSE: BRITANNIA), {{ ta2.dataset.as_of }}. Source:
[Yahoo Finance]({{ ta2.dataset.source_url }}). Historical data, for illustration only.

Three panels: price with the bands, the bandwidth underneath, and the ATR at
the bottom. Notice how the bands bulge during the late-2024 decline and pinch
in the quiet stretches. Bandwidth ranged from **{{ bb.bandwidth_min_pct }}%**
({{ bb.bandwidth_min_date | date: "%-d %B %Y" }}) to **{{ bb.bandwidth_max_pct }}%**
({{ bb.bandwidth_max_date | date: "%-d %B %Y" }}) — an elevenfold difference in how much the same
stock was moving, over 24 months.

## The two readings people take from the bands

**1. "Price touched the upper band, so it's overbought."** This is the
common reading and mostly a mistake. A close above the upper band means price
moved more than two standard deviations from its average — which happens most
often during strong trends, when it keeps happening. In this dataset:

| Event | Count | With 10 sessions of data after | Average return over the next 10 sessions | Share positive |
|---|---:|---:|---:|---:|
| Close above the upper band | {{ bb.closes_above_upper }} | {{ bb.n_with_10d_forward_after_upper }} | **{{ bb.avg_10d_return_after_close_above_upper_pct }}%** | {{ bb.share_positive_10d_after_upper_pct }}% |
| Close below the lower band | {{ bb.closes_below_lower }} | {{ bb.n_with_10d_forward_after_lower }} | **{{ bb.avg_10d_return_after_close_below_lower_pct }}%** | {{ bb.share_positive_10d_after_lower_pct }}% |

Events too close to the end of the data to have ten sessions after them are
left out of the averages and shares.

Read that carefully. After a close *above* the upper band, the stock was on
average slightly *higher* ten days later, not lower. After a close *below* the
lower band, it was on average slightly *lower*, and it finished higher only
{{ bb.share_positive_10d_after_lower_pct }}% of the time — a coin flip, not a bounce. The "reversal" reading points
the wrong way in this sample — the same pinned-in-a-trend problem the
[RSI post]({% post_url 2026-10-14-rsi %}) documented. That's
{{ bb.n_with_10d_forward_after_upper | plus: bb.n_with_10d_forward_after_lower }}
scored events on one stock, so treat it as an illustration, not a law. But it is not evidence for
the reversal reading.

**2. "The bands are pinching — a big move is coming."** This is the
**squeeze**, and it is the more defensible use, because it's a statement about
volatility rather than direction. Volatility clusters — quiet days tend to
follow quiet days, and loud days follow loud ones — but over longer stretches
it drifts back toward its usual level. So an unusually quiet spell can't last
forever, and when it ends, the moves get bigger. Whether *up* or *down* is not
part of the claim.

Two squeezes in this dataset, defined as bandwidth hitting a
{{ bb.squeeze_lookback_bars }}-session low:

| Squeeze | Bandwidth | Close | 20 sessions later | Move |
|---|---:|---:|---:|---:|
| {{ sq1.date }} | {{ sq1.bandwidth_pct }}% | ₹{% include inr.html n=sq1.close %} | ₹{% include inr.html n=sq1.close_20_bars_later %} ({{ sq1.later_date }}) | **+{{ sq1.move_20_bars_pct }}%** |
| {{ sq2.date }} | {{ sq2.bandwidth_pct }}% | ₹{% include inr.html n=sq2.close %} | ₹{% include inr.html n=sq2.close_20_bars_later %} ({{ sq2.later_date }}) | **+{{ sq2.move_20_bars_pct }}%** |

The January 2025 squeeze was followed by a {{ sq1.move_20_bars_pct }}% move in four weeks — the
kind of chart that ends up in a tutorial. The December 2025 squeeze was
*tighter* — the narrowest bands in the whole two years — and resolved into
{{ sq2.move_20_bars_pct }}%, which is an ordinary month. Same setup, tighter reading, nothing much
happened.

One honesty note: each row is dated to the *last* session of its squeeze, the
day the bands were tightest — which you could only know afterwards. Measured
from the first session of each squeeze ({{ sq1.first_date | date: "%-d %B %Y" }} and
{{ sq2.first_date | date: "%-d %B %Y" }}), the 20-session moves were +{{ sq1.move_20_bars_from_first_pct }}% and
+{{ sq2.move_20_bars_from_first_pct }}% — much closer together, which makes the same point less
dramatically.

That is the honest shape of the squeeze: it raises the odds of a large move
without promising one, and it says nothing at all about direction.

## ATR: the formula

**ATR — Average True Range** — answers the simplest volatility question there
is: on a typical day, how many rupees does this stock travel?

```
True Range (TR) = max( High − Low,
                       |High − Previous Close|,
                       |Low  − Previous Close| )

ATR(14) = Wilder-smoothed average of TR over 14 sessions
          (α = 1/14, the same smoothing RSI uses)
```

Why "true" range rather than just high minus low? Because of gaps. If a stock
closes at 5,000 and opens the next morning at 4,850, the day's high–low range
might be tiny while the *actual* move from yesterday was 150. True range
counts that gap.

For Britannia, ATR ranged from ₹{% include inr.html n=atr.atr_min %}
({{ atr.atr_min_date | date: "%-d %B %Y" }}) to ₹{% include inr.html n=atr.atr_max %}
({{ atr.atr_max_date | date: "%-d %B %Y" }}), and the median was about
**{{ atr.atr_pct_median }}%** of the price. So on an ordinary day this stock
travelled roughly 2% of its value — a number worth knowing before deciding how
far away a stop-loss belongs.

## What ATR is actually for: sizing a stop

This is the genuinely practical use, and it's about risk management rather
than prediction. A stop-loss placed "5% below" is arbitrary — 5% is nothing
for a volatile small-cap and a lot for a staid large-cap. A stop placed
**two ATRs below** adapts to the stock's own behaviour.

Worked on a historical date — {{ st.date | date: "%-d %B %Y" }}, the golden-cross day from the
moving-averages post, chosen for continuity, not as a signal:

| | |
|---|---:|
| Close | ₹{% include inr.html n=st.close %} |
| ATR(14) | ₹{% include inr.html n=st.atr %} |
| Stop at 2 × ATR below | ₹{% include inr.html n=st.stop_2atr %} ({{ st.stop_distance_pct }}% away) |
| Risk budget (illustrative: 2% of a ₹1,00,000 account) | ₹{% include inr.html n=st.risk_budget %} |
| Shares such that a stop-out loses the budget | ₹{% include inr.html n=st.risk_budget %} ÷ (2 × ₹{{ st.atr }}) = **{{ st.shares_for_budget }}** |
| Lowest low over the next 20 sessions | ₹{% include inr.html n=st.lowest_low_next_20_bars %} |
| Stop hit? | {% if st.stop_hit_within_20_bars %}Yes{% else %}No{% endif %} |

The chain is: the stock's volatility sets the stop distance, the stop distance
plus a fixed rupee risk sets the position size. Volatile stock → wider stop →
fewer shares. That is the entire logic of ATR-based position sizing, and the
risk series on this blog builds
[a whole post]({% post_url 2026-11-07-position-sizing-and-the-one-percent-rule %})
on it. Here, the point is only
that ATR turns "how far away should my stop be?" from a guess into a
measurement.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

# Bollinger Bands: 20-day SMA ± 2 population std devs
mid = df.close.rolling(20).mean()
sd  = df.close.rolling(20).std(ddof=0)        # ddof=0: population, as Bollinger specified
df["upper"], df["lower"] = mid + 2*sd, mid - 2*sd
df["bandwidth"] = (df.upper - df.lower) / mid * 100

# ATR(14), Wilder smoothing
prev = df.close.shift()
tr = pd.concat([df.high - df.low,
                (df.high - prev).abs(),
                (df.low - prev).abs()], axis=1).max(axis=1)
df["atr"] = tr.ewm(alpha=1/14, adjust=False).mean()

print(df[["close", "bandwidth", "atr"]].iloc[20:].describe().round(1))
```

`ddof=0` matters. pandas defaults to the sample standard deviation
(`ddof=1`), which gives slightly wider bands than most charting software.
Neither is "wrong", but if your numbers don't match your broker's chart, this
is usually why.

## Common mistakes

- **Reading a band touch as a reversal signal.** In this dataset closes above
  the upper band were followed, on average, by further gains. In a trend, price
  walks the band.
- **Reading a squeeze as directional.** The squeeze says "a bigger move is
  more likely." It does not say which way, and the tightest squeeze in two
  years was followed by very little.
- **Using a fixed-percentage stop on every stock.** 5% is two and a half ATRs
  for this stock and might be half an ATR for a volatile small-cap. Let the
  stock's own range set the distance.
- **Placing the stop exactly at 2 × ATR because a post said so.** Two is a
  convention. The principle is *scale to volatility*; the multiplier is a
  choice you should be able to defend.
- **Forgetting the warmup.** The first 20 bandwidth values and the first
  ~14 ATR values are not real readings.

**Takeaway:** Bollinger Bands and ATR measure how much a stock moves, not
where it's going — and they're most useful when you let them stay in that
lane. On two years of Britannia, closes above the upper band were followed by
gains more often than falls, the tightest squeeze of the period resolved into
an ordinary month, and the one thing ATR reliably did was turn "how far away
should my stop be?" into a number.
