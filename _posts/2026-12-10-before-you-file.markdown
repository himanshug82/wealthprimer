---
layout: post
title: "Before you file: the statement, the AIS, and what to reconcile"
seo_title: "Before you file: the AIS and what to reconcile"
description: "The department already holds most of your numbers. Reconciling a capital gains statement against the AIS, and the checks worth doing before you submit."
image: /assets/og/before-you-file.png
date: 2026-12-10 09:00:00 +0530
series: tax
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "November 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## The documents, and why reconciliation matters

The earlier posts in this series covered the rules for Tax Year 2026-27 (FY, or financial year, 2026-27), as at November 2026. A return filed in December 2026 relates to an earlier year (FY 2025-26), which on this post's own account (the 2025 Act took effect from 1 April 2026) falls under the earlier Income-tax Act, 1961. The rules described in this series are those of the 2025 Act, as read; where the 1961 Act's rule for that year is the same is not confirmed here, so check the current rule for the year you are filing. This one is about the practical end: the papers you
work from, and the checks that reconciliation involves before anything is submitted.

The premise is simple and worth stating bluntly. **The tax department already
has much of this data** (as we understand how the reporting works). Mutual funds, brokers, banks and registrars report
transactions against your PAN (permanent account number). Filing isn't
telling them what happened; it's agreeing with a record they already hold. In our view, a mismatch between what you report and what
the department holds is a likelier source of a query than an arithmetic slip.

## The three documents

| Document | What it holds | Where it comes from |
|---|---|---|
| **Capital gains statement** | Every redemption, matched to purchase lots, with gains split long/short | Your fund house, registrar (CAMS, Computer Age Management Services, or KFintech) or broker |
| **Tax credit statement (historically Form 26AS)** | Tax deducted and deposited against your PAN. Check the current form names under the new Rules. | The income tax portal |
| **Annual Information Statement (AIS)** | Broader: dividends, interest, securities transactions, deposits | The income tax portal |

The capital gains statement is the one that saves the most work. Registrars and platforms offer capital gains statements, and
some statements do the FIFO (first in, first out) matching for you; check what yours covers. As
[the SIP (systematic investment plan) post]({% post_url 2026-11-20-sips-and-fifo %}) showed, the matching is tedious by
hand when a single redemption touches sixty lots.

## Reading a capital gains statement

Expect columns roughly like these, per redemption:

| Column | What to check |
|---|---|
| Purchase date | Determines the holding period — and whether FIFO matched what you expected |
| Purchase value | Should reflect grandfathering on pre-Feb-2018 equity |
| Sale date and value | The transfer, not when money reached your bank |
| Short-term gain | Taxed at {{ r.equity_stcg_pct }}% for listed equity with STT (securities transaction tax) paid, as read in the 2025 Act; check the 1961 Act's text for FY 2025-26 |
| Long-term gain | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption |

Four things to verify rather than assume:

**Grandfathering has been applied.** For equity bought on or before 31
January 2018, the cost should be the higher of actual cost and the 31 January
2018 value (that value capped at the sale price), as the equity post describes. Some statements handle this cleanly; check rather than assume, as
[the equity post]({% post_url 2026-11-08-equity-and-equity-funds %}) showed it can exclude
a substantial slice of gain.

**Debt units are split by purchase date.** Units bought before and on/after
1 April 2023 have followed different rules, per
[the debt post]({% post_url 2026-12-04-debt-funds-gold-and-the-rest %}), which also notes that the definitions have changed since and need checking. If the statement
doesn't distinguish them, ask the provider.

**The exemption is applied once, across everything.** A statement from one
fund house can't know about your gains elsewhere. Aggregate across all
sources yourself before applying the ₹{% include inr.html n=r.ltcg_annual_exemption %}.

**Switches appear as redemptions.** A switch is generally treated as a sale. If you switched
plans or schemes during the year, those transactions belong in the gain
computation even though no money reached your bank.

## Checking the AIS

Open the AIS (Annual Information Statement) and compare it against your own records. What you're looking for
is anything in one and not the other, in either direction.

- **Dividends** reported by companies and funds
- **Interest** from banks and bonds
- **Securities transactions** reported by brokers and registrars

Two practical points. The AIS has a **feedback mechanism** — if an entry is
wrong or duplicated, you can flag it rather than silently reporting something
different. And the AIS is **not always complete or correct**: it can miss
things and occasionally double-count. It is a cross-check, not the truth.
Where your records and the AIS disagree, work out which is right instead of
deferring to either automatically.

## What reconciliation involves

The list below describes the steps reconciliation typically involves; it is a description of the process, not a prescription.

1. **The consolidated capital gains statement** for the full
   financial year, from every registrar and broker used.
2. **Long-term gains aggregated across all sources**, with the
   ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption applied once.
3. **Grandfathering** on anything bought before February 2018.
4. **Pre- and post-April-2023 debt units** kept separate.
5. **Switches** counted as redemptions.
6. **Losses applied** — this year's, then anything carried forward, respecting
   [the set-off rules]({% post_url 2026-11-16-losses-set-off-and-harvesting %}).
7. **Reconciliation against the AIS**, with feedback filed on anything wrong.
8. **TDS (tax deducted at source) in the tax credit statement**, checked so that credit can be claimed for it.
9. **Whether surcharge applies.** Above ₹50 lakh of total income a
   surcharge is added to the tax. The Finance Act, 2026 sets the surcharge for the assessment year starting 1 April 2026 (section 2 and the First Schedule, Part I-A), with a 15% cap on dividends and
   the special-rate capital gains, and a highest rate of 25% under the new regime.
10. **{{ r.cess_pct }}% cess** added on the computed tax (after any surcharge).
11. **Filing by the due date.** As the ICAI (Institute of Chartered Accountants of India) copy of the Income-tax Act, 2025 reads, and as we assume the earlier Act's position for FY 2025-26 is similar (not checked), carrying forward most
    capital losses requires a return filed by the due date; the rules differ by
    type of loss (house property losses, for instance), so check the current rule for yours.
12. **Records kept.** Purchase dates and costs matter for as long as you
    hold the asset, which may be decades.

That last point is quietly the most important. In our view, a common
practical problem in Indian investment tax isn't a misunderstood rule — it's
someone unable to establish what they paid for shares bought fifteen years
ago, through a broker that no longer exists.

## Common mistakes

- **Reading a statement as final.** A statement is a record from the provider's side. It can miss grandfathering, treat switches differently or know nothing about gains elsewhere.
- **Assuming the portal data is complete.** The AIS is built from what others report. Gaps and errors exist, which is why it has a feedback option.
- **Applying the exemption once per statement.** The annual exemption applies across all of a year's long-term equity gains, not to each fund house separately.
- **Throwing away old purchase records.** Cost and date are needed for as long as you hold the asset.

## What this series doesn't cover

Being clear about the edges, in the spirit of the honest closing posts in the
[technical analysis]({% post_url 2026-10-11-what-technical-analysis-cannot-do %}) and
[mutual funds]({% post_url 2026-10-11-reading-a-factsheet %}) series.

Later posts in this series cover other topics. Some edges stay uncovered:

- **Property in detail.** Reinvestment reliefs, the transitional rate option,
  and strict deadlines. Large amounts and real complexity.
- **Inheritance and estates.** How holding periods and costs carry across
  when assets pass on death, and estate planning generally.
- **Anything contested.** Notices, appeals, and disputes are not
  self-service.

And the standing caveat for this whole series: rates and rules change with
every Budget, and the **Income-tax Act, 2025** replaced the 1961 Act from
1 April 2026 — renumbering nearly everything and
replacing "Previous Year" and "Assessment Year" with a single **Tax Year**.
Anything you read that predates 2026, including section references, needs
checking against the current position.

## Sources

- [Income-tax Act, 2025 (a copy hosted by the Institute of Chartered Accountants of India, ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026 (No. 4 of 2026)](https://egazette.gov.in/WriteReadData/2026/271439.pdf), Gazette of India, 30 March 2026: opened 2 November 2026 for the surcharge. The Income-tax Act, 1961 was not opened.

**Takeaway:** Filing is mostly reconciliation — the department already holds
the data, so the work is making your records agree with it, and, in our view,
mismatches are a likelier source of queries than arithmetic slips. The single annual exemption applies to long-term gains aggregated across every source, grandfathering matters on old holdings, and switches count as sales.
Purchase records matter for as long as you hold the asset.
