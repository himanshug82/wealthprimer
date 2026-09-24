---
layout: page
title: "Series"
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
read in order — later posts link back to earlier ones instead of re-explaining
the same ground twice.

Posts publish on a schedule, so a series list grows over time, and new series
appear here as their first post goes live.

{% for s in site.data.series %}
{%- assign in_series = site.posts | where: "series", s.slug -%}
{%- if in_series.size == 0 -%}{%- continue -%}{%- endif %}
### [{{ s.title }}]({{ '/series/' | append: s.slug | append: '/' | relative_url }})

{{ s.description }}

*{{ in_series.size }} post{% if in_series.size != 1 %}s{% endif %} published so far.*
{% endfor %}
