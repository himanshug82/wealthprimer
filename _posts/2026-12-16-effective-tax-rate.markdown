---
layout: post
title: "Effective tax rate and deferred tax: why tax isn't PBT × a fixed rate"
seo_title: "Effective tax rate and deferred tax explained"
description: "The effective tax rate is tax expense divided by profit before tax. Why it differs from the statutory rate, and how deferred tax works, on Desi Bites."
image: /assets/og/effective-tax-rate.png
date: 2026-12-16 09:00:00 +0530
series: jargon
term: "Effective tax rate"
needs_review: tax
rules_as_of: "November 2026"
---

{% assign et = site.data.jargon_m9.etr %}
{% assign df = et.deferred %}

## What is the effective tax rate?

The **effective tax rate (ETR)** is the tax a company charged to its income statement in a year divided by its [profit before tax (PBT)]({% post_url 2026-08-22-reading-an-income-statement %}). It is a measured result, unlike the **statutory rate**, which is the headline rate set by law. The two can differ for several reasons: surcharge and cess on top of the headline rate; **permanent** differences (a common shorthand for income that is exempt and expenses the tax rules don't allow); and different rates on different income or changes in rates. **Timing** differences between accounting and tax rules do not, on their own, move the effective rate, because deferred tax (below) is there to absorb them. This post explains the mechanics on Desi Bites Foods, the blog's fictional company. It doesn't state any real company's tax rate, and it is not tax advice. It is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

```
Effective tax rate  =  Tax expense  /  Profit before tax

Tax expense  =  Current tax  +  Deferred tax
```

**Current tax** is what is payable for the year under the tax rules. **Deferred tax** is the accounting entry for differences in *timing* between when something hits accounting profit and when it hits taxable profit.

## Worked example: Desi Bites, three years

FY means financial year.

| Year | PBT (₹ lakh) | Tax (₹ lakh) | Effective tax rate |
|---|---:|---:|---:|
{% for r in et.rows %}| {{ r.fy }} | {{ r.pbt }} | {{ r.tax }} | {{ r.etr_pct }}% |
{% endfor %}
The case study uses a round {{ et.statutory_rate_pct | round }}% for teaching, before surcharge and cess. The effective rate sits within a fraction of a point of it every year, because the case-study books are built without unusual items; the small gaps are rounding to whole lakh.

A real company can sit well away from the headline, and here is how, on PBT of ₹{{ et.permanent.pbt | round }} lakh at that {{ et.permanent.rate_pct | round }}%:

| What changes | Tax (₹ lakh) | Effective tax rate |
|---|---:|---:|
| ₹{{ et.permanent.exempt_income | round }} lakh of the profit is exempt | {{ et.permanent.tax_with_exempt }} | {{ et.permanent.etr_with_exempt_pct }}% |
| ₹{{ et.permanent.disallowed | round }} lakh of expenses is disallowed | {{ et.permanent.tax_with_disallowed }} | {{ et.permanent.etr_with_disallowed_pct }}% |

Surcharge and cess lift the rate with no such difference at all. Under the Finance Act, 2026, for Tax Year 2026-27 (FY 2026-27), a domestic company with turnover up to ₹400 crore in tax year 2024-25 has a {{ et.surcharge_cess.headline_pct | round }}% rate. With {{ et.surcharge_cess.surcharge_pct | round }}% surcharge on income from ₹1 crore to ₹10 crore and {{ et.surcharge_cess.cess_pct | round }}% cess, that comes to {{ et.surcharge_cess.all_in_pct }}% (ignoring marginal relief near the band edges). Section 200 of the Income-tax Act, 2025 also offers an optional 22% rate, on its own conditions and surcharge. A one-year gap says little by itself, so compare several years and read the tax note in the annual report.

## What deferred tax means

Suppose a machine is depreciated ₹{{ df.book_dep | round }} lakh in the accounts this year, but the tax rules allow ₹{{ df.tax_dep | round }} lakh. Taxable profit is then lower than accounting profit by ₹{{ df.timing_difference | round }} lakh, for now. Over the asset's life the difference reverses, and the tax is paid later. Take PBT of ₹{{ df.pbt | round }} lakh and a {{ df.rate_pct | round }}% rate:

| | ₹ lakh |
|---|---:|
| Tax actually payable this year ((PBT + book depreciation − tax depreciation) × rate) | {{ df.current_tax }} |
| Deferred tax: tax on the ₹{{ df.timing_difference | round }} lakh difference, payable later | {{ df.dtl_created }} |
| **Tax expense in the income statement** | **{{ df.total_tax | round }}** |

The tax expense equals the rate times accounting profit (₹{{ df.pbt | round }} lakh × {{ df.rate_pct | round }}% = ₹{{ df.total_tax | round }} lakh) even though only ₹{{ df.current_tax }} lakh is due now. The remaining ₹{{ df.dtl_created }} lakh shows up on the balance sheet as a **deferred tax liability**: tax that will fall due when the timing difference reverses. That is the point of deferred tax: it matches the tax expense to the profit it relates to, so the **effective rate stays at {{ df.rate_pct | round }}% here** (₹{{ df.total_tax | round }} lakh on ₹{{ df.pbt | round }} lakh) even though the cash tax is lower this year. A timing difference changes when the cash leaves, not the effective rate. The accounting standard is Ind AS (Indian Accounting Standards) 12, *Income Taxes*, and a reader doesn't need its detail to read the number.

## Common mistakes

- **Expecting the effective rate to equal the statutory rate.** A gap can come from surcharge and cess, permanent differences or rate changes, and the annual report's tax note usually reconciles it. Look at that note before drawing a conclusion.
- **Comparing a one-year effective rate across companies.** One-off items (a write-off, a change in rates) distort a single year.
- **Treating deferred tax as a cash tax.** It's an accounting entry for taxes that will fall due or be saved in future years. Current tax is the part payable for this year; the cash can move at different times through advance tax, TDS (tax deducted at source) and refunds.
- **Not saying which tax rate you used for ROCE after tax.** Either the statutory or the effective rate can be used, in our view, and the answer differs, so state which. [ROCE (return on capital employed)]({% post_url 2026-09-03-roce %}) is a pre-tax measure, so it needs adjusting before you compare it with post-tax numbers.

**Takeaway:** The effective tax rate is the tax expense in the accounts divided by profit before tax, and it differs from the headline rate for reasons including surcharge, cess, exemptions and disallowed expenses. Deferred tax is the accounting for timing differences: it keeps them from distorting the rate, and it is not an extra tax paid today.
