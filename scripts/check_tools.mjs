// Run the on-page calculators' real formulas (assets/js/calc.js) against the
// cases in _data/tool_defaults.json, which scripts/derive_tool_defaults.py
// builds from each post's data. Catches a formula in calc.js drifting from the
// post it illustrates. Local check (scripts/ship_check.sh); needs Node.
//
//     node scripts/check_tools.mjs
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const F = createRequire(import.meta.url)(join(root, "assets/js/calc.js"));
const data = JSON.parse(readFileSync(join(root, "_data/tool_defaults.json"), "utf8"));
const rnd = (x, d) => Math.round(x * 10 ** d) / 10 ** d;

// Rolling returns cases carry a series (a committed CSV column, or inline text)
// instead of plain inputs; parser cases carry the text to parse.
const iso = (t) => new Date(t).toISOString().slice(0, 10);
function series(s) {
  if (s.text) return F.parseSeries(s.text);
  const [head, ...rows] = readFileSync(join(root, s.csv), "utf8").trim().split(/\r?\n/);
  const col = head.split(",").indexOf(s.column);
  return F.parseSeries(rows.map((r) => { const f = r.split(","); return f[0] + "," + f[col]; })
    .filter((l) => !l.endsWith(",")).join("\n"));
}
function run(c) {
  if (c.calc === "parseSeries") {
    const p = F.parseSeries(c.text);
    if (p.error) return p;
    return { rows: p.rows, first: iso(p.dates[0]), last: iso(p.dates[p.rows - 1]), first_value: p.values[0],
             last_value: p.values[p.rows - 1], gap_from: p.gap ? iso(p.gap[0]) : "none" };
  }
  if (c.calc === "rollingReturns") {
    const p = series(c.series);
    return F.rollingReturns(p.dates, p.values, c.inputs.years, c.inputs.threshold);
  }
  return F[c.calc](c.inputs);
}

let n = 0, bad = 0;
for (const [tool, spec] of Object.entries(data)) {
  if (tool.startsWith("_")) continue;
  for (const c of spec.cases) {
    const got = run(c);
    for (const [key, [want, d]] of Object.entries(c.expect)) {
      n++;
      const same = typeof want === "string" ? String(got[key]) === want : rnd(got[key], d) === rnd(want, d);
      if (!same) {
        bad++;
        console.log(`FAIL ${tool} ${c.calc}(${JSON.stringify(c.inputs || c.text)}).${key} = ${typeof want === "string" ? got[key] : rnd(got[key], d)}, post shows ${want}`);
      }
    }
  }
}
console.log(`${n} calculator figures checked against the posts: ${bad} mismatch(es)`);
process.exit(bad ? 1 : 0);
