/*
 * Site search for /search/ (decision D2). Loads /search.json once (built by Jekyll from the
 * published posts, tools and pages) and filters it in the browser: no server, no third-party
 * service, the query never leaves the page.
 *
 * Every word in the query must appear in an entry's title, glossary term, description or
 * section. Ranking: term and title matches above description matches, then site order
 * (newest posts first). Results are built with textContent, never innerHTML.
 */
(function () {
  "use strict";

  var list = document.getElementById("search-results");
  var status = document.getElementById("search-status");
  var input = document.getElementById("search-page-q");
  if (!list || !status || !input) return;

  var MAX = 50;
  var index = null;

  function norm(s) {
    return (s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, "");
  }

  function score(entry, words) {
    var t = norm(entry.t), k = norm(entry.k), d = norm(entry.d), s = norm(entry.s);
    var total = 0;
    for (var i = 0; i < words.length; i++) {
      var w = words[i], hit = 0;
      if (k && k.indexOf(w) !== -1) hit += 6;
      if (t.indexOf(w) !== -1) hit += 4;
      if (d.indexOf(w) !== -1) hit += 1;
      if (s.indexOf(w) !== -1) hit += 1;
      if (!hit) return 0;
      total += hit;
    }
    return total;
  }

  function render(query) {
    while (list.firstChild) list.removeChild(list.firstChild);
    var words = norm(query).split(/[^a-z0-9%&/.₹-]+/).filter(Boolean);
    if (!words.length) { status.textContent = ""; return; }

    var hits = [];
    for (var i = 0; i < index.length; i++) {
      if (!index[i].u) continue;
      var sc = score(index[i], words);
      if (sc) hits.push({ e: index[i], sc: sc, i: i });
    }
    hits.sort(function (a, b) { return b.sc - a.sc || a.i - b.i; });

    status.textContent = hits.length === 0
      ? "No results for “" + query + "”. Try a shorter word, or browse the glossary."
      : hits.length + (hits.length === 1 ? " result" : " results") + " for “" + query + "”" +
        (hits.length > MAX ? ", showing the first " + MAX : "");

    hits.slice(0, MAX).forEach(function (h) {
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = h.e.u;
      a.textContent = h.e.t;
      li.appendChild(a);
      var meta = [h.e.s, h.e.dt].filter(Boolean).join(" · ");
      if (meta) {
        var m = document.createElement("span");
        m.className = "search-meta";
        m.textContent = meta;
        li.appendChild(m);
      }
      if (h.e.d) {
        var p = document.createElement("p");
        p.textContent = h.e.d;
        li.appendChild(p);
      }
      list.appendChild(li);
    });
  }

  function run() {
    var q = input.value.trim();
    var url = new URL(window.location.href);
    if (q) url.searchParams.set("q", q); else url.searchParams.delete("q");
    window.history.replaceState(null, "", url);
    render(q);
  }

  var initial = new URLSearchParams(window.location.search).get("q") || "";
  input.value = initial;
  status.textContent = initial ? "Searching…" : "";

  fetch(list.getAttribute("data-index"))
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (data) {
      index = data;
      render(initial);
      var timer;
      input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(run, 120); });
      input.form.addEventListener("submit", function (e) { e.preventDefault(); run(); });
    })
    .catch(function () {
      status.textContent = "Search could not load. Browse the glossary or the series pages instead.";
    });
})();
