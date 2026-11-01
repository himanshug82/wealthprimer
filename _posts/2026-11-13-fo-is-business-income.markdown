---
layout: post
title: "F&O taxation in India: business income, not capital gains"
description: "F&O profits and losses are business income: a different return form, different set-off rules, and a turnover that isn't what you think. On SEBI's data."
image: /assets/og/fo-is-business-income.png
date: 2026-11-13 09:00:00 +0530
series: tax
term: "Business income (F&O turnover)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "September 2026"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign f = t2.fno %}
{% assign r = site.data.tax.rates %}
{% assign sebi = site.data.fno.sources.fy25_fy26_study %}

## A different head of income altogether

This post describes the rules for Tax Year 2026-27 (FY 2026-27, April 2026 to March 2027), as at September 2026. Its examples use illustrative figures, and its tax amounts assume a 30% marginal rate: that is the old regime's rate at the example salary. Under the new regime the marginal rate at that salary is lower, so the tax figures would be smaller. The mechanics are the same.

Everything in the tax series so far — holding periods, the {{ r.equity_ltcg_pct }}% rate, the
₹{% include inr.html n=r.ltcg_annual_exemption %} exemption, FIFO (first in, first out) — belongs to **capital gains**. None of it applies
to futures and options.

Trading in **F&O — futures and options** — is treated as a **business**. Your
net result for the year is business income (or a business loss), taxed at
your slab rate along with your salary and everything else. That single
classification changes the return form you file, what you can deduct, what a
loss can be set against, and introduces a "turnover" concept that trips up
nearly everyone.

Specifically, F&O is *non-speculative* business income. That word matters:
**intraday equity trading** (buying and selling the same shares within a day
without delivery) is *speculative* business, with narrower set-off rules — as
generally understood, its losses can be set only against speculative gains and carry forward four
years (not confirmed in a primary source here; check the current rule). F&O losses have wider set-off, as below.

Why this post follows the [F&O reality check]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %})
follows from the numbers there: SEBI's data show most individuals who trade
derivatives lose money, and this post describes how that loss is treated for tax.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Selling your old bike for more than you paid is one kind of money — a
"gain". Running a lemonade stand is another kind — a "business", where you
add up everything you made, subtract everything you spent, and the result is
your profit or loss for the summer.

The tax people say F&O trading is a lemonade stand, not a bike sale. So you
use the lemonade-stand rules: keep receipts, add up all the days, and if the
stand lost money you may be allowed to subtract that loss from other things
you earned — but not from your pocket money (salary).

</details>

## Turnover is not what you traded

For a business, "turnover" usually means sales. For F&O the tax rules — via
the guidance note on tax audits from ICAI (the Institute of Chartered
Accountants of India), as summarised in secondary sources — define it as (check the Guidance Note itself, which this post has not opened):

```
F&O turnover = sum of the ABSOLUTE profit or loss on each closed trade
```

Not the contract value, not the margin, not the premium. A trade that made
₹60,000 adds ₹60,000; a trade that *lost* ₹95,000 also adds ₹95,000. On the secondary sources read, the
premium received on options you sold is not added separately; it is already
inside the trade's profit or loss. Check the Guidance Note on this point.

Turnover matters for one reason only: thresholds. It decides whether you need
a **tax audit** and whether you can use the **presumptive** scheme. It is not
your income and it is not taxed.

## Worked example: a trader with the average loss

Take a trader whose net result for the year equals the average individual
loss SEBI (the Securities and Exchange Board of India) reported for FY 2025-26 (a research statistic, not a worked-example price, so the 3-month lag does not apply) —
**₹{% include inr.html n=f.avg_loss %}**, from its
[study of individual traders' profitability]({{ sebi.url }}) published
{{ sebi.date }} — made up of five trades:

| Trade | Result | Adds to turnover |
|---|---:|---:|{% for t in f.trades %}
| {{ forloop.index }} | {% if t < 0 %}−₹{% assign ta = t | times: -1 %}{% include inr.html n=ta %}{% else %}+₹{% include inr.html n=t %}{% endif %} | ₹{% if t < 0 %}{% include inr.html n=ta %}{% else %}{% include inr.html n=t %}{% endif %} |{% endfor %}
| **Net result (business loss)** | **−₹{% include inr.html n=f.avg_loss %}** | |
| **Turnover** | | **₹{% include inr.html n=f.turnover %}** |

The audit threshold for a business with almost all receipts and payments digital — which F&O typically
is, since nothing settles in cash — is **₹{% include inr.html n=f.audit_threshold %}** of turnover (Income-tax Act, 2025, as read in the ICAI copy; the cash-share condition is tested over the whole business). Our
trader would need to repeat this year's activity about {{ f.trades_to_reach_audit_threshold }} times over to
reach it. For a trader with these numbers the turnover-based audit rule does not bind; the presumptive scheme below works differently.

## What the loss can and cannot offset

Suppose the same trader has a salary of ₹{% include inr.html n=f.salary %}, bank interest of
₹{% include inr.html n=f.interest_income %} and a short-term capital gain of ₹{% include inr.html n=f.stcg %} from
selling some shares.

A non-speculative business loss can be set off in the same year against
**any head of income except salary**:

| | Available | Set off | Remaining loss |
|---|---:|---:|---:|
| Salary | ₹{% include inr.html n=f.salary %} | **not allowed** | ₹{% include inr.html n=f.avg_loss %} |
| Interest (other sources) | ₹{% include inr.html n=f.interest_income %} | ₹{% include inr.html n=f.setoff_against_interest %} | ₹{% assign rem1 = f.avg_loss | minus: f.setoff_against_interest %}{% include inr.html n=rem1 %} |
| Short-term capital gain | ₹{% include inr.html n=f.stcg %} | ₹{% include inr.html n=f.setoff_against_stcg %} | ₹{% include inr.html n=f.carried_forward %} |

Tax saved this year by the set-off, at a 30% slab on the interest and
{{ r.equity_stcg_pct }}% on the gain, with cess: **₹{% include inr.html n=f.tax_saved_by_setoff_with_cess %}**. The remaining
₹{% include inr.html n=f.carried_forward %} carries forward for **{{ f.carry_forward_years }} years** — but from next year it
can only be set against *business* income (including future F&O profits),
not against interest or capital gains.

Two conditions apply:

1. **The return form.** Business income needs the business return form (ITR
   stands for income tax return; ITR-3 under the forms in use at the time of writing), not the ITR-2 used for capital gains
   alone. Check the current form names.
2. **The due date.** In the Income-tax Act, 2025, a loss generally can be carried forward only if the return is filed by the due date. The set-off in the same year survives; the
   ₹{% include inr.html n=f.carried_forward %} for future years would not carry forward. Check the current rule for your type of loss.

One more consequence of having business income: the rules on switching between the old and new regimes differ from those for a salaried filer. Check the current rule (the [ELSS post]({% post_url 2026-11-09-elss-and-the-deduction-that-moved %}) describes the two regimes).

## The presumptive scheme

There is a simplified scheme for small businesses: declare **{{ f.presumptive_rate_pct }}% of your
digital turnover** as profit, skip the books, skip the audit. It's available
up to ₹{% include inr.html n=f.presumptive_turnover_limit %} of turnover.

Here is how it compares for a trader with a loss:

| | Actual result | Presumptive |
|---|---:|---:|
| Turnover | ₹{% include inr.html n=f.turnover %} | ₹{% include inr.html n=f.turnover %} |
| Income declared | −₹{% include inr.html n=f.avg_loss %} (loss) | +₹{% include inr.html n=f.presumptive_deemed_profit %} ({{ f.presumptive_rate_pct }}% deemed profit) |
| Tax at 30% + cess | ₹0 | ₹{% include inr.html n=f.presumptive_tax_with_cess %} |
| Loss available for set-off / carry-forward | ₹{% include inr.html n=f.avg_loss %} | none |

The scheme deems a profit; it does not allow a loss to be declared. Under it, tax is computed on the deemed profit and the actual loss is not
carried forward. The conditions for leaving the scheme (the audit and lock-out rules for opting out within five years) are described in secondary sources only; check the current rule.

Without the scheme, a trader whose turnover is under the audit threshold can report the actual loss,
subject to keeping books of account; a broker's P&L statement and ledger are the core of them.

## What you can deduct

Because it's a business, the costs of running it reduce the income (or
deepen the loss): brokerage, exchange and clearing charges, **STT (securities
transaction tax)**, stamp duty, GST on brokerage, charting and analytics
subscriptions, data feeds, internet, depreciation on a laptop used for
trading. Whether fees to a SEBI-registered adviser are deductible is arguable; this post does not say. Keep invoices. None of this is
available against capital gains, which is one of the few respects in which
the business classification helps.

Worth knowing: the Finance Bill 2026 memorandum (indiabudget.gov.in) proposed raising STT from 1 April 2026 — futures from 0.02% to 0.05% of the traded price, and
options premium from 0.1% to 0.15%. (This post has not opened the enacted Finance Act.) STT is a cost of trading, and it's also the
"house's cut" the [F&O post]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}) described —
paid on every trade, win or lose.

## Common mistakes

- **Reporting F&O under capital gains.** Wrong head, wrong form, and the
  loss rules above don't exist there.
- **Setting the loss against salary.** Not permitted. Interest, rent,
  capital gains and other business income, yes; salary, never.
- **Computing turnover from contract values.** On the secondary sources read, it's the sum of absolute
  profits and losses, not contract value.
- **Netting intraday equity against F&O.** Intraday equity is a separate, *speculative* business with
  its own loss rules.

**Takeaway:** F&O results are business income at your slab, not capital
gains. Losses can offset interest and gains but never
salary, and carry forward eight years if the return is filed on time. On the sources read, "turnover" is the sum of every trade's absolute result, and the presumptive scheme, which deems a profit, cannot declare a loss.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists the sources these rules were checked against; most are secondary sources, and no professional has reviewed this post.*
