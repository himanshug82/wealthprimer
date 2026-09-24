---
layout: post
title: "What technical analysis cannot do"
description: "The honest reckoning that closes the series: hindsight bias, subjectivity, overfitting, and the questions about a business that no chart can answer."
image: /assets/og/what-technical-analysis-cannot-do.png
date: 2026-10-17 09:00:00 +0530
series: technical-analysis
---

{% assign ta = site.data.ta %}
{% assign r = ta.rsi %}
{% assign up1 = r.overbought_but_kept_rising.change_pct %}
{% assign fell1 = r.overbought_then_fell.change_pct | abs %}

## The reckoning

The first nine posts covered candlesticks, levels, trend lines, averages,
volume and oscillators. Now the reckoning — not as a disclaimer bolted on at
the end, but because a series that taught you those tools and skipped this
would have been selling something.

Everything below is drawn from the same Britannia dataset the rest of the
series used. None of it is hypothetical. A second module follows this post —
volatility, relative strength, multiple timeframes and backtesting — and it
keeps the same rule: every signal gets checked against what actually happened.

## 1. It cannot see anything that isn't in the price

This is the structural limit, and no indicator gets around it.

A price series knows nothing about whether the company is solvent, whether
its auditors resigned, whether receivables are being recognised aggressively,
or whether the promoter has pledged their shareholding. The
[fundamental toolkit]({% post_url 2026-10-07-capstone-britannia-end-to-end %}) exists precisely because those questions
cannot be answered from a chart.

When a company fails, the chart shows the failure happening. It does not show
it coming, and afterwards everyone points to the chart and says it was
obvious. The [OCF/PAT ratio]({% post_url 2026-09-20-ocf-pat %}) can raise a question about earnings
quality. A moving average cannot, ever, in principle.

## 2. Signals are far rarer, or far noisier, than the tutorials suggest

The tutorials show you a signal and its outcome. They don't show you the base
rates. From this dataset:

| Indicator | What two years actually contained |
|---|---|
| 50/200 crossover | **{{ ta.sma_crossover.golden_cross_count }}** golden cross, **{{ ta.sma_crossover.death_cross_count }}** death crosses observed (the 50-day was already below the 200-day when the 200-day first existed) |
| MACD signal crossover | **{{ ta.macd.total_crossovers }}** signals — one every ~{{ ta.macd.avg_trading_days_between_signals }} trading days |
| RSI above 70 | **{{ ta.rsi.days_above_70 }}** days |

Look at the first and second rows together. The golden cross is so rare that
two years of data yields a single instance — from which nothing whatsoever
can be concluded. The MACD crossover is so common that most of its signals
are noise, clustered exactly in the sideways periods where they're least
informative.

Neither is a usable evidence base from one chart. One is too rare to test;
the other is too noisy to trust. That's not a criticism of these particular
indicators — it's the general shape of the problem.

## 3. The same signal produces opposite outcomes

The RSI table from [that post]({% post_url 2026-10-14-rsi %}) is worth repeating, because
it is the single most honest thing in this series:

| Signal | Date | RSI | Change over the next {{ r.horizon_sessions }} sessions |
|---|---|---:|---|
| Overbought | {{ r.overbought_but_kept_rising.date }} | {{ r.overbought_but_kept_rising.rsi }} | **+{{ up1 }}%** |
| Overbought | {{ r.overbought_then_fell.date }} | {{ r.overbought_then_fell.rsi }} | **{{ r.overbought_then_fell.change_pct }}%** |
| Oversold | {{ r.oversold_but_kept_falling.date }} | {{ r.oversold_but_kept_falling.rsi }} | **{{ r.oversold_but_kept_falling.change_pct }}%** |

Every outcome is measured over the same fixed window — about three months —
not to whichever peak or trough came later.

Two nearly identical overbought readings, ten weeks apart, on the same
stock. One preceded a {{ up1 }}% rise. The other preceded a {{ fell1 }}% fall. Nothing
available *at the time* distinguished them.

## 4. It is trivially easy to fool yourself

The [chart patterns post]({% post_url 2026-10-16-chart-patterns %}) demonstrated this
rather than asserting it. A textbook double top — two peaks {{ ta.apparent_double_top.cherry_picked_peak_gap_pct }}% apart —
dissolved once every swing high in the window was listed: six of them, in a
{{ ta.apparent_double_top.band_width_pct }}% band, with the tallest occurring *before* both chosen peaks and
another arriving *after* them, before the pattern had even confirmed.

Nobody set out to deceive anyone there. That's what makes it worth dwelling
on. Selecting the points that fit is what pattern recognition *does*, and the
only defence is procedural: enumerate everything first, decide the criteria
before you look, and write down what would prove you wrong.

## 5. Every "objective" indicator hides a choice

Technical indicators feel objective because they're arithmetic. They aren't,
because someone chose the parameters:

- Why 14 periods for RSI, not 9 or 21?
- Why 12/26/9 for MACD?
- Why a 50-day and 200-day average, rather than 40 and 180?
- How many bars either side define a "swing high"?
- Does a trend line break on one close beyond it, or two?

Every one of those changes the signals. And the [trend lines
post]({% post_url 2026-10-11-trend-lines %}) showed how much can ride on it: the January
2025 downtrend break happened by **₹2.40** on a single close. A slightly
different rule, and there was no signal that day at all.

Which brings up the deeper problem. Search enough parameter combinations
against data you already have and something will look excellent by chance
alone. That's **overfitting**, and it's the reason strategies that backtest
beautifully so often disappoint afterwards. If a rule's performance collapses
when you change 14 to 15, you found a feature of that dataset, not of markets.

## 6. One stock over two years proves nothing

This series has been careful about this and it bears restating plainly.
Everything here came from {{ ta.dataset.bars }} bars of one large-cap Indian stock over two
years. That is an illustration of *mechanism* — how an indicator is computed
and what it looked like when it fired. It is not evidence about whether any
of it works.

Real evidence would need thousands of instances across many stocks, sectors,
market conditions and decades, with trading costs included and the rules
fixed in advance. Where that work exists, the results are modest. Park and
Irwin's 2007 survey of the research (*Journal of Economic Surveys*) found
that many studies reporting profitable technical rules were weakened by data
snooping, rules picked after the fact, or understated costs. And Sullivan,
Timmermann and White (1999) found that the best moving-average rules from an
earlier century-long study stopped working in the decade after it.

Be suspicious of anyone who shows you one chart. Including this one.

## 7. If a simple rule worked, it would stop working

The [first post]({% post_url 2026-10-08-what-technical-analysis-is %}) left
a tension open. Technical analysis assumes the price already reflects
everything — and then studies past prices to guess the next one. Economists
have a name for the relevant idea: **weak-form efficiency** (Fama, 1970). It
says past prices are already reflected in today's price, so no rule built only
on past prices should beat the market after costs, except by luck.

You don't have to believe markets are perfectly efficient to feel the force
of the argument. If a simple chart rule reliably made money, traders would
pile into it — buying a little earlier, selling a little earlier — and in
doing so trade the edge away. So the rule printed in every textbook is the
one least likely to still work. That doesn't settle the debate; some effects,
like momentum (Jegadeesh and Titman, 1993), have been studied for decades and
are still argued over. But it explains why the edges researchers do find tend
to be small, short-lived and eaten by costs.

## So is any of it worth knowing?

Yes — held at the right level of confidence.

**What it's reasonably good for:**

- **A compact description of what happened.** A candlestick chart genuinely
  packs more information into less space than any table of prices.
- **Identifying where price has previously reacted.** The
  ₹{% include inr.html n=ta.resistance_zone.low %}–₹{% include inr.html n=ta.resistance_zone.high %} band was tested seven times over seventeen months. That is a
  real, observable fact about this stock, not an interpretation.
- **Imposing discipline.** Deciding in advance what would count as a break,
  and writing it down, is a genuinely useful habit — arguably more valuable
  than any signal it generates.
- **Understanding what other participants are watching.** A lot of people
  watch the 200-day average. That alone gives it some effect, regardless of
  whether it has predictive merit.

**What it cannot do:**

- Tell you what happens next
- Reveal anything not already expressed in price and volume
- Assign a probability to any outcome
- Distinguish, at the time, a signal that will work from one that won't
- Substitute for knowing what the business is and whether it can pay its debts

## The honest position

Technical analysis is a language for describing price behaviour. As a
description, it's genuinely useful — more compact and more precise than
talking about charts in prose.

As prediction, the evidence is much weaker than its confident vocabulary
implies, and the vocabulary is part of the problem. "Overbought" sounds like
a fact about value; it's a statement about the last fourteen sessions.
"Confirmed breakout" sounds like something settled; it's a threshold someone
picked. Words like these do a lot of quiet persuading.

The most useful thing this series can leave you with isn't a setup. It's a
habit: before accepting any signal, ask how many times that signal occurred
in the same data and what happened on the *other* occasions. Ask what you'd
have to ignore for the pattern to hold. Ask what would change your mind.

Applied honestly, that habit will disqualify most of what gets published
about charts — including, quite often, the chart in front of you.

**Takeaway:** Technical analysis describes what price has done, compactly and
sometimes usefully, but it can't see anything outside the price, and the same
reading routinely precedes opposite outcomes. Any simple rule that did work
reliably would tend to get traded away once enough people used it. Treat it as
a vocabulary for describing markets rather than a method for predicting them —
and be most sceptical of the chart that fits your existing view best.
