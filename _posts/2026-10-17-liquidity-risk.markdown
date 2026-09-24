---
layout: post
title: "Liquidity risk: what it costs to get out, and how long it takes"
description: "Impact cost, days to liquidate, and the stress tests small-cap and mid-cap funds have published since 2024 — what they show and what they can't."
image: /assets/og/liquidity-risk.png
date: 2026-10-17 09:00:00 +0530
series: risk
term: "Liquidity risk"
---

{% assign r2 = site.data.risk2 %}
{% assign d = r2.dataset %}
{% assign lq = r2.liquidity %}
{% assign bk = lq.book %}
{% assign o1 = bk.orders[0] %}
{% assign o2 = bk.orders[1] %}
{% assign o3 = bk.orders[2] %}
{% assign tf = lq.toy_fund %}
{% assign ss = lq.stress_small %}
{% assign sm = lq.stress_mid %}

## A price on the screen is not a price you can get

Every stock and fund shows a price. What it doesn't show is how much of it you
could actually sell *at* that price, today, before the price moves against
you. That gap is **liquidity risk**: the risk that turning a holding into cash
takes longer, or costs more, than you expected — usually at exactly the
moment you need the cash.

It has two faces. For a single order, it's the cost of pushing through the
buyers waiting at each price. For a portfolio — a mutual fund with thousands
of crores in small companies — it's time: how many days of normal trading it
would take to sell a large slice without flooding the market. This post
works both, and then reads the stress-test numbers that
small-cap and mid-cap funds have published since 2024.

## The formula

```
Impact cost (NSE's definition, for a given order size):
    Ideal price     =  (best buy price + best sell price) / 2
    Impact cost %   =  (ideal price − your average fill) / ideal price × 100   (selling)
                       (your average fill − ideal price) / ideal price × 100   (buying)

Days to liquidate one holding, trading a fraction of daily volume:
    Days  =  Rupees to sell  /  (participation rate × average daily traded value)

Days to sell a fund pro rata (every holding in proportion):
    Days  =  the slowest holding's days — the fund isn't done until it is
```

NSE Indices describes impact cost as "the percentage mark up observed while
buying / selling the desired quantity of a stock with reference to its ideal
price (best buy + best sell) / 2" ([methodology
document](https://www.niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf),
September 2026). It's one of the tests for index membership: a Nifty 50 stock
must have "traded at an average impact cost of 0.50 % or less during the last
six months for 90% of the observations for a portfolio of Rs. 10 crores."

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You want to sell 50 mangoes at the school fair. The first kid will pay ₹20
for three. The next will pay ₹19 for five. After that, people want them for
₹15. Selling *all* 50 today means taking whatever the later buyers offer.

Wait a few days and sell ten a day, and you might get ₹20 for all of them. So
you choose: sell fast and cheap, or slow and full-price. A big fund holding a
small company's shares faces the same choice — just with crores instead of
mangoes.

</details>

## Worked example 1: impact cost on an order book

A hypothetical order book — best sell at ₹{{ bk.best_ask }}, and these buyers
waiting:

| Bid price (₹) | Shares wanted |
|---:|---:|{% for b in bk.bids %}
| {{ b.price }} | {% include inr.html n=b.qty %} |{% endfor %}

The ideal price is ({{ bk.bids[0].price }} + {{ bk.best_ask }}) / 2 =
₹{{ bk.ideal }}. Now sell three different sizes:

| Shares sold | Average fill (₹) | Impact cost | Rupees lost vs ideal |
|---:|---:|---:|---:|{% for o in bk.orders %}
| {% include inr.html n=o.qty %} | {{ o.avg_price }} | {{ o.impact_pct }}% | ₹{% include inr.html n=o.cost_rupees %} |{% endfor %}

The first {% include inr.html n=o1.qty %} shares only pay half the spread. By
{% include inr.html n=o3.qty %} shares you've eaten deep into the book
and the average cost per share is {{ o3.impact_pct | divided_by: o1.impact_pct | round: 1 }}
times higher. Impact cost grows faster than order size — which is why it
matters far more to a large fund than to you. (The
[volume post]({% post_url 2026-10-07-volume %}) covers what traded quantity
does and doesn't tell you.)

## Worked example 2: how big is "big" for a real stock?

Britannia (NSE: BRITANNIA), a Nifty 50 company, daily data
{{ lq.britannia_window_start | date: "%-d %B %Y" }} to
{{ lq.britannia_window_end | date: "%-d %B %Y" }}
([Yahoo Finance]({{ d.britannia_source_url }}); NSE volume only, BSE
excluded, {{ lq.britannia_zero_volume_rows }} zero-volume rows dropped).
Historical data, for illustration only.

Median value traded per day: **₹{{ lq.britannia_median_traded_cr }} crore**.
If a seller wants to be no more than {{ lq.participation_pct }}% of each
day's trading — a common rule of thumb to avoid moving the price — here's how
long an exit takes:

| Position to sell | Trading days at {{ lq.participation_pct }}% of median daily value |
|---:|---:|{% for e in lq.exit_rows %}
| ₹{% include inr.html n=e.position_cr %} crore | {{ e.days }} |{% endfor %}

For an individual, even a large one, a Nifty 50 stock is effectively liquid.
For a fund holding hundreds of crores, the same arithmetic starts to count
in weeks — and that's a large-cap. Scale the median traded value down to a
small company trading a crore or two a day and the days multiply.

## Worked example 3: a fund is only as liquid as its slowest holding

A hypothetical ₹{% include inr.html n=tf.total_cr %} crore fund, selling every
holding pro rata at {{ lq.participation_pct }}% of each stock's average daily
value traded (ADV):

| Holding | Held (₹ cr) | ADV (₹ cr) | Can sell per day (₹ cr) | Days for 25% | Days for 50% |
|---|---:|---:|---:|---:|---:|{% for row in tf.rows %}
| {{ row.stock }} | {{ row.held_cr }} | {{ row.adv_cr }} | {{ row.sell_per_day_cr }} | {{ row.days_25 }} | {{ row.days_50 }} |{% endfor %}

Sold pro rata, the fund needs **{{ tf.days_50 }} trading days** to sell half —
set entirely by the micro-cap that's a tenth of the portfolio. Leave that one
out and it's {{ tf.days_50_ex_d }}. That's why the industry's stress test
(next section) drops the least liquid slice before counting days: otherwise
one illiquid tail would dominate every number. But the dropped slice doesn't
disappear: someone still has to sell it.

## The small-cap and mid-cap stress tests

After a direction from SEBI (the Securities and Exchange Board of India)
that the industry body AMFI (Association of Mutual
Funds in India) passed on to fund houses on 27 February 2024, small-cap and
mid-cap schemes began publishing risk parameters from March 2024, including a
liquidity stress test. The disclosures sit on AMFI's
[risk parameters page]({{ d.stress_source_url }}); the SEBI direction also
asked for policies on "moderating inflows, portfolio rebalancing" and on
protecting investors "from the first mover advantage of redeeming investors",
as fund houses' own policy documents quote it.

The standard format's column header reads: "Pro-rata liquidation after
removing bottom 20% of portfolio based on scrip liquidity (considering 10% PV
with 3x volumes)", where PV is participation volume and volumes are
"3-Month Daily Average traded volumes on both NSE and BSE". The result is the
"number of days that will be required to liquidate 50% and 25% of the
portfolio respectively on a pro-rata basis, under stress condition." The
format doesn't spell out the "3x volumes" adjustment further, so we don't
interpret it here.

Here is what the disclosures for **March 2026 portfolios** said, category by
category ([AMFI data]({{ d.stress_csv | relative_url }}), as published):

| | Small-cap schemes | Mid-cap schemes |
|---|---:|---:|
| Schemes reporting | {{ ss.schemes }} | {{ sm.schemes }} |
| Category assets (₹ crore) | {% include inr.html n=ss.aum_total_cr %} | {% include inr.html n=sm.aum_total_cr %} |
| Median days to sell 50% | {{ ss.median_days_50 }} | {{ sm.median_days_50 }} |
| Longest days to sell 50% | {{ ss.max_days_50 }} | {{ sm.max_days_50 }} |
| Asset-weighted average days to sell 50% | {{ ss.aum_weighted_days_50 }} | {{ sm.aum_weighted_days_50 }} |
| Schemes needing more than 30 days for 50% | {{ ss.schemes_over_30_days }} | {{ sm.schemes_over_30_days }} |
| Share of category assets in those schemes | {{ ss.share_aum_over_30_days_pct }}% | {{ sm.share_aum_over_30_days_pct }}% |
| Largest scheme: assets (₹ crore) / days for 50% | {% include inr.html n=ss.largest_aum_cr %} / {{ ss.largest_days_50 }} | {% include inr.html n=sm.largest_aum_cr %} / {{ sm.largest_days_50 }} |
| Rank correlation, scheme size vs days | {{ ss.spearman_aum_days }} | {{ sm.spearman_aum_days }} |

Two things stand out. The *typical* small-cap scheme reported
{{ ss.median_days_50 }} days to sell half its portfolio, but the
*asset-weighted* figure was {{ ss.aum_weighted_days_50 }}: the biggest schemes
take the longest, and most of the category's money sits in them
({{ ss.share_aum_over_30_days_pct }}% of small-cap assets were in schemes
reporting more than 30 days). And size and days line up almost perfectly —
a rank correlation of {{ ss.spearman_aum_days }}. That's worked example 3 at
industry scale: the same stocks, held in larger amounts, take longer to
sell.

These are self-reported numbers under one stylised scenario, not a
measurement of any fund's quality, and this post doesn't rank or name
schemes. They describe the category: when a large share of investors want out
of small companies at once, a fund can't sell at yesterday's prices on
yesterday's timetable.

## What a fund investor actually bears

You redeem at the day's NAV (net asset value — the per-unit value of the
fund; see [what a mutual fund is]({% post_url 2026-09-25-what-a-mutual-fund-is %}))
and get your money within days, whatever the stress test says. The cost of
selling illiquid stocks lands on the fund — and therefore on whoever *stays*.
Early redeemers leave at a NAV that doesn't yet reflect the discount the fund
will take selling the rest. That's the "first mover advantage" the SEBI
direction refers to. For debt funds SEBI has separate tools: liquidity-ratio
rules for open-ended debt schemes (circular of 25 June 2021) and a
[swing pricing framework](https://www.sebi.gov.in/legal/circulars/sep-2021/circular-on-swing-pricing-framework-for-mutual-fund-schemes_52997.html)
(circular of 29 September 2021) that can lower the NAV for exiting investors
when outflows are heavy. The
[debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) covers how
debt fund NAVs move in the first place.

## Common mistakes

- **Confusing a low share price with a liquid stock.** A ₹20 share that
  trades, say, ₹50 lakh a day is far less liquid than a ₹5,000 share that
  trades ₹150 crore. Liquidity is rupees traded, not the price tag — see
  [market cap]({% post_url 2026-09-27-market-cap %}) for why price alone
  says little.
- **Trusting average volume in a crisis.** Volume is measured in normal times
  and vanishes when everyone is selling. Averages are also flattered by a few
  huge days; medians are more honest, and even they assume someone is on the
  other side.
- **Assuming daily redemption means daily liquidity.** A fund promises you
  cash in days; its portfolio may need weeks. Normally the gap is invisible.
  In a stampede it's paid by the investors who remain.
- **Reading the stress-test days as a verdict.** They're one scenario,
  calculated by the fund house, dropping the least liquid 20%. A higher
  number describes size and holdings; it doesn't say a fund is bad, and a low
  number doesn't make a small-cap fund safe.

**Takeaway:** Liquidity risk is the gap between the price on the screen and
the price you can actually get for your size, in the time you have. In March
2026's stress tests the median small-cap fund reported {{ ss.median_days_50 }}
days to sell half its portfolio; the largest reported {{ ss.largest_days_50 }}. When everyone heads for the same door, size is what
slows you down.
