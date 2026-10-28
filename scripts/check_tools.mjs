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

let n = 0, bad = 0;
for (const [tool, spec] of Object.entries(data)) {
  if (tool.startsWith("_")) continue;
  for (const c of spec.cases) {
    const got = F[c.calc](c.inputs);
    for (const [key, [want, d]] of Object.entries(c.expect)) {
      n++;
      if (rnd(got[key], d) !== rnd(want, d)) {
        bad++;
        console.log(`FAIL ${tool} ${c.calc}(${JSON.stringify(c.inputs)}).${key} = ${rnd(got[key], d)}, post shows ${want}`);
      }
    }
  }
}
console.log(`${n} calculator figures checked against the posts: ${bad} mismatch(es)`);
process.exit(bad ? 1 : 0);
