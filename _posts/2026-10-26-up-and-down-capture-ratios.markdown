---
layout: post
title: "Up and down capture ratios, explained"
description: "Capture ratios compare what a fund did in its benchmark's up and down months. How to compute them, and why benchmark, window and formula change the answer."
image: /assets/og/up-and-down-capture-ratios.png
date: 2026-10-26 09:00:00 +0530
series: mutual-funds
term: "Capture ratio (up and down)"
---

{% assign m = site.data.mf4 %}
{% assign c = m.capture %}
{% assign h = c.hybrid_vs_tri_10y %}
{% assign h5 = c.hybrid_vs_tri_5y %}
{% assign hp = c.hybrid_vs_pri_10y %}
{% assign ix = c.index_vs_tri_10y %}
{% assign ixp = c.index_vs_pri_10y %}
{% assign src = m.sources %}

## What a capture ratio tells you

A capture ratio compares what a fund did in the months its benchmark rose, or fell, with what the benchmark itself did in those months.

Two numbers come out of it. The **up-capture ratio** says how much of the benchmark's gains in rising months the fund kept. The **down-capture ratio** says how much of the benchmark's losses in falling months it took. A fund with 80 up-capture and 65 down-capture rose about four-fifths as much as its benchmark in good months and fell about two-thirds as much in bad ones.

It's a way of describing *behaviour*, not a score. The [drawdown post]({% post_url 2026-09-29-drawdown %}) showed how long a fall can hurt; capture ratios put a number on how much of a fall a fund passed on. They also sit close to [beta]({% post_url 2026-10-02-beta %}), which measures the same sensitivity as one slope across all months. This post is part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).

## The formula

```
Up-capture   = average fund return in benchmark-up months
               ÷ average benchmark return in those months   × 100

Down-capture = average fund return in benchmark-down months
               ÷ average benchmark return in those months   × 100

Capture ratio = Up-capture ÷ Down-capture
```

"Months" is the usual choice, built from month-end NAVs (**NAV — net asset value**, a fund's price per unit). Some providers compound the returns instead of averaging them. Both are in use, and they give different answers on the same data. We use the simple average and show the compounded version once, further down.

## Worked example: a hybrid fund and an index fund, ten years

We need a benchmark and a window. The benchmark is the **Nifty 50 TRI — total return index**, which counts dividends as reinvested. We take it from NSE (the National Stock Exchange) through its index company, [NSE Indices]({{ src.tri.url }}). The window is {{ c.window_10y.base_month | append: "-01" | date: "%B %Y" }} month-end to {{ c.window_10y.last_month | append: "-01" | date: "%B %Y" }} month-end: {{ h.months }} monthly returns. Of those, {{ h.up_months }} were months when the TRI rose and {{ h.down_months }} were months when it fell.

The two funds are {{ src.funds.index_fund.name }} and {{ src.funds.hybrid.name }}, both {{ src.funds.index_fund.plan }} plans, with NAVs from the Association of Mutual Funds in India (AMFI), via [mfapi.in](https://api.mfapi.in/mf/{{ src.funds.index_fund.code }}). Data is as of 31 March 2026 (the index file ends on 30 March), more than three months before this post, and is shown for illustration only. Neither fund is being assessed.

The steps for each fund:

1. Take the last common trading day's NAV and TRI in each month.
2. Turn them into monthly returns.
3. Split the months into those where the TRI rose and those where it fell.
4. Average the fund's and the TRI's return in each group, and divide.

| | Index fund | Hybrid fund |
|---|---:|---:|
| TRI's average return in up months | {{ ix.bm_avg_up_month_pct }}% | {{ h.bm_avg_up_month_pct }}% |
| Fund's average return in those months | {{ ix.fund_avg_up_month_pct }}% | {{ h.fund_avg_up_month_pct }}% |
| **Up-capture** | **{{ ix.up_capture_avg }}** | **{{ h.up_capture_avg }}** |
| TRI's average return in down months | {{ ix.bm_avg_down_month_pct }}% | {{ h.bm_avg_down_month_pct }}% |
| Fund's average return in those months | {{ ix.fund_avg_down_month_pct }}% | {{ h.fund_avg_down_month_pct }}% |
| **Down-capture** | **{{ ix.down_capture_avg }}** | **{{ h.down_capture_avg }}** |
| Capture ratio | {{ ix.capture_ratio_avg }} | {{ h.capture_ratio_avg }} |

The index fund is close to 100 in both directions. It can't do much else: it holds the same stocks and pays its costs every month, so it keeps a little less than all of the gains and takes a little more than all of the losses.

The hybrid fund keeps {{ h.up_capture_avg }}% of the gains and takes {{ h.down_capture_avg }}% of the losses. A fund holding part of its money outside Nifty 50 stocks will show numbers below 100 in both directions almost by construction. This table can't separate that from anything the manager did. It also isn't a verdict: the [hybrid funds post]({% post_url 2026-10-18-hybrid-funds %}) covers what the category holds.

Note the yardstick, too. The Nifty 50 TRI is not this hybrid fund's own benchmark. We use it for both funds to hold the ruler constant, so the numbers describe behaviour relative to large-company equity, not performance against the fund's mandate.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your friend runs up and down a hill. You follow on a scooter.

Going up, you only get partway as high as your friend does in the same time. Going down, you also don't drop as far. "Up-capture" is how much of the climb you copied. "Down-capture" is how much of the drop you copied.

Copying less of the drop sounds great. But if you also copied less of the climb, you were just on a gentler slope. Capture ratios help you see which one happened.

</details>

## The same fund, different answers

The answer depends on three choices. Here is the hybrid fund, and the index fund, with one choice changed at a time.

| Fund | Benchmark | Window | Up-capture | Down-capture |
|---|---|---|---:|---:|
| Hybrid | Nifty 50 TRI | 10 years | {{ h.up_capture_avg }} | {{ h.down_capture_avg }} |
| Hybrid | Nifty 50 TRI | last 5 years | {{ h5.up_capture_avg }} | {{ h5.down_capture_avg }} |
| Hybrid | Nifty 50 **price** index | 10 years | {{ hp.up_capture_avg }} | {{ hp.down_capture_avg }} |
| Index fund | Nifty 50 TRI | 10 years | {{ ix.up_capture_avg }} | {{ ix.down_capture_avg }} |
| Index fund | Nifty 50 **price** index | 10 years | {{ ixp.up_capture_avg }} | {{ ixp.down_capture_avg }} |

Three things to read off it.

**The window matters.** The hybrid fund's up-capture is {{ h.up_capture_avg }} over ten years and {{ h5.up_capture_avg }} over the last five. Its down-capture hardly moves ({{ h.down_capture_avg }} against {{ h5.down_capture_avg }}). The ratio is {{ h.capture_ratio_avg }} in one window and {{ h5.capture_ratio_avg }} in the other.

**The benchmark must include dividends if the fund does.** A fund's NAV includes the dividends its stocks pay. The price index leaves them out. Against the price index, the index fund shows {{ ixp.up_capture_avg }} up and {{ ixp.down_capture_avg }} down, which reads like a fund that beat its index in both directions. It didn't: the fund holds the same stocks, and the dividends are the whole difference. The [benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %}) calls this comparing like with like.

**The formula matters.** For the hybrid fund over ten years, compounding the up and down months instead of averaging them gives {{ h.up_capture_comp }} up and {{ h.down_capture_comp }} down, against {{ h.up_capture_avg }} and {{ h.down_capture_avg }}. Same data, two standard definitions.

## Doing it in Python

```python
import pandas as pd

nav = pd.read_csv("uti-aggressive-hybrid-fund-nav.csv", parse_dates=["date"]).set_index("date").nav_direct_growth.dropna()
tri = pd.read_csv("nifty50-tri.csv", parse_dates=["date"]).set_index("date").nifty50_tri_close

both = pd.concat([nav, tri], axis=1, join="inner").dropna()      # same trading days only
both.columns = ["fund", "bench"]
month_end = both.groupby(both.index.to_period("M")).last()
ret = month_end.pct_change().loc["2016-04":"2026-03"]            # 120 monthly returns

up, down = ret[ret.bench > 0], ret[ret.bench < 0]
up_capture = up.fund.mean() / up.bench.mean() * 100
down_capture = down.fund.mean() / down.bench.mean() * 100
print(f"up {up_capture:.1f}  down {down_capture:.1f}  ratio {up_capture/down_capture:.2f}")
```

The two CSV files are in this site's repository. Swap the file and the dates to test another fund, and swap the TRI for the benchmark that fund actually uses.

## Common mistakes

- **Using the wrong benchmark.** A price index for a fund that includes dividends nudges both ratios in the fund's favour with no skill involved. An index the fund doesn't track describes the gap between two mandates, not how the fund did its job.
- **Reading low down-capture as protection.** If up-capture is lower by the same proportion, the fund just had less exposure. Look at the two together, as the ratio does, and ask what the fund holds.
- **Quoting a ratio without the window, benchmark and formula.** Change any of the three and the number moves, as the table shows.
- **Letting a few big months decide.** An average gives a crash month far more pull than a quiet one, so a window with one or two violent months can swing both ratios. Check how many months are really doing the work.

**Takeaway:** A capture ratio says how much of its benchmark's rises and falls a fund passed on, and the answer depends on the benchmark, the window and the formula. A number quoted without all three is not a fact about the fund, and it was never a score.
