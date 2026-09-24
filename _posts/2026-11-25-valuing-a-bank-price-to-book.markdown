---
layout: post
title: "Valuing a bank: why price-to-book is the anchor, and what justifies it"
description: "Banks are valued on book because their assets are mostly money near fair value. How P/B, ROE and cost of equity fit together, and why ROA × leverage is the key."
image: /assets/og/valuing-a-bank-price-to-book.png
date: 2026-11-25 09:00:00 +0530
series: fundamental-analysis
term: "Price-to-book for banks"
---

{% assign b = site.data.real_bank %}
{% assign f25 = b.reported.FY25 %}
{% assign d = b.derived_fy25 %}
{% assign v = b.valuation %}
{% assign mk = b.market %}
{% assign mcap_lakh_cr = v.market_cap_cr | divided_by: 100000 | round: 2 %}

## Why not P/E, and definitely not DCF

For most companies this blog has anchored valuation on
[P/E]({% post_url 2026-09-24-price-to-earnings %}) and, when the cash flows
could be forecast, a [DCF]({% post_url 2026-10-05-terminal-value-and-the-full-dcf %}).
Neither works cleanly for a bank.

A DCF needs free cash flow, and for a bank that number is close to
meaningless: taking in deposits looks like a cash inflow, lending them out
looks like an outflow, and the "capex" line is nearly empty. P/E works, but
it sits on top of a profit figure that the
[provisions post]({% post_url 2026-11-23-gnpa-nnpa-and-provisions %}) showed
to be partly discretionary and strongly cyclical — the same bank can post
half the profit in a bad credit year with no change in franchise.

What a bank does have is a balance sheet where most assets are financial —
loans, bonds, cash — carried at, or close to, what they are worth. A factory's
book value is an accounting artefact of old purchase prices and depreciation
schedules. A bank's book value is a reasonable first estimate of what the
shareholders actually own. That is why bank valuation starts from
**[price-to-book]({% post_url 2026-09-25-price-to-book %})**.

## The formula, and the identity behind it

```
P/B  =  Price per share  /  Book value per share

and, because P/E = Price / EPS and ROE = EPS / Book value per share,

P/B  =  P/E  ×  ROE
```

That identity is the key to the whole subject. A bank's P/B is high when the
market pays a lot for each rupee of earnings *and* the bank earns a lot on
each rupee of book. Two banks with the same P/E can have wildly different P/B
purely because one earns a 16% return on its equity and the other 8%.

## Worked example: HDFC Bank at 30 June 2025

Financials from HDFC Bank's [results for the year ended 31 March 2025]({{ b.company.source_url }})
(standalone). Price: NSE (National Stock Exchange) close on {{ mk.price_date }}, from
[Yahoo Finance]({{ mk.source_url }}). Historical, for illustration only.

One wrinkle first. HDFC Bank issued 1:1 bonus shares (record date
{{ mk.bonus_record_date }}), so price databases now show pre-bonus dates at
half the price actually traded: Yahoo shows ₹{% include inr.html n=mk.price_adjusted_yahoo %}
for 30 June 2025, when the share changed hands at about
₹{% include inr.html n=mk.price %}. The FY25 EPS and book value are on the
pre-bonus share count, so the *pre-bonus* price is the consistent one to pair
with them. Mixing an adjusted price with unadjusted per-share figures would
halve every multiple below.

| | |
|---|---:|
| Shareholders' equity (capital + reserves), 31 Mar 2025 | ₹{% include inr.html n=f25.shareholders_equity %} crore |
| Shares outstanding (face value ₹1 → capital ₹{{ f25.capital }} crore) | {{ f25.shares_cr }} crore |
| **Book value per share** | **₹{% include inr.html n=f25.book_value_per_share %}** |
| Price, 30 June 2025 (pre-bonus basis) | ₹{% include inr.html n=mk.price %} |
| **P/B** | **{{ v.pb }}x** |
| EPS (basic), FY25 | ₹{{ f25.eps_basic }} |
| **P/E** | **{{ v.pe }}x** |
| ROE on closing equity (PAT / equity) | {{ v.roe_on_closing_equity_pct }}% |
| P/E × ROE (identity check) | {{ v.pe_x_roe_check }}x |
| Market capitalisation | ≈ ₹{{ mcap_lakh_cr }} lakh crore |
| Dividend yield (₹{{ mk.dividend_per_share_fy25 }} FY25 dividend) | {{ v.dividend_yield_pct }}% |

The identity holds to rounding: {{ v.pe }} × {{ v.roe_on_closing_equity_pct }}%
≈ {{ v.pe_x_roe_check }}x. (Using ROE on *average* equity —
{{ d.roe_pct }}% — would shift both terms slightly; the identity only closes
exactly when P/E, ROE and book value share one basis.)

## What justifies a P/B above 1

A bank trading at book value is being valued at what its shareholders
nominally own. Above 1, the market is paying for the *return* the bank earns
on that book being higher than what shareholders could demand elsewhere.
Below 1, it is saying the opposite — or that the book value isn't real.

The textbook expression, from the dividend-discount model:

```
Justified P/B  =  (ROE − g)  /  (Ke − g)

where  Ke = cost of equity (see the WACC post)
       g  = sustainable long-run growth
```

If a bank earns exactly its cost of equity (ROE = Ke), the fraction is 1 —
it deserves to trade at book. Every point of ROE above Ke pushes the
justified multiple up; every point of Ke above ROE pushes it below 1.

Here is the formula applied to a generic bank earning a {{ v.justified_pb_illustrative_roe_pct }}% ROE — a round
number in the neighbourhood of large Indian private banks, not HDFC Bank's —
with *illustrative* pairs of the two inputs nobody can observe. Growth is
kept at or below the roughly 10% long-run nominal growth ceiling from the
[terminal value post]({% post_url 2026-10-05-terminal-value-and-the-full-dcf %}),
and the last row is the aggressive case, with g creeping up to within two
points of Ke:

| Scenario | Cost of equity | Growth | Justified P/B |
|---|---:|---:|---:|{% for s in v.justified_pb_scenarios %}
| {{ s.label }} | {{ s.cost_of_equity_pct }}% | {{ s.growth_pct }}% | **{{ s.pb }}x** |{% endfor %}

Read that table for what it actually demonstrates. One percentage point on
each of two unobservable inputs (A to B) moves the "justified" multiple from
about {{ v.justified_pb_scenarios[0].pb }}x to {{ v.justified_pb_scenarios[1].pb }}x. Two points on each (A to C) takes it
to {{ v.justified_pb_scenarios[2].pb }}x, and pushing g close to Ke (D) gets you
{{ v.justified_pb_scenarios[3].pb }}x — the same g-too-close-to-r blow-up the terminal value post
warned about. Same bank, same ROE, more than double the answer from inputs
nobody can observe. The formula is a way to *think* about why
multiples differ. It is not a way to decide whether one is right, and this
post doesn't try. (The [margin of safety post]({% post_url 2026-10-06-margin-of-safety-and-sensitivity %})
made the same point about DCF inputs; banks just make it faster.)

## ROA × leverage: where the ROE comes from

The [DuPont]({% post_url 2026-09-30-dupont-roe-decomposition %}) post split
ROE into margin, turnover and leverage. For a bank the first two collapse
into one number — [return on assets]({% post_url 2026-09-05-roa %}) — and the
decomposition becomes:

```
ROE  =  ROA  ×  (Average assets / Average equity)
```

| | FY25 |
|---|---:|
| ROA (PAT / average total assets) | {{ d.roa_pct }}% |
| × Leverage (average assets / average equity) | {{ d.avg_leverage }}x |
| **= ROE** | **{{ d.roa_x_leverage_pct }}%** (direct: {{ d.roe_pct }}%) |

This is the most useful two-line summary of any bank. ROA says how well it
lends: HDFC Bank earned about ₹{{ d.roa_pct }} on every ₹100 of assets. Leverage says
how many times that thin return is multiplied for shareholders: about
{{ d.avg_leverage }} times. The [capital adequacy post]({% post_url 2026-11-24-capital-adequacy %})
is what caps the second number; the [NIM]({% post_url 2026-11-21-nim-and-the-spread %}),
[CASA]({% post_url 2026-11-22-casa-and-the-deposit-franchise %}) and
[provisions]({% post_url 2026-11-23-gnpa-nnpa-and-provisions %}) posts are what
drive the first.

Two banks with the same ROE can be very different animals: one earning 2% on
assets at 7x leverage, another earning 1% at 14x. Same ROE, half the
cushion. Always split it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine two piggy banks. Each has ₹100 inside — that's the *book value*.

Piggy A somehow turns its ₹100 into ₹115 every year. Piggy B only manages
₹107. If someone offered to sell you Piggy A for ₹150 and Piggy B for ₹150,
you'd obviously pick A — it earns more on the same ₹100.

So people will pay *more than ₹100* for Piggy A, and how much more depends
on how much better than "normal" its ₹15 a year is. That's P/B: price over
the ₹100 inside, justified by how hard the ₹100 works.

</details>

## Where P/E still helps

P/E isn't useless for banks; it's a cross-check. When P/B and P/E disagree —
a high P/B with a modest P/E — it means ROE is unusually high, and the
question becomes whether that ROE is sustainable or a good year in the credit
cycle. When P/B is low and P/E is high, profits are depressed and the market
is valuing the book, not the year. Read the pair together.

Book value itself also deserves scrutiny. It is "close to fair" only if the
loans are worth what they're carried at — which loops straight back to
provision coverage. A bank with thin coverage and a rising NPA book has a
book value that is partly fiction, and a low P/B on a fictional book is not
cheap.

## Common mistakes

- **Comparing P/B across banks with different ROE.** P/B = P/E × ROE. A
  3x bank at 15% ROE and a 1x bank at 5% ROE can be on the same P/E. The
  multiple alone says nothing.
- **Reading P/B below 1 as a bargain.** It may mean the market doubts the
  book — under-provisioned loans, or an ROE below cost of equity that
  destroys value every year.
- **Mixing adjusted and unadjusted figures.** Bonus issues and splits halve
  the price in databases but not in last year's filing. Check the basis
  before dividing.
- **Trusting a justified-P/B formula.** As the table shows, two guessed
  inputs can produce almost any answer. Use it to understand *why* multiples
  differ, never to conclude that one is wrong.
- **Ignoring leverage inside ROE.** The same ROE from twice the leverage is
  not the same quality of return. Split it into ROA and leverage every time.

**Takeaway:** Banks are valued on book because their assets are mostly money
carried near what it's worth, and P/B = P/E × ROE ties the multiple to how
hard that book works. HDFC Bank at 30 June 2025 sat at about {{ v.pb }}x
book and {{ v.pe }}x earnings on a {{ d.roe_pct }}% ROE built from
{{ d.roa_pct }}% ROA and {{ d.avg_leverage }}x leverage. The "justified P/B"
formula, fed a generic {{ v.justified_pb_illustrative_roe_pct }}% ROE and a few plausible input pairs, returned
anything from {{ v.justified_pb_scenarios[0].pb }}x to {{ v.justified_pb_scenarios[3].pb }}x, which is all you need to know
about using it to decide anything.
