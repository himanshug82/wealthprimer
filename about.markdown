---
nav_section: about
layout: page
title: About
description: "About Wealth Primer: a software engineer and retail investor explaining investing concepts for Indian readers, with sourced data and no stock tips."
permalink: /about/
---

{%- comment -%}
ProfilePage + Person structured data: names the author every post links to in its byline
(_layouts/post.html). Only facts stated on this page; sameAs lists accounts the author runs.
{%- endcomment -%}
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfilePage","url":{{ page.url | absolute_url | jsonify }},
"mainEntity":{"@type":"Person","name":{{ site.author | jsonify }},"url":{{ page.url | absolute_url | jsonify }},
"image":{{ '/assets/avatar.svg' | absolute_url | jsonify }},
"description":"Software engineer and retail investor who writes Wealth Primer, an investing education blog for Indian readers.",
"sameAs":["https://twitter.com/{{ site.twitter_username }}","https://github.com/wealthprimer/wealthprimer"]}}
</script>

<img class="about-avatar" src="{{ '/assets/avatar.svg' | relative_url }}" alt="HG monogram for Himanshu Gupta, the author" width="96" height="96">

I'm Himanshu Gupta. I run Wealth Primer and I'm responsible for every post on it.

I've spent 20 years writing software — starting out on order and inventory
management systems for large retailers, and later moving into large-scale
distributed systems, including open-source work in the supply-chain space.
Somewhere along the way I became this blog's target audience too: I've been a
retail investor for the last decade, and I've made my fair share of mistakes
along the way. The last few years, I've been trying to bring more structure
to that by moving toward rule-based, systematic trading — and Wealth Primer
is part of that effort. I write up what I'm learning, partly to hold myself
accountable to actually understanding it, and share it because it might be
useful to someone else working through the same things.

## What I'm not

I'm not a SEBI-registered Research Analyst or Investment Adviser, and I'm not
a chartered accountant or tax professional — just a retail investor and hobby
coder doing my homework in public. Take everything here as a fellow learner's
notes, not advice. Posts that state a tax or market rule say so under their
title, with the date the rule was checked. See the
[privacy & disclaimer policy]({{ '/privacy/' | relative_url }}) for the full
version.

## What I write about

How investing works in India, one concept at a time: reading a company's
accounts, the ratios built from them, how mutual fund returns and costs are
measured, how charts are read (and what they can't tell you), how investments
are taxed, and how risk and leverage work. Good places to start:

- [The Indian Investor's Guide to Mutual Funds]({{ '/guides/mutual-funds/' | relative_url }})
- [How to Analyse Stocks]({{ '/guides/stocks/' | relative_url }})
- [Understanding Investment Risk]({{ '/guides/risk/' | relative_url }})
- [Building Your Investment Portfolio]({{ '/guides/portfolio/' | relative_url }})
- [Every series]({{ '/series/' | relative_url }}) and the
  [calculators]({{ '/tools/' | relative_url }})

## How I work

My software background shapes how the blog is built. Every number on it is
sourced and lagged, and most are derived by script from committed data files
rather than typed in, so a table and the sentence beside it can't drift apart.
The [data & methodology page]({{ '/methodology/' | relative_url }}) lists each
dataset, its source and the rules the posts follow. What posts will never
contain (tips, calls, verdicts on real companies), how they are checked
before publishing, and how mistakes are corrected are on the
[editorial standards page]({{ '/editorial-standards/' | relative_url }}),
which also keeps a public log of corrections.

Each post shows when it was published, when it was last changed in substance,
and, where it has had one, when it was last re-checked against its sources.

Wealth Primer has no sponsors, paid promotions or affiliate links, and no one
pays for coverage.

## Elsewhere

- Twitter/X: [@wealthprimer_in](https://twitter.com/wealthprimer_in)
- Code & calculators: [github.com/wealthprimer/wealthprimer](https://github.com/wealthprimer/wealthprimer)
- Email: [{{ site.email }}](mailto:{{ site.email }}) — spotted a mistake? Send
  the post's link and what looks wrong.
