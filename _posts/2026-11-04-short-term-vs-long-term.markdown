---
layout: post
title: "STCG vs LTCG: the holding period that changes your tax rate"
description: "Twelve months for listed equity, twenty-four for most other assets, as we read the Act. How the holding period is counted, and why a day changes the rate."
image: /assets/og/short-term-vs-long-term.png
date: 2026-11-04 09:00:00 +0530
series: tax
term: "STCG and LTCG (capital gains)"
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## One line, two very different outcomes

The [last post]({% post_url 2026-11-02-how-investment-income-is-taxed %}) said the holding
period decides most of what happens to a capital gain. This post is about
exactly where that line sits and how it's counted, because the difference
either side of it is large and entirely mechanical. Everything here is for
**Tax Year 2026-27 (FY 2026-27)**; FY is *financial year*, and STCG and LTCG are
short-term and long-term capital gains.

For listed equity and equity mutual funds:

| Held for | Classified as | Rate |
|---|---|---:|
| {{ r.equity_holding_months }} months or less | Short-term | **{{ r.equity_stcg_pct }}%** |
| More than {{ r.equity_holding_months }} months | Long-term | **{{ r.equity_ltcg_pct }}%** above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year |

These rates are in the Income-tax Act, 2025 (sections 196 and 198), and the Finance Act, 2026 did not change them. Cess and any surcharge are extra.

Sold at exactly 12 months, a ₹5,00,000 gain is short-term and taxed at {{ r.equity_stcg_pct }}% — ₹1,00,000. Sold just over 12 months, the first ₹{% include inr.html n=r.ltcg_annual_exemption %} is exempt and the rest is taxed at {{ r.equity_ltcg_pct }}%, which
comes to ₹46,875. Same investment, same gain, a day or so apart, and less than
half the tax. The rest of this post is about how that line is drawn.

## The two holding periods, Tax Year 2026-27

The line isn't in the same place for everything:

| Asset | Long-term after |
|---|---|
| Listed shares (NSE, the National Stock Exchange, or BSE, the Bombay Stock Exchange) | {{ r.equity_holding_months }} months |
| Equity mutual funds (the equity-oriented test below) | {{ r.equity_holding_months }} months |
| Listed bonds and debentures (market-linked debentures are the exception: always short-term) | {{ r.equity_holding_months }} months |
| Unlisted shares | {{ r.other_holding_months }} months |
| Property (land, buildings) | {{ r.other_holding_months }} months |
| Listed gold ETFs | {{ r.equity_holding_months }} months |
| Physical gold, jewellery; unlisted gold funds of funds | {{ r.other_holding_months }} months |
| Specified debt funds, units bought on or after 1 April 2023 | *No long-term rate at all — slab rate always* |

The gold rows show listed gold [ETFs (exchange-traded funds)]({% post_url 2026-10-13-index-funds-vs-etfs %}) at {{ r.equity_holding_months }} months and gold [funds of funds]({% post_url 2026-10-20-international-funds %}) at {{ r.other_holding_months }}. Those lines follow from the Act's wording as we read it: a listed security gets twelve months, and an unlisted fund unit falls to the general twenty-four. How gold funds were classified changed in recent years, so an older sale may have followed different rules.

Two things worth noting.

**"Equity fund" has a definition.** For tax, a fund qualifies as equity-oriented
only if at least 65% of its money is in equity shares of domestic listed companies. A fund that invests through another listed fund has a stricter test: 90% in that fund, which must itself hold 90% in such shares (section 198(8) of the Act). Some funds you'd
assume are equity funds — certain international funds, some hybrids, funds of
funds — may not meet it and then fall under the other rules. The
factsheet tells you; [the post on reading one]({% post_url 2026-10-11-reading-a-factsheet %}) covers where
to look.

**That last row is not an oversight.** For specified debt funds the gain is taxed at the slab rate whatever the holding period. The debt funds post in this series covers the definition.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a shop that gives you a discount for being a loyal customer — but
only once you've been a member for a full year.

Buy something on day 364 of your membership and you pay full price. Buy the
same thing on day 366 and you get the discount. Nothing about the item
changed. Nothing about you changed. Only the date did.

Tax on investments works the same way: the rate depends on a date, not on
anything about the investment.

</details>

## How the period is counted

Three rules that catch people out.

**Count from the date of acquisition to the date of transfer.** Not from when
the money left your account, and not from the financial year. For a mutual fund purchase the date that matters is generally the date units were
allotted, which can differ from the date you placed the order; check your statement.

**"More than 12 months" means more than.** Exactly twelve months is not
long-term. Someone who bought on 15 March 2025 crosses the line only after
15 March 2026.

**Each purchase has its own clock.** This is the one that matters most in
practice. Buy the same fund in five separate transactions and you hold five
lots with five different acquisition dates. Redeeming "the fund" redeems
specific lots, each classified on its own. That's the subject of
the FIFO (first in, first out) post in this series, and it's why a single SIP
(systematic investment plan) redemption can produce both long-term and short-term gains at once.

## Worked example: one day either side

The numbers here are round and illustrative, not taken from a real fund's
history. Suppose a ₹5,00,000 investment in an equity fund gained ₹5,00,000 —
a clean doubling — and compare selling just before and just after the twelve-month mark. Assumptions: no other long-term equity gains in the year, so the full exemption is available, and surcharge is excluded (it can change the answer at high incomes):

| | Sold at 12 months | Sold at 12 months + 1 day |
|---|---:|---:|
| Gain | ₹5,00,000 | ₹5,00,000 |
| Classified as | Short-term | Long-term |
| Exempt | — | ₹{% include inr.html n=r.ltcg_annual_exemption %} |
| Taxable | ₹5,00,000 | ₹3,75,000 |
| Rate | {{ r.equity_stcg_pct }}% | {{ r.equity_ltcg_pct }}% |
| Tax | ₹1,00,000 | ₹46,875 |
| Plus {{ r.cess_pct }}% cess | ₹1,04,000 | ₹48,750 |
| **Difference in tax** | | **₹55,250 lower** |

The same gain carries ₹55,250 less tax on the right-hand side. That is a
mechanical comparison, not a reason to hold or sell: the price can move
between the two dates by far more than the tax difference, in either direction.

## Common mistakes

- **Applying the 12-month rule to everything.** Physical gold and property
  need {{ r.other_holding_months }} months. Getting this wrong on a property sale changes the tax.
- **Assuming any equity-sounding fund gets equity treatment.** A minimum-share test in the Act decides it, not the fund's name.
- **Counting from the wrong date.** Allotment to transfer, not
  financial-year boundaries, and not the date you placed the order.
- **Treating "12 months" as inclusive.** The test is *more than* twelve months, and each purchase has its own clock: one holding is many lots.

## Sources

- [Income-tax Act, 2025 (a copy hosted by the Institute of Chartered Accountants of India, ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself, as read in that copy. Points not found there are marked "check the current rule".
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the amendments and the rates for Tax Year 2026-27.

**Takeaway:** For listed equity and equity funds the line between short-term and long-term gains is 12 months, and for most other assets 24, counted from allotment or purchase to transfer and needing to be *more than*, not equal to. Each purchase carries its own clock, so one holding can contain both kinds of lot.
