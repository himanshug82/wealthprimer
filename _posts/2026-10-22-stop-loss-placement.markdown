---
layout: post
title: "Stop-loss placement: fixed %, ATR or swing low — how often each gets hit"
description: "Three common ways to place a stop, tested on every day of two years of Britannia: how often each was hit, what gaps did to them, and what they cost."
image: /assets/og/stop-loss-placement.png
date: 2026-10-22 09:00:00 +0530
series: technical-analysis
term: "Stop-loss"
---

{% assign t3 = site.data.ta3 %}
{% assign ds = t3.dataset %}
{% assign s = t3.stops %}
{% assign fx = s.fixed_5pct %}
{% assign at = s.atr_2x %}
{% assign sw = s.swing_low_20 %}
{% assign ns = s.no_stop %}
{% assign ns_worst = ns.worst_return_pct | abs %}
{% assign fx_worst = fx.worst_return_pct | abs %}
{% assign big_gap = t3.gaps.biggest.size_pct | abs %}

## A different kind of test

Every post in this run so far has tested a *signal*: something that claims
to tell you what price will do next. A stop-loss doesn't claim that. It's a
rule for getting out: *if price falls to here, I sell.* The
[position-sizing post]({% post_url 2026-10-10-position-sizing-and-the-one-percent-rule %})
showed why that matters. The stop distance, together with the rupees you're
willing to lose, sets how many shares you can hold.

So the useful questions about a stop aren't "does it predict?" They are:

- How often does it get hit?
- When it's hit, do you actually get out at the stop price?
- How often does it throw you out of a trade that would have recovered?

Those can all be measured.

## Three ways to place a stop

| Rule | Stop price | The idea |
|---|---|---|
| **Fixed {{ s.fixed_pct }}%** | Entry × (1 − {{ s.fixed_pct }}%) | Simple, the same for every stock |
| **{{ s.atr_mult }} × ATR** | Entry − {{ s.atr_mult }} × ATR(14) | Wider when the stock is jumpy, tighter when it's calm ([Bollinger and ATR post]({% post_url 2026-10-12-bollinger-bands-and-atr %})) |
| **Swing low** | Just below the lowest low of the last {{ s.swing_lookback }} sessions | Below the level the market recently "defended" |

**ATR (Average True Range)** is the average daily range, including overnight
gaps, smoothed over 14 sessions.

## The formula for the test

```
Entry:     the close of EVERY session with 20 sessions of history
           and 20 sessions of future (no hand-picked entries)
Stop hit:  any later session's low ≤ stop price
Exit:      at the stop price — or at the open, if the stock opened below
           the stop (a gap straight through it)
Not hit:   exit at the close 20 sessions after entry
Costs:     0.1% per side, on every entry and exit

Whipsaw:   stopped out, but the close 20 sessions after entry was
           ABOVE the entry price
```

Entering on every day matters. Tutorials show a stop saving you from one
crash they picked. Here there are **{{ s.entries }} entries**, from
{{ s.first_entry | date: "%-d %B %Y" }} to {{ s.last_entry | date: "%-d %B %Y" }}, good
days and bad. The last {{ s.dropped_no_forward_data }} sessions of the data can't be
entries because they don't have 20 sessions after them. Entries are a day
apart, so neighbouring trades overlap heavily. Treat this as {{ s.entries }}
related examples, not {{ s.entries }} independent experiments.

Britannia (NSE: BRITANNIA), {{ ds.stock_as_of }}, from
[Yahoo Finance]({{ ds.stock_source_url }}). Historical data, for illustration only.

## How far away each stop sat

![How far each stop rule put the stop from the entry]({{ '/assets/charts/ta3-stops.svg' | relative_url }})

| | Fixed {{ s.fixed_pct }}% | {{ s.atr_mult }} × ATR | Swing low |
|---|---:|---:|---:|
| Median distance from entry | {{ fx.median_distance_pct }}% | {{ at.median_distance_pct }}% | {{ sw.median_distance_pct }}% |
| Closest | {{ fx.min_distance_pct }}% | {{ at.min_distance_pct }}% | {{ sw.min_distance_pct }}% |
| Furthest | {{ fx.max_distance_pct }}% | {{ at.max_distance_pct }}% | {{ sw.max_distance_pct }}% |

The ATR stop moved within a fairly narrow band. The swing-low stop was all
over the place: {{ sw.min_distance_pct }}% away when the entry happened to be right at
the recent low, and {{ sw.max_distance_pct }}% away after a sharp rally. A stop placed
by "where the chart says" can put very different amounts of money at risk
from one day to the next, unless the position size adjusts to match.

## What happened

| | No stop | Fixed {{ s.fixed_pct }}% | {{ s.atr_mult }} × ATR | Swing low |
|---|---:|---:|---:|---:|
| Stop hit within 20 sessions | — | **{{ fx.hit_pct }}%** | **{{ at.hit_pct }}%** | **{{ sw.hit_pct }}%** |
| Median sessions until hit | — | {{ fx.median_sessions_to_hit }} | {{ at.median_sessions_to_hit }} | {{ sw.median_sessions_to_hit }} |
| Stopped trades that would have been up at 20 sessions (whipsaw) | — | {{ fx.whipsaw_pct }}% | {{ at.whipsaw_pct }}% | {{ sw.whipsaw_pct }}% |
| Gapped through the stop | — | {{ fx.gapped_through }} | {{ at.gapped_through }} | {{ sw.gapped_through }} |
| Extra loss beyond the stop, when gapped | — | {{ fx.avg_extra_slippage_when_gapped_pct }}% | {{ at.avg_extra_slippage_when_gapped_pct }}% | {{ sw.avg_extra_slippage_when_gapped_pct }}% |
| Average trade, after costs | {{ ns.avg_return_pct }}% | {{ fx.avg_return_pct }}% | {{ at.avg_return_pct }}% | {{ sw.avg_return_pct }}% |
| Worst trade, after costs | {{ ns.worst_return_pct }}% | {{ fx.worst_return_pct }}% | {{ at.worst_return_pct }}% | {{ sw.worst_return_pct }}% |
| Trades ending positive | {{ ns.share_positive_pct }}% | {{ fx.share_positive_pct }}% | {{ at.share_positive_pct }}% | {{ sw.share_positive_pct }}% |

Four things stand out.

**1. How often a stop is hit mostly depends on how far away it is.** The ATR
and swing-low stops had the same median distance and were hit about equally
often. The fixed stop sat a little further away and was hit less. There's no
magic in the method. Closer stops get hit more.

**2. The swing-low stop was hit fastest and whipsawed most.** A median of
{{ sw.median_sessions_to_hit }} sessions to be stopped out, and {{ sw.whipsaw_pct }}% of those
stops threw out a trade that was higher 20 sessions later. That's what happens
when many stops sit just under an obvious level. Ordinary day-to-day wobble
reaches them.

**3. A stop is not a guaranteed exit price.** A {{ s.fixed_pct }}% stop produced a
worst loss of {{ fx_worst }}%, because the stock opened below the stop on a
gap-down day. The largest gap in this data, covered in the
[gaps post]({% post_url 2026-10-16-do-gaps-get-filled %}), was {{ big_gap }}%.
Stops that were gapped through lost an average of an extra
{{ fx.avg_extra_slippage_when_gapped_pct }}% (fixed) and {{ at.avg_extra_slippage_when_gapped_pct }}%
(ATR) beyond the stop price. Real fills can also be worse than a day's low,
which this test doesn't model.

**4. Stops changed the shape of outcomes, not the average.** Without a stop the
worst 20-session trade lost {{ ns_worst }}%. With any of the three, the worst was
under 10%. But the average trade barely moved, and fewer trades ended
positive. On overlapping entries from one stock, differences in the averages
this small are noise. What a stop reliably did here was *cap the damage from
a single trade*, and it paid for that in more small losses.

## What this test can't tell you

- **Which rule is "best".** That depends on what you're trying to limit, and
  how you size positions. A tighter stop with a bigger position can risk the
  same rupees as a wider stop with a smaller one.
- **Anything beyond 20 sessions.** A longer holding period gives every stop
  more time to be hit.
- **Anything beyond this stock.** A more volatile stock would hit the fixed
  {{ s.fixed_pct }}% stop far more often, which is the whole argument for scaling
  stops to volatility in the first place.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")
o, lo, c = df.open.values, df.low.values, df.close.values
H, COST = 20, 0.001

def trade(i, stop):
    for j in range(i + 1, i + H + 1):
        if lo[j] <= stop:                           # stop touched
            return min(o[j], stop) / c[i] - 1 - 2 * COST, True   # gap → fill at open
    return c[i + H] / c[i] - 1 - 2 * COST, False

res = [trade(i, c[i] * 0.95) for i in range(20, len(df) - H)]   # every day, fixed 5%
r = pd.DataFrame(res, columns=["ret", "hit"])
print(f"hit {r.hit.mean():.0%}  avg {r.ret.mean():.2%}  worst {r.ret.min():.1%}")
```

Swap `c[i] * 0.95` for `c[i] - 2 * atr[i]`, or for the lowest low of the last
20 sessions, to test the other two rules.

## Common mistakes

- **Judging a stop by the one crash it avoided.** Test it on every entry,
  including the ones where it threw you out just before a recovery.
- **Assuming you'll get the stop price.** Overnight gaps go straight through
  stops. The worst loss on a {{ s.fixed_pct }}% stop in this data was nearly double
  the stop distance.
- **Putting the stop where everyone else does.** Just under an obvious low is
  the most crowded place on the chart. Here it was hit fastest and whipsawed
  most.
- **Choosing the distance without choosing the size.** A stop's distance
  only means something together with the number of shares. The
  [position-sizing post]({% post_url 2026-10-10-position-sizing-and-the-one-percent-rule %})
  covers that half.

**Takeaway:** How often a stop gets hit depends mostly on how far away it is, not on the method used to place it. On two years of Britannia, stops capped the worst trade but didn't improve the average, and gaps pushed some losses well past the stop. A stop is a rule for limiting damage, not a guaranteed exit price.
