---
layout: post
title: "Arbitrage funds: an equity fund that behaves like a debt fund"
description: "How an arbitrage fund earns the gap between a share's cash and futures prices, what that did on real NAV data from 2018 to 2026, and why it's taxed as equity."
image: /assets/og/arbitrage-funds.png
date: 2026-10-19 09:00:00 +0530
series: mutual-funds
term: "Arbitrage fund"
---

{% assign m = site.data.mf3 %}
{% assign a = m.arbitrage %}
{% assign ar = a.arbitrage %}
{% assign ov = a.overnight %}
{% assign fh = a.full_history %}
{% assign t = a.trade %}
{% assign r = m.reg %}
{% assign src = m.sources %}

## A strange-looking fund

An **arbitrage fund** is, by the rules of SEBI (the Securities and Exchange
Board of India), a hybrid fund that keeps at least
65% of its assets in equity and equity-related instruments and "follows an
arbitrage strategy" (paragraph {{ r.hybrid_para }} of SEBI's
[Master Circular for Mutual Funds]({{ r.mc26.url }}),
{{ r.mc26.date | date: "%-d %B %Y" }}). It owns a lot of shares. And yet its
[NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %}) (net asset value, the
per-unit value of the fund) moves like a debt fund's: in the
[hybrid funds post]({% post_url 2026-10-18-hybrid-funds %}) it was the only
fund that rose in 2008, early 2020 and early 2026.

The trick is that almost every share it buys, it also *sells* in the futures
market at the same time. The two positions cancel each other's price risk. What
is left is a small, fairly predictable gap between the two prices — and
that gap is what the fund earns.

## The formula

A stock future is a contract to buy or sell the share on a fixed date (the
monthly expiry) at a price agreed today. It usually trades a little *above*
the share's cash-market price, because whoever buys the future instead of the
share gets the same exposure without paying the full price up front. That premium is
roughly the interest cost of holding the share until expiry:

```
Future price  ≈  Cash price × (1 + r × days/365)  −  expected dividends

Arbitrage trade: buy the share at the cash price S,
                 sell the future at F, hold both until expiry.

Locked-in gain  =  F − S          (whatever the share does in between)
Return          =  (F − S) / S
Annualised      ≈  (F − S) / S × 365 / days
```

On expiry day the future settles at the cash price, so the two legs converge.
If the share has risen, the stock gains and the future loses the same amount;
if it has fallen, the reverse. Either way, the fund keeps F − S, less trading
costs.

## Worked example 1: one trade

A **hypothetical** share, not a real company:

| | |
|---|---:|
| Cash-market price | ₹{% include inr.html n=t.spot %} |
| Future expiring in {{ t.days }} days | ₹{% include inr.html n=t.future %} |
| Spread locked in | ₹{% include inr.html n=t.spread %} per share |
| Return over {{ t.days }} days | {{ t.spread_pct }}% |
| Annualised (× 365 / {{ t.days }}) | about {{ t.annualised_pct }}% |

{% assign lo = t.spot | minus: 100 %}{% assign hi = t.spot | plus: 100 %}Suppose on expiry the share closes at ₹{% include inr.html n=lo %}. The fund
loses ₹100 on the share and gains ₹{{ t.future | minus: lo | round }} on the
short future, for a net gain of ₹{{ t.spread | round }}. At ₹{% include inr.html n=hi %} it gains ₹100 on
the share and loses ₹{{ hi | minus: t.future | round }} on the future, for the
same net gain of ₹{{ t.spread | round }}. The market's direction has
dropped out of the answer.

Then do it again next month, across dozens of stocks, and park the rest in
short-term debt to meet margin calls. That's the fund.

## Worked example 2: seven and a bit years of a real one

UTI Arbitrage Fund (regular plan, growth; AMFI scheme code
{{ src.arbitrage.regular_code }}; AMFI is the Association of Mutual Funds in India) against the UTI Overnight Fund that the
[debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) used, from
{{ a.window_start | date: "%-d %B %Y" }} (when the overnight scheme took on its
present mandate) to {{ src.end | date: "%-d %B %Y" }}. Source:
{{ src.label }}. Historical data, for illustration only. **This post takes no
view on either fund**; they're here because they have long histories from
one fund house. Both columns are **pre-tax** NAV returns — and the two are
taxed differently, which the last section covers.

| | Arbitrage fund | Overnight fund |
|---|---:|---:|
| Annualised return | {{ ar.cagr_pct }}% | {{ ov.cagr_pct }}% |
| Annualised volatility | {{ ar.volatility_pct }}% | {{ ov.volatility_pct }}% |
| Days the NAV fell | {{ ar.negative_days_pct }}% | {{ ov.negative_days_pct }}% |
| Worst 1-year return | {{ ar.rolling_1y_min_pct }}% | {{ ov.rolling_1y_min_pct }}% |
| Median 1-year return | {{ ar.rolling_1y_median_pct }}% | {{ ov.rolling_1y_median_pct }}% |
| Best 1-year return | {{ ar.rolling_1y_max_pct }}% | {{ ov.rolling_1y_max_pct }}% |

1. **The returns sit close together.** Across {% include inr.html n=a.rolling_1y_windows %} one-year
   windows ending on each day both funds published a NAV, the arbitrage fund
   was ahead in {{ a.rolling_1y_arb_ahead_pct }}% of them, by a median of
   {{ a.rolling_1y_median_gap_pp }} percentage points. That's the order of
   gap you'd expect from two ways of earning roughly the short-term interest
   rate.
2. **But it isn't a straight line.** The arbitrage fund's NAV fell on
   {{ ar.negative_days_pct }}% of days — about one in three. The overnight
   fund's never fell. The fund marks both legs to market every day, and
   the gap between the cash and futures price wobbles day to day as traders'
   demand shifts. A bad day was small — the worst was
   {% include inr.html n=ar.worst_day_pct %}% on {{ ar.worst_day | date: "%-d %B %Y" }} — but
   it happens often.
3. **Those daily wobbles wash out by expiry.** Over its whole AMFI history
   from {{ fh.start | date: "%B %Y" }}, only {{ fh.negative_months }} of
   {{ fh.months }} calendar months ended lower, and the worst month was
   {% include inr.html n=fh.worst_month_pct %}%. Its deepest fall from a peak was
   {% include inr.html n=fh.max_drawdown.pct %}%, in {{ fh.max_drawdown.trough_date | date: "%B %Y" }}, recovered by
   {{ fh.max_drawdown.recovered_date | date: "%-d %B" }}.
4. **The spread moves with interest rates.** Calendar-year returns:

| Year | Arbitrage fund | Overnight fund |
|---|---:|---:|{% for y in a.calendar_years %}
| {{ y.year }} | {{ y.arbitrage_pct }}% | {{ y.overnight_pct }}% |{% endfor %}

Both dipped in 2020–22 when rates were low and rose again as rates climbed —
the cost-of-carry formula at work. In {{ a.calendar_years[3].year }} the arbitrage fund
earned *less* than the overnight fund. An arbitrage fund is not a way to
beat short-term rates; it's another way of earning something close to them.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your friend will buy your cricket bat from you next month for ₹1,006, no
matter what. Today, a shop sells the same bat for ₹1,000.

So you buy the bat for ₹1,000 and shake hands with your friend on ₹1,006.
Next month the bat might be worth ₹900 or ₹1,100 in the shop — you don't
care. You've already agreed to sell it for ₹1,006. You made ₹6 for holding a
bat for a month.

That's all an arbitrage fund does, with shares instead of bats, over and over.

</details>

## Why it's taxed as equity

This is a big part of the category's appeal. For tax purposes, an
**equity-oriented fund** is one where "{{ r.tax_equity_fund.text }}"
([{{ r.tax_equity_fund.section }}]({{ r.tax_equity_fund.url }}), which
applies from 1 April 2026). An arbitrage fund *does* hold those shares, in the cash market. The
test counts the shares; it doesn't subtract the short futures that hedge them.
So a fund whose returns look like a debt fund's gets equity-fund tax treatment,
which can be lighter than the slab-rate treatment of debt-fund gains.

The rates and holding periods are in the tax series (the equity funds
post<!-- RELINK 2026-10-29-equity-and-equity-funds -->), which starts later.
This is also why the comparison table above is pre-tax only: after tax the
gap between the two can be much wider than
{{ a.rolling_1y_median_gap_pp }} percentage points, in either fund's favour
depending on your slab and holding period. Check the current rules for your
own case.

## Common mistakes

- **Treating it as risk-free because the market risk is hedged.** The
  directional risk is gone; the rest isn't. The fund still holds short-term
  debt (with its own credit and rate risk), still has daily NAV falls, and
  the spread itself can shrink to very little when few traders want leverage.
- **Using it for money you need next week.** Its NAV falls on about a third
  of days, and some arbitrage funds carry an
  [exit load]({% post_url 2026-10-07-exit-load %}) on redemptions within a
  short period. Over days, an overnight or liquid fund is the steadier tool.
- **Comparing its return with a debt fund's without adjusting for tax.**
  The pre-tax numbers were within a percentage point of each other. The
  after-tax numbers are what you actually keep, and they depend on your
  slab.
- **Reading "65% equity" as equity exposure.** Almost all of that 65% is
  hedged. The fund's net exposure to the stock market going up or down is
  close to zero.

**Takeaway:** An arbitrage fund buys shares and sells their futures at the
same time, so it earns the small gap between the two prices rather than the
market's direction. It returned about what an overnight fund did before tax,
with more daily wobble, and is taxed as equity because it owns the shares it
has hedged.
