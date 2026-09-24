---
layout: post
title: "Offer for sale and delisting: when promoters sell shares, and when they buy everyone out"
description: "An offer for sale moves existing shares to new owners; a delisting buys out the public. The OFS window and reverse book building, on fictional Desi Bites."
image: /assets/og/offer-for-sale-and-delisting.png
date: 2026-10-20 09:00:00 +0530
series: jargon
term: "Offer for sale (OFS) and delisting"
---

{% assign o = site.data.jargon_m7.ofs %}
{% assign x = o.exchange_ofs %}
{% assign dl = o.delist %}

## What an offer for sale is

Companies issue new shares; shareholders sell existing ones. An **offer for
sale (OFS)** is the second kind, done in bulk: a promoter or large investor
offers a block of shares they already own to the public. The company's share
count doesn't change and **the company receives nothing** — the money goes to
whoever sold.

You meet OFS in two places:

1. **Inside an IPO.** Many initial public offers are a mix of a *fresh
   issue* (new shares, money to the company) and an *OFS* (existing
   shares, money to the sellers). The [DRHP post]({% post_url 2026-10-09-reading-a-drhp %})
   explains why that split is the first thing to check.
2. **After listing, through the exchange.** SEBI (the Securities and Exchange
   Board of India) runs a separate OFS window on the stock exchanges for
   listed companies, under a framework last rewritten on 10 January 2023
   ([SEBI/HO/MRD/MRD-PoD-3/P/CIR/2023/10](https://www.sebi.gov.in/legal/circulars/jan-2023/comprehensive-framework-on-offer-for-sale-ofs-of-shares-through-stock-exchange-mechanism_67157.html)).
   The seller announces a **floor price** by 5 pm the day before; non-retail
   investors bid on day T, retail investors on T+1; at least 10% of the offer
   is reserved for retail investors (bids up to ₹2 lakh) and at least 25%
   for mutual funds and insurers. It's open to companies with an average
   market cap of ₹1,000 crore or more, with a ₹25 crore minimum size — and,
   whatever their size, to promoters selling down to meet the minimum public
   shareholding rule.

**Delisting** is the opposite move: the promoter (the "acquirer") buys out
the public so the shares stop trading altogether. The rules are the SEBI
(Delisting of Equity Shares) Regulations, 2021, amended on 25 September 2024
and 3 September 2025
([consolidated text](https://www.sebi.gov.in/legal/regulations/sep-2025/securities-and-exchange-board-of-india-delisting-of-equity-shares-regulations-2021-last-amended-on-september-3-2025-_96548.html)).
In outline:

- The company's shareholders must approve it by special resolution, and
  public shareholders' votes in favour must be at least twice their votes
  against (reg. 11).
- The price is found by **reverse book building**: public shareholders bid
  the price at which they're willing to sell, and the **discovered price**
  is the one at which enough shares have been tendered to take the
  acquirer's holding to **90%** of the shares (reg. 21). The acquirer can't
  bid below a regulated **floor price** (reg. 19A).
- Since the 2024 amendment, an acquirer of a frequently traded company can
  instead offer a **fixed price** at least 15% above the floor (reg. 20A),
  and if a reverse book building falls short, may make a **counter-offer**
  provided its holding plus tendered shares reaches at least 75% and at
  least half the public shareholding has been tendered (reg. 22(4)). The 90%
  test for success still applies.
- Shareholders who didn't tender can sell to the acquirer at the delisting
  price for at least a year after delisting (reg. 26).

## The rules in one table

| | Fresh issue | Offer for sale | Delisting offer |
|---|---|---|---|
| Who sells | The company (new shares) | Existing holders | The public, to the acquirer |
| Money goes to | The company | The sellers | The public shareholders who tender |
| Share count | Rises | Unchanged | Unchanged |
| Public shareholding | Rises | Rises | Falls toward zero |
| Price set by | Book building / fixed | Floor price + bids | Reverse book building (or fixed price) |

## Worked example 1: a promoter OFS to reach 25% public

*Hypothetical.* The [free float post]({% post_url 2026-10-18-free-float-and-promoter-holding %})
noted that Desi Bites' [fictional](/case-study/) public shareholding, 20%,
would be below India's 25% minimum. The exchange OFS window is one way a
promoter fixes that. Desi Bites' ₹{{ x.desi_mcap_cr }} crore market cap is far under the
₹{% include inr.html n=x.ofs_mcap_threshold_cr %} crore threshold, but a promoter selling to meet the minimum can use it anyway,
and in one tranche can go below the ₹{{ x.min_size_cr }} crore minimum size.

| | |
|---|---:|
| Shares the promoter offers | {% include inr.html n=x.shares %} |
| Floor price (hypothetical) | ₹{{ x.floor_price }} |
| Size at the floor | ₹{{ x.size_lakh }} lakh (₹{{ x.size_cr }} crore) |
| Reserved for retail (at least 10%) | {% include inr.html n=x.retail_min_shares %} shares |
| Reserved for mutual funds and insurers (at least 25%) | {% include inr.html n=x.mf_ins_min_shares %} shares |
| Promoter holding after | {{ x.promoter_after_lakh }} lakh shares ({{ x.promoter_after_pct }}%) |
| Public holding after | {{ x.public_after_pct }}% |
| Total shares | {{ x.shares_total_lakh_unchanged }} lakh — unchanged |

The company raises nothing. Its share count, earnings per share and balance
sheet are exactly as before; only the names on the register change.

## Worked example 2: a reverse book building for Desi Bites

*Hypothetical.* Now the other direction. Desi Bites' promoter, at
{{ dl.promoter_pct }}%, proposes to delist. The floor price works out at ₹{{ dl.floor_price }}. To
reach {{ dl.threshold_pct }}% the promoter needs {{ dl.shares_needed_lakh }} lakh of the public's shares
tendered. Public shareholders bid:

| Bid price | Shares tendered (lakh) | Cumulative (lakh) | Acquirer's holding if accepted |
|---:|---:|---:|---:|{% for l in dl.ladder %}
| ₹{% include inr.html n=l.price %} | {{ l.shares_lakh }} | {{ l.cumulative_lakh }} | {{ l.acquirer_pct_if_accepted }}% |{% endfor %}

A further {{ dl.not_tendered_lakh }} lakh shares weren't tendered at all.

1. Walk down the table until the cumulative column first reaches
   {{ dl.shares_needed_lakh }} lakh. That happens at ₹{% include inr.html n=dl.discovered_price %} — the **discovered price**,
   {{ dl.premium_to_floor_pct }}% above the floor.
2. If the acquirer accepts, every share tendered at or below ₹{% include inr.html n=dl.discovered_price %}
   ({{ dl.accepted_lakh }} lakh) is bought at ₹{% include inr.html n=dl.discovered_price %}, whatever its holder bid.
   Cost: ₹{% include inr.html n=dl.cost_at_discovered_lakh %} lakh. The acquirer ends at {{ dl.acquirer_after_pct }}%.
3. Shares bid above ₹{% include inr.html n=dl.discovered_price %} aren't bought in the offer. Their holders,
   and those who never tendered, can sell to the acquirer at ₹{% include inr.html n=dl.discovered_price %} for
   at least a year after delisting.
4. The acquirer can also reject the discovered price, in which case the
   offer fails and the company stays listed — or, if the conditions above
   are met, try a counter-offer.

Notice who sets the price: the *last* shareholder needed to reach 90%. A
few holders bidding high can move the price a long way — here, to
{{ dl.premium_to_floor_pct }}% above the floor.

## Common mistakes

- **Reading an OFS as the company raising money.** It doesn't. A promoter
  OFS changes who owns the shares, not what the company has. Whether it's
  a signal about the business depends on why they're selling — meeting a
  public-shareholding rule is very different from an early exit.
- **Assuming a delisting will happen at a big premium.** The acquirer can
  reject the discovered price and walk away, and the shares stay listed.
  Buying a stock because a delisting is "coming" is a bet on an offer that
  may never be made or may fail.
- **Not tendering and forgetting about it.** After a successful delisting
  the remaining shares no longer trade on the exchange. The right to sell
  at the delisting price lasts at least a year; after that, an unlisted
  minority stake is hard to sell.
- **Confusing the floor price with the offer price.** The floor is the
  minimum the regulations allow. The price paid is discovered by the bids,
  or set as a fixed premium over the floor.

**Takeaway:** an offer for sale moves existing shares to new owners and
puts no money into the company; a delisting does the reverse, buying the
public out at a price the public's own bids discover. In both, read who is
selling to whom, and why.
