---
layout: post
title: "ELSS tax saving: what happened to the 80C deduction"
description: "As we read the rules, the ₹1.5 lakh deduction applies only in the old regime. What that means for ELSS, and how its lock-in interacts with tax on exit."
image: /assets/og/elss-and-the-deduction-that-moved.png
date: 2026-11-22 09:00:00 +0530
series: tax
term: "ELSS"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## The question that changed, Tax Year 2026-27

This post describes the rules for Tax Year 2026-27 (FY 2026-27, the financial
year from April 2026 to March 2027), as at November 2026. For many years, the
standard route to a tax deduction in India was the one long known as 80C: up to
₹1.5 lakh in ELSS (equity-linked savings scheme) funds, the PPF (Public
Provident Fund), life insurance premiums, EPF (Employees' Provident Fund)
contributions, or home loan principal.

Whether that deduction applies to you now depends on which tax regime you are in. The cap and the default-regime position below are from sections 123 and 202 of the Income-tax Act, 2025.

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
everything — what everyone called 80C is now section 123, with the same ₹1.5 lakh cap.


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

One thing about that lock-in is widely misunderstood. As generally described the lock-in is three years (check the current scheme terms). Other tax-linked savings products, such as PPF and tax-saving fixed deposits, have their own, different lock-ins; they are not covered here, so check each product's current terms.

**It applies per instalment, not per investment.** A monthly SIP (systematic investment plan) into an ELSS
fund locks each instalment for three years from *its own* date. The
instalment made in month 36 is locked until month 72. People routinely expect
the whole holding to unlock three years after they started; it doesn't. This
is the same lot-by-lot logic as [FIFO (first in, first out)]({% post_url 2026-11-20-sips-and-fifo %}), applied
to a lock-in instead of a holding period.

## And it's still an equity fund

Whichever regime you're in, ELSS gains are taxed exactly like any other
equity fund — covered in the
[equity post]({% post_url 2026-11-08-equity-and-equity-funds %}):

| | |
|---|---|
| Holding period | Always long-term on exit, since the lock-in exceeds {{ r.equity_holding_months }} months |
| Rate | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption, plus {{ r.cess_pct }}% cess (and surcharge where it applies) |

The deduction reduces your taxable income when you invest. It does not make
the eventual gain tax-free. Both facts get run together constantly.

## How the two regimes differ, briefly

This post does not say which regime suits anyone; it describes what differs.

- The old regime allows deductions (home loan interest, insurance premiums,
  house rent allowance and others) against higher slab rates.
- The new regime allows few deductions against lower slab rates. It also has a
  rebate (section 156 of the Act) that removes tax on total
  income up to ₹12 lakh for a resident individual, but not tax on
  special-rate gains such as long-term equity gains.
- A deduction reduces tax by the taxpayer's marginal rate (plus the
  {{ r.cess_pct }}% cess) on the amount deducted. The size of that saving depends
  on the slab the income falls in and on which regime applies. Surcharge, where it applies, adds to this.
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
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the amendments and the rates for Tax Year 2026-27.

**Takeaway:** The ₹1.5 lakh deduction applies only in the old
regime, and the new regime is the default. ELSS has a lock-in per
instalment (about three years, as generally described; check the scheme terms), and its gains are taxed like any other equity fund whichever
regime applies.
