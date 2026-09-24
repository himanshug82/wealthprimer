---
layout: post
title: "T+1 settlement: what happens between clicking 'buy' and owning the share"
description: "Indian stock trades settle one working day after the trade. What the clearing corporation does in between, when shares reach your demat, and what T+0 adds."
image: /assets/og/t-plus-1-settlement.png
date: 2026-10-16 09:00:00 +0530
series: jargon
term: "T+1 settlement"
---

{% assign st = site.data.jargon_m7.settlement %}
{% assign ex = site.data.jargon_m7.exdiv[0] %}
{% assign t_day = st.last_buy_date_entitled | date: "%A %-d %B %Y" %}
{% assign t1_day = st.settles_on | date: "%A %-d %B %Y" %}
{% assign qty = 10 %}
{% assign cost = ex.cum_close | times: qty %}

## What T+1 means

When you buy a share on the NSE or BSE, the trade happens instantly but the
*exchange of money for shares* — **settlement** — happens later. "T" is the
trade day. **T+1** means settlement on the next working day: that's when the
seller's shares move and the buyer's money moves.

In between, a **clearing corporation** (NSE Clearing for NSE trades) steps in
as the buyer to every seller and the seller to every buyer. The technical
word is **novation**: NSE Clearing "becomes the counterparty to every member
by novation and meets all settlement obligations, regardless of member
defaults" ([NSE Clearing PFMI disclosure, 31 March 2025](https://www.nseclearing.in/sites/default/files/disclosure-doc/2025-05/PFMI%20Disclosure_March%202025.pdf)).
That's why you never worry about *who* sold you the share. Your counterparty
is the clearing corporation, not a stranger.

India got here in steps. T+3 became T+2 from 1 April 2003 (as the circular
below recounts). SEBI (the
Securities and Exchange Board of India) let exchanges offer T+1 from
1 January 2022 ([SEBI/HO/MRD2/DCAP/P/CIR/2021/628, 7 September 2021](https://www.sebi.gov.in/legal/circulars/sep-2021/introduction-of-t-1-rolling-settlement-on-an-optional-basis_52462.html)),
and the exchanges moved stocks across in batches, smallest first, from
25 February 2022. By SEBI's account the shift was "fully implemented w.e.f.
January 27, 2023" ([SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/20, 21 March 2024](https://www.sebi.gov.in/legal/circulars/mar-2024/introduction-of-beta-version-of-t-0-rolling-settlement-cycle-on-optional-basis-in-addition-to-the-existing-t-1-settlement-cycle-in-equity-cash-markets_82455.html)).

## The rule: the T+1 timeline

The deadlines on settlement day, from SEBI's settlement rules
([Master Circular, Chapter 3 "Settlement"](https://www.sebi.gov.in/sebi_data/commondocs/dec-2024/RE_Chapter%203%20-%20Settlement%20FINAL_p.pdf);
payout time from [SEBI/HO/MRD/MRD-PoD-2/P/CIR/2024/137, 10 October 2024](https://www.sebi.gov.in/sebi_data/attachdocs/oct-2024/1728572020490.pdf)):

| When | What happens |
|---|---|
| T (trade day) | Order matched; the clearing corporation takes both sides; your broker blocks margin |
| T+1, by 11:00 am | Pay-in: sellers' shares and buyers' money reach the clearing corporation |
| T+1, by 1:30 pm | Pay-out of funds to sellers |
| T+1, by 3:30 pm | Pay-out of securities, credited directly to the buyer's demat account |

```
Settlement day = Trade day + 1 working (settlement) day
```

Weekends and settlement holidays don't count, so a Friday trade settles on
Monday.

## Worked example: a Britannia purchase on a Friday

Say you bought {{ qty }} Britannia shares at the {{ ex.last_cum_date | date: "%-d %B %Y" }} close of
₹{% include inr.html n=ex.cum_close %} (NSE; for illustration only), about ₹{% include inr.html n=cost %}.

1. **T = {{ t_day }}.** The trade executes. Your broker takes the money (or
   margin) from your account; the shares appear in your broker app as
   bought, but not yet in your demat account.
2. **T+1 = {{ t1_day }}.** Saturday and Sunday aren't settlement days. By
   11:00 am the money has gone to the clearing corporation; by 3:30 pm the
   shares are in your demat account.
3. **What it bought you.** {{ t1_day | split: " " | first }} {{ st.settles_on | date: "%-d %B" }} happened to be Britannia's
   record date for its FY 2024-25 final dividend (the next post in this
   module explains record dates). Because the Friday purchase settled that
   day, you'd be on the register and entitled. Buy on the Monday itself and
   the shares settle on {{ st.buy_on_record_date_settles | date: "%A %-d %B" }} — too late.

Under the old T+2 cycle, the last day to buy for the same record date would
have been {{ st.t_plus_2_last_buy | date: "%A %-d %B" }}. One day of settlement is one day of
lead time.

### What if a seller doesn't deliver?

The clearing corporation still owes the buyer the shares, so it holds an
**auction** on T+1 to buy them from someone else, with pay-in and pay-out by
T+2. If the auction doesn't find them, the position is **closed out** in
cash at the higher of the highest price in the stock since the trade and 20%
above the latest close — a deliberately painful price for the defaulting
seller (SEBI Master Circular, Chapter 3, sections 1.6 and 2).

### And T+0?

Since 28 March 2024 there's also an *optional* **T+0** (same-day) settlement
for a limited list of stocks, in a separate session from 9:15 am to 1:30 pm
with a band of ±1% around the regular market's price
([SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/20](https://www.sebi.gov.in/legal/circulars/mar-2024/introduction-of-beta-version-of-t-0-rolling-settlement-cycle-on-optional-basis-in-addition-to-the-existing-t-1-settlement-cycle-in-equity-cash-markets_82455.html)).
It began with 25 stocks and, from 31 January 2025, SEBI extended it in
monthly batches toward the top 500 by market cap
([SEBI/HO/MRD/MRD-PoD-3/P/CIR/2024/172, 10 December 2024](https://www.sebi.gov.in/sebi_data/attachdocs/dec-2024/1733829354031.pdf)).
Broker participation is optional, so many investors won't see it at all.
SEBI's board papers shelved the earlier idea of optional *instant*
settlement "for now"
([board memorandum, November 2024](https://www.sebi.gov.in/sebi_data/meetingfiles/nov-2024/1731577464307_1.pdf)).
Check which stocks and brokers offer T+0 before assuming you can use it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You swap your comic for a friend's toy car, but you both leave them with the
class teacher overnight. Next morning the teacher hands you the car and hands
your friend the comic. If your friend forgot to bring the car, the teacher
still owes you one, so she finds another car from someone else and makes
your friend pay extra for it.

The teacher is the clearing corporation. "Overnight" is the +1.

</details>

## Common mistakes

- **Thinking you own the share the moment the order fills.** You have a
  trade the clearing corporation guarantees; the share itself arrives in your demat account on
  T+1. That timing matters for record dates, pledges and transfers.
- **Selling shares before they've arrived.** Selling on T+1 shares bought on
  T is common ("buy today, sell tomorrow"), and usually works because the
  purchase settles the same day. But if your purchase itself falls short —
  your seller defaulted — your own delivery is short too, and it's your sale
  that goes to auction or close-out.
- **Counting calendar days.** Settlement days skip weekends and exchange
  settlement holidays. A trade on the day before a long weekend can take
  four calendar days to settle.
- **Assuming T+0 is available everywhere.** It's an optional, limited
  window for a list of stocks and participating brokers. The default for
  every Indian equity trade is still T+1.

**Takeaway:** in India a share trade settles one working day after it's
made: money and shares change hands through the clearing corporation, and
the shares land in your demat by the afternoon of T+1. Know that date — it
decides whether a purchase counts for a dividend or a record date.
