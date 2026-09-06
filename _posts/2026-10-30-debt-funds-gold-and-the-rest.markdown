---
layout: post
title: "Debt funds, gold and the rest: where the slab rate takes over"
description: "Where the concessional rates stop and your slab rate takes over. Debt fund units bought from April 2023, gold, property, and the end of indexation."
image: /assets/og/debt-funds-gold-and-the-rest.png
date: 2026-10-30 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## Everything that isn't equity

The [last post]({% post_url 2026-10-29-equity-and-equity-funds %}) covered listed shares
and equity funds — favourable rates, a 12-month line, an annual exemption.
Almost nothing else gets that treatment, and one large category lost it
entirely.

## Debt funds: the change that invalidated a decade of advice

This is the most consequential change in recent Indian investment taxation,
and the most under-appreciated.

**Units of specified debt mutual funds bought on or after 1 April 2023 are
taxed at your slab rate, whatever the holding period.** No long-term
category. No concessional rate. No indexation.

Before that date, debt funds held over three years were taxed at 20% *with
indexation* — meaning your cost was adjusted upward for inflation before
computing the gain, which in a moderate-inflation environment could reduce
the taxable gain to almost nothing. That was the entire reason debt funds
were preferred over fixed deposits by anyone in a higher slab.

That advantage is gone for new purchases. A debt fund and a fixed deposit are
now taxed broadly alike — at your slab rate.

| | Debt fund bought before 1 Apr 2023 | Debt fund bought on/after 1 Apr 2023 |
|---|---|---|
| Long-term category | Yes, after 24 months | **None** |
| Rate | Concessional | **Your slab rate** |
| Indexation | Available on older units | **No** |

**The practical consequence**: if you hold debt fund units bought before that
cut-off, they follow the older treatment, and your holding may contain both
kinds. Your capital gains statement should distinguish them; if it doesn't,
that's worth chasing before you file.

**Why this still isn't a reason to abandon debt funds.** Even taxed
identically to a deposit, a debt fund defers the tax until you redeem, while
a fixed deposit is taxed on interest accrued each year whether or not you
touch it. Deferral has real value over long periods. The tax *rate* changed;
the *timing* advantage didn't.

## Gold

| Form | Treatment |
|---|---|
| Physical gold, jewellery | Long-term after {{ r.other_holding_months }} months |
| Gold ETFs and gold funds | Follows the debt-fund rules above for units bought from April 2023 |
| Sovereign Gold Bonds | Held to maturity: capital gains exempt for individuals — the standout feature of the instrument |

Sovereign Gold Bonds are worth a line of their own. Redeemed at maturity with
the RBI, the capital gain is exempt for individual investors. Sell them on the
secondary market before maturity instead and normal capital gains rules
apply. Same instrument, entirely different tax outcome depending on how you
exit.

## Property

Long-term after {{ r.other_holding_months }} months. The 2024 changes removed indexation for most
assets and moved property to a flat rate — with a transitional option for
property acquired before 23 July 2024, where a resident individual may choose
between the new flat rate without indexation and the older rate with it,
whichever is lower.

Property also carries reinvestment reliefs — rolling gains into another
residential property, or into specified bonds within a window — that have no
equivalent in the fund world. These are genuinely complicated, the amounts
are large, and the deadlines are strict. This is a paragraph telling you the
reliefs exist, not a guide to using them; property sales are the clearest case
in this whole series for paying a professional.

## Unlisted shares

Long-term after {{ r.other_holding_months }} months. Relevant to anyone holding employee stock in an
unlisted company, or investing in startups — and note that the shares
becoming listed later doesn't retrospectively change how the earlier holding
period was counted.

## International funds

The trap here is the label. A fund investing in foreign equities is usually
**not** an "equity fund" for Indian tax purposes, because the 65% test refers
to Indian equity. So a US-focused fund typically does not get the 12-month
line or the {{ r.equity_ltcg_pct }}% rate, and is taxed under the other rules.

People are consistently surprised by this, because the fund holds nothing but
shares. The definition is about *where*, not *what*.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a sports club that gives a discount to members who play cricket.

You turn up saying you play baseball. It's a bat, a ball, throwing and
catching — surely close enough? The club says no: the discount is written for
cricket specifically.

Tax rules are written like that club's rulebook. "Equity fund" is a defined
term with a specific test, not a description of what the fund feels like. A
fund full of foreign shares can miss the definition completely.

</details>

## The whole picture

| Asset | Long-term after | Long-term rate |
|---|---|---|
| Listed shares, equity funds | {{ r.equity_holding_months }} months | {{ r.equity_ltcg_pct }}% above ₹{% include inr.html n=r.ltcg_annual_exemption %} |
| Debt funds bought from Apr 2023 | *No long-term category* | Slab rate |
| Gold ETFs and funds from Apr 2023 | *No long-term category* | Slab rate |
| Physical gold | {{ r.other_holding_months }} months | Flat rate, no indexation |
| Property | {{ r.other_holding_months }} months | Flat rate, transitional option for older purchases |
| Unlisted shares | {{ r.other_holding_months }} months | Flat rate |
| International funds | {{ r.other_holding_months }} months | Flat rate |
| Sovereign Gold Bonds at maturity | — | Exempt for individuals |

Plus {{ r.cess_pct }}% cess on the tax throughout.

## Common mistakes

- **Reading pre-2023 advice on debt funds.** Indexation on units bought from
  April 2023 does not exist. Check the date on anything you read.
- **Assuming all your debt units follow one rule.** Pre- and post-April-2023
  purchases are treated differently and can sit in the same folio.
- **Expecting international funds to be taxed as equity.** The 65% test is
  about Indian equity.
- **Selling Sovereign Gold Bonds early without checking.** Held to maturity
  the gain is exempt for individuals; sold on the exchange it isn't.
- **Treating property like a large mutual fund.** Different holding period,
  transitional options, reinvestment reliefs and strict deadlines.
- **Concluding debt funds are now pointless.** The rate advantage went; the
  deferral advantage over annually-taxed deposit interest did not.

**Takeaway:** Outside listed equity and equity funds, the concessional rates
mostly don't apply — and debt funds bought from April 2023 lost their
long-term category entirely, taxed at your slab rate however long you hold
them. Check the purchase date on debt units, check whether an "equity" fund
actually holds Indian equity, and treat property as its own subject with its
own professional.
