---
layout: post
title: "Time value: why an option loses value near expiry"
description: "An option's price is intrinsic value plus time value, and the time part drains faster as expiry nears. Decay worked out on a hypothetical index, with the model stated."
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
is positive, otherwise zero. **Time value** is everything else in the price:
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
per unit.

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
   the time left is six times as long. In this model time value for a
   given strike is proportional to the square root of time left, not to time
   left, which is why the last days are steep.

The same arithmetic runs against the seller of the option: whatever time value
the buyer loses, the seller (see [the writing post]({{ '/2026/11/08/option-writing-and-margin/' | relative_url }}))
keeps, if the index does not move to change the picture.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a ticket to a cricket match that has a *chance* of being very
valuable, say if a famous player is playing. The longer before the match,
the more things could happen, so the ticket is worth more. As match day
gets closer, the surprises run out. On match day, the ticket is only worth
what that day's game is actually worth. The "maybe something exciting will
happen" part of the price melts away, slowly at first and then very fast.

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

**Takeaway:** An option's price is intrinsic value plus time value, and time value drains to zero by expiry, slowly at first and then quickly. If the index stands still, a buyer's option loses value every day that passes, while the same time value is what an option seller collects.
