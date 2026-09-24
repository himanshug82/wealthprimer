---
layout: post
title: "Concentration risk: when one stock is most of what you own"
description: "ESOPs, a family business, one favourite share: what holding a single stock does to volatility and drawdowns, measured on two years of real prices."
image: /assets/og/concentration-risk.png
date: 2026-10-18 09:00:00 +0530
series: risk
term: "Concentration risk"
---

{% assign r2 = site.data.risk2 %}
{% assign d = r2.dataset %}
{% assign c = r2.concentration %}
{% assign ps = c.portfolios.stock %}
{% assign p7 = c.portfolios.seventy %}
{% assign ph = c.portfolios.half %}
{% assign pi = c.portfolios.index %}

## The portfolio nobody chose

Plenty of Indian investors hold one stock as most of their wealth without
ever deciding to. An engineer whose ESOPs (employee stock options) and RSUs
(restricted stock units) have vested for eight years. A family whose savings
sit in the listed company a grandparent founded. Someone who bought one share
early, watched it multiply, and never trimmed.

**Concentration risk** is the risk that comes from a large share of your
money depending on a single company, sector or source. It isn't that the one
stock is bad. It's that you're exposed to everything that can happen to *one*
business — a lost contract, a fraud, a regulatory change, a management
mistake — with nothing else in the portfolio to absorb it.

This post measures that on real prices. Britannia is used only because this
blog already has its price history; nothing here is a view on the company.

## The formula

```
A stock's variance splits into two parts:

    σ²(stock)  =  β² × σ²(market)   +   σ²(specific)
                  └ moves with the market ┘   └ the company's own news ┘

Share of the stock's variance the market explains  =  ρ²
Share that is company-specific                     =  1 − ρ²

A portfolio with weight w in the stock and (1 − w) in the index:

    σ²(portfolio)  =  w²σ²(stock) + (1 − w)²σ²(index) + 2·w·(1 − w)·ρ·σ(stock)·σ(index)
```

The first line is the key. Market risk is shared by everything you could own;
diversification can't remove it. The company-specific part is the risk that
diversification *does* remove — which is the only reason to hold more than
one thing. A concentrated portfolio keeps it, all of it. Beta (β) and
correlation (ρ) are explained in the
[beta post]({% post_url 2026-10-02-beta %}) and the
[diversification post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %}).

## Worked example: ₹10 lakh, four ways, April 2024 to March 2026

Britannia (NSE: BRITANNIA) daily closing prices and the Nifty 50 price
index, {{ c.start | date: "%-d %B %Y" }} to {{ c.end | date: "%-d %B %Y" }}
({{ c.days }} common trading days; sources:
[Yahoo Finance, BRITANNIA.NS]({{ d.britannia_source_url }}) and
[Yahoo Finance, ^NSEI]({{ d.nifty_source_url }})). Both are *price* series — dividends
excluded on both sides, so the comparison is like for like. Historical data,
for illustration only.

Over this window Britannia's correlation with the index was **{{ c.rho }}**,
so the market explained about **{{ c.systematic_share_pct | round }}%** of its
daily variance. The other {{ c.specific_share_pct | round }}% was
Britannia's own.

Four ₹{% include inr.html n=c.start_value %} portfolios, bought on day one and
left alone:

| | 100% Britannia | 70% Britannia / 30% index | 50 / 50 | 100% Nifty 50 |
|---|---:|---:|---:|---:|
| Value at the end (₹) | {% include inr.html n=ps.end_value %} | {% include inr.html n=p7.end_value %} | {% include inr.html n=ph.end_value %} | {% include inr.html n=pi.end_value %} |
| Return over the period | {{ ps.return_pct }}% | {{ p7.return_pct }}% | {{ ph.return_pct }}% | {{ pi.return_pct }}% |
| Annualised volatility | {{ ps.vol_pct }}% | {{ p7.vol_pct }}% | {{ ph.vol_pct }}% | {{ pi.vol_pct }}% |
| Maximum drawdown | {{ ps.max_dd_pct }}% | {{ p7.max_dd_pct }}% | {{ ph.max_dd_pct }}% | {{ pi.max_dd_pct }}% |
| Maximum drawdown (₹) | {% include inr.html n=ps.max_dd_rupees %} | {% include inr.html n=p7.max_dd_rupees %} | {% include inr.html n=ph.max_dd_rupees %} | {% include inr.html n=pi.max_dd_rupees %} |
| Worst 21-trading-day return | {{ ps.worst_21d_pct }}% | {{ p7.worst_21d_pct }}% | {{ ph.worst_21d_pct }}% | {{ pi.worst_21d_pct }}% |
| Lowest value reached (₹) | {% include inr.html n=ps.lowest_value %} | {% include inr.html n=p7.lowest_value %} | {% include inr.html n=ph.lowest_value %} | {% include inr.html n=pi.lowest_value %} |

![Drawdowns of the single-stock, 50/50 and index portfolios]({{ '/assets/charts/risk2-concentration.svg' | relative_url }})

Read it honestly, because it cuts both ways.

**The single stock ended ahead.** Over these particular two years,
100% Britannia returned {{ ps.return_pct }}% while the index returned
{% include inr.html n=pi.return_pct %}%, a gap of {{ c.stock_minus_index_pp }} percentage points.
Concentration can do that — it's the reason people stay concentrated.

**The ride was much rougher.** The one-stock portfolio fell
{{ ps.max_dd_pct | abs }}% from its peak
({{ ps.peak_date | date: "%-d %B %Y" }}) to its trough
({{ ps.trough_date | date: "%-d %B %Y" }}) — ₹{% include inr.html n=ps.max_dd_rupees %}
on paper — against {{ pi.max_dd_pct | abs }}% for the index. Its
volatility was {{ ps.vol_pct }}% against {{ pi.vol_pct }}%. Every step of
diversification in the table narrows the swings. The 50/50 mix's volatility
was close to the index's ({{ ph.vol_pct }}% against {{ pi.vol_pct }}%), though
its drawdown was still deeper.

**One path isn't the distribution.** This is the part a two-year chart can't
show. The index's result is roughly what an index holder gets, give or take.
A single stock's result is one draw from a very wide range. The
company-specific part — {{ c.specific_share_pct | round }}% of the variance here — happened to
help this time; it could as easily have hurt, and for some companies it ends
at zero. Looking at the one stock you happened to hold, after it did well, is
survivorship bias in miniature.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your whole class bets on the cricket score. Some kids bet on the total runs
of the whole team. One kid bets everything on one batter.

When the team has a normal day, the team-bettors get a normal result. The
one-batter kid gets either a big win (century!) or nothing (duck!). Over a
season, the team-bettors' results cluster together. The one-batter kids'
results are all over the place — a few very happy, some very sad.

Holding one stock is being the one-batter kid. It isn't wrong to be lucky.
It's just that you can't tell, in advance, whether you're the century or the
duck.

</details>

## The ESOP problem: two bets on one company

For an employee, concentration is worse than the table suggests, because the
paycheck is a second position in the same company. If the business hits
trouble, the share price, the bonus and possibly the job can all go at once —
exactly when you'd want your savings to be doing something different from
your income. That's correlation again, just between your portfolio and your
career.

There are practical frictions too. Vesting schedules and lock-ins decide when
shares can be sold. Employees classed as "designated persons" under their
company's insider-trading code can only trade in open trading windows. And
selling has tax consequences at vesting and at sale — the tax series covers
how ESOPs and RSUs are taxed. None of these makes concentration less risky;
they make it slower to reduce.

## Doing it in Python

```python
import pandas as pd, numpy as np

brit = pd.read_csv("britannia-ohlcv-2024-04-to-2026-03.csv",
                   parse_dates=["date"]).set_index("date").close
nifty = pd.read_csv("nifty50-price-index.csv",
                    parse_dates=["date"]).set_index("date").nifty50_pri_close
px = pd.concat([brit, nifty], axis=1, keys=["stock", "index"], sort=True).dropna()
rel = px / px.iloc[0]

for w in (1.0, 0.7, 0.5, 0.0):
    v = 10_00_000 * (w * rel.stock + (1 - w) * rel["index"])   # buy and hold
    dd = (v / v.cummax() - 1).min()
    vol = v.pct_change().std() * np.sqrt(252)
    print(f"{w:.0%} stock: end {v.iloc[-1]:,.0f}  vol {vol:.1%}  max drawdown {dd:.1%}")

print("market's share of the stock's variance:",
      round(px.pct_change().corr().iloc[0, 1] ** 2, 3))
```

## Common mistakes

- **Judging concentration by how it turned out.** A concentrated position
  that did well looks like conviction; one that did badly looks like a
  mistake. Both were the same risk. Judge the size of the bet, not the
  outcome.
- **Counting the stock at its peak value.** A holding that has multiplied
  feels like "house money". A
  [drawdown]({% post_url 2026-09-29-drawdown %}) of
  {{ ps.max_dd_pct | abs }}% on a position that's half your net
  worth is a real loss, whatever you originally paid.
- **Forgetting your job is a position.** Salary, bonus and ESOPs from one
  employer are one exposure, not three.
- **Thinking a sector fund or a handful of related stocks fixes it.** Five
  private banks or three group companies share most of their risk. Check how
  they move together, not how many there are.
- **Assuming the market will warn you.** Company-specific shocks —
  accounting problems, a lost licence — often arrive as a gap, not a trend.
  The [arithmetic of losses]({% post_url 2026-10-09-the-arithmetic-of-losses %})
  applies to them with no time to react.

**Takeaway:** Concentration widens the range of outcomes, because it keeps
the company-specific risk that diversification would have removed. Over these two years a single stock beat
the index and fell nearly twice as far on the way. You can't know in advance
which side of the range your one stock will land on.
