---
layout: post
title: "Compounding: why time does most of the work"
description: "Compounding means returns earn returns. The formula, the rule of 72 checked against the exact answer, and why the last decade adds more than the first two."
image: /assets/og/compounding-and-time.png
date: 2027-01-20 09:00:00 +0530
series: money-before-markets
term: "Compounding (and rule of 72)"
---

{% assign c = site.data.mbm2.compounding %}
{% assign ds = site.data.mbm2.dataset %}
{% assign sip = c.sip %}
{% assign d1 = c.decades[0] %}
{% assign d2 = c.decades[1] %}
{% assign d3 = c.decades[2] %}
{% assign g10 = c.grid[3] %}
{% assign g10_30 = g10.values[3] %}

## What compounding means

**Compounding** is what happens when a return is left invested and starts
earning a return of its own. In year one, you earn on what you put in. In year
two, you earn on that plus year one's gain. The gains pile up on gains, so the
amount added each year keeps growing even if the rate stays the same.

The rate matters, but so does how long it runs, and that second part is the
one people underrate. This post works through the arithmetic, checks a
popular shortcut against the exact answer, and then looks at what a real
index did, because real returns don't arrive at a steady rate. It starts the
portfolio posts in [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

## The formula

```
Value after n years  =  amount × (1 + r) ^ n          r = yearly rate, as a decimal

Years to double (exact)        =  ln 2 / ln(1 + r)
Years to double (rule of 72)   ≈  72 / (rate in %)
```

The same formula, run backwards, is the [CAGR]({% post_url 2026-09-26-point-to-point-returns %})
(compound annual growth rate): the steady yearly rate that would turn a
starting value into an ending one.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You roll a small snowball down a long, snowy hill. At first it picks up a
little snow each turn, because it's small. But the bigger it gets, the more
snow sticks to it on every turn. Near the bottom it grows more in one turn
than it did in the whole first stretch.

The snow is your return. The size of the ball is what you already have. And
the length of the hill is time: a longer hill makes a much bigger ball, even
if the snow is exactly the same.

</details>

## Worked example: ₹1 lakh at a steady rate

These rates are assumptions chosen to show the arithmetic, not forecasts of
any investment. Each cell is ₹1,00,000 left alone at that rate, compounded
once a year.

| Rate a year | After {{ c.horizons[0] }} years | After {{ c.horizons[1] }} years | After {{ c.horizons[2] }} years | After {{ c.horizons[3] }} years |
|---:|---:|---:|---:|---:|
{% for row in c.grid -%}
| {{ row.rate_pct | replace: "-", "−" }}% | {{ row.values[0] }} | {{ row.values[1] }} | {{ row.values[2] }} | {{ row.values[3] }} |
{% endfor %}

Read across a row and the gaps between columns widen, even allowing for the
later columns being ten years apart rather than five. Read down the last
column and the effect of the rate widens too: the rupee gap between
neighbouring rates is far larger after {{ c.horizons[3] }} years than after
{{ c.horizons[0] }}.

### Where the gain arrives

Take the {{ c.decade_rate_pct | replace: "-", "−" }}% row over {{ c.horizons[3] }} years and split the gain into decades:

| Years | Starts at (₹) | Ends at (₹) | Gain in these 10 years (₹) | Share of the total gain |
|---|---:|---:|---:|---:|
{% for d in c.decades -%}
| {{ d.years }} | {{ d.start }} | {{ d.end }} | {{ d.gain }} | {{ d.share_pct | replace: "-", "−" }}% |
{% endfor %}

The rate never changes, yet the last ten years add {{ d3.share_pct | replace: "-", "−" }}% of
the total gain and the first ten add {{ d1.share_pct | replace: "-", "−" }}%. That's the whole
point of compounding in one table: the late years are the big ones, and they
only happen if the money is still invested.

### The same total, spent over different spans

Two made-up savers each run a SIP (systematic investment plan: a fixed sum
invested every month) and put in the same total, at an assumed
{{ sip.rate_pct }}% a year, each instalment at the start of the month. Both
stop on the same day: A starts now, B starts {{ sip.b.years }} years later.

| Saver | Monthly amount (₹) | For | Total put in (₹) | Value on the shared end date (₹) |
|---|---:|---:|---:|---:|
| A | {{ sip.a.monthly }} | {{ sip.a.years }} years | {{ sip.a.paid }} | {{ sip.a.fv }} |
| B | {{ sip.b.monthly }} | {{ sip.b.years }} years | {{ sip.b.paid }} | {{ sip.b.fv }} |

Same money in, same finishing date. Saver A ends with about
{{ sip.a_over_b }} times as much, because A's early instalments had up to
twice as long to compound. The
[step-up SIP post]({% post_url 2026-10-25-step-up-sips %}) works the
related question of raising the amount each year.

### Checking the rule of 72

| Rate | Rule of 72 says | Exact answer | Rule's error (years; + means the rule overstates) |
|---:|---:|---:|---:|
{% for r in c.rule72 -%}
| {{ r.rate_pct | replace: "-", "−" }}% | {{ r.rule72 }} years | {{ r.exact }} years | {{ r.gap }} |
{% endfor %}

Between about 6% and 12% the shortcut is within about a tenth of a year. At very
low or very high rates it drifts further, as the first and last rows show.

### What a real index did

Real returns don't come at a steady rate. The Nifty 50 Total Returns Index
(TRI, the index with dividends reinvested, from
[NSE Indices]({{ ds.tri_source_url }}), the index arm of the National Stock Exchange) turned ₹1,00,000 on {{ ds.start }}
into ₹{% include inr.html n=c.real.lakh_became %} by {{ ds.end }}: a
CAGR of {{ c.real.cagr_pct | replace: "-", "−" }}% over {{ c.real.years }} years. But
{{ c.real.negative_fys }} of the {{ ds.fy_count }} financial years in between
were negative. The worst, {{ c.real.worst_fy }}, was {{ c.real.worst_fy_pct | replace: "-", "−" }}%;
the best, {{ c.real.best_fy }}, was +{{ c.real.best_fy_pct | replace: "-", "−" }}%. The index
carries no fund costs or tax, so a real investor would have ended with less.
Past data to March 2026, for illustration only.

A CAGR describes the start and the end, not the ride between them.
A steady rate equal to the CAGR reaches the same end value as the real,
bumpy path. A real investor gets that end value only by sitting through the
bad years, which is
the subject of the [drawdown post]({% post_url 2026-09-29-drawdown %}).

## Common mistakes

1. **Treating an assumed rate as a promise.** Every table here is arithmetic
   on an assumed rate. Change the rate by two points and the
   {{ c.horizons[3] }}-year column moves a lot, as the grid shows. A plan
   built on one number needs a range beside it.
2. **Forgetting inflation.** ₹{% include inr.html n=g10_30 %} in
   {{ c.horizons[3] }} years is not ₹{% include inr.html n=g10_30 %}
   of today's money. The [real returns post]({% post_url 2026-10-20-inflation-and-real-returns %})
   shows how to take inflation out; compounding works on prices too.
3. **Interrupting it.** The big gains are at the end. Withdrawing early, or
   stopping and restarting, cuts off the years that add the most. The
   decade table makes that concrete.
4. **Averaging yearly returns.** The average of +50% and −50% is 0%, but the
   money falls 25%. Compounding uses the geometric rate, not the simple
   average; the [arithmetic of losses post]({% post_url 2026-10-09-the-arithmetic-of-losses %})
   works this through.

**Takeaway:** Compounding rewards time: at a steady rate, the last decade of
thirty adds more than the first two together. The rate is an assumption and
real years are bumpy, so the lever you control is how long the money stays
invested.
