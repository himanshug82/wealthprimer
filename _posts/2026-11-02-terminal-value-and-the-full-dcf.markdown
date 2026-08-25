---
layout: post
title: "Terminal value: the number that quietly becomes most of your valuation"
date: 2026-11-02 09:00:00 +0530
series: fundamental-analysis
---

{% assign dcf = site.data.case_study.dcf %}
{% assign r = dcf.result %}
{% assign listing = site.data.case_study.listing %}

## The problem with stopping at year five

The [last post]({% post_url 2026-10-31-forecasting-free-cash-flow %}) forecast Desi Bites'
free cash flow to the firm (FCFF) through FY30. But the company doesn't dissolve on 31 March
2030. It carries on generating cash for decades, and all of that has value
too.

Forecasting it year by year isn't the answer — nobody can model FY47 with a
straight face. Instead, everything past the forecast horizon gets collapsed
into a single figure: the **terminal value**, the worth of all remaining
cash flows as of the final forecast year.

It sounds like a tidying-up exercise. It is usually most of the answer. In
the model below it's **{{ r.terminal_pct_of_ev }}% of the enterprise value** — the five years we
carefully forecast account for barely a quarter. That ratio is typical, and
it should make you handle this input more carefully than any other in the
model, not less.

## The formula

The standard approach is the **Gordon Growth model**, which values a cash
flow stream growing at a constant rate forever:

```
                FCFF_final × (1 + g)
Terminal Value = ─────────────────────
                      (WACC − g)

where  g = perpetual growth rate, forever
```

Then discount that back like any other future amount:

```
PV of Terminal Value = Terminal Value / (1 + WACC)ⁿ
```

Note it's discounted over `n` years — five here, not six. The terminal value
is expressed *as of* the end of FY30, so it travels back the same distance as
the FY30 cash flow.

## Choosing g, and the constraint that governs it

There's one rule about the perpetual growth rate, and it isn't a
convention — it's arithmetic. **`g` must be less than WACC.** Look at the
denominator: as `g` approaches WACC, the terminal value approaches infinity,
and past it the formula returns a negative number that means nothing.

That isn't a quirk of the formula. It's the formula refusing to model
something incoherent: a company growing faster than its cost of capital,
forever, would eventually be worth more than everything else in existence.

In practice `g` should sit at or below the long-run nominal growth rate of
the economy the company operates in — roughly 10–11% nominal for India, being
real growth plus inflation. This series uses {{ dcf.assumptions.terminal_growth }}%. A common alternative
is to use the expected long-run inflation rate, on the reasoning that a
mature company grows with prices and no faster.

Anything approaching 8–9% is a claim that the business will outgrow the
Indian economy in perpetuity. That's a big thing to assert in a spreadsheet
cell.

## Worked example: assembling the whole discounted cash flow model

Everything from the last four posts, in one place. All figures ₹ Lakh, as of
{{ dcf.valuation_date }}, discounted at {{ dcf.wacc.wacc }}%.

**Step 1 — discount the forecast cash flows.**

| Year | FCFF | Discount factor | Present value |
|---|---:|---:|---:|{% for y in dcf.forecast %}
| {{ y.year }} | {{ y.fcff }} | {{ y.discount_factor }} | {{ y.pv }} |{% endfor %}
| **Sum of PVs** | | | **{{ r.pv_forecast_fcff }}** |

**Step 2 — compute and discount the terminal value.**

```
TV = {{ dcf.forecast[4].fcff }} × (1 + 0.05) / (0.1391 − 0.05)
   = {{ dcf.forecast[4].fcff }} × 1.05 / 0.0891
   = {{ r.terminal_value }}

PV of TV = {{ r.terminal_value }} × {{ dcf.forecast[4].discount_factor }} = {{ r.pv_terminal_value }}
```

**Step 3 — add them for enterprise value.**

| | ₹ Lakh |
|---|---:|
| PV of forecast FCFF (FY26–FY30) | {{ r.pv_forecast_fcff }} |
| PV of terminal value | {{ r.pv_terminal_value }} |
| **Enterprise value** | **{{ r.enterprise_value }}** |

**Step 4 — bridge from enterprise value to equity value.**

This is the step people skip. Enterprise value is what the whole *business*
is worth, to lenders and shareholders together. Shareholders own what's left
after the lenders are paid, so subtract net debt:

| | ₹ Lakh |
|---|---:|
| Enterprise value | {{ r.enterprise_value }} |
| Less: Debt | {{ listing.post_ipo_debt }} |
| Add: Cash & equivalents | {{ listing.post_ipo_cash }} |
| **Equity value** | **{{ r.equity_value }}** |

Desi Bites holds far more cash than debt after its IPO — net debt of
₹{% include inr.html n=r.net_debt %} Lakh, i.e. net *cash* of ₹1,480 Lakh — so this step adds value rather
than subtracting it. Subtracting a negative is a reliable place to fumble a
sign; the sanity check is that a company with spare cash must be worth more
than the same company without it.

**Step 5 — divide by shares.**

| | |
|---|---:|
| Equity value | ₹{% include inr.html n=r.equity_value %} Lakh |
| Shares outstanding | {{ r.shares_lakh }} lakh |
| **Value per share** | **₹{% include inr.html n=r.value_per_share %}** |

## The model disagrees with the market

Desi Bites listed at ₹{% include inr.html n=r.ipo_price %}. This DCF says ₹{% include inr.html n=r.value_per_share %} — some 38% below the IPO price.

The tempting move here is to go back and adjust assumptions until the model
agrees with the price. Resist it, thoroughly. A model tuned to match a price
you already knew has told you nothing you didn't already know.

The useful move is to run the logic backwards and ask: *what would have to be
true* for ₹{% include inr.html n=r.ipo_price %} to be right? Holding the same forecast and the same WACC, that
price implies a perpetual growth rate of **{{ dcf.reverse.implied_terminal_growth }}%** — a claim that Desi
Bites grows at roughly the pace of the entire Indian economy, forever.

Or, keeping terminal growth at {{ dcf.assumptions.terminal_growth }}% and pushing on the operating
assumptions instead:

| Scenario | Assumptions | Value per share |
|---|---|---:|
| Base case | Growth fading 18% → 10%, [EBITDA]({% post_url 2026-08-28-ebitda-margin %}) margin to 17.5% | ₹{% include inr.html n=r.value_per_share %} |
| Market case | Growth 25% for five years, EBITDA margin to 20% | ₹{% include inr.html n=dcf.reverse.scenario_market_case %} |
| Aggressive | Growth 30% for five years, EBITDA margin to 22% | ₹{% include inr.html n=dcf.reverse.scenario_aggressive %} |

Now the ₹{% include inr.html n=r.ipo_price %} price says something specific and testable: it's priced for
sustained 25–30% revenue growth with meaningful margin expansion. Whether
that's optimistic or reasonable is a judgement about the business — but at
least it's a judgement about something concrete, rather than a squabble about
whether a stock "looks expensive."

This is a **reverse DCF**, and for most people it's the more useful direction
of travel. Forward DCF asks you to produce assumptions and hands you a
number. Reverse DCF takes the market's number and hands you the assumptions
hiding inside it — and those assumptions are far easier to argue with.

## The calculator

The full model as runnable Python — change the assumptions at the top and
everything downstream re-computes:

```python
FY25_REVENUE, TAX, DEP_PCT, NWC_PCT = 2592.0, 0.25, 0.045, 0.0868
WACC, TERMINAL_G = 0.1391, 0.05
NET_DEBT, SHARES = -1480.0, 12.5

growth    = [0.18, 0.16, 0.14, 0.12, 0.10]
margin    = [0.172, 0.174, 0.175, 0.175, 0.175]
capex_pct = [0.08, 0.08, 0.06, 0.05, 0.05]

flows, revenue = [], FY25_REVENUE
for g, m, cx in zip(growth, margin, capex_pct):
    prev, revenue = revenue, revenue * (1 + g)
    dep = revenue * DEP_PCT
    ebit = revenue * m - dep
    flows.append(ebit * (1 - TAX) + dep - revenue * cx - (revenue - prev) * NWC_PCT)

pv_flows = sum(cf / (1 + WACC) ** n for n, cf in enumerate(flows, start=1))
tv = flows[-1] * (1 + TERMINAL_G) / (WACC - TERMINAL_G)
pv_tv = tv / (1 + WACC) ** len(flows)

ev = pv_flows + pv_tv
equity = ev - NET_DEBT
print(f"PV of forecast   {pv_flows:8.1f}")
print(f"PV of terminal   {pv_tv:8.1f}  ({pv_tv / ev:.0%} of EV)")
print(f"Enterprise value {ev:8.1f}")
print(f"Value per share  {equity / SHARES:8.2f}")
```

<!-- GOOGLE-SHEET-TODO: a view-only Google Sheet version of this model still
     needs to be built and linked here ("make a copy to use"), per the
     calculators section of CLAUDE.md. The Python above stands on its own
     until then. -->

## Common mistakes

- **Not checking what share of the value is terminal.** If terminal value is
  {{ r.terminal_pct_of_ev }}% of your enterprise value, you have not really valued five years of
  forecasts — you've valued a growth rate in perpetuity, with a five-year
  preamble. Always compute this percentage. If it's above about 80%, the
  forecast horizon is probably too short.
- **Setting g too close to WACC.** The gap between them is the denominator.
  Narrow it and the terminal value explodes on arithmetic alone, not on
  anything you learned about the business.
- **Discounting the terminal value by the wrong number of years.** It's
  n years for an n-year forecast, not n + 1. Off by one here and the whole
  valuation shifts by roughly the WACC.
- **Getting the net debt sign wrong.** Subtract net debt from enterprise
  value. When the company holds net cash, net debt is negative and you're
  subtracting a negative — which adds. Sanity-check the direction every time.
- **Using the wrong share count.** Use the diluted, post-issue count, as the
  [EPS post]({% post_url 2026-10-09-eps %}) covered. Dividing by the pre-IPO count here would have
  produced ₹497 a share instead of ₹{% include inr.html n=r.value_per_share %} — a 25% error from one wrong cell.
- **Presenting the output as a precise number.** ₹{% include inr.html n=r.value_per_share %} is the arithmetic
  consequence of a stack of estimates. It is not what the share is worth to
  two decimal places, and the next post is entirely about why.

**Takeaway:** Terminal value collapses everything past the forecast horizon
into one number, and that number is usually most of the valuation — so the
perpetual growth rate deserves more scrutiny than any line in the forecast.
And when the model disagrees with the market price, the productive question
is never "which is right" but "what is the market assuming that I'm not."
