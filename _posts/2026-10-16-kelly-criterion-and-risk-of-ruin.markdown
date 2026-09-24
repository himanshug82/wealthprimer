---
layout: post
title: "Risk of ruin and the Kelly criterion: the maths of how much to bet"
description: "Kelly's 1956 formula says how much of your capital to stake on an edge. Why full Kelly is brutal, and why the edge you plug in is the part most likely wrong."
image: /assets/og/kelly-criterion-and-risk-of-ruin.png
date: 2026-10-16 09:00:00 +0530
series: risk
term: "Kelly criterion"
---

{% assign r2 = site.data.risk2 %}
{% assign k = r2.kelly %}
{% assign mch = k.monte_carlo.half %}
{% assign mcf = k.monte_carlo.full %}
{% assign mcd = k.monte_carlo.double %}
{% assign e55 = k.estimation_table[0] %}
{% assign e53 = k.estimation_table[2] %}
{% assign e52 = k.estimation_table[3] %}
{% assign e51 = k.estimation_table[4] %}

## Two ways to lose everything with an edge

Suppose you really do have an edge: a bet that wins a little more often than
it loses. There are still two ways to go broke with it. Bet a fixed amount
too large for your capital and a normal losing streak wipes you out before
the edge has time to show up. Bet too large a *fraction* of your capital each
time and something subtler happens: your money shrinks over time even though
every single bet is in your favour.

**Risk of ruin** is the chance that a betting or trading plan loses all of
its capital — or, more usefully, falls to a level you can't come back from.
The **Kelly criterion** is the answer to the question underneath it: if you
have an edge, what fraction of your current capital should each bet be, so
that your money grows as fast as possible over the long run? John L. Kelly Jr.
derived it at Bell Labs in
[1956]({{ k.kelly_1956_url }}) (*A New Interpretation of Information Rate*,
Bell System Technical Journal), and the mathematician Edward Thorp took it
from blackjack tables to markets. His survey chapter,
[*The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market*]({{ k.thorp_url }})
(2006), is the source for the drawdown results below.

This post is maths on a coin and on historical fund returns. The fractions
that come out are properties of the examples, not a sizing recommendation —
and the second half of the post is about why the formula's input is the
part you should trust least. It picks up where the
[position sizing post]({% post_url 2026-10-10-position-sizing-and-the-one-percent-rule %})
left off: that post fixed the rupees at risk per trade by convention; Kelly
tries to *derive* the stake from the edge.

## The formula

```
A bet that wins with probability p and loses with probability q = 1 − p.
A win pays b times the stake; a loss costs the stake.

Growth per bet if you stake a fraction f of capital:
    g(f)  =  p × ln(1 + b·f)  +  q × ln(1 − f)

Kelly fraction (the f that maximises g):
    f*  =  (b·p − q) / b          even-money bet (b = 1):  f* = p − q

Continuous version, for an asset with expected excess return μ − r
and volatility σ (both annual):
    f*  =  (μ − r) / σ²

Gambler's ruin — a FIXED stake, N stakes of capital, even money, p > ½:
    P(eventually lose everything)  =  (q / p)^N

Thorp, for betting a fraction c of Kelly (c = 1 is full Kelly):
    P(capital ever falls to a fraction x of the start)  =  x^(2/c − 1)
```

Three things to notice. Kelly maximises the *growth rate* — the average of
the logarithm of wealth — not the average outcome. It stakes a *fraction*,
so the rupee bet shrinks after losses and grows after wins, which is why a
pure fraction never literally hits zero. And the whole thing runs on *p* and
*b* (or μ, r and σ): numbers you have to estimate.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You have a coin that lands heads a bit more than half the time, and every
heads wins you as much as you bet. Should you bet all your pocket money on each toss?
No — one tails and you're done forever. Should you bet one rupee at a time?
You'd be safe, but you'd barely grow.

Kelly is the in-between answer: always bet the same *slice* of whatever you
have right now. With this coin the best slice is small. Bet a bigger slice
and the bad tosses hurt so much more than the good ones help that you end up
poorer, even with a lucky coin.

</details>

## Worked example: a coin that lands heads {{ k.p_pct }}% of the time

An even-money bet (*b* = {{ k.b }}) that wins {{ k.p_pct }}% of the time and
loses {{ k.q_pct }}%. Kelly says f* = {{ k.p_pct }}% − {{ k.q_pct }}% = {{ k.f_star_pct }}% of
current capital per bet. Here is the growth rate at different fractions, and
what it compounds to over {% include inr.html n=k.n_bets %} bets for the
typical (median) player:

| Fraction staked | × Kelly | Growth per bet | Median wealth after {% include inr.html n=k.n_bets %} bets |
|---:|---:|---:|---:|{% for row in k.growth_table %}
| {{ row.f_pct }}% | {{ row.kelly_multiple }} | {{ row.growth_per_bet_pct }}% | {{ row.median_multiple_1000 }}× |{% endfor %}

The curve is lopsided. Half Kelly ({{ mch.f_pct }}%) keeps
{{ k.half_kelly_growth_share_pct | round }}% of the maximum growth rate.
Double Kelly ({{ mcd.f_pct }}%) — the *same* edge, the *same* coin — has a
growth rate of roughly zero: growth crosses zero at
{{ k.f_zero_growth_pct }}%, and anything beyond shrinks your money in the
long run. That's Thorp's point about overbetting: being too aggressive is
punished far more than being too timid.

### Why full Kelly is brutal

Maximum growth doesn't mean a comfortable ride. We simulated
{% include inr.html n=k.mc_paths %} players, each making
{% include inr.html n=k.n_bets %} bets on the same coin (fixed random seed, in
`scripts/derive_risk2.py`):

| Strategy | Chance of falling to half the start, at some point | Chance of losing 70%, at some point | Chance of ending below the start | Median final wealth |
|---|---:|---:|---:|---:|
| Half Kelly ({{ mch.f_pct }}%) | {{ mch.p_ever_half_pct }}% | {{ mch.p_ever_lose_70_pct }}% | {{ mch.p_below_start_pct }}% | {{ mch.median_final_multiple }}× |
| Full Kelly ({{ mcf.f_pct }}%) | {{ mcf.p_ever_half_pct }}% | {{ mcf.p_ever_lose_70_pct }}% | {{ mcf.p_below_start_pct }}% | {{ mcf.median_final_multiple }}× |
| Double Kelly ({{ mcd.f_pct }}%) | {{ mcd.p_ever_half_pct }}% | {{ mcd.p_ever_lose_70_pct }}% | {{ mcd.p_below_start_pct }}% | {{ mcd.median_final_multiple }}× |

Thorp's formula gives the long-run chance of ever halving as
{{ mcf.thorp_p_half_pct }}% at full Kelly and {{ mch.thorp_p_half_pct }}% at
half Kelly; the simulation, over a finite {% include inr.html n=k.n_bets %}
bets, lands just under both. So a full-Kelly bettor with a *genuine* edge,
known exactly, still has roughly even odds of watching their capital halve
along the way. Thorp wrote that most cautious users "find the frequency of
substantial bankroll reduction to be uncomfortably large", and bet less.
Recall from the
[arithmetic of losses]({% post_url 2026-10-09-the-arithmetic-of-losses %})
what a 50% drawdown needs to repair: a 100% gain.

### Fixed stakes: the gambler's ruin

The other way to be ruined is to bet a fixed rupee amount. With *N* stakes of
capital, the chance of eventually losing everything:

| Win probability | 5 stakes | 10 stakes | 20 stakes | 50 stakes |
|---:|---:|---:|---:|---:|{% for row in k.ruin_table %}
| {{ row.p_pct }}% | {{ row.n5 }}% | {{ row.n10 }}% | {{ row.n20 }}% | {{ row.n50 }}% |{% endfor %}

At a fair 50/50, ruin is certain eventually, however deep your pockets. A
genuine {{ k.p_pct }}% edge with only five stakes of capital still carries a
{{ k.ruin_table[3].n5 }}% chance of going broke. Edge and staying power are
different things.

## The weak link: the edge you plug in

Every number above assumed you *know* the win probability is {{ k.p_pct }}%. You never do. Here's what
happens if you believe {{ k.p_pct }}% and bet accordingly, but the true
probability is lower:

![Growth per bet against fraction staked, for the believed and a smaller true edge]({{ '/assets/charts/risk2-kelly.svg' | relative_url }})

| True win probability | True Kelly fraction | Growth per bet, staking 10% (full Kelly on your belief) | Growth per bet, staking 5% (half) | Median wealth after {% include inr.html n=k.n_bets %} bets: 10% / 5% |
|---:|---:|---:|---:|---:|{% for row in k.estimation_table %}
| {{ row.p_true_pct | round }}% | {{ row.true_kelly_pct }}% | {{ row.growth_full_pct }}% | {{ row.growth_half_pct }}% | {{ row.median_full_1000 }}× / {{ row.median_half_1000 }}× |{% endfor %}

Overestimate a {{ e52.p_true_pct | round }}% edge as {{ k.p_pct }}% and full
Kelly shrinks the typical player's money to {{ e52.median_full_1000 }}× over
{% include inr.html n=k.n_bets %} bets — while half Kelly, on the same wrong
belief, still grows it to {{ e52.median_half_1000 }}×. That's the practical
case for fractional Kelly: not timidity, but insurance against your own
estimate.

### What "the edge" looks like on real data

The continuous formula f* = (μ − r) / σ² can be fed actual history. We did it
for the {{ site.data.risk.dataset.fund_name }} (regular-plan growth NAV, or net asset value; AMFI, the Association of
Mutual Funds in India, via
[mfapi.in]({{ r2.dataset.fund_source_url }})), using financial-year returns
over every rolling five-year window, with the UTI Overnight Fund's return as
*r*. Before 2018 that fund wasn't an overnight portfolio, so read it as a
cash-like proxy. Data to {{ r2.dataset.as_of }}; historical, for illustration
only.

| Window | Mean return over cash | Volatility | "Kelly fraction" |
|---|---:|---:|---:|{% for row in k.windows %}
| {{ row.window }} | {{ row.mean_excess_pct }}% | {{ row.stdev_pct }}% | {{ row.kelly_fraction }} |{% endfor %}

The same fund, the same formula, and the answer ranges from
{% include inr.html n=k.window_min %} (bet *against* it) to {{ k.window_max }}
(borrow to hold {{ k.window_max }} times your capital), depending on which five
years you happened to feed it. {{ k.windows_negative }} of
{{ k.windows_count }} windows said short it; {{ k.windows_above_one }} said
use leverage. This is not a finding about the index fund. It's the
estimation problem made visible: five annual returns can't pin down μ, and
Kelly is very sensitive to μ. Anyone who quotes a single Kelly fraction for an
asset is quoting a guess about the future dressed as a formula.

## Doing it in Python

```python
import numpy as np

p, f, bets, players = 0.55, 0.10, 1000, 20_000
rng = np.random.default_rng(0)
wins = rng.random((players, bets)) < p
log_path = np.cumsum(np.where(wins, np.log1p(f), np.log1p(-f)), axis=1)

ever_halved = (log_path.min(axis=1) <= np.log(0.5)).mean()
median_end = np.exp(np.median(log_path[:, -1]))
print(f"ever halved: {ever_halved:.1%}   median final wealth: {median_end:.1f}x")

# the growth rate for any fraction, true p and payoff b
g = lambda f, p, b=1: p * np.log1p(b * f) + (1 - p) * np.log1p(-f)
print([round(g(x, 0.52) * 100, 3) for x in (0.05, 0.10)])   # believed 0.55, truth 0.52
```

Change `p` to 0.52 while leaving `f` at 0.10 and watch the median fall below
one: the believed edge was 0.55, the true one smaller.

## Common mistakes

- **Treating the Kelly fraction as a target.** It's a ceiling. Because
  overbetting is punished so much harder than underbetting, most people who
  use Kelly at all use a fraction of it — and still size positions with the
  cruder rules from the
  [position sizing post]({% post_url 2026-10-10-position-sizing-and-the-one-percent-rule %}).
- **Plugging in a backtested edge.** A win rate from your own backtest is the
  most optimistic estimate you'll ever have — see
  [backtesting honestly]({% post_url 2026-10-15-how-to-backtest-honestly %}).
  If the true edge is even a few points smaller, full Kelly on the backtest
  can shrink your money.
- **Assuming markets are coins.** The coin has fixed odds, independent
  tosses and a known payoff. Markets have fat tails, gaps through stops,
  changing odds and bets that move together. Ten "independent" positions in
  correlated stocks are closer to one big bet, as the
  [diversification post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %})
  showed — and Kelly sized as if they were ten is overbetting.
- **Reading "never goes broke" as "safe".** A fraction bet never reaches
  exactly zero, but a 90% drawdown is ruin in every sense that matters — for
  your plans and for your nerve.

**Takeaway:** Kelly tells you the stake that grows capital fastest *if you
know your edge exactly* — and even then it means a coin-flip chance of
halving along the way. You never know your edge exactly, and betting double
the true Kelly fraction grows nothing. The formula's real lesson is
directional: when unsure, bet smaller.
