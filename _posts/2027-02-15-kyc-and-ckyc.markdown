---
layout: post
title: "KYC and CKYC: why you verify once"
seo_title: "KYC vs CKYC: what KRAs and the central registry do"
description: "KYC records for the securities market sit with KYC registration agencies and the central KYC registry. What each one does, and why validated KYC travels."
image: /assets/og/kyc-and-ckyc.png
date: 2027-02-15 09:00:00 +0530
series: market-basics
term: "KYC, KRA and CKYC"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign k = site.data.market_basics_m2.kyc %}

## What KYC, KRA and CKYC are

**KYC (know your client)** is the identity and address check every
SEBI-registered intermediary (a broker, a depository participant, a fund
house) must do before you can transact. SEBI is the Securities and Exchange
Board of India. Two central record-keepers mean you shouldn't have to repeat
it with every new intermediary:

- A **KRA (KYC registration agency)** holds the KYC records of securities
  market clients, under SEBI's KRA Regulations of 2011.
- The **CKYCR (Central KYC Records Registry)**, run by CERSAI (the Central
  Registry of Securitisation Asset Reconstruction and Security Interest of
  India), holds KYC records across the financial sector, under the Prevention
  of Money-laundering Rules, 2005. A client's record there carries a **CKYC
  number**.

This post sets out what SEBI's KYC master circular says each one does, as read
in November 2026. It's part of
[Your first year in the market]({{ '/series/market-basics/' | relative_url }}),
after [demat, trading and bank accounts]({% post_url 2026-12-11-demat-trading-bank-accounts %}).

## The rules

From SEBI's [KYC master circular of 12 October 2023]({{ k.url }}):

| Step | Who | Rule (paragraph) |
|---|---|---|
| Upload to the KRA | The intermediary that did your KYC | Within {{ k.upload_kra_days }} working days of completing it (84) |
| Confirm to you | The KRA | A letter within {{ k.kra_letter_days }} working days of receiving your KYC documents (91) |
| Check the record | The KRA | Within 2 days, verify PAN (including that it's linked to Aadhaar), name and address, plus mobile number and email (96–97); a client whose details can't be verified can't transact further until they are (99) |
| Mark it validated | The KRA | Records verified against official databases, such as the Income Tax Department's PAN database or Aadhaar, become "validated records" (100) |
| Reuse it | The next intermediary | Validated records are portable: the client needn't do KYC again, and the intermediary fetches the record from the KRA (101) |
| Upload to the CKYCR | The intermediary | Within {{ k.ckyc_days }} days of starting the relationship (115) |

The table describes resident individuals. For individual non-resident
clients (people resident outside India, outside countries the Financial
Action Task Force lists as non-compliant) onboarded from 3 December 2026,
SEBI's [circular of 4 November 2026]({{ k.nov26_url }}) replaces these steps
to that extent: the KRA tags each detail as validated or not, and every KYC
record is portable, validated or not.

In {{ k.consultation }}, SEBI also consulted on simplifying client on-boarding
and the KRA framework. Changes that follow from it may alter some of these
steps, so check the current rule.

## Worked example: a second broker

A hypothetical investor did KYC with a broker last year, and the KRA marked
the record **validated** after checking PAN, name, address, mobile and email.
This year she opens an account with a second broker.

1. **The second broker fetches her record from the KRA** (paragraph 101).
   She doesn't repeat the full KYC process.
2. **If her address has changed**, she gives the broker the updated
   documents, and the KRA confirms the update to her by letter (paragraph 91).
3. **If her record had not been validated**, say the mobile number couldn't be
   verified, she couldn't transact further until it was (paragraph 99).

The CKYC number does a similar job across banks, insurers and other
regulated entities, under the Prevention of Money-laundering Rules.

## Common mistakes

1. **Thinking each new broker means full KYC again.** A validated KRA record
   is portable. What a new intermediary may still need is its own account
   opening forms and your consent.
2. **Treating every status other than "validated" alike.** A record whose
   details couldn't be verified stops you transacting (paragraph 99). One
   that was verified but not against official databases still works; it just
   isn't portable (paragraphs 100–101). Your broker or fund house can tell
   you your KRA status.
3. **Not updating details after a move or a new number.** The KRA verifies
   mobile and email, and a detail it can't verify can stop you transacting.
4. **Treating KYC as a one-off.** Records are updated when your details change,
   and intermediaries upload updated records to the CKYCR as they get them
   (paragraph 116).

**Takeaway:** KYC records for the securities market sit with KYC registration
agencies, and a validated record travels with you to the next broker or fund
house. Keep your PAN, address, mobile and email current, because an
unverified record can stop you transacting.

## Sources

- SEBI, [Master Circular on Know Your Client (KYC) norms for the securities market]({{ k.url }}), SEBI/HO/MIRSD/SECFATF/P/CIR/2023/169, 12 October 2023, paragraphs 82–101 and 113–117, read on 21 November 2026.
- SEBI circular HO/38/30/12(3)2026-MIRSD-POD2/I/25175/2026, [4 November 2026]({{ k.nov26_url }}): KYC for individual non-resident clients, paragraphs 4.2, 7 and 8, read on 21 November 2026.
