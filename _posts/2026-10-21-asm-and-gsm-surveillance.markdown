---
layout: post
title: "ASM and GSM: what it means when the exchange puts a stock under surveillance"
description: "The exchanges' surveillance lists raise margins, narrow price bands and slow trading in stocks with unusual moves. What each stage changes for a trader."
image: /assets/og/asm-and-gsm-surveillance.png
date: 2026-10-21 09:00:00 +0530
series: jargon
term: "ASM and GSM (surveillance measures)"
---

{% assign sv = site.data.jargon_m7.surveillance %}
{% assign g2 = sv.gsm[1] %}
{% assign g3 = sv.gsm[2] %}

## What ASM and GSM are

Some stocks move in ways the exchanges don't like: a small company's price
doubling in weeks on little news, a handful of accounts doing most of the
trading, a valuation wildly out of line with the business. Instead of
halting such stocks, the exchanges put them on **surveillance lists** that
make speculative trading slower and more expensive.

All of them are set up the same way: "SEBI and Exchanges, pursuant to
discussions in joint surveillance meetings, have decided…" (NSE's
[ASM](https://www.nseindia.com/regulations/additional-surveillance-measure),
[GSM](https://www.nseindia.com/regulations/graded-surveillance-measure) and
[ESM](https://www.nseindia.com/regulations/enhanced-surveillance-measure-esm)
pages). The exchanges publish the lists, and a stock moves between stages
as they review it.

| Framework | In force since | Aimed at | Stages |
|---|---|---|---|
| **GSM** — Graded Surveillance Measure | 14 March 2017 | Stocks whose "price [is] not commensurate with financial health and fundamentals" | I to IV |
| **ASM** — Additional Surveillance Measure | 26 March 2018 | Unusual price or volume behaviour: big high-low swings, client concentration, low delivery, few unique traders | Long-term I to IV; short-term I and II |
| **ESM** — Enhanced Surveillance Measure | 5 June 2023 | Small companies with unusual moves; now all companies (main board and SME) under ₹{% include inr.html n=sv.esm_mcap_limit_cr %} crore market cap | I and II |

Dates from NSE's FAQs: [GSM FAQ v1.1, June 2026](https://nsearchives.nseindia.com//web/mediaattachment/2026-06/FAQs_-_Graded_Surveillance_Measure_GSM_Version_1.1_20260612125858.pdf),
[ASM FAQ, August 2026](https://nsearchives.nseindia.com//web/mediaattachment/2026-08/FAQs_-_Additional_Surveillance_Measure_ASM_20260812103311.pdf),
and circular [NSE/SURV/56948, 2 June 2023](https://nsearchives.nseindia.com/content/circulars/SURV56948.pdf)
for ESM, which began with main-board companies under
₹{{ sv.esm_launch_mcap_limit_cr }} crore and has since been widened.

The exchanges are explicit that this is not a verdict on the company:
"The shortlisting of securities under ASM is purely on account of market
surveillance and it should not be construed as an adverse action against the
concerned company / entity" (ASM FAQ, Q4; the ESM FAQ says the same). The
criteria change from time to time — GSM's own FAQ notes changes agreed at a
May 2026 meeting — so check the current FAQ rather than any summary,
this one included.

## The rules: what each stage changes

The tools are few and they stack:

- **Higher margin** — up to 100%: you must put up the full trade value
  upfront, no leverage.
- **Narrower price band** — down to 5% or 2% (the
  [circuit limits post]({% post_url 2026-10-15-circuit-limits-and-price-bands %})
  explains bands).
- **Trade-for-trade settlement** — every trade must be settled by delivery;
  no buying and selling the same stock in a day to net off.
- **A deposit on top** — GSM's *Additional Surveillance Deposit* (ASD),
  paid in cash, interest-free, and not usable as margin for anything else.
- **Less frequent trading** — at the later GSM stages, once a week.

GSM, stage by stage (GSM FAQ v1.1, Q4). Stage I sets a 100% margin; from
Stage II trades are trade-for-trade, so the buyer pays in full, and the ASD
comes on top:

| Stage | Paid upfront | ASD (% of trade value) | Trading | Price band |
|---|---:|---:|---|---|{% for g in sv.gsm %}
| {{ g.stage }} | {{ g.margin_pct }}% | {{ g.asd_pct }}% | {{ g.trading }} | {{ g.band }} |{% endfor %}

Long-term ASM steps up in a similar way: 100% margin at Stage I, a
lower price band at each of Stages II and III, and gross settlement with a
5% band at Stage IV (ASM FAQ).

## Worked example: a ₹1 lakh purchase in a GSM stock

*Hypothetical.* Imagine a small company on GSM. What does a buyer have to put
up for ₹{% include inr.html n=sv.trade_value %} worth of shares at each stage?

| Stage | Paid upfront (₹) | ASD (₹) | **Total locked up (₹)** |
|---|---:|---:|---:|{% for g in sv.gsm %}
| {{ g.stage }} | {{ g.margin_rs }} | {{ g.asd_rs }} | **{{ g.total_locked_rs }}** |{% endfor %}

1. At Stage I nothing is borrowed: ₹{% include inr.html n=sv.trade_value %} of shares needs ₹{% include inr.html n=sv.trade_value %} of cash.
2. At Stage II the same purchase ties up ₹{% include inr.html n=g2.total_locked_rs %}: the price, plus a
   ₹{% include inr.html n=g2.asd_rs %} deposit the exchange holds interest-free.
3. At Stage III it's ₹{% include inr.html n=g3.total_locked_rs %}, and you can only trade on one day a
   week. A position you want to exit on a Wednesday waits till Monday.
4. With a 5% band, the most the position can move in a trading session is
   ₹{% include inr.html n=sv.max_daily_move_5pct_rs %} — in either direction, and a locked lower circuit
   can repeat session after session.

For a company the size of our [fictional](/case-study/) Desi Bites
(₹{{ sv.desi_mcap_cr }} crore market cap), ESM is the framework in play: every company under
₹{% include inr.html n=sv.esm_mcap_limit_cr %} crore is in its universe, and a burst of unusual price moves could
put it on the list. Being in the universe isn't being on the list.

## Common mistakes

- **Reading a surveillance tag as a fraud finding.** For ASM and ESM the
  exchanges say outright it isn't an adverse action against the company.
  It's a flag on the *trading*, not a finding against the business.
- **Reading it as irrelevant.** The flip side: the lists exist because the
  trading pattern looked unusual. A stock that's run far ahead of its
  financials on thin volume is on GSM for a reason worth knowing.
- **Being surprised by the cash call.** Moving from normal margin to 100%,
  plus an ASD at GSM Stage II, means an existing trading plan can suddenly
  need much more capital — and intraday strategies stop working under
  trade-for-trade.
- **Checking once.** Stages change on each review. Look at the exchange's
  current list (NSE publishes [ASM](https://www.nseindia.com/reports/asm) and
  [GSM](https://www.nseindia.com/reports/gsm) reports) before trading a small
  stock, not a screenshot from last month.

**Takeaway:** ASM, GSM and ESM are the exchanges' brakes on unusual trading
in a stock — higher margins, narrower bands, delivery-only trades, and at
the extreme, trading once a week. They flag the trading, not wrongdoing by the company, but
they change what a trade costs and how easily you can get out.
