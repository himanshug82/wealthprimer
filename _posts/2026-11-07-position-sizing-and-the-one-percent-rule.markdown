---
layout: post
title: "Position sizing: the 1% rule, and letting volatility pick the number"
description: "How much to buy is a risk decision, not a conviction decision. ATR, the 1–2% rule, and why the same stock gets a different position size on different days."
image: /assets/og/position-sizing-and-the-one-percent-rule.png
date: 2026-11-07 09:00:00 +0530
series: risk
term: "Position sizing"
---

{% assign rk = site.data.risk %}
{% assign d = rk.dataset %}
{% assign p = rk.position_sizing %}
{% assign calm = p.example_calm %}
{% assign wild = p.example_wild %}
{% assign mid = p.example_mid %}

## The question almost nobody asks first

Most conversations about a trade or an investment are about *what* and
*when*. Which stock, which fund, which level, which day. The question that
decides whether a bad call is survivable — *how much* — usually gets answered
by feel: a round number, whatever's in the account, "about the same as last
time."

**Position sizing** is the discipline of answering that question first, and
answering it from the amount you're prepared to lose rather than the amount
you hope to make. This post shows the standard method, with one twist that
matters more than the rule itself: letting the market's own volatility set
the number.

Everything here is method, worked on historical prices. It isn't a suggestion
to buy anything.

## The formula

```
Risk per position (₹)  =  Capital × risk %             (the 1–2% rule)

Shares  =  Risk per position  /  Stop distance per share

Stop distance  =  k × ATR                              (k is usually 1.5–3)
```

Three ideas stacked up:

1. **Decide the rupees you'll lose if you're wrong** before you decide
   anything else. The convention is 1% of capital per position, 2% at the
   aggressive end. On ₹{% include inr.html n=p.capital %} that's
   ₹{% include inr.html n=calm.risk_rupees %}.
2. **Decide where "wrong" is** — the exit price that proves the idea didn't
   work. The distance from entry to that exit is your risk per share.
3. **Divide.** Rupees you'll risk ÷ rupees at risk per share = shares.

Step 2 is where volatility comes in.

## ATR: how much does this thing normally move?

**ATR — Average True Range** — is the average of each day's *true range*
over the last 14 days, where true range is the largest of: today's high minus
low, the gap from yesterday's close up to today's high, and the gap from
yesterday's close down to today's low. Wilder's smoothing, same as the
[RSI]({% post_url 2026-10-14-rsi %}).

```
TR  =  max( High − Low,  |High − Prev Close|,  |Low − Prev Close| )
ATR =  Wilder-smoothed 14-day average of TR   (α = 1/14)
```

It answers one question: on a normal day, how far does this stock travel? A
stop placed *inside* that distance will be hit by ordinary noise, not by the
idea being wrong. So the stop goes a multiple of ATR away — 2× is a common
default — and the position is sized so that being stopped out costs exactly
the rupees decided in step 1.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you're allowed to lose at most ₹100 playing carnival games. One game
costs ₹5 a go, another costs ₹20 a go. You can afford 20 tries at the first
and only 5 at the second — same ₹100 either way.

ATR tells you how much a stock "costs a go" — how far it normally wobbles. A
wobbly stock costs more per share to hold safely, so you hold fewer shares.
The ₹100 you're willing to lose stays the same. The number of tries changes.

</details>

## Worked example: Britannia, three days, three sizes

Britannia (NSE: BRITANNIA), daily data {{ d.britannia_start }} to
{{ d.britannia_end }}. Source: [Yahoo Finance]({{ d.britannia_source_url }}).
Historical data, for illustration only — these dates were chosen after the
fact to show the range, which is exactly what you can't do in real time.

![Britannia price with 14-day ATR as a percentage of price]({{ '/assets/charts/risk-atr.svg' | relative_url }})

Over these two years the 14-day ATR ranged from ₹{{ p.atr_min }} to
₹{{ p.atr_max }} a share — {{ p.atr_pct_min }}% to {{ p.atr_pct_max }}% of the
price. Fix the rules (₹{% include inr.html n=p.capital %} capital, {{ p.risk_pct }}% risk,
stop at {{ p.atr_multiple }}× ATR) and see what they produce on the calmest
day, a middling one, and the wildest:

| | Calmest day | Middling day | Wildest day |
|---|---:|---:|---:|
| Date | {{ calm.date }} | {{ mid.date }} | {{ wild.date }} |
| Close | ₹{% include inr.html n=calm.close %} | ₹{% include inr.html n=mid.close %} | ₹{% include inr.html n=wild.close %} |
| 14-day ATR | ₹{{ calm.atr }} ({{ calm.atr_pct }}%) | ₹{{ mid.atr }} ({{ mid.atr_pct }}%) | ₹{{ wild.atr }} ({{ wild.atr_pct }}%) |
| Stop distance ({{ p.atr_multiple }} × ATR) | ₹{{ calm.stop_distance }} | ₹{{ mid.stop_distance }} | ₹{{ wild.stop_distance }} |
| Stop price | ₹{% include inr.html n=calm.stop_price %} | ₹{% include inr.html n=mid.stop_price %} | ₹{% include inr.html n=wild.stop_price %} |
| Risk budget ({{ p.risk_pct }}%) | ₹{% include inr.html n=calm.risk_rupees %} | ₹{% include inr.html n=mid.risk_rupees %} | ₹{% include inr.html n=wild.risk_rupees %} |
| **Shares** | **{{ calm.shares }}** | **{{ mid.shares }}** | **{{ wild.shares }}** |
| Position value | ₹{% include inr.html n=calm.position_value %} | ₹{% include inr.html n=mid.position_value %} | ₹{% include inr.html n=wild.position_value %} |
| As % of capital | {{ calm.position_pct_of_capital }}% | {{ mid.position_pct_of_capital }}% | {{ wild.position_pct_of_capital }}% |

Same stock, same rules, and the position is nearly twice as large on the calm
day as on the wild one. That is the method working as designed. On
{{ wild.date }} — in the middle of the 26% decline the
[RSI post]({% post_url 2026-10-14-rsi %}) documented — the stock was moving
{{ wild.atr_pct }}% a day. A stop had to sit further away to survive the
noise, so fewer shares could be held for the same ₹{% include inr.html n=wild.risk_rupees %}
of risk.

Now compare the habit most people actually have — buying a fixed number of
shares, say {{ p.fixed_shares }}, regardless:

| {{ p.fixed_shares }} shares, {{ p.atr_multiple }}× ATR stop | Calmest day | Middling day | Wildest day |
|---|---:|---:|---:|
| Rupees at risk | ₹{% include inr.html n=calm.fixed_50_risk_rupees %} | ₹{% include inr.html n=mid.fixed_50_risk_rupees %} | ₹{% include inr.html n=wild.fixed_50_risk_rupees %} |
| As % of capital | {{ calm.fixed_50_risk_pct }}% | {{ mid.fixed_50_risk_pct }}% | **{{ wild.fixed_50_risk_pct }}%** |

The fixed-share buyer *thinks* they're taking the same risk every time. They
aren't. On the wildest day they're risking {{ wild.fixed_50_risk_pct }}% of
capital without having decided to — nearly double the calm-day figure, and
right when the market is at its least forgiving.

## Why 1–2%

The number isn't sacred; the logic behind it is. Recall the
[recovery table]({% post_url 2026-11-06-the-arithmetic-of-losses %}): a 20%
drawdown needs a 25% gain to repair, a 50% drawdown needs 100%. Risking 1%
per position means a run of ten consecutive losers — which will happen to
anyone who trades long enough — costs about 10%. At 5% per position, the
same run costs about 40%, and the account needs a 67% gain just to get back
to where it started. Position sizing is how you make sure your worst
realistic streak is a setback and not an ending.

It also does something quieter: it separates *how sure you are* from *how
much you hold*. Conviction is the least reliable input in investing. Sizing
by volatility takes it out of the calculation.

## Doing it in Python

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

prev = df.close.shift(1)
tr = pd.concat([df.high - df.low,
                (df.high - prev).abs(),
                (df.low - prev).abs()], axis=1).max(axis=1)
df["atr"] = tr.ewm(alpha=1/14, adjust=False).mean()   # Wilder

capital, risk_pct, k = 10_00_000, 0.01, 2
df["stop_dist"] = k * df.atr
df["shares"] = (capital * risk_pct // df.stop_dist).astype(int)

print(df[["close", "atr", "stop_dist", "shares"]].iloc[14:].describe().round(1))
```

Skip the first 14 rows — like every smoothed indicator, ATR has a warmup
during which its values mean nothing.

## Common mistakes

- **Sizing by conviction.** "I'm really sure about this one" is exactly when
  a fixed risk budget earns its keep.
- **Buying the same number of shares every time.** As the second table shows,
  that's a random risk budget wearing a consistent-looking costume.
- **Placing the stop inside the ATR.** A stop closer than one day's normal
  range is a coin-flip on noise, not a test of the idea.
- **Treating the stop as a guarantee.** Stops are orders, not promises. Gaps
  at the open and illiquid stocks can take you out well past the stop price —
  which is a reason to size *smaller* than the formula, never larger.
- **Applying the rule per position but not per portfolio.** Ten positions at
  1% each in ten highly correlated stocks is closer to one position at 10%.
  That's the next post.
- **Forgetting the rule exists once a position is winning.** Position sizing
  governs entries. It says nothing about when to sell, and it isn't a trading
  system. It just keeps you in the game long enough for one to matter.

**Takeaway:** Decide the rupees you'll lose before you decide what to buy,
then let the stock's own volatility set how many shares that buys. On
Britannia, the same 1% rule produced {{ calm.shares }} shares on its calmest
day and {{ wild.shares }} on its wildest — the method is *supposed* to hold
less of what's moving more. Most people do the opposite without noticing.
