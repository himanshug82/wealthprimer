---
layout: post
title: "Capital adequacy: the buffer that makes deposits safe"
description: "CAR, CET1, Tier 1, Tier 2 and risk-weighted assets, decoded. What the 11.7% floor is made of, why it's measured on risk not size, and the headroom in rupees."
image: /assets/og/capital-adequacy.png
date: 2026-11-24 09:00:00 +0530
series: fundamental-analysis
term: "Capital adequacy ratio (CAR)"
---

{% assign b = site.data.real_bank %}
{% assign f25 = b.reported.FY25 %}
{% assign f24 = b.reported.FY24 %}
{% assign c = b.capital %}
{% assign m = b.regulatory_minimum %}
{% assign rwa_lakh_cr = c.rwa | divided_by: 100000 | round: 1 %}
{% assign assets_lakh_cr = f25.total_assets | divided_by: 100000 | round: 1 %}
{% assign headroom_lakh_cr = c.headroom_rupees | divided_by: 100000 | round: 2 %}

## The question debt-to-equity was trying to ask

For a manufacturer, [debt-to-equity]({% post_url 2026-09-15-debt-to-equity %})
and [interest coverage]({% post_url 2026-09-17-interest-coverage %}) answer
one question: if things go wrong, how much can the company lose before the
lenders lose too?

For a bank the question is identical and far more serious, because the
"lenders" are depositors — millions of them, holding money they believe is
safe. The [first post]({% post_url 2026-11-20-why-ratios-break-on-a-bank %})
showed that HDFC Bank's equity is about {{ f25.equity_to_assets_pct }}% of its
balance sheet. If loans worth more than that went bad and stayed bad,
depositors would be the ones absorbing the loss.

**Capital adequacy** is the regulatory answer. It says: a bank must hold
enough of its *own* money — shareholders' capital, which can absorb losses
without anyone being owed anything — relative to the *risk* it is running.
Not relative to its size. Relative to its risk.

## The formula, and why the denominator is odd

```
Capital adequacy ratio (CAR)  =  Regulatory capital  /  Risk-weighted assets (RWA)
```

**Risk-weighted assets** are the balance sheet re-counted by riskiness. Each
asset is multiplied by a weight that reflects how likely it is to lose money:

| Asset | Typical risk weight (simplified) |
|---|---:|
| Cash, balances with RBI, government securities | 0% |
| Home loans (well-collateralised) | 35–50% |
| Corporate loans (depends on rating) | 20–150% |
| Unsecured personal loans | 125% |
| Credit-card receivables | 150% |
| Certain exposures RBI wants to discourage | higher, by regulation |

So ₹100 of government bonds adds ₹0 to RWA; ₹100 of credit-card balances adds
₹150. (Those two unsecured rows were raised by RBI, November 2023: personal
loans from 100% to 125%, and bank credit-card receivables from 125% to 150%.) A bank with a large, safe book has RWA well below its total assets; a
bank lending aggressively can have RWA near or above them.

**Regulatory capital** comes in layers, in order of how cleanly each can
absorb a loss:

| Layer | What it is | Absorbs losses… |
|---|---|---|
| **Common Equity Tier 1 (CET1)** | Share capital plus retained earnings and reserves, less deductions | First, while the bank is still operating |
| **Additional Tier 1 (AT1)** | Perpetual bonds that convert to equity or are written down if capital falls too far | Next, by contract |
| **Tier 2** | Subordinated debt with a long maturity, certain provisions | Only if the bank fails |

Tier 1 is CET1 plus AT1. Total capital adds Tier 2. Each has its own minimum,
and CET1's is the one that matters most because it is the only layer that is
unambiguously the shareholders' money.

## Worked example: HDFC Bank, 31 March 2025

From HDFC Bank's [results for the year ended 31 March 2025]({{ b.company.source_url }})
(standalone). Historical, for illustration only.

![Capital adequacy stack]({{ '/assets/charts/bank-capital-stack.svg' | relative_url }})

| | Reported |
|---|---:|
| Risk-weighted assets | ≈ ₹{% include inr.html n=c.rwa %} crore |
| Total assets, for comparison | ₹{% include inr.html n=f25.total_assets %} crore |
| RWA as % of total assets | {{ c.rwa_to_total_assets_pct }}% |
| CET1 ratio | {{ f25.cet1_pct }}% |
| Tier 1 ratio | {{ f25.tier1_pct }}% |
| **Total CAR** | **{{ f25.car_pct }}%** (FY24: {{ f24.car_pct }}%) |

The filing's own sentence: the CAR "was at 19.6% as on March 31, 2025 …
as against a regulatory requirement of {{ m.total }}%."

Two things to read off this. First, RWA is about {{ c.rwa_to_total_assets_pct }}%
of the balance sheet — roughly ₹{{ rwa_lakh_cr }} lakh crore of "risk" on
₹{{ assets_lakh_cr }} lakh crore of assets, because a large slice of the assets
is government securities and cash that carry no weight. Second, almost all of
the capital is the good kind: CET1 is {{ f25.cet1_pct }} of the
{{ f25.car_pct }} points.

## What the 11.7% is made of

The regulatory floor isn't one number; it is a stack, and the filing's 11.7%
is the sum for this particular bank:

| Component | % of RWA | What it is |
|---|---:|---|
| Minimum total capital (CRAR) | {{ m.crar }}% | RBI's base requirement — one point above the international Basel III minimum of 8% |
| Capital conservation buffer | {{ m.ccb }}% | Must be met from CET1; a bank that dips into it faces restrictions on dividends and bonuses |
| D-SIB surcharge | {{ m.dsib_surcharge }}% | Extra CET1 for banks RBI designates as **Domestic Systemically Important** — too big to be allowed to fail quietly |
| **Requirement** | **{{ m.total }}%** | |

Within the base 9%, RBI requires at least {{ m.cet1_min }}% as CET1 and
{{ m.tier1_min }}% as Tier 1. The D-SIB surcharge depends on the bucket RBI
places a bank in, and it moves. The {{ m.dsib_surcharge }}% above is what applied to HDFC
Bank on 31 March 2025. RBI's D-SIB list (reaffirmed in its press release of
13 November 2024) placed HDFC Bank in a higher bucket from 1 April 2025, with
a {{ m.dsib_surcharge_from_apr2025 }}% surcharge — lifting the floor to {{ m.total_from_apr2025 }}%. Always check the
current designation rather than the last one you read.

## The headroom, in rupees

Ratios in percentage points hide the scale. Convert:

| | ₹ crore |
|---|---:|
| Capital held (≈ {{ f25.car_pct }}% of RWA) | {% include inr.html n=c.capital_at_car %} |
| Capital required (≈ {{ m.total }}% of RWA) | {% include inr.html n=c.capital_at_reg_min %} |
| **Headroom above the floor** ({{ c.headroom_pct_points }} points) | **{% include inr.html n=c.headroom_rupees %}** |

About ₹{{ headroom_lakh_cr }} lakh crore of capital sits above the regulatory
minimum. For a sense of proportion: the entire gross NPA book from the
[previous post]({% post_url 2026-11-23-gnpa-nnpa-and-provisions %}) was
₹{% include inr.html n=f25.gross_npa %} crore — about
{{ c.gross_npa_as_pct_of_cet1 }}% of the bank's CET1 capital. That is the
comparison capital adequacy is built to make: the losses that have shown up
so far, against the money available to absorb losses.

This is a statement about the arithmetic at one date, not about safety in
general. Capital ratios are computed on the *current* risk weights and the
*current* classification of loans; a severe enough shock changes both at
once.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you run a lending club with your classmates' money. The teacher sets a
rule: for every ₹100 you lend to a risky borrower, you must have ₹12 of your
*own* pocket money in the club. For lending to the safest kids, you need
almost none.

Why? Because if the risky borrowers don't pay, the loss comes out of your
pocket money first — and your classmates still get all their money back. Your
pocket money is the *capital*. The teacher's ₹12-per-₹100 rule is *capital
adequacy*. And the risky-vs-safe weighting is *risk-weighted assets*.

If you have ₹19.55 for every ₹100 instead of ₹12, you've got a cushion. If
you're at ₹11, the teacher stops you lending more until you top it up.

</details>

## Why capital is expensive, and why that matters

Every rupee of equity a bank holds is a rupee it isn't leveraging. The
[first post]({% post_url 2026-11-20-why-ratios-break-on-a-bank %}) showed
₹1 of equity supporting about ₹{{ f25.leverage_assets_to_equity }} of assets.
More capital means a lower multiple, which — for the same return on assets —
means a lower return on equity. That trade-off is the whole tension of bank
regulation: regulators want more capital; shareholders' returns are diluted by
it.

It is also why a bank raises capital: when RWA grows (more lending, or a
shift into higher-weight loans) faster than retained profits add to CET1, the
ratio falls toward the floor and the bank must either slow lending or issue
shares. Watching the CET1 ratio trend tells you how much room a bank has to
grow before that choice arrives.

## Common mistakes

- **Dividing capital by total assets.** That is a *leverage ratio*, which
  RBI also tracks, but it isn't CAR. CAR's denominator is risk-weighted, which
  is why RWA is about {{ c.rwa_to_total_assets_pct }}% of assets here.
- **Reading a high CAR as a target.** Capital above the floor is a buffer,
  and it's also an unleveraged asset. Banks manage *toward* a comfortable
  level, not toward the maximum.
- **Ignoring the layers.** Two banks at 16% CAR, one with 15% CET1 and one
  with 10% CET1 plus a lot of Tier 2 debt, are not equally capitalised. CET1
  is the number to anchor on.
- **Treating risk weights as fixed truth.** They are regulatory conventions
  and RBI changes them — raising weights on unsecured consumer credit, for
  example, mechanically lowers every affected bank's CAR overnight with no
  change in the loans themselves.
- **Assuming the minimum is the same for every bank.** D-SIB surcharges
  differ by bank and are reviewed. Read the requirement the bank itself
  states in its filing.

**Takeaway:** Capital adequacy asks how much of a bank's own money stands
between its risks and its depositors, measured against risk-weighted assets,
not the balance sheet. HDFC Bank's FY25 filing shows {{ f25.car_pct }}% total
capital and {{ f25.cet1_pct }}% CET1 against a {{ m.total }}% floor built
from a 9% base, a 2.5% conservation buffer and a D-SIB surcharge — about
₹{{ headroom_lakh_cr }} lakh crore of headroom. It is the ratio that replaces
debt-to-equity for a bank, and the one that decides how fast it can grow.
