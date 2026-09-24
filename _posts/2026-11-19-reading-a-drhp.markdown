---
layout: post
title: "Reading a DRHP: the Desi Bites IPO, retold from the prospectus"
description: "A prospectus tells you what the money is for, who is selling, what could go wrong and what you're paying. The six sections that matter, on the Desi Bites IPO."
image: /assets/og/reading-a-drhp.png
date: 2026-11-19 09:00:00 +0530
series: fundamental-analysis
term: "DRHP (draft red herring prospectus)"
---

{% assign c2 = site.data.case_study_2 %}
{% assign d = c2.drhp %}
{% assign v = d.valuation_at_issue %}
{% assign l = site.data.case_study.listing %}
{% assign fy25 = site.data.case_study.income_statement.FY25 %}

## The longest document most investors never open

This module has spent six posts on what a listed company publishes. The
seventh goes back to the document that made it a listed company in the
first place.

A **DRHP — Draft Red Herring Prospectus** — is what a company files with
SEBI (or, for the SME platforms, with the exchange) when it wants to sell
shares to the public. "Draft" because it's filed for review; "red herring"
because the final price and quantity are left blank until close to the
issue. Once approved and priced it becomes the RHP, and then the
prospectus. It is typically 300 to 500 pages, it's free, and it's the most
complete, most legally accountable description of a business you will
ever get — because every statement in it exposes the company and its
bankers to liability if it's wrong.

Desi Bites Foods filed its DRHP in March 2025 and listed on NSE Emerge on
{{ l.listing_date }} at ₹{{ l.ipo_price }} a share. Fictional company, fictional filing,
real structure. Here's how to read one in an evening rather than a week.

## 1. Fresh issue or offer for sale?

Page one of the summary tells you the most important thing about any IPO:
where the money goes.

```
Fresh issue      → company sells NEW shares → money goes INTO the company
Offer for sale   → existing holders sell    → money goes to THEM, not the company
```

Desi Bites' issue was {{ d.issue_type | downcase }}: {{ d.fresh_issue_shares_lakh }} lakh new shares raising
₹{% include inr.html n=d.issue_size %} lakh, all of it going into the business. That's the cleaner
story — the company needs capital and is asking for it.

An **offer for sale (OFS)** is the other kind. The company gets nothing;
early investors or the promoter are cashing out, and you are buying from
people who know the business far better than you do. Plenty of legitimate
IPOs are mostly OFS — venture funds need exits — but an IPO that's 90% OFS
with a promoter selling down is a different proposition from one that's
90% fresh issue, and the cover page tells you which.

## 2. Objects of the issue: what the money is for

For a fresh issue, this section is a promise, and one the company will be
held to — listed companies must report deviations from stated objects to
the exchange every quarter until the funds are spent.

| Desi Bites, stated objects | ₹ lakh | Share |
|---|---:|---:|{% for o in d.objects %}
| {{ o.object }} | {{ o.amount }} | {{ o.pct }}% |{% endfor %}
| **Total** | **{{ d.issue_size }}** | 100% |

Read the labels carefully. *Capex for a named project* is specific and
checkable. *Working capital* is vaguer but legitimate. *General corporate
purposes* is the catch-all — money with no stated use — and
{{ d.gcp_cap_note | downcase }}, precisely because companies would otherwise
put everything there. *Inorganic growth* means acquisitions not yet
identified, which is a request to trust management's judgement on deals it
hasn't found.

Now the reckoning. By 31 March 2026, Desi Bites had spent
₹{% include inr.html n=d.actual_use_by_fy26_end.acquisitions %} lakh on an acquisition (against ₹500 lakh stated) and
₹{% include inr.html n=d.actual_use_by_fy26_end.capex %} lakh on capex (against ₹700 lakh), with ₹{% include inr.html n=d.actual_use_by_fy26_end.unspent %} lakh unspent.
{{ d.deviation_note }} Neither deviation is scandalous; both are exactly
the kind of thing the [capital allocation post]({% post_url 2026-11-18-capital-allocation %})
said to watch, and the prospectus is the yardstick that makes watching
possible.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your friend wants ₹1,000 from you and your classmates to grow her lemonade
stand. Before you chip in, you'd want a note that says: what will you buy
with it (a bigger table? a second stand?), what could go wrong (rain? a
rival stand?), how much lemonade did you sell last year, and — very
important — is the ₹1,000 going to the stand, or into her pocket because
she's selling you *her* share?

A prospectus is that note, written by lawyers, 400 pages long. The
questions are the same.

</details>

## 3. Risk factors: the section written by the lawyers

Every DRHP has 30 to 60 pages of risk factors, and most readers skip them
because they're written to protect the company from being sued ("we may
be adversely affected by…"). Skim anyway, because the *specific* ones are
buried among the boilerplate. Desi Bites' first six:

{% for rf in d.risk_factors %}{{ forloop.index }}. {{ rf }}
{% endfor %}

Ignore the ones that could apply to any company on earth (competition,
economic conditions, regulation). Read the ones that could only apply to
this one. Items 1, 3, 4 and 6 above are that kind: one plant, a
promoter-family distributor handling {{ d.related_party.share_of_fy25_revenue_pct }}% of revenue, a trademark
dispute, and a tax demand. Each of those turned up later in this module —
in the [contingent liabilities post]({% post_url 2026-11-16-contingent-liabilities-pledges-and-promoter-holding %})
and the [forensic post]({% post_url 2026-11-14-desi-bites-cooks-the-books %}). The
prospectus told you first.

## 4. Promoters and related parties

Two sections, read together. **Our Promoters** tells you who controls the
company and what else they do: {{ d.promoter.background }}. Holding
{{ d.promoter.holding_pre_ipo_pct }}% before the issue and {{ d.promoter.holding_post_ipo_pct }}% after. Look here for other companies the
promoter runs (competing? supplying?), for litigation against them
personally, and for how long they've actually run *this* business.

**Related party transactions** lists every dealing between the company and
the promoter's circle — usually three to five years of them. Desi Bites':
*{{ d.related_party.entity }}* bought ₹{% include inr.html n=d.related_party.fy25_revenue_via_rp %} lakh of product in FY25 — {{ d.related_party.share_of_fy25_revenue_pct }}% of
revenue — on {{ d.related_party.credit_terms }}. That's not necessarily wrong; family
distributors are how many Indian consumer businesses started. It is a
channel through which revenue can be pulled forward or margins shifted,
and the longer credit terms are a small example of the favour flowing one
way. This is the same note you'll read in every annual report afterwards,
and the prospectus is where you first see how large it is.

## 5. The financials: restated, and three years of them

A DRHP carries three years of **restated** financial statements — audited
numbers re-presented on a consistent basis. For Desi Bites that's the
FY23–FY25 model this blog has used all along, at [/case-study/]({{ '/case-study/' | relative_url }}).
Three things to do with them that the summary page won't:

- **Check the trend, not the last year.** Companies list after their best
  year. FY25 was Desi Bites' best by every measure. That's not a
  coincidence; it's when bankers advise listing.
- **Run the cash conversion.** [OCF/PAT]({% post_url 2026-09-20-ocf-pat %}) over three
  years. Desi Bites' was {{ site.data.case_study.ratios.FY23.ocf_pat }}, {{ site.data.case_study.ratios.FY24.ocf_pat }}, {{ site.data.case_study.ratios.FY25.ocf_pat }} — profit turning into cash every
  year. A company listing on rising profit and falling cash conversion is
  the pattern the forensic post described.
- **Look at the pre-IPO round.** If investors bought shares six months
  before the issue at a third of the IPO price, the prospectus must say
  so, in a table of "weighted average cost of acquisition." It's the most
  quietly informative table in the document.

## 6. Basis for the issue price: what you're paying

The **Basis for Offer Price** section is where the company justifies
₹{{ l.ipo_price }}. It gives the multiples at the issue price and a peer comparison:

| At ₹{{ l.ipo_price }}, FY25 numbers | |
|---|---:|
| [P/E]({% post_url 2026-09-24-price-to-earnings %}), on diluted EPS of ₹{{ l.eps_diluted }} | **{{ v.pe_diluted }}x** |
| P/E, on pre-issue EPS of ₹{{ l.eps_undiluted }} | {{ v.pe_undiluted }}x |
| [P/B]({% post_url 2026-09-25-price-to-book %}), on post-issue book value | {{ v.pb }}x |
| [EV/EBITDA]({% post_url 2026-09-26-ev-ebitda %}) | {{ v.ev_ebitda }}x |
| [Market cap]({% post_url 2026-09-27-market-cap %}) at issue | ₹{% include inr.html n=v.market_cap %} lakh |

Two traps here, both covered earlier in this blog. The prospectus will
often quote P/E on the *pre-issue* share count — {{ v.pe_undiluted }}x looks better than
{{ v.pe_diluted }}x, and the [EPS post]({% post_url 2026-09-23-eps %}) explained why the
diluted figure is the honest one for a buyer at listing. And the peer table
is chosen by the company: large, richly valued peers make the issue look
cheap. The [comparables post]({% post_url 2026-10-01-relative-valuation-comparables %})
is about choosing that table yourself.

One thing the section will *not* say is whether ₹{{ l.ipo_price }} is a good price.
Nor will this blog. The [margin of safety post]({% post_url 2026-10-06-margin-of-safety-and-sensitivity %})
showed a DCF of the same numbers landing well below the issue price, and
the reverse DCF showed what growth ₹{{ l.ipo_price }} implied. The prospectus gives you
every input for that exercise. It leaves the conclusion to you, which is
the correct division of labour.

## Common mistakes

- **Not checking fresh issue versus OFS.** The single most important line
  in the document, on the cover.
- **Skipping risk factors because they're boilerplate.** Two-thirds are.
  The specific third is the company telling you, under legal duress, what
  it's worried about.
- **Reading the P/E the company chose.** Recompute it on diluted EPS and
  on your own peer set.
- **Anchoring on the last year.** Companies list after a strong year. Read
  three, and read cash conversion.
- **Ignoring the related-party section because it's dull.** It's the map
  of every channel through which value can leave the company.
- **Forgetting the prospectus after listing.** It's the promise. The
  quarterly deviation reports and the annual report are where you check
  whether it was kept — which is what this whole module has been doing.

**Takeaway:** A prospectus is the most complete and most legally
accountable description of a business you'll ever be handed, and most
investors read only the price. Read six things: fresh issue or offer for
sale, what the money is for, the specific risk factors, who the promoter
is and what flows to their relatives, three years of restated cash
conversion, and the multiples on *diluted* earnings. Then keep the
document — every annual report afterwards is a report on whether its
promises were kept.
