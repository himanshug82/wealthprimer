---
layout: post
title: "Survivorship bias in fund performance tables"
description: "Fund tables show only the funds still alive. A zero-skill simulation shows how closing the laggards makes survivors look better than the funds that started."
image: /assets/og/survivorship-bias-in-fund-tables.png
date: 2026-11-01 09:00:00 +0530
series: mutual-funds
term: "Survivorship bias"
---

{% assign m = site.data.mf4 %}
{% assign sv = m.survivorship %}

## What survivorship bias is

Survivorship bias is what happens when you study only the things that are still around, and the ones that dropped out would have changed the answer.

For funds, the dropouts are the schemes that were merged into a sibling or wound up. In our view their track records often drop out of the tables you see later, so a ten-year table lists the funds that made it to year ten. The weak ones aren't in it, and the average looks better than the group that started.

Earlier posts mentioned this in passing: the [benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %}) and the [star ratings post]({% post_url 2026-10-16-why-star-ratings-mislead %}) both note that the peer group is missing its worst members. This post measures it, on a case where we know the truth. It's part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).

## How to measure it

```
Survivorship gap = metric for the funds still alive
                   − same metric for every fund that started
```

In real data you can't do this, because the closed funds' records are hard to find. In a simulation you can. We build a world where every fund is identical in skill, close some of them, and look at what the survivors' table says.

## A simulated world with no skill

This is a simulation, not market data. It uses a fixed random seed (seed {{ sv.seed }}), so the results are the same every time you run it.

- {{ sv.funds }} funds start together and run for {{ sv.years }} years ({{ sv.months }} months).
- Every fund earns the benchmark's return, less costs of {{ sv.cost_per_month_pct }}% a month, plus random luck with a standard deviation of {{ sv.noise_sd_monthly_pct }}% a month. **No fund has any skill.** Any difference between funds is luck and costs.
- The benchmark compounds at about {{ sv.benchmark_cagr_pct }}% a year in this run.
- {{ sv.rule }}

The closing rule is our assumption. Real funds are merged or closed for many reasons, not just recent performance (small size, a change of plan), and we haven't measured how often. The point here is the direction of the effect, not its size.

| Year-end | Funds closed | Funds remaining |
|---|---:|---:|
{% for rv in sv.reviews -%}
| Year {{ rv.month | divided_by: 12 }} | {{ rv.closed }} | {{ rv.alive_after }} |
{% endfor %}

By year {{ sv.years }}, {{ sv.survivors }} of the {{ sv.funds }} funds are left, or {{ sv.survivors_share_pct }}%.

## What the ten-year table shows

Here is the same simulated result read two ways. In both, the returns are identical. Only the list of funds differs.

| Ten-year result, annual return minus benchmark | Every fund that started | Survivors only |
|---|---:|---:|
| Funds counted | {{ sv.funds }} | {{ sv.survivors }} |
| Average excess return (percentage points a year) | {{ sv.all_mean_excess_pct }} | {{ sv.survivor_mean_excess_pct }} |
| Median excess return | {{ sv.all_median_excess_pct }} | {{ sv.survivor_median_excess_pct }} |
| Share of funds ahead of the benchmark | {{ sv.all_ahead_share_pct }}% | {{ sv.survivor_ahead_share_pct }}% |

Every fund in this world has zero skill. The full group trails the benchmark by a little more than its costs ({{ sv.cost_per_month_pct | times: 12 | round: 2 }} points a year, plus a small compounding drag), and about {{ sv.all_ahead_share_pct }}% of them get ahead by luck. A reader of the survivors table sees a smaller shortfall and {{ sv.survivor_ahead_share_pct }}% ahead, and could reasonably conclude something about the managers. There's nothing to conclude. The table is just missing the funds that had a bad stretch of luck.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine 100 kids enter a school race, and the slowest ones get sent home after each lap. At the end, the kids still running are fast. If you only look at that group, you'd think "children in this school are fast runners."

But you only saw the kids who stayed. The ones who were sent home were slow, and they were part of the school too. Fund tables work the same way: they show the runners still on the track.

</details>

## Doing it in Python

```python
import numpy as np

rng = np.random.default_rng(2026)
n, months = 500, 120
bench = rng.normal(0.009, 0.045, size=months)                 # one benchmark path
funds = bench + rng.normal(-0.0008, 0.012, size=(n, months))  # no skill: benchmark - costs + luck

growth = np.hstack([np.ones((n, 1)), np.cumprod(1 + funds, axis=1)])   # column m = value after m months
cagr = lambda g, m: g ** (12 / m) - 1
excess = cagr(growth[:, -1], months) - cagr(np.prod(1 + bench), months)

alive = np.ones(n, dtype=bool)
for m in range(36, 109, 12):                                   # annual reviews, years 3 to 9
    trailing = growth[:, m] / growth[:, m - 36]                # last 36 months
    candidates = np.where(alive)[0]
    worst = candidates[np.argsort(trailing[candidates])[: round(len(candidates) * 0.10)]]
    alive[worst] = False

print(f"all funds:  mean excess {excess.mean()*100:.2f} pts, ahead of benchmark {(excess > 0).mean()*100:.1f}%")
print(f"survivors:  mean excess {excess[alive].mean()*100:.2f} pts, ahead {(excess[alive] > 0).mean()*100:.1f}%  ({alive.sum()} of {n})")
```

Change the closing rule or the cost, and watch how the gap moves.

## Common mistakes

- **Reading a category average as if it were the whole category.** It's the average of what's left. The [benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %}) calls out the same trap.
- **Treating a "share of funds beating the index" figure as complete.** Ask whether the count includes funds that were closed or merged during the period, and check before you rely on it.
- **Using a list of top performers as evidence of skill.** A list built from past results has already selected on those results. See the [star ratings post]({% post_url 2026-10-16-why-star-ratings-mislead %}) for the same problem in rating form.
- **Taking the simulation as a measurement.** The direction holds in every run: closing laggards lifts the survivors' average. The size depends on the closing rule, which is assumed here. This post doesn't quote a real survival rate because we haven't verified one.

## Sources

- [SEBI Master Circular for Mutual Funds (20 March 2026)](https://www.sebi.gov.in/legal/master-circulars/mar-2026/master-circular-for-mutual-funds_100491.html): SEBI's rules on scheme mergers and consolidation, one way funds drop out of tables.
- [AMFI, net asset value data](https://www.amfiindia.com/net-asset-value): AMFI's NAV data.

**Takeaway:** A table of today's funds leaves out the ones that were closed or merged, which makes the group look better than the one that started. In a world where no fund has any skill, closing the laggards still leaves a survivors' table that looks respectable.
