---
layout: post
title: "F&O taxation in India: business income, not capital gains"
description: "F&O profits and losses are business income: a different return form, different set-off rules, and a turnover that isn't what you think. On SEBI's data."
image: /assets/og/fo-is-business-income.png
date: 2026-11-26 09:00:00 +0530
series: tax
term: "Business income (F&O turnover)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign f = t2.fno %}
{% assign r = site.data.tax.rates %}
{% assign sebi = site.data.fno.sources.fy25_fy26_study %}

## A different head of income altogether, Tax Year 2026-27

This post describes the rules for Tax Year 2026-27 (FY 2026-27, April 2026 to March 2027), as at November 2026. The rules are as read in the Income-tax Act, 2025 and the Finance Act, 2026. Its examples use illustrative figures, and its tax amounts assume a 30% marginal rate. That 30% is the old regime's top slab, which starts above ₹10 lakh (Finance Act, 2026, First Schedule, Part I-B). The new-regime slab table in section 202 of the Act gives lower rates at the salary used below, so under the new regime the tax figures would be smaller. The mechanics are the same.

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
without delivery) is *speculative* business, with narrower set-off rules — its
losses can be set only against speculative gains and carry forward four
years (Income-tax Act, 2025, section 113). F&O losses have wider set-off, as below.

This post picks up where the [F&O reality check]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %})
left off. SEBI's data in that post show most individuals who trade
derivatives lose money; here we describe how such a loss is treated for tax.

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

Not the contract value and not the margin. A trade that made
₹60,000 adds ₹60,000; a trade that *lost* ₹95,000 also adds ₹95,000. How option premium is treated in this sum (whether premium received on options you sold is counted, and how) is something this post has not confirmed: the Guidance Note was not opened. Check the Guidance Note on this point before relying on any turnover figure.

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
is, since nothing settles in cash — is **₹{% include inr.html n=f.audit_threshold %}** of turnover (section 63 of the Income-tax Act, 2025; cash must be no more than 5% of both receipts and payments, otherwise the limit is ₹1 crore). Our
trader would need to repeat this year's activity about {{ f.trades_to_reach_audit_threshold }} times over to
reach it. On turnover alone, a trader with these numbers is far from the threshold. That is not the whole audit question: the presumptive scheme below has its own audit condition, which can apply to a trader who declares less than the deemed profit.

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
{{ r.equity_stcg_pct }}% on the gain, with cess: **₹{% include inr.html n=f.tax_saved_by_setoff_with_cess %}**. This is the saving if the loss is reported as an actual loss. Whether doing so would also require a tax audit for a trader like this one is covered in the presumptive section below, and it is not netted off here. The remaining
₹{% include inr.html n=f.carried_forward %} carries forward for **{{ f.carry_forward_years }} years** — but from next year it
can only be set against *business* income (including future F&O profits),
not against interest or capital gains.

Two conditions apply:

1. **The return form.** Business income needs the business return form (ITR
   stands for income tax return; ITR-3 under the forms in use at the time of writing), not the ITR-2 used for capital gains (ITR-4 may be available under the presumptive scheme; check)
   alone. Check the current form names.
2. **The due date.** Under section 121 of the Income-tax Act, 2025, a business loss can be carried forward only if it was determined on a return filed under section 263(1), which sets the due date. The set-off in the same year survives; the
   ₹{% include inr.html n=f.carried_forward %} for future years would not carry forward.

One more consequence of having business income: the rules on switching regimes differ. Under section 202(4), someone with business income opts out of the new regime by the due date; that choice carries forward, can be withdrawn only once, and after that the option is gone unless the business income ends. A person without business income chooses year by year with the return (the [ELSS post]({% post_url 2026-11-22-elss-and-the-deduction-that-moved %}) describes the two regimes).

## The presumptive scheme

There is a simplified scheme for small businesses: declare **{{ f.presumptive_rate_pct }}% of your
digital turnover** as profit, with fewer books and no audit if the conditions are met. Section 58 of the Act sets it at 6% of turnover received digitally and 8% of the rest, or the actual profit if higher. It's for resident individuals, HUFs (Hindu undivided families) and firms other than LLPs (limited liability partnerships), within limits of ₹2 crore of turnover, or ₹{% include inr.html n=f.presumptive_turnover_limit %} if cash receipts are no more than 5%. Check the definition of an eligible assessee if your case is unusual.

Here is how it compares for a trader with a loss, at the assumed 30% rate described at the top (an illustrative old-regime rate). The table shows the tax on the F&O result alone; it does not include the tax the loss would save through set-off, which is calculated in the section above:

| | Actual result | Presumptive |
|---|---:|---:|
| Turnover | ₹{% include inr.html n=f.turnover %} | ₹{% include inr.html n=f.turnover %} |
| Income declared | −₹{% include inr.html n=f.avg_loss %} (loss) | +₹{% include inr.html n=f.presumptive_deemed_profit %} ({{ f.presumptive_rate_pct }}% deemed profit) |
| Tax on the F&O result at 30% + cess | ₹0 (a loss); a tax audit may apply, see below | ₹{% include inr.html n=f.presumptive_tax_with_cess %} |
| Loss available for set-off / carry-forward | ₹{% include inr.html n=f.avg_loss %} | none |

The scheme deems a profit; it does not allow a loss to be declared. Under it, tax is computed on the deemed profit and the actual loss is not
carried forward. Leaving the scheme has a cost: under section 58(7) and (8), someone who uses it and then declares otherwise in any of the next five years can't return for five years, and needs books and an audit if total income is above the basic exemption.

Outside the scheme, a trader whose turnover is under the audit threshold can generally report the actual result,
subject to keeping books of account (a broker's P&L statement and ledger are the core of them) and to the audit condition in the next sentence. Declaring less than the deemed profit when total income is above the basic exemption brings a requirement to keep books and get audited, under section 58(3) of the Act, for someone eligible for the scheme. On that reading, a trader like the one in this example, who reports a loss and has a salary, would need an audit even though turnover is far below the threshold, if eligible.

## What you can deduct

Because it's a business, the costs of running it can reduce the income (or
deepen the loss). The list below is as generally described in secondary sources, not
checked against the Act; check the current rule: brokerage, exchange and clearing charges, **STT (securities
transaction tax)**, stamp duty, GST (goods and services tax) on brokerage, charting and analytics
subscriptions, data feeds, internet, depreciation on a laptop used for
trading. Whether any other cost is deductible, such as fees to an adviser, is not covered here. None of this is
available against capital gains, which is one of the few respects in which
the business classification helps.

Worth knowing: section 159 of the Finance Act, 2026 raised STT — futures from 0.02% to 0.05% of the traded price, and
options premium from 0.1% to 0.15%, and from 0.125% to 0.15% on the sale of an option that is exercised (the section gives rates, not the base for that last one). STT is a cost of trading, and it's also the
"house's cut" the [F&O post]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}) described —
paid on each sale, win or lose.

## Common mistakes

- **Reporting F&O under capital gains.** Wrong head, wrong form, and the
  loss rules above don't exist there.
- **Setting the loss against salary.** Not permitted. Interest, rent,
  capital gains and other business income, yes; salary, never.
- **Computing turnover from contract values.** On the secondary sources read, it's built from the absolute profits and losses of closed trades, not contract value (how option premium enters is unconfirmed).
- **Netting intraday equity against F&O.** Intraday equity is a separate, *speculative* business with
  its own loss rules.

**Takeaway:** F&O results are business income at your slab, not capital
gains. Losses can offset interest and gains but never
salary, and generally carry forward eight years if the return is filed on time (a loss return may also carry an audit requirement; see above). On the sources read, "turnover" is built from every trade's absolute result, and the presumptive scheme, which deems a profit, cannot declare a loss.

## Sources

- Income-tax Act, 2025 ([ICAI copy of the Gazette text](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf)): audit threshold and presumptive scheme (sections 63 and 58), set-off and carry-forward of business losses (sections 109, 112, 121), speculation loss (section 113), the new regime and opting out (section 202).
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: STT rates (section 159) and the old-regime slabs (First Schedule, Part I-B). Opened 2 November 2026.
- SEBI study on individual traders' profitability (linked above): the average loss used in the example.
- Not opened: the ICAI Guidance Note on tax audit (the turnover definition), and the list of deductible costs (secondary sources in the module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)).

