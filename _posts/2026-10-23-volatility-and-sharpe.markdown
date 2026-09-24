---
layout: post
title: "Volatility and Sharpe: was the return worth the ride?"
description: "Two funds return 12% very differently. Standard deviation as a measure of the ride, the Sharpe ratio, and the assumptions Sharpe quietly makes about returns."
image: /assets/og/volatility-and-sharpe.png
date: 2026-10-23 09:00:00 +0530
series: mutual-funds
term: "Sharpe ratio and volatility"
---

{% assign mf = site.data.mf %}
{% assign f = mf.index_fund %}
{% assign v = mf.volatility_and_sharpe %}

## Return alone doesn't settle anything

Two funds both return 12% a year. One drifts up steadily; the other lurches
between +40% and −25%. Same destination, and almost nobody would call them
equally good.

To say why, you need a number for the lurching. That number is
**volatility**, and once you have it you can ask the more useful question:
how much return did each unit of lurching buy?

## Volatility

Volatility is the standard deviation of returns — how widely daily (or
monthly) returns scatter around their average.

```
1. Compute daily returns:        rₜ = NAVₜ / NAVₜ₋₁ − 1
2. Take their standard deviation: σ_daily
3. Annualise:                     σ_annual = σ_daily × √252

(252 ≈ trading days in a year. Use √12 for monthly data.)
```

The √ comes from variance scaling with time while standard deviation scales
with its square root — which assumes returns are independent day to day.
That's an approximation, and it's worth knowing it's an approximation.

For this fund, over {{ f.years_of_history }} years:

| | |
|---|---:|
| Annualised return | {{ v.annualised_return_pct }}% |
| Annualised volatility | **{{ v.annualised_volatility_pct }}%** |

{{ f.name }}, {{ f.plan_regular }}, {{ v.period }}. Source:
[AMFI via mfapi.in]({{ f.source_url }}). Historical data, for illustration only.

A volatility of {{ v.annualised_volatility_pct }}% means that in a typical year, returns landed roughly
within ±21 percentage points of the average — very roughly, two years in
three. It's a diversified large-cap index fund, and it is still a
substantially bouncy thing to own.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Two friends walk to school and both take 20 minutes on average.

One takes 19, 20, 21, 20 minutes — boringly reliable. The other takes 8
minutes, then 35, then 12, then 25. Same average, wildly different
experience. You can plan around the first friend; you can't around the second.

Volatility is a number for how unpredictable the second friend is.

And the Sharpe ratio asks the follow-up question: if the unreliable friend
got there *faster on average*, was the unpredictability worth it?

</details>

## The Sharpe ratio

Devised by William Sharpe in 1966, this is the standard measure of
**risk-adjusted return** — return per unit of volatility, over and above what
a risk-free asset pays:

```
             Portfolio Return − Risk-Free Rate
Sharpe =    ──────────────────────────────────
                     Volatility
```

The risk-free rate belongs there because you could have earned it without any
volatility at all. Only the *excess* over that is compensation for taking
risk. In India, the 10-year government bond yield is the usual proxy.

For this fund:

| | |
|---|---:|
| Annualised return | {{ v.annualised_return_pct }}% |
| Less: risk-free rate | {{ v.risk_free_pct }}% |
| Excess return | {{ v.annualised_return_pct | minus: v.risk_free_pct | round: 2 }}% |
| ÷ Volatility | {{ v.annualised_volatility_pct }}% |
| **Sharpe ratio** | **{{ v.sharpe }}** |

## That is not a good number

A Sharpe of {{ v.sharpe }} means each unit of volatility bought about {{ v.sharpe }} units of excess
return. Conventional rules of thumb call anything above 1 good and below 0.5
poor.

This series is not going to dress that up. Over this particular twenty-year
window, a Nifty 50 index fund delivered a fairly unimpressive amount of
return for the volatility endured.

But notice the phrase doing the work: *this particular window*. The
[point-to-point post]({% post_url 2026-10-19-point-to-point-returns %}) showed this window
starts near an April 2006 high and ends after a weak Q1 2026, and that the
whole-period return of {{ v.annualised_return_pct }}% sits below the {{ mf.rolling_returns.years_5.median }}% median of five-year rolling
windows. Sharpe inherits that problem completely — the numerator is a
point-to-point return, so a Sharpe ratio is exactly as start-date-dependent
as the return inside it.

Which is the real lesson. A Sharpe ratio quoted without its measurement
period is not a fact about a fund.

## What Sharpe misses

Three limitations worth carrying.

**It treats upside and downside identically.** Standard deviation punishes a
+15% month exactly as much as a −15% month. But investors do not experience
those symmetrically at all. The **Sortino ratio** exists for this reason — it
divides by downside deviation only, counting just the falls.

**It assumes returns are normally distributed.** They aren't. Real market
returns have fat tails: extreme events happen far more often than a normal
distribution predicts. The 2008 crash covered in the
[drawdown post]({% post_url 2026-10-22-drawdown %}) was a many-standard-deviation event
that a normal distribution says should essentially never occur.

**It says nothing about how long you suffered.** A fund can post a decent
Sharpe while spending six years below its previous peak — as this one did.
Sharpe and drawdown recovery measure genuinely different things, and neither
substitutes for the other.

## Comparing funds with it

Sharpe is most useful comparatively, and only under strict conditions: the
same measurement period, the same risk-free rate, the same data frequency,
and comparable asset classes. Change any of those and the comparison breaks.

Comparing a debt fund's Sharpe to an equity fund's is particularly
meaningless — a low-volatility fund can post a flattering Sharpe on modest
returns simply because the denominator is small.

## Doing it in Python

```python
import pandas as pd, numpy as np

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date")
r = nav.nav_regular_growth.dropna()

daily = r.pct_change().dropna()
vol = daily.std() * np.sqrt(252) * 100

years = (r.index[-1] - r.index[0]).days / 365.25
ann_return = ((r.iloc[-1] / r.iloc[0]) ** (1/years) - 1) * 100

for rf in (6.0, 6.5, 7.0):
    print(f"rf {rf}%  ->  Sharpe {(ann_return - rf)/vol:.3f}")
```

Run that loop and notice how much the assumed risk-free rate moves the
answer — a percentage point of risk-free rate shifts Sharpe by about 0.05
here. Another reason to distrust a Sharpe quoted to two decimals without its
assumptions.

## Common mistakes

- **Quoting Sharpe without the period and risk-free rate.** Both change the
  answer materially; neither is usually disclosed.
- **Comparing Sharpe across asset classes.** A liquid fund can out-Sharpe an
  equity fund while returning far less.
- **Treating volatility as risk.** Volatility is fluctuation. The risk that
  matters is permanent loss, or being forced to sell at a bad moment.
- **Forgetting the normality assumption.** Fat tails mean the worst cases are
  worse than the maths implies.
- **Using monthly data and comparing to daily-data figures.** Monthly
  sampling smooths away volatility and inflates Sharpe.
- **Assuming a higher Sharpe means a better fund for you.** It measures
  efficiency, not suitability — and says nothing about how long you'd have
  spent underwater.

**Takeaway:** Volatility measures how much returns scatter, and Sharpe asks
how much excess return each unit of that scatter bought. This fund's {{ v.sharpe }} over
twenty years is a genuinely unflattering figure — and since its numerator is
a point-to-point return, it's every bit as sensitive to the chosen start date
as any other single-window number in this series.
