---
layout: post
title: "F&O is business income, not capital gains"
description: "Derivatives profits and losses are business income: a different return form, different set-off rules, and a turnover figure that isn't what you think. Worked on SEBI's average loss."
image: /assets/og/fo-is-business-income.png
date: 2026-12-16 09:00:00 +0530
series: tax
term: "Business income (F&O turnover)"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign f = t2.fno %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, verified against public
sources in {{ v.verified_on }}. Educational content, not tax advice.*

## A different head of income altogether

Everything in the tax series so far — holding periods, the {{ r.equity_ltcg_pct }}% rate, the
₹{% include inr.html n=r.ltcg_annual_exemption %} exemption, FIFO — belongs to **capital gains**. None of it applies
to futures and options.

Trading in **F&O — Futures and Options** — is treated as a **business**. Your
net result for the year is business income (or a business loss), taxed at
your slab rate along with your salary and everything else. That single
classification changes the return form you file, what you can deduct, what a
loss can be set against, and introduces a "turnover" concept that trips up
nearly everyone.

Specifically, F&O is *non-speculative* business income. That word matters:
**intraday equity trading** (buying and selling the same shares within a day
without delivery) is *speculative* business, with far harsher rules — its
losses can only be set against speculative gains and carry forward four
years. F&O losses are treated much more generously, as below.

Why this post follows the [F&O reality check]({% post_url 2026-11-05-what-the-fo-numbers-actually-say %})
is obvious once you look at the numbers there: most individuals who trade
derivatives lose money, and the *tax* treatment of that loss is the one part
of the outcome they can still do something about.

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
the accountants' body's guidance note — define it as:

```
F&O turnover = sum of the ABSOLUTE profit or loss on each closed trade
```

Not the contract value, not the margin, not the premium. A trade that made
₹60,000 adds ₹60,000; a trade that *lost* ₹95,000 also adds ₹95,000. The
premium received on options you sold is *not* added separately — it's already
inside the trade's profit or loss.

Turnover matters for one reason only: thresholds. It decides whether you need
a **tax audit** and whether you can use the **presumptive** scheme. It is not
your income and it is not taxed.

## Worked example: a trader with the average loss

Take a trader whose net result for the year equals the average individual
loss SEBI reported for FY26 — **₹{% include inr.html n=f.avg_loss %}** — made up of five
trades:

| Trade | Result | Adds to turnover |
|---|---:|---:|{% for t in f.trades %}
| {{ forloop.index }} | {% if t < 0 %}−₹{% assign ta = t | times: -1 %}{% include inr.html n=ta %}{% else %}+₹{% include inr.html n=t %}{% endif %} | ₹{% if t < 0 %}{% include inr.html n=ta %}{% else %}{% include inr.html n=t %}{% endif %} |{% endfor %}
| **Net result (business loss)** | **−₹{% include inr.html n=f.avg_loss %}** | |
| **Turnover** | | **₹{% include inr.html n=f.turnover %}** |

The audit threshold for a fully digital business — which F&O always is,
since nothing settles in cash — is **₹{% include inr.html n=f.audit_threshold %}** of turnover. Our
trader would need to repeat this year's activity about {{ f.trades_to_reach_audit_threshold }} times over to
reach it. For most individuals the turnover-based audit rule simply never
binds; what does bind is the presumptive-scheme trap below.

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

Two conditions, both absolute:

1. **File ITR-3.** Business income needs the business return form, not the
   ITR-2 you'd use for capital gains alone. Salary plus F&O means ITR-3.
2. **File it by the due date.** A loss reported in a late return cannot be
   carried forward. The set-off in the same year survives; the
   ₹{% include inr.html n=f.carried_forward %} for future years is lost.

## The presumptive trap

There is a simplified scheme for small businesses: declare **{{ f.presumptive_rate_pct }}% of your
digital turnover** as profit, skip the books, skip the audit. It's available
up to ₹{% include inr.html n=f.presumptive_turnover_limit %} of turnover.

It sounds convenient. For a losing trader it's a trap:

| | Actual result | Presumptive |
|---|---:|---:|
| Turnover | ₹{% include inr.html n=f.turnover %} | ₹{% include inr.html n=f.turnover %} |
| Income declared | −₹{% include inr.html n=f.avg_loss %} (loss) | +₹{% include inr.html n=f.presumptive_deemed_profit %} ({{ f.presumptive_rate_pct }}% deemed profit) |
| Tax at 30% + cess | ₹0 | ₹{% include inr.html n=f.presumptive_tax_with_cess %} |
| Loss available for set-off / carry-forward | ₹{% include inr.html n=f.avg_loss %} | none |

The scheme cannot declare a loss. Opting in means paying tax on a profit you
didn't make and forfeiting a loss you did. And opting *out* within five years
of opting in locks you out for the next five and, if your total income is
above the basic exemption, makes an audit compulsory in the exit year.

The flip side is the good news: if you have **never** used the presumptive
scheme, you can report an F&O loss without an audit as long as turnover is
under the threshold. You do need to keep books — a broker's P&L statement
and ledger are the core of them.

## What you can deduct

Because it's a business, the costs of running it reduce the income (or
deepen the loss): brokerage, exchange and clearing charges, **STT (Securities
Transaction Tax)**, stamp duty, GST on brokerage, charting and analytics
subscriptions, data feeds, internet, depreciation on a laptop used for
trading, and fees to a SEBI-registered adviser. Keep invoices. None of this is
available against capital gains, which is one of the few respects in which
the business classification helps.

Worth knowing: STT on futures and options sales rose from 1 April 2026 (one
source reports futures from 0.02% to 0.05% of traded price and options
premium from 0.10% to 0.15%). It's a deductible cost, and it's also the
"house's cut" the [F&O post]({% post_url 2026-11-05-what-the-fo-numbers-actually-say %}) described —
paid on every trade, win or lose.

## Common mistakes

- **Reporting F&O under capital gains.** Wrong head, wrong form, and the
  loss rules you're relying on don't exist there.
- **Filing late and expecting to carry the loss forward.** The carry-forward
  dies with the deadline.
- **Setting the loss against salary.** Not permitted. Interest, rent,
  capital gains and other business income, yes; salary, never.
- **Computing turnover from contract values.** It's the sum of absolute
  profits and losses. Contract-value turnover would push nearly everyone
  over the audit threshold; the correct method pushes almost nobody.
- **Opting for presumptive tax "to keep it simple".** For a loss year it
  converts a deductible loss into a taxable phantom profit and locks you in.
- **Ignoring intraday equity.** It's a separate, *speculative* business with
  its own, much tighter, loss rules. Don't net it against F&O.
- **Not keeping the broker's tax P&L.** It's the book of accounts you'll be
  asked for, and the source for every figure above.

**Takeaway:** F&O results are business income at your slab, not capital
gains — so they go in ITR-3, losses can offset interest and gains but never
salary, and a loss carries forward eight years only if you file on time.
"Turnover" is the sum of every trade's absolute result, which is why the
audit threshold rarely binds; the presumptive scheme, which can't declare a
loss, is the trap to avoid.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists every source these rules were checked against, and the points a
professional should confirm before you rely on them.*
