---
layout: post
title: "Circuit limits: why a stock can be 'locked' at upper circuit, and when the whole market stops"
description: "Price bands cap how far a stock can move in a day; market-wide circuit breakers halt everything. How NSE's 2/5/10/20% bands and the index triggers work."
image: /assets/og/circuit-limits-and-price-bands.png
date: 2026-10-15 09:00:00 +0530
series: jargon
term: "Circuit limit (price band)"
---

{% assign c = site.data.jargon_m7.circuit %}
{% assign m = c.march_2020["2020-03-23"] %}
{% assign ipo_cr = site.data.case_study.listing.ipo_proceeds | divided_by: 100 %}
{% assign base_date = c.mwcb_base_date | date: "%-d %B %Y" %}

## What a circuit limit is

A **price band** — in everyday speech a **circuit limit** or **circuit
filter** — is the furthest a stock's price is allowed to move from the
previous day's close in a single session. On the NSE and BSE the bands come
in fixed sizes: 2%, 5%, 10% or 20% either way, with the exchange publishing
each stock's band daily ([NSE, price bands](https://www.nseindia.com/static/products-services/equity-market-price-bands);
[daily list](https://www.nseindia.com/regulations/daily-price-bands-reports)).
SEBI (the Securities and Exchange Board of India) allows "individual scrip
wise price bands up to 20% either way" for stocks without derivatives
([SEBI Master Circular for Stock Exchanges and Clearing Corporations,
SEBI/HO/MRD2/PoD-2/CIR/P/2023/171, 16 October 2023](https://www.sebi.gov.in/sebi_data/commondocs/oct-2023/Chapter-1-Trading_p.pdf), para 2.3.1).

When a stock hits the top of its band it is at **upper circuit**; at the
bottom, **lower circuit**. Trading doesn't stop. Orders simply can't be
placed outside the band. So a stock at upper circuit usually shows a long
queue of buyers at the limit price and no sellers — it's "locked", and a buy
order may sit there all day unfilled.

Stocks that have futures and options (F&O) trading work differently. They
have no fixed band, only a **dynamic** one: it starts at 10% of the previous
close and can be widened ("flexed") during the day if trades keep hitting
it. Since SEBI's [circular of 24 May 2024](https://www.sebi.gov.in/legal/circulars/may-2024/enhancement-of-dynamic-price-bands-for-scrips-in-the-derivatives-segment_83574.html)
(SEBI/HO/MRD/TPD-1/P/CIR/2024/58), the flexes come in steps of 5%, then 3%,
then 2%, with cooling-off periods in between, and the band *slides* rather
than just widening — the lower limit moves up when the upper one is flexed.
NSE put the sliding part live from 18 November 2024
([NSE/FAOP/64995](https://nsearchives.nseindia.com/content/circulars/FAOP64995.pdf), 8 November 2024).
Britannia is an F&O stock, so it has no fixed circuit.

Then there's a second, bigger switch. A **market-wide circuit breaker
(MWCB)** halts *all* equity and equity-derivative trading across the country
when the Nifty 50 or the Sensex, whichever gets there first, falls or rises
10%, 15% or 20% from its previous close ([SEBI CIR/MRD/DP/25/2013, 3 September
2013](https://www.sebi.gov.in/legal/circulars/sep-2013/index-based-market-wide-circuit-breaker-mechanism_25303.html)).

## The rule

```
Upper circuit = Previous close × (1 + band)
Lower circuit = Previous close × (1 − band)
                (rounded to the tick size by the exchange)

MWCB trigger levels = Previous day's index close × (1 ± 10%, 15%, 20%)
```

How long the market stops depends on when the index gets there
([NSE, market-wide circuit breakers](https://www.nseindia.com/products-services/equity-market-circuit-breakers)):

| Trigger | Hit | Trading halts for | Then |
|---|---|---|---|
| 10% | before 1:00 pm | 45 minutes | 15-minute pre-open call auction |
| 10% | 1:00 pm to 2:30 pm | 15 minutes | 15-minute pre-open call auction |
| 10% | at or after 2:30 pm | no halt | — |
| 15% | before 1:00 pm | 1 hour 45 minutes | 15-minute pre-open call auction |
| 15% | 1:00 pm to before 2:00 pm | 45 minutes | 15-minute pre-open call auction |
| 15% | on or after 2:00 pm | rest of the day | — |
| 20% | any time | rest of the day | — |

## Worked example: Desi Bites' band, and the market's

**A stock band.** Desi Bites Foods (our [fictional](/case-study/) company)
has no F&O contracts, so it gets a fixed band. Suppose it closed at
₹{{ c.desi_prev_close }} yesterday (a hypothetical price). Its limits for today, under each
possible band:

| Band | Upper circuit | Lower circuit |
|---:|---:|---:|{% for b in c.desi_bands %}
| {{ b.band_pct }}% | ₹{{ b.upper }} | ₹{{ b.lower }} |{% endfor %}

If Desi Bites sits in the 5% band and some good news lands, the most it can
rise today is to ₹{{ c.desi_bands[1].upper }}. Tomorrow the band resets around *that* close, so a
big re-rating plays out as several days of upper circuits rather than one
jump — with most buyers unfilled each day.

A new listing has its own rule. On listing day the stock trades in a
one-hour pre-open call auction with no band; after that, an issue of up to
₹250 crore (Desi Bites' ₹{{ ipo_cr }} crore IPO included) gets a 5% band around the
auction price and trades in the "trade-for-trade" segment — every trade must
be settled by delivery, no intraday netting — for its first 10 days; larger
issues get a 20% band (SEBI Master Circular, 2023, paras 2.6 and 17.2).

**The market's switch.** The Nifty 50 closed at {% include inr.html n=c.mwcb_base_close %} on {{ base_date }}
(price index, Yahoo Finance; for illustration only). The next session's
downside trigger levels would have been roughly:

| Fall | Points | Nifty level |
|---:|---:|---:|{% for l in c.mwcb_levels %}
| {{ l.fall_pct }}% | {{ l.points }} | {{ l.trigger_level }} |{% endfor %}

These are rare. The last cluster came in the COVID crash: SEBI's annual
report for 2019-20 records circuit filters being hit "three times in India"
that year ([SEBI Annual Report 2019-20](https://www.sebi.gov.in/sebi_data/attachdocs/feb-2021/1612940539512.pdf), p. 2).
In our closing-price data, the Nifty closed at {% include inr.html n=m.close %} on 23 March 2020,
down {{ m.close_change_pct | abs }}% from {% include inr.html n=m.prev_close %} the previous session —
below that day's 10% trigger ({% include inr.html n=m.ten_pct_trigger %}) but above the 15% one
({% include inr.html n=m.fifteen_pct_trigger %}). The rule also works upwards: on 18 May 2009, the
day after the general-election results, the market was halted twice as the
Nifty rose past its upper triggers and closed for the rest of the day
([NSE press release, 18 May 2009](https://nsearchives.nseindia.com/content/press/18052009.htm)).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

In a school auction for a cricket bat, the teacher says: "No bid today can be
more than ₹10 above yesterday's price." If everyone wants the bat, the price
still only goes up ₹10 today, and lots of kids go home without it. Tomorrow
it can go up another ₹10.

And if the whole school starts shouting at once, the principal rings a bell
and everyone sits down for 45 minutes to calm down. That's the market-wide
circuit breaker.

</details>

## Common mistakes

- **Reading "upper circuit" as proof of demand you can act on.** A locked
  upper circuit means the queue of buyers is longer than the queue of
  sellers *at a capped price*. Your order joins the back of that queue. And
  small, thin stocks can hit circuit on very little volume, which is exactly
  why the exchanges watch them (the surveillance post later in this module
  covers how).
- **Thinking the band limits your loss.** A lower circuit stops the price
  printing lower *today*; it doesn't let you sell. Locked lower circuits
  with no buyers can run for days, and the loss arrives anyway.
- **Assuming every stock has a circuit.** F&O stocks, Britannia among them,
  have a dynamic band that widens during the day. A 15% intraday move is
  possible there in a way it isn't for a stock in the 5% band.
- **Confusing the stock band with the market-wide breaker.** One caps a
  single share's move and never stops trading; the other stops the whole
  market. They're different tools set by different rules.

**Takeaway:** a circuit limit caps how far one stock's price can move in a
day; it doesn't stop trading and it doesn't guarantee you a fill. The
market-wide breaker is the separate, rarely used switch that halts everything
when the Nifty or Sensex moves 10%, 15% or 20%.
