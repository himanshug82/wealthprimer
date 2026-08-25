---
layout: post
title: "WACC: the discount rate, and where it actually comes from"
date: 2026-10-29 09:00:00 +0530
series: fundamental-analysis
---

{% assign w = site.data.case_study.dcf.wacc %}
{% assign bi_is25 = site.data.real_company.income_statement.FY25 %}
{% assign bi_bs24 = site.data.real_company.balance_sheet.FY24 %}
{% assign bi_bs25 = site.data.real_company.balance_sheet.FY25 %}

## The rate you were told to take as given

The [last post]({% post_url 2026-10-27-discounting-time-value-of-money %}) discounted
cash flows at {{ w.wacc }}% and asked you to accept the number on faith. It also showed
that this single input swings the answer more than almost anything else in a
valuation. Time to earn it.

The rate you discount at should reflect what the money you're valuing
*costs*. A company is funded from two pockets — shareholders and lenders —
and each pocket demands a different return. **WACC — the Weighted Average
Cost of Capital** — blends the two in proportion to how much of each the
company actually uses.

Think of it as the hurdle rate. If a business can't earn more than its WACC
on the money it deploys, it's destroying value no matter how healthy the
profit line looks. (This is also the honest answer to why [ROCE]({% post_url 2026-09-03-roce %})
matters: ROCE above WACC is value creation, ROCE below it isn't.)

## The formula

```
WACC = (E / (D + E)) × Ke  +  (D / (D + E)) × Kd × (1 − t)

where  E  = market value of equity
       D  = market value of debt
       Ke = cost of equity
       Kd = cost of debt (pre-tax)
       t  = corporate tax rate
```

Two things in there aren't obvious.

**Why the (1 − t) on debt only.** Interest is a tax-deductible expense in
India, so borrowing ₹100 at 10% doesn't really cost the company ₹10 — it
costs ₹10 minus the tax it no longer pays on that ₹10. Dividends get no such
treatment. That deductibility is a genuine, structural advantage of debt over
equity, and the formula has to reflect it.

**Why equity is more expensive than debt.** It reliably surprises people that
Ke comes out higher than Kd. Lenders get paid first, get contractual
interest, and usually hold security. Shareholders get whatever's left over,
after everyone else, with no promises attached. For accepting that, they
demand more. Equity is the expensive money.

## Step 1: the cost of equity

There's no invoice for what shareholders expect — nobody sends the company a
bill. It has to be estimated, and the standard tool is the **Capital Asset
Pricing Model (CAPM)**:

```
Ke = Risk-Free Rate + Beta × Equity Risk Premium
```

| Input | What it is | Where to get it |
|---|---|---|
| Risk-free rate | Return on a genuinely safe asset | 10-year Government of India bond yield |
| Equity risk premium | Extra return investors demand for holding stocks over bonds | Estimated from long-run market data; 6–8% is the usual range quoted for India |
| Beta | How much this stock moves relative to the overall market | Regression against an index, or a sector average |

Beta is the piece worth pausing on. A beta of 1.0 means the stock tends to
move with the market. Above 1.0 means it swings harder in both directions;
below 1.0 means it's steadier. CAPM's core claim is that investors should be
compensated for the risk they *can't* diversify away — the market-wide kind —
and beta is its measure of that.

It's also the model's weakest limb. Beta is estimated from past price
movements, and a company's future volatility need not resemble its past.
Treat it as a defensible convention rather than a measurement.

## Step 2: the cost of debt

This one is easier, because there *is* an invoice. A company's interest
expense and its borrowings are both sitting in the accounts:

```
Kd (pre-tax) = Interest Expense / Average Total Debt
```

For a company with recently issued debt, the yield on that debt is better
still. But the accounts version is usually close enough and always available.

## Worked example: Desi Bites Foods Ltd

Building the rate used throughout this series' discounted cash flow (DCF)
model. First, the cost of
equity:

| Input | Value | Source |
|---|---:|---|
| Risk-free rate | {{ w.risk_free_rate }}% | Roughly the 10-year G-Sec (Government Security) yield, mid-2025 |
| Equity risk premium | {{ w.equity_risk_premium }}% | Illustrative India ERP |
| Beta | {{ w.beta }} | Illustrative, small-cap packaged foods |
| **Cost of equity** | **{{ w.cost_of_equity }}%** | {{ w.risk_free_rate }} + {{ w.beta }} × {{ w.equity_risk_premium }} |

Then the cost of debt, which for once comes straight out of the
[case study](/case-study/) rather than being assumed:

| Input | Value | Source |
|---|---:|---|
| FY25 interest expense | ₹47 Lakh | Income statement |
| Average term loan | ₹430 Lakh | (FY24 ₹460 + FY25 ₹400) / 2 |
| Cost of debt, pre-tax | {{ w.cost_of_debt }}% | 47 / 430 |
| Tax rate | {{ site.data.case_study.dcf.assumptions.tax_rate }}% | Indian domestic corporate rate |
| **Cost of debt, after tax** | **{{ w.cost_of_debt_after_tax }}%** | {{ w.cost_of_debt }} × (1 − 0.25) |

Now the weights. These use **market** values, not book values — the whole
point is what capital costs today, and Desi Bites' equity is worth its
₹{% include inr.html n=site.data.case_study.listing.market_cap %} Lakh market capitalisation at the IPO price, not the
₹{% include inr.html n=site.data.case_study.listing.post_ipo_equity %} Lakh of book equity:

| | ₹ Lakh | Weight |
|---|---:|---:|
| Equity (market cap) | {{ w.market_value_equity }} | {{ w.weight_equity }}% |
| Debt | {{ w.market_value_debt }} | {{ w.weight_debt }}% |
| **Total capital** | **8,400** | **100%** |

And the blend:

```
WACC = 0.952 × 14.20%  +  0.048 × 8.20%
     = 13.52%          +  0.39%
     = {{ w.wacc }}%
```

The result sits almost on top of the cost of equity, and that's not a
coincidence. Desi Bites is 95% equity-funded at market values, so the cheap
debt barely moves the average. Worth internalising: for most equity-heavy
companies, WACC is the cost of equity with a rounding error attached, and
agonising over the cost of debt is wasted effort.

## Worked example: Britannia's cost of debt

The one piece of a real company's WACC that can be read directly off the
filings, rather than estimated. From the
[audited consolidated FY25 results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf).
For illustration only.

{% assign bi_avg_debt = bi_bs24.total_borrowings | plus: bi_bs25.total_borrowings | divided_by: 2.0 %}
{% assign bi_kd = bi_is25.interest | times: 100.0 | divided_by: bi_avg_debt | round: 2 %}
{% assign bi_tax_rate = bi_is25.tax | times: 100.0 | divided_by: bi_is25.pbt | round: 1 %}

| | ₹ Crore |
|---|---:|
| FY25 finance costs | {{ bi_is25.interest }} |
| Total borrowings, FY24 | {{ bi_bs24.total_borrowings }} |
| Total borrowings, FY25 | {{ bi_bs25.total_borrowings }} |
| Average borrowings | {{ bi_avg_debt }} |
| **Cost of debt, pre-tax** | **{{ bi_kd }}%** |

Its effective tax rate is also observable — ₹{% include inr.html n=bi_is25.tax %} Cr of tax on ₹{% include inr.html n=bi_is25.pbt %} Cr of
pre-tax profit, or {{ bi_tax_rate }}%. So Britannia's after-tax cost of debt is roughly
{{ bi_kd }} × (1 − {{ bi_tax_rate }}%), a little over 6%.

Note how much cheaper that is than Desi Bites' {{ w.cost_of_debt }}%. Large, established,
low-leverage borrowers get better terms than small ones — which is itself a
real competitive advantage, and one that never shows up in a margin.

The rest of Britannia's WACC — its beta, its equity risk premium — would be
estimated, not observed, and this blog isn't going to publish a discount rate
for a real listed company. That's a short step from publishing a valuation
for it, and this is an educational blog, not a research service.

## The circularity nobody mentions

Look again at the weights in the Desi Bites table. To compute WACC, we used
the market value of equity — which came from the share price. But the entire
purpose of computing WACC is to discount cash flows and arrive at... a value
for the equity.

So the input depends on the output. That's genuinely circular, and it isn't
a mistake in this post — it's an acknowledged awkwardness in the standard
method. In practice people use the current market capitalisation and accept
the circularity, or iterate until the numbers settle, or use a target capital
structure instead of the current one.

It's worth knowing about, because it undercuts any claim that a DCF is
independent of market prices. The market price usually leaks into the model
through this door.

## Common mistakes

- **Using book value weights instead of market values.** Book equity is a
  historical accounting artefact. WACC is about what capital costs now, and
  for a listed company that means market capitalisation.
- **Forgetting the tax shield on debt.** Skip the (1 − t) and you overstate
  WACC, which understates the valuation. It's a small term in an
  equity-heavy company and a large one in a leveraged company.
- **Reaching for precision the inputs can't support.** The equity risk
  premium is an estimate with a range of several percentage points, and beta
  shifts depending on the period and index you regress against. A WACC quoted
  as "13.91%" is a convenient handle for a genuinely fuzzy number, not a
  measurement — this series carries the two decimals only so the arithmetic
  reconciles.
- **Applying one company's WACC to a different company.** Costs of capital
  are specific to the borrower and its risk. Britannia's cost of debt isn't
  available to Desi Bites, and that difference is the point.
- **Using WACC to discount cash flows meant for shareholders alone.** WACC
  is the blended cost of *all* capital, so it pairs with cash flows available
  to all capital providers — free cash flow to the firm, which the next post
  builds. Pair it with equity-only cash flows and you've double-counted the
  debt.

**Takeaway:** WACC blends what shareholders demand with what lenders charge,
weighted by how much of each the company uses and adjusted for the tax
deduction on interest. For an equity-heavy business it lands within a
whisker of the cost of equity — and since that number rests on an estimated
risk premium and a backward-looking beta, the honest way to hold a WACC is
as a plausible range, not a figure to two decimal places.
