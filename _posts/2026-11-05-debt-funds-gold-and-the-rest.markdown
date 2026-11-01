---
layout: post
title: "Debt funds, gold and the rest: where the slab rate takes over"
seo_title: "Tax on debt funds and gold: where the slab rate applies"
description: "Where the concessional rates stop and your slab rate takes over. Debt fund units bought from April 2023, gold, property, and the end of indexation."
image: /assets/og/debt-funds-gold-and-the-rest.png
date: 2026-11-05 09:00:00 +0530
series: tax
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "August 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## Everything that isn't equity

The [last post]({% post_url 2026-11-04-equity-and-equity-funds %}) covered listed shares
and equity funds — specific rates, a 12-month line, an annual exemption.
Most other assets are treated differently, and debt funds changed the most.
This post covers **Tax Year 2026-27 (FY 2026-27)**; FY is *financial year*.

## Debt funds: the change that invalidated a decade of advice

**Gains on units of specified mutual funds acquired on or after 1 April 2023 are
taxed at your slab rate, whatever the holding period.** No long-term
category and no indexation.

"Specified" has a precise meaning. In the Income-tax Act, 2025 a specified
mutual fund is one that invests **more than 65%** of its money in debt and
money-market instruments — or a [fund of funds]({% post_url 2026-10-20-international-funds %}) that invests in such funds. In plain terms: a debt fund. The definition has been changed over the years and this post does not trace
that history, so check the current rule for a fund you hold.

*Indexation* meant adjusting your cost upward for inflation before computing
the gain. For debt funds it is gone for sales on or after 23 July 2024,
whenever the units were bought. For units acquired from April 2023 the
long-term category is also gone, so a debt fund's gain and a fixed deposit's
interest are both taxed at the slab rate. The *timing* differs: see below.

| | Debt fund bought before 1 Apr 2023 | Debt fund bought on/after 1 Apr 2023 |
|---|---|---|
| Long-term category | Yes, after 24 months (12 if listed, e.g. a debt ETF) | **None** |
| Long-term rate | 12.5%, as we read the current rules; check the current rule | **Your slab rate** |
| Indexation | **No** — gone for sales on or after 23 July 2024 | **No** |

**In practice**: units bought before that cut-off may still have a long-term
category, and a holding can contain both kinds. Your capital gains statement
should distinguish them.

**Timing.** A debt fund's gain is taxed when you redeem, while fixed deposit
interest is generally taxed as it accrues each year. The rate on the two can be
the same slab rate; the year in which the tax falls is not. That is a
description of mechanics, not a comparison of which product suits anyone.

## Gold

| Form | Treatment |
|---|---|
| Physical gold, jewellery | Long-term after {{ r.other_holding_months }} months |
| Gold ETFs (listed) | Long-term after {{ r.equity_holding_months }} months, taxed at the long-term rate; check the current rule |
| Gold funds of funds (unlisted) | Long-term after {{ r.other_holding_months }} months, taxed at the long-term rate; check the current rule |
| Sovereign Gold Bonds | Redeemed at maturity: capital gains exempt for individuals — from 1 April 2026, only if you subscribed at issue and held continuously |

**Gold funds and the "specified" label.** How gold ETFs and gold funds of funds are classified has changed over the last few years. The current definition (more than 65% debt) doesn't cover a gold fund, but this post doesn't trace the earlier rules; if you're reconciling an older return, check the rule that applied to the year of sale.

Sovereign Gold Bonds are worth a line of their own. Redeemed at maturity with
the RBI (Reserve Bank of India), the capital gain has long been exempt for
individual investors. Budget 2026 narrowed that: from 1 April 2026 the
exemption at redemption applies only to an original subscriber who holds the bond
until it matures (Memorandum to the Finance Bill, 2026, under Sources; that is the Bill's explanation, and the enacted Finance Act was not re-checked). The tax treatment of bonds bought on the exchange is not covered here.
Sold before maturity, normal capital gains rules apply. Same instrument,
different outcomes depending on how you got in and how you exit; check the current
rule.

## Property

Long-term after {{ r.other_holding_months }} months. The 2024 changes removed indexation for most
assets and moved property to a flat 12.5% — with a transitional option for
land or buildings acquired before 23 July 2024, where a resident individual or
HUF (Hindu undivided family) may pay the lower of 12.5% without indexation and
20% with it.

Property also carries reinvestment reliefs — rolling gains into another
residential property, or into specified bonds within a window — that have no
equivalent in the fund world. These are genuinely complicated, the amounts
are large, and the deadlines are strict. This is a paragraph saying the
reliefs exist, not a guide to them; property is outside what this series covers in detail.

## Unlisted shares

Long-term after {{ r.other_holding_months }} months. Relevant to anyone holding employee stock in an
unlisted company, or investing in startups. One wrinkle if the company later
lists: the holding-period line follows what the shares are *on the day you
sell*. Sell after listing and the {{ r.equity_holding_months }}-month line for listed shares applies,
counted from when you originally acquired them. Which rate and exemption then
apply can turn on further conditions for pre-IPO (initial public offering)
shares; check the current rule.

## International funds

The trap here is the label. A fund investing in foreign equities is usually
**not** an "equity fund" for Indian tax purposes, because the test counts
domestic listed equity. So a US-focused fund typically does not get the equity
rate or the annual exemption, and is taxed under the other rules: long-term after {{ r.equity_holding_months }} months for a
listed international ETF or {{ r.other_holding_months }} months for an unlisted fund of funds.
Rates and earlier-year rules for these funds are not traced here; check the current rule.

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
| Gold ETFs, international ETFs (listed) | {{ r.equity_holding_months }} months | Long-term rate; check the current rule |
| Gold and international funds of funds | {{ r.other_holding_months }} months | Flat rate |
| Physical gold | {{ r.other_holding_months }} months | Flat rate, no indexation |
| Property | {{ r.other_holding_months }} months | Flat rate, transitional option for older purchases |
| Unlisted shares | {{ r.other_holding_months }} months | Flat rate |
| Unlisted bonds and debentures; market-linked debentures | — | Slab rate (Act s.76(2)) |
| Sovereign Gold Bonds at maturity | — | Exempt for original subscribers held to maturity (from 1 Apr 2026, per the Bill's Memorandum) |

Plus {{ r.cess_pct }}% cess on the tax throughout.

## Common mistakes

- **Reading old advice on debt or gold funds.** Indexation on debt funds is
  gone for sales since 23 July 2024, and the "specified fund" definition has
  changed over time. Check the date on anything you read.
- **Assuming all your debt units follow one rule.** Pre- and post-April-2023
  purchases are treated differently and can sit in the same folio.
- **Expecting international funds to be taxed as equity.** The equity test
  counts Indian listed equity.
- **Treating property like a large mutual fund.** Different holding period,
  transitional options, reinvestment reliefs and strict deadlines.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.
- [RBI, FAQs on Sovereign Gold Bonds](https://www.rbi.org.in/commonman/English/Scripts/FAQs.aspx?Id=1658): RBI's FAQs on Sovereign Gold Bonds.

**Takeaway:** Outside listed equity and equity funds, the equity rates and exemption don't apply, and gains on specified debt fund units acquired from April 2023 are taxed at the slab rate however long they are held. Check the purchase date on debt units and whether a fund counts as "equity" for tax.
