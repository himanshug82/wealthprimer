---
layout: post
title: "Before you file: the statement, the AIS, and what to reconcile"
description: "The department already holds most of your numbers. Reconciling a capital gains statement against the AIS, and the checks worth doing before you submit."
image: /assets/og/before-you-file.png
date: 2026-11-04 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Educational content, not tax
advice — and filing in particular is worth professional help if the amounts
are meaningful.*

## The documents, and why reconciliation matters

Eight posts of rules. This one is about the practical end: the papers you
work from, and the checks worth doing before anything is submitted.

The premise is simple and worth stating bluntly. **The tax department already
has most of this data.** Mutual funds, brokers, banks and registrars report
transactions against your PAN. Filing isn't telling them what happened; it's
agreeing with a record they already hold. Notices overwhelmingly arise from
mismatches, not from honest arithmetic errors.

## The three documents

| Document | What it holds | Where it comes from |
|---|---|---|
| **Capital gains statement** | Every redemption, matched to purchase lots, with gains split long/short | Your fund house, registrar (CAMS/KFintech) or broker |
| **Form 26AS** | Tax deducted and deposited against your PAN | The income tax portal |
| **Annual Information Statement (AIS)** | Broader: dividends, interest, securities transactions, deposits | The income tax portal |

The capital gains statement is the one that saves the most work. A
consolidated statement from CAMS or KFintech covers most fund houses at once
and does the FIFO matching for you — which, as
[the SIP post]({% post_url 2026-11-02-sips-and-fifo %}) showed, is genuinely tedious by
hand when a single redemption touches sixty lots.

## Reading a capital gains statement

Expect columns roughly like these, per redemption:

| Column | What to check |
|---|---|
| Purchase date | Determines the holding period — and whether FIFO matched what you expected |
| Purchase value | Should reflect grandfathering on pre-Feb-2018 equity |
| Sale date and value | The transfer, not when money reached your bank |
| Short-term gain | Taxed at {{ r.equity_stcg_pct }}% for equity |
| Long-term gain | {{ r.equity_ltcg_pct }}% above the ₹{% include inr.html n=r.ltcg_annual_exemption %} annual exemption |

Four things worth verifying rather than assuming:

**Grandfathering has been applied.** For equity bought on or before 31
January 2018, the cost should be the higher of actual cost and the 31 January
2018 value. Some statements handle this cleanly; check rather than assume, as
[the equity post]({% post_url 2026-10-29-equity-and-equity-funds %}) showed it can exclude
a substantial slice of gain.

**Debt units are split by purchase date.** Units bought before and on/after
1 April 2023 follow different rules, per
[the debt post]({% post_url 2026-10-30-debt-funds-gold-and-the-rest %}). If the statement
doesn't distinguish them, chase it.

**The exemption is applied once, across everything.** A statement from one
fund house can't know about your gains elsewhere. Aggregate across all
sources yourself before applying the ₹{% include inr.html n=r.ltcg_annual_exemption %}.

**Switches appear as redemptions.** Every switch is a sale. If you switched
plans or schemes during the year, those transactions belong in the gain
computation even though no money reached your bank.

## Checking the AIS

Open the AIS and compare it against your own records. What you're looking for
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

## The checklist

1. **Download the consolidated capital gains statement** for the full
   financial year, from every registrar and broker you used.
2. **Aggregate long-term gains across all sources**, then apply the
   ₹{% include inr.html n=r.ltcg_annual_exemption %} exemption once.
3. **Check grandfathering** on anything bought before February 2018.
4. **Separate pre- and post-April-2023 debt units.**
5. **Include switches** as redemptions.
6. **Apply losses** — this year's, then anything carried forward, respecting
   [the set-off rules]({% post_url 2026-11-01-losses-set-off-and-harvesting %}).
7. **Reconcile against the AIS**, and file feedback on anything wrong.
8. **Check TDS in Form 26AS** and claim credit for it.
9. **Add {{ r.cess_pct }}% cess** on the computed tax.
10. **File by the due date** — non-negotiable if you have losses to carry
    forward, since late filing destroys them.
11. **Keep the records.** Purchase dates and costs matter for as long as you
    hold the asset, which may be decades.

That last point is quietly the most important. The single most common
practical problem in Indian investment tax isn't a misunderstood rule — it's
someone unable to establish what they paid for shares bought fifteen years
ago, through a broker that no longer exists.

## What this series didn't cover

Being clear about the edges, in the spirit of the honest closing posts in the
[technical analysis]({% post_url 2026-10-17-what-technical-analysis-cannot-do %}) and
[mutual funds]({% post_url 2026-10-26-reading-a-factsheet %}) series.

- **Non-resident taxation.** NRIs face different rules, TDS on redemptions,
  and potentially a double-taxation treaty. Genuinely different subject.
- **Business income from trading.** Frequent trading, and derivatives in
  particular, can be treated as business income rather than capital gains —
  different rules, different forms, possibly an audit requirement.
- **Property in detail.** Reinvestment reliefs, the transitional rate option,
  and strict deadlines. Large amounts and real complexity.
- **Estate and gift matters.** Inheritance, gifting between relatives, and
  how holding periods and costs carry across.
- **Anything contested.** Notices, appeals, and disputes are not
  self-service.

And the standing caveat for this whole series: rates and rules change with
every Budget, and the **Income-tax Act, 2025** replaced the 1961 Act from
1 April 2026 — carrying the rates over but renumbering nearly everything and
replacing "Previous Year" and "Assessment Year" with a single **Tax Year**.
Anything you read that predates 2026, including section references, needs
checking against the current position.

**Takeaway:** Filing is mostly reconciliation — the department already holds
the data, so the work is making your records agree with it, and mismatches
are what generate notices. Aggregate long-term gains across every source
before applying the single annual exemption, check grandfathering on old
holdings, treat switches as sales, and file on time so your losses survive.
Then keep the purchase records, because you will need them long after you've
forgotten this post.
