---
layout: page
title: "Search"
permalink: /search/
description: "Search every Wealth Primer explainer, calculator and glossary term for Indian investors by keyword, from P/E and NAV to XIRR, drawdown and capital gains."
noindex: true
sitemap: false
---
{%- comment -%}
Client-side search (decision D2): assets/js/search.js loads /search.json and filters it in the
browser. No server, no third-party service, nothing sent anywhere. The form also works from the
header box, which submits ?q= here. Noindexed: a search page is not a page to rank.
{%- endcomment -%}

<form class="search-page-form" role="search" action="{{ '/search/' | relative_url }}" method="get">
  <label class="visually-hidden" for="search-page-q">Search Wealth Primer</label>
  <input id="search-page-q" type="search" name="q" placeholder="Try ROCE, rolling returns or exit load" autocomplete="off">
  <button type="submit">Search</button>
</form>

<p class="search-status" id="search-status" aria-live="polite"></p>
<ol class="search-results" id="search-results" data-index="{{ '/search.json' | relative_url }}"></ol>

<noscript>
  <p>Search needs JavaScript. You can browse every term in the <a href="{{ '/glossary/' | relative_url }}">glossary</a> or every post by <a href="{{ '/series/' | relative_url }}">series</a> instead.</p>
</noscript>

<script src="{{ '/assets/js/search.js' | relative_url }}" defer></script>
