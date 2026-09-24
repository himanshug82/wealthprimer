---
layout: post
title: "REITs and InvITs: one payout, three tax treatments"
description: "A REIT or InvIT payout arrives as one credit but splits into interest, dividend and capital repayment, each taxed differently. Plus capital gains on the units."
image: /assets/og/reits-and-invits.png
date: 2026-11-09 09:00:00 +0530
series: tax
term: "REIT and InvIT taxation"
---

{% assign t3 = site.data.tax3 %}
{% assign v = t3.verification %}
{% assign x = t3.reit %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, checked against the
text of the Income-tax Act, 2025 and the Finance Act, 2026 in {{ v.verified_on }}.
Educational content, not tax advice.*

## A payout that isn't one thing

A **REIT — real estate investment trust** — owns rent-earning property such as
office parks and malls. An **InvIT — infrastructure investment trust** — owns
things like toll roads and power lines. Both are registered with SEBI (the
Securities and Exchange Board of India), and the tax law calls both
**business trusts**. This post is about units listed on the stock exchanges.

Most of their assets usually sit inside companies the trust owns, called
**SPVs — special purpose vehicles**. Money reaches you in two hops: the SPV pays
the trust, and the trust pays you. How the SPV paid the trust decides how you
are taxed.

That's the whole idea behind this post. The Act says a trust's distribution
keeps **the same character in your hands that it had in the trust's hands**
(section 223 of the 2025 Act). So one payout of, say, ₹{{ x.total_pu }} a unit
is really several different kinds of money wearing one label:

| Component | Where it came from | In your hands |
|---|---|---|
| **Interest** | The SPV paid interest on loans from the trust | Taxed at your slab |
| **Dividend** | The SPV paid a dividend to the trust | **Exempt** — *unless* the SPV chose the lower company tax rate, then taxed at your slab |
| **Rent** (REITs) | Property the REIT owns directly | Taxed at your slab |
| **Repayment of debt / capital** | The SPV repaid loans, or the trust returned capital | Not taxed as income up to a limit — but it **reduces your cost** |
| Other income | For example, interest on the trust's own deposits | Taxed inside the trust; exempt in your hands |

The trust tells you the split. It has to give each unit holder a statement of
the nature of what it paid. Your job is to use it rather than treating the
whole credit as one thing.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You and your friends put money into a lemonade club. The club lends some of
it to a lemonade stand, and buys a share of a second stand.

At the end of the month the club hands you ₹24. But it came from three
places: ₹9 was the first stand paying *interest* on its loan, ₹5 was your
share of the second stand's *profits*, and ₹10 was the first stand paying
back part of the *loan itself*.

The first two are earnings. The last one is partly your own money coming
back. It wouldn't be fair to tax it like earnings — but it does mean your
share of the club is now worth a bit less on paper.

</details>

## Why the dividend is sometimes taxed and sometimes not

A company can pay tax at the normal rate, or opt for a lower rate by giving
up most deductions (section 200 of the 2025 Act). If the SPV **didn't** opt
for the lower rate, it has already paid full tax on its profit, and the
dividend it passes up is exempt in your hands. If it **did** opt, the dividend
is taxed at your slab rate.

You can't tell which from the payout. The trust's statement tells you, and
it can differ between SPVs of the same trust.

## The "repayment of debt" component

Before the Finance Act 2023, this piece was taxed nowhere: the trust didn't pay tax on it and
the unit holder didn't either. The Finance Act 2023 closed that gap, and the
2025 Act carries the rule forward (section 92(2)(k)). The formula:

```
Taxable "specified sum" = A − B − C   (never below zero)

A = ALL such repayments on the unit since it was issued,
    including those paid to earlier holders
B = the price at which the trust ISSUED the unit
C = amounts already taxed under this rule in earlier years
```

In words: repayments are tax-free until, cumulatively, they exceed the
**issue price** of the unit. Only the excess is taxed, at your slab.

And the part that isn't taxed isn't forgotten. It is **deducted from your
cost of acquisition** (section 72(4)), so it comes back as a larger capital
gain when you sell. It's a deferral, not an exemption.

Two consequences:

- **The formula uses the issue price, not your purchase price.** If you
  bought on the exchange, the history before you arrived counts.
- **A young trust is far from the limit; an old one may not be.** A trust that has been
  returning capital for a decade may have crossed its issue price, and from
  then on every rupee of "repayment" is taxable income.

## Worked example: one year of distributions

A hypothetical listed REIT, round numbers. Our investor bought
{% include inr.html n=x.units %} units on the exchange on {{ x.buy_date }} at
₹{{ x.buy_price }}; the trust had originally issued them at ₹{{ x.issue_price }}.
In {{ v.financial_year }} the trust pays ₹{{ x.total_pu }} a unit. Its
statement splits it as below, and says the SPV has **not** opted for the lower
company rate. We assume a 30% slab plus {{ r.cess_pct }}% cess, and income
below ₹50 lakh, so no surcharge.

| Component | Per unit | Received | Tax treatment | Tax with cess |
|---|---:|---:|---|---:|
| Interest from SPV | ₹{{ x.interest_pu }} | ₹{% include inr.html n=x.interest %} | Slab | ₹{% include inr.html n=x.interest_tax_with_cess %} |
| Dividend from SPV | ₹{{ x.dividend_pu }} | ₹{% include inr.html n=x.dividend %} | Exempt | ₹0 |
| Repayment of debt | ₹{{ x.repay_pu }} | ₹{% include inr.html n=x.repay %} | Reduces cost | ₹0 now |
| **Total** | **₹{{ x.total_pu }}** | **₹{% include inr.html n=x.total %}** | | **₹{% include inr.html n=x.interest_tax_with_cess %}** |

- **TDS.** The trust deducts 10% on the interest part: ₹{% include inr.html n=x.interest_tds %}.
  There's no TDS on a dividend from an SPV that hasn't opted for the lower
  rate. So ₹{% include inr.html n=x.interest_balance_due %} is still due when you file.
- **The dividend, had the SPV opted.** Then it would be taxed like the
  interest: ₹{% include inr.html n=x.dividend_tax_if_spv_opted_with_cess %} with cess, with ₹{% include inr.html n=x.dividend_tds_if_spv_opted %} deducted at source.
- **The repayment.** All repayments on this unit since issue come to
  ₹{{ x.cum_repay_pu }}, against an issue price of ₹{{ x.issue_price }}. So
  A − B − C is below zero, the specified sum is ₹{{ x.specified_sum_pu }}, and
  nothing is taxed this year. Instead the cost of the holding falls from
  ₹{% include inr.html n=x.cost_before %} to ₹{% include inr.html n=x.cost_after %} (₹{{ x.cost_after_pu }} a unit).

So the tax on a ₹{% include inr.html n=x.total %} payout is ₹{% include inr.html n=x.interest_tax_with_cess %}, about
{{ x.effective_tax_on_distribution_pct }}% of it. Treat the whole payout as
interest and you'd pay ₹{% include inr.html n=x.tax_if_all_treated_as_interest_with_cess %} — ₹{% include inr.html n=x.overpay_if_all_interest %} too much. Treat it all as
exempt and you'd under-report the interest.

### When the repayment does get taxed

An older, hypothetical InvIT issued units at ₹{{ x.invit_issue_price }}. By this year,
repayments on each unit since issue — to everyone who ever held it — total
₹{{ x.invit_cum_repay_y1 }}.

| | Year 1 | Year 2 |
|---|---:|---:|
| A: repayments since issue | ₹{{ x.invit_cum_repay_y1 }} | ₹{{ x.invit_cum_repay_y2 }} |
| B: issue price | ₹{{ x.invit_issue_price }} | ₹{{ x.invit_issue_price }} |
| C: already taxed | ₹0 | ₹{{ x.invit_specified_y1_pu }} |
| **Specified sum per unit** | **₹{{ x.invit_specified_y1_pu }}** | **₹{{ x.invit_specified_y2_pu }}** |
| On {% include inr.html n=x.invit_units %} units, taxed at slab | ₹{% include inr.html n=x.invit_specified_y1 %} | ₹{% include inr.html n=x.invit_specified_y2 %} |
| Tax with cess | ₹{% include inr.html n=x.invit_tax_y1_with_cess %} | ₹{% include inr.html n=x.invit_tax_y2_with_cess %} |

C is what stops the same rupee being taxed twice: year 2 taxes only the new
₹{{ x.invit_specified_y2_pu }}.

## Selling the units

Listed REIT and InvIT units are taxed almost exactly like listed shares:

| | Listed REIT/InvIT units |
|---|---|
| Long-term after | {{ r.equity_holding_months }} months |
| Short-term rate | {{ r.equity_stcg_pct }}% (sold on the exchange, STT paid) |
| Long-term rate | {{ r.equity_ltcg_pct }}% above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year |
| Annual exemption | **Shared** with equity shares and equity funds — one ₹{% include inr.html n=r.ltcg_annual_exemption %} across all of them |

**STT** is securities transaction tax, charged on exchange trades. This is
the July 2024 position. Before 23 July 2024, units of a listed business trust
needed **36 months** to become long-term, and the rates were 15% and 10%
(per the Memorandum to the Finance (No. 2) Bill, 2024). Anything older you
read on REIT taxation may still carry those numbers.

Continuing the example: the investor sells all {% include inr.html n=x.units %} units on
{{ x.sale_date }} at ₹{{ x.sale_price }}, {{ x.months_held }} months after buying.

| | |
|---|---:|
| Sale value | ₹{% include inr.html n=x.sale_value %} |
| Cost, **after** deducting the ₹{% include inr.html n=x.repay %} repayment | ₹{% include inr.html n=x.cost_after %} |
| **Long-term gain** | **₹{% include inr.html n=x.gain %}** |
| Tax if the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption is unused | ₹0 |
| Tax if the exemption is already used on other equity gains | ₹{% include inr.html n=x.ltcg_tax_if_exemption_used_with_cess %} |
| Tax had it been sold within {{ r.equity_holding_months }} months (at {{ r.equity_stcg_pct }}%) | ₹{% include inr.html n=x.stcg_tax_if_within_12m_with_cess %} |

Using the original cost would show a gain of ₹{% include inr.html n=x.gain_if_cost_not_reduced %}, understating it
by exactly the ₹{% include inr.html n=x.repay %} of repayment that was tax-free on the way in.

The [holding-period post]({% post_url 2026-10-28-short-term-vs-long-term %}) covers how the
holding period is counted, and the
[equity post]({% post_url 2026-10-29-equity-and-equity-funds %}) covers the annual exemption.

## Surcharge and TDS, briefly

Above ₹50 lakh of total income, a surcharge is added to the tax, as the
[opening post of this series]({% post_url 2026-10-27-how-investment-income-is-taxed %})
explained. The interest and rent components are ordinary income, so their
surcharge can go higher. Capital gains on the units, and the taxable dividend
component, are capped at 15%.

The 10% TDS on the taxable components, like TDS on
[dividends and interest]({% post_url 2026-10-31-dividends-and-interest %}), is an advance, not
the final tax. In the 30% slab you'll owe the difference.

## Common mistakes

- **Treating the whole distribution as one kind of income.** Check the
  trust's statement. The split decides the tax, and it can change from one
  quarter to the next.
- **Assuming every dividend from a trust is exempt.** It's exempt only if the
  SPV didn't opt for the lower company tax rate. The statement tells you
  which.
- **Forgetting that repayments reduce your cost.** The tax-free repayment
  comes back as a bigger capital gain on sale. Your broker's capital gains
  statement may not adjust for it, so check before you file.
- **Plugging your purchase price into the formula.** The repayment test uses
  the trust's *issue* price and every repayment since issue, including those
  paid to earlier holders. A long-lived trust can cross the line before you
  ever bought in.
- **Using pre-2024 rules on a sale.** Listed units are long-term after
  {{ r.equity_holding_months }} months now, not 36, at {{ r.equity_ltcg_pct }}%, and they share the equity exemption.

**Takeaway:** A REIT or InvIT payout is several incomes in one credit:
interest and rent are taxed at your slab, dividends are exempt unless the SPV
chose the lower company tax rate, and "repayment of debt" is tax-free until
repayments pass the issue price — while it lowers your cost. Read the trust's
split, not the credit.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax3.yml)
lists the sections of the Income-tax Act, 2025 behind every rule here, and
the points a professional should confirm before you rely on them.*
