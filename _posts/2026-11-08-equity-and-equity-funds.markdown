---
layout: post
title: "Capital gains tax on shares and equity funds: LTCG and STCG"
description: "Listed shares and equity funds: the short-term and long-term rates, the annual exemption, cess and grandfathering, with worked examples on real fund NAVs."
image: /assets/og/equity-and-equity-funds.png
date: 2026-11-08 09:00:00 +0530
series: tax
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign a = t.example_lumpsum %}
{% assign g = t.example_grandfathering %}

## The rules in full, Tax Year 2026-27

This post covers **Tax Year 2026-27 (FY 2026-27)**; FY is *financial year*. These rules cover listed shares and equity mutual funds — the assets most
retail investors actually hold — where securities transaction tax (STT) was paid on the sale.
As we understand it, that is automatic on any sale through a stock exchange and on an equity-fund
redemption. For long-term gains on shares, section 198 of the Act also requires STT on the purchase,
with exceptions the government can notify. Short-term capital gains (STCG) and long-term capital gains (LTCG)
split at the line explained in the
[holding-period post]({% post_url 2026-11-04-short-term-vs-long-term %}):

```
Held {{ r.equity_holding_months }} months or less   ->  STCG at {{ r.equity_stcg_pct }}%
Held more than {{ r.equity_holding_months }} months  ->  LTCG at {{ r.equity_ltcg_pct }}%, but the first
                              Rs {% include inr.html n=r.ltcg_annual_exemption %} of long-term gains
                              each financial year is exempt

Plus {{ r.cess_pct }}% health and education cess, applied on the TAX.
```

Surcharge is excluded throughout this post; it applies at high incomes and can change the answer (it is capped at 15% on these gains). The rates and the exemption are in sections 196 and 198 of the Income-tax Act, 2025.

Three features of that exemption are worth stating precisely, because each is
routinely misunderstood.

**It's per financial year, not per transaction.** ₹{% include inr.html n=r.ltcg_annual_exemption %} across everything you
sell in the year, not per fund and not per sale.

**It's per person.** Two adults each get their own.

**It doesn't carry forward.** Unused, it's gone on 31 March. The losses post in this series looks at what that means for a sale and repurchase.

## Worked example: a real gain, and real tax

Using the fund NAV (net asset value, the per-unit price) history from the
[Mutual Funds series]({% post_url 2026-09-25-what-a-mutual-fund-is %}) — UTI Nifty 50 Index Fund (regular
plan, growth), NAVs from AMFI (the Association of Mutual Funds in India), as
of 31 March 2026, used for illustration only — a ₹{% include inr.html n=a.invested %} investment held
comfortably past the long-term line:

| | |
|---|---:|
| Bought {{ a.buy_date | date: "%-d %B %Y" }} at NAV | ₹{% include inr.html n=a.buy_nav %} |
| Units | {{ a.units }} |
| Sold {{ a.sell_date | date: "%-d %B %Y" }} at NAV | ₹{% include inr.html n=a.sell_nav %} |
| Sale value | ₹{% include inr.html n=a.value %} |
| Cost | ₹{% include inr.html n=a.invested %} |
| **Gain** | **₹{% include inr.html n=a.gain %}** |
| Holding period | {% include inr.html n=a.holding_days %} days — long-term |
| Less: annual exemption | ₹{% include inr.html n=a.exempt %} |
| **Taxable** | **₹{% include inr.html n=a.taxable %}** |
| Tax at {{ r.equity_ltcg_pct }}% | ₹{% include inr.html n=a.tax_before_cess %} |
| **Tax including {{ r.cess_pct }}% cess** | **₹{% include inr.html n=a.tax_with_cess %}** |

A gain of ₹{% include inr.html n=a.gain %}, tax of ₹{% include inr.html n=a.tax_with_cess %} — an effective rate of
{{ a.tax_with_cess | times: 100.0 | divided_by: a.gain | round: 1 }}% on the whole gain, because the exemption absorbs the first
₹{% include inr.html n=r.ltcg_annual_exemption %} and the cess adds a little back. (The figures are computed from unrounded numbers; recomputing from the rounded ₹{% include inr.html n=a.tax_before_cess %} gives a figure one rupee different.)

The buy date in this example (April 2020) sits near the March 2020 market low,
so the gain is larger than a typical holding would show. It was picked so that
tax is actually payable, to show the mechanics.

Note what the effective rate is *not*: it isn't 12.5%, and it isn't 13%. The
exemption means the effective rate rises toward 13% as the gain grows and is
zero for small gains. Quoting "LTCG is 12.5%" as though it were a flat charge
overstates the tax on modest gains considerably.

## Two quirks if your income is modest

Both are easy to miss.

**Unused basic exemption can absorb these gains**, for a resident individual or HUF (Hindu undivided family), under sections 196(2) and 198(3) of the Act. If your other income is
below the basic exemption limit (the slab that's taxed at zero), the unused
part can be set against equity gains before the
{{ r.equity_stcg_pct }}% or {{ r.equity_ltcg_pct }}% applies. Someone with little other income can
owe less than the headline rate suggests.

**The new-regime rebate doesn't cover long-term gains.** The new regime's rebate — up to
₹60,000, for income up to ₹12 lakh (section 156 of the Act) — is not allowed against
the tax on these long-term gains (section 198(7)). For short-term gains there is no equally direct line, but section 156(3) limits the rebate to tax at the new regime's slab rates, which as we read it leaves the special-rate tax out too. So someone under ₹12 lakh can owe nothing on
salary and still owe tax on a long-term equity gain. How the ₹12 lakh limit itself
counts such gains is not covered here.

## Grandfathering: the 31 January 2018 rule

As commonly described, long-term gains on listed equity were tax-free until 2018 and a tax was then introduced, with gains accrued *before* the cut-off date protected; we have not checked that history against a source, so check the current rule. The protection is described as applying to anything held since.

The rule, for equity acquired before **1 February 2018** (section 90(7) of the Act). For a listed share, fair market value means the highest price quoted that day; for an unlisted fund unit, the NAV (net asset value):

```
Cost for tax purposes = the HIGHER of
                          (a) what you actually paid, and
                          (b) the LOWER of
                                - the fair market value on 31 January 2018, and
                                - the sale price
```

Worked through, on the same fund:

| | |
|---|---:|
| Bought {{ g.buy_date | date: "%-d %B %Y" }}, invested | ₹{% include inr.html n=g.invested %} |
| Units | {{ g.units }} |
| Value on {{ g.fmv_date | date: "%-d %B %Y" }} | ₹{% include inr.html n=g.fmv_value %} |
| Sold {{ g.sell_date | date: "%-d %B %Y" }} for | ₹{% include inr.html n=g.sale_value %} |
| Higher of cost and 31-Jan-2018 value | ₹{% include inr.html n=g.grandfathered_cost %} |
| **Gain, with grandfathering** | **₹{% include inr.html n=g.gain_with_grandfathering %}** |
| Gain, without it | ₹{% include inr.html n=g.gain_without %} |
| **Gain excluded from tax** | **₹{% include inr.html n=g.gain_excluded %}** |

₹{% include inr.html n=g.gain_excluded %} of gain doesn't count, because it accrued before the tax
existed. {% assign ge = g.gain_excluded | times: r.equity_ltcg_pct | divided_by: 100.0 | times: 1.04 | round %}Taxed at {{ r.equity_ltcg_pct }}% plus cess, with the exemption already used elsewhere, it would have cost about ₹{% include inr.html n=ge %}.

The cap matters too, and it applies only to the 31 January 2018 leg: if the
asset is now worth *less* than its 31 January 2018 value, that value is
capped at the sale price, so grandfathering can't manufacture an artificial
loss. But if your actual cost is above the sale price, you still get your real
loss — the cap never pushes your actual cost down.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine your school announces that from next Monday, anyone who grows taller
will owe a "tall tax" on the extra centimetres.

That would be unfair to people who were already tall — they grew before
anyone said anything. So the school measures everyone on Sunday and only
counts growth *after* that.

31 January 2018 was the measuring day for Indian shares. Anything you'd
already gained by then doesn't count. Only growth after that day is taxed.

</details>

## What about buying and selling costs?

The Act lets you deduct expenditure "wholly and exclusively" connected with the sale (section 72(1)). Brokerage is the usual example. The Act doesn't list items, so how far that reaches for exchange fees and GST (goods and services tax) on them is a reading, not a stated rule.

**STT is the exception** — section 72(3) of the Income-tax Act, 2025 does not allow it as a deduction when computing capital gains. You pay it, and you
can't net it off. Worth knowing because broker statements list it alongside
other charges.

## Common mistakes

- **Thinking the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption applies per fund or per sale.** It's one
  allowance per person per financial year, across all equity long-term gains.
- **Expecting the exemption to carry forward.** It expires on 31 March.
- **Quoting {{ r.equity_ltcg_pct }}% as the effective rate.** With the exemption and the cess,
  the effective rate is lower on small gains and approaches 13% on large ones.
- **Forgetting grandfathering on old holdings.** On anything bought before
  February 2018, using actual cost can overstate the gain.
- **Deducting STT.** The Act does not allow STT as a deduction.

## Sources

- [Income-tax Act, 2025 (a copy hosted by the Institute of Chartered Accountants of India, ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself, as read in that copy. Points not found there are marked "check the current rule".
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the amendments and the rates for Tax Year 2026-27.

**Takeaway:** Equity and equity funds are taxed at {{ r.equity_stcg_pct }}% short-term and {{ r.equity_ltcg_pct }}% long-term, with the first ₹{% include inr.html n=r.ltcg_annual_exemption %} of long-term gains each year exempt. The allowance is per person, per year, and expires unused. For holdings bought before February 2018, the grandfathered cost can change the gain.
