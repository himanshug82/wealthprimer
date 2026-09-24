---
layout: post
title: "Index funds vs ETFs: same fifty stocks, two wrappers"
description: "An index fund and an ETF on the Nifty 50 hold the same shares; what differs is buying at NAV or at market price — and the traps: iNAV, spreads, splits, payouts."
image: /assets/og/index-funds-vs-etfs.png
date: 2026-12-09 09:00:00 +0530
series: mutual-funds
term: "ETF (exchange-traded fund)"
---

{% assign m = site.data.mf2 %}
{% assign e = m.etf_vs_index_fund %}
{% assign f = e.funds %}
{% assign split = m.discontinuities.etf_split %}
{% assign pay = m.discontinuities.etf_payouts[0] %}
{% assign td = e.avg_tracking_difference_pp %}
{% assign te = e.tracking_error_pct %}

## The portfolio is identical. The wrapper isn't.

An **ETF — Exchange-Traded Fund** — is a mutual fund whose units are listed on
a stock exchange. An index fund and an ETF tracking the Nifty 50 both hold the
same fifty companies in the same proportions. If you looked only at what's
inside, you couldn't tell them apart.

The difference is entirely in how you get in and out:

| | Index fund | ETF |
|---|---|---|
| Where you buy | From the fund house (directly or via a platform) | On the NSE/BSE, from another investor, like a share |
| Price you pay | That day's **NAV**, whatever it turns out to be | The **market price** at the moment you trade |
| Minimum | Often ₹100–₹500 | One unit (a few hundred rupees for a Nifty ETF) |
| Account needed | Folio with the fund house | Demat + trading account |
| Costs | Expense ratio only | Expense ratio (usually lower) **plus** brokerage, bid-ask spread, demat charges |
| SIP | Native | Only if your broker builds one for you |
| Dividends | Growth plan reinvests automatically | Some ETFs **pay out** occasionally (this one did once, in February 2021); you get cash, with no growth-plan option to reinvest |

The [first post in this series]({% post_url 2026-10-18-what-a-mutual-fund-is %})
explained that NAV is what one unit's share of the portfolio is worth. For an
index fund, that *is* your price. For an ETF, NAV is what the unit is worth —
but the price is whatever the last buyer and seller agreed on, which can sit
above or below it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a big jar of fifty different sweets, and two ways to own a scoop of it.

Way one: you give the jar's owner your money at the end of the day, and they
hand you exactly what a scoop is worth at closing time. No haggling.

Way two: the scoops are printed as tokens, and people trade the tokens with
each other all day in the playground. Most of the time a token sells for about
what a scoop is worth. But if lots of kids suddenly want tokens and nobody's
selling, you might pay more than a scoop is worth. If nobody wants them, you
might sell for less. The sweets in the jar didn't change. The price of the
token did.

</details>

## iNAV: the number that keeps the price honest

Because an ETF trades all day while NAV is computed once at the close, the
exchange publishes an **iNAV — indicative NAV** — every few seconds, computed
from the live prices of the fifty underlying stocks. It's what a unit is worth
*right now*.

```
Premium / discount  =  (Market price − iNAV) / iNAV
```

For a large, liquid Nifty 50 ETF this is usually a few basis points either way.
Large institutions called *authorised participants* keep it there: if the
price drifts above iNAV, they create new units from the underlying shares and
sell them; if it drifts below, they buy units and redeem them for the shares.
The arbitrage is what tethers price to value.

The tether can fray. Thin ETFs — small ones, or ones tracking less liquid
indices — can trade several percent away from iNAV for hours, and a market
order placed in a hurry will happily fill at that price. Rule for ETF orders:
**look at the iNAV, and use a limit order.** There is no equivalent risk in an
index fund, because there is no price other than NAV.

## The data: same index, three wrappers

UTI runs both a Nifty 50 index fund and a Nifty 50 ETF. Here is ₹100 in each
from {{ e.window_start }} (the ETF's first NAV) to {{ e.window_end }}, {{ e.years }} years, alongside
the Nifty 50 price index. Source: {{ m.sources.label }}, codes
{{ m.sources.etf.code }}, {{ m.sources.index_fund.regular_code }} and {{ m.sources.index_fund.direct_code }}; index from
Yahoo Finance. Historical data, for illustration only — this is about how the
wrappers behave, not about either product's merits.

![Growth of ₹100 in a Nifty 50 ETF, the same fund house's index fund (direct and regular), and the price index]({{ '/assets/charts/mf2-etf-vs-index-fund.svg' | relative_url }})

| | Annualised return | ₹100 became |
|---|---:|---:|
| {{ f.nifty_pri.name }} | {{ f.nifty_pri.cagr_pct }}% | ₹{{ f.nifty_pri.growth_of_100 }} |
| {{ f.index_fund_regular.name }} | {{ f.index_fund_regular.cagr_pct }}% | ₹{{ f.index_fund_regular.growth_of_100 }} |
| {{ f.index_fund_direct.name }} | {{ f.index_fund_direct.cagr_pct }}% | ₹{{ f.index_fund_direct.growth_of_100 }} |
| {{ f.etf.name }} | {{ f.etf.cagr_pct }}% | ₹{{ f.etf.growth_of_100 }} |

Two things to notice, and one big caveat.

First, all three fund lines sit **above** the price index, by about a
percentage point a year. That is not skill — it's dividends. The
[benchmarks post]({% post_url 2026-10-25-benchmarks-and-comparing-like-with-like %})
explained that the price index excludes the dividends the fifty companies pay,
while the funds receive them. Measured against the total-return index, all
three would sit slightly *below* it, by roughly their costs.

Second, the ordering: ETF, then direct plan, then regular plan. Year by year:

| Year | ETF − index | Direct − index | Regular − index |
|---|---:|---:|---:|{% for y in e.calendar_years %}
| {{ y.year }} | {{ y.etf_minus_pri_pp }} pp | {{ y.direct_minus_pri_pp }} pp | {{ y.regular_minus_pri_pp }} pp |{% endfor %}
| **Average** | **{{ td.etf_minus_pri_pp }} pp** | **{{ td.direct_minus_pri_pp }} pp** | **{{ td.regular_minus_pri_pp }} pp** |

The gap between the columns is the cost difference between the wrappers — the
[tracking difference]({% post_url 2026-11-28-tracking-error-and-tracking-difference %}),
which is what an index product's expense ratio actually costs you. The ETF's
lower expense ratio shows up as a consistently larger dividend-plus-cost gap
over the index.

**The caveat**: the ETF's line is its *NAV*, adjusted for two events described
below. It is what a unit was worth — not what you could have bought or sold
one for. Brokerage, the bid-ask spread and any premium or discount to iNAV all
come off the ETF's number and none of them come off the index fund's. No
market-price series is used here, because there isn't a reliable free one;
so this comparison flatters the ETF by exactly the amount of those frictions.

## Two things that happened to the ETF's NAV, and what they teach

The raw NAV series for this ETF contains two jumps that are not market moves,
and both are lessons in reading an ETF's history.

**A 1:10 unit split, {{ split.date }}.** The NAV went from ₹{% include inr.html n=split.nav_before %} to
₹{{ split.nav_after }} overnight. Nobody lost anything: each unit became ten, and each
was worth a tenth. Fund houses do this to make one unit affordable — a ₹2,000
unit is awkward for someone investing ₹500 a month. The
[face value and splits post]({% post_url 2026-12-06-face-value-splits-and-bonuses %})
covers the same idea for shares. If you download NAV history and don't correct
for it, every return you compute across that date is wrong by a factor of ten.

**A payout, {{ pay.ex_date }}.** The Nifty rose that day; the ETF's NAV fell by
{{ pay.nav_gap_vs_index_pct | abs }}% relative to it — from ₹{% include inr.html n=pay.nav_before %} to ₹{% include inr.html n=pay.nav_after %} per
unit — because the fund distributed roughly ₹{{ pay.estimated_payout_per_unit }} a unit to holders.
That cash landed in investors' bank accounts, not in the NAV. An index fund's
growth plan would have reinvested it silently. So an ETF-vs-index-fund
comparison on raw NAV understates the ETF by the payout; the ETF line above
assumes the payout was reinvested, which is the only fair basis.

Both events are routine. Both quietly break any spreadsheet that hasn't been
told about them.

## Which wrapper, then?

Not a recommendation — a checklist of which *frictions* apply to you:

- You invest small amounts monthly and want it automatic → the index fund's
  native SIP is the path of least resistance.
- You already run a demat account, trade in larger lumps, and will use limit
  orders against iNAV → the ETF's lower expense ratio can outweigh the
  trading costs.
- You want dividends reinvested without thinking → growth-plan index fund.
- You are buying something *other* than a large, liquid Nifty/Sensex ETF →
  check the traded volume and the premium/discount history first. Thin ETFs
  are where the wrapper bites.

## Common mistakes

- **Market orders on an ETF.** You get whatever price is on the screen, which
  in a thin ETF can be several percent from iNAV. Limit orders, always.
- **Comparing ETF NAV returns with index fund returns and calling it a
  verdict.** NAV ignores the spread and brokerage you actually pay on the ETF.
- **Not correcting for splits.** A 1:10 split looks like a 90% crash in a raw
  NAV download.
- **Forgetting an ETF may pay out.** The cash arrives in your bank account and
  is taxed as dividend income in the year received — see the
  [dividends and interest post]({% post_url 2026-10-31-dividends-and-interest %}).
  A growth-plan index fund defers all of that until you sell.
- **Assuming "ETF" means "index".** Most Indian ETFs are passive, but the
  wrapper and the strategy are separate choices. Read the scheme document.

**Takeaway:** An index fund and an ETF on the same index own the same stocks;
the difference is that one sells you units at NAV and the other lets you trade
them at a price. Over ten years the ETF's lower cost showed up as about a
quarter of a percentage point a year — before the brokerage, spread and iNAV
gap that only the ETF buyer pays. Choose the wrapper for the frictions that
apply to you, not for the portfolio, which is identical.
