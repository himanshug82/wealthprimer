---
layout: post
title: "SCORES and SMART ODR: where to complain"
description: "If a broker, fund house or listed company ignores your complaint, SEBI has two routes: SCORES and SMART ODR. What each covers, with day counts and costs."
image: /assets/og/scores-and-smart-odr.png
date: 2026-12-06 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign s = site.data.market_basics.scores %}

## Two routes, one order

When something goes wrong with a broker, a fund house or a listed company, the entity's own grievance desk is the natural first stop (for SMART ODR it is a stated pre-requisite, below). SEBI (the Securities and Exchange Board of India) runs two further routes:

- **SCORES** (SEBI Complaints Redress System) is an online complaint platform. A complaint is passed to the entity, which must answer within a set number of days; SEBI and a designated body monitor it.
- **SMART ODR** is online dispute resolution (**ODR**; SMART stands for Securities Market Approach for Resolution Through ODR): a conciliator, and then an arbitrator if conciliation fails, working on a platform instead of in a court.

This post describes how both work as written in SEBI's own FAQ (frequently asked questions) for SCORES (the October 2024 file: [SEBI SCORES 2.0 FAQ]({{ s.faq_url }})) and SEBI's investor pages on [SCORES]({{ s.investor_url }}) and [SMART ODR]({{ s.odr_url }}), as at {{ s.as_of }}. SEBI introduced the upgraded SCORES 2.0 in April 2024. It is part of [Your first year in the market]({{ '/series/market-basics/' | relative_url }}); the plumbing it protects is in [how accounts work]({% post_url 2026-12-01-demat-trading-bank-accounts %}) and [broker and counterparty risk]({% post_url 2026-10-21-broker-and-counterparty-risk %}).

It explains how to use the process, not what any complaint's merits are, and it is not legal advice.

## What SCORES covers

SEBI's FAQ says SCORES is for complaints about the securities market against listed companies, SEBI-registered intermediaries and market infrastructure institutions (the exchanges, depositories and clearing corporations). It also lists matters that SCORES does not consider, which include:

- complaints that are anonymous, incomplete or without supporting documents;
- disputes arising from a private agreement with a company or intermediary;
- complaints against unlisted or delisted companies;
- matters that belong to another regulator, such as the RBI (Reserve Bank of India), IRDAI (Insurance Regulatory and Development Authority of India) or PFRDA (Pension Fund Regulatory and Development Authority), or that are in court or in an ODR already.

That list is a selection from the FAQ, not the whole list. Read the FAQ before filing.

## The stages and day counts

| Stage | Who acts | Time allowed (calendar days), as printed |
|---|---|---|
| Lodge the complaint | You | Within {{ s.limitation_years }} year of the cause of action; SEBI may reject later ones |
| Entity's reply (ATR, action taken report; the ATR is the entity's written response to your complaint) | The broker, fund house or company | {{ s.atr_days }} days from receiving the complaint |
| First review | You ask; the designated body takes it up | You ask within {{ s.review_request_days }} days of the ATR; the body replies within {{ s.designated_days }} days |
| Second review | You ask; SEBI takes it up | You ask within {{ s.second_review_days }} days of the designated body's ATR |
| If the entity or designated body misses its deadline | The system | The complaint is escalated automatically to the next level |

SEBI's investor page says SCORES 2.0 cut the redressal timeline from 30 to 21 calendar days.

### Worked example: the clock for one complaint

Suppose {{ s.example_complaint }}, and you lodge a complaint on **day 0**. This is an illustrative case, not a real one.

- By **day {{ s.example_atr_day }}** the broker has to upload its ATR. If it does not, the complaint goes up a level automatically.
- If the ATR arrives on day {{ s.example_atr_day }} and you are not satisfied, you can ask for a review up to **day {{ s.example_review_last_day }}** ({{ s.review_request_days }} days after the ATR).
- If you do not ask, SEBI's FAQ treats the complaint as satisfied and it is disposed of after the {{ s.review_request_days }} days.

How long the designated body or SEBI actually takes after that is stated only as the {{ s.designated_days }}-day figure above; the FAQ does not promise a final answer by a date.

## What SMART ODR is, and how it links to SCORES

SEBI's investor page describes SMART ODR as a portal for disputes against regulated entities with a direct individual-investor interface, including stock brokers, depository participants, mutual funds and registrars. The steps, as SEBI describes them:

1. **Take the complaint to the intermediary first.** The page says this is a pre-requisite.
2. **Pre-conciliation.** The platform contacts both sides to try for an amicable settlement. SEBI's page says this stage is free for both.
3. **Conciliation.** Neutral conciliators help both sides agree. SEBI's page says the conciliation fee is paid by the market participant, not the investor: ₹{% include inr.html n=s.conciliation_ok_rs %} plus taxes if conciliation succeeds, ₹{% include inr.html n=s.conciliation_fail_rs %} plus taxes if it does not.
4. **Arbitration.** If conciliation fails, arbitration can start. The arbitrator's decision is binding on both sides. SEBI's page says the arbitration cost is "to be incurred by both initiator and respondent", so ODR is not free for the investor at this stage; the fee schedule is not stated here.

The two routes are linked. SEBI's FAQ (question 35) says that if you opt for ODR while a SCORES complaint is pending, the SCORES complaint is treated as disposed, and it lists a dispute pending in ODR as something SCORES will not take. So you pick one path rather than run both.

Two details this post does not state, because the sources it opened do not settle them: the **time limits for each ODR stage**, and the **current fee schedule**, which SEBI's page says to confirm in the circulars. The ODR circular is cited in SEBI's FAQ as {{ s.odr_circular }}; the sources we saw cite more than one circular number, so confirm the current reference on sebi.gov.in.

## Common mistakes

- **Expecting SCORES to decide the case.** SEBI's FAQ calls SCORES "only a facilitative platform" for getting redressal from the entity. Disputes that need adjudication on third-party rights or questions of law can be disposed of rather than decided there.
- **Skipping the intermediary before ODR.** SEBI's SMART ODR page says taking the complaint up with the intermediary first is a pre-requisite.
- **Filing a complaint about a bank or an insurer on SCORES.** Matters that sit with the RBI, IRDAI or PFRDA are listed as outside SCORES.
- **Letting a window lapse.** After the entity's ATR you have {{ s.review_request_days }} days to ask for a review, and a complaint filed more than a year after the cause of action may be rejected.

**Takeaway:** SCORES passes a complaint to the entity; SCORES then gives it {{ s.atr_days }} days to reply, with reviews to follow if you ask in time, and SMART ODR is the online conciliation and arbitration route. Confirm the current rules on sebi.gov.in, as the day counts and fees can change.
