---
layout: post
title: "Equity and equity funds: 20%, 12.5%, and the ₹1.25 lakh that isn't taxed"
description: "Listed shares and equity funds: the short-term and long-term rates, the annual exemption, cess and grandfathering, with worked examples on real fund NAVs."
image: /assets/og/equity-and-equity-funds.png
date: 2026-10-29 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}
{% assign a = t.example_lumpsum %}
{% assign g = t.example_grandfathering %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## The rules in full

These rules cover listed shares and equity mutual funds — the assets most
retail investors actually hold — where securities transaction tax (STT) was paid on the sale.
That's automatic on any sale through a stock exchange and on an equity-fund
redemption. For long-term gains on shares, STT on the purchase is needed too,
with notified exceptions such as shares allotted in an IPO (initial public
offering). Short-term capital gains (STCG) and long-term capital gains (LTCG)
split at the line explained in the
[holding-period post]({% post_url 2026-10-28-short-term-vs-long-term %}):

```
Held {{ r.equity_holding_months }} months or less   ->  STCG at {{ r.equity_stcg_pct }}%
Held more than {{ r.equity_holding_months }} months  ->  LTCG at {{ r.equity_ltcg_pct }}%, but the first
                              Rs {{ r.ltcg_annual_exemption }} of long-term gains
                              each financial year is exempt

Plus {{ r.cess_pct }}% health and education cess, applied on the TAX.
```

Three features of that exemption are worth stating precisely, because each is
routinely misunderstood.

**It's per financial year, not per transaction.** ₹{% include inr.html n=r.ltcg_annual_exemption %} across everything you
sell in the year, not per fund and not per sale.

**It's per person.** Two adults each get their own.

**It doesn't carry forward.** Unused, it's gone on 31 March. This is the
entire basis of the harvesting idea in
the losses post later in this series.

## Worked example: a real gain, and real tax

Using the fund NAV (net asset value, the per-unit price) history from the
[Mutual Funds series]({% post_url 2026-10-18-what-a-mutual-fund-is %}) — UTI Nifty 50 Index Fund (regular
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

A gain of about ₹9.2 lakh, tax of about ₹1.03 lakh — an effective rate of
roughly 11% on the whole gain, because the exemption absorbs the first
₹1.25 lakh and the cess adds a little back.

Note what the effective rate is *not*: it isn't 12.5%, and it isn't 13%. The
exemption means the effective rate rises toward 13% as the gain grows and is
zero for small gains. Quoting "LTCG is 12.5%" as though it were a flat charge
overstates the tax on modest gains considerably.

## Two quirks if your income is modest

Both apply to resident individuals, and both are easy to miss.

**Unused basic exemption can absorb these gains.** If your other income is
below the basic exemption limit (the slab that's taxed at zero), the unused
part can be set against short-term and long-term equity gains before the
{{ r.equity_stcg_pct }}% or {{ r.equity_ltcg_pct }}% applies. A student or a retiree with little other income can
owe less than the headline rate suggests.

**The new-regime rebate doesn't cover them.** The new regime's rebate — up to
₹60,000, for income up to ₹12 lakh, from FY 2025-26 — can't be used against
tax on these special-rate gains; the Finance Act 2025 made that explicit after
disputes over earlier years. So someone under ₹12 lakh can owe nothing on
salary and still owe tax on an equity gain. How the ₹12 lakh limit itself
counts such gains has been argued over; check the current rules, or a
professional, if you're near it.

## Grandfathering: the 31 January 2018 rule

Long-term gains on listed equity were entirely tax-free until 2018. When the
tax was introduced, gains accrued *before* it existed were protected — and
that protection still applies to anything you've held since.

The rule, for equity acquired on or before **31 January 2018**:

```
Cost for tax purposes = the HIGHER of
                          (a) what you actually paid, and
                          (b) the LOWER of
                                - the value on 31 January 2018, and
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

₹{% include inr.html n=g.gain_excluded %} of gain simply doesn't count, because it accrued before the tax
existed. On this example that's worth roughly ₹9,300 in tax.

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

Brokerage, exchange fees and GST on them are part of your cost of
acquisition or reduce your sale proceeds, so they reduce the gain.

**STT is the exception** — it is specifically
not allowed as a deduction when computing capital gains. You pay it, and you
can't net it off. Worth knowing because broker statements list it alongside
charges that *are* deductible.

## Common mistakes

- **Thinking the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption applies per fund or per sale.** It's one
  allowance per person per financial year, across all equity long-term gains.
- **Expecting the exemption to carry forward.** It expires on 31 March.
- **Quoting {{ r.equity_ltcg_pct }}% as the effective rate.** With the exemption and the cess,
  the effective rate is lower on small gains and approaches 13% on large ones.
- **Forgetting grandfathering on old holdings.** On anything bought before
  February 2018, using actual cost overstates the gain, sometimes by a lot.
- **Deducting STT.** Deductible costs yes; STT no.
- **Assuming the fund withholds the tax.** For residents it generally
  doesn't. The full redemption arrives and the liability is yours to settle.

**Takeaway:** Equity and equity funds are taxed at {{ r.equity_stcg_pct }}% short-term and {{ r.equity_ltcg_pct }}%
long-term, with the first ₹{% include inr.html n=r.ltcg_annual_exemption %} of long-term gains each year exempt — an
allowance that is per person, per year, and gone if unused. On anything held
since before February 2018, check the grandfathered cost before computing
the gain: on the example here it excluded ₹{% include inr.html n=g.gain_excluded %} that would otherwise have
been taxed.
