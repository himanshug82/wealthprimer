---
layout: post
title: "Discounting: what a rupee five years from now is worth today"
date: 2026-10-27 09:00:00 +0530
series: fundamental-analysis
---

## The one idea the rest of valuation is built on

Offer someone ₹1,00,000 today or ₹1,00,000 in five years, and nobody
hesitates. Today, obviously. That instinct is correct, and the reasons
behind it are the whole of this post:

1. **You could invest it.** ₹1,00,000 in a government bond at 6.5% becomes
   more than ₹1,37,000 in five years. Waiting costs you that.
2. **Inflation.** ₹1,00,000 buys less in 2031 than it does in 2026.
3. **Risk.** A promise of money in five years is only as good as whoever is
   promising it. Some of them won't pay.

So a future rupee is worth less than a rupee today. **Discounting** is
simply the arithmetic that says *how much* less. Everything in the next
three posts — free cash flow forecasts, terminal value, and the full
**discounted cash flow (DCF)** model that the
[last post]({% post_url 2026-10-25-relative-valuation-comparables %}) promised — is this
single idea applied repeatedly.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your friend wants to borrow ₹100 and pay you back next year. If you'd said
yes to ₹100 today, would you say yes to getting ₹100 back in a year? Probably
not — you'd want a bit extra for waiting, and for the chance your friend
forgets.

Say ₹110 feels fair. That means, to you, ₹110 next year is worth exactly ₹100
today. Flip that around and you've done discounting: to find what future
money is worth now, you *shrink* it by however much you'd have demanded for
waiting. The longer the wait and the flakier the friend, the more you shrink
it.

</details>

## The formula

Compounding runs forwards; discounting is the same equation run backwards.

```
Future Value  = Present Value × (1 + r)ⁿ

                    Future Value
Present Value =  ────────────────
                     (1 + r)ⁿ

where  r = the discount rate (per year)
       n = number of years away
```

That denominator has a name worth knowing, because it appears in every DCF
table you'll ever read:

```
                        1
Discount Factor  =  ──────────
                     (1 + r)ⁿ
```

Multiply any future amount by its discount factor to get its present value.
A discount factor of 0.52 means "a rupee arriving in that year is worth 52
paise to me now."

## Worked example: the discount factors in this series

The DCF later in this series discounts Desi Bites' cash flows at
{{ site.data.case_study.dcf.wacc.wacc }}% — where that rate comes from is the
next post's job. For
now, take it as given and look at what it does to money over time:

| Year | n | Calculation | Discount factor | ₹100 in that year is worth |
|---|---:|---|---:|---:|
| FY26 | 1 | 1 / 1.1391¹ | 0.8779 | ₹87.79 |
| FY27 | 2 | 1 / 1.1391² | 0.7706 | ₹77.06 |
| FY28 | 3 | 1 / 1.1391³ | 0.6765 | ₹67.65 |
| FY29 | 4 | 1 / 1.1391⁴ | 0.5939 | ₹59.39 |
| FY30 | 5 | 1 / 1.1391⁵ | 0.5213 | ₹52.13 |

Read the last row again, because it's the row that trips people up. At a
{{ site.data.case_study.dcf.wacc.wacc }}% discount rate, money arriving five years out is worth barely half
its face value today. Not because anything went wrong — that's just what a
14%-ish rate does over five years.

This is also why long-dated cash flows get so little respect in a DCF, and
why the terminal value (covered two posts from now) needs handling with care:
it sits *past* the final forecast year, gets discounted hardest, and still
usually ends up being most of the answer.

## The discount rate is the entire argument

Here's what makes discounting treacherous. The arithmetic is trivial. The
input isn't — and small changes in `r` produce large changes in the answer.
Same ₹100 arriving in FY30:

| Discount rate | Factor | Present value of ₹100 |
|---:|---:|---:|
| 8% | 0.6806 | ₹68.06 |
| 11% | 0.5935 | ₹59.35 |
| {{ site.data.case_study.dcf.wacc.wacc }}% | 0.5213 | ₹52.13 |
| 17% | 0.4561 | ₹45.61 |
| 20% | 0.4019 | ₹40.19 |

Between 8% and 20% — both perfectly arguable rates for an Indian small-cap —
the same future rupee is worth anywhere from 40 to 68 paise. That's a 70%
spread on an identical cash flow, decided entirely by an assumption.

Hold onto that. When a DCF spits out a precise-looking value per share, this
is the joint where most of the imprecision entered.

## Discounting a stream: present value

Real valuations don't discount one payment, they discount a series of them.
The rule is unglamorous: discount each year separately, then add.

Suppose a business hands you ₹200 Lakh a year for three years, and you
discount at 13.91%:

| Year | Cash flow (₹ Lakh) | × Discount factor | Present value (₹ Lakh) |
|---|---:|---:|---:|
| 1 | 200 | 0.8779 | 175.6 |
| 2 | 200 | 0.7706 | 154.1 |
| 3 | 200 | 0.6765 | 135.3 |
| | **600** | | **465.0** |

₹600 Lakh of promised money is worth ₹465 Lakh today. The ₹135 Lakh
difference is the price of waiting.

## Doing it in Python

Worth having, because you'll want to check DCF spreadsheets against
something:

```python
def present_value(cash_flows, rate):
    """cash_flows: list of amounts, one per year, starting one year from now."""
    return sum(cf / (1 + rate) ** n for n, cf in enumerate(cash_flows, start=1))

flows = [200, 200, 200]
print(round(present_value(flows, 0.1391), 1))   # 465.0
```

Five lines, and it's the engine inside every DCF model in this series. The
hard part was never the code.

## Common mistakes

- **Discounting with a rate that doesn't match the cash flow.** Cash flows
  available to *all* investors (debt and equity) get discounted at the
  weighted average cost of capital. Cash flows available to shareholders
  only get discounted at the cost of equity. Mismatch these and the answer
  is wrong in a way that looks perfectly reasonable.
- **Mixing nominal and real.** If your cash flows already include inflation
  (nominal — which is how forecasts are normally built), discount at a
  nominal rate. Discounting nominal cash flows at a real rate quietly
  inflates the valuation.
- **Getting the timing off by a year.** A cash flow arriving in year one is
  divided by (1 + r)¹, not (1 + r)⁰. It sounds obvious, and it's an extremely
  common spreadsheet error — usually because someone put FY25 actuals in the
  first forecast column.
- **Treating the discount rate as a fact.** It's an assumption, it's
  contestable, and as the table above showed, it moves the answer more than
  almost anything else in the model. Anyone who quotes a discount rate to
  two decimal places without flinching hasn't thought about it hard enough.
- **Assuming a higher discount rate is the "safe" or conservative choice.**
  It's conservative for the *valuation*, but it isn't automatically more
  accurate. Padding the rate to feel prudent is just a different way of
  making the number up.

**Takeaway:** A rupee tomorrow is worth less than a rupee today, and
discounting is the arithmetic that prices the wait — divide each future cash
flow by (1 + r)ⁿ and add them up. The formula is easy; the discount rate is
the argument, and it moves the answer more than any other input you'll
choose.
