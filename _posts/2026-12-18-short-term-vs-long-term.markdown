---
layout: post
title: "Short-term vs long-term: the date that changes the rate"
date: 2026-12-18 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice.*

## One line, two very different outcomes

The [last post]({% post_url 2026-12-16-how-investment-income-is-taxed %}) said the holding
period decides most of what happens to a capital gain. This post is about
exactly where that line sits and how it's counted, because the difference
either side of it is large and entirely mechanical.

For listed equity and equity mutual funds:

| Held for | Classified as | Rate |
|---|---|---:|
| {{ r.equity_holding_months }} months or less | Short-term | **{{ r.equity_stcg_pct }}%** |
| More than {{ r.equity_holding_months }} months | Long-term | **{{ r.equity_ltcg_pct }}%** above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year |

Sell on day 365 and a ₹5,00,000 gain is taxed at {{ r.equity_stcg_pct }}% — ₹1,00,000. Sell on
day 366 and the first ₹{% include inr.html n=r.ltcg_annual_exemption %} is exempt and the rest is taxed at {{ r.equity_ltcg_pct }}%, which
comes to ₹46,875. Same investment, same gain, one day apart, and less than
half the tax.

That gap is the single largest piece of tax arithmetic available to an
ordinary investor, and it requires nothing except knowing the date you
bought.

## The two holding periods

The line isn't in the same place for everything:

| Asset | Long-term after |
|---|---|
| Listed shares (NSE/BSE) | {{ r.equity_holding_months }} months |
| Equity mutual funds (≥65% in Indian equity) | {{ r.equity_holding_months }} months |
| Listed bonds and debentures | {{ r.equity_holding_months }} months |
| Unlisted shares | {{ r.other_holding_months }} months |
| Property (land, buildings) | {{ r.other_holding_months }} months |
| Gold, jewellery, gold funds | {{ r.other_holding_months }} months |
| Specified debt funds bought on/after 1 Apr 2023 | *No long-term rate at all — slab rate always* |

Two things worth noting.

**"Equity fund" has a definition.** A fund qualifies for equity treatment
only if it holds at least 65% in Indian equity. Some funds you'd assume are
equity funds — certain international funds, some hybrids, funds of funds —
don't clear that bar and are taxed under the other rules entirely. The
factsheet tells you; [the post on reading one]({% post_url 2026-12-14-reading-a-factsheet %}) covers where
to look.

**That last row is not an oversight.** Debt funds bought from April 2023
have no long-term category. Holding them for a decade earns no rate benefit.
That's post four in this series.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a shop that gives you a discount for being a loyal customer — but
only once you've been a member for a full year.

Buy something on day 364 of your membership and you pay full price. Buy the
same thing on day 366 and you get the discount. Nothing about the item
changed. Nothing about you changed. Only the date did.

Tax on investments works the same way, and the discount is big. The only
skill involved is checking your membership date before you buy.

</details>

## How the period is counted

Three rules that catch people out.

**Count from the date of acquisition to the date of transfer.** Not from when
the money left your account, and not from the financial year. The unit
allotment date is what counts, which for a mutual fund purchase is the date
units were allotted, not necessarily the date you clicked buy.

**"More than 12 months" means more than.** Exactly twelve months is not
long-term. If you bought on 15 March 2025, the gain becomes long-term on
16 March 2026, not 15 March.

**Each purchase has its own clock.** This is the one that matters most in
practice. Buy the same fund in five separate transactions and you hold five
lots with five different acquisition dates. Redeeming "the fund" redeems
specific lots, each classified on its own. That's the entire subject of
the FIFO post later in this series, and it's why a single SIP
redemption can produce both long-term and short-term gains at once.

## Worked example: one day either side

Take the real fund used throughout this blog. Suppose a ₹5,00,000 investment
gained ₹5,00,000 — a clean doubling — and compare selling just before and
just after the twelve-month mark:

| | Sold at 12 months | Sold at 12 months + 1 day |
|---|---:|---:|
| Gain | ₹5,00,000 | ₹5,00,000 |
| Classified as | Short-term | Long-term |
| Exempt | — | ₹{% include inr.html n=r.ltcg_annual_exemption %} |
| Taxable | ₹5,00,000 | ₹3,75,000 |
| Rate | {{ r.equity_stcg_pct }}% | {{ r.equity_ltcg_pct }}% |
| Tax | ₹1,00,000 | ₹46,875 |
| Plus {{ r.cess_pct }}% cess | ₹1,04,000 | ₹48,750 |
| **Difference** | | **₹55,250 saved** |

A day's patience, on a single transaction, worth ₹55,250.

Now the honest caveat, because this is where tax thinking goes wrong.
Holding an investment you want to sell purely to cross a tax line is a bet
that the price won't fall more than the tax you'd save. Here the tax saving
is about 11% of the gain. If the holding drops 15% while you wait, you've
paid more for the tax saving than it was worth. The tax tail should not wag
the investment dog — but when the decision is genuinely marginal, and the
date is close, it's free money to check.

## Common mistakes

- **Applying the 12-month rule to everything.** Gold and property need
  {{ r.other_holding_months }} months. Getting this wrong on a property sale is expensive.
- **Assuming any equity-sounding fund gets equity treatment.** The 65%
  Indian-equity test decides it, not the fund's name.
- **Counting from the wrong date.** Allotment to transfer, not
  financial-year boundaries, and not the date you placed the order.
- **Treating "12 months" as inclusive.** You need *more than* twelve months.
- **Forgetting each purchase has its own clock.** One holding is many lots.
- **Holding a deteriorating investment for the tax rate.** The saving is
  roughly 11% of the gain on equity. A larger price fall wipes it out.

**Takeaway:** The holding period is the single most consequential fact about
a capital gain — twelve months for listed equity and equity funds,
twenty-four for most other assets, counted from allotment and needing to be
*more than*, not equal to. On equity the difference is worth roughly 11% of
the gain, which is worth a calendar check before you sell and never worth
holding something you've decided to be rid of.
