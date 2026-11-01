---
layout: post
title: "Trend lines: drawing a trend, and knowing when it broke"
description: "An uptrend has a definition, not a mood: higher highs and higher lows. Drawing trend lines, spotting a break, and why ranges are commoner than trends."
image: /assets/og/trend-lines.png
date: 2026-10-05 09:00:00 +0530
series: technical-analysis
term: "Trend lines"
---

{% assign ta = site.data.ta %}
{% assign tl = site.data.ta_trendlines %}

## Trends are structure, not vibes

"The stock is in an uptrend" gets said as though it were a mood. It isn't —
it has a definition, and the definition is about structure:

- An **uptrend** is a sequence of higher highs and higher lows.
- A **downtrend** is a sequence of lower highs and lower lows.
- Everything else is a **range**, and ranges are extremely common.

That third category matters more than most introductions admit. A stock is
often not trending at all — it's oscillating, and forcing a trend line onto
a range is one of the quickest ways to fool yourself.

Where [support and resistance]({% post_url 2026-10-04-support-and-resistance %}) described
*horizontal* levels, a trend line describes a *sloping* one — and the logic
is the same: a price area that has repeatedly mattered.

A **trend line** makes the structure visible: a straight line drawn through
the swing lows of an uptrend, or the swing highs of a downtrend, then
*extended forward*. It does two jobs — it describes the slope of the move so
far, and it gives you something specific that can later be violated.

## How to draw one

The rules are simple and the discipline is the hard part:

```
Uptrend line   — connect two or more swing LOWS,  extend to the right
Downtrend line — connect two or more swing HIGHS, extend to the right
```

Two points define a line. The *third* touch is what makes it interesting,
because that's the first time the line predicted something and was right.

Three rules that keep the exercise honest:

1. **A straight line, not a curve or a dog-leg.** If you need a bend to make
   it fit, it isn't a trend line.
2. **Draw it and leave it.** Adjusting the line every time price misbehaves
   is drawing a picture of the past, not a test of anything.
3. **Decide in advance what "broken" means.** A single intraday poke through,
   or a daily close beyond it? Both are defensible. Choosing afterwards is
   not.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a ball rolling down a long ramp, bouncing as it goes. Each bounce
comes back up a bit lower than the last.

If you laid a ruler along the tops of those bounces, you'd have a straight
line sloping down. And you could slide the ruler forward and guess roughly
how high the *next* bounce will get.

That's a trend line. The interesting moment is when a bounce goes right past
your ruler — because it means something changed about the ramp.

</details>

## Two real trend lines

Both of these come from the same Britannia data, drawn by connecting exactly
two swing points and extending. No adjusting, no curves.

![Britannia trend lines and their breaks]({{ '/assets/charts/ta-trendlines.svg' | relative_url }}){: width="594" height="320"}

Britannia (NSE: BRITANNIA), daily, September 2024 to March 2026. Source:
[Yahoo Finance]({{ ta.dataset.source_url }}). Historical data, for illustration only.

**The downtrend line.** Connect the {{ ta.major_decline.peak_date | date: "%-d %B %Y" }} high of ₹{% include inr.html n=ta.major_decline.peak_high %} to the
{{ tl.down.anchor2_date | date: "%-d %B %Y" }} high of ₹{% include inr.html n=tl.down.anchor2_high %} and extend. That line describes a fall of
about ₹{{ tl.down.slope_per_day }} a day.

It broke on **{{ tl.down.break_date | date: "%-d %B %Y" }}**, when the stock closed at ₹{% include inr.html n=tl.down.break_close %} against a
line sitting at ₹{% include inr.html n=tl.down.break_line %}. A margin of ₹{{ tl.down.break_margin }} — which tells you something
important about how unclean these signals are in practice. On the day, that
break would have looked like nothing at all.

**The uptrend line.** Connect the {{ ta.major_decline.trough_date | date: "%-d %B %Y" }} low of ₹{% include inr.html n=ta.major_decline.trough_low %} to the
{{ tl.up.anchor2_date | date: "%-d %B %Y" }} low of ₹{% include inr.html n=tl.up.anchor2_low %} and extend. That line rises about ₹{{ tl.up.slope_per_day }} a day.

It then held — every dip through the rest of 2025 found support at or above
it — for **{{ tl.up.days_from_anchor1 }} days** counted from the first anchor, or {{ tl.up.days_from_anchor2 }} from the second,
the day the line could first be drawn, before finally breaking on {{ tl.up.break_date | date: "%-d %B %Y" }}, right at
the end of this dataset.

## What the two lines actually teach

Put side by side, they make a point no textbook diagram does.

The downtrend line broke by ₹{{ tl.down.break_margin }} on a single close. If your rule was "a
daily close beyond the line," you had a signal. If your rule was "two
consecutive closes," or "a close 1% beyond," you didn't — not that day. Same
chart, same line, different answer, entirely because of a threshold you chose
before you started. Or worse, after.

The uptrend line is the opposite story: it did real work for nearly a year, and
a line that survives {{ tl.up.days_from_anchor2 }} days and multiple tests is describing something
genuine about who was buying the dips.

Both are true at once. Trend lines are neither useless nor precise. They're
approximate descriptions that occasionally give you a clean answer and
frequently give you a judgement call.

## Doing it in Python

Two points, a slope, and an extension — that's all a trend line is:

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

def trendline(d1, v1, d2, v2):
    t1, t2 = pd.Timestamp(d1), pd.Timestamp(d2)
    slope = (v2 - v1) / (t2 - t1).days          # rupees per calendar day
    return lambda when: v1 + slope * (pd.Timestamp(when) - t1).days

up = trendline("2025-03-04", 4506.0, "2025-04-07", 4605.1)

after = df.loc["2025-04-08":]
broken = after[after.close < [up(d) for d in after.index]]
print("first close below the line:", broken.index[0].date())
```

Note what the code forces you to do: state the break rule explicitly
(`close < line`). The ambiguity doesn't disappear in code — it just becomes
impossible to hide from.

## Common mistakes

- **Redrawing the line when price breaks it.** The single most common
  self-deception in technical analysis. A line you keep adjusting can never
  be wrong, which means it can never tell you anything.
- **Using two points and calling it confirmed.** Any two points make a line.
  The third touch is the first real evidence.
- **Forcing a trend line onto a range.** If price is oscillating sideways,
  the trend line you draw will look convincing and mean nothing.
- **Not defining "broken" in advance.** As the ₹{{ tl.down.break_margin }} break above shows, the
  threshold decides the signal. Pick it first.
- **Drawing on a linear scale for long periods.** Over multiple years a
  constant *percentage* trend curves upward on a linear axis. For long
  horizons, a log scale is the more honest picture.
- **Assuming a break means reversal.** A broken uptrend line means the
  previous rate of ascent stopped. That could be a reversal — or a pause, or
  a slower uptrend.

**Takeaway:** A trend line is a straight line through two swing points,
extended forward, and its value is that it can be violated — an uptrend is
higher highs and higher lows, not a feeling. Draw it once, define what
"broken" means before you need the answer, and remember that a line breaking
by ₹{{ tl.down.break_margin }} on one close is technically a signal and practically a coin toss.
