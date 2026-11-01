---
layout: post
title: "How investment income is taxed in India: the map"
description: "Capital gains, dividends and interest are taxed under genuinely different rules. The map of how investment income is taxed in India, mechanics first."
image: /assets/og/how-investment-income-is-taxed.png
date: 2026-11-02 09:00:00 +0530
series: tax
needs_review: tax
rules_for: "Tax Year 2026-27 (FY 2026-27)"
rules_as_of: "August 2026"
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

## Why this series exists

The posts on this blog so far have been about what an investment is worth.
None of them mentioned that you don't keep all of it.

Tax is one of the costs that sits between an investment's return and what you
keep, alongside fees. This series is about **Tax Year 2026-27 (FY 2026-27)**,
the year starting 1 April 2026 (FY is *financial year*). The rules differ by
type of income, and by how long an asset was held: a gain realised eleven
months in and a gain realised thirteen months in are taxed differently for no
reason except the calendar.

This series covers the mechanics. It won't tell you what to do.

## A note on how this series is written

Indian tax law was rewritten recently. The **Income-tax Act, 2025** replaced
the 1961 Act with effect from 1 April 2026, and while the rates and slabs
carried over unchanged, almost every section was renumbered — the old section
80C became section 123 — and the twin concepts of "Previous Year" and "Assessment
Year" were collapsed into a single **Tax Year**.

So this series teaches *mechanics* rather than citations. Holding periods,
rates, set-off rules and the FIFO convention are stable; section numbers are
not, and a post built around them would be stale before it was useful. Where
you need to cite chapter and verse — filing, disputes, anything contested —
that's a job for a professional and the current text of the Act.

## Three kinds of investment income

Almost everything an investment pays you falls into one of three buckets, and
they are taxed under genuinely different rules. Getting the bucket right is
most of the work.

| | What it is | Broadly how it's taxed |
|---|---|---|
| **Capital gains** | Profit from selling an asset for more than you paid | Depends on the asset *and* how long you held it |
| **Dividends** | A share of profits paid out by a company or fund | Added to your income, taxed at your slab rate |
| **Interest** | Paid on deposits, bonds, some debt instruments | Added to your income, taxed at your slab rate |

Two things follow immediately.

**Capital gains are the complicated one.** Dividends and interest simply join
your income. Capital gains have their own rates, their own holding-period
rules, their own exemption, and their own loss rules — which is why most of
the posts in this series are about them.

**A capital gain is taxed when you sell, not while you hold.** A holding that
has quadrupled has no capital gains tax due while you hold it. Tax on capital
gains is triggered by the *transaction*, not by the gain existing. (Dividends
and interest are different: they can be taxed as they are received or accrue,
and tax can be deducted at source before you sell anything. Later posts cover
both.)

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you collect trading cards.

- If a card you own becomes more valuable, nobody asks you for anything. You
  just own a better card. That's an *unrealised* gain.
- The moment you **sell** it for more than you paid, the profit counts, and a
  slice goes in tax. That's a **capital gain**.
- If the card company sends you a small payment just for owning the card,
  that's like a **dividend** — and it counts as income the moment it arrives,
  whether you wanted it or not.

The big one people miss: a card going up in value triggers no capital gains
tax until you sell. Holding isn't a taxable event. Selling is.

</details>

## The single most important variable

For capital gains, the question that decides almost everything is: **how long
did you hold it?**

```
Held for a SHORT period   ->  Short-Term Capital Gain (STCG)
Held for a LONG period    ->  Long-Term Capital Gain (LTCG)
```

Where the line falls depends on the asset:

| Asset | Long-term after |
|---|---|
| Listed shares, equity mutual funds | **{{ r.equity_holding_months }} months** |
| Unlisted shares, property, physical gold and many other assets | **{{ r.other_holding_months }} months** (some listed instruments differ; check the asset) |

And the rates for listed equity and equity funds:

| | Rate |
|---|---:|
| Short-term (≤ {{ r.equity_holding_months }} months) | {{ r.equity_stcg_pct }}% |
| Long-term (> {{ r.equity_holding_months }} months) | {{ r.equity_ltcg_pct }}%, on gains above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year |

There is also a **{{ r.cess_pct }}% health and education cess** applied on top of the tax
itself — not on the gain. It's small, it's easy to forget, and it makes a
{{ r.equity_ltcg_pct }}% headline rate an effective {{ r.equity_ltcg_pct | times: 1.04 | round: 2 }}%. Most published examples omit it; the
worked examples in this series include it.

Above ₹50 lakh of total income a **surcharge** is added to the tax too, before
the cess. The Memorandum to the Finance Bill, 2026 (listed under Sources) shows
the surcharge on equity capital gains and dividends capped at 15%, and the
highest surcharge rate on other income cut from 37% to 25% under the new
regime. The Bill is not the enacted Act, and the old-regime position was not
re-checked, so check the current rule. The worked examples in this series
assume income below ₹50 lakh, so no surcharge.

The next post is entirely about that
holding-period line, because a day either side of it changes the rate by
7.5 percentage points.

## One thing that has changed

Debt mutual funds no longer work the way many older articles describe. Gains
on units of "specified" debt funds acquired on or after 1 April 2023 are taxed
at the investor's slab rate whatever the holding period, and indexation is
gone for sales from 23 July 2024. If you're reading an article that mentions
indexation on debt funds, check its date and check the current rule. The debt
funds post in this series covers the definition.

## Where the rest of the series goes

Later posts take each bucket in turn — gains on equity and on debt, dividends
and interest, losses, SIPs, deductions, filing, and the special cases. The
[series page]({{ '/series/tax/' | relative_url }}) lists them in order.

The worked examples in the core posts of this series run on the real NAV (net asset
value, a fund's per-unit price) history used in the
[Mutual Funds series]({% post_url 2026-09-25-what-a-mutual-fund-is %}) — UTI Nifty 50 Index
Fund (regular plan, growth), NAVs from AMFI (the Association of Mutual Funds in
India), as of 31 March 2026, used for illustration only — so the tax
arithmetic sits on actual prices rather than round invented numbers.

## Common mistakes

- **Thinking unrealised gains are taxed.** Capital gains tax isn't due on a
  gain you haven't realised by selling.
- **Using one holding-period rule for everything.** Twelve months for listed
  equity, twenty-four for most other assets. Applying the equity rule to gold
  or property gets it wrong.
- **Reading pre-2023 articles on debt funds.** Indexation on debt funds is
  gone for sales on or after 23 July 2024, and the rules for specified funds
  changed; check the current rule.
- **Forgetting the cess.** It's {{ r.cess_pct }}% on the tax, not on the gain — small, but it
  lifts a {{ r.equity_ltcg_pct }}% rate to an effective {{ r.equity_ltcg_pct | times: 1.04 | round: 2 }}%.
- **Assuming the fund deducts tax for you.** For resident investors, mutual
  funds generally do not deduct tax on capital gains at redemption. The money
  arrives whole and the liability is yours.

## Sources

- [Income-tax Act, 2025 (a copy hosted by ICAI)](https://resource.cdn.icai.org/87647dtc-aps2139-inceome-tax-act-2025.pdf): the Act itself.
- [Finance Act, 2026, Gazette of India](https://egazette.gov.in/WriteReadData/2026/271439.pdf): the Finance Act that made the 2026 changes.
- [Memorandum explaining the provisions of the Finance Bill, 2026](https://www.indiabudget.gov.in/doc/memo.pdf): the government's explanation of those changes.

**Takeaway:** Investment income splits into capital gains, dividends and interest, and only the first has rules of its own, with a rate that turns on what you held and for how long. A capital gain is taxed when you sell; dividends and interest follow their own timing.
