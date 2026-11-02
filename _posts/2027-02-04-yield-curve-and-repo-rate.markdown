---
layout: post
title: "Yield curve and the repo rate: what the shape tells you"
seo_title: "What is a yield curve? Shape, repo rate and bond prices"
description: "The yield curve plots bond yields against maturity. Normal, flat and inverted shapes on an illustrative curve, and why long bonds move more."
image: /assets/og/yield-curve-and-repo-rate.png
date: 2027-02-04 09:00:00 +0530
series: jargon
term: "Yield curve"
---

{% assign c = site.data.jargon_m9.curve %}

## What is a yield curve?

A **yield curve** is a line that plots the yield on bonds of the same credit quality (usually government bonds) against how long until they mature. Short bonds on the left, long bonds on the right. The height at each point is the [YTM (yield to maturity)]({% post_url 2026-10-05-yield-to-maturity %}) for that maturity. Its **shape** is what people read: whether longer bonds pay more than shorter ones, the same, or less.

The **repo rate** is the rate at which the RBI (Reserve Bank of India) lends to banks against government securities. It is set by the RBI's Monetary Policy Committee and is its main policy rate. The textbook account is that short-term yields stay close to the policy rate and what markets expect it to do, while long-term yields also reflect expected inflation and the supply of and demand for bonds. This post uses an **illustrative** curve: the numbers are invented to show shapes, and are not a quote for any date. It is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

There is no formula for the curve itself. It is read off the yields. Two things are calculated from it:

```
Term spread          =  yield on a long bond  −  yield on a short bond
Price of a zero-coupon bond  =  Face value / (1 + yield)^years
```

## Worked example: three illustrative shapes

| Shape | 1 year | 2 years | 3 years | 5 years | 10 years | 10-year minus 1-year |
|---|---:|---:|---:|---:|---:|---:|
{% for s in c.curves %}{% assign sp = s.term_spread_10y_1y_pp %}| {{ s.shape | capitalize }} | {{ s.y1 }}% | {{ s.y2 }}% | {{ s.y3 }}% | {{ s.y5 }}% | {{ s.y10 }}% | {% include inr.html n=sp %} points |
{% endfor %}
- **Normal (upward-sloping):** longer bonds yield more. The usual compensation for tying money up longer and carrying more price risk.
- **Flat:** the same yield at every maturity.
- **Inverted:** short bonds yield *more* than long ones. This happens when markets expect the policy rate to fall, among other reasons. Inversions are often discussed as a warning sign, but the link to what follows is a matter of history, not a rule, and this post doesn't claim one.

On the normal curve, here is what a ₹1,000 zero-coupon bond (one that pays nothing until maturity) costs at each point, and what happens to its price if every yield on the curve rises by one point:

| Years to maturity | Yield | Price (₹) | Price change if yields rise 1 point |
|---:|---:|---:|---:|
{% for z in c.zero_prices %}{% assign pc = c.plus_1pt[forloop.index0].pct_change %}| {{ z.years }} | {{ z.yield_pct }}% | {{ z.price }} | {% include inr.html n=pc %}% |
{% endfor %}
The same one-point rise costs the ten-year bond several times what it costs the one-year bond. That is the [modified duration]({% post_url 2026-10-06-modified-duration %}) point in a different costume: **long bonds are more sensitive to yield changes**, which is why the right-hand end of the curve is where interest-rate risk sits.

## Common mistakes

- **Reading "the yield curve" as one rate.** It is a set of rates by maturity. When someone says it "rose", ask whether the whole line moved or only one end.
- **Treating the repo rate as the rate on every loan or bond.** It is a policy rate between the RBI and banks. Other rates are linked to it, imperfectly and with a lag.
- **Assuming an inverted curve predicts something.** It describes where yields are. What follows depends on much else.
- **Mixing credit qualities.** A curve compares like with like. A government curve and a corporate curve are different lines with a gap between them.

**Takeaway:** The yield curve plots bond yields against maturity, and its shape (upward, flat or inverted) shows how the market prices time. Because longer bonds lose more when yields rise, the same rate move hurts the long end of the curve far more than the short end.
