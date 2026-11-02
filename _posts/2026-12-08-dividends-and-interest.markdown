---
layout: post
title: "Dividends and interest: taxed at your slab, with TDS on top"
description: "Both are added to your income and taxed at your slab rate. What changed when the dividend distribution tax went, and how TDS arrives before you file."
image: /assets/og/dividends-and-interest.png
date: 2026-12-08 09:00:00 +0530
series: tax
term: "Dividend and interest taxation (TDS)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## The simple bucket, with one sharp edge (Tax Year 2026-27)

For **Tax Year 2026-27 (FY 2026-27)** (FY is *financial year*), dividends and interest are simpler than capital gains:
both are **added to your total income and taxed at whatever slab rate
you fall into**. For a resident individual there are no holding periods and no
special rates, and dividends get no annual exemption. Savings-account interest
carries a small deduction, but only in the old regime (see below).

The sharp edge is that this used to be very different, and a lot of what
people believe about dividends dates from before it changed.

## Dividends are taxed in your hands

Older articles describe a system in which companies paid a dividend
distribution tax and the investor was mostly not taxed on the dividend itself.
That system was replaced. This post doesn't trace when or how, because it no longer applies to Tax Year 2026-27.
**Dividends are now added to the recipient's income and taxed at their slab rate.**

The practical effect depends entirely on your slab, and it's large:

| Your slab (illustrative, before surcharge; which regime's slabs apply is not shown) | Tax on ₹1,00,000 of dividend | With {{ r.cess_pct }}% cess |
|---|---:|---:|
| 5% | ₹5,000 | ₹5,200 |
| 20% | ₹20,000 | ₹20,800 |
| 30% | ₹30,000 | ₹31,200 |

Compare that with long-term capital gains on equity at {{ r.equity_ltcg_pct }}% with a
₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption: in the top slab, ignoring surcharge (capped at 15% on dividends and on these gains), a rupee of dividend carries a
higher rate than a rupee of long-term equity gain.

That bears on a point from the
[opening mutual funds post]({% post_url 2026-09-25-what-a-mutual-fund-is %}) and the
[growth vs IDCW post]({% post_url 2026-12-06-growth-vs-idcw %}): an IDCW (income
distribution cum capital withdrawal) payout is not extra return. The payout is
income at your slab rate when received, whereas the same value left in a growth
option is a capital gain, taxed when units are sold.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two ways of getting pocket money.

**Way one:** your savings jar just grows, and you only count it when you
decide to spend some. You're taxed on the bit you take, when you
take it.

**Way two:** every month someone takes coins out of your jar and hands them
to you — and you're taxed on those coins straight away, at your usual rate,
even if you put them right back.

Your jar has the same money in both cases. The difference is when the
counting happens and at what rate.

</details>

## TDS: tax deducted before it reaches you

Unlike capital gains, dividends and interest often arrive with tax already
withheld. **TDS — tax deducted at source** — means the payer deducts a slice
and deposits it against your PAN (permanent account number) before paying you the rest.

TDS on dividends and interest for residents is set by the table in section 393(1) of the Income-tax Act, 2025, and thresholds move with Budgets. As that table reads for Tax Year 2026-27:

| Income | TDS rate | Threshold in the table |
|---|---:|---|
| Dividend from a domestic company | 10% | None in the main row, but section 393(4) removes TDS where an individual's non-cash dividends from that company are ₹10,000 or less in the year |
| Bank, co-operative bank or post-office deposit interest | 10% | ₹50,000 a year (₹1,00,000 for a senior citizen) |
| Other interest, not on securities | 10% | ₹10,000 a year |
| Interest on securities | Rates in force | ₹10,000 a year |

These come from the table and the Finance Act, 2026 (First Schedule, Part II). Bonds have further carve-outs. Two things matter more than the exact thresholds.

**TDS is not your final tax.** It's an advance. Suppose, hypothetically, 10%
was withheld: if your slab is 30%, that leaves you owing the balance when you file. If you're below the
taxable limit, you claim it back as a refund. Either way, the deduction is
not the end of the story — and treating it as though it were is how people
end up with unexpected demands.

**No PAN can mean a higher rate.** Where PAN isn't provided, section 397 of the Act generally means
deduction at 20% if that's higher than the normal rate. Worth checking on old
accounts and inherited holdings.

## Interest

Same treatment, added to income at your slab rate. Some specifics worth
knowing:

- **Savings account interest** carries a deduction of up to ₹10,000 under section 153 of the Act. A senior citizen instead gets up to ₹50,000 on deposit interest in any account. Both sit in the part of the Act the new regime excludes (section 202(2)), so as we read it they apply only in the old regime.
- **Fixed deposit interest is generally taxable as it accrues each year**, not when the
  deposit matures. People with multi-year cumulative deposits routinely miss
  this and then face several years' tax at once.
- **Public Provident Fund interest and Employees' Provident Fund interest** have their own exemption rules, with limits; they are not covered here.

That fixed-deposit accrual point is the one that catches many people. How a bank deducts TDS on a cumulative deposit varies. The tax is generally due
year by year.

## Form 26AS and the AIS

Everything deducted against your PAN shows up in two places: **Form 26AS**
(the tax credit statement) and the **Annual Information Statement (AIS)**,
which is broader and includes reported dividends, interest and securities
transactions.

The tax department holds much of this data, so a mismatch between what you
report and what's in your AIS can lead to a query. Under the Income-tax Rules, 2026 the annual statement is Form No. 168 (rule 245), and the name "Form 26AS" doesn't appear in the Rules we read, so expect the labels to change for Tax Year 2026-27. The *Before you file* post
in this series covers reading these statements.

## Common mistakes

- **Believing dividends are still tax-free.** Older articles describe a system
  in which they mostly were in the investor's hands; that system
  ended.
- **Treating TDS as the final tax.** It's an advance against a liability that
  may be larger or smaller.
- **Missing accrued fixed-deposit interest.** Generally taxable each year, even on a
  cumulative deposit that pays nothing until maturity.
- **Assuming small dividends escape tax.** Below the TDS threshold means
  nothing was *deducted*, not that nothing is *taxable*.

## Sources

- [Income-tax Act, 2025 (a copy hosted by the Institute of Chartered Accountants of India, ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself, as read in that copy. Points not found there are marked "check the current rule".
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the amendments and the rates for Tax Year 2026-27.

**Takeaway:** Dividends and interest are added to your income and taxed at your slab rate, and TDS deducted along the way is an advance, not the final tax. Fixed deposit interest is generally taxed as it accrues, and the AIS already shows the tax department much of what you received.
