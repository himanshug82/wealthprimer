---
layout: page
title: "Glossary"
permalink: /glossary/
description: "A–Z index of every financial term and ratio Wealth Primer has explained — P/E, ROCE, drawdown, XIRR, WACC and more — each linking to the post that decodes it with a worked example."
---

{%- comment -%}
Built from every published post that carries a `term:` in its front matter,
across all series — a Jargon post on ROCE, the FA post on WACC and the MF post
on drawdown are all glossary entries. Add `term:` to a post and it appears
here on its publish date; there is nothing to edit on this page.

This is the page CLAUDE.md's "link at first use" rule points at: if a term is
listed here, a new post should link to its post instead of re-explaining it.
{%- endcomment -%}

Every term below links to the post that explains it — definition, formula,
and a worked example on real numbers. It grows as posts publish; if a term you
need isn't here yet, it's probably on the [series roadmap]({{ '/series/' | relative_url }}).

{% assign terms = site.posts | where_exp: "p", "p.term" | sort_natural: "term" %}
{% assign letters = "" | split: "" %}
{% for p in terms %}{% assign l = p.term | slice: 0 | upcase %}{% unless letters contains l %}{% assign letters = letters | push: l %}{% endunless %}{% endfor %}

<p class="glossary-letters">
{%- for l in letters -%}
<a href="#{{ l | downcase }}">{{ l }}</a>
{%- endfor -%}
</p>

<p class="glossary-count">{{ terms.size }} terms so far.</p>

{% assign current = "" %}
{% for p in terms %}
{%- assign l = p.term | slice: 0 | upcase -%}
{%- if l != current -%}
{%- if current != "" %}</dl>{% endif -%}
{%- assign current = l %}
<h3 class="glossary-letter" id="{{ l | downcase }}">{{ l }}</h3>
<dl class="glossary-list">
{%- endif -%}
{%- assign meta = site.data.series | where: "slug", p.series | first -%}
<dt><a href="{{ p.url | relative_url }}">{{ p.term | escape }}</a>{% if meta %} <a class="post-series-tag" href="{{ '/series/' | append: p.series | append: '/' | relative_url }}">{{ meta.title }}</a>{% endif %}</dt>
<dd>{{ p.description | escape }}</dd>
{%- endfor %}
{%- if current != "" %}</dl>{% endif %}
