---
layout: page
title: "Series"
description: "Every Wealth Primer learning series in reading order: jargon, fundamental analysis, technical analysis, mutual funds, tax and risk for Indian investors."
permalink: /series/
---
{%- comment -%}
Only series with at least one published post are listed (same rule as the
homepage cards and the footer) — a series shows up here the day its first
post goes live.
{%- endcomment -%}
{%- assign live_count = 0 -%}
{%- for s in site.data.series -%}
{%- assign in_series = site.posts | where: "series", s.slug -%}
{%- if in_series.size > 0 -%}{%- assign live_count = live_count | plus: 1 -%}{%- endif -%}
{%- endfor %}

Wealth Primer is organised into learning series{% if live_count > 1 %} — {{ live_count }} so far{% endif %}. Each one is written to be
read in order: later posts link back to earlier ones instead of re-explaining
the same ground. Pick the series that matches the question you have today;
the [glossary]({{ '/glossary/' | relative_url }}) is the quickest way in if
you're after one term.

Posts publish on a schedule, so each series grows over time, and a new series
appears here when its first post goes live.

{% for s in site.data.series %}
{%- assign in_series = site.posts | where: "series", s.slug | sort: "date" -%}
{%- if in_series.size == 0 -%}{%- continue -%}{%- endif %}
{%- assign first = in_series | first -%}{%- assign latest = in_series | last %}
## [{{ s.title }}]({{ '/series/' | append: s.slug | append: '/' | relative_url }})

{{ s.about | default: s.description }}

- **Start with:** [{{ first.title }}]({{ first.url | relative_url }})
- **Latest:** [{{ latest.title }}]({{ latest.url | relative_url }}) ({{ latest.date | date: "%-d %B %Y" }})
- **{{ in_series.size }} post{% if in_series.size != 1 %}s{% endif %} so far** — [see them all in reading order]({{ '/series/' | append: s.slug | append: '/' | relative_url }})
{% endfor %}
