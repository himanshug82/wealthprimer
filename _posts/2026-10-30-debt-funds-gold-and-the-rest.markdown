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

"Specified" has a precise meaning. From FY 2025-26 onward (Finance Act 2025),
a specified mutual fund is one that invests **more than 65%** of its money in
debt and money-market instruments — or a fund of funds that puts at least 65%
into such funds. In plain terms: a debt fund.

Before 1 April 2023, debt funds held over three years were taxed at 20% *with
indexation* — meaning your cost was adjusted upward for inflation before
computing the gain, which in a moderate-inflation environment could reduce
the taxable gain to almost nothing. That was the entire reason debt funds
were preferred over fixed deposits by anyone in a higher slab.

That advantage is gone for everyone. Indexation on debt funds ended for any
sale on or after 23 July 2024, whenever the units were bought. For units
bought from April 2023, the long-term category went too, so a debt fund and a
fixed deposit are now taxed broadly alike — at your slab rate.

| | Debt fund bought before 1 Apr 2023 | Debt fund bought on/after 1 Apr 2023 |
|---|---|---|
| Long-term category | Yes, after 24 months (12 if listed, e.g. a debt ETF) | **None** |
| Long-term rate | 12.5% flat | **Your slab rate** |
| Indexation | **No** — gone for sales on or after 23 July 2024 | **No** |

**The practical consequence**: if you hold debt fund units bought before that
cut-off, they still have a long-term category — but a sale today is taxed at
12.5% without indexation, not the old 20% with it. Your holding may contain
both kinds. Your capital gains statement should distinguish them; if it doesn't,
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
| Gold ETFs (listed) | Long-term after {{ r.equity_holding_months }} months, taxed at 12.5% |
| Gold funds of funds (unlisted) | Long-term after {{ r.other_holding_months }} months, taxed at 12.5% |
| Sovereign Gold Bonds | Redeemed at maturity: capital gains exempt for individuals — from 1 April 2026, only if you subscribed at issue and held continuously |

**Why gold funds aren't on the slab rate any more.** Until 31 March 2025 the
test for a "specified" fund was different — not more than 35% in Indian
equity — and that swept in gold ETFs, gold funds of funds, international funds
and many hybrids along with debt funds. The Finance Act 2025 narrowed it to
funds that are more than 65% debt, so from 1 April 2025 gold funds get a
long-term category again. If you're reconciling an older return: gold fund
units bought after 1 April 2023 and sold before 1 April 2025 were taxed at
your slab rate.

Sovereign Gold Bonds are worth a line of their own. Redeemed at maturity with
the RBI (Reserve Bank of India), the capital gain has long been exempt for
individual investors. Budget 2026 narrowed that: from 1 April 2026 the
exemption at redemption applies only if you subscribed at the original issue
and held the bond continuously until it matured (Finance Act 2026, as
summarised by the National Institute of Securities Markets and others). Bonds
bought on the exchange no longer get it at maturity — the gain is taxed as a
long-term gain at 12.5%. Sell before maturity and
normal capital gains rules apply either way. Same instrument, very different
tax outcomes depending on how you got in and how you exit; check the current
rule before relying on the exemption.

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
unlisted company, or investing in startups. One wrinkle if the company later
lists: the holding-period line follows what the shares are *on the day you
sell*. Sell after listing and the {{ r.equity_holding_months }}-month line for listed shares applies,
counted from when you originally acquired them. Which rate and exemption then
apply can turn on further conditions, so pre-IPO (initial public offering)
shares are worth a professional's check.

## International funds

The trap here is the label. A fund investing in foreign equities is usually
**not** an "equity fund" for Indian tax purposes, because the 65% test refers
to Indian equity. So a US-focused fund typically does not get the equity
rate or the annual exemption, and is taxed under the other rules.
From FY 2025-26 onward that means 12.5% long-term, after {{ r.equity_holding_months }} months for a
listed international ETF or {{ r.other_holding_months }} months for an unlisted fund of funds.
(Units bought after 1 April 2023 and sold before 1 April 2025 were taxed at
slab — the same old "specified fund" test that caught gold funds.)

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
| Debt funds bought before Apr 2023 | {{ r.other_holding_months }} months ({{ r.equity_holding_months }} if listed) | Flat rate, no indexation |
| Gold ETFs, international ETFs (listed) | {{ r.equity_holding_months }} months | Flat rate |
| Gold and international funds of funds | {{ r.other_holding_months }} months | Flat rate |
| Physical gold | {{ r.other_holding_months }} months | Flat rate, no indexation |
| Property | {{ r.other_holding_months }} months | Flat rate, transitional option for older purchases |
| Unlisted shares | {{ r.other_holding_months }} months | Flat rate |
| Sovereign Gold Bonds at maturity | — | Exempt for individuals who subscribed at issue and held throughout (from 1 Apr 2026) |

Plus {{ r.cess_pct }}% cess on the tax throughout.

## Common mistakes

- **Reading old advice on debt or gold funds.** Indexation on debt funds is
  gone for any sale since 23 July 2024, whenever you bought. And advice from
  2023–24 that gold and international funds are slab-rate forever is out of
  date from FY 2025-26. Check the date on anything you read.
- **Assuming all your debt units follow one rule.** Pre- and post-April-2023
  purchases are treated differently and can sit in the same folio.
- **Expecting international funds to be taxed as equity.** The 65% test is
  about Indian equity.
- **Selling Sovereign Gold Bonds early without checking.** Held to maturity
  from the original issue, the gain is exempt for individuals; sold on the
  exchange it isn't — and from 1 April 2026, bonds *bought* on the exchange
  don't get the exemption at maturity either.
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
