---
layout: page
title: "Series"
permalink: /series/
---

Wealth Primer is organised into four learning series. Each one is written to be
read in order — later posts link back to earlier ones instead of re-explaining
the same ground twice.

Posts publish on a schedule, so a series list grows over time.

{% for s in site.data.series %}
{%- assign in_series = site.posts | where: "series", s.slug -%}
### [{{ s.title }}]({{ '/series/' | append: s.slug | append: '/' | relative_url }})

{{ s.description }}

*{{ in_series.size }} post{% if in_series.size != 1 %}s{% endif %} published so far.*
{% endfor %}
