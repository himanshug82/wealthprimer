---
layout: post
title: "The arithmetic of losses: why −50% needs +100%"
description: "Losses and gains aren't symmetric, and the average return you're quoted isn't the return you get. Volatility drag, worked on twenty years of a real index fund."
image: /assets/og/the-arithmetic-of-losses.png
date: 2026-11-06 09:00:00 +0530
series: risk
term: "Volatility drag"
---

{% assign rk = site.data.risk %}
{% assign d = rk.dataset %}
{% assign a = rk.arithmetic_of_losses %}

## Two facts that are easy to know and hard to feel

The [last post]({% post_url 2026-11-05-what-the-fo-numbers-actually-say %}) was about a base
rate. This one is about arithmetic — two pieces of it that every investor
"knows" and almost nobody prices in.

**Fact one: losses and gains are not symmetric.** Lose half your money and a
50% gain does not get you back. You need 100%.

**Fact two: the average return is not the return you get.** A fund whose
yearly returns average 13% does not turn ₹1 lakh into what 13% a year would.
It turns it into less — and the bouncier the ride, the bigger the gap.

Neither is a market opinion. Both are consequences of multiplication, and both
show up in real data.

## The formula

```
Gain needed to recover from a loss L (as a fraction):

    G  =  1 / (1 − L)  −  1

Volatility drag (approximation):

    Geometric mean  ≈  Arithmetic mean  −  σ² / 2

where σ is the standard deviation of the periodic returns.
```

σ (sigma) is the
[standard deviation]({% post_url 2026-10-23-volatility-and-sharpe %}) — a
measure of how widely returns swing around their own average.

## Part one: the recovery table

![Gain needed to break even against loss from peak]({{ '/assets/charts/risk-recovery.svg' | relative_url }})

| Loss from peak | Gain needed to break even |
|---:|---:|{% for row in a.recovery_table %}
| −{{ row.loss_pct }}% | **+{{ row.gain_needed_pct }}%** |{% endfor %}

The curve bends upward, and it bends hard. A 10% loss needs an 11% gain —
close enough to symmetric that you'd never notice. A 50% loss needs 100%. A
90% loss needs a tenfold rise.

This is why the [drawdown post]({% post_url 2026-10-22-drawdown %}) made such a
point of recovery *time*. When {{ d.fund_name }} fell {{ a.gfc_fall_pct }}% from
its January 2008 peak, getting back did not require a {{ a.gfc_fall_pct | abs }}% rise.
It required **+{{ a.gfc_gain_needed_pct }}%** — which is why the wait was nearly
six years, even though the year right after the crash was spectacular
(+{{ a.fy10_pct }}% in FY10).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You have 100 marbles. You lose half — 50 left. Now you win back "half" —
half of *what you have*, which is 25. You've got 75. You lost 50 and won 50%,
and you're still 25 short.

To get back to 100 from 50 you need to *double* what you have. Losing half
and winning half aren't opposites, because "half" is measured from a smaller
pile the second time.

</details>

## Part two: the average that lies

Here are the financial-year returns of {{ d.fund_name }}'s
{{ d.fund_plan }} for every full year in the data — 1 April to 31 March,
{{ a.years }} years:

| Year | Return | | Year | Return |
|---|---:|---|---|---:|{% assign half = a.years | divided_by: 2 %}{% for i in (0..9) %}{% assign j = i | plus: half %}{% assign x = a.fy_returns[i] %}{% assign y = a.fy_returns[j] %}
| {{ x.fy }} | {{ x.return_pct }}% | | {{ y.fy }} | {{ y.return_pct }}% |{% endfor %}

Source: [AMFI via mfapi.in]({{ d.fund_source_url }}), data to {{ d.as_of }}.
Historical data, for illustration only.

Add those twenty numbers up and divide by twenty:

| | |
|---|---:|
| **Arithmetic mean** of the yearly returns | **{{ a.arithmetic_mean_pct }}%** |
| Actual compound annual growth (CAGR) | **{{ a.geometric_mean_pct }}%** |
| Gap — the volatility drag | {{ a.drag_pp }} percentage points |
| Standard deviation of yearly returns | {{ a.fy_return_stdev_pct }}% |
| σ²/2 approximation of the drag | {{ a.drag_approx_pp }} percentage points |

The fund's yearly returns *averaged* {{ a.arithmetic_mean_pct }}%. Its actual
growth rate — the CAGR the
[point-to-point returns post]({% post_url 2026-10-19-point-to-point-returns %}) defined —
was {{ a.geometric_mean_pct }}%. Nearly three percentage points a year went
missing, and nobody took them. They were consumed by the bouncing.

Put money on it:

| ₹1,00,000 invested for {{ a.years }} years | Ends at |
|---|---:|
| If it had grown at the {{ a.arithmetic_mean_pct }}% "average" every year | ₹{% include inr.html n=a.lakh_at_arithmetic_mean %} |
| What it actually became (NAV {{ a.start_nav }} → {{ a.end_nav }}) | **₹{% include inr.html n=a.lakh_actual %}** |

The "average return" version is worth about 66% more than the real one. Same
twenty years, same fund. The only difference is that one number describes
what happened and the other describes something that never did.

## Why the bouncing costs money

Look at {{ a.worst_fy }} and FY10 in the table. {{ a.worst_fy }} was
{{ a.fy09_pct }}%; the next year was **+{{ a.fy10_pct }}%**, the second-best year in
twenty. The arithmetic average of those two years is a healthy
+{{ a.fy09_pct | plus: a.fy10_pct | divided_by: 2.0 | round: 1 }}% a year.

Compound them instead — which is what your money actually does:

```
(1 − 0.363) × (1 + 0.718)  =  0.637 × 1.718  =  1.095
```

Two years, a {{ a.fy09_fy10_compound_pct }}% total gain. About 4.6% a year, not
{{ a.fy09_pct | plus: a.fy10_pct | divided_by: 2.0 | round: 1 }}%. A fall followed by an even larger
rise still left the investor barely ahead, because the rise was earned on the
smaller, post-fall amount. That is the recovery table from part one, and it
is the whole mechanism of volatility drag: the more a return series swings,
the more of its arithmetic average gets eaten on the way to becoming an
actual compound return.

The σ²/2 shortcut tells you roughly how much. Yearly returns with a standard
deviation of {{ a.fy_return_stdev_pct }}% should lose about
{{ a.drag_approx_pp }} percentage points to drag; the real gap was
{{ a.drag_pp }}. Close enough to be useful, and it means one thing very
directly: **two investments with the same average return are not equal. The
smoother one compounds faster.** This is the arithmetic underneath the
[Sharpe ratio]({% post_url 2026-10-23-volatility-and-sharpe %}) — volatility
isn't just uncomfortable, it's expensive.

## Doing it in Python

```python
import pandas as pd

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date")
r = nav.nav_regular_growth.dropna()

# financial-year (Apr-Mar) returns
fy = r.groupby(r.index.to_period("Q-MAR").asfreq("Y-MAR")).last()
fy = pd.concat([pd.Series({fy.index[0] - 1: r.iloc[0]}), fy])
ret = fy.pct_change().dropna()

arith = ret.mean()
geo = (r.iloc[-1] / r.iloc[0]) ** (1 / len(ret)) - 1
print(f"arithmetic {arith:.2%}  geometric {geo:.2%}  "
      f"drag {arith - geo:.2%}  approx {ret.std(ddof=0)**2 / 2:.2%}")

# the recovery table
for loss in (0.1, 0.2, 0.5, 0.6, 0.9):
    print(f"-{loss:.0%} needs +{1 / (1 - loss) - 1:.0%}")
```

## Common mistakes

- **Mentally netting a −20% year against a +20% year.** They don't cancel.
  You're down 4%.
- **Compounding an "average return" forward.** Any projection built on an
  arithmetic average of past yearly returns overstates the result, and by
  more the bouncier the asset. Use the CAGR.
- **Treating volatility as merely emotional.** It has a rupee cost: the same
  average return with a higher standard deviation compounds to less.
- **Assuming a big up-year has "repaired" a big down-year.** +{{ a.fy10_pct }}%
  after {{ a.fy09_pct }}% left the investor up {{ a.fy09_fy10_compound_pct }}% over two
  years. Look at the level, not the headline.
- **Forgetting this applies to your own trading.** Every leveraged position,
  every stop-loss hit and re-entry, every drawdown in a trading account is a
  small version of the recovery table. The next two posts are about exactly
  that.

**Takeaway:** Losing half needs a double to recover, and a fund whose yearly
returns averaged {{ a.arithmetic_mean_pct }}% actually compounded at
{{ a.geometric_mean_pct }}% — the {{ a.drag_pp }} points in between were eaten
by volatility, not by anyone. Avoiding large losses isn't caution for its own
sake; it's the fastest way to compound.
