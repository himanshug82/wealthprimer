---
layout: post
title: "Gold ETFs vs gold fund of funds: the same metal, two wrappers"
seo_title: "Gold ETF vs gold fund of funds: how each works"
description: "A gold ETF trades on the exchange; a gold fund of funds is a mutual fund that buys one. How each works, what each layer costs, and UTI's two compared."
image: /assets/og/gold-silver-etfs-and-fofs.png
date: 2027-04-16 09:00:00 +0530
series: mutual-funds
term: "Gold ETF vs gold fund of funds"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign g = site.data.mf5.gold %}

## Two ways to hold the same gold

A **gold ETF** (exchange-traded fund) is a fund whose units track the price
of gold and trade on the stock exchange like a share: they are bought through
a broker into a demat account (the electronic account that holds securities),
at the market price during the day. A **gold
fund of funds** (FoF) is an ordinary mutual fund that puts its money into a
gold ETF. Its units come from the fund house at the day's NAV (net asset
value), with no demat account, and you can set up a SIP (systematic
investment plan) like any other fund.

Silver ETFs and silver funds of funds work the same way, with silver
underneath. This post compares the two wrappers, not the metals: nothing
here is a view on gold or silver. It's part of
[Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).
The [index funds vs ETFs post]({% post_url 2026-10-13-index-funds-vs-etfs %})
covers the same trade-off for equity.

## How the costs stack up

```
Gold ETF:         your return  ≈  gold's return  −  the ETF's expenses
                                  − brokerage and the bid-ask spread when you trade
                                  ± any gap between the ETF's market price and its NAV

Gold FoF:         your return  ≈  the ETF's return (at the price the FoF pays)
                                  −  the FoF's own expenses
```

The ETF's NAV is already net of the ETF's own costs. The FoF's NAV is net of
the FoF's costs too, on top of whatever is inside the ETF it holds. So the
FoF is a second layer: convenience (no demat, SIPs, no brokerage) in
exchange for a second expense ratio. The
[expense ratio post]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %})
shows how a yearly cost compounds.

## Worked example: UTI's gold ETF and its fund of funds

Two real series from AMFI (the Association of Mutual Funds in India), via
mfapi.in: the [UTI Gold ETF]({{ g.etf_url }}) and the
[UTI Gold ETF Fund of Fund]({{ g.fof_url }}) (regular and direct plans),
which invests in it. Neither is a recommendation; they share a fund house,
which keeps the comparison simple. From {{ g.start }}, a month after the
FoF's first NAV, to {{ g.end }}: {{ g.years }} years, past data, pre-tax, for
illustration only. The ETF's NAV was adjusted for a unit split in March 2021,
before this window.

| {{ g.start }} to {{ g.end }} | Return a year | ₹1 lakh became (₹) |
|---|---:|---:|
| Gold ETF, at NAV | {{ g.etf.cagr_pct }}% | {{ g.etf.lakh_became }} |
| Gold FoF, regular plan | {{ g.fof_regular.cagr_pct }}% | {{ g.fof_regular.lakh_became }} |
| Gold FoF, direct plan | {{ g.fof_direct.cagr_pct }}% | {{ g.fof_direct.lakh_became }} |

What the table shows, and doesn't:

1. **Regular against direct is a clean comparison.** The two plans hold the
   same portfolio; only their expenses differ. The regular plan trailed the
   direct plan by {{ g.fof_direct.cagr_pct | minus: g.fof_regular.cagr_pct | round: 2 }}
   percentage points a year, which reflects the regular plan's extra cost,
   its distribution commission. With returns this high, the gap in returns
   is a little larger than the gap in yearly costs.
2. **FoF against the ETF's NAV is not a clean comparison.** To this end date
   the direct FoF ran {{ g.gap_direct_pp | abs }} points a year *ahead* of the
   ETF's NAV. Costs and any cash the FoF held could only have held it back,
   so the lead has to come from pricing: SEBI's rules value a FoF's ETF units
   at the ETF's closing price on the exchange (master circular, paragraph
   3.6.4.1), and that price can sit above or below the ETF's NAV. The lead
   also depends on the end date, as the table below shows.
3. **Neither row includes trading costs.** An ETF investor also pays
   brokerage and the bid-ask spread on each trade; the FoF investor doesn't.
   How much that matters depends on how often and how much you trade.

Same start, different end dates: the ETF's NAV return minus the direct
FoF's, a year. A negative number means the FoF was ahead.

| Ending | ETF minus direct FoF |
|---|---:|
{% for x in g.sensitivity -%}
| {{ x.end }} | {{ x.gap_pp | replace: "-", "−" }} points |
{% endfor %}

A week before the end, the ETF's NAV was ahead. The sign comes from where
the window happens to end, not from a steady pattern.

The return itself reflects gold's price over these particular
{{ g.years }} years. It says nothing about any other period.

## Common mistakes

1. **Comparing wrappers on one period's returns.** Two products holding the
   same metal should differ by costs and pricing quirks, not by much else.
   A large gap in a table usually comes from different dates, a price-vs-NAV
   gap or a data issue.
2. **Ignoring the ETF's market price.** An ETF bought at a premium to its NAV
   starts behind; one sold at a discount ends behind. The exchange shows both
   the price and the NAV.
3. **Forgetting the second expense ratio.** The FoF's convenience has a
   yearly cost on top of the ETF's. Over a long holding period it compounds.
4. **Assuming the tax is the same as for shares.** Gold ETFs and gold FoFs are
   taxed under their own rules, which the
   [debt funds, gold and the rest post]({% post_url 2026-11-28-debt-funds-gold-and-the-rest %})
   covers.

**Takeaway:** A gold ETF and a gold fund of funds hold the same gold in two
wrappers: the ETF trades on the exchange and needs a demat account; the FoF
buys the ETF for you, at the price of a second expense ratio. Compare them on
costs and convenience, not on one period's returns.

## Sources

- SEBI Master Circular for Mutual Funds, 27 June 2024, paragraph 3.6.4.1 (valuation of ETF units held by a fund of funds) ([SEBI]({{ site.data.mf5.cutoff.master_circular_url }})), read on 21 November 2026.
- NAVs: AMFI via mfapi.in ([ETF]({{ g.etf_url }}), [FoF]({{ g.fof_url }})); our copies: [ETF]({{ g.csv_etf | relative_url }}), [FoF]({{ g.csv_fof | relative_url }}).
