---
layout: post
title: "Bonds, debentures and SGBs: listed or not decides the tax"
description: "Bond interest is taxed at your slab; the gain depends on listing. Listed bonds can be long-term; unlisted ones and MLDs never are. SGBs differ again."
image: /assets/og/bonds-debentures-and-sgbs.png
date: 2026-12-24 09:00:00 +0530
series: tax
term: "Bond and SGB taxation"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t3 = site.data.tax3 %}
{% assign v = t3.verification %}
{% assign x = t3.bonds %}
{% assign r = site.data.tax.rates %}
{% assign bd = site.data.jargon_m6.bond %}
{% assign bd_gain = bd.face | minus: bd.buy_price %}

## Two kinds of return, taxed separately, Tax Year 2026-27

This post describes Tax Year 2026-27 (FY, or financial year, 2026-27, April 2026 to March 2027). YTM is yield to maturity. Rules are as read in the Income-tax Act, 2025 and the Finance Act, 2026.

A bond pays you in two ways. There's the **coupon** — the interest it pays
each year — and there's whatever you make or lose on the price, if you sell
before maturity or bought away from face value. The
[YTM (yield to maturity) post]({% post_url 2026-10-05-yield-to-maturity %}) folded both into one yield.
Tax pulls them apart again:

```
Coupon / interest   ->  "income from other sources", taxed at your slab
Price gain or loss  ->  capital gain, taxed by what the bond IS:
                        listed, unlisted, market-linked, or a Sovereign Gold Bond
```

The interest side is simple and the same for almost every bond. The gain
side is where the rules changed in 2023 and 2024, and where the answer turns
on a detail most investors never check: **is the bond listed?**

A **debenture** is a company's bond; the tax rules treat bonds and debentures
alike. An **NCD** (non-convertible debenture) is the kind retail investors
usually meet in a public issue.

## Interest: slab rate, with TDS above a threshold

Interest on bonds and debentures is added to your income and taxed at your
slab rate, exactly like the deposit interest in the
[dividends and interest post]({% post_url 2026-12-08-dividends-and-interest %}).

TDS (tax deducted at source) on "interest on securities" is 10% for a
resident (Finance Act, 2026, First Schedule, Part II), once the year's interest from a payer crosses
₹{% include inr.html n=x.ncd_tds_threshold %} (section 393(1) of the Income-tax Act, 2025). Listed demat debentures used to be exempt from TDS; that
exemption was removed from 1 April 2023 (Memorandum to the Finance Bill,
2023), the memorandum's reason being under-reporting of the interest. Securities of the Central or a State Government carry no deduction, except the taxable savings bonds listed in section 393(4), Sl. 6, and any the government notifies.

**Worked example.** ₹{% include inr.html n=x.ncd_invested %} in a listed NCD (non-convertible debenture) paying {{ x.ncd_coupon_pct }}%, at a 30% slab
plus {{ r.cess_pct }}% cess (income below ₹50 lakh, so no surcharge):

| | |
|---|---:|
| Interest for the year | ₹{% include inr.html n=x.ncd_interest %} |
| TDS at 10% (above the ₹{% include inr.html n=x.ncd_tds_threshold %} threshold) | ₹{% include inr.html n=x.ncd_tds %} |
| Tax at 30% + cess | ₹{% include inr.html n=x.ncd_tax_with_cess %} |
| **Still due when you file** | **₹{% include inr.html n=x.ncd_balance_due %}** |

## Capital gains: four different answers

| What you hold | Long-term after | Short-term | Long-term |
|---|---|---|---|
| **Listed** bond or debenture | {{ r.equity_holding_months }} months | Slab | {{ r.equity_ltcg_pct }}%, no indexation, **no** ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption |
| **Unlisted** bond or debenture | *Never* — always short-term | Slab | — |
| **Market-linked debenture** (listed or not) | *Never* — always short-term | Slab | — |
| **Sovereign Gold Bond** | See below | | |

A few notes on where these come from, because each one surprises someone. Two things are out of scope here: zero-coupon bonds (the Act gives them the 12-month line, but their treatment isn't covered further) and accrued interest paid when buying on the secondary market.

**Listed bonds** count as a "security listed in a recognised stock exchange",
so they share listed shares' 12-month line.
The ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption is only for equity shares, equity-fund units
and business-trust units, so a listed bond's long-term gain is taxed at
{{ r.equity_ltcg_pct }}% from the first rupee (sections 197 and 198).

**Unlisted bonds and debentures** sold, redeemed or maturing on or after
23 July 2024 are treated as short-term *whatever the holding period*, and
taxed at your slab. The reasoning in the Memorandum to the
Finance (No. 2) Bill, 2024: they are debt instruments, so their gains should
be taxed at the applicable rate, like interest.

**MLDs — market-linked debentures** — are debentures whose return is linked
to a market index or other securities rather than a fixed coupon. Their gains are
always short-term, listed or not, under the same provision. The Finance Bill 2023
memorandum places the change in FY 2023-24 (Finance Act 2023). Debt mutual fund units bought on or after 1 April 2023 are treated the same way; see the [debt funds tax post]({% post_url 2026-12-04-debt-funds-gold-and-the-rest %}).

**Worked example.** The same ₹{% include inr.html n=x.same_gain %} gain, taxed four ways (30% slab,
{{ r.cess_pct }}% cess):

| The gain came from | Tax with cess |
|---|---:|
| Listed bond, held more than {{ r.equity_holding_months }} months | ₹{% include inr.html n=x.gain_tax_ltcg_with_cess %} |
| Listed bond, held {{ r.equity_holding_months }} months or less | ₹{% include inr.html n=x.gain_tax_slab_with_cess %} |
| Unlisted bond, any holding period | ₹{% include inr.html n=x.gain_tax_slab_with_cess %} |
| Market-linked debenture, any holding period | ₹{% include inr.html n=x.gain_tax_slab_with_cess %} |

The tax differs by ₹{% include inr.html n=x.gain_tax_difference %} between the first row and the others, on the same gain. The size
of the gap depends on the slab rate that applies to you.

Where do bond gains come from, if you hold to maturity? Mostly from buying
below face value. The YTM post's bond bought at ₹{% include inr.html n=bd.buy_price %} and repaid at
₹{% include inr.html n=bd.face %} earns ₹{% include inr.html n=bd_gain %} of its yield as a capital gain rather than as interest. If that bond is listed and held more than a year, that slice is taxed at {{ r.equity_ltcg_pct }}% while the
coupons are taxed at your slab.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You lend your cousin ₹100 and she promises ₹8 every year plus your ₹100 back
at the end. The ₹8s are "interest", and the tax rule for those is simple.

Now say you buy that promise from a friend for ₹96 instead. At the end you
still get ₹100 — ₹4 more than you paid. That extra ₹4 is a "gain", and gains
have their own rules.

For some promises (the ones traded on a proper exchange) a gain kept for over
a year gets a lower tax. For promises traded privately, or fancy ones whose
payout depends on the stock market, the tax people say: "that's just interest
in disguise" — and tax it the same as the ₹8s.

</details>

## Sovereign Gold Bonds

**SGBs** are issued by the RBI (Reserve Bank of India) on the government's
behalf, priced in grams of gold. Per [the RBI's FAQ](https://www.rbi.org.in/commonman/English/Scripts/FAQs.aspx?Id=1658) (a page headed "Updated as on February 4, 2019", so
check the current scheme terms) they pay **{{ x.sgb_coupon_pct }}% a
year** on the issue value, run **eight years**, and allow early redemption
with the RBI after the fifth year.

**The interest** is taxable at your slab, like any bond interest, and **no
TDS** is deducted — so it's easy to forget, and it's taxable all the same.

**The gain at redemption** is where Budget 2026 changed things, as
[the debt funds and gold post]({% post_url 2026-12-04-debt-funds-gold-and-the-rest %}) noted.
From 1 April 2026, redemption is not treated as a transfer — so no capital
gain arises — only if the bond was **held by an individual from the date of
original issue till maturity** (section 70(1)(x) of the 2025 Act, as substituted by section 43 of the Finance Act, 2026).

| How you got in and out | Gain at the end |
|---|---|
| Subscribed at issue, held to maturity | **Exempt** |
| Bought on the exchange, held to maturity (and over {{ r.equity_holding_months }} months) | Taxable: long-term after {{ r.equity_holding_months }} months (it's a listed security), {{ r.equity_ltcg_pct }}%, no ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption |
| Sold on the exchange before maturity | Normal capital gains, same rates |
| Redeemed early with the RBI after year five | **Check first** — on the new wording this isn't "maturity" |

That last row deserves care. The old wording, which the 2025 Act first
carried over, covered any redemption by an individual. The new wording says "till maturity", and we
found no official clarification of how an early redemption with the RBI is
treated. Check the current rule before relying on either reading.

**Worked example.** {{ x.sgb_grams }} units (grams) subscribed at issue at
₹{% include inr.html n=x.sgb_issue_price %}, redeemed at maturity at ₹{% include inr.html n=x.sgb_maturity_price %}. Round, hypothetical prices.

| | Subscribed at issue | Bought on exchange at ₹{% include inr.html n=x.sgb_exchange_price %} |
|---|---:|---:|
| Cost | ₹{% include inr.html n=x.sgb_invested %} | ₹{% include inr.html n=x.sgb_exchange_cost %} |
| Maturity value | ₹{% include inr.html n=x.sgb_maturity_value %} | ₹{% include inr.html n=x.sgb_maturity_value %} |
| Gain | ₹{% include inr.html n=x.sgb_gain_issue %} | ₹{% include inr.html n=x.sgb_gain_exchange %} |
| **Tax on the gain, with cess** | **₹0** | **₹{% include inr.html n=x.sgb_tax_exchange_with_cess %}** |

Interest on the original holding: ₹{% include inr.html n=x.sgb_interest_yr %} a year, taxed at
₹{% include inr.html n=x.sgb_interest_tax_yr_with_cess %} a year at 30% plus cess — ₹{% include inr.html n=x.sgb_interest_tax_total_with_cess %} over the eight years. The exemption
covers the gold price gain, not the coupon.

## Surcharge

All of the above assumes income under ₹50 lakh. Above it, a surcharge is
added before cess. Bond interest, and gains taxed at slab, follow the ordinary
scale. Which gains get a lower surcharge cap is set out, with its source, in the
[opening post]({% post_url 2026-11-02-how-investment-income-is-taxed %}). As we read the Finance Act's surcharge provisions, the 15% cap covers long-term gains under section 197, which includes listed bonds and SGBs bought on the exchange, but not gains taxed at slab.

## Common mistakes

- **Assuming bond gains get the ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption.** It's for equity, equity
  funds and REIT (real estate investment trust) and InvIT (infrastructure investment trust) units, as in the
  [REITs and InvITs post]({% post_url 2026-12-22-reits-and-invits %}). Listed bonds pay
  {{ r.equity_ltcg_pct }}% on the whole long-term gain.
- **Holding an unlisted bond "for the long-term rate".** There isn't one any
  more: since 23 July 2024 a gain on an unlisted bond or debenture is
  taxed at slab however long it is held.
- **Forgetting SGB interest because no TDS was deducted.** It's taxable every
  year, at your slab.
- **Buying SGBs on the exchange expecting the maturity exemption.** From
  1 April 2026 it needs the original subscription and continuous holding till
  maturity.

**Takeaway:** Bond interest is taxed at your slab every year; the gain
depends on the wrapper. Listed bonds become long-term after {{ r.equity_holding_months }} months at
{{ r.equity_ltcg_pct }}% with no exemption, unlisted bonds and market-linked debentures are
taxed at slab, and an SGB's gain is tax-free only if you subscribed at
issue and held to maturity.

*The module's [data file](https://github.com/himanshug82/wealthprimer/blob/main/_data/tax3.yml)
lists the sections of the Income-tax Act, 2025 behind the rules here, and
earlier notes. The rates and the SGB wording here were re-read in the [Finance Act, 2026](https://egazette.gov.in/WriteReadData/2026/271439.pdf) on 2 November 2026.*
