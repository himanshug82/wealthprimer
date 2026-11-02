---
layout: post
title: "Hedging with a put: what the insurance costs"
seo_title: "Protective put: how hedging with a put option works"
description: "A protective put caps your loss in exchange for a premium. The payoff table on a hypothetical index, and why renewing the cover every month adds up."
image: /assets/og/protective-put-hedging.png
date: 2027-02-02 09:00:00 +0530
series: risk
term: "Protective put (hedging)"
---

{% assign r4 = site.data.risk4 %}
{% assign p = r4.put %}

## What is a protective put?

A **hedge** is a position taken to reduce the damage from another one. A **protective put** is the simplest: you hold something that can fall, and you also buy a [put option]({% post_url 2026-11-06-call-and-put-options %}) on it. If the price falls below the put's strike, the put gains and offsets some of the loss. If the price rises, the put expires worthless, and you are out its premium.

That is insurance, and it behaves like insurance: you pay a premium for protection you hope not to use, the protection has a deductible, and the cover runs out on a date. This post works the arithmetic on a hypothetical index. It describes how the instrument works and what it costs; it isn't a suggestion to hedge or to buy any option. It builds on the [payoff and breakeven post]({% post_url 2026-11-10-option-payoff-and-breakeven %}) and the [time value post]({% post_url 2026-11-14-option-time-value %}), and belongs to the [Risk, Leverage and Your Own Brain]({{ '/series/risk/' | relative_url }}) series.

## The formula

At expiry, for one lot of the underlying (the index or a position that moves like it):

```
Profit/loss of the holding  =  (Index at expiry − starting level) × lot size
Put payoff                  =  max(strike − index at expiry, 0) × lot size
Premium paid                =  premium per unit × lot size

Hedged profit/loss          =  holding P/L  +  put payoff  −  premium paid
Worst case                  =  (strike − starting level) × lot size − premium paid
                               (reached at any index level at or below the strike)
Breakeven                   =  starting level + premium per unit
```

## Worked example: a hypothetical index

Everything here is hypothetical. The "Sample Index" stands at {% assign lv = p.level %}{% include inr.html n=lv %}, one lot is {{ p.lot }} units, so the holding is worth ₹{% assign v = p.value %}{% include inr.html n=v %}. The option premiums come from a teaching model (Black-Scholes, {{ p.vol_pct }}% volatility, {{ p.days }} days to expiry, zero interest rate and dividends), the same one used in the [options posts]({% post_url 2026-11-30-implied-volatility %}). No real quote is used.

Two puts, a month to expiry:

| | At-the-money put | Out-of-the-money put |
|---|---:|---:|
| Strike | {% assign x = p.atm.strike %}{% include inr.html n=x %} | {% assign x = p.otm.strike %}{% include inr.html n=x %} |
| Premium per unit | ₹{{ p.atm.prem }} | ₹{{ p.otm.prem }} |
| Premium for the lot | ₹{% assign x = p.atm.cost %}{% include inr.html n=x %} | ₹{% assign x = p.otm.cost %}{% include inr.html n=x %} |
| Premium as a share of the holding | {{ p.atm.cost_pct }}% | {{ p.otm.cost_pct }}% |
| Worst-case loss for the month | ₹{% assign x = p.atm.worst_loss %}{% include inr.html n=x %} ({{ p.atm.worst_loss_pct }}%) | ₹{% assign x = p.otm.worst_loss %}{% include inr.html n=x %} ({{ p.otm.worst_loss_pct }}%) |
| Index level where the hedged holding breaks even | {% assign x = p.breakeven_atm_level %}{% include inr.html n=x %} | {% assign x = p.breakeven_otm_level %}{% include inr.html n=x %} |

And the profit or loss at expiry, in rupees, for different index levels:

| Index at expiry | Change | Holding alone | With the at-the-money put | With the out-of-the-money put |
|---:|---:|---:|---:|---:|
{% for row in p.rows %}| {% assign lv2 = row.level %}{% include inr.html n=lv2 %} | {% assign mv = row.move_pct %}{% include inr.html n=mv %}% | {% assign a = row.unhedged %}{% include inr.html n=a %} | {% assign b = row.atm_hedged %}{% include inr.html n=b %} | {% assign c = row.otm_hedged %}{% include inr.html n=c %} |
{% endfor %}
Three things show up in the columns:

1. **The loss is capped, not removed.** However far the index falls, the at-the-money version loses ₹{% assign x = p.atm.worst_loss %}{% include inr.html n=x %} and the out-of-the-money version ₹{% assign x = p.otm.worst_loss %}{% include inr.html n=x %}. The lower-premium put buys less protection: the loss it allows is bigger.
2. **You give up a slice of every good outcome.** On the upside, the hedged lines sit below the holding-alone column by the premium. The protection is paid for in rupees whether or not it is used.
3. **A flat month costs you.** If the index ends where it started, the unhedged holding is at ₹0 and the hedged ones are down by their premiums.

## The cost of renewing the cover

Puts expire. To keep the protection on, you buy a new one each period. On the same assumptions, a month of at-the-money cover costs {{ p.atm.cost_pct }}% of the holding. Twelve of them, added up and not compounded, come to roughly {{ p.atm.rolled_12x_pct }}% of the holding in a year. The out-of-the-money version comes to roughly {{ p.otm.rolled_12x_pct }}%. These are model numbers for an assumed volatility, and real option prices move with volatility ([implied volatility]({% post_url 2026-11-30-implied-volatility %}) is the market's price for it), but the pattern is general: continuous insurance on a risky holding is a recurring expense, and it is paid for by the same holding.

That is why hedging with options is usually described as a trade-off between a smaller maximum loss and a lower expected return, not as something free. Whether the trade-off suits anyone is a personal question this post doesn't answer.

## Common mistakes

- **Reading "limited loss" as "no loss".** The loss is capped at the strike gap plus the premium. A put 3% below the market means the first 3% of a fall is yours, plus the premium.
- **Forgetting the cover expires.** A one-month put protects a one-month window. A fall that starts in the second month is unhedged unless a new put was bought.
- **Mismatching the hedge and the holding.** A put on an index only hedges a portfolio that moves with that index. A concentrated stock portfolio can fall while the index doesn't, and the put pays nothing.
- **Comparing the premium with one outcome.** The premium looks small next to a 10% fall and large next to a flat year. Both happen; the cost is paid in both.

## Doing it in Python

```python
lot, start, strike, premium = 75, 20000, 20000, 343     # hypothetical Sample Index

def hedged_pl(index_at_expiry):
    holding = (index_at_expiry - start) * lot
    put = max(strike - index_at_expiry, 0) * lot
    return holding + put - premium * lot

for s in (18000, 19000, 20000, 21000, 22000):
    print(s, (s - start) * lot, hedged_pl(s))    # holding alone vs hedged
```

**Takeaway:** A protective put caps the loss on something you own in exchange for a premium that you pay whether or not the fall comes. On a hypothetical index, renewing at-the-money cover every month cost a large share of the holding's value over a year, so protection is a trade-off, not a free option.
