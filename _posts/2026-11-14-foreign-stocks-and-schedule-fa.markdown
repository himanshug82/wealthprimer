---
layout: post
title: "Foreign stocks and Schedule FA: the disclosure is the hard part"
seo_title: "Foreign stocks and Schedule FA: the disclosure"
description: "Foreign shares need 24 months to count as long-term, with no annual exemption. US dividends are commonly cut 25% at source; foreign assets are disclosed."
image: /assets/og/foreign-stocks-and-schedule-fa.png
date: 2026-11-14 09:00:00 +0530
series: tax
term: "Schedule FA (foreign assets)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "September 2026"
---

{% assign t2 = site.data.tax2 %}
{% assign v = t2.verification %}
{% assign x = t2.foreign %}
{% assign r = site.data.tax.rates %}

## Three separate obligations

This post describes the rules as we last checked them for Tax Year 2026-27 (FY 2026-27, the year from April 2026 to March 2027). Parts rest on secondary sources, and each is marked "check the current rule" where that applies. In particular, the US withholding rates, Form 67, the Black Money Act penalty and the exchange-rate convention below come from secondary sources only (see the note at the end). From the Income-tax Act, 2025 itself we read only the holding periods, the definition of "rate of exchange" and the foreign-assets filing duty.

Buying a share of a US-listed company through an Indian app feels like buying
any other share. For tax it creates three obligations that Indian shares
don't:

1. **Different capital-gains rules** — a 24-month holding period, slab-rate
   short-term tax, and no annual exemption.
2. **Withholding abroad on dividends**, which you then credit against Indian
   tax with the right form filed at the right time.
3. **Disclosure**: every foreign asset you held during the reporting period
   goes into **Schedule FA** of your return, whether or not it earned
   anything, with no minimum value.

The first two cost money. The third is the one with a penalty attached, and
the penalty can be large relative to the amounts some people invest. (It does
not apply below a value threshold, covered below; the duty to disclose does.)

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

## Capital gains in Tax Year 2026-27: 24 months, slab, no exemption

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
changed. And the rupee conversion uses a prescribed rate, not the rate your
broker happened to give you. The Income-tax Act, 2025 defines the "rate of exchange"
as the rate determined or recognised by the Central Government (section 2(24)); the
specific rate is set in the Income-tax Rules, which this post has not read, so
we cannot state it as settled. A commonly described approach converts each leg at the
**SBI TT buying rate** — the State Bank of India's telegraphic-transfer
buying rate — on a prescribed date, such as the last day of the month before
the month of the transaction. Practice differs: some advisers apply the rate to
the gain itself, computed in dollars and converted once. The difference can be
material. Check the current rule in the Rules.

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
[holding-period post]({% post_url 2026-11-03-short-term-vs-long-term %}) explained why the
clock matters; for foreign shares it runs twice as long and the short-term
penalty is steeper.

## Dividends: withheld at 25%, then credited

US companies pay dividends to Indian residents after withholding **25%** under
the India–US tax treaty, as commonly described — assuming your broker has a W-8BEN form on file for
you; without one, 30% is commonly withheld. We have not opened the treaty or
US rules for this post: check the current rate. In India the *gross* dividend is added to your income
at slab, exactly as in the
[dividends post]({% post_url 2026-11-06-dividends-and-interest %}) — and the tax already
paid in the US is credited against your Indian tax.

| | |
|---|---:|
| Dividend declared | ${{ x.dividend_usd }} |
| Withheld in the US (25%) | ${{ x.dividend_us_withheld_usd }} |
| Gross dividend in rupees (at ₹{{ x.fx_sell }}) | ₹{% include inr.html n=x.dividend_inr_gross %} |
| Indian tax at 30% + cess | ₹{% include inr.html n=x.dividend_india_tax_with_cess %} |
| − Credit for US tax (₹{% include inr.html n=x.dividend_us_withheld_inr %}) | |
| **Further tax payable in India** | **₹{{ x.dividend_india_payable_after_credit }}** |

The credit isn't automatic. It is commonly described as requiring **Form 67**
(a form name from the earlier Rules, which may be renumbered under the new Act).
Filing it with or before your return is the usual description; a 2022 amendment
is reported to allow filing later if the return itself was filed in time. We have
not opened that notification or the current Rules, so check the current rule for
the form's name and deadline. The income and credit must also be reported consistently in **Schedule FSI** (foreign-source
income) and **Schedule TR** (tax relief). If the credit is not claimed, the same dividend can end up taxed in both countries: Indian tax on
the full ₹{% include inr.html n=x.dividend_inr_gross %} with nothing set against it. Whether any excess US withholding can be
recovered when the Indian tax is lower is not something we have confirmed; check the current rule.

## TCS on the way out

Money sent abroad under the **LRS — Liberalised Remittance Scheme** — attracts
**TCS (tax collected at source)** of **{{ x.lrs_tcs_rate_pct }}%** on the amount above
₹{% include inr.html n=x.lrs_tcs_threshold %} per financial year for investment purposes (education and
medical remittances have lower rates). That is the rate and threshold in the TCS table of the Income-tax Act, 2025 (ICAI copy) as we read it; Budget 2026 changes were not checked, so check the current rule. Remit ₹{% include inr.html n=x.lrs_remit_example %} to a foreign
broker in a year and ₹{% include inr.html n=x.lrs_tcs_example %} is collected up front.

It is not a tax on investing. Like TDS (tax deducted at source), it's an advance: it appears in your tax statements (AIS, the Annual Information Statement, and the older Form 26AS) and is adjusted against your tax when you file, or refunded. But it's
cash out of your account for up to a year, and it makes the remittance
visible to the department — which brings us to disclosure.

## Schedule FA: the part that actually bites

If you are **resident and ordinarily resident** in India and held *any*
foreign asset at *any* time in the reporting period, you must report it in Schedule FA
of your income-tax return (ITR, the income-tax return; ITR-2 or ITR-3 under the earlier forms). The
Income-tax Act, 2025 ties the duty to holding foreign assets "at any time during the tax year"
(section 263(1)(a)(ix) as we read it). Four things about this catch people out:

**The period may not match the financial year.** For returns filed under the
earlier Act (FY 2025-26), Schedule FA is commonly described as running on the
calendar year, 1 January to 31 December 2025, not the April–March year the rest of the return
uses. We have not confirmed the period for Tax Year 2026-27 returns, so check
what the current form asks for before you fill it in.

**There is no minimum.** One share, held for a week, then sold — reportable.
A foreign brokerage account with a dormant $3 balance — reportable.
Sell-to-cover RSU shares from a foreign parent that existed for one day —
reportable.

**It covers more than shares.** Foreign brokerage accounts, foreign bank
accounts, RSUs and ESOPs of a foreign employer (from the
[ESOPs and RSUs post]({% post_url 2026-11-11-esops-and-rsus %})), foreign retirement
accounts, foreign insurance with a cash value.

**It asks for values you have to reconstruct.** For each asset: the initial
cost, the *peak* value and the closing value for the reporting period (the
earlier forms used the calendar year and 31 December; check the current form
for Tax Year 2026-27), and the income it produced — all in rupees at the prescribed
rate. Nobody sends you a statement in this format. You build it.

The penalty framework is the **Black Money Act**, not ordinary income-tax
law. As commonly described, it carries a flat penalty of ₹{% include inr.html n=x.bma_penalty %} per year for non-disclosure or
inaccurate disclosure, with prosecution possible in serious cases. Since
1 October 2024 that penalty is described as not being levied where the aggregate value of your
foreign assets (excluding immovable property) does not exceed
₹{% include inr.html n=x.bma_penalty_exemption_threshold %}. We have only secondary sources for this, so check the
current rule and whether the statute says "under" or "up to". Note what any such relief covers: the *penalty*, not the *duty to disclose*.
The schedule is still required.

## Common mistakes

- **Applying Indian-equity treatment to foreign shares.** The ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption exists only for
  STT-paid Indian equity (STT is securities transaction tax), and foreign shares need 24 months, not 12, to be long-term.
- **Using your broker's conversion rate.** The Rules prescribe a rate (we have not read it). Practice differs between
  converting each leg and converting the gain, so check the current rule.
- **Skipping the foreign tax credit form.** No form, no credit for the 25% already paid in the
  US, as the earlier Rules worked.
- **Leaving Schedule FA blank because "it's tiny".** There is no minimum value for the duty to disclose. Any threshold relief
  applies to the penalty, not the disclosure. RSUs (restricted stock units) of a foreign parent count too: the shares *and*
  the foreign brokerage account they sit in are both foreign assets.

**Takeaway:** Foreign shares are taxed like unlisted ones — long-term only
after 24 months, short-term at your slab, {{ r.equity_ltcg_pct }}% beyond with no ₹{% include inr.html n=r.ltcg_annual_exemption %}
exemption, and the rupee's fall counts as gain. US dividends commonly lose 25% at source,
with credit in India dependent on the foreign tax credit form (check the current rule). A separate obligation is Schedule FA: every foreign asset held in the reporting period, no minimum value for the duty to disclose —
with a ₹{% include inr.html n=x.bma_penalty %} penalty regime that, as commonly described, applies above a value threshold.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax2.yml)
lists the sources behind these rules. For this post they are mostly secondary
(broker and adviser explainers); the Income-tax Act, 2025 was read only where
stated above, and the treaty, the Rules and the Black Money Act were not opened.
Treat the foreign-tax points as "check the current rule".*
