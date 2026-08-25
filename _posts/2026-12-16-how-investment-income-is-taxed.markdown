---
layout: post
title: "How investment income is taxed in India: the map"
date: 2026-12-16 09:00:00 +0530
series: tax
---

{% assign t = site.data.tax %}
{% assign r = t.rates %}

*Rules described here apply to **{{ r.financial_year }}**. Tax rules change with each
Budget — check anything important against the current position before acting
on it. This is educational content, not tax advice; if the amounts matter,
talk to someone who files professionally.*

## Why this series exists

Fifty-nine posts on this blog have been about what an investment is worth.
None of them mentioned that you don't keep all of it.

Tax is the largest, most predictable drag on long-term returns after fees —
and unlike returns, it's substantially within your control. Not through
anything clever or aggressive, but through knowing which rules apply to what,
and when. A gain realised eleven months in and a gain realised thirteen
months in are taxed differently for no reason except the calendar.

This series covers the mechanics. It won't tell you what to do.

## A note on how this series is written

Indian tax law was rewritten recently. The **Income-tax Act, 2025** replaced
the 1961 Act with effect from 1 April 2026, and while the rates and slabs
carried over unchanged, almost every section was renumbered — the old section
80C became 123 — and the twin concepts of "Previous Year" and "Assessment
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
rules, their own exemption, and their own loss rules — which is why seven of
the nine posts in this series are about them.

**Nothing is taxed until you sell.** A holding that has quadrupled owes
nothing while you hold it. Tax on capital gains is triggered by the
*transaction*, not by the gain existing. That single fact does more work in
practical tax outcomes than any technique.

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

The big one people miss: the first case costs nothing, forever, until you
sell. Holding isn't a taxable event. Selling is.

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
| Unlisted shares, property, gold, most other assets | **{{ r.other_holding_months }} months** |

And the rates for listed equity and equity funds:

| | Rate |
|---|---:|
| Short-term (≤ {{ r.equity_holding_months }} months) | {{ r.equity_stcg_pct }}% |
| Long-term (> {{ r.equity_holding_months }} months) | {{ r.equity_ltcg_pct }}%, on gains above ₹{% include inr.html n=r.ltcg_annual_exemption %} a year |

There is also a **{{ r.cess_pct }}% health and education cess** applied on top of the tax
itself — not on the gain. It's small, it's easy to forget, and it makes a
12.5% headline rate an effective 13%. Most published examples omit it; the
worked examples in this series include it.

The next post is entirely about that
holding-period line, because a day either side of it changes the rate by
7.5 percentage points.

## One trap worth knowing now

Debt mutual funds no longer work the way most older articles describe. Units
of specified debt funds bought **on or after 1 April 2023** are taxed at your
slab rate regardless of how long you hold them — no long-term rate, no
indexation benefit, no reward for patience.

If you're reading an article that mentions indexation on debt funds, check
its date. That's post four in this series.

## What this series covers

| Post | Covers |
|---|---|
| Short-term vs long-term | The holding-period line, and why the date matters |
| Equity and equity funds | The {{ r.equity_stcg_pct }}%/{{ r.equity_ltcg_pct }}% rates, the exemption, grandfathering |
| Debt, gold and the rest | Where the slab rate applies instead |
| Dividends and interest | Slab rate, and TDS arriving before you file |
| Losses | Set-off, carry-forward, and harvesting |
| SIPs and FIFO | Why one redemption is many separate tax lots |
| ELSS and deductions | What survived the move to the new regime |
| Before you file | Reading a capital gains statement against your AIS |

Every worked example runs on the real fund NAV history used in the
[Mutual Funds series]({% post_url 2026-11-28-what-a-mutual-fund-is %}), so the tax arithmetic sits on
actual prices rather than round invented numbers.

## Common mistakes

- **Thinking unrealised gains are taxed.** They aren't. Nothing is due until
  you sell.
- **Using one holding-period rule for everything.** Twelve months for listed
  equity, twenty-four for most other assets. Applying the equity rule to gold
  or property gets it wrong.
- **Reading pre-2023 articles on debt funds.** Indexation on debt funds
  bought from April 2023 no longer exists.
- **Forgetting the cess.** It's {{ r.cess_pct }}% on the tax, not on the gain — small, but it
  makes 12.5% into 13%.
- **Assuming the fund deducts tax for you.** For resident investors, mutual
  funds generally do not deduct tax on capital gains at redemption. The money
  arrives whole and the liability is yours.
- **Trusting section numbers from older articles.** With the 2025 Act in
  force, the numbering in anything written before 2026 no longer matches.

**Takeaway:** Investment income splits into capital gains, dividends and
interest, and only the first has rules of its own — its rate turns on what
you held and for how long. Nothing is owed until you sell, which makes the
decision to sell the single most consequential tax decision most investors
make, usually without noticing they've made it.
