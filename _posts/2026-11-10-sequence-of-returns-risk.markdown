---
layout: post
title: "Sequence-of-returns risk: the same twenty years, in a different order"
description: "Reorder twenty real annual returns and a ₹10,000 SIP ends anywhere from ₹27 lakh to ₹2.6 crore. Why the order of returns matters when money moves in or out."
image: /assets/og/sequence-of-returns-risk.png
date: 2026-11-10 09:00:00 +0530
series: risk
term: "Sequence-of-returns risk"
---

{% assign rk = site.data.risk %}
{% assign d = rk.dataset %}
{% assign s = rk.sequence_of_returns %}
{% assign act = s.orders.actual %}
{% assign best = s.orders.best_first %}
{% assign worst = s.orders.worst_first %}

## A risk that doesn't show up in any return figure

Most return statistics on this blog — point-to-point CAGR, volatility,
Sharpe — are computed from a sequence of returns, and none of them cares
about the *order* of that sequence. Shuffle twenty years of annual returns
and the CAGR is identical. So is the volatility. (XIRR is the exception: it's
built from your own cash flows, so order matters to it — which is exactly why
two SIP investors in the same fund can end up with very different XIRRs.)

Your money, however, cares enormously — as long as money is moving in or out
along the way. A crash in year one of a SIP and a crash in year twenty are
the same return statistic and completely different outcomes. That gap is
**sequence-of-returns risk**, and it's the reason the
[SIP post's]({% post_url 2026-10-24-sips-xirr-and-timing-myths %}) Jan 2007 investor
and its twenty-year investor had such different experiences with the same
fund.

## The setup

Take {{ d.fund_name }}'s {{ d.fund_plan }} and its {{ s.years }} financial-year
returns, {{ s.first_fy }} to {{ s.last_fy }} — the same twenty numbers the
[arithmetic of losses post]({% post_url 2026-11-06-the-arithmetic-of-losses %})
tabulated. Source: [AMFI via mfapi.in]({{ d.fund_source_url }}), data to
{{ d.as_of }}. Historical data, for illustration only.

Now run them in three orders:

| Order | First three years | Last three years |
|---|---|---|
| **Actual** ({{ s.first_fy }} → {{ s.last_fy }}) | {{ act.first_three_fy_pct | join: "%, " }}% | {{ act.last_three_fy_pct | join: "%, " }}% |
| **Best years first** | {{ best.first_three_fy_pct | join: "%, " }}% | {{ best.last_three_fy_pct | join: "%, " }}% |
| **Worst years first** | {{ worst.first_three_fy_pct | join: "%, " }}% | {{ worst.last_three_fy_pct | join: "%, " }}% |

Same twenty returns in every row. Same average, same CAGR, same volatility.

## Case one: a lump sum doesn't care

₹{% include inr.html n=s.lump_sum_start %} invested at the start and left alone
for {{ s.years }} years ends at **₹{% include inr.html n=s.lump_sum_end_any_order %}** in
all three orders. Multiplication commutes: (1+a)(1+b) is (1+b)(1+a). If
nothing goes in or out, the order of returns is irrelevant to where you end
up — and the CAGR on every factsheet you've ever read is silently a lump-sum
statistic.

## Case two: a SIP cares a great deal

Now put ₹{% include inr.html n=s.sip_monthly %} a month in for the same twenty
years — ₹{% include inr.html n=s.sip_invested %} in total, each year's return
applied evenly across its twelve months:

![SIP value under three orderings of the same twenty annual returns]({{ '/assets/charts/risk-sequence.svg' | relative_url }})

| Order | Final value |
|---|---:|
| Actual | ₹{% include inr.html n=act.sip_final %} |
| Best years first | **₹{% include inr.html n=best.sip_final %}** |
| Worst years first | **₹{% include inr.html n=worst.sip_final %}** |

Ten times. Not 10% — a factor of ten between the best and worst ordering of
*exactly the same returns*.

The reason is mechanical. With a SIP, most of your money is in the fund
during the *later* years — the last year's returns act on twenty years of
accumulated contributions, the first year's on a few months' worth. So the
late returns dominate. Worst-years-first puts {{ worst.first_three_fy_pct | first }}%
on almost nothing and +{{ worst.last_three_fy_pct | last }}% on the full pile.
Best-years-first does the reverse, and turns ₹24 lakh of contributions into
barely ₹27 lakh.

Notice which way this cuts. For someone *accumulating*, an early crash is the
good sequence — cheap units when the pile is small, growth when it's large.
The Jan 2007 SIP investor from the earlier post lived through the bad
version: five years of contributions, a crash landing on the accumulated
pile, and a return of nothing. They weren't unlucky about *what* happened.
They were unlucky about *when*.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Suppose you get ₹10 pocket money every week and keep it in a jar. Some weeks
a magic jar doubles what's inside; some weeks it halves it.

If the halving weeks come *first*, they hurt a jar with ₹10 or ₹20 in it — no
big deal. The doubling weeks then come when the jar is full. Great.

If the doubling weeks come first, they double ₹10 into ₹20 — nice, but small.
Then the halving weeks come when the jar has hundreds in it. Ouch.

Same number of doublings and halvings. The order decides whether you end up
rich or annoyed.

</details>

## Case three: a retiree cares in the opposite direction

Flip the cash flows. Start with ₹{% include inr.html n=s.swp_start %} and
withdraw ₹{% include inr.html n=s.swp_monthly %} a month — a **SWP**, a
Systematic Withdrawal Plan — for twenty years, against the same three
orderings:

| Order | Balance after {{ s.years }} years |
|---|---:|
| Actual | ₹{% include inr.html n=act.swp_final %} |
| Best years first | **₹{% include inr.html n=best.swp_final %}** |
| Worst years first | **₹0 — money ran out in year {{ worst.swp_depleted_year | round }}** |

Now the early years dominate, because that's when the pile is largest and the
withdrawals are eating into a falling balance. The ordering that was best for
the saver is fatal for the spender: worst-years-first empties the account in
about {{ worst.swp_depleted_year }} years, while best-years-first leaves it
five times its starting size after two decades of withdrawals.

This is why the [drawdown post's]({% post_url 2026-10-22-drawdown %}) recovery
times matter so much more to someone withdrawing than to someone
accumulating. A six-year recovery is a long wait when you're adding money.
It's a hole you may never climb out of when you're taking money out every
month during the fall.

## What you can actually do about it

You can't choose your sequence. You can change how exposed you are to it:

- **When accumulating, sequence risk is mostly on your side** — early crashes
  help. The exposure is in the last few years before you need the money,
  when the pile is largest. That's the honest case for gradually reducing
  equity as a goal approaches: not because returns will be worse, but because
  a bad *sequence* at that point can't be waited out.
- **When withdrawing, the first few years are everything.** A cash buffer
  covering a couple of years of withdrawals, so that a crash early in
  retirement is met by spending cash rather than selling units at the low, is
  the standard defence. It costs return in good sequences and saves the
  portfolio in bad ones.
- **Judge SIP outcomes with this in mind.** Two people, same fund, same
  monthly amount, same discipline, five years apart — very different XIRRs.
  Neither is a verdict on the fund or on the habit.

## Doing it in Python

```python
import pandas as pd, numpy as np

nav = pd.read_csv("uti-nifty50-index-fund-nav.csv",
                  parse_dates=["date"]).set_index("date").nav_regular_growth.dropna()
fy = nav.groupby(nav.index.to_period("Q-MAR").asfreq("Y-MAR")).last()
fy = pd.concat([pd.Series({fy.index[0] - 1: nav.iloc[0]}), fy])
annual = fy.pct_change().dropna().values          # 20 FY returns

def sip(returns, monthly=10000):
    v = 0.0
    for R in returns:
        m = (1 + R) ** (1/12) - 1
        for _ in range(12):
            v = (v + monthly) * (1 + m)
    return v

for name, seq in {"actual": annual,
                  "best first": np.sort(annual)[::-1],
                  "worst first": np.sort(annual)}.items():
    print(f"{name:12s} SIP ends at Rs {sip(seq):,.0f}   "
          f"lump sum x{np.prod(1 + seq):.2f}")
```

The lump-sum multiple prints the same number three times. The SIP doesn't.
That contrast is the entire post.

## Common mistakes

- **Using a fund's CAGR to project a SIP or a retirement.** CAGR is
  order-blind. Your cash flows aren't.
- **Concluding a SIP "didn't work" from a bad five-year stretch.** The same
  contributions in a different order would have compounded fine. The habit
  wasn't the problem; the sequence was.
- **Holding the same asset mix while saving and while spending.** The two
  face opposite sequence risks. Early volatility helps one and can ruin the
  other.
- **Treating a big final pot as proof of skill.** Someone whose best years
  landed last did well partly because of when they were born. So did someone
  whose crash came first.
- **Assuming a cash buffer is "wasted" return.** It is, in good sequences.
  It's the only thing that works in bad ones, and you don't get to know which
  you'll have.

**Takeaway:** Twenty real annual returns, reordered, take the same
₹10,000-a-month SIP anywhere from ₹27 lakh to ₹2.6 crore — and empty or
quintuple a retiree's ₹50 lakh — while a lump sum ends at the same figure
every time. Returns don't care about order. Money moving in or out does, and
the years when the most money is exposed are the ones that decide.
