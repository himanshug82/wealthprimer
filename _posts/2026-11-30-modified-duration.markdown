---
layout: post
title: "Modified duration: how hard a bond falls when rates rise"
description: "Modified duration is the percentage a bond's price moves for a one-point move in yields. Our 5-year bond's is 4.05; a 10-year bond's is about twice that."
image: /assets/og/modified-duration.png
date: 2026-11-30 09:00:00 +0530
series: jargon
term: "Modified duration"
---

{% assign bd = site.data.jargon_m6.bond %}

## What duration means

The [YTM post]({% post_url 2026-11-29-yield-to-maturity %}) showed that bond
prices fall when yields rise. **Modified duration** says *by how much*: it is
the approximate percentage change in a bond's price for a one-percentage-point
change in its yield.

A duration of 4 means a 1% rise in yields knocks roughly 4% off the price; a
1% fall adds roughly 4%. Longer-dated bonds have higher durations, which is
why a gilt fund holding ten-year government bonds swings far more than a
liquid fund holding paper that matures in weeks — even though the government
bonds carry no credit risk at all.

Duration is the number that turns "interest rate risk" from a phrase into a
quantity.

## The formula

Two versions. **Macaulay duration** is the weighted-average time until you
receive the bond's cash flows, with each flow weighted by its present value:

```
Macaulay duration  =  Σ [ t × PV(CF_t) ] / Price

Modified duration  =  Macaulay duration / (1 + y)

Price change (%)   ≈  − Modified duration × Δy (in percentage points)
```

Macaulay is in years and has a nice intuition — it's the bond's "centre of
gravity" in time. Modified is the one you use for price sensitivity. For a
zero-coupon bond, Macaulay duration equals the maturity exactly, because all
the money arrives at the end. Modified duration is a bit lower, since it's
divided by (1 + y) — {{ bd.comparison[3].modified }} versus {{ bd.comparison[3].macaulay | round }} for the ten-year zero in the table
further down.

## Worked example: the same ₹{% include inr.html n=bd.face %} bond

Same fictional bond as last time: {{ bd.coupon_pct }}% coupon, {{ bd.years }} years, priced at
₹{{ bd.buy_price }} for a YTM of {{ bd.ytm_pct }}% (₹{{ bd.price_at_ytm }} at exactly {{ bd.ytm_pct | round }}%, the base the
percentage changes below are measured from).

Reusing the present-value table from the YTM post and weighting each year by
its PV:

| | |
|---|---:|
| Macaulay duration | {{ bd.macaulay_duration }} years |
| ÷ (1 + {{ bd.ytm_pct }}%) → **Modified duration** | **{{ bd.modified_duration }}** |

So the rule of thumb says a one-point move in yields should move the price by
about {{ bd.modified_duration }}%. Check it against the actual repricing:

| Yield moves to | Price | Actual change | Duration estimate |
|---|---:|---:|---:|
| {{ bd.ytm_pct | plus: 1 }}% (+1 pt) | ₹{{ bd.price_if_ytm_plus_1pct }} | {{ bd.pct_change_plus_1 }}% | −{{ bd.modified_duration }}% |
| {{ bd.ytm_pct | minus: 1 }}% (−1 pt) | ₹{% assign _pdn = bd.price_if_ytm_minus_1pct %}{% assign _pdn_i = _pdn | round %}{% if _pdn == _pdn_i %}{% include inr.html n=_pdn_i %}.00{% else %}{% include inr.html n=_pdn %}{% endif %} | +{{ bd.pct_change_minus_1 }}% | +{{ bd.modified_duration }}% |

Close, and not identical: the actual fall is a little smaller than the
estimate and the actual rise a little larger. That asymmetry is **convexity**
— the price-yield curve bends — and it always works in the bondholder's
favour. Duration is a straight-line approximation of a curve; it's excellent
for small moves and drifts for large ones.

## Why maturity matters so much

Same coupon, same yield, different maturities:

| Bond | Macaulay | Modified duration | Price change for +1 pt |
|---|---:|---:|---:|{% for c in bd.comparison %}
| {{ c.bond }} | {{ c.macaulay }} | {{ c.modified }} | {{ c.price_change_actual_plus_1pct }}% |{% endfor %}

A one-year bond barely notices a rate move. A ten-year bond loses about 7% —
seven times as much — on the identical change in yields. And the ten-year
zero coupon, which pays nothing until the end, loses nearly 9%.

This table is the whole reason debt funds are not "safe" in the way a fixed
deposit is. A fund holding ten-year gilts carries essentially zero risk of not
being repaid and very real risk of losing 7% in a year when yields rise a
point. A liquid fund, holding paper with a duration measured in weeks, carries
almost none of that. Both are "debt funds". The
[debt funds tax post]({% post_url 2026-10-30-debt-funds-gold-and-the-rest %}) treats
them alike; the market does not.

Every debt fund factsheet quotes its portfolio's modified duration for exactly
this reason. It is the single most useful number on the page.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Think of a see-saw with the bond's payments sitting along it — small coupons
spread out, and one big lump (the repayment) at the far end. Duration is where
you'd have to put the pivot to balance it. Payments that arrive far away push
the balance point out.

Now: the further out the balance point, the longer the lever — and the more a
small push (a change in interest rates) swings the whole thing.

</details>

## Common mistakes

- **Reading "government bond fund" as "no risk".** No *credit* risk. A gilt
  fund with a duration of 7 has as much interest rate risk as the table says.
- **Confusing duration with maturity.** A 5-year coupon bond has a duration
  of about 4, not 5, because the coupons arrive early. Only a zero-coupon
  bond's *Macaulay* duration equals its maturity (its modified duration is
  still a little lower).
- **Applying duration to big yield moves.** It's a linear approximation. For
  a 3-point move the convexity correction is no longer a rounding error.
- **Forgetting it cuts both ways.** Duration is also how much you *gain* when
  yields fall. Investors who bought long-duration funds before a rate-cutting
  cycle earned exactly this.

**Takeaway:** Modified duration is roughly the percentage a bond's price moves
for a one-point move in yields — {{ bd.modified_duration }} for our five-year bond, about 7 for a
ten-year one. It's why two funds that are both "debt" can behave nothing
alike, and it's the first number to read on a debt fund's factsheet.
