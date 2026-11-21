---
layout: post
title: "Asset allocation: the mix decides most of the ride"
description: "Asset allocation is how a portfolio splits money across asset classes. Seven equity, bond and gold mixes over 18 years: return, volatility and worst fall."
image: /assets/og/asset-allocation.png
date: 2027-01-23 09:00:00 +0530
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
[asset classes]({% post_url 2027-01-21-asset-classes %}): so much in
equity, so much in bonds, perhaps some gold or cash. A 60/40 portfolio, for
example, keeps 60% in equity and 40% in bonds.

It's usually the first portfolio decision, ahead of which fund to buy,
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
Bonds are the UTI Gilt Fund, regular plan, and gold is the UTI Gold ETF
(exchange-traded fund), both NAVs (net asset values) from AMFI, the
Association of Mutual Funds in India (sources and the gold ETF's split
adjustment are in the [asset classes post]({% post_url 2027-01-21-asset-classes %})).

Each mix starts at its target weights and is reset to them on the first
trading day of every financial year, as described in the
[rebalancing post]({% post_url 2027-01-11-rebalancing-arithmetic %}). No
tax, no trading costs. Past data, for illustration only; none of these
mixes is a recommendation.

| Equity / bonds / gold | CAGR | ₹10 lakh became (₹) | Volatility, a year | Worst drawdown | Worst year | Negative years, of {{ ds.fy_count }} |
|---|---:|---:|---:|---:|---:|---:|
{% for k in m.allocation.order -%}
{% assign r = al[k] -%}
| {{ r.equity }} / {{ r.gilt }} / {{ r.gold }} | {{ r.cagr_pct }}% | {{ r.ten_lakh_became }} | {{ r.vol_pct }}% | {{ r.max_dd_pct }}% | {{ r.worst_fy_pct }}% ({{ r.worst_fy }}) | {{ r.negative_fys }} |
{% endfor %}

CAGR is the compound annual growth rate, from the
[point-to-point returns post]({% post_url 2026-09-26-point-to-point-returns %}).

### What the table shows

1. **The ride changed far more than the return.** All-equity had a
   volatility of {{ a100.vol_pct }}% and a worst drawdown of
   {{ a100.max_dd_pct }}%: ₹10 lakh fell by about
   ₹{% include inr.html n=a100.dd_on_ten_lakh %} at the bottom, in
   {{ a100.dd_trough }}. The 60/40 mix had {{ a60.vol_pct }}% and
   {{ a60.max_dd_pct }}%, a fall of about
   ₹{% include inr.html n=a60.dd_on_ten_lakh %}. Its CAGR was
   {{ a60.cagr_pct }}%, against {{ a100.cagr_pct }}% for all-equity.
2. **That near-tie is a feature of this period, not a law.** Government
   bonds had a strong run here ({{ a0.cagr_pct }}% a year), and resetting the
   mix each year bought equity after its falls. Over a period when bonds did
   worse, or equity rose without big falls, the gap between the two CAGRs
   would likely be wider. More equity meant a bumpier ride in every row;
   whether it also meant more return depended on the period.
3. **Below about 40% equity, more bonds stopped shrinking the worst fall.** The
   20/80 mix's worst drawdown ({{ al.m20_80.max_dd_pct }}%) was no better
   than 40/60's ({{ a40.max_dd_pct }}%), though volatility kept falling,
   because the bonds had a fall of their own (early 2009, in the
   [asset classes post]({% post_url 2027-01-21-asset-classes %})).
4. **A slice of gold helped here, for this period's reasons.** Swapping
   10 points of bonds for gold (60/30/10) raised the CAGR to
   {{ ag.cagr_pct }}% with the same volatility as 60/40. Gold had an
   unusually strong end to the period, so this row says more about the
   period than about gold; the limits post later in this series looks at
   how much it depends on the dates.

## Common mistakes

1. **Choosing the mix by the best CAGR in a backtest.** Any table like this
   one ranks mixes by what happened in one stretch. Rerun it over a
   different stretch and the ranking can flip. In our view, the falls a mix
   produced are a sturdier guide than the return it showed.
2. **Counting the drawdown in percent and not in rupees.** A
   {{ a60.max_dd_pct }}% fall sounds manageable. On ₹10 lakh it's
   ₹{% include inr.html n=a60.dd_on_ten_lakh %} gone for a while, and the
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
