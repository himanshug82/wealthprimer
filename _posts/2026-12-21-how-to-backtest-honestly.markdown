---
layout: post
title: "How to backtest an indicator honestly"
description: "Three rules, one stock, one window: how look-ahead bias, costs and parameter-picking change a backtest — and why none of fifteen SMA pairs beat buy-and-hold."
image: /assets/og/how-to-backtest-honestly.png
date: 2026-12-21 09:00:00 +0530
series: technical-analysis
term: "Backtesting (look-ahead bias, overfitting)"
---

{% assign ta2 = site.data.ta2 %}
{% assign bt = ta2.backtest %}
{% assign bh = bt.buy_and_hold %}
{% assign s1 = bt.strategies.sma_50_200 %}
{% assign s2 = bt.strategies.sma_20_50 %}
{% assign s3 = bt.strategies.rsi_30_70 %}
{% assign s3flat = s3.next_day_with_cost_flat_start %}
{% assign gb = bt.grid_best %}
{% assign gw = bt.grid_worst %}

## The question the whole series has been avoiding

Every post in this series ended the same way: *here is a signal that worked,
here is the same signal that didn't, and one chart cannot tell you which is
typical.* Fair enough. But the obvious follow-up is: **so test it properly.**
Take the rule, run it over the whole history, count the rupees.

That is a backtest, and it is the right instinct. It is also the single
easiest place in all of investing to fool yourself, because the mistakes don't
look like mistakes. They look like a strategy that works. This post runs three
rules from earlier posts through a backtest, makes the classic errors on
purpose, and shows what each one does to the answer.

The dataset is the same: Britannia (NSE: BRITANNIA),
{{ ta2.dataset.as_of }}. The backtest window is shorter — it starts on
{{ bt.start | date: "%-d %B %Y" }}, the first day a 200-day average exists — and runs
{{ bt.bars }} sessions to {{ bt.end | date: "%-d %B %Y" }}, about {{ bt.years }} years. Every
strategy and the benchmark are measured over that identical window with
₹{% include inr.html n=bt.start_capital %} to start.

## The three rules

All three are long-only: either you hold the stock or you hold cash. No
shorting, no leverage.

| Rule | In | Out |
|---|---|---|
| **SMA 50/200** — the [golden cross]({% post_url 2026-10-12-moving-averages %}) | 50-day average above 200-day | 50-day below 200-day |
| **SMA 20/50** — the same idea, faster | 20-day above 50-day | 20-day below 50-day |
| **RSI 30/70** — the textbook [oscillator]({% post_url 2026-10-14-rsi %}) rule | RSI falls below 30 | RSI rises above 70 |

And the benchmark every rule has to beat: **buy on day one, do nothing.**

## Mistake 1: trading at a price you couldn't have had

The first backtest most people write computes today's signal from today's
close and then buys at today's close. It feels natural. It's impossible. The
close is the last price of the day; by the time you know it, the market is
shut. The earliest you can act is tomorrow.

This is **look-ahead bias**: using information in the decision that wasn't
available when the decision had to be made. It's the most common backtest
error and, in more elaborate systems, the hardest to spot.

| Rule | Same-day close (look-ahead), a year | Next-day close (honest), a year |
|---|---:|---:|
| SMA 50/200 | {{ s1.lookahead_no_cost.cagr_pct }}% | {{ s1.next_day_no_cost.cagr_pct }}% |
| SMA 20/50 | {{ s2.lookahead_no_cost.cagr_pct }}% | {{ s2.next_day_no_cost.cagr_pct }}% |
| RSI 30/70 | {{ s3.lookahead_no_cost.cagr_pct }}% | {{ s3.next_day_no_cost.cagr_pct }}% |

*Annualised returns, no costs.*

Here the gap is small — under a percentage point either way, and for the RSI
rule the honest version actually did marginally better, which is just noise.
That's because these rules trade rarely and a one-day slip on a large-cap
doesn't move much. Don't be reassured. For a rule that trades often, or on
volatile stocks, the same one-day error can be big enough to turn a losing
strategy into a "winning" one, and even in this dataset it's worth
{{ s1.lookahead_no_cost.cagr_pct | minus: s1.next_day_no_cost.cagr_pct | round: 1 }} of a
percentage point a year on the slow 50/200 rule. The fix is one line of code — shift the signal by a day — and
there is no excuse for skipping it.

## Mistake 2: forgetting that trading costs money

Every buy and every sell pays brokerage, STT (Securities Transaction Tax),
exchange charges, GST and stamp duty, and loses a little to the bid–ask
spread. Call it **{{ bt.cost_per_side_pct }}% per side** here — illustrative,
and on the low side for a retail account.

| Rule | Next-day, no costs | Next-day, with costs | Trades |
|---|---:|---:|---:|
| SMA 50/200 | {{ s1.next_day_no_cost.cagr_pct }}% | **{{ s1.next_day_with_cost.cagr_pct }}%** | {{ s1.next_day_with_cost.trades }} |
| SMA 20/50 | {{ s2.next_day_no_cost.cagr_pct }}% | **{{ s2.next_day_with_cost.cagr_pct }}%** | {{ s2.next_day_with_cost.trades }} |
| RSI 30/70 | {{ s3.next_day_no_cost.cagr_pct }}% | **{{ s3.next_day_with_cost.cagr_pct }}%** | {{ s3.next_day_with_cost.trades }} |

Again modest, because these rules trade one to five times in a year. Scale
the same 0.1% up to a rule that trades weekly and costs alone eat several
percentage points annually — which is one reason the
[MACD post]({% post_url 2026-10-15-macd %}) was so uneasy about a signal
every fifteen sessions.

## The honest scoreboard

Next-day execution, costs included, the same window for everyone:

![Equity curves: buy and hold vs the three rules]({{ '/assets/charts/ta2-backtest.svg' | relative_url }})

Britannia (NSE: BRITANNIA), daily bars, {{ bt.start | date: "%-d %B %Y" }} to {{ bt.end | date: "%-d %B %Y" }}. Source:
[Yahoo Finance]({{ ta2.dataset.source_url }}). Historical data, for illustration only.

| | Final value | [Return a year]({% post_url 2026-10-19-point-to-point-returns %}) | [Worst drawdown]({% post_url 2026-10-22-drawdown %}) | Trades | Time invested |
|---|---:|---:|---:|---:|---:|
| **Buy and hold** | ₹{% include inr.html n=bh.final_value %} | **{{ bh.cagr_pct }}%** | {{ bh.max_drawdown_pct }}% | {{ bh.trades }} | {{ bh.pct_time_invested }}% |
| SMA 50/200 | ₹{% include inr.html n=s1.next_day_with_cost.final_value %} | {{ s1.next_day_with_cost.cagr_pct }}% | {{ s1.next_day_with_cost.max_drawdown_pct }}% | {{ s1.next_day_with_cost.trades }} | {{ s1.next_day_with_cost.pct_time_invested }}% |
| SMA 20/50 | ₹{% include inr.html n=s2.next_day_with_cost.final_value %} | {{ s2.next_day_with_cost.cagr_pct }}% | {{ s2.next_day_with_cost.max_drawdown_pct }}% | {{ s2.next_day_with_cost.trades }} | {{ s2.next_day_with_cost.pct_time_invested }}% |
| RSI 30/70 | ₹{% include inr.html n=s3.next_day_with_cost.final_value %} | **{{ s3.next_day_with_cost.cagr_pct }}%** | {{ s3.next_day_with_cost.max_drawdown_pct }}% | {{ s3.next_day_with_cost.trades }} | {{ s3.next_day_with_cost.pct_time_invested }}% |

*Trades counts entries into the stock. A rule that's already holding the
stock when the window opens counts that as its first trade.*

Three things to take from this table, in order of how tempting they are to
misread.

**The 20/50 crossover lost a quarter of the money.** Five trades, every one of
them late into a move and late out of it — the whipsaw the moving-averages
post warned about, in rupees. The 50/200 version did less damage only because
it traded once: it bought after the June 2025 golden cross, sat through the
subsequent decline, and finished below where it started while buy-and-hold
finished up.

**The RSI rule "won."** {{ s3.next_day_with_cost.cagr_pct }}% a year against
{{ bh.cagr_pct }}% for doing nothing, with a worst drawdown of only
{{ s3.next_day_with_cost.max_drawdown_pct | abs }}%. This is the row that gets
screenshotted. Now look at the last two columns: **{{ s3.next_day_with_cost.trades }}
trades, invested {{ s3.next_day_with_cost.pct_time_invested }}% of the time.**
The rule sat in cash for seven-eighths of the period and happened to be in the
stock during a few good weeks. Three trades is not a strategy; it's three coin
flips that landed well. The drawdown is small because there was almost no time
for one to happen.

And one of those three trades wasn't even taken inside the test. RSI went
oversold on {{ s3.carried_in_from_oversold_date | date: "%-d %B %Y" }}, a month before the window
opens, so the rule starts the window already holding the stock. Start it in
cash like everything else and it returns {{ s3flat.cagr_pct }}% a year on
{{ s3flat.trades }} trades, invested {{ s3flat.pct_time_invested }}% of the
time — still ahead of buy-and-hold on paper, and still far too few trades to
mean anything. A backtest's start date is one more choice that can move the
answer.

**Buy-and-hold is the row to beat, and it's harder than it looks.** It paid
one commission, was never out of the market, and took the full
{{ bh.max_drawdown_pct | abs }}% drawdown. Every rule that "avoids" that drawdown has
to avoid it *and* be back in for the recovery, and on this evidence, none of
the moving-average rules managed it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a friend says they have a system for guessing which way a coin will
land. You ask them to prove it, and they flip a coin three times, call it right
twice, and say "see — 67% accuracy."

Three flips proves nothing. You'd want to see hundreds. And you'd want to make
sure they call it *before* the coin lands, not after — and that they don't
quietly stop counting the flips they got wrong.

A backtest is the same test for a trading rule. Most of the ways to cheat are
accidental. This post is about spotting them.

</details>

## Mistake 3: picking the parameters after you've seen the answer

Why 50 and 200? Why 20 and 50? Because they're conventions. But the moment
you ask "what if I tried 30 and 150?", you're on a slope that ends in
**overfitting** — choosing the settings that happened to work on the data you
already have, and mistaking that for a rule that works.

Here is every combination of a fast average from {10, 20, 30, 50} and a slow
one from {50, 100, 150, 200}, honestly executed, costs included, same window:

| Fast \ Slow |{% for s in bt.grid_table.slows %} {{ s }} |{% endfor %}
|---|{% for s in bt.grid_table.slows %}---:|{% endfor %}{% for row in bt.grid_table.rows %}
| **{{ row.fast }}** |{% for c in row.cells %} {{ c }} |{% endfor %}{% endfor %}

*Annualised return. Buy-and-hold over the same window: {{ bh.cagr_pct }}%.*

The spread between the best pair ({{ gb.fast }}/{{ gb.slow }}, {{ gb.cagr_pct }}%)
and the worst ({{ gw.fast }}/{{ gw.slow }}, {% if gw.cagr_pct < 0 %}−{% endif %}{{ gw.cagr_pct | abs }}%) is
**{{ bt.grid_spread_pp }} percentage points a year** — on the same stock,
over the same fourteen months, from the same idea. The only thing that changed
was two numbers chosen by the person running the test.

And the line that matters most: **{{ bt.grid_beating_buy_and_hold }} of the
{{ bt.grid_size }} pairs beat buy-and-hold.** Not the conventional ones, not
the optimised ones. If you had searched this grid, found 50/100, and published
it as "the setting that works for Britannia", you would have been reporting
the least-bad loser.

The general lesson: if a rule only works for specific parameter values and
falls apart for neighbouring ones, it isn't a rule. It's a description of one
dataset's noise.

## What an honest backtest needs, and this one doesn't have

Even with look-ahead removed, costs added and parameters held fixed, this
test is nowhere near sufficient evidence for or against any of these rules.
Being clear about why is the point of the exercise:

- **One stock.** A rule has to be tested on many, ideally chosen *before*
  looking at which ones it worked on.
- **{{ bt.years }} years.** Across a single market regime. The 50/200 cross
  earned its reputation over decades and many markets; a year of one company
  says nothing either way.
- **A handful of trades.** Three trades, five trades, one trade. No
  statistical claim survives sample sizes like that.
- **No out-of-sample test.** Every parameter was evaluated on the same data it
  would be "chosen" from. The minimum honest procedure is to pick settings on
  one period and test them on another you haven't looked at.
- **Survivorship.** Britannia is in this dataset because it's a large,
  long-lived company. A rule tested only on the companies that survived to be
  tested is flattered by construction.
- **Slippage and fills.** The test assumes you got the next day's close. Real
  fills are worse in exactly the fast markets where these rules trigger.

None of these are fixable in a blog post. They are fixable in a serious
research process, and when people have done that work at scale, the results
have been modest. Park and Irwin's 2007 survey (*Journal of Economic
Surveys*) found that many studies reporting profitable technical rules were
weakened by data snooping, rules picked after the fact, or understated costs.
Sullivan, Timmermann and White (1999) found that the best moving-average rules
from a century of Dow Jones data stopped working in the decade that followed.
In our reading, simple trend rules have shown uneven, cost-sensitive edges in
some markets and periods — nothing like the reliability the tutorials imply. Which is roughly what the
[limitations post]({% post_url 2026-10-17-what-technical-analysis-cannot-do %})
said before running a single test.

## Doing it in Python

The entire honest backtest is about fifteen lines. The two that matter are
marked.

```python
import pandas as pd

df = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                 parse_dates=["date"]).set_index("date")

signal = (df.close.rolling(50).mean() > df.close.rolling(200).mean()).astype(int)

pos = signal.shift(1).fillna(0)          # (1) act on TOMORROW's close, not today's
ret = df.close.pct_change().fillna(0)
cost = pos.diff().abs().fillna(0) * 0.001  # (2) pay 0.1% every time position changes

strat = pos.shift(1).fillna(0) * ret - cost
equity = 100000 * (1 + strat).cumprod()
bench  = 100000 * (1 + ret).cumprod()

start = df.index[200]                      # compare over the same window
for name, eq in [("rule", equity), ("buy & hold", bench)]:
    eq = eq[start:] / eq[start] * 100000
    dd = (eq / eq.cummax() - 1).min() * 100
    print(f"{name:11s} final ₹{eq.iloc[-1]:,.0f}  worst drawdown {dd:.1f}%")
```

Replace line (1) with `pos = signal` and you have a look-ahead backtest. Delete line (2) and you
have a free-trading one. Both will look better than this. Neither is real.

## Common mistakes

- **Computing the signal and the trade from the same bar.** Look-ahead bias.
  Shift the signal.
- **Testing without costs.** Costs are the one part of the result you know in
  advance. Leaving them out is choosing to be wrong by a known amount.
- **Searching parameters and reporting the best.** That's the answer to "what
  worked?", not "what works?". Fifteen pairs, zero beat the benchmark, and one
  of them would still have looked publishable.
- **Comparing against nothing.** Every rule here has to beat doing nothing,
  and doing nothing is a surprisingly strong opponent.
- **Trusting a small drawdown from a rule that's rarely invested.** Sitting in
  cash {{ 100 | minus: s3.next_day_with_cost.pct_time_invested }}% of the time is why the RSI rule's drawdown is small. That's not
  risk control; it's absence.
- **Concluding anything from one stock and fourteen months.** Including the
  conclusion that these rules don't work. This test can't show that either.

**Takeaway:** A backtest is the right idea and the easiest place in investing
to fool yourself. On one stock and fourteen months, look-ahead bias and costs
each moved the answer by under a point, but choosing the moving-average
lengths after the fact moved it by {{ bt.grid_spread_pp }} points a year — and
none of the fifteen pairs beat simply holding, while the rule that "won"
traded three times. Shift your signal by a day, pay your costs, fix your parameters
before you look, and then remember that even a clean test on one chart proves
almost nothing.
