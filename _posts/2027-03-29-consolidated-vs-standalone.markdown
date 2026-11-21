---
layout: post
title: "Consolidated vs standalone: which accounts to read"
description: "Consolidated accounts add a parent and its subsidiaries together; standalone shows the parent alone. How the two differ, worked on Desi Bites' FY26 books."
image: /assets/og/consolidated-vs-standalone.png
date: 2027-03-29 09:00:00 +0530
series: fundamental-analysis
term: "Consolidated statements"
---

{% assign k = site.data.fa5.consolidation %}
{% assign rev = k.rows[0] %}
{% assign pat = k.rows[13] %}

## What consolidated and standalone mean

A company that owns other companies publishes two sets of accounts.
**Standalone** statements show the parent company on its own: its sales, its
costs, and its shareholdings in other companies as a single "investment"
line. **Consolidated** statements treat the parent and every company it
controls (its subsidiaries) as one economic unit: their revenue, costs,
assets and debts are added together line by line, and deals between them are
removed.

For a group, the consolidated numbers describe the business a shareholder
owns a slice of. The standalone numbers describe one legal entity inside it.
This post shows how one becomes the other, on the fictional
[Desi Bites Foods]({{ '/case-study/' | relative_url }}), part of
[Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}).

## The rule, and the arithmetic

Ind AS 110 (the Indian Accounting Standard on consolidated financial
statements) says a parent shall present consolidated statements, and that
the test for including a company is **control**: power over it, exposure to
its returns, and the ability to use that power to affect those returns
(paragraphs 4, 7 and 10–18). The consolidation procedure is in paragraph B86:

```
Consolidated line  =  parent's line  +  each subsidiary's line
                      −  transactions inside the group (eliminated in full)

Parent's "investment in subsidiary"  →  replaced by the subsidiary's own
                                        assets and liabilities, plus goodwill

Non-controlling interest  =  the share of a subsidiary the parent doesn't own,
                             shown inside equity, separately (paragraph 22)
```

Consolidation starts on the date control is obtained (paragraph 20), so a
subsidiary bought mid-year contributes only the months after that date.

## Worked example: Desi Bites and Chatpata, FY26

In the [goodwill post]({% post_url 2026-10-07-goodwill-exceptional-items-and-other-income %}),
Desi Bites bought Chatpata Foods for ₹{% include inr.html n=k.investment %}
lakh on {{ k.acquired }}. Here we add the fact that makes this a
consolidation question: Chatpata is a company of its own,
{{ k.sub_name }}, and Desi Bites owns {{ k.ownership_pct }}% of it. In the
six months it was owned, Chatpata also sold ₹{{ k.intragroup_sales }} lakh
of snacks to its parent (they cost Chatpata ₹{{ k.intragroup_cost }} lakh),
and the parent sold all of them on to customers by 31 March 2026. All of
this is fictional, invented to show the method. Figures in ₹ lakh.

**Step 1: the FY26 income statement, built up.** EBITDA is earnings before
interest, tax, depreciation and amortisation (see the
[EBITDA margin post]({% post_url 2026-08-28-ebitda-margin %})); EBIT is
earnings before interest and tax.

| ₹ lakh, FY26 | Desi Bites, standalone | Chatpata (Oct–Mar) | Group adjustments | Consolidated |
|---|---:|---:|---:|---:|
{% for row in k.rows -%}
| {{ row.line }} | {{ row.parent }} | {{ row.sub }} | {{ row.adj }} | {{ row.consolidated }} |
{% endfor %}

Two kinds of adjustment sit in the third column:

1. **The intragroup sale is removed.** Chatpata booked
   ₹{{ k.intragroup_sales }} lakh of revenue selling to Desi Bites, and Desi
   Bites booked the same ₹{{ k.intragroup_sales }} lakh as a cost when it
   resold the goods. From the group's point of view, nothing was sold to
   anyone outside, so both sides go. Gross profit doesn't change; revenue and
   cost both shrink.
2. **A consolidation-only cost appears.** The Chatpata brand
   (₹{{ k.brand }} lakh) was recognised as an intangible asset only in the
   group's books, when the purchase price was allocated. Its amortisation is
   a group cost that appears in neither company's own accounts.

Chatpata's own figures assume a {{ k.sub_tax_rate_pct }}% tax rate, and the
deferred tax that would arise on the brand is ignored for simplicity. The
₹{{ site.data.case_study_2.acquisition.integration_costs }} lakh of acquisition and integration costs (the exceptional item) is
shown in the parent's own income statement here; in a parent's separate
accounts, some acquisition costs may instead be added to the cost of the
investment, so check the company's stated policy.

**Step 2: the balance sheet line that changes.** On its standalone balance
sheet, Desi Bites shows one line, "investment in subsidiary",
₹{% include inr.html n=k.investment %} lakh, what it paid. The consolidated
balance sheet replaces it with what was bought:

| At acquisition, ₹ lakh | |
|---|---:|
| Chatpata's fixed assets | {{ k.fixed_assets }} |
| Inventory | {{ k.inventory }} |
| Receivables | {{ k.receivables }} |
| Brand (recognised by the group) | {{ k.brand }} |
| Less: payables | −{{ k.payables }} |
| **Identifiable net assets** | **{{ k.net_assets }}** |
| Goodwill | {{ k.goodwill }} |
| **Equals the price paid** | **{{ k.investment }}** |

So the consolidated balance sheet carries ₹{{ k.goodwill }} lakh of goodwill
and a brand (₹{{ k.brand_closing }} lakh by year-end, after amortisation)
that the standalone one never shows.

**Step 3: what changes for a reader.**

- Revenue: ₹{% include inr.html n=rev.parent %} lakh standalone against
  ₹{% include inr.html n=rev.consolidated %} lakh consolidated.
- PAT (profit after tax): ₹{{ k.parent_pat }} lakh against
  ₹{{ k.cons_pat }} lakh.
- EBITDA margin: {{ k.parent_ebitda_margin_pct }}% standalone,
  {{ k.sub_ebitda_margin_pct }}% in Chatpata's own books,
  {{ k.cons_ebitda_margin_pct }}% for the group. The acquired business runs
  at a lower margin, and only the consolidated figure shows the blend.
  Chatpata's own figure is above the {% include inr.html n=site.data.case_study_2.acquisition.ebitda_margin_h2 %}% the goodwill post gave for its
  sales to outside customers, because its books also include the margin on
  sales to its parent; the parent's own margin is lower by the same amount.
  Both effects vanish in the consolidated column.

**If Desi Bites owned 80%, not 100%.** The consolidated statements would
still include all of Chatpata's revenue and costs, because control, not
ownership share, decides inclusion. Then
{{ k.nci_example_pct }}% of Chatpata's profit as it appears in the group
accounts, after the brand amortisation (paragraphs B88 and B94), would be
shown as belonging to the non-controlling interest: ₹{{ k.nci_example_share }}
lakh, leaving ₹{{ k.nci_example_owners_pat }} lakh attributable to Desi Bites'
own shareholders. That attributable figure, not total PAT, is the one
[EPS]({% post_url 2026-09-23-eps %}) (earnings per share) is built on.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your family runs a sweet shop, and your aunt runs a namkeen stall that your
family owns. The shop's own notebook shows the shop's sales, and one line
saying "we own the stall".

Now write one big notebook for the whole family business. You add the
stall's sales and costs to the shop's. But when the stall sold namkeen to
the shop, that wasn't a real sale to a customer, so you cross it out. The
big notebook is the consolidated one.

</details>

## Common mistakes

1. **Reading the standalone numbers of a group.** For a company with large
   subsidiaries, standalone revenue and profit can leave out most of the
   business. Groups often publish both sets side by side, so check which one
   a results table or a screener is showing.
2. **Adding parent and subsidiary figures yourself.** Simple addition double
   counts intragroup sales. Here it would overstate revenue by
   ₹{{ k.intragroup_sales }} lakh and miss the brand amortisation.
3. **Comparing growth across a year with an acquisition.** Consolidated
   revenue jumps when a subsidiary is added, without any existing business
   growing. The [quarterly results post]({% post_url 2026-10-05-reading-quarterly-results %})
   covers separating organic growth from acquired growth.
4. **Using total PAT when there's a non-controlling interest.** Per-share
   figures and the [P/E]({% post_url 2026-09-24-price-to-earnings %})
   (price-to-earnings) ratio should use the profit
   attributable to the parent's shareholders.

**Takeaway:** Consolidated accounts treat a parent and the companies it
controls as one business and strip out deals between them; standalone
accounts show the parent alone. For a group, the consolidated set is usually
the one that describes what a shareholder owns.

## Sources

- Ind AS 110, *Consolidated Financial Statements*, paragraphs 4, 7, 10–22, B86, B88 and B94. The Ministry of Corporate Affairs' (MCA's)
  [Ind AS page](https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/accounting-standards.html)
  refuses automated requests, so the text was read on 21 November 2026 in
  [a copy of the notified standard](https://ca2013.com/rule/indian-accounting-standard-ind-110-2/)
  on the Companies Act Integrated Ready Reckoner, a third-party site. Check
  the paragraphs against MCA's text before relying on them.
