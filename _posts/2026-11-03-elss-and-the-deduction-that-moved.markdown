---
layout: post
title: "ELSS and the deduction that moved: 80C under the new regime"
description: "The ₹1.5 lakh deduction still exists, but only in the old regime. What that means for ELSS, and how its lock-in interacts with tax on the way out."
image: /assets/og/elss-and-the-deduction-that-moved.png
date: 2026-12-30 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## The question that changed

For two decades, "how do I save tax?" had a standard answer in India: put
₹1.5 lakh into something that qualifies for the deduction long known as 80C —
ELSS funds, PPF, life insurance premiums, EPF contributions, home loan
principal.

That answer is now conditional, and for a growing number of people it's
simply no longer available.

## Two regimes, one of them now the default

India runs two parallel personal tax systems, and you choose between them:

| | Old regime | New regime |
|---|---|---|
| Slab rates | Higher | Lower |
| Deductions and exemptions | Available | **Mostly not** |
| Status | Opt in | **Default** |

The trade is explicit: the new regime gives lower rates in exchange for
giving up most deductions. And because it is the **default**, the deduction
disappears unless you actively choose the old regime.

So the tax-saving investment that was reflexive for a generation of Indian
investors now only helps if you've opted into the regime where it exists.

**Note on section numbers.** The Income-tax Act, 2025 renumbered almost
everything — what everyone called 80C is now a differently numbered provision.
The deduction and the ₹1.5 lakh cap carried over unchanged. This series
refers to it by what it does rather than by number, because the number is
the part that changed.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two mobile phone plans.

**Plan A** has a higher monthly price, but you can claim money back for lots
of things — your case, your screen protector, your headphones.

**Plan B** is cheaper every month, but you can't claim anything back.

Neither is automatically better. It depends entirely on how much stuff you
were actually going to claim. Someone who buys nothing is better off on Plan
B; someone who claims a lot might do better on Plan A.

The catch: if you don't choose, you're put on Plan B. And then keeping the
receipts achieves nothing at all.

</details>

## What ELSS actually is

**ELSS — Equity Linked Savings Scheme** — is an equity mutual fund with two
distinguishing features:

- Contributions qualify for the ₹1.5 lakh deduction **in the old regime**
- A **three-year lock-in** on every contribution

Two things about that lock-in are widely misunderstood.

**It's the shortest lock-in among the traditional tax-saving options** —
compare PPF at fifteen years, or tax-saving fixed deposits at five. That's a
genuine advantage of ELSS within its category.

**It applies per instalment, not per investment.** A monthly SIP into an ELSS
fund locks each instalment for three years from *its own* date. The
instalment made in month 36 is locked until month 72. People routinely expect
the whole holding to unlock three years after they started; it doesn't. This
is the same lot-by-lot logic as [FIFO]({% post_url 2026-12-28-sips-and-fifo %}), applied
to a lock-in instead of a holding period.

## And it's still an equity fund

Whichever regime you're in, ELSS gains are taxed exactly like any other
equity fund — covered in the
[equity post]({% post_url 2026-12-20-equity-and-equity-funds %}):

| | |
|---|---|
| Holding period | Always long-term on exit, since the lock-in exceeds {{ r.equity_holding_months }} months |
| Rate | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption |

The deduction reduces your taxable income when you invest. It does not make
the eventual gain tax-free. Both facts get run together constantly.

## Choosing a regime, briefly

This is a personal calculation and it genuinely varies. The shape of it:

- The old regime can win where you have **large, real deductions you'd have
  incurred anyway** — substantial home loan interest, significant insurance
  premiums, house rent allowance.
- The new regime tends to win where deductions would be **manufactured** —
  investments made only for the deduction, in products you wouldn't otherwise
  want.

That second point is the one worth internalising. A deduction is worth your
marginal rate — at 30%, ₹1.5 lakh deducted saves ₹45,000. That's real. But it
is *not* a reason to buy a product with poor returns or a fifteen-year
lock-in you didn't want. A bad investment with a tax break attached is
usually still a bad investment; the break is a one-off saving against a
commitment that runs for years.

The genuinely useful move is to check both regimes against your actual
numbers each year, rather than assuming the answer carries over. The tax
department publishes a calculator for exactly this.

## Common mistakes

- **Assuming the deduction is still available by default.** The new regime
  is the default and mostly doesn't have it.
- **Investing for a deduction you can't claim.** Buying ELSS in December
  while filing under the new regime achieves nothing tax-wise.
- **Thinking the ELSS lock-in runs from when you started.** Three years per
  instalment, each on its own clock.
- **Believing the deduction makes gains tax-free.** It reduces income now;
  the gains are taxed as equity later.
- **Choosing a regime once and never revisiting.** Your deductions change as
  loans are repaid and circumstances shift.
- **Letting the tax break choose the product.** A 30% saving once doesn't
  redeem fifteen years in something you didn't want.

**Takeaway:** The ₹1.5 lakh deduction still exists, but only in the old
regime — and since the new regime is the default, tax-saving investments now
help only if you've actively chosen the system where they count. ELSS remains
the shortest lock-in of the traditional options at three years per
instalment, and its gains are taxed like any other equity fund regardless of
which regime you file under.
