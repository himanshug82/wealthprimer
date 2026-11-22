---
nav_section: about
layout: page
title: "Editorial standards"
permalink: /editorial-standards/
description: "How Wealth Primer posts are made and kept honest: what we never publish, where numbers come from, how rules are sourced, and how we correct mistakes."
---

Wealth Primer explains how investing works for Indian readers: what a ratio
measures, how a fund's returns are calculated, how a tax rule applies. This
page sets out the standards every post is held to, so you can judge for
yourself how far to trust what you read here.

## What we never publish

- **No tips or calls.** No post tells you to buy, sell or hold anything, and
  none gives a target price, a fair value or a "multibagger" pick.
- **No verdicts on real companies or funds.** When a post names a real company
  or fund, it is there to show how a calculation works on real numbers. We
  don't say whether its valuation is justified, whether its management is good,
  or whether one fund beats another. Valuation models (discounted cash flows,
  justified multiples) are only ever run on
  [Desi Bites Foods]({{ '/case-study/' | relative_url }}), a fictional company,
  or on generic numbers.
- **No personalised advice.** The author is not a SEBI-registered Research
  Analyst or Investment Adviser, and nothing here is tailored to your situation.
- **No hype.** We don't describe any investment as "guaranteed", "sure-shot"
  or "can't lose". Such words appear only when a post explains a product's own
  terms or why a claim like that is a warning sign.

## Independence

Wealth Primer has no sponsored posts, no paid promotions and no affiliate
links, and it carries no advertising. No company, fund house, broker or
platform pays for coverage or sees a post before it is published. If
advertising is ever added, it will be labelled as advertising, it will not
change what any post says, and ad categories that conflict with these
standards (trading platforms, crypto and betting) will be blocked.

The [calculators]({{ '/tools/' | relative_url }}) follow the same line: they
run on numbers you enter and show the working. They never rank, screen or score
real securities or funds, and they never tell you what to do.

## How a post is made

**Structure.** Most posts follow the same pattern: a definition, the formula, a
worked example on real data, the common mistakes people make with the concept,
and a short takeaway. Posts say what a concept can't tell you as well as what
it can.

**Numbers.** Figures in worked examples are calculated by script from committed
data files and rendered into the post from those files, not typed in by hand,
so a chart and the sentence beside it can't disagree. Each dataset, its source
and its date range are listed on the
[data & methodology page]({{ '/methodology/' | relative_url }}).

**Lagged data.** Any real market price, NAV or company figure used in a worked
example is at least three months old when the post publishes, and the post
states its as-of date. This is our own rule, set deliberately on the cautious
side; it is not a quotation of a regulation. Past figures are used to show how
a calculation works, never as a signal about what happens next.

**Sources.** Data comes from primary sources wherever they can be reached:
company filings, AMFI, the exchanges, RBI, SEBI and government publications.
Where a post relies on a secondary source (a data vendor, or a report of a
study rather than the study itself), it says so.

**Checks before publishing.** Before a post is scheduled, it is checked
against a written list: that it makes no call or verdict, that each sentence
interpreting a table says no more than the table shows, that rules are sourced,
and that the house style is followed. The author decides what is published.

## Tax and regulation

Rules change often, and a confident sentence about an old rule can cost a
reader money. So:

- Every rule, rate, threshold or deadline is taken from the primary source
  (the Act, a CBDT notification, a SEBI or RBI circular), cited with its number
  and date. If we can't confirm the current position from the source, the post
  says so and tells you to check.
- A post that states a tax, market or insurance rule shows a notice under its
  title with the date its rules were checked. It also says plainly that the
  author is not a tax professional (or the relevant professional) and that the
  post has not been reviewed by one. No professional review is currently
  planned; we won't claim one that hasn't happened.
- Tax posts teach how a rule works. They don't tell you how to save tax or what
  you should do.
- Rule-bearing posts are re-checked after each Union Budget, and their "rules
  as at" date changes only when the rules really were re-checked.

## Dates on a post

- **Published** is the date the post first went live.
- **Updated** appears only when a post has been changed in substance: a
  correction, a rule that changed, or new data. Fixing a typo or a broken link
  doesn't change it.
- **Rules as at** (on tax and regulation posts) is the date the rules were last
  checked against their sources.

## Corrections

We would rather fix a mistake in public than leave it standing.

**How to tell us.** Email [{{ site.email }}](mailto:{{ site.email }}) with the
post's link and what looks wrong. A number that doesn't reconcile, a rule that
has changed, a sentence that says more than its data shows: all welcome.

**What we do.**

1. Check the claim against the source or the data file.
2. Fix it at the source. A wrong number is corrected in the data file, so every
   post that uses it updates together.
3. For a material error (a wrong figure, rule, sign or interpretation), add a
   dated note at the end of the post saying what was wrong and what changed,
   and update the post's "Updated" date. Typos, formatting and broken links are
   fixed without a note.
4. Correction notes are never deleted.

We can't answer questions about your own investments or taxes; see the
[disclaimer]({{ '/privacy/' | relative_url }}).

### Correction log

{% assign corrected = site.posts | where_exp: "p", "p.corrections" -%}
{%- if corrected.size > 0 -%}
| Post | Corrected | What changed |
|---|---|---|
{% for p in corrected -%}
{%- for c in p.corrections -%}
| [{{ p.title | escape }}]({{ p.url | relative_url }}#corrections) | {{ c.date | date: "%-d %B %Y" }} | {{ c.note | strip_newlines | replace: "|", "&#124;" }} |
{% endfor -%}
{%- endfor %}
{%- else -%}
No corrections have been logged yet.
{%- endif %}

Correction notes began on 22 November 2026. Before then, fixes were made
without notes on the posts. The largest was
a full review of every post then published, in September 2026, which corrected
a number of interpretive errors. Every change to the site, including those, is
recorded in its public history on
[GitHub](https://github.com/himanshug82/wealthprimer/commits/main).

## Who writes this

Wealth Primer is written by [Himanshu Gupta]({{ '/about/' | relative_url }}),
a software engineer and retail investor. More about the author and why the blog
exists is on the [about page]({{ '/about/' | relative_url }}).
