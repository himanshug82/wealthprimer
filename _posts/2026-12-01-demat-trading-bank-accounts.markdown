---
layout: post
title: "Demat, trading and bank accounts: who holds what"
description: "Your shares sit in a demat account, your orders go through a trading account, your cash moves through a bank account. What each does, and the BSDA rules."
image: /assets/og/demat-trading-bank-accounts.png
date: 2026-12-01 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign b = site.data.market_basics.bsda %}

## What each account does

To buy a share on the Indian exchanges you use three accounts that do three different jobs:

| Account | What it does | Who runs it |
|---|---|---|
| **Bank account** | Holds your cash; money moves out to pay for purchases and in from sales | Your bank |
| **Trading account** | Lets you place buy and sell orders on the exchange | Your stockbroker (a member of the exchange) |
| **Demat account** | Holds the securities themselves in electronic form | A depository participant (DP), registered with a depository |

"Demat" is short for dematerialised: physical share certificates converted into electronic records. In India the depository — the institution that keeps those records — is either NSDL (National Securities Depository Limited) or CDSL (Central Depository Services (India) Limited). You never deal with the depository directly. You open the account with a DP, which is often your broker or a bank.

CDSL's own FAQ (frequently asked questions) describes the arrangement this way: the depository becomes the "registered owner" in the company's books, and the investor is the "beneficial owner", who receives all the benefits of holding the securities. In plain terms: the depository is on the company's register and you hold the benefits.

The point of the split is that your securities don't sit on your broker's books. For what happens when a broker fails, see [broker and counterparty risk]({% post_url 2026-10-21-broker-and-counterparty-risk %}).

## The flow of a trade

Simplified (settlement runs through the exchange's clearing system):

```
Bank account  --(cash)-->  broker  --(order)-->  exchange
Demat account  <--(shares credited after settlement)--  clearing system
```

The settlement cycle is covered in [T+1 settlement]({% post_url 2026-10-16-t-plus-1-settlement %}).

## What a basic services demat account (BSDA) is

A demat account normally carries an annual maintenance charge (AMC) set by the DP. SEBI (the Securities and Exchange Board of India) has a lower-cost version, the basic services demat account. Under the rules below, a DP is meant to open a BSDA for an eligible holder unless the holder consents, through a verifiable channel, to a regular account.

Rules as at {{ b.as_of }}, from SEBI circular {{ b.circular_2024 }} ([source]({{ b.url_2024 }})), as amended by circular {{ b.circular_2025 }} ([source]({{ b.url_2025 }})):

- An individual can have one BSDA across all depositories, and must hold only one demat account where they are the sole or first holder.
- The value of securities held must not exceed ₹{{ b.limit_lakh }} lakh at any time.
- Maximum annual maintenance charge: nil up to ₹{{ b.free_up_to_lakh }} lakh of holdings; up to ₹{{ b.max_amc_rs }} for holdings above ₹{{ b.free_up_to_lakh }} lakh and up to ₹{{ b.limit_lakh }} lakh.
- Above the limit, the DP may charge regular rates from that date.
- The December 2025 circular excludes certain securities (zero-coupon zero-principal bonds and delisted securities) from the threshold, requires DPs to reassess eligibility every quarter, and says DPs open only a BSDA for eligible holders unless the holder gives consent for a regular account through a verifiable channel.
- Other charges for BSDA are at par with a regular account. Electronic statements are free; a physical statement may be charged up to ₹{{ b.statement_fee_max_rs }}.

These are the limits as written in those circulars. **Check the current rule** and your DP's own tariff before relying on them: both change.

## Worked example: how the BSDA charge steps up

An illustrative investor, with holdings values chosen for the example (not market data):

| Holding value (₹ lakh) | Status | Maximum AMC under BSDA rules |
|---:|---|---|
{% for e in b.examples -%}
| {{ e.holding_lakh }} | {{ e.status }} | {{ e.max_amc }} |
{% endfor %}

1. At the first holding, the BSDA charge is nil.
2. At the second, it is capped, not necessarily charged: ₹{{ b.max_amc_rs }} is a maximum.
3. At the third, the account is over the limit, so regular charges may apply from the date the limit is crossed.

The cap is on the maintenance charge only. It says nothing about brokerage or other fees.

## Common mistakes

- **Thinking the broker "has" your shares.** The shares are in your demat account at the depository. The broker has your trading access, not your holdings. If you pledge shares as margin, they stay in your demat account under a pledge in the broker's favour; see [broker and counterparty risk]({% post_url 2026-10-21-broker-and-counterparty-risk %}).
- **Assuming BSDA status is permanent.** Eligibility depends on holdings and on having only one demat account as first holder; the DP reassesses it every quarter, and crossing the limit ends it.
- **Mixing up the three accounts when something goes wrong.** A payment problem starts at the bank, an order problem at the broker, a holding problem at the DP — and the DP is often the broker, so the names can overlap.
- **Ignoring charges other than AMC.** The BSDA cap covers maintenance only.

**Takeaway:** Your bank holds the cash, your broker places the order, and your demat account holds the shares — three accounts, three jobs. BSDA caps one charge, the annual maintenance fee, within limits that change, so check the circular and your DP's tariff.
