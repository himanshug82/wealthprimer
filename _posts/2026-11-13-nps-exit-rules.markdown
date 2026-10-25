---
layout: post
title: "NPS exit rules: what you can take out, and when"
description: "NPS exit rules from PFRDA's regulations: the annuity share, lump-sum slabs, premature exit and partial withdrawal, worked on PFRDA's own examples."
image: /assets/og/nps-exit-rules.png
date: 2026-11-13 09:00:00 +0530
series: money-before-markets
term: "NPS (National Pension System)"
---

{% assign m = site.data.mbm %}
{% assign n = m.nps %}
{% assign rg = n.regs %}
{% assign fq = n.faq %}
{% assign pr = n.premature %}
{% assign pt = n.partial %}

## What the NPS is, and what this post covers

The **National Pension System (NPS)** is a retirement scheme regulated by **PFRDA**, the Pension Fund Regulatory and Development Authority. A subscriber pays into an individual pension account over the years, the money is invested through pension funds, and the rules decide how much can come out, when, and how.

This post covers only that last part, the exit and withdrawal rules, because they are what surprises people. How big the corpus becomes depends on returns along the way and on their order, which [sequence of returns risk]({% post_url 2026-10-13-sequence-of-returns-risk %}) explains, and what it buys depends on [inflation]({% post_url 2026-10-20-inflation-and-real-returns %}). How the money is invested, the choice of funds and how returns are taxed are not covered. It is part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}).

The rules below are from the [Exits and Withdrawals (Amendment) Regulations, 2025]({{ rg.url }}), notified {{ rg.notified | date: "%-d %B %Y" }} and published in the Gazette on {{ rg.published | date: "%-d %B %Y" }} ([Gazette PDF]({{ rg.pdf }})), and PFRDA's [FAQ (frequently asked questions) for the All Citizen Model]({{ fq.url }}), updated March 2026. The regulations are as of their {{ rg.published | date: "%-d %B %Y" }} publication, plus the later amendment noted below. They were read on {{ rg.read | date: "%-d %B %Y" }}. A later amendment, notified {{ rg.amend_2026.notified | date: "%-d %B %Y" }}, {{ rg.amend_2026.subject }}; from its text, it does not touch the exit rules described here. PFRDA can amend these again, so check the current text.

## Terms you need

- **Accumulated pension wealth (APW)** is the value of the account at exit.
- An **annuity** is a product bought from an insurer that pays a regular pension for life or a set period. The share the rules require you to put into an annuity isn't available as a lump sum.
- **Lump sum** means taking money out. It can be taken at once or through **systematic lump sum withdrawal (SLW)** or **systematic unit redemption (SUR)**, both of which pay it out in instalments.
- **Normal exit** is leaving the NPS at age {{ n.vesting_age }}, or after {{ n.vesting_years }} years in a pension scheme (the regulations say the 15-year route does not apply to a scheme subscribed to because of employment). **Premature exit** is leaving before that.

## The rules for a non-government subscriber

| Situation | What the regulations require |
|---|---|
| Normal exit, any corpus | At least {{ n.annuity_min_pct }}% of APW buys an annuity; the rest can be taken as a lump sum |
| Normal exit, APW up to ₹{% include inr.html n=n.slab_full %} | The whole amount can be withdrawn as a lump sum |
| Normal exit, APW above ₹{% include inr.html n=n.slab_full %} up to ₹{% include inr.html n=n.slab_mid_top %} | A lump sum of up to ₹{% include inr.html n=n.slab_mid_lump_max %}; the balance goes to SUR for at least six years or to an annuity |
| Premature exit | At least {{ n.annuity_min_premature_pct }}% of APW buys an annuity; if APW is ₹{% include inr.html n=n.premature_full %} or less, the whole amount can be withdrawn |
| Staying on | A subscriber can defer taking the lump sum or buying the annuity up to age {{ n.defer_age }} |

Two cases differ from the table. A subscriber who joins after attaining age 60 and exits before 85 follows regulation 4(1)(e): at least 20% to an annuity, and the whole corpus can be withdrawn if it is ₹{% include inr.html n=n.slab_mid_top %} or less. And a corporate sector subscriber of a government-owned or government-controlled body, on superannuation, exits under the government sector rule in regulation 3. For a **government sector subscriber** on normal exit, the minimum annuity share is {{ n.annuity_min_govt_pct }}%, under regulation 3 of the same regulations. The two groups follow different rules, so check which you are.

## Worked example: PFRDA's own three corpora

PFRDA's FAQ illustrates normal exit for a non-government subscriber with corpora of ₹6 lakh, ₹9 lakh and ₹13 lakh. The table applies the regulations to the same amounts, and the numbers match the FAQ's.

| APW at exit (₹) | Option | Lump sum, at most (₹) | SUR for six years or annuity (₹) | Annuity, at least (₹) |
|---|---|---:|---:|---:|
{% for e in n.examples -%}
{% if e.full_withdrawal -%}
| {{ e.apw }} | Whole amount | {{ e.apw }} | - | - |
{% endif -%}
{% if e.lump_max_slab -%}
| {{ e.apw }} | Slab option | {{ e.lump_max_slab }} | at least {% assign x = e.balance_after_slab_lump %}{% include inr.html n=x %} | - |
{% endif -%}
| {{ e.apw }} | The 80/20 option | {{ e.lump_max_option_a }} | - | {{ e.annuity_min }} |
{% endfor %}
Premature exit works differently. With APW of ₹{% include inr.html n=pr.apw %}, at least ₹{% include inr.html n=pr.annuity_min %} must go to an annuity and at most ₹{% include inr.html n=pr.lump_max %} can be taken out.

The FAQ adds that the whole of the corpus can be used to buy an annuity at normal exit, at any size.

## Partial withdrawal before exit

The FAQ describes a limited way to take money out while still subscribed. These are PFRDA's stated terms:

- It opens after {{ pt.min_years }} years from the date of subscription to the pension scheme.
- Before age 60, up to {{ pt.max_times_before_60 }} times, with at least {{ pt.gap_years_before_60 }} years between two withdrawals.
- The first withdrawal can be up to {{ pt.pct }}% of the subscriber's *own contributions*, excluding returns. With own contributions of ₹{% include inr.html n=pt.own_contributions %}, that is ₹{% include inr.html n=pt.first_max %}.
- Permitted purposes only: children's higher education or marriage; a one-time purchase or construction of a home (not if you already own one, other than ancestral property); medical treatment; expenses from disability; and settling a loan secured against the account.

## Common mistakes

- **Assuming everything can be taken at 60.** Above the slabs, at least {{ n.annuity_min_pct }}% has to go into an annuity, and a premature exit sends at least {{ n.annuity_min_premature_pct }}% into one.
- **Mixing up the government and non-government rules.** The minimum annuity share is {{ n.annuity_min_govt_pct }}% in one case and {{ n.annuity_min_pct }}% in the other.
- **Relying on old explainers.** The rules were amended in December 2025. A page written before that may describe different percentages.
- **Counting partial withdrawal as access to the whole corpus, like an [emergency fund]({% post_url 2026-11-08-emergency-fund-sizing %}).** The cap is on own contributions, not on the account's value, and the purposes are restricted.

**Takeaway:** NPS decides at exit how much of your corpus must become an annuity and how much you can take out, and the answer depends on your corpus, your age, whether you are a government or non-government subscriber, and whether you leave early. Read the current exit regulations for your category before assuming what is available.
