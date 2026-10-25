---
layout: post
title: "What mutual fund metrics can't tell you"
description: "Returns, Sharpe, capture ratios, ratings and the rest all describe the past. An honest look at what each fund metric leaves out, with numbers from this series."
image: /assets/og/what-fund-metrics-cant-tell-you.png
date: 2026-11-07 09:00:00 +0530
series: mutual-funds
---

{% assign m = site.data.mf4 %}
{% assign c = m.capture %}
{% assign h10 = c.hybrid_vs_tri_10y %}
{% assign h5 = c.hybrid_vs_tri_5y %}
{% assign ixp = c.index_vs_pri_10y %}
{% assign ixt = c.index_vs_tri_10y %}
{% assign r = m.risk_ratios.index_fund_vs_tri %}
{% assign sv = m.survivorship %}
{% assign tc = m.turnover.cases.base %}
{% capture ir_ix %}{% include inr.html n=r.information_ratio %}{% endcapture %}

## The numbers describe the past

Everything in [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}) has been a way of summarising what a fund did. That's useful, and it's also the limit. A summary of a past is not a view of a future, and each metric throws away something that mattered.

This post goes through what each one throws away, using numbers from the last few posts (market data as of March 2026). It teaches no new metric, and it doesn't conclude that any of them is useless. They are useful for asking better questions. They are not good at giving answers.

## What each metric leaves out

| Metric | What it tells you | What it can't tell you | Shown in |
|---|---|---|---|
| Point-to-point return | What happened between two dates | Anything about other dates | [Point-to-point returns]({% post_url 2026-09-26-point-to-point-returns %}) |
| Rolling returns | How outcomes varied across many start dates | Whether the next window looks like them | [Rolling returns]({% post_url 2026-09-27-rolling-returns %}) |
| Drawdown | How far and how long a fall lasted | How you'd have behaved during it | [Drawdown]({% post_url 2026-09-29-drawdown %}) |
| Volatility, Sharpe | Return per unit of wobble | Fat tails, and how long losses lasted | [Volatility and Sharpe]({% post_url 2026-09-30-volatility-and-sharpe %}) |
| Sortino, information ratio | Falls only; return against a benchmark | Whether the bar or the benchmark was the right one | [Sortino and information ratio]({% post_url 2026-10-28-sortino-and-information-ratio %}) |
| Capture ratios | How much of up and down months a fund kept | Why: lower exposure or better choices | [Capture ratios]({% post_url 2026-10-26-up-and-down-capture-ratios %}) |
| Expense ratio | The disclosed running cost | Price impact, tax, and what the cost bought | [Expense ratios]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %}) |
| Portfolio turnover | How much the fund traded | Whether the trading paid for itself | [Portfolio turnover]({% post_url 2026-10-30-portfolio-turnover-ratio %}) |
| Star ratings | A rank within a peer group | The peer group's missing members, and the future | [Star ratings]({% post_url 2026-10-16-why-star-ratings-mislead %}) |
| Riskometer | A label for the portfolio's risk at one date | Risk of loss to you, over your horizon | [The riskometer]({% post_url 2026-10-22-the-riskometer %}) |

## Five ways the numbers moved when we changed the question

**The window.** The hybrid fund's up-capture was {{ h10.up_capture_avg }} over ten years and {{ h5.up_capture_avg }} over the last five. Same fund, same benchmark, two windows. Its capture ratio went from {{ h10.capture_ratio_avg }} to {{ h5.capture_ratio_avg }}.

**The benchmark.** Against the Nifty 50 total return index, the index fund's capture was {{ ixt.up_capture_avg }} up and {{ ixt.down_capture_avg }} down. Against the price index, it was {{ ixp.up_capture_avg }} and {{ ixp.down_capture_avg }}, which looks like beating the index in both directions. The fund held the same stocks. The dividends explain the difference.

**The formula.** The same index fund had a Sharpe of {{ r.sharpe }} and a Sortino of {{ r.sortino }} over the same ten years. Neither is wrong. They answer different questions, and they can't be compared with each other.

**The benchmark again.** The information ratio for that index fund against its own benchmark was {{ ir_ix }}. That's a cost, {{ r.active_return_pct | abs }} points a year, divided by a very small wander of {{ r.tracking_error_pct }} points. It says nothing about the fund's quality.

**Who's in the table.** In a simulated world where no fund had any skill, a survivors-only table showed {{ sv.survivor_ahead_share_pct }}% of funds ahead of the benchmark. The full group of {{ sv.funds }} had {{ sv.all_ahead_share_pct }}%. Both came from identical returns.

None of this is an argument against measuring. It's an argument for asking, every time: over which dates, against what, calculated how, and for which funds?

## What no metric covers

Some things don't appear in any of the numbers above.

- **The manager next year.** The [manager changes post]({% post_url 2026-10-23-manager-changes-and-style-drift %}) showed how a fund can change while keeping its name. A track record belongs to whoever earned it.
- **Costs that have no line.** The price impact of a fund's own trading is in no expense line. Our made-up busy fund lost about {{ tc.fund_b.impact_drag_pct_of_aum }}% of its assets a year to it, against about {{ tc.fund_a.impact_drag_pct_of_aum }}% for a quiet one, on an assumed impact cost.
- **Your own behaviour.** A fund's drawdown is a number. Sitting through it is a decision, and no table measures whether you would.
- **Tax and your goals.** None of these metrics knows your tax position, your horizon, or what the money is for.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A cricket scorecard tells you how many runs a batter scored yesterday. It's accurate, and it's useful.

It doesn't tell you whether they'll score tomorrow, whether the pitch was easy, or whether the bowlers were having a bad day. Two batters with the same runs can have played very different innings.

Fund numbers are scorecards. They record what happened. They don't know what comes next.

</details>

## Common mistakes

- **Stacking metrics as if more numbers meant more evidence.** Sharpe, Sortino, capture ratios and drawdown are all computed from the same return history. Five numbers from one history are not five pieces of independent evidence.
- **Looking for the one metric that picks the winner.** Each metric answers a narrow question. No combination of them predicts which fund will do well, and this series has not claimed one does.
- **Taking a precise-looking figure at face value.** A Sharpe of {{ r.sharpe }} quoted to two decimals carries every assumption behind it: the dates, the risk-free rate, the data frequency. Ask for them.
- **Treating the metrics as a substitute for reading the documents.** The factsheet, the scheme documents and the category rules tell you what the fund is allowed to do. The numbers only tell you what it did.

**Takeaway:** Fund metrics describe a past, over a window, against a benchmark, for the funds still around, and each one leaves something out. Use them to ask better questions about a fund, not to predict how it will do.
