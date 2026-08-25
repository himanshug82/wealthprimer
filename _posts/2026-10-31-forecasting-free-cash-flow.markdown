---
layout: post
title: "Forecasting free cash flow: the half of a DCF that actually matters"
date: 2026-10-31 09:00:00 +0530
series: fundamental-analysis
---

{% assign dcf = site.data.case_study.dcf %}
{% assign a = dcf.assumptions %}
{% assign bi_r = site.data.real_company.ratios.FY25 %}

## What we're forecasting, and why it isn't profit

We have a discount rate. We need something to discount. That something is
**free cash flow to the firm (FCFF)** — the cash a business generates that's
genuinely available to everyone who funded it, lenders and shareholders
both, after paying for everything the business needs to keep running and
growing.

Two words in there are doing real work.

**Cash**, not profit. Profit is an accounting opinion about which period a
transaction belongs to. Depreciation reduces profit without any money
leaving; a factory purchase drains the bank account without touching profit
much at all. A discounted cash flow (DCF) model values cash because cash is what you can
actually pay out.
This blog's post on [OCF/PAT]({% post_url 2026-10-03-ocf-pat %}) is the same argument in ratio form.

**To the firm**, not to shareholders. FCFF is measured *before* interest
payments, which is why it pairs with [WACC]({% post_url 2026-10-29-wacc-cost-of-capital %})
— the blended cost of all capital. The debt gets accounted for on the other
side, when we subtract net debt at the end. Handle it in both places and
you've charged for the borrowing twice.

## The formula

```
FCFF = EBIT × (1 − tax rate)          ← operating profit, after notional tax
     + Depreciation & Amortisation    ← add back: reduced profit, cost no cash
     − Capital Expenditure            ← subtract: real cash, never hit profit
     − Increase in Net Working Capital ← subtract: cash tied up in the business
```

Line by line:

- **EBIT × (1 − t)**, sometimes called NOPAT — Net Operating Profit After
  Tax. Start from [operating profit]({% post_url 2026-08-22-reading-an-income-statement %}),
  before interest, and tax it as if the company had no debt at all. The tax
  benefit of the debt has already been handled inside WACC.
- **Add back depreciation.** It was subtracted to get to EBIT, but no money
  moved. This is the classic reason [EBITDA]({% post_url 2026-08-28-ebitda-margin %}) exists as a concept.
- **Subtract capex.** Machines wear out and factories need building. Skip
  this and you've valued a business that never reinvests, which is a business
  that eventually stops existing.
- **Subtract the increase in [net working capital]({% post_url 2026-09-17-net-working-capital %}) (NWC).** Growth swallows cash.
  Selling more means holding more inventory and waiting on more receivables,
  and that money is tied up until the business shrinks again. The
  [cash conversion cycle]({% post_url 2026-09-13-cash-conversion-cycle %}) post covers the mechanics.

Note that working capital enters as the *change*, not the level. A company
with steady working capital consumes no incremental cash even if the balance
is large; a fast-growing one bleeds cash into it every year.

## Building the forecast

Forecasting isn't guessing a revenue number for FY30. It's choosing a small
set of drivers and letting the arithmetic carry them forward. For Desi
Bites, five drivers do the whole job:

| Driver | Assumption | Reasoning |
|---|---|---|
| Revenue growth | 18% falling to 10% by FY30 | FY24 and FY25 both grew ~20%; growth rates fade as a base gets larger |
| EBITDA margin | 17.2% rising to 17.5% | FY25 was 17.0% after three years of steady expansion; assumes the trend flattens |
| Depreciation | {{ a.depreciation_pct_revenue }}% of revenue | FY25 actual: 115 / 2,592 = 4.4% |
| Capex | 8% of revenue, easing to 5% | The IPO raised money for expansion, so capex runs above FY25's {{ site.data.case_study.ratios.FY25.capex_intensity }}% before normalising |
| Working capital | {{ a.nwc_pct_revenue }}% of revenue | FY25: (inventory 211 + receivables 199 − payables 185) / 2,592 |

The fading growth rate deserves a defence, since it's the assumption people
most often get wrong. Extrapolating 20% growth indefinitely produces
absurdities quickly — a company growing 20% a year for 30 years becomes
larger than its entire addressable market. High growth attracts competition,
large bases are harder to grow, and the fade is the norm. Assume otherwise
and you should be able to say why.

Also note what the capex assumption is doing. Desi Bites raised
₹{% include inr.html n=site.data.case_study.listing.ipo_proceeds %} Lakh in its IPO explicitly to expand. Modelling flat capex
while that cash sits on the balance sheet would give you the cash *and* the
growth for free. If the money is being spent, the model has to spend it.

## Worked example: Desi Bites Foods Ltd, FY26–FY30

All figures ₹ Lakh, built off the FY25 actuals in the
[case study](/case-study/).

| | {% for y in dcf.forecast %}{{ y.year }} | {% endfor %}
|---|{% for y in dcf.forecast %}---:|{% endfor %}
| Revenue growth | {% for y in dcf.forecast %}{{ y.revenue_growth }}% | {% endfor %}
| Revenue | {% for y in dcf.forecast %}{{ y.revenue }} | {% endfor %}
| EBITDA margin | {% for y in dcf.forecast %}{{ y.ebitda_margin }}% | {% endfor %}
| EBITDA | {% for y in dcf.forecast %}{{ y.ebitda }} | {% endfor %}
| Less: Depreciation | {% for y in dcf.forecast %}{{ y.depreciation }} | {% endfor %}
| **EBIT** | {% for y in dcf.forecast %}**{{ y.ebit }}** | {% endfor %}
| NOPAT (EBIT × 0.75) | {% for y in dcf.forecast %}{{ y.nopat }} | {% endfor %}
| Add: Depreciation | {% for y in dcf.forecast %}{{ y.depreciation }} | {% endfor %}
| Less: Capex | {% for y in dcf.forecast %}{{ y.capex }} | {% endfor %}
| Less: Increase in NWC | {% for y in dcf.forecast %}{{ y.change_in_nwc }} | {% endfor %}
| **FCFF** | {% for y in dcf.forecast %}**{{ y.fcff }}** | {% endfor %}

Now read the FCFF row, because it tells a story the revenue row hides.
Revenue climbs smoothly every single year. Free cash flow does not — it sits
at ₹{% assign _f0 = dcf.forecast[0].fcff %}{% include inr.html n=_f0 %} Lakh in FY26 and ₹{% assign _f1 = dcf.forecast[1].fcff %}{% include inr.html n=_f1 %} Lakh in FY27, then jumps to ₹{% assign _f2 = dcf.forecast[2].fcff %}{% include inr.html n=_f2 %} Lakh in
FY28 and keeps climbing.

Nothing improved operationally in FY28. Capex intensity simply dropped from
8% to 6% as the expansion programme wound down. The business was generating
plenty of operating cash in FY26 and FY27; it was spending it on factories.

This is worth dwelling on, because the same effect appears in real accounts.
The [free cash flow post]({% post_url 2026-10-01-free-cash-flow %}) noted that Britannia's FCF rose
between FY24 and FY25 mainly because capex fell from 3.3% to {{ bi_r.capex_intensity }}% of revenue,
not because operations got better. Weak free cash flow during a build-out
phase is not the same thing as a weak business — and strong free cash flow
from a capex holiday is not the same thing as a strong one.

## Doing it in Python

The whole forecast, in a form you can change one number in and re-run:

```python
FY25_REVENUE = 2592.0
TAX, DEP_PCT, NWC_PCT = 0.25, 0.045, 0.0868

growth = [0.18, 0.16, 0.14, 0.12, 0.10]
margin = [0.172, 0.174, 0.175, 0.175, 0.175]
capex_pct = [0.08, 0.08, 0.06, 0.05, 0.05]

revenue = FY25_REVENUE
for year, (g, m, cx) in enumerate(zip(growth, margin, capex_pct), start=2026):
    prev, revenue = revenue, revenue * (1 + g)
    dep = revenue * DEP_PCT
    ebit = revenue * m - dep
    fcff = (ebit * (1 - TAX) + dep
            - revenue * cx
            - (revenue - prev) * NWC_PCT)
    print(f"FY{year}  revenue {revenue:7.1f}  EBIT {ebit:6.1f}  FCFF {fcff:6.1f}")
```

Run it and you get the FCFF row above. Change `growth` to a flat 25% and
watch what happens to the answer — that's the exercise the sensitivity post
two posts from now is built on.

## Common mistakes

- **Subtracting interest.** The single most common FCFF error. Interest is
  excluded here *by design*, because WACC already accounts for the cost of
  debt. Subtract it as well and you've penalised the company twice for the
  same borrowing.
- **Ignoring working capital entirely.** It's the least visible line and it
  can be the difference between a business that funds its own growth and one
  that needs a rights issue every three years.
- **Forecasting capex below depreciation forever.** That's a company whose
  asset base is shrinking. Fine for a few years of a capex holiday, incoherent
  as a permanent assumption — over the long run, maintenance capex and
  depreciation should converge.
- **Building a ten-year forecast because it looks more thorough.** Nobody
  can forecast year eight of an Indian mid-cap. Longer forecasts don't add
  accuracy, they add false precision — and they quietly shift value out of
  the explicit forecast and into the terminal value, where it's harder to
  scrutinise. Five years is the usual compromise.
- **Assuming margins expand indefinitely.** Every percentage point of margin
  expansion needs a reason — pricing power, scale, a better mix. "It went up
  last year" isn't one.
- **Forecasting backwards from the answer.** If you know what the share
  price is and you nudge growth rates until the model agrees with it, you
  haven't valued anything. You've decorated a number you already had.

**Takeaway:** Free cash flow to the firm is operating profit after notional
tax, plus depreciation, minus capex and the cash growth swallows into working
capital — the money genuinely available to everyone who funded the business.
Forecast it from a handful of defensible drivers rather than a revenue
hunch, and expect the cash flow line to be lumpier than the revenue line,
because reinvestment is lumpy.
