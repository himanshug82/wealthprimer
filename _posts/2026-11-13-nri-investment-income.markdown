---
layout: post
title: "NRI investment income: same rates, tax taken at source"
description: "An NRI pays largely the same rates on Indian gains and interest, but the tax is deducted at source. TDS, treaties and TRCs, and NRE vs NRO interest."
image: /assets/og/nri-investment-income.png
date: 2026-11-13 09:00:00 +0530
series: tax
term: "NRI taxation (TDS, DTAA, NRE/NRO)"
---

{% assign t3 = site.data.tax3 %}
{% assign v = t3.verification %}
{% assign x = t3.nri %}
{% assign g = t3.gifts %}
{% assign r = site.data.tax.rates %}

*Rules described here apply to **{{ v.financial_year }}**, checked against the
text of the Income-tax Act, 2025 and the Finance Act, 2026 in {{ v.verified_on }}.
Educational content, not tax advice — and for non-residents especially, the
rules of the country you live in matter as much as India's.*

## What changes when you leave

An **NRI — non-resident Indian** — is, for tax, simply an Indian citizen (or
person of Indian origin) who isn't resident in India in the tax year. Broadly,
under section 6 of the 2025 Act you're resident if you spend **{{ x.resident_days }} days or
more** in India in the year, or **{{ x.short_stay_days }} days** in the year plus {{ x.lookback_days }} days over
the previous {{ x.lookback_years }} years; for a citizen who's working abroad, or visiting, the
second test is relaxed. Edge cases — the 120-day rule, "deemed residents",
the "not ordinarily resident" middle status — are beyond this post. Settle
your status first, because everything below depends on it.

A non-resident is taxed in India only on income that arises, or is
received, in India. For an
investor that's the familiar list: capital gains on Indian shares and funds,
dividends, and interest on Indian deposits and bonds. The **rates** are
largely the ones earlier posts in this series used. What changes is
**collection**:

| | Resident | Non-resident |
|---|---|---|
| Mutual fund redemption | No TDS; you pay at filing (or through [advance tax]({% post_url 2026-11-11-advance-tax-for-investors %})) | **TDS on the gain** at the applicable rate |
| Fund IDCW, share dividends | 10% TDS above a threshold | 20% TDS, or the treaty rate if lower |
| Bank interest | 10% TDS above a threshold | **NRO: 30% TDS** plus cess · **NRE: exempt** |

## TDS on capital gains

When a non-resident sells or redeems, the payer (the fund house, or the
broker for listed shares) deducts tax from the **gain** before paying out.
The rates come from the Finance Act, 2026 (First Schedule, Part II), for a
non-resident Indian:

| Gain | TDS rate |
|---|---:|
| Long-term, equity shares and equity funds (above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year) | {{ x.tds_eq_ltcg_pct }}% |
| Short-term, equity shares and equity funds (STT paid) | {{ x.tds_eq_stcg_pct }}% |
| Other long-term gains | {{ x.tds_eq_ltcg_pct }}% |
| Other income, including short-term gains on debt funds | {{ x.tds_other_pct }}% |

Plus **{{ r.cess_pct }}% cess** on the TDS, and a **surcharge** once the amount paid
crosses ₹50 lakh (capped at 15% on capital gains and dividends).

The rates match what a resident would pay on the same gain, at a 30% slab.
The differences are timing and a few resident-only reliefs: a resident with
low income can set the unused basic exemption against special-rate gains,
and claim the rebate that cancels tax on small incomes. Those are for
residents only (sections 196 to 198 and 156). An NRI can't use either.

## Worked example: two real funds

Same terms, real NAVs: an NRI redeems the same UTI Nifty 50 Index Fund
holding the [equity post]({% post_url 2026-10-29-equity-and-equity-funds %}) used (₹{% include inr.html n=g.ls_invested %} invested on
{{ g.ls_buy_date }}), plus ₹{% include inr.html n=x.gilt_invested %} put into
UTI Gilt Fund (regular plan, growth — the fund from the
[debt funds post]({% post_url 2026-10-12-debt-funds-explained %})) on {{ x.gilt_buy_date }}. Both are
redeemed on {{ x.gilt_sell_date }} (AMFI NAVs via mfapi.in, as of 31 March 2026,
used for illustration only; we apply {{ v.financial_year }}'s rates, which
are unchanged from the year before). Payments are well under ₹50 lakh, so no
surcharge.

| | Equity index fund | Gilt fund |
|---|---:|---:|
| NAV at purchase → redemption | ₹{{ g.ls_buy_nav }} → ₹{{ g.ls_sell_nav }} | ₹{{ x.gilt_buy_nav }} → ₹{{ x.gilt_sell_nav }} |
| Redemption value | ₹{% include inr.html n=x.eq_value %} | ₹{% include inr.html n=x.gilt_value %} |
| Gain | ₹{% include inr.html n=x.eq_gain %} | ₹{% include inr.html n=x.gilt_gain %} |
| Treated as | Long-term, equity | Short-term, whatever the holding period (debt fund bought after 1 April 2023) |
| Taxable | ₹{% include inr.html n=x.eq_taxable %} (after the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption) | ₹{% include inr.html n=x.gilt_gain %} |
| TDS rate | {{ x.tds_eq_ltcg_pct }}% + cess | {{ x.tds_other_pct }}% + cess |
| **Deducted at source** | **₹{% include inr.html n=x.eq_tds_with_cess %}** | **₹{% include inr.html n=x.gilt_tds_with_cess %}** |

A resident in the 30% slab would owe exactly the same on each: ₹{% include inr.html n=x.eq_tds_with_cess %} and
₹{% include inr.html n=x.gilt_resident_tax_with_cess %}. The difference is that the resident gets the full redemption
and pays later; the NRI receives the money with the tax already gone. The
gilt fund's treatment is the debt-fund rule from the
[debt funds tax post]({% post_url 2026-10-30-debt-funds-gold-and-the-rest %}): no long-term category for units
bought from April 2023.

Two consequences follow. **TDS can overshoot.** The payer doesn't know your
other losses or your treaty position, so if your actual liability is lower,
you get the difference back only by filing a return. And if you expect a
lower liability in advance, you can apply for a **lower or nil TDS
certificate** (section 395).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

When you live at home and sell your comics to a friend, your parents trust
you to hand over their share of the money at the end of the month.

When you've moved to another city, they can't check up on you as easily. So
they ask your friend to hand their share straight to them and give you the
rest. You still owe the same share either way — you just never hold it. And
if the friend took too much, you have to write to your parents to get it
back.

</details>

## Treaties, and the certificate that unlocks them

India has **DTAAs — double taxation avoidance agreements** — with many
countries, as the [foreign stocks post]({% post_url 2026-11-08-foreign-stocks-and-schedule-fa %})
touched on from the other side. For a non-resident, the rule is simple: **the
Act or the treaty, whichever is more beneficial** (section 159(4)). A treaty
may cap India's tax on interest or dividends below the Act's rate, or
allocate the right to tax some gains to the country where you live. What a
given treaty says is in its own articles; this post doesn't summarise any.

To claim a treaty benefit, you need a **TRC — tax residency certificate** —
from the government of the country where you're resident, plus the prescribed
documents and declaration (section 159(8)). No TRC, no treaty relief: the
payer deducts at the Act's rate, and your return is assessed at it too. Give the TRC and
declaration to the fund house or bank *before* the payment, and each year,
since a TRC covers a period.

And tax paid in India usually has to be dealt with again in your country of
residence, which may tax your worldwide income and give credit for India's
tax. That side is outside this series entirely.

## NRE and NRO accounts

Non-residents hold Indian bank money in two main kinds of account, and the
tax difference between them is stark:

| | NRE (non-resident external) | NRO (non-resident ordinary) |
|---|---|---|
| Typically holds | Money brought in from abroad | Income earned in India (rent, dividends, redemptions) |
| Interest on ₹{% include inr.html n=x.nro_interest %} | **Exempt** | Taxable |
| TDS | None | {{ x.tds_other_pct }}% + cess = ₹{% include inr.html n=x.nro_tds_with_cess %} |

The NRE exemption (Schedule IV of the 2025 Act) is for an individual who is a
"person resident outside India" **under FEMA** — the Foreign Exchange
Management Act — which has its own residence test, separate from the tax
one. When you move back and become resident under FEMA, the exemption stops;
the account should be redesignated, and interest from then on is taxable.

The NRO TDS rate is steep because it's the Act's rate for "other income". If
your total Indian income is modest, the TDS may exceed your actual liability,
and you recover it by filing — or head it off with a treaty rate and TRC, or
a lower-deduction certificate.

## Common mistakes

- **Treating TDS as the final tax.** It's a deduction on account, like a
  resident's. If it's more than you owe, the refund comes only through a
  return.
- **Assuming the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption is lost abroad.** It isn't; TDS on equity
  long-term gains applies only above it. What an NRI loses is the resident-only
  basic-exemption adjustment and rebate.
- **Claiming a treaty rate without a TRC.** The relief needs the certificate
  and the prescribed declaration, on file with the payer in time.
- **Keeping an NRE account after moving back.** The exemption follows your
  FEMA status, not the account's name.
- **Settling Indian tax and ignoring the other country.** The country you
  live in may tax the same income, with a credit for India's tax — a separate
  set of rules.

## What this series doesn't cover

Being clear about the edges, as the
[before-you-file post]({% post_url 2026-11-04-before-you-file %}) was. Since then this
series has picked up some of that post's gaps — gifts and clubbing, and the
basics of non-resident investment income — but these stay out:

- **Residence edge cases.** Deemed residents, "resident but not ordinarily
  resident" status, and the year you leave or return.
- **The other country's tax.** Foreign tax credits abroad, reporting of
  Indian accounts overseas, and how a treaty's tie-breaker decides residence.
- **Property in detail.** Rental income, the transitional rate option,
  reinvestment reliefs, and TDS when a non-resident sells property.
- **Estates and trusts.** Wills, succession across borders, private trusts
  and HUFs (Hindu undivided families).
- **Business income beyond F&O**, crypto and other virtual digital assets,
  and unlisted-company investing beyond the basics.
- **Anything contested.** Notices, appeals, penalties, and disputes.

And the standing caveat: this series was written for {{ v.financial_year }},
the first year under the Income-tax Act, 2025. The rates and the rules will
move with each Budget. Check the current position — and, where the amounts
matter, pay someone who files professionally.

**Takeaway:** For an NRI, most Indian investment income is taxed at the same
rates a resident would pay — the difference is that it's taken at source,
{{ x.tds_other_pct }}% on NRO interest and on debt-fund gains. NRE interest is exempt, a
treaty rate needs a TRC, and any excess TDS comes back only if you file.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax3.yml)
lists the sections of the Income-tax Act, 2025 behind every rule here, and
the points a professional should confirm before you rely on them.*
