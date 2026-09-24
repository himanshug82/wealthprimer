---
layout: post
title: "Diversification is a correlation problem, not a counting problem"
description: "Ten funds can be one bet. What correlation does to portfolio volatility, and why how holdings move together matters far more than how many you own."
image: /assets/og/diversification-is-a-correlation-problem.png
date: 2026-11-09 09:00:00 +0530
series: risk
term: "Correlation"
---

{% assign rk = site.data.risk %}
{% assign d = rk.dataset %}
{% assign c = rk.correlation %}

## "I'm diversified — I hold eight funds"

Ask an Indian retail investor how they manage risk and the most common answer
is a count: eight funds, twenty stocks, three AMCs (asset management
companies, the firms that run mutual funds). The count feels like
safety. Often it isn't, because diversification was never about how many
things you own. It's about whether they fall at the same time.

The number that measures "at the same time" is **correlation**, and this post
is about what it does to a portfolio — with the arithmetic, and with two
years of real daily returns.

## The formula

```
Correlation (ρ) between two return series:  from −1 to +1
    +1  →  always move together, in proportion
     0  →  no linear relationship
    −1  →  always move opposite

Volatility of a two-asset portfolio (weights w₁, w₂; volatilities σ₁, σ₂):

    σ²(portfolio)  =  w₁²σ₁²  +  w₂²σ₂²  +  2·w₁·w₂·ρ·σ₁·σ₂

Many equally weighted assets, each with volatility σ, all pairwise ρ:

    σ²(portfolio)  =  σ² × [ 1/n  +  (1 − 1/n)·ρ ]
```

The middle line is the one that does the work. If ρ is 1, the portfolio
volatility is just the weighted average of the two — you've gained nothing.
Anything below 1 makes the last term smaller, and the portfolio is less
volatile than the average of its parts. That reduction is the *only* thing
diversification gives you, and ρ controls how much of it you get.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You sell ice cream. To be safe you open a second stall — also selling ice
cream, on the same beach. On a rainy day both stalls are empty. You have two
stalls and one problem.

Now suppose the second stall sells umbrellas instead. Rainy day: ice cream is
dead, umbrellas fly. Sunny day: the reverse. Some money comes in every day.

Two ice-cream stalls are "correlated" — they have good and bad days together.
Ice cream and umbrellas aren't. Owning two things only helps when they don't
have their bad days at the same time.

</details>

## Table one: what correlation does to two assets

Two assets, each with 20% annual volatility, held 50/50:

| Correlation ρ | Portfolio volatility |
|---:|---:|{% for row in c.two_asset_table %}
| {{ row.rho }} | **{{ row.portfolio_vol_pct }}%** |{% endfor %}

At ρ = 1 you own two things and get one thing's risk. How correlated are real
Indian equity funds? Two funds from this blog's data — the {{ d.fund_name }} and
Parag Parikh Flexi Cap, a flexi-cap fund that also holds foreign stocks —
correlated at {{ c.two_funds_daily_rho }} on daily returns and
{{ c.two_funds_monthly_rho }} on monthly returns,
{{ c.two_funds_window_start | slice: 0, 4 }}–{{ c.two_funds_window_end | slice: 0, 4 }}.
Two large-cap funds holding the same companies will usually sit higher still.
At ρ = 0.9 you've shaved half a percentage point. You have to get down to a correlation
near zero before the portfolio is meaningfully calmer than either piece, and
negative correlations, which are rare and unstable, are where the dramatic
reductions live.

## Table two: what adding more of the same does

Now hold *n* assets, equally weighted, each 20% volatile, every pair
correlated at {{ c.n_asset_rho }} — a generous stand-in for "a lot of Indian
equity funds", since the two real funds above were more correlated than
that:

| Holdings (n) | Portfolio volatility |
|---:|---:|{% for row in c.n_asset_table %}
| {{ row.n }} | **{{ row.portfolio_vol_pct }}%** |{% endfor %}

Going from one holding to two removes 1.6 percentage points of volatility.
Going from ten to a *thousand* removes 0.4. The formula's floor is
σ × √ρ = {{ c.rho_floor_vol_pct }}%, and no amount of counting gets below it.
That floor is the risk the holdings share — the market itself — and the only
way under it is to add things that *aren't* correlated, not more things that
are.

This is what "eight funds" usually buys: a portfolio close to the floor
({{ c.eight_asset_vol_pct }}% against {{ c.rho_floor_vol_pct }}%), with eight
[expense ratios]({% post_url 2026-10-21-expense-ratios-direct-vs-regular %}).

## Worked example: Britannia and the Nifty 50

Daily returns of Britannia (NSE: BRITANNIA) against the Nifty 50 price index,
{{ c.window_start | date: "%-d %B %Y" }} to {{ c.window_end | date: "%-d %B %Y" }}, {{ c.days }} trading days.
Sources: [Yahoo Finance, BRITANNIA.NS]({{ d.britannia_source_url }}) and
[Yahoo Finance, ^NSEI]({{ d.nifty_source_url }}). Historical data, for
illustration only.

![Scatter of Britannia daily returns against Nifty 50 daily returns]({{ '/assets/charts/risk-correlation.svg' | relative_url }})

| | |
|---|---:|
| Correlation, Britannia vs Nifty 50 | **{{ c.britannia_nifty_rho }}** |
| Beta of Britannia to the Nifty 50 (see below) | {{ c.britannia_beta }} |
| 60-day rolling correlation, lowest | {{ c.rolling_60d_min | replace: "-", "−" }} ({{ c.rolling_60d_min_date | date: "%-d %B %Y" }}) |
| 60-day rolling correlation, highest | {{ c.rolling_60d_max | replace: "-", "−" }} ({{ c.rolling_60d_max_date | date: "%-d %B %Y" }}) |
| Britannia annualised volatility | {{ c.britannia_vol_pct }}% |
| Nifty 50 annualised volatility | {{ c.nifty_vol_pct }}% |
| Naive average of the two | {{ c.naive_average_vol_pct }}% |
| **Volatility of a 50/50 portfolio** | **{{ c.portfolio_5050_vol_pct }}%** |

**Beta** measures how much a stock tends to move for each 1% move in the
index: a beta of {{ c.britannia_beta }} means Britannia moved, on average,
about {{ c.britannia_beta }}% for every 1% the Nifty 50 moved. It combines
correlation with relative volatility.

Two things here.

First, a single FMCG (fast-moving consumer goods) stock and the broad index had a correlation of only
{{ c.britannia_nifty_rho }} over these two years — lower than most people
would guess for a Nifty 50 constituent. It moved on its own news (the FY25 margin
compression the [gross margin post]({% post_url 2026-08-26-gross-margin %})
discussed, for one) as much as on the market's. And the relationship wasn't stable: over 60-day
windows it ranged from {{ c.rolling_60d_min | replace: "-", "−" }} to {{ c.rolling_60d_max }}.
Correlation is a description of a period, not a property of a stock.

Second, look at what that did to a 50/50 mix. Averaging the two volatilities
gives {{ c.naive_average_vol_pct }}%. The actual portfolio volatility was
{{ c.portfolio_5050_vol_pct }}% — barely above the index alone
({{ c.nifty_vol_pct }}%), despite half
the money sitting in a stock that was {{ c.britannia_vol_pct }}% volatile. The
low correlation ate most of Britannia's extra bounce. *That* is
diversification doing something.

For contrast, the {{ d.fund_name }} — a fund built to track that same index —
had a correlation of **{{ c.index_fund_nifty_rho }}** with it over
{{ c.index_fund_nifty_window_start | slice: 0, 4 }}–2026. Holding it alongside
another Nifty 50 fund, or alongside a large-cap fund whose top holdings are
the same fifty companies, is table one's first row. Two names, one bet.

## What this means in practice

Diversification is a question about *what moves together*, so the useful
audit isn't "how many do I hold?" but:

- Do my equity funds hold the same companies? (Overlap between large-cap
  funds can exceed half the portfolio.)
- Is everything I own priced off the same thing — Indian equity, Indian
  rates, the rupee?
- What did all of it do in March 2020, together?

The [drawdown post]({% post_url 2026-10-22-drawdown %}) showed a fifty-stock
index falling 60%. Fifty holdings didn't prevent that, because fifty Indian
large-caps in a crash have a correlation much closer to one. The things that would
have helped weren't more stocks. They were things that weren't stocks.

## Doing it in Python

```python
import pandas as pd, numpy as np

brit = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                   parse_dates=["date"]).set_index("date").close
nifty = pd.read_csv("nifty50-price-index.csv",
                    parse_dates=["date"]).set_index("date").nifty50_pri_close

rets = pd.concat([brit, nifty], axis=1, keys=["brit", "nifty"]).dropna().pct_change().dropna()
rho = rets.brit.corr(rets.nifty)
beta = rets.brit.cov(rets.nifty) / rets.nifty.var()
vol = rets.std() * np.sqrt(252) * 100

w = np.array([0.5, 0.5])
port_vol = np.sqrt(w @ rets.cov().values @ w) * np.sqrt(252) * 100
print(f"rho {rho:.2f}  beta {beta:.2f}  vols {vol.round(1).to_dict()}  "
      f"50/50 portfolio {port_vol:.1f}%")
print(rets.brit.rolling(60).corr(rets.nifty).describe().round(2))
```

`w @ cov @ w` is the two-asset formula from above, generalised to any number
of holdings — feed it a whole portfolio's return matrix and it tells you what
your diversification is actually worth.

## Common mistakes

- **Counting holdings instead of measuring correlation.** Table two: past
  ten, the count stops mattering. What you add matters.
- **Assuming two funds with different names are different bets.** Check the
  holdings. Two large-cap funds are usually one position.
- **Treating correlation as fixed.** Britannia's ran from {{ c.rolling_60d_min | replace: "-", "−" }}
  to {{ c.rolling_60d_max }} within two years. And in a crash, correlations
  between risky assets rise toward one — precisely when you need them not to.
- **Diversifying within one asset class and calling it done.** Fifty Indian
  stocks are still one exposure to Indian equity.
- **Confusing low correlation with low risk.** Britannia was *more* volatile
  than the index. It kept the 50/50 mix almost as calm as the index alone
  only because it was volatile at different times. Both facts matter.
- **Paying eight expense ratios for one portfolio.** If the funds are at the
  correlation floor, the fees are the only thing you've multiplied.

**Takeaway:** Diversification reduces risk only to the extent the things you
own fall at different times, and correlation is the number that measures
{% assign ten = c.n_asset_table | where: "n", 10 | first %}that. Ten equity funds correlated at {{ c.n_asset_rho }} get you a portfolio only about
15% less volatile than one ({{ ten.portfolio_vol_pct }}% vs {{ c.n_asset_sigma }}%), and no number of them gets
below {{ c.rho_floor_vol_pct }}% — while a single stock correlated at
{{ c.britannia_nifty_rho }} with the index cut a 50/50 portfolio's bounce almost to the index's
own. Count less; check what moves together.
