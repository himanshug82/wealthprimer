---
layout: page
title: "Tools"
permalink: /tools/
description: "Free calculators for Indian investors: rolling returns, SIP and XIRR, DCF, loss recovery, cost drag and real returns, each tied to its explainer post."
---

{%- comment -%}
Cards are built from _data/tools.yml; there is nothing to edit on this page.
To add a tool, add an entry there, a stub page in _tools/<id>.md, and link it
from the relevant posts with {% include tool.html id="..." %}.
{%- endcomment -%}

Calculators you can use without writing code. Each one comes with a post
that explains the method step by step, and each reproduces that post's
worked example, so you can check it before trusting it with your own numbers.

The calculators work right on the page. The Google Sheets open view-only: use
**File → Make a copy** to get your own editable version. Either way, nothing
you type is shared with us or anyone else.

<ul class="tools-grid">
{%- for t in site.data.tools %}
{%- assign _ps = site.data.series | where: "slug", t.series | first -%}
{%- assign _post = site.posts | where: "slug", t.post | first %}
<li class="tool-card" id="{{ t.id }}">
<span class="tool-kind">{{ t.kind | escape }}{% if _ps %} · {{ _ps.title | split: " — " | first }}{% endif %}</span>
<h2><a href="{{ '/tools/' | relative_url }}{{ t.id }}/">{{ t.name | escape }}</a></h2>
<p>{{ t.summary | escape }}</p>
<p class="tool-data">Prefilled with: {{ t.data | escape }}.</p>
<p class="tool-actions">
{%- if t.calc %}
<a class="button button-primary" href="{{ '/tools/' | relative_url }}{{ t.id }}/">Use the calculator</a>
{%- else %}
<a class="button button-primary" href="{{ t.url }}">Open the {{ t.kind | escape }}</a>
<a class="tool-explainer" href="{{ '/tools/' | relative_url }}{{ t.id }}/">How to use it</a>
{%- endif %}
{%- if _post %}
<a class="tool-explainer" href="{{ _post.url | relative_url }}">How it works: {{ _post.title | escape }}</a>
{%- endif %}
</p>
</li>
{%- endfor %}
</ul>

These are teaching tools. They show how a calculation works on the numbers
you give them; they don't tell you what to buy, sell or hold, and they don't
value any real listed company. See the [disclaimer]({{ '/privacy/' | relative_url }}).
