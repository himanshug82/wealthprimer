---
layout: post
title: "Implied volatility, plainly: what a price implies"
description: "Implied volatility is the volatility that makes a pricing model return an option's price. How it is read back from a price, and what it is not."
image: /assets/og/implied-volatility.png
date: 2026-11-07 09:00:00 +0530
series: risk
term: "Implied volatility"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}
{% assign iv = r.implied_vol %}

## What implied volatility means

**Implied volatility (IV)** is the level of volatility that, when put into an
option pricing model along with the strike, index level and time to expiry,
gives exactly the option's current market price. It is *backed out of a
price*, not measured from past returns. Past returns give **historical
volatility** (the standard deviation of returns, as in the
[volatility and Sharpe post]({% post_url 2026-09-30-volatility-and-sharpe %}));
IV is what the option's price implies about the size of moves *the model
needs* to justify that price.

Two things IV is not. It is not a forecast the market has certified: it is a
number that depends on the model used to read it, and on option prices that
also reflect demand and supply. And it says nothing about direction. A high
IV means a price that implies large moves up *or* down, not a move in a
chosen direction. This post is part of the options module in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}).

## The formula

There is no tidy algebraic formula for IV. The pricing model runs one way
(volatility in, price out), so IV is found by trying volatilities until the
model's price matches the quoted price:

```
Model price( strike, index level, days to expiry, volatility )  =  quoted price

IV  =  the volatility that makes this equation true
```

The model here is the same teaching model as the
[time value post]({{ '/2026/11/06/option-time-value/' | relative_url }}):
Black–Scholes–Merton, zero interest rate, zero dividends. All prices are
hypothetical and the underlying is the Sample Index at {{ c.level }}.

## Worked example, in two directions

**Volatility in, price out.** An at-the-money call (strike {{ c.strike }}) with
{{ iv.days }} days to expiry, priced at different volatilities. Prices are in
index points to one decimal; the per-lot column uses the price rounded to a
whole point, as the module's other posts do (so {{ iv.vol_rows[1].atm_call }} points is
{{ c.call_prem }} points, or ₹{% assign cpr = c.call_prem_rs %}{% include inr.html n=cpr %} a lot, at {{ iv.vol_rows[1].vol_pct }}%).

| Volatility used (annual) | Call price (points) | Price per lot (₹) |
|---:|---:|---:|
{% for row in iv.vol_rows -%}
{% assign lotv = row.lot_rs -%}
| {{ row.vol_pct }}% | {{ row.atm_call }} | {% include inr.html n=lotv %} |
{% endfor %}

Two features of this table follow from the model. Price rises with
volatility, because larger possible moves make the right more valuable. And
for this at-the-money option the relationship is nearly a straight line: each
extra volatility point adds about {{ iv.one_vol_point_pts }} index points to
the price. A move from {{ iv.vol_up.from_pct }}% to {{ iv.vol_up.to_pct }}%
takes the price from {{ iv.vol_up.price_from }} to {{ iv.vol_up.price_to }},
a rise of {{ iv.vol_up.gain_pts }} points with the index unchanged.

**Price in, volatility out.** Suppose these hypothetical call prices are
quoted at five different strikes, all for the same {{ iv.days }}-day expiry.
Solving for the volatility that reproduces each price gives its IV:

| Strike | Quoted price (points) | Implied volatility |
|---:|---:|---:|
{% for row in iv.iv_rows -%}
| {{ row.strike }} | {{ row.price }} | {{ row.iv_pct }}% |
{% endfor %}

Each IV was found by trial and checked: putting it back into the model returns
the quoted price. The prices are made up for the exercise. Whether real
options at different strikes or expiries show the same IV is something to
look at in real data, and this table does not claim any pattern.

### Why time and volatility are tied together

A quick check on the model: the same at-the-money call at four times the
time to expiry (120 days instead of 30) is priced at {{ iv.sqrt.price_120d }}
points against {{ iv.sqrt.price_30d }}, a ratio of {{ iv.sqrt.ratio }}. Volatility
is annual, and the spread of outcomes grows with the square root of time, so
four times the time doubles the price here. That is one reason IV is quoted
as an annual percentage whatever the option's remaining life.

## Common mistakes

- **Reading IV as a prediction of direction.** The model's volatility enters
  call and put prices symmetrically. A high IV makes both dearer.
- **Reading IV as "the market's expected move" without the model.** IV is a
  model-dependent translation of a price. A different model, or different
  assumptions about interest and dividends, gives a different number from the
  same price.
- **Comparing IV with historical volatility and calling the gap a verdict.**
  The two measure different things over different periods, and the gap does not,
  by itself, show that either is wrong. This post draws no conclusion from any real IV
  level, and uses none.
- **Treating a rising IV as news about the index.** In the first table the
  price rises by {{ iv.vol_up.gain_pts }} points with the index frozen. An
  option can gain or lose value from a change in IV alone. The
  [India VIX post]({{ '/2026/11/09/india-vix/' | relative_url }}) covers a
  published volatility index (VIX, the volatility index) that is based on option prices.

**Takeaway:** Implied volatility is the volatility that makes a pricing model return an option's quoted price; it is read back from the price and depends on the model. A higher IV means a dearer option, whichever way the index goes, so the price can change even when the index does not.
