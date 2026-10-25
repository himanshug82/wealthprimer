---
layout: post
title: "G-secs and T-bills: lending to the government"
description: "G-secs and T-bills are how the government borrows. How a T-bill's discount, a bond's coupon and its yield relate, using RBI's June 2026 auction results."
image: /assets/og/g-secs-and-t-bills.png
date: 2026-11-10 09:00:00 +0530
series: money-before-markets
term: "G-sec (government security)"
---

{% assign m = site.data.mbm %}
{% assign g = m.gsec %}
{% assign a = g.auction %}
{% assign tb = g.tbill %}
{% assign rd = g.retail_direct %}

## What a G-sec is

A **government security (G-sec)** is, in the words of the RBI (Reserve Bank of India), "a tradeable instrument issued by the Central Government or the State Governments." You lend money to the government and it repays you under fixed terms.

RBI's [primer on the G-sec market]({{ tb.source.url }}) (page dated {{ tb.source.page_date | date: "%-d %B %Y" }}) splits them by length:

- **Treasury bills (T-bills)** have original maturities under one year. As the primer describes them, they come in three tenors, 91, 182 and 364 days, are zero-coupon, and "pay no interest."
- **Dated securities**, often called government bonds, have original maturities of one year or more. They pay interest on the face value, half-yearly.

This is part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}). The [fixed deposit vs debt fund post]({% post_url 2026-11-09-fixed-deposit-vs-debt-fund %}) compared a fixed deposit (FD) with a debt fund; a gilt fund is a fund that holds the securities described here.

## How a T-bill earns and how a bond earns

A T-bill pays no coupon. It is issued below its face value and repaid at face value, so your return is the gap, called the **discount**. A dated security pays a **coupon** (a fixed rate on face value, in two instalments a year) and is repaid at face value on maturity. Its price on any day can be above or below face value, and that price sets its **yield**.

```
T-bill discount        =  face value − price paid
T-bill yield (simple)  =  discount / price paid  ×  365 / days to maturity

Bond coupon per half-year  =  face value × coupon rate / 2
Price below face value  →  yield above the coupon rate      (and the reverse)
```

The simple T-bill yield is an annualised measure for illustration. RBI's auction results report an **implicit yield at cut-off**, which is the yield the winning price works out to.

For a fuller treatment of what yield means for a bond held to the end, see [yield to maturity (YTM)]({% post_url 2026-10-05-yield-to-maturity %}).

## Worked example 1: RBI's own T-bill illustration

RBI's primer gives this example: a 91-day T-bill of ₹100 face value "may be issued at say ₹98.20", a discount of ₹1.80. The figures are RBI's illustration, not an auction result.

1. Discount = ₹{% include inr.html n=tb.face %} − ₹{{ tb.price_text }} = ₹{{ tb.discount_text }}.
2. Simple yield over the {{ tb.days }} days = {{ tb.discount_text }} / {{ tb.price_text }} = a gain of about {% assign p = tb.discount | divided_by: tb.price | times: 100 | round: 2 %}{% include inr.html n=p %}% in {{ tb.days }} days.
3. Annualised: that gain × 365 / {{ tb.days }} = **{% include inr.html n=tb.simple_yield_pct %}%** a year, simple.

## Worked example 2: four securities, one RBI auction

On {{ a.date | date: "%-d %B %Y" }} the RBI published the results of its [auction of four central government securities]({{ a.url }}), titled "{{ a.title }}". Prices are per ₹100 of face value. Data is as of that date, shown for illustration only.

| Security | Coupon | Cut-off price (₹) | Implicit yield at cut-off | Amount accepted (₹ crore) |
|---|---:|---:|---:|---:|
{% for r in a.rows -%}
| {{ r.name }} | {% assign x = r.coupon_pct %}{% include inr.html n=x %}% | {{ r.price_text }} | {{ r.yield_text }}% | {{ r.accepted_cr }} |
{% endfor %}
{{ a.devolvement }} "SGrB" is the label as printed in the release; this post doesn't cover that bond type.

What the table shows, and no more:

1. **Price against face value tells you where yield sits against the coupon.** {{ a.n_below_par }} of the {{ a.rows | size }} sold below ₹100, and their yields are above their coupons. The rest sold above ₹100, and their yields are below their coupons.
2. **The coupon is fixed; the yield isn't.** Per ₹10,000 of face value, {{ a.rows[0].name }} pays ₹{% assign x = a.rows[0].annual_coupon_per_10k %}{% include inr.html n=x %} a year, as two payments of ₹{{ a.rows[0].half_yearly_text }}. The cost of that ₹10,000 of face value at the cut-off price of ₹{{ a.rows[0].price_text }} was ₹{% assign x = a.rows[0].cost_of_10k_face %}{% include inr.html n=x %}. The yield of {{ a.rows[0].yield_text }}% is the return on that price, not on face value.
3. **On that day, yields mostly rose with maturity.** The 2029 bond cleared at {{ a.rows[0].yield_text }}%, the 2033 bond at {{ a.rows[1].yield_text }}% and the 2055 bond at {{ a.rows[2].yield_text }}%. The fourth bond, the 2056 maturity, cleared slightly below the 2055 bond, at {{ a.rows[3].yield_text }}%. That is one auction on one day. It isn't a rule about how yields relate to maturity.

## Can an individual buy one?

RBI's [Retail Direct scheme]({{ rd.url }}) lets individuals open a gilt account with RBI and bid in primary auctions of T-bills, dated G-secs and State Development Loans (SDLs, bonds issued by state governments). Individuals bid on a non-competitive basis: "by only entering the desired amount of securities, without entering a price." The minimum investment was ₹{% include inr.html n=rd.min_bid_face %} as on {{ rd.as_on | date: "%-d %B %Y" }}, the date printed on the page. Check the current terms before relying on that figure.

How the interest and gains are taxed is a separate question, covered in the Tax series. This post doesn't state a rule.

## Common mistakes

- **Reading the coupon as the return.** The coupon is set at issue. What you earn depends on the price you pay. In the table, the 2055 bond's coupon is below its yield because it sold below face value.
- **Assuming a G-sec's price can't fall.** RBI's primer says plainly that "if market interest rate levels rise, the price of a bond falls." Sell before maturity and you get the market price, not face value. [Modified duration]({% post_url 2026-10-06-modified-duration %}) measures how much.
- **Mixing up discount and coupon.** A T-bill has no coupon; its return is entirely the discount. Comparing it to a bond's coupon rate compares different things.
- **Treating one auction as "the" rate.** The table is a single day's results. Yields change from one auction to the next.

**Takeaway:** A G-sec is a tradeable loan to the government: a T-bill earns by being bought at a discount, and a dated security pays a fixed coupon while its price moves with market yields. Read the price against face value to see whether the yield is above or below the coupon, and remember that selling before maturity means taking the market price.
