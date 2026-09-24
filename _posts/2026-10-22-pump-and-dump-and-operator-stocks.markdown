---
layout: post
title: "Pump and dump: how an \"operator\" stock works, from a SEBI order"
description: "Circular trades, YouTube videos, a price up twelvefold, then the exit. One SEBI case read from its orders, how exchange surveillance works, and the red flags."
image: /assets/og/pump-and-dump-and-operator-stocks.png
date: 2026-10-22 09:00:00 +0530
series: risk
term: "Pump and dump"
---

{% assign r2 = site.data.risk2 %}
{% assign pd = r2.pump %}
{% assign src = pd.sources %}

## A price rise that was manufactured

"Operator stock" is Indian market slang for a share whose price is being
steered by a group of people rather than by buyers and sellers acting
independently. The classic version is a **pump and dump**: build up a
holding in a small, thinly traded company; push the price up with trades
among yourselves; advertise the rising price to the public with a story;
then sell your holding to the people the story brought in. The public's
buying is the exit.

It's illegal — SEBI (the Securities and Exchange Board of India) prohibits
it under the SEBI (Prohibition of Fraudulent and Unfair Trade Practices
relating to Securities Market) Regulations, 2003 — and it recurs, because it works until it's caught. The
[finfluencers post]({% post_url 2026-10-15-how-finfluencers-make-money %})
listed it as the rarest and most damaging way content gets monetised. This
post reads one case from SEBI's own orders, to see the mechanics with real
numbers.

The case is SEBI's in the matter of Sadhna Broadcast Ltd (now Crystal
Business System Ltd, per the final order). The company is named because the
orders are public; the individuals aren't, because the point is the scheme.
Everything below is as the orders state it. SEBI's interim findings were
*prima facie*; orders can be appealed to the Securities Appellate Tribunal,
and press reports say at least one party's appeal against the final order
succeeded.

## The numbers of a pump

There's no formula for fraud, but there is arithmetic for its victims:

```
Rise from the pre-scheme price to the peak   =  peak / start  −  1
Fall from the peak to later                  =  later / peak  −  1
Gain needed to get back to the peak          =  peak / later  −  1
Volume multiple                              =  average daily volume during / before
```

Every price in the order is adjusted for a 10-for-1 share split in June 2022.
A stock's *circuit* (price band) is the furthest its price may move in a
day; a stock locked at the upper circuit has buyers queued and almost no
sellers, and at the lower circuit the reverse.

| | Figure | Source |
|---|---:|---|
| Closing price before the examination period (April 2022) | ₹{{ pd.pre_close }} | Interim order |
| Close on 14 July 2022, end of "patch 1" | ₹{{ pd.p1_close }} (+{{ pd.p1_rise_pct_reported }}%) | Interim order |
| Peak close, 12 August 2022 | ₹{{ pd.peak_close }} (+{{ pd.p2_rise_pct_reported }}% more; {{ pd.multiple_to_peak | round }}× the start) | Interim order |
| Days at the upper circuit in patch 1 | {{ pd.upper_circuit_days }} of {{ pd.patch1_days }} | Interim order |
| Average daily volume: before / patch 1 / patch 2 (shares) | {% include inr.html n=pd.adv_pre %} / {% include inr.html n=pd.adv_p1 %} / {% include inr.html n=pd.adv_p2 %} | Interim order |
| Unique buyers: patch 1 / patch 2 | {% include inr.html n=pd.buyers_p1 %} / {% include inr.html n=pd.buyers_p2 %} | Interim order |
| Small shareholders: June → September 2022 | {% include inr.html n=pd.small_holders_before %} ({{ pd.small_holders_before_pct }}% of shares) → {% include inr.html n=pd.small_holders_after %} ({{ pd.small_holders_after_pct }}%) | Interim order |
| December 2022: lower circuit every trading day | {{ pd.dec2022_lower_circuit_days }} days, ₹{{ pd.dec2022_from_text }} → ₹{{ pd.dec2022_to_text }} ({% include inr.html n=pd.dec2022_fall_pct %}%) | Final order |
| Price at the time of the final order (May 2025) | "around Rs. {{ pd.later_price_text }}" | Final order |

From the ₹{{ pd.peak_close }} peak to about ₹{{ pd.later_price_text }} is a fall of
{{ pd.fall_from_peak_pct | abs }}%. Getting back to the peak from
there would take a gain of {% include inr.html n=pd.gain_to_recover_pct %}% —
the [arithmetic of losses]({% post_url 2026-10-09-the-arithmetic-of-losses %})
at its most extreme.

## How the scheme worked, per the orders

The interim order ([2 March 2023]({{ src.interim }})) sorts the
{{ pd.noticees_interim }} people and entities it named into four roles:

1. **Volume creators** "who both bought and sold shares … hence contributing
   to a rise in trading volumes and interest in the scrip." In the first
   patch — from late April to mid-July 2022 — average daily volume rose
   {{ pd.adv_multiple_p1 }} times and the price {{ pd.p1_price_multiple }} times, before the
   videos.
2. **Misleading message disseminators**, who ran two YouTube channels. In the
   second half of July 2022, videos with false claims went up; five videos
   drew a combined {{ pd.views_crore }} crore views, "aided by promotion
   through paid advertising campaigns" — the order traces debits for Google
   ads of ₹{{ pd.ad_spend_cr }} crore in one noticee's bank account over
   January–September 2022.
3. **Net sellers** — including promoter shareholders — who "offloaded a
   significant part of their holdings at inflated prices and booked profits."
   The order found that "the sale of shares by many of the Net Sellers had
   matched with the buy orders of the Volume Creators", and that the disseminators sold "contrary to the buy
   recommendations in the YouTube Channels."
4. **Information carriers**, who passed information between the others.

The videos' claims, as the order records them, included a large film
contract with "a big American corporation" and a technical-analysis pitch:
"The technical indicators like Relative Strength Index (RSI) and Moving
Average Convergence/Divergence (MACD) suggest that the price of the company
is very bullish mode and the target price is INR 76 in three months and INR
340 in one year." The company posted a denial on BSE on 18 July 2022; two of
the videos were uploaded after it. The order also notes "no material relevant
price sensitive corporate announcements were made during the examination
period." (For what [RSI]({% post_url 2026-10-08-rsi %}) and
[MACD]({% post_url 2026-10-09-macd %}) actually measure — and what they
can't — see those posts. An indicator on a manipulated price measures the
manipulation.)

The outcome, in stages:

- **Interim order, 2 March 2023:** {{ pd.noticees_interim }} noticees barred
  from dealing in securities; alleged unlawful gains of
  ₹{{ pd.impounded_cr }} crore impounded.
- **Confirmatory order, [20 July 2023]({{ src.confirmatory }}):** the
  findings confirmed for the parties it covered, with the total alleged gain
  modified to ₹{% include inr.html n=pd.impounded_modified %}.
- **Final order, [29 May 2025]({{ src.final }}):** after an investigation
  covering {{ pd.noticees_final }} entities, {{ pd.five_year_bans }} barred for
  five years and most others for one; disgorgement with interest and penalties. In the
  order's words: "a classic pump-and-dump scheme. The price was
  systematically pushed upward through collusive trading, followed by
  aggressive promotional activity to draw in retail investors, and finally, a
  coordinated sell-off by the promoters."

Note who holds the shares at the end. Between June and September 2022 the
number of small shareholders went from {% include inr.html n=pd.small_holders_before %}
to {% include inr.html n=pd.small_holders_after %}, and their share of the
company from {{ pd.small_holders_before_pct }}% to
{{ pd.small_holders_after_pct }}%.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Four friends own all the stickers of a boring cartoon. They start trading the
stickers back and forth with each other at higher and higher prices, loudly,
in the playground. "Did you hear? Rahul paid ₹50 for one!"

Other kids notice the price going up and want in. Then one friend tells
everyone the cartoon is getting a movie. Now everyone wants the stickers.

The four friends sell all their stickers to the other kids at ₹50. There's no
movie. Next week nobody wants the stickers at any price — and the kids who
bought last are left holding them.

</details>

## What the exchanges watch for

SEBI and the exchanges don't wait for complaints. Two frameworks put
restrictions on stocks that trip objective filters, often while a pump is
still running:

- **GSM, the Graded Surveillance Measure** — introduced by
  [NSE circular of 23 February 2017]({{ src.gsm_circular }}) for "securities
  which witness an abnormal price rise not commensurate with financial health
  and fundamentals like Earnings, Book value, Fixed assets, Net-worth, P/E
  multiple" (P/E is the [price-to-earnings ratio]({% post_url 2026-09-24-price-to-earnings %})).
  Stages escalate from 100% margin and a 5% price band to
  trade-for-trade settlement, trading once a week, and a freeze on upward
  moves ([NSE FAQ]({{ src.gsm_faq }})).
- **ASM, the Additional Surveillance Measure** — in force from 26 March 2018,
  on parameters including "High Low Variation, Client Concentration, Close to
  Close Price Variation, Market Capitalization, Volume Variation, Delivery
  Percentage, No. of Unique PANs, PE" — PANs being the Permanent Account
  Numbers of distinct traders ([NSE FAQ]({{ src.asm_faq }})).

A stock on either list isn't accused of anything: BSE's FAQ says
shortlisting "should not be construed as an adverse action against the
concerned security" ([BSE FAQ]({{ src.asm_bse_faq }})). But it tells you the
stock's price or trading has tripped a surveillance filter — worth knowing
before you buy on a tip. SEBI has also issued repeated public cautions
against unsolicited tips on SMS, WhatsApp and Telegram, including on
[14 October 2020]({{ src.caution_2020 }}) and
[21 May 2025]({{ src.caution_2025 }}).

## Red flags

| Signal | Why it matters |
|---|---|
| A sharp rise with no company announcement | The final order urged caution with "sudden spikes in prices without any attributable change in fundamentals" |
| Volume that jumps many times over in a small company | Trading among insiders shows up as volume first — here, {{ pd.adv_multiple_p1 }} times before the videos |
| Upper circuit day after day | A stock that only goes up and can't be bought is a stock with no sellers — yet |
| Unsolicited tips with a target price and a deadline | SEBI's cautions warn specifically about tips "indicating target prices" |
| Claims the company itself denies | Here, the denial was on BSE's site while videos kept going up |
| The stock is on an ASM or GSM list | Not an accusation, but a filter has noticed something |
| Promoters or large holders selling into the rise | Visible in quarterly shareholding patterns, usually too late |

## Common mistakes

- **Taking a rising price as confirmation of the story.** In a pump the
  price is the advertisement. The rise is manufactured precisely so that it
  looks like evidence.
- **Assuming you'll get out in time.** The order records a month of lower
  circuits in December 2022. When a stock is locked at its lower limit
  there are sellers and no buyers — a stop-loss order can't execute.
- **Trusting technical signals on thin, manipulated stocks.** RSI, MACD and
  breakouts describe what the price did. When the price is the product, they
  describe the product.
- **Thinking a regulator's order gets your money back.** Impounding and
  disgorgement go after the wrongdoers' gains; they are not, in general, a
  refund to everyone who bought at the top.

**Takeaway:** A pump and dump manufactures the evidence — a rising price and
heavy volume — then sells to whoever believes it. In this case SEBI's orders
record a price up {{ pd.multiple_to_peak | round }} times with no price-sensitive company news, and a
later fall of {{ pd.fall_from_peak_pct | abs }}% from the peak.
When a small stock is rising with no announcement and a stranger is urging you
in, ask who is selling to you.
