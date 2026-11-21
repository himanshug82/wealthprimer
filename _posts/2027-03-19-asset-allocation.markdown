---
layout: post
title: "Asset allocation: how the mix changes the ride"
description: "Asset allocation is how a portfolio splits money across asset classes. Seven equity, bond and gold mixes over 18 years: return, volatility and worst fall."
image: /assets/og/asset-allocation.png
date: 2027-03-19 09:00:00 +0530
series: money-before-markets
term: "Asset allocation"
---

{% assign m = site.data.mbm2 %}
{% assign ds = m.dataset %}
{% assign al = m.allocation.rows %}
{% assign a100 = al.m100_0 %}
{% assign a60 = al.m60_40 %}
{% assign a40 = al.m40_60 %}
{% assign a0 = al.m0_100 %}
{% assign ag = al.m60_30_10 %}
{% assign a80 = al.m80_20 %}

## What asset allocation means

**Asset allocation** is how a portfolio's money is split across
[asset classes]({% post_url 2027-03-15-asset-classes %}): so much in
equity, so much in bonds, perhaps some gold or cash. A 60/40 portfolio, for
example, keeps 60% in equity and 40% in bonds.

In our view it's the first portfolio decision, ahead of which fund to buy,
because the asset classes behave so differently. Two portfolios of similar
funds can have very different rides if one is 90% equity and the other 30%.
This post shows how much, on Indian data. It belongs to
[Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

## The formula

```
Portfolio return in a period  =  Σ (weight of each asset × that asset's return)

Weights drift as assets move. Rebalancing resets them to target.
```

The return is a weighted average, but the bumpiness isn't. How much the mix
calms the ride depends on how the assets move together, their correlation,
which the [diversification post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %})
works through. Volatility and maximum drawdown are defined in the
[volatility]({% post_url 2026-09-30-volatility-and-sharpe %}) and
[drawdown]({% post_url 2026-09-29-drawdown %}) posts.

## Worked example: seven mixes, {{ ds.start }} to {{ ds.end }}

Equity is the Nifty 50 TRI (Total Returns Index, dividends reinvested, from
[NSE Indices]({{ ds.tri_source_url }}), part of the National Stock Exchange).
Bonds are the UTI Gilt Fund (from UTI Mutual Fund), regular plan, and gold is the UTI Gold ETF
(exchange-traded fund), both NAVs (net asset values) from AMFI, the
Association of Mutual Funds in India (sources and the gold ETF's split
adjustment are in the [asset classes post]({% post_url 2027-03-15-asset-classes %})).

Each mix starts at its target weights and is reset to them on the first
trading day of every financial year, as described in the
[rebalancing post]({% post_url 2027-02-19-rebalancing-arithmetic %}). No
tax, no trading costs. The gilt fund's and gold ETF's own costs are in their
NAVs, and the gilt fund is a regular plan, the costlier plan type; the index
has no costs, so the comparisons lean towards equity. Past data, for
illustration only; none of these
mixes is a recommendation.

CAGR is the compound annual growth rate, from the
[point-to-point returns post]({% post_url 2026-09-26-point-to-point-returns %}).

| Equity / bonds / gold | CAGR | ₹10 lakh became (₹) | Volatility, a year | Worst drawdown | Worst year | Negative years, of {{ ds.fy_count }} |
|---|---:|---:|---:|---:|---:|---:|
{% for k in m.allocation.order -%}
{% assign r = al[k] -%}
| {{ r.equity }} / {{ r.gilt }} / {{ r.gold }} | {{ r.cagr_pct | replace: "-", "−" }}% | {{ r.ten_lakh_became }} | {{ r.vol_pct | replace: "-", "−" }}% | {{ r.max_dd_pct | replace: "-", "−" }}% | {{ r.worst_fy_pct | replace: "-", "−" }}% ({{ r.worst_fy }}) | {{ r.negative_fys }} |
{% endfor %}

### What the table shows

1. **The ride changed far more than the return.** All-equity had a
   volatility of {{ a100.vol_pct | replace: "-", "−" }}% and a worst drawdown of
   {{ a100.max_dd_pct | replace: "-", "−" }}%: the ₹10 lakh put in on {{ ds.start }} was worth
   ₹{% include inr.html n=a100.peak_value %} on {{ a100.dd_peak }} and
   ₹{% include inr.html n=a100.trough_value %} on {{ a100.dd_trough }}. The 60/40 mix
   had {{ a60.vol_pct }}% and {{ a60.max_dd_pct }}%: from
   ₹{% include inr.html n=a60.peak_value %} to
   ₹{% include inr.html n=a60.trough_value %} over the same months. Its CAGR
   was {{ a60.cagr_pct }}%, the same as all-equity's {{ a100.cagr_pct }}% to
   one decimal.
2. **That tie is a feature of this period, not a law.** Government bonds
   had a strong run here ({{ a0.cagr_pct }}% a year, even net of a regular
   plan's costs). The [rebalancing post]({% post_url 2027-02-19-rebalancing-arithmetic %})
   found that whether yearly resets helped or hurt changed with the start
   year, so this one window can't say why the two ended level. More equity
   meant higher volatility in every row; whether it also meant more return
   depended on the period.
3. **Below about 40% equity, more bonds stopped shrinking the worst fall.** The
   20/80 mix's worst drawdown ({{ al.m20_80.max_dd_pct | replace: "-", "−" }}%) was no better
   than 40/60's ({{ a40.max_dd_pct | replace: "-", "−" }}%), though volatility kept falling,
   because the bonds had a fall of their own (early 2009, in the
   [asset classes post]({% post_url 2027-03-15-asset-classes %})).
4. **A slice of gold helped here, for this period's reasons.** Swapping
   10 points of bonds for gold (60/30/10) raised the CAGR to
   {{ ag.cagr_pct }}% with the same volatility as 60/40, though its worst
   drawdown was slightly deeper ({{ ag.max_dd_pct }}% against
   {{ a60.max_dd_pct }}%). Gold had an
   unusually strong end to the period, so this row says more about the
   period than about gold; the limits post later in this series looks at
   how much it depends on the dates.

## Common mistakes

1. **Choosing the mix by the best CAGR in a backtest.** Any table like this
   one ranks mixes by what happened in one stretch. Rerun it over a
   different stretch and the ranking can flip. In our view, the falls a mix
   produced are a sturdier guide than the return it showed.
2. **Counting the drawdown in percent and not in rupees.** A
   {{ a60.max_dd_pct }}% fall sounds manageable. In the table it meant
   ₹{% include inr.html n=a60.peak_to_trough %} of a ₹10 lakh start's value
   gone for a while, and the
   [behavioural biases post]({% post_url 2026-10-14-behavioural-biases-indian-edition %})
   explains why that's when selling feels most urgent.
3. **Setting a mix and never looking again.** Without resets, a 60/40
   portfolio drifts towards whatever rose most, usually equity, so its risk
   grows quietly. The table assumes a yearly reset; skipping it changes the
   numbers.
4. **Confusing allocation with diversification across funds.** Ten equity
   funds are a 100/0 allocation. The rows above differ because the asset
   classes differ, not because there are more holdings.

**Takeaway:** Asset allocation sets how rough the ride will be: in this
data, moving from all-equity to 60/40 cut the worst fall by close to half.
Whether it also cost return depends on the period, which is why, in our
view, the falls a mix produces say more than the backtest's best row.
