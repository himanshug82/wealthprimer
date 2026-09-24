---
layout: post
title: "Debt funds explained: accrual, mark-to-market, and why a gilt fund can fall"
description: "How a debt fund earns — accrual plus repricing — and why an overnight fund never had a down day while a gilt fund fell 16% and took three years to recover."
image: /assets/og/debt-funds-explained.png
date: 2026-12-08 09:00:00 +0530
series: mutual-funds
term: "Debt fund (accrual vs mark-to-market)"
---

{% assign m = site.data.mf2 %}
{% assign dbt = m.debt %}
{% assign ov = dbt.funds.overnight %}
{% assign mm = dbt.funds.money_market %}
{% assign g = dbt.funds.gilt %}
{% assign gl = dbt.gilt_long_run %}
{% assign src = m.sources %}

## Two ways a debt fund makes money

The first nine posts in this series used an equity index fund for every
calculation. A **debt fund** holds bonds instead of shares — government
securities, treasury bills, bank certificates of deposit, corporate bonds —
and it earns in two quite different ways at once.

**Accrual.** A bond pays interest (the *coupon*). A fund holding ₹100 crore
of bonds yielding 7% is owed roughly ₹1.9 lakh of interest every single day,
whether or not anyone is watching. That income is added to the fund's assets
daily, which is why a debt fund's NAV tends to creep upward in a nearly
straight line.

**Mark-to-market.** The fund also has to value every bond it holds at what
the bond would fetch *today*. Bond prices move inversely to interest rates:
when market yields rise, the fixed coupon on an existing bond looks less
attractive, so its price falls. That revaluation hits the NAV the same day.

Which of the two dominates depends on one number — how far away the bonds'
cash flows are, which the [modified duration post]({% post_url 2026-11-30-modified-duration %})
covers. A fund holding paper that matures tomorrow has almost nothing to
reprice; a fund holding 15-year government bonds has a great deal.

```
Daily NAV change  ≈  Accrual (YTM ÷ 365)  −  Modified duration × Change in yield
```

YTM is the [yield to maturity]({% post_url 2026-11-29-yield-to-maturity %}) —
the annual return the fund's bonds lock in if held to maturity. The first term
is steady and positive. The second is noisy and can be large
in either direction. Every debt fund is a mix of the two, and the SEBI
category tells you roughly what mix.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you lent your friend ₹100 and they promised to pay you ₹7 a year for
ten years, then the ₹100 back. Every day, you're a little richer — about 2
paise — because interest is building up. That's accrual.

Now imagine a new friend shows up offering ₹9 a year on the same deal.
Suddenly nobody wants to buy your ₹7-a-year loan off you for ₹100; they'd only
pay maybe ₹90. You still get your ₹7 a year, but *today* your loan is worth
less. That's mark-to-market.

If your loan ended tomorrow, nobody would care about the ₹9 offer — you're
about to get your ₹100 back anyway. The longer the loan, the more the new
offer hurts. That's duration.

</details>

## Three funds, one fund house, very different behaviour

To see the two forces separately, here are three debt funds from the same
fund house, chosen because they sit at very different points on the duration
scale. Nothing here is about which is *better*; they are built to do
different jobs.

| Fund | What it holds | Typical duration |
|---|---|---|
| {{ ov.name }} | Paper maturing the next business day | 1 day |
| {{ mm.name }} | Money-market instruments up to a year | A few months |
| {{ g.name }} | Government securities, often long-dated | Several years |

Regular plans, {{ dbt.window_start }} to {{ dbt.window_end }} ({{ dbt.years }} years). Source:
{{ src.label }}, scheme codes {{ src.overnight.code }}, {{ src.money_market.code }} and {{ src.gilt.code }}. Historical NAV
data, for illustration only.

![Growth of ₹100 in three UTI debt funds since May 2018, and the gilt fund's rolling one-year return since 2007]({{ '/assets/charts/mf2-debt-funds.svg' | relative_url }})

| | {{ ov.name }} | {{ mm.name }} | {{ g.name }} |
|---|---:|---:|---:|
| Annualised return | {{ ov.cagr_pct }}% | {{ mm.cagr_pct }}% | {{ g.cagr_pct }}% |
| Annualised volatility | {{ ov.volatility_pct }}% | {{ mm.volatility_pct }}% | {{ g.volatility_pct }}% |
| Days with a negative NAV change | {{ ov.negative_days_pct }}% | {{ mm.negative_days_pct }}% | {{ g.negative_days_pct }}% |
| Worst single day | {{ ov.worst_day_pct }}% | {{ mm.worst_day_pct }}% | {{ g.worst_day_pct }}% |
| Worst fall from a peak | {{ ov.max_drawdown.worst_pct }}% | {{ mm.max_drawdown.worst_pct }}% | {{ g.max_drawdown.worst_pct }}% |
| Worst 1-year return | {{ ov.rolling_1y_min_pct }}% | {{ mm.rolling_1y_min_pct }}% | {{ g.rolling_1y_min_pct }}% |
| Best 1-year return | {{ ov.rolling_1y_max_pct }}% | {{ mm.rolling_1y_max_pct }}% | {{ g.rolling_1y_max_pct }}% |

Read the columns left to right. The overnight fund had **no** down days at all
in nearly eight years — pure accrual, nothing to reprice. The money market
fund had a few dozen ({{ mm.negative_days }} of {% include inr.html n=mm.days %} days — about one day in
{{ mm.days | times: 1.0 | divided_by: mm.negative_days | round }}), the worst being a {{ mm.worst_day_pct }}% day in the March 2020 panic, and it
was back at its high within {{ mm.max_drawdown.days_to_recover }} days. The gilt fund fell on
{{ g.negative_days_pct }}% of days — roughly two in five — because it is mostly a mark-to-market
instrument wearing a debt fund's label.

Notice the returns, too. The gilt fund's extra {{ g.cagr_pct | minus: ov.cagr_pct | round: 2 }}
percentage points a year over the overnight fund came with roughly
{{ g.volatility_pct | divided_by: ov.volatility_pct | round }} times the volatility. That is the trade the
[Sharpe ratio post]({% post_url 2026-10-23-volatility-and-sharpe %}) taught you to
look for — extra return is not free, and the price is paid in days like the ones
below.

## When rates move, the long end moves most

The same three funds through five interest-rate episodes. A blank cell means
the fund did not yet carry its present mandate for that window (the
overnight scheme became an overnight fund around May 2018, during SEBI's
recategorisation — that's where its NAV series changes character — and its
earlier history reflects a different portfolio).

| Episode | Window | Overnight | Money market | Gilt |
|---|---|---:|---:|---:|{% for e in dbt.episodes %}
| {{ e.label }} | {{ e.start }} to {{ e.end }} | {% if e.overnight_pct %}{{ e.overnight_pct }}%{% else %}—{% endif %} | {% if e.money_market_pct %}{{ e.money_market_pct }}%{% else %}—{% endif %} | **{{ e.gilt_pct }}%** |{% endfor %}

Two of those rows are the whole lesson.

**2013.** When the RBI squeezed liquidity in July 2013 to defend the rupee,
short-term yields spiked and long-bond prices fell. The gilt fund lost
{{ dbt.episodes[1].gilt_pct }}% between mid-May and late August, while the money market fund
quietly earned {{ dbt.episodes[1].money_market_pct }}% over the same fourteen weeks. Same rate
shock, opposite sign — because one fund had almost nothing to reprice and the
other had years of it.

**2008–09.** The other direction. As the RBI slashed rates after the Lehman
collapse, the gilt fund gained {{ dbt.gilt_2008_rally.rally_pct }}% between 1 October 2008 and its
peak on {{ dbt.gilt_2008_rally.peak_date }} — an equity-sized return from a government-bond fund —
and then gave back {{ dbt.gilt_2008_rally.fall_from_peak_to_31jan_pct | abs }}% within the month, including a
{{ dbt.gilt_worst_day.pct }}% single day on {{ dbt.gilt_worst_day.date }}.

Over its full {{ gl.years }}-year history the gilt fund's worst fall from a peak was
**{{ gl.max_drawdown.worst_pct }}%** (peak {{ gl.max_drawdown.peak_date }}, trough {{ gl.max_drawdown.trough_date }}), and it took
**{{ gl.max_drawdown.days_to_recover }} days** — over three years — to get back to that high. Its
worst one-year return was {{ gl.rolling_1y_min_pct }}%; its best was {{ gl.rolling_1y_max_pct }}%. Those are not
numbers most people associate with "debt".

## Credit risk: the third thing, which this data doesn't show

Everything above is *interest-rate* risk, on funds holding government or
top-rated paper. There is a separate risk the NAV history of these three funds
cannot illustrate: the borrower not paying.

A fund holding lower-rated corporate bonds earns a higher yield precisely
because some of those borrowers might default. When one does, the fund writes
the bond down — sometimes to zero, sometimes overnight. Indian debt-fund
investors saw this in 2018–2020 across several fund houses. The lesson is
structural, not about any one fund: a debt fund's yield above a government
bond of the same maturity is the market's price for credit risk, and that risk
tends to arrive all at once rather than a little each day.

The categories post later this week explains how SEBI's category labels
signal both risks — duration by name, credit by portfolio rules.

## Doing it in Python

The accrual-versus-repricing split is visible in the data with two lines: the
fraction of down days, and the size of the worst one.

```python
import pandas as pd

funds = {
    "overnight": "uti-overnight-fund-nav.csv",
    "money_market": "uti-money-market-fund-nav.csv",
    "gilt": "uti-gilt-fund-nav.csv",
}
for name, path in funds.items():
    nav = pd.read_csv(path, parse_dates=["date"]).set_index("date")
    r = nav.nav_regular_growth.loc["2018-05-03":].pct_change().dropna()
    print(f"{name:13s} down days {100*(r<0).mean():5.1f}%   "
          f"worst day {100*r.min():6.2f}%   "
          f"ann. vol {100*r.std()*252**0.5:5.2f}%")
```

One warning: two of these CSVs carry a face-value change (the NAV jumps ×100
on a single day when the unit face value moved from ₹10 to ₹1,000). A
`pct_change()` across that day reads as a 10,000% return. Check for
impossible one-day moves before computing anything — the
[data & methodology page]({{ '/methodology/' | relative_url }}) describes how
the series used here were spliced.

## Common mistakes

- **Reading "debt" as "safe".** The gilt fund holds the safest borrower in
  India and still fell {{ gl.max_drawdown.worst_pct }}% and needed three years to recover. Safe
  from default is not the same as safe from repricing.
- **Choosing a debt fund by last year's return.** A gilt fund's best years are
  the ones just after rates fell. The category that topped a one-year table
  usually did so *because* of the move that has now already happened.
- **Matching the wrong duration to the goal.** Money needed in six months
  does not belong in a fund whose NAV can fall 8% in a quarter. The
  duration of the fund and the horizon of the goal should roughly agree.
- **Ignoring credit risk because the NAV looks smooth.** Accrual funds
  holding lower-rated paper look like the overnight fund's line above — right
  up to the day a borrower defaults.
- **Forgetting tax.** Debt-fund gains bought after 1 April 2023 are taxed at
  your slab rate regardless of holding period — see the
  [tax series post on debt funds]({% post_url 2026-10-30-debt-funds-gold-and-the-rest %}).

**Takeaway:** A debt fund earns two ways — interest accruing daily, and bonds
repricing as rates move — and duration decides which one you feel. Across
eight years the overnight fund never had a down day, while the gilt fund fell
on two days in five — and over its full history once lost 16% peak to trough. Same fund house, same
word on the label, completely different instruments.
