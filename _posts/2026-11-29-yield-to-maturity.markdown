---
layout: post
title: "YTM: what a bond actually pays if you hold it to the end"
description: "YTM is the one rate that makes a bond's coupons and repayment worth its price today. A 7% bond bought at Rs 960 yields 8%; a fund's quoted YTM isn't a promise."
image: /assets/og/yield-to-maturity.png
date: 2026-11-29 09:00:00 +0530
series: jargon
term: "YTM (yield to maturity)"
---

{% assign bd = site.data.jargon_m6.bond %}

## What YTM means

A bond pays a fixed **coupon** — say 7% of its ₹1,000 face value, every year —
and returns the face value at maturity. But you rarely buy a bond at exactly
₹1,000. If you pay less, you earn the coupons *and* a gain on the way to
₹1,000; pay more and you earn the coupons *minus* a loss. **Yield to maturity
(YTM)** is the one rate that accounts for both: the annual return you'd earn
if you bought at today's price, collected every coupon, and were repaid at
maturity.

Technically, it's the discount rate at which the present value of all the
bond's future cash flows equals its price. If that sentence sounds like the
[discounting post]({% post_url 2026-10-02-discounting-time-value-of-money %}),
it should — YTM is the same idea run backwards: instead of choosing a rate and
computing a value, you know the value (the price) and solve for the rate.

## The formula

```
                 C           C                 C + F
Price  =  ───────────  +  ─────────  + … +  ───────────
           (1 + y)¹       (1 + y)²           (1 + y)ⁿ

  C = annual coupon, F = face value, n = years to maturity
  y = YTM — solve for the y that makes the right side equal the price
```

There's no closed-form solution; you iterate (a spreadsheet's `RATE` or
`YIELD` function does it). The intuition is what matters: **price and yield
move in opposite directions**. Pay less, earn more.

## Worked example: a ₹{% include inr.html n=bd.face %} bond

Fictional bond, {{ bd.coupon_pct | round }}% annual coupon, {{ bd.years }} years to maturity, bought at
₹{% include inr.html n=bd.buy_price %}. (Indian government bonds usually pay their coupon in two
half-yearly instalments; one annual coupon keeps the arithmetic simple.)

First, the wrong-but-tempting number. **Current yield** is just coupon over
price: ₹{% include inr.html n=bd.annual_coupon %} / ₹{% include inr.html n=bd.buy_price %} = {{ bd.current_yield_pct }}%. It ignores that you'll also be
repaid ₹{% include inr.html n=bd.face %} for a bond you paid ₹{% include inr.html n=bd.buy_price %} for.

Now solve for the rate that discounts every cash flow back to ₹{% include inr.html n=bd.buy_price %}:

| Year | Cash flow | Present value at {{ bd.ytm_pct }}% |
|---|---:|---:|{% for s in bd.schedule_at_ytm %}
| {{ s.year }} | ₹{% include inr.html n=s.cash_flow %} | ₹{{ s.pv_at_ytm }} |{% endfor %}
| **Total** | | **₹{{ bd.price_at_ytm }} ≈ ₹{{ bd.buy_price | round }}** |

**YTM = {{ bd.ytm_pct | round }}%.** (Strictly, the rate that lands on ₹{{ bd.buy_price | round }} to the paisa is
{{ bd.ytm_exact_pct }}% — a hair above. Every figure here, and in the next post, uses the
rounded {{ bd.ytm_pct | round }}%, which is why the total comes to ₹{{ bd.price_at_ytm }}.) The extra {{ bd.ytm_pct | minus: bd.current_yield_pct | round: 2 }} points over the current
yield is, roughly, the ₹{{ bd.face | minus: bd.buy_price | round }} gain to face value, spread over five years.

The same bond at different prices, or equivalently different market yields:

| If the market yield is | The bond trades at |
|---:|---:|{% for p in bd.price_ladder %}
| {{ p.ytm_pct }}% | ₹{% include inr.html n=p.price %} |{% endfor %}

At a 7% yield the 7% bond is worth exactly par. Every point the market yield
rises, the price falls — and by *less* each time (₹44, ₹42, ₹40, ₹38 here),
which is a property called convexity you don't need yet. The next post, on
modified duration, puts a number on how much.

## What YTM means on a debt fund factsheet

Every debt fund factsheet quotes a **portfolio YTM** — the weighted average
YTM of the bonds it holds. Three reasons it isn't the return you'll get:

1. **It's before expenses.** Subtract the expense ratio. A portfolio YTM of
   7.5% in a fund charging 0.8% is a 6.7% starting point.
2. **The fund doesn't hold to maturity.** Open-ended funds buy and sell
   constantly; as yields move, so do bond prices, and so does the NAV. Only a
   *target-maturity* fund, held to its end date, roughly locks in its YTM.
3. **Yields change.** Coupons received get reinvested at whatever the market
   yield is then, not at today's YTM.

So portfolio YTM is a good description of what the fund currently owns and a
poor forecast of what you'll earn. The
[debt funds post]({% post_url 2026-10-30-debt-funds-gold-and-the-rest %})
covered how the gains are taxed.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your uncle promises to give you ₹70 every birthday for five years, and ₹1,000
on the fifth one. A friend offers to sell you that promise for ₹960 today.

YTM asks: if I hand over ₹960 now and collect everything my uncle promised,
what interest rate am I really earning? Because I paid less than ₹1,000 and
get ₹1,000 back at the end, it's a bit more than the ₹70-a-year suggests —
about 8%, not 7%.

</details>

## Common mistakes

- **Confusing coupon rate with yield.** The coupon is fixed at issue. The
  yield depends on what you paid. A "7% bond" yields 7% only if bought at par.
- **Using current yield as the return.** It skips the pull to par — {{ bd.current_yield_pct }}%
  versus {{ bd.ytm_pct | round }}% here.
- **Treating a fund's portfolio YTM as a promised return.** It's gross of
  expenses, assumes holding to maturity, and assumes yields don't move. Three
  assumptions, all routinely false.
- **Forgetting the relationship runs both ways.** If yields fall after you
  buy, your bond's price rises — the mirror image of the risk.

**Takeaway:** YTM is the single rate that makes a bond's future coupons and
repayment worth exactly what you paid for it — {{ bd.ytm_pct | round }}% for a {{ bd.coupon_pct | round }}% bond bought at
₹{% include inr.html n=bd.buy_price %}. Price and yield move in opposite directions, and a debt fund's quoted
YTM is a description of its holdings, not a forecast of your return.
