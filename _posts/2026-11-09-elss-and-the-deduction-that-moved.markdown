---
layout: post
title: "ELSS tax saving: what happened to the 80C deduction"
description: "The ₹1.5 lakh deduction still exists, but only in the old regime. What that means for ELSS, and how its lock-in interacts with tax on the way out."
image: /assets/og/elss-and-the-deduction-that-moved.png
date: 2026-11-09 09:00:00 +0530
series: tax
term: "ELSS"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## The question that changed

This post describes the rules for Tax Year 2026-27 (FY 2026-27, the financial
year from April 2026 to March 2027), as at November 2026. For two decades, the
standard route to a tax deduction in India was the one long known as 80C: up to
₹1.5 lakh in ELSS (equity-linked savings scheme) funds, the PPF (Public
Provident Fund), life insurance premiums, EPF (Employees' Provident Fund)
contributions, or home loan principal.

Whether that deduction applies to you now depends on which tax regime you are in.

## Two regimes, one of them now the default

India runs two parallel personal tax systems, and you choose between them:

| | Old regime | New regime |
|---|---|---|
| Slab rates | Typically higher rates at a given income | Typically lower rates at a given income |
| Deductions and exemptions | Available | **Mostly not** |
| Status | Opt in | **Default** |

The trade is explicit: the new regime has lower rates in exchange for
giving up most deductions. Because it is the **default**, the deduction
applies only to someone who has chosen the old regime. A deduction-linked
investment therefore has a tax effect only in the regime where the deduction exists.

**Note on section numbers.** The Income-tax Act, 2025 renumbered almost
everything — what everyone called 80C is now a differently numbered provision.
The Act's provision for the provident fund and life-insurance-premium deduction keeps the ₹1.5 lakh cap (as read in the ICAI copy of the Act). This series
refers to it by what it does rather than by number, because the number is
the part that changed.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two mobile phone plans.

**Plan A** has a higher monthly price, but you can claim money back for lots
of things — your case, your screen protector, your headphones.

**Plan B** is cheaper every month, but you can't claim anything back.

Neither is automatically better. It depends on how much stuff you
actually claim. Someone who buys nothing does better on Plan B; someone who
claims a lot might do better on Plan A.

The catch: if you don't choose, you're put on Plan B, and then the receipts
count for nothing.

</details>

## What ELSS actually is

**ELSS — equity-linked savings scheme** — is an equity mutual fund with two
distinguishing features:

- Contributions qualify for the ₹1.5 lakh deduction **in the old regime**
- A **three-year lock-in** on every contribution (as ELSS schemes are generally described; the Act text read for this series refers only to notified mutual fund schemes, so check the current scheme terms)

Two things about that lock-in are widely misunderstood.

**The lock-in is three years, as generally described; check the current scheme terms.** For comparison, PPF's term is fifteen years
and tax-saving fixed deposits are typically locked for five years (those two
figures come from the schemes' own rules, not from this post's sources; check the
current terms).

**It applies per instalment, not per investment.** A monthly SIP into an ELSS
fund locks each instalment for three years from *its own* date. The
instalment made in month 36 is locked until month 72. People routinely expect
the whole holding to unlock three years after they started; it doesn't. This
is the same lot-by-lot logic as [FIFO]({% post_url 2026-11-08-sips-and-fifo %}), applied
to a lock-in instead of a holding period.

## And it's still an equity fund

Whichever regime you're in, ELSS gains are taxed exactly like any other
equity fund — covered in the
[equity post]({% post_url 2026-11-04-equity-and-equity-funds %}):

| | |
|---|---|
| Holding period | Always long-term on exit, since the lock-in exceeds {{ r.equity_holding_months }} months |
| Rate | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption |

The deduction reduces your taxable income when you invest. It does not make
the eventual gain tax-free. Both facts get run together constantly.

## How the two regimes differ, briefly

This post does not say which regime suits anyone; it describes what differs.

- The old regime allows deductions (home loan interest, insurance premiums,
  house rent allowance and others) against higher slab rates.
- The new regime allows few deductions against lower slab rates. It also has a
  rebate that, in the ICAI copy of the Income-tax Act, 2025, removes tax on total
  income up to ₹12 lakh for a resident individual, but not on tax on
  special-rate gains such as equity capital gains. Check the current limit.
- A deduction reduces tax by the taxpayer's marginal rate (plus the
  {{ r.cess_pct }}% cess) on the amount deducted. The size of that saving depends
  on the slab the income falls in and on which regime applies.
- Whether a taxpayer can switch regimes from year to year depends on the type of
  income (salary or business). The switching rules are not covered here; check the
  current rule.

## Common mistakes

- **Assuming the deduction is still available by default.** The new regime
  is the default and mostly doesn't have it.
- **Counting a deduction you can't claim.** Under the new regime the deduction
  is not available, so an ELSS contribution has no deduction effect.
- **Thinking the ELSS lock-in runs from when you started.** Three years per
  instalment, each on its own clock.
- **Believing the deduction makes gains tax-free.** It reduces income now;
  the gains are taxed as equity later.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.

**Takeaway:** The ₹1.5 lakh deduction still exists, but only in the old
regime, and the new regime is the default. ELSS has a three-year lock-in per
instalment, and its gains are taxed like any other equity fund whichever
regime applies.
