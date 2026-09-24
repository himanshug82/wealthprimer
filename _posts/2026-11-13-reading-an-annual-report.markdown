---
layout: post
title: "Reading an annual report: the map, and where the bodies are buried"
description: "An annual report is 140 pages written by the people it judges. Which sections to read first, which to skip, and why the notes beat the chairman's letter."
image: /assets/og/reading-an-annual-report.png
date: 2026-11-13 09:00:00 +0530
series: fundamental-analysis
term: "Annual report"
---

{% assign c2 = site.data.case_study_2 %}
{% assign ar = c2.annual_report %}
{% assign f = c2.fy26 %}

## A document written by the people it judges

The [capstone post]({% post_url 2026-10-07-capstone-britannia-end-to-end %}) ended the
first module with a checklist and an honest limit: financial statements tell
you what kind of business you're looking at, not whether the price is right.
This module is about the *rest* of what a company publishes — the 140 pages
around those five pages of statements — and how to read it without being
led by the nose.

Start with the uncomfortable fact. An **annual report** is the company's
account of its own year, written by management, approved by a board that
management largely selected, and designed (photographs, typography, the
chairman's smile) to reassure. Most of it is truthful. Almost none of it is
neutral. The skill is knowing which pages were written *for* you and which
were written *at* you.

Desi Bites Foods, the fictional snacks company this blog has followed since
[its first post]({% post_url 2026-08-18-meet-desi-bites-foods %}), listed on
the main boards of the NSE (National Stock Exchange) and BSE in June 2025. Its first annual report as a listed company covers
{{ ar.fy | split: "," | first }}, and it's the example throughout this module. Everything about
Desi Bites is invented; the *structure* of the report is what every Indian
listed company files.

## The map

Roughly {{ ar.approx_pages }} pages, in the order they appear — with the order you should
actually read them in:

| Section | Pages | Written by | Read it… | What it really is |
|---|---:|---|---:|---|{% for s in ar.sections %}
| **{{ s.name }}** | ~{{ s.pages }} | {{ s.who_writes }} | {{ s.read_order }}{% if s.read_order == 1 %}st{% elsif s.read_order == 2 %}nd{% elsif s.read_order == 3 %}rd{% else %}th{% endif %} | {{ s.what_it_is }} |{% endfor %}

Two things jump out of that table.

First, **the reading order is almost the reverse of the page order.** The
report opens with the most persuasive material and closes with the most
informative. That isn't an accident.

Second, **the notes to accounts are half the report.** Seventy pages of
small type that most readers never open, sitting behind five pages of
statements that this blog spent a whole module on. Every number in those five
pages has its explanation in the seventy.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine your school report card came with a twenty-page essay by you about
how your year went, a note from the principal, and then — at the very back —
the actual marks, followed by fifty pages of the teachers' detailed comments.

The essay is nice to read. The marks are the facts. But the teachers'
comments are where you find out *why* the maths mark dropped, whether the
science project was really finished, and what the "extra credit" actually
was.

Grown-ups reading an annual report should go straight to the marks and then
the comments. The essay can wait.

</details>

## Step 1: the auditor's report (six pages, read first)

The **independent auditor's report** is the only part of the document
written by someone the company didn't employ to say nice things — though it
did pay them, which is worth remembering. Three things to find in it:

**The opinion.** It comes in four grades. *Unmodified* ("true and fair
view") is the normal case. *Qualified* means "true and fair except for the
following" — read the following. *Adverse* means the statements are
materially wrong. *Disclaimer* means the auditor couldn't get enough
evidence to form a view at all. The last two are rare and are the loudest
sound a document can make.

**Key audit matters (KAMs).** For listed companies, from audits of FY2018-19
onward (auditing standard SA 701), auditors must list the areas that took the
most judgement. These are, by definition, where the numbers are
softest. For Desi Bites the KAM is *{{ ar.kam_example }}* — which is
exactly the area the next post shows being abused.

**Emphasis-of-matter paragraphs.** The auditor agrees with the statements
but wants you to look at something — often a pending dispute, a significant
uncertainty, or a change in accounting policy. It's the auditor pointing. (A
*material* doubt about going concern is louder still: under the revised SA 570
it gets its own separately headed section in the report.)

## Step 2: the statements (five pages)

You know these. [Balance sheet]({% post_url 2026-08-20-reading-a-balance-sheet %}),
[income statement]({% post_url 2026-08-22-reading-an-income-statement %}),
[cash flow]({% post_url 2026-08-24-reading-a-cash-flow-statement %}), and the
statement of changes in equity — which most readers skip and shouldn't,
because it's where share issues, buybacks and dividends are laid out in one
place.

Desi Bites' FY26 headline figures, in ₹ lakh:

| | FY25 | FY26 |
|---|---:|---:|
| Revenue | {{ site.data.case_study.income_statement.FY25.revenue }} | {{ f.revenue }} |
| EBITDA | {{ site.data.case_study.income_statement.FY25.ebitda }} | {{ f.ebitda }} |
| Other income | — | {{ f.other_income }} |
| Exceptional items | — | {{ f.exceptional_items }} |
| PAT | {{ site.data.case_study.income_statement.FY25.pat }} | {{ f.pat }} |
| Cash & bank | {{ site.data.case_study.balance_sheet.FY25.cash }} | {{ f.balance_sheet.cash }} |
| Goodwill | — | {{ f.balance_sheet.goodwill }} |

Revenue up {{ f.ratios.revenue_growth }}%, PAT up {{ f.ratios.pat_growth }}%. Two new lines — *other
income* and *exceptional items* — and two new balance sheet items, goodwill
and a cash pile roughly five times last year's. Every one of those is a
question, and none of them is answered on these five pages.

## Step 3: the MD&A (management's version of why)

The **management discussion and analysis (MD&A)** is the one section where
management is obliged to explain the year in words: volumes versus prices,
input costs, new capacity, competition, what the risks are. It's the only
place the *why* is written down, which makes it indispensable — and it's
written by the people whose bonuses depend on the answer, which makes it
something to read against the numbers rather than instead of them.

A practical test: for each claim in the MD&A, find the line in the
statements that would be true if the claim were true. "Strong volume growth"
should show up as revenue growing faster than any price increase
mentioned. "Improved operational efficiency" should show up as opex growing
slower than revenue. "Prudent working capital management" should show up in
[debtor days]({% post_url 2026-09-08-debtor-days %}) and
[inventory days]({% post_url 2026-09-07-inventory-days %}). When the words
and the lines disagree, believe the lines.

Desi Bites' MD&A says revenue grew {{ f.ratios.revenue_growth }}%. The notes say the
existing business grew {{ f.ratios.organic_revenue_growth }}%; the other {{ f.ratios.revenue_growth | minus: f.ratios.organic_revenue_growth | round: 1 }} points came from a
company it bought in October. Both statements are true. Only one of them
appears in the MD&A's opening paragraph.

## Step 4: the notes (seventy pages — but only seven matter first)

You don't read all seventy. You read these, in this order:

| Note | Why it's on the shortlist |
|---|---|{% for n in ar.notes_to_read_first %}
| **{{ n.note }}** | {{ n.why }} |{% endfor %}

The pattern: every note on that list is a place where a number on the
statements could be *true and misleading at the same time*. Revenue can be
real and pulled forward. A profit can be genuine and come from selling a
building. A balance sheet can balance and omit a ₹120 lakh tax demand
because it's "contingent." The notes are where the statements confess.

The next few posts in this module each take one of those notes and work
through it on Desi Bites: the forensic checks, the quarterly rhythm,
contingent liabilities and pledges, and goodwill.

## Steps 5 to 8: the persuasive pages

Read the chairman's letter *after* all of the above, and read it as a
document about management rather than about the company. Does it mention
the things you found in the notes? If the year had an exceptional item, a
missed target, or a KAM about revenue cut-off, does the letter acknowledge
it or talk about "headwinds" and "our journey"? A letter that engages with
the bad news is worth more than one that doesn't — and the difference is
only visible if you already know what the bad news was.

The directors' report and governance report are mostly statutory
boilerplate, with two exceptions worth a minute each: the **AOC-2 annexure**
(related-party contracts the board approved) and the list of **independent
directors who resigned during the year**, with their stated reasons.
"Personal reasons" three times in one year is information.

## Common mistakes

- **Reading front to back.** The report is sequenced to persuade. Start at
  the auditor's report and the notes; the letter can wait.
- **Treating "unmodified opinion" as a clean bill of health.** It means the
  statements fairly present what happened under the accounting rules. It
  does not mean the business is good, the profit is high quality, or the
  accounting choices were conservative. The key audit matters tell you where
  the auditor sweated.
- **Skipping the notes because they're long.** Seven of them do most of the
  work. Start there.
- **Believing the MD&A's adjectives.** "Robust," "resilient" and
  "strategic" have no line on the P&L. Find the number each claim implies
  and check it.
- **Ignoring the statement of changes in equity.** It's a one-page record of
  every share issued, every dividend paid and every reserve moved. For a
  company that just listed, it's where dilution is spelled out.
- **Reading one year.** An annual report shows two years side by side. The
  useful unit is three to five reports, read for what *changed* — in
  policies as much as in numbers. A quiet change to the revenue recognition
  policy is a bigger event than a loud change in the margin.

**Takeaway:** An annual report is 140 pages written by the people it judges,
sequenced to persuade: the reassuring letter up front, the seventy pages of
notes at the back. Read it backwards — auditor's report, statements, then
the seven notes where a true number can still mislead — and treat the
chairman's letter as evidence about management, not about the company.
