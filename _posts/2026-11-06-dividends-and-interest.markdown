---
layout: post
title: "Dividends and interest: taxed at your slab, with TDS on top"
description: "Both are added to your income and taxed at your slab rate. What changed when the dividend distribution tax went, and how TDS arrives before you file."
image: /assets/og/dividends-and-interest.png
date: 2026-11-06 09:00:00 +0530
series: tax
term: "Dividend and interest taxation (TDS)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "August 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## The simple bucket, with one sharp edge

For **Tax Year 2026-27 (FY 2026-27)** (FY is *financial year*), dividends and interest are simpler than capital gains:
both are **added to your total income and taxed at whatever slab rate
you fall into**. No holding periods, no special rates, no annual exemption.

The sharp edge is that this used to be very different, and a lot of what
people believe about dividends dates from before it changed.

## Dividends are taxed in your hands

Older articles describe a system in which companies paid a dividend
distribution tax and the investor was mostly not taxed on the dividend itself.
That system was replaced; its details weren't re-checked for this post.
**Dividends are now added to the recipient's income and taxed at their slab rate.**

The practical effect depends entirely on your slab, and it's large:

| Your slab (illustrative) | Tax on ₹1,00,000 of dividend | With {{ r.cess_pct }}% cess |
|---|---:|---:|
| 5% | ₹5,000 | ₹5,200 |
| 20% | ₹20,000 | ₹20,800 |
| 30% | ₹30,000 | ₹31,200 |

Compare that with long-term capital gains on equity at {{ r.equity_ltcg_pct }}% with a
₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption: in the top slab a rupee of dividend carries a
higher rate than a rupee of long-term equity gain.

That bears on a point from the
[opening mutual funds post]({% post_url 2026-09-25-what-a-mutual-fund-is %}) and the
[growth vs IDCW post]({% post_url 2026-11-05-growth-vs-idcw %}): an IDCW (income
distribution cum capital withdrawal) payout is not extra return. The payout is
income at your slab rate when received, whereas the same value left in a growth
option is a capital gain, taxed when units are sold.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two ways of getting pocket money.

**Way one:** your savings jar just grows, and you only count it when you
decide to spend some. You're taxed a little, on the bit you take, when you
take it.

**Way two:** every month someone takes coins out of your jar and hands them
to you — and you're taxed on those coins straight away, at your usual rate,
even if you put them right back.

Your jar has the same money in both cases. The difference is when the
counting happens and at what rate.

</details>

## TDS: tax deducted before it reaches you

Unlike capital gains, dividends and interest usually arrive with tax already
withheld. **TDS — tax deducted at source** — means the payer deducts a slice
and deposits it against your PAN (permanent account number) before paying you the rest.

| Income | Typically deducted at |
|---|---|
| Dividends from shares and mutual funds | Check the current rule (rate and threshold) |
| Bank fixed deposit interest | Check the current rule |
| Interest on bonds | Check the current rule; many listed demat debentures differ |

The Income-tax Act, 2025 sets rates and thresholds in a TDS table, and
thresholds move with Budgets. The table in the Act we opened showed a ₹1,00,000
bank-interest threshold for senior citizens and ₹50,000 for others, and a ₹10,000
threshold for interest on securities; we did not reconcile the dividend row, which
conflicts with an older Budget note, so no figure is given here. Two things matter more than the exact thresholds.

**TDS is not your final tax.** It's an advance. If you're in the 30% slab,
10% withheld leaves you owing the balance when you file. If you're below the
taxable limit, you claim it back as a refund. Either way, the deduction is
not the end of the story — and treating it as though it were is how people
end up with unexpected demands.

**No PAN means a much higher rate.** Where PAN isn't provided, deduction runs
at a considerably higher rate. Worth checking on old accounts and inherited
holdings.

## Interest

Same treatment, added to income at your slab rate. Some specifics worth
knowing:

- **Savings account interest** gets a modest deduction in the Act (₹10,000 a year for most individuals; a higher limit for senior citizens). Whether it is available in the new regime is not confirmed here; check the current rule.
- **Fixed deposit interest is generally taxable as it accrues each year**, not when the
  deposit matures. People with multi-year cumulative deposits routinely miss
  this and then face several years' tax at once.
- **Public Provident Fund interest and Employees' Provident Fund interest** have their own exemption rules, with limits; they are not covered here, so check the current rule.

That fixed-deposit accrual point is the one that catches most people. The
bank may not deduct anything until maturity, but the tax was due year by
year.

## Form 26AS and the AIS

Everything deducted against your PAN shows up in two places: **Form 26AS**
(the tax credit statement) and the **Annual Information Statement (AIS)**,
which is broader and includes reported dividends, interest and securities
transactions.

The tax department already has this data, so a mismatch between what you
report and what's in your AIS can lead to a query. The *Before you file* post
in this series covers reading these statements.

## Common mistakes

- **Believing dividends are still tax-free.** They've been taxed in the
  recipient's hands since 2020.
- **Treating TDS as the final tax.** It's an advance against a liability that
  may be larger or smaller.
- **Missing accrued fixed-deposit interest.** Taxable each year, even on a
  cumulative deposit that pays nothing until maturity.
- **Assuming small dividends escape tax.** Below the TDS threshold means
  nothing was *deducted*, not that nothing is *taxable*.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.

**Takeaway:** Dividends and interest are added to your income and taxed at your slab rate, and TDS deducted along the way is an advance, not the final tax. Fixed deposit interest is generally taxed as it accrues, and the AIS already shows the tax department what you received.
