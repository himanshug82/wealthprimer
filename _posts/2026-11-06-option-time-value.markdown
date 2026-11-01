---
layout: post
title: "Time value: why an option loses value near expiry"
description: "An option's price is intrinsic value plus time value, and time value drains faster near expiry. Decay worked on a hypothetical index, model stated."
image: /assets/og/option-time-value.png
date: 2026-11-06 09:00:00 +0530
series: risk
term: "Time value"
---

{% assign r = site.data.risk3 %}
{% assign c = r.contract %}
{% assign tv = r.time_value %}

## What time value is

An option's price has two parts. **Intrinsic value** is what the option would
pay if it expired right now: for a call, the index minus the strike, if that
is positive, otherwise zero (for a put, the strike minus the index, if positive). **Time value** is everything else in the price:
what buyers pay for the chance that the index moves in their favour before
expiry. So:

```
Option price  =  Intrinsic value  +  Time value
```

A note on the word "intrinsic". In the
[margin of safety post]({% post_url 2026-10-01-margin-of-safety-and-sensitivity %})
"intrinsic value" meant a business's estimated worth from its cash flows. Here
it has a much narrower, purely arithmetical sense: the payoff if exercised
today. The two have nothing to do with each other.

As expiry nears there is less time left for a favourable move, so the time
value falls to zero by expiry. What it leaves behind is the intrinsic value
alone. This post is part of the module on options in
[Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}).

## The model, stated

The prices below are not market quotes. They come from a standard teaching
model, **Black–Scholes–Merton** pricing for a European option (one that can be
exercised only at expiry), with these assumptions: **zero interest rate, zero
dividends, and a constant annual volatility of {{ tv.vol_pct }}%**
([volatility]({% post_url 2026-09-30-volatility-and-sharpe %}) here means the
standard deviation of annual returns). The index is held flat at
{{ c.level }} while the days pass, to isolate the effect of time alone. Real
option prices also move with the index and with the market's changing view of
volatility; that is the subject of the [next post]({{ '/2026/11/07/implied-volatility/' | relative_url }}).

## Worked example: three calls, same index, shrinking time

Three call options on the hypothetical Sample Index, all priced with the model
above and the index unchanged at {{ c.level }}. Prices are in index points
per unit, shown to one decimal ({{ r.time_value.days }} days out, the at-the-money call is {{ tv.rows[0].atm_price }};
the module's other posts round that to whole points).

| Days to expiry | At-the-money call (strike 20000): price | ...of which time value | In-the-money call (strike 19500): price | ...of which time value | Out-of-the-money call (strike 20500): price (all time value) |
|---:|---:|---:|---:|---:|---:|
{% for row in tv.rows -%}
| {{ row.days }} | {{ row.atm_price }} | {{ row.atm_tv }} | {{ row.itm_price }} | {{ row.itm_tv }} | {{ row.otm_price }} |
{% endfor %}

The in-the-money call has {{ c.level | minus: 19500 }} points of intrinsic value (20000 − 19500) in every row, so its time value is the price minus that. Reading the table:

1. **Time value falls to zero at expiry.** On day 0 the at-the-money and
   out-of-the-money calls are worth nothing, and the in-the-money call is
   worth its intrinsic value of {{ c.level | minus: 19500 }} points.
2. **It falls faster as expiry nears.** The at-the-money call loses about
   {{ tv.note.first_leg_per_day }} points a day between 30 and 20 days out. It loses
   {{ tv.note.last_day }} points in the last day, from day 1 to expiry.
3. **It is not a straight line.** Thirty days out, the at-the-money call's time value is
   {{ tv.note.tv_30_over_tv_5_ratio }} times its time value five days out, although
   the time left is six times as long. In this model the time value of an at-the-money option is proportional to the square root of the time left, not to the time
   left, which is why the last days are steep.

The seller of the option sits on the other side of the same arithmetic: whatever time value
the buyer loses, the seller (see [the writing post]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }}))
keeps only if the index does not move, and the seller pays out whatever payoff the buyer's
option finishes with, which the writing post shows has no upper limit on a short call.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine an ice lolly on a hot day. When it comes out of the freezer it is
all lolly. Every minute it sits in the sun, a little more of it melts, and the
last bit goes fastest. An option is like that: the "maybe something big will
happen before the deadline" part of its price is the lolly, and it melts away
as the deadline gets closer, slowly at first and then very fast. When the
deadline arrives only what is really left, the intrinsic value, remains.

</details>

## Common mistakes

- **Expecting an option to rise just because the index sits still.** In the
  table the index never moves, and every option's price falls or stays at its
  intrinsic floor. A flat index costs the buyer time value.
- **Assuming decay is even.** A figure like "so many points a day" is an
  average; the daily loss is small a month out and large in the final days.
- **Treating the model's numbers as market prices.** Real quotes differ from
  any model, and the volatility input is itself a judgement; the next post
  turns the model around to read that judgement from a price.

**Takeaway:** An option's price is intrinsic value plus time value, and time value drains to zero by expiry, slowly at first and then quickly. If the index stands still, a buyer's option loses value every day that passes; whoever is on the other side of that contract carries the payoff risk the writing post describes.
