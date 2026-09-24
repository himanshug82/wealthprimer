---
layout: post
title: "Relative strength vs the index: the other RS, and the one that means what it says"
description: "Not RSI. Relative strength divides a stock by its index to show whether it's beating the market. Britannia vs Nifty 50 over two years, and what the ratio hid."
image: /assets/og/relative-strength-vs-the-index.png
date: 2026-12-19 09:00:00 +0530
series: technical-analysis
term: "Relative strength (vs index)"
---

{% assign ta2 = site.data.ta2 %}
{% assign rs = ta2.relative_strength %}
{% assign dw = rs.decline_window %}

## Two things called RS, one of them misnamed

The [RSI post]({% post_url 2026-10-14-rsi %}) flagged this in passing: the
Relative Strength *Index* has nothing to do with strength relative to anything.
It compares a stock only to its own recent behaviour.

This post is about the other one — plain **relative strength**, sometimes
written RS or "comparative relative strength" to keep it apart from RSI. This
one means exactly what it says: is the stock doing better or worse than the
market it trades in?

It's a simple idea, it's badly under-used compared with RSI, and it answers a
question every long-term holder eventually asks: *my stock is up, but is that
me or is that just the market?*

## The formula

```
Relative strength = Stock price / Index level

Rebased:  RS(t) = ( Stock(t) / Index(t) ) ÷ ( Stock(0) / Index(0) ) × 100
```

The rebasing just sets the ratio to 100 on the first day so it reads like a
percentage: 110 means the stock has beaten the index by 10% since the start;
90 means it has lagged by 10%.

Three things about the ratio are worth spelling out:

- **It rises when the stock outperforms — even if both are falling.** A stock
  down 5% while the index is down 15% has *rising* relative strength. That is
  the whole point and also the main way people misread it.
- **The absolute level is arbitrary**, because it depends on the rebasing date.
  Only the direction and the changes mean anything.
- **It is a ratio of two noisy series**, so it is itself noisy. People put a
  moving average on it for the same reason they put one on price.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your class sits an exam. You scored 65, up from 60 last time — good news?

Depends. If the whole class averaged 80 this time, up from 55, you actually
did *worse* compared with everyone else, even though your own score went up.
If the class average fell to 40, your 65 is spectacular.

Relative strength is your score divided by the class average. It tells you
whether you're pulling ahead of the room or falling behind it — separately
from whether your own score went up or down.

</details>

## The chart

![Britannia vs Nifty 50, and the relative strength ratio]({{ '/assets/charts/ta2-relative-strength.svg' | relative_url }})

Britannia (NSE: BRITANNIA) and the Nifty 50 price index, daily,
{{ rs.common_start }} to {{ rs.common_end }} ({{ rs.common_bars }} common
sessions). Sources: [Yahoo Finance, BRITANNIA.NS]({{ ta2.dataset.source_url }})
and [Yahoo Finance, ^NSEI]({{ ta2.dataset.index_source_url }}). Historical
data, for illustration only.

The top panel shows both rebased to 100. The bottom panel is the ratio, with
its {{ rs.ma_period }}-day moving average.

| | |
|---|---:|
| Britannia, total return over the window | **{{ rs.stock_total_return_pct }}%** |
| Nifty 50 (price index), total return | **{{ rs.index_total_return_pct }}%** |
| Difference | **{{ rs.stock_minus_index_pp }} percentage points** |
| Relative strength at the start | {{ rs.rs_start }} |
| Relative strength at the end | **{{ rs.rs_end }}** |
| Lowest | {{ rs.rs_low }} on {{ rs.rs_low_date }} |
| Highest | {{ rs.rs_high }} on {{ rs.rs_high_date }} |

Over two years the stock beat the index by about eleven points. But the path
matters more than the endpoint. The ratio *rose* for the first six months, to
about 115 in early October 2024. Then it collapsed in just two, to
{{ rs.rs_low }} in December 2024. Then it spent the next nine months climbing
back to {{ rs.rs_high }} — barely above where it had been a year earlier.
Someone who looked only in October 2024 would have called this a market leader.
Someone who looked only in December 2024 would have called it a laggard.
Someone who looked in September 2025 would have called it a leader again. All
three would have been describing the same two years.

Note that the Nifty figure is the **price** index, which excludes dividends.
The [benchmarks post]({% post_url 2026-10-25-benchmarks-and-comparing-like-with-like %})
explained why that flatters anything compared against it by roughly the
dividend yield; the same caveat applies here, though it's small over two years
and doesn't change the shape of the ratio.

## The part the ratio hides

Here is where relative strength earns its keep, and also where it misleads if
you stop reading too early.

The [trend lines post]({% post_url 2026-10-11-trend-lines %}) built its
examples on Britannia's five-month slide from its {{ dw.start }} peak to the
{{ dw.end }} trough. Over that same window:

| {{ dw.start }} → {{ dw.end }} | Change |
|---|---:|
| Britannia | **{{ dw.stock_pct }}%** |
| Nifty 50 | **{{ dw.index_pct }}%** |

The index fell too. Roughly half of Britannia's decline was the market, not
the stock — which the price chart alone can't tell you, and which the ratio
shows immediately. That is the constructive use of relative strength:
**separating what the company did from what the market did**.

It also shows the trap. During the worst stretch of that decline the ratio was
falling — Britannia was underperforming a falling market — and an investor
reading "weak relative strength" as a signal would have been right about
direction but for reasons that had nothing to do with the ratio. The ratio
describes; it doesn't forecast.

## Relative strength and the moving average

Putting a {{ rs.ma_period }}-day average on the ratio and asking "is RS above
or below its average?" is the standard way people turn this into a trend
reading. In this dataset RS sat above its average **{{ rs.pct_bars_rs_above_ma }}%**
of the time. The longest stretch below was {{ rs.longest_stretch_below_ma_bars }}
sessions (about eleven weeks); the longest above was
{{ rs.longest_stretch_above_ma_bars }}.

The best 60-session stretch of relative performance was
**+{{ rs.best_60d_relative.pct }}%** ending {{ rs.best_60d_relative.date }};
the worst was **{{ rs.worst_60d_relative.pct }}%** ending
{{ rs.worst_60d_relative.date }}. Those are big swings for a large, stable
consumer company against its own index — a reminder that "relative strength"
is not a stable property of a stock but a description of a particular window.

## Why this matters beyond charts

Relative strength is one of the few technical ideas with a direct line to the
fundamental side of this blog. If a company's relative strength has been
falling for a year while its [ROCE]({% post_url 2026-09-03-roce %}) and
[free cash flow]({% post_url 2026-09-19-free-cash-flow %}) are unchanged,
either the market has re-rated it — its [P/E]({% post_url 2026-09-24-price-to-earnings %})
has compressed — or the rest of the market has been re-rated upwards. Both are
worth knowing. Neither is visible on a price chart alone.

## Doing it in Python

```python
import pandas as pd

stock = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                    parse_dates=["date"]).set_index("date").close
nifty = pd.read_csv("nifty50-price-index.csv",
                    parse_dates=["date"]).set_index("date").nifty50_pri_close

both = pd.concat([stock.rename("stock"), nifty.rename("nifty")], axis=1).dropna()
rs = both.stock / both.nifty
rs = rs / rs.iloc[0] * 100                 # rebase to 100 on day one
rs_ma = rs.rolling(50).mean()

print(f"RS end {rs.iloc[-1]:.1f}  low {rs.min():.1f} on {rs.idxmin().date()}  "
      f"high {rs.max():.1f} on {rs.idxmax().date()}")
print(f"above its 50-day MA {(rs > rs_ma).mean()*100:.0f}% of the time")
```

The `.dropna()` after the concat matters: the two series have slightly
different trading calendars (the index file has a few dates the stock file
doesn't, and vice versa), and a ratio on a day where one side is missing is
garbage.

## Common mistakes

- **Confusing it with RSI.** RSI is a 0–100 oscillator about a stock's own
  momentum. Relative strength is an unbounded ratio against a benchmark. Same
  letters, unrelated tools.
- **Reading rising RS as "the stock is going up."** It means the stock is
  beating the index. Both can be falling.
- **Comparing against the wrong index.** A mid-cap against the Nifty 50, or a
  bank against a consumer index, produces a ratio that mostly measures the
  sector gap. Compare like with like.
- **Treating the level as meaningful.** 111 means nothing on its own; it
  depends entirely on where you started the clock. Only the slope matters.
- **Assuming it persists.** Two years contained an eleven-week stretch of
  underperformance and a nine-month stretch of outperformance on the same
  stock. Relative strength is a description of a window, not a trait.

**Takeaway:** Relative strength — the stock divided by its index — separates
what a company did from what the market did, which is the one question a
price chart can't answer on its own. Over two years Britannia beat the Nifty
by about eleven points, but the ratio rose for six months, collapsed over two,
then climbed for nine, and half of the stock's worst decline turned out to
be the market's. Read it as a description. It has never been a forecast.
