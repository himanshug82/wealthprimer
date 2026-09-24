---
layout: post
title: "Counterparty risk: what the Karvy case showed, and what changed after"
description: "Your shares sit in your demat account, so how did a broker pledge them? The Karvy case from SEBI's own orders, and the rules that now keep client assets apart."
image: /assets/og/broker-and-counterparty-risk.png
date: 2026-10-21 09:00:00 +0530
series: risk
term: "Counterparty risk"
---

{% assign r2 = site.data.risk2 %}
{% assign kv = r2.karvy %}
{% assign src = kv.sources %}
{% assign ge = kv.g_example %}

## The risk in the plumbing

Most risk on this blog comes from prices: a stock falls, a fund draws down.
**Counterparty risk** is different. It's the risk that someone you depend on
to hold, move or pay your money doesn't do it — a broker, a bank, a
depository participant (DP, the firm through which you hold your demat
account). The investment can be fine and you can still lose access to it.

For most Indian investors this was abstract until November 2019, when SEBI
(the Securities and Exchange Board of India) passed an order against Karvy
Stock Broking Ltd (KSBL), a retail stock broker with, as the orders show,
hundreds of thousands of clients.
This post tells that story strictly from SEBI's and NSE's own documents, then
walks through the rules that now sit between a broker and your assets.

## Where your assets actually sit

| What you hold | Where it sits | Who could misuse or lose it |
|---|---|---|
| Shares | Your demat account at a depository (NSDL or CDSL), through a DP | Anyone with authority to move them out — historically, a broker holding your power of attorney |
| Money for trading | Paid to the broker; now passed on to the clearing corporation by the end of each day | The broker, in the hours or days before it moves on |
| Margin collateral | Pledged from your demat account, not transferred | Less exposed since pledges replaced transfers (see below) |
| Mutual fund units | Held by the fund, a trust; its assets with a custodian | The fund's plumbing, not your distributor |

The weak point, historically, was the second and third rows plus one
document: the **power of attorney (POA)** many investors signed when opening
an account, letting the broker move securities out of their demat account to
meet settlement. That's the key Karvy used.

## The formula: SEBI's client-money check

Since a SEBI circular of
[26 September 2016]({{ src.circ_2016 }}), brokers report weekly figures that
let exchanges test whether client money is all there:

```
A  =  money in all client bank accounts
B  =  cash and cash-like collateral (fixed deposits, the funded part of bank
      guarantees)
      deposited with clearing corporations
C  =  total credit balances owed to clients (after adjustments)
D  =  total debit balances owed by clients

G  =  (A + B) − C          G negative → less money than clients are owed: an alert

If |G| > |D|:   H  =  |G| − |D|
                → part of the shortfall can't be explained by funding other
                  clients' debts: client money possibly used for the broker's
                  own purposes
```

A hypothetical broker's week, in ₹ crore:

| A | B | C | D | G = (A + B) − C | H = \|G\| − \|D\| |
|---:|---:|---:|---:|---:|---:|
| {{ ge.A }} | {{ ge.B }} | {{ ge.C }} | {{ ge.D }} | {{ ge.G }} | {{ ge.H }} |

Clients are owed ₹{{ ge.C }} crore; ₹{{ ge.A | plus: ge.B }} crore is
visible. Of the ₹{{ ge.G | abs }} crore gap, up to ₹{{ ge.D }}
crore could be the broker funding other clients' debit balances (which the
circular also flags); the remaining ₹{{ ge.H }} crore is the alert that client money went
somewhere else. It's a check on *money*. The Karvy case was largely about
*securities*.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your class keeps its trip money with the class monitor. Each child's money is
still *theirs*; the monitor just holds it.

Now imagine the monitor quietly uses everyone's money as a deposit to borrow
a bicycle for himself. As long as nobody asks for their money back at the
same time, nothing looks wrong. The day they do, the money isn't there.

The fixes are simple: the teacher counts the money every week, the monitor
isn't allowed to use it as a deposit, and at the end of each day the money
goes into the teacher's locked box instead of the monitor's pocket.

</details>

## Worked example: the Karvy case, from the orders

Every figure below is quoted from the document cited in that row. The
interim order's findings were *prima facie* — what SEBI found at that stage,
before the full proceedings.

| Date | What happened | Source |
|---|---|---|
| 22 November 2019 | SEBI's ex-parte interim order, on an NSE preliminary report: KSBL had prima facie sold "excess securities … to the tune of Rs. {{ kv.excess_sold_cr }} Crore through {{ kv.excess_sold_related_clients }} related clients", and "a net amount of Rs. {{ kv.to_group_company_cr }} crores" had been transferred to a group company. KSBL was barred from taking new clients, and depositories were told not to act on its client POAs | [SEBI interim order]({{ src.interim_order }}) |
| 2 December 2019 | NSDL transferred securities from a KSBL account back to clients who had paid for them in full: {% include inr.html n=kv.nsdl_clients_returned %} clients. NSE suspended KSBL's membership the same day | [SEBI confirmatory order]({{ src.confirmatory_order }}); [SEBI final order]({{ src.final_order }}) |
| 23 November 2020 | NSE declared KSBL a defaulter and expelled it; investor claims against the Investor Protection Fund capped at ₹{{ kv.ipf_limit_karvy_lakh }} lakh per investor | [NSE public notice]({{ src.nse_notice }}) |
| 24 November 2020 | SEBI confirmed the interim directions; it recorded NSE's statement that funds and securities of about ₹{% include inr.html n=kv.nse_settled_cr %} crore belonging to about {{ kv.nse_settled_investors_lakh }} lakh investors had been settled | [SEBI confirmatory order]({{ src.confirmatory_order }}) |
| 28 April 2023 | SEBI's final order: KSBL and its promoter and managing director restrained from the securities market for {{ kv.ban_years }} years | [SEBI final order]({{ src.final_order }}) |

The final order fills in the scale. The value of client securities KSBL had
pledged grew from ₹{{ kv.pledged_jun2017_cr }} crore in June 2017 to
₹{% include inr.html n=kv.pledged_mar2018_cr %} crore by March 2018 and
₹{% include inr.html n=kv.pledged_sep2019_cr %} crore by September 2019; about
₹{{ kv.raised_cr }} crore was raised against them. As on 5 September 2019,
"at least {{ kv.pledged_share_pct }} percent of the total shares in all its
clients' holding were pledged by KSBL to borrow funds for its own use." As on
22 November 2019, funds of ₹{{ kv.unsettled_funds_cr }} crore and securities of
₹{% include inr.html n=kv.unsettled_securities_cr %} crore were unsettled with
{% include inr.html n=kv.unsettled_clients %} clients.

The mechanism, in plain words: clients' shares were moved, using the POAs
they had signed, into an account KSBL controlled but hadn't properly
reported, then pledged with lenders. The money raised went to KSBL's own use, and the
orders trace large sums on to group companies.

## What the rules say now

The first of these predates the Karvy order and was being phased in as it
broke; the rest came after. Dates are the circulars' own.

| Rule | Circular | What it does |
|---|---|---|
| No pledging client securities to raise money | [20 June 2019]({{ src.circ_2019 }}) | From 1 September 2019 (later extended to 1 October, per SEBI's Karvy interim order), client securities in a broker's accounts "cannot be pledged to the Banks/NBFCs for raising funds, even with authorization by client" — NBFCs being non-banking financial companies |
| Margin by pledge, not transfer | [25 February 2020]({{ src.circ_2020 }}), in force from 1 August 2020 | Collateral stays in your demat account, pledged; "title transfer collateral arrangements" prohibited |
| Regular settlement of idle client money | [27 July 2022]({{ src.circ_2022_running }}), from 1 October 2022 | Unused client funds returned on the first Friday of each quarter (or month, if the client chose) |
| Block mechanism for sales | [18 August 2022]({{ src.circ_2022_block }}), from 14 November 2022 | Shares you're selling are blocked in your own demat account instead of moving to the broker |
| Client money upstreamed daily | [8 June 2023]({{ src.circ_2023_upstream }}), from 1 July 2023 | "no clients' funds shall be retained" by brokers on an end-of-day basis; it goes to the clearing corporation |
| Trading on blocked funds (a UPI, or Unified Payments Interface, block) | [23 June 2023]({{ src.circ_2023_upi }}), from 1 January 2024; [11 November 2024]({{ src.circ_2024_upi }}) | Money stays blocked in your bank account until the trade settles; from 1 February 2025 qualified stock brokers (the large brokers SEBI designates for extra obligations) must offer it or a 3-in-1 account; optional for clients |
| Higher Investor Protection Fund cap at NSE | [NSE press release, 13 August 2024]({{ src.nse_ipf_2024 }}) | From ₹{{ kv.ipf_limit_karvy_lakh }} lakh to ₹{{ kv.ipf_limit_now_lakh }} lakh per investor per claim, for defaults declared from that date |

The direction of travel is clear: keep client assets in the client's own
account (pledged or blocked, not transferred), move client cash out of the
broker's hands daily, and check the totals weekly. Each rule closes a door
Karvy-style misuse relied on.

## Common mistakes

- **Assuming a demat account means nobody else can touch your shares.** The
  shares are in your name, but any authority you've signed — a POA, a
  mandate — is a key. Know what you've signed, and read the depository's own
  statements (the CAS, consolidated account statement), not just the
  broker's.
- **Leaving large idle balances with a broker.** Money sitting "for the next
  trade" is exposure to the broker that earns nothing. The settlement rules
  shrink it; they don't make it zero.
- **Reading the protection fund as insurance on your portfolio.** It
  compensates eligible claims against a defaulting broker, up to a cap, after
  a process. It doesn't cover trading losses, and it isn't instant.
- **Thinking counterparty risk is only about brokers.** Every link — bank,
  DP, platform, fund — is one. Regulation reduces the risk at each link; it
  doesn't remove the value of checking.

**Takeaway:** You can own an investment and still lose access to it if someone
between you and it misuses what they hold. The Karvy orders show how client
securities were pledged for a broker's own borrowing; the rules since keep
your shares in your account and your cash out of the broker's hands
overnight. Check your depository statement, not just your broker's.
