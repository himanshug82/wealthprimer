---
layout: post
title: "The CAS: every holding on one statement"
seo_title: "Consolidated account statement (CAS): what it shows and when"
description: "The consolidated account statement lists your demat holdings and mutual fund units in one place. Who sends it, how often, and how it picks a depository."
image: /assets/og/consolidated-account-statement.png
date: 2027-02-14 09:00:00 +0530
series: market-basics
term: "CAS (consolidated account statement)"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign c = site.data.market_basics_m2.cas %}

## What the CAS is

A **consolidated account statement (CAS)** is a single statement of
everything you hold in the securities market: shares and other securities in
your demat accounts, and units in mutual fund folios, matched across them by
your PAN (permanent account number). It's sent by a depository, NSDL
(National Securities Depository Ltd) or CDSL (Central Depository Services
Ltd), the institutions that hold securities in electronic form.

It's the one document that shows your whole portfolio in one place, whichever
brokers and fund houses you've used. This post sets out the rules as read in
November 2026. It's part of
[Your first year in the market]({{ '/series/market-basics/' | relative_url }}),
after the post on [demat, trading and bank accounts]({% post_url 2026-12-11-demat-trading-bank-accounts %}).

## The rules

From the [Master Circular for Depositories of 3 December 2024]({{ c.mc_url }})
issued by SEBI (the Securities and Exchange Board of India), paragraphs 1.24
and 1.25. Paragraph 1.24 already includes the
[1 July 2024 circular]({{ c.c2024_url }}) that made email the default, and was
amended by the [circular of 14 February 2025]({{ c.c2025_url }}).

| Question | Rule |
|---|---|
| Who gets it from a depository? | Anyone whose PAN appears both in a demat account and in a mutual fund folio. Holdings are matched by PAN; for joint holdings, by the first holder's PAN and the pattern of holding |
| What if I have demat accounts but no fund units? | Paragraph 1.25 asks the depositories to send a CAS consolidated across both depositories in that case too, on the same terms |
| Who sends it otherwise? | If you have mutual fund units but no demat account, the fund houses' registrars (RTAs, registrar and transfer agents) send your CAS |
| Which depository, if you have accounts with both? | The one where your demat account was opened earlier, by default; you can ask for the other |
| How often? | Monthly if there was any transaction in any of your demat accounts or folios that month; half-yearly otherwise |
| How? | By email to your registered address by default (since {{ c.email_default_from }}), with a quarterly SMS (text message) saying which email it goes to; you can ask for paper instead |
| By when? (monthly) | Fund houses send their data to the depositories within {{ c.data_days }} days of the month end; email CAS within {{ c.ecas_days }} days; paper within {{ c.physical_days }} days (from {{ c.effective }}) |
| By when? (half-yearly) | Email by {{ c.half_yearly_ecas }}; paper by {{ c.half_yearly_physical }} (also from {{ c.effective }}) |
| Can I opt out? | Yes, by negative consent; the depository then tells the fund houses not to share your data |

Sending the CAS also counts as the depository participant's statement of
account to you, and as the fund house's statement under the mutual fund
regulations (paragraph 1.24.14).

## Worked example: one investor, two depositories

A hypothetical investor has:

- a demat account with an NSDL participant, opened in 2019,
- a second demat account with a CDSL participant, opened in 2022, and
- units in three mutual fund folios, all under the same PAN.

In {{ c.example_month }} she buys shares in one of the demat accounts.

1. **Who sends her CAS?** NSDL, by default, because that's where her earlier
   demat account is. It consolidates both demat accounts and all three folios.
2. **How often?** She transacted in {{ c.example_month }}, so she gets a
   monthly CAS for it.
3. **When?** By email by {{ c.example_ecas_by }}, or on paper by
   {{ c.example_physical_by }} if she has asked for paper.
4. **If she has a quiet month**, with no transaction anywhere, that month
   gets no monthly CAS; her holdings appear in the half-yearly one.

## Common mistakes

1. **Assuming no CAS means no holdings on record.** A quiet month produces
   no monthly CAS. Check the half-yearly one, or ask the depository.
2. **Missing it because of an old email address.** It goes to the email
   registered with the depository and the fund houses. If those differ or are
   out of date, the statement goes astray; the quarterly SMS shows which
   address is on file.
3. **Expecting it to show everything you own.** It covers securities in
   demat form and mutual fund units. Bank deposits, insurance policies and
   shares still held as paper certificates aren't on it.
4. **Treating it as a tax statement.** It lists holdings and transactions;
   it isn't a capital gains statement. Gains are worked out separately,
   which the [Tax series]({{ '/series/tax/' | relative_url }}) covers.

**Takeaway:** The CAS is one statement of every demat holding and mutual fund
unit under your PAN, sent by email by the depository where your oldest demat
account sits. It comes monthly if anything moved and half-yearly if nothing
did.

## Sources

- SEBI, [Master Circular for Depositories]({{ c.mc_url }}), 3 December 2024, paragraphs 1.24 and 1.25 (NSDL's reproduction, circular 2024-0176), read on 21 November 2026.
- SEBI circular SEBI/HO/MRD-PoD2/CIR/P/2024/93, [1 July 2024]({{ c.c2024_url }}): email as the default (built into the 2024 master circular).
- SEBI circular SEBI/HO/MRD/PoD1/CIR/P/2025/16, [14 February 2025]({{ c.c2025_url }}): revised timelines, effective {{ c.effective }}.
