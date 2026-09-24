---
layout: post
title: "Foreign stocks and Schedule FA: the disclosure is the hard part"
description: "US-share gains are long-term only after 24 months, at 12.5% with no exemption; dividends are withheld at 25% and credited; every foreign asset is disclosed, no minimum."
image: /assets/og/foreign-stocks-and-schedule-fa.png
date: 2026-12-17 09:00:00 +0530
series: tax
term: "Schedule FA (foreign assets)"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign x = t2.foreign %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, verified against public
sources in {{ v.verified_on }}. Educational content, not tax advice.*

## Three separate obligations

Buying a share of a US-listed company through an Indian app feels like buying
any other share. For tax it creates three obligations that Indian shares
don't:

1. **Different capital-gains rules** — a 24-month holding period, slab-rate
   short-term tax, and no annual exemption.
2. **Withholding abroad on dividends**, which you then credit against Indian
   tax with the right form filed at the right time.
3. **Disclosure**: every foreign asset you held at any point in the calendar
   year goes into **Schedule FA** of your return, whether or not it earned
   anything, with no minimum value.

The first two cost money. The third is the one that generates notices, and
the penalty for getting it wrong is out of all proportion to the amounts
most people invest.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Keeping a piggy bank at home is easy: nobody asks about it. Keeping a piggy
bank at a cousin's house in another country comes with rules. You have to
tell your parents it exists — even if it has one coin in it — and tell them
every year, because they can't see it from here. If the cousin's parents take
a small cut of any coins you're given, you show the receipt and your parents
charge you less. And if you never mention the piggy bank at all, the
punishment is much bigger than the coins.

</details>

## Capital gains: 24 months, slab, no exemption

Foreign listed shares are treated like unlisted shares, not like Indian
listed ones:

| | Indian listed shares | Foreign shares |
|---|---|---|
| Long-term after | {{ r.equity_holding_months }} months | **{{ r.other_holding_months }} months** |
| Short-term rate | {{ r.equity_stcg_pct }}% | **Your slab rate** |
| Long-term rate | {{ r.equity_ltcg_pct }}% | {{ r.equity_ltcg_pct }}%, no indexation |
| Annual exemption | ₹{% include inr.html n=r.ltcg_annual_exemption %} | **None** |

Two further wrinkles. Gains are computed in **rupees**, so a move in the
exchange rate is part of your gain (or loss) even if the dollar price never
changed. And the rupee conversion uses a prescribed rate — the **SBI TT
buying rate on the last day of the month before** the month of purchase, and
likewise for the sale — not the rate your broker happened to give you.

### Worked example

A hypothetical purchase of US shares for ${% include inr.html n=x.usd_buy %}, sold {{ x.months_held }} months
later for ${% include inr.html n=x.usd_sell %}. The exchange rates are illustrative stand-ins for the
prescribed SBI rate.

| | |
|---|---:|
| Cost: ${% include inr.html n=x.usd_buy %} × ₹{{ x.fx_buy }} | ₹{% include inr.html n=x.inr_cost %} |
| Sale: ${% include inr.html n=x.usd_sell %} × ₹{{ x.fx_sell }} | ₹{% include inr.html n=x.inr_sale %} |
| **Long-term gain** (held > {{ r.other_holding_months }} months) | **₹{% include inr.html n=x.gain_inr %}** |
| of which rupee depreciation alone (${% include inr.html n=x.usd_buy %} × ₹{{ x.fx_change }}) | ₹{% include inr.html n=x.currency_component_inr %} |
| Exemption | none |
| **Tax at {{ r.equity_ltcg_pct }}% with cess** | **₹{% include inr.html n=x.ltcg_tax_with_cess %}** |

The same ₹{% include inr.html n=x.gain_inr %} gain on Indian listed shares would have been taxed at
₹{% include inr.html n=x.same_gain_indian_listed_tax_with_cess %}, because ₹{% include inr.html n=r.ltcg_annual_exemption %} of it would have been
exempt. And had the shares been sold inside 24 months, the whole gain would
sit in the slab: ₹{% include inr.html n=x.stcg_tax_with_cess_if_within_24m %} at 30% plus cess. The
[holding-period post]({% post_url 2026-10-28-short-term-vs-long-term %}) explained why the
clock matters; for foreign shares it runs twice as long and the short-term
penalty is steeper.

## Dividends: withheld at 25%, then credited

US companies pay dividends to Indian residents after withholding **25%** under
the India–US tax treaty. In India the *gross* dividend is added to your income
at slab, exactly as in the
[dividends post]({% post_url 2026-10-31-dividends-and-interest %}) — and the tax already
paid in the US is credited against your Indian tax.

| | |
|---|---:|
| Dividend declared | ${{ x.dividend_usd }} |
| Withheld in the US (25%) | ${{ x.dividend_us_withheld_usd }} |
| Gross dividend in rupees (at ₹{{ x.fx_sell }}) | ₹{% include inr.html n=x.dividend_inr_gross %} |
| Indian tax at 30% + cess | ₹{% include inr.html n=x.dividend_india_tax_with_cess %} |
| − Credit for US tax (₹{% include inr.html n=x.dividend_us_withheld_inr %}) | |
| **Further tax payable in India** | **₹{{ x.dividend_india_payable_after_credit }}** |

The credit isn't automatic. It requires **Form 67** (being renumbered under
the new Act), filed on the portal *before* you submit the return, and the
income and credit reported consistently in **Schedule FSI** (foreign-source
income) and **Schedule TR** (tax relief). Miss the form and you pay Indian tax
on the full ₹{% include inr.html n=x.dividend_inr_gross %} with no credit — a genuine double tax, entirely
self-inflicted. Someone below the 25% effective rate in India gets no refund
of the excess US withholding either; the credit is capped at the Indian tax
on that income.

## TCS on the way out

Money sent abroad under the **LRS — Liberalised Remittance Scheme** — attracts
**TCS (Tax Collected at Source)** of **{{ x.lrs_tcs_rate_pct }}%** on the amount above
₹{% include inr.html n=x.lrs_tcs_threshold %} per financial year for investment purposes (education and
medical remittances have lower rates). Remit ₹{% include inr.html n=x.lrs_remit_example %} to a foreign
broker in a year and ₹{% include inr.html n=x.lrs_tcs_example %} is collected up front.

It is not a tax on investing. Like TDS, it's an advance: it shows up in Form
26AS and is adjusted against your tax when you file, or refunded. But it's
cash out of your account for up to a year, and it makes the remittance
visible to the department — which brings us to disclosure.

## Schedule FA: the part that actually bites

If you are **resident and ordinarily resident** in India and held *any*
foreign asset at *any* time in the year, you must report it in Schedule FA
of ITR-2 or ITR-3. Four things about this catch people out:

**It runs on the calendar year, not the financial year.** For the return
covering FY 2025-26 you report assets held between 1 January and 31 December
2025. This is the only schedule in the return on that basis, and it's because
the data India receives from other countries under automatic exchange arrives
by calendar year.

**There is no minimum.** One share, held for a week, then sold — reportable.
A foreign brokerage account with a dormant $3 balance — reportable.
Sell-to-cover RSU shares from a foreign parent that existed for one day —
reportable.

**It covers more than shares.** Foreign brokerage accounts, foreign bank
accounts, RSUs and ESOPs of a foreign employer (from the
[previous post]({% post_url 2026-12-14-esops-and-rsus %})), foreign retirement
accounts, foreign insurance with a cash value.

**It asks for values you have to reconstruct.** For each asset: the initial
cost, the *peak* value during the calendar year, the closing value on 31
December, and the income it produced — all in rupees at the SBI TT buying
rate. Nobody sends you a statement in this format. You build it.

The penalty framework is the **Black Money Act**, not ordinary income-tax
law: a flat penalty of ₹{% include inr.html n=x.bma_penalty %} per year for non-disclosure or
inaccurate disclosure, with prosecution possible in serious cases. Since
1 October 2024 that penalty is not levied where the aggregate value of your
foreign assets (excluding immovable property) is under
₹{% include inr.html n=x.bma_penalty_exemption_threshold %} — a relief for small investors, but note carefully
what it relieves: the *penalty*, not the *duty to disclose*. The schedule is
still required, and the department has been matching foreign-remittance and
exchange-of-information data against returns and issuing notices where the
schedule is blank.

## Common mistakes

- **Applying the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption to foreign shares.** It exists only for
  STT-paid Indian equity.
- **Selling at 13 months and calling it long-term.** Foreign shares need 24.
- **Using your broker's conversion rate.** The rules prescribe the SBI TT
  buying rate on the last day of the preceding month — for both legs.
- **Skipping Form 67.** No form, no credit for the 25% already paid in the
  US.
- **Leaving Schedule FA blank because "it's tiny".** No minimum. The ₹20 lakh
  relief applies to the penalty, not the disclosure.
- **Reporting foreign assets by financial year.** Schedule FA runs
  1 January – 31 December.
- **Forgetting the foreign parent's RSUs.** The shares *and* the foreign
  brokerage account they sit in are both foreign assets.
- **Treating TCS as a cost.** It's an advance, recoverable when you file —
  but only if you file, and only if it's in your 26AS.

**Takeaway:** Foreign shares are taxed like unlisted ones — long-term only
after 24 months, short-term at your slab, {{ r.equity_ltcg_pct }}% beyond with no ₹{% include inr.html n=r.ltcg_annual_exemption %}
exemption, and the rupee's fall counts as gain. US dividends lose 25% at source
that you recover only by filing Form 67. But the obligation that actually
hurts is Schedule FA: every foreign asset, every calendar year, no minimum —
and a ₹{% include inr.html n=x.bma_penalty %} penalty regime waiting for the ones left blank.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists every source these rules were checked against, and the points a
professional should confirm before you rely on them.*
