// Behavioral checks for the teaching example, using only Node's standard library.
import assert from "node:assert/strict";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const { rows, select, summarize, status } = require("../examples/dashboard/demo-data.js");

assert.equal(new Set(rows.map(row => row.id)).size, 12);
assert.deepEqual(summarize(rows), {
  count: 12, book: 915000, pairedBook: 833000, pairedBill: 833000,
  net: 0, gross: 14000, missingBook: 82000, missing: 2, equal: 6, different: 4,
});
assert.deepEqual(["PERIOD-1", "PERIOD-2"].map(period => {
  const s = summarize(select(rows, { period }));
  return [s.count, s.book, s.net, s.gross, s.missingBook];
}), [[6, 450000, 2000, 12000, 40000], [6, 465000, -2000, 2000, 42000]]);
assert.equal(summarize(select(rows, { state: "STATE-A", period: "PERIOD-1" })).net, 5000);
assert.equal(select(rows, { state: "STATE-A", period: "PERIOD-2", exceptions: true }).length, 0);
assert.equal(select(rows, { exceptions: true }).length, 6);
assert.deepEqual(select(rows), rows);
assert.equal(status(rows[3]), "Missing bill");
assert.equal(summarize([rows[3]]).pairedBill, 0);
assert.equal(summarize([rows[3]]).missingBook, 40000);
assert.equal(summarize([rows[1], rows[2]]).net, 0);
assert.equal(summarize([rows[1], rows[2]]).gross, 10000);
assert.equal(summarize([]).count, 0);

// Every possible UI selection must preserve the displayed population identities.
for (const state of ["all", "STATE-A", "STATE-B", "STATE-C"])
  for (const period of ["all", "PERIOD-1", "PERIOD-2"])
    for (const exceptions of [false, true]) {
      const source = select(rows, { state, period, exceptions });
      const s = summarize(source);
      assert.equal(s.count, s.equal + s.different + s.missing);
      assert.equal(s.book, s.pairedBook + s.missingBook);
      assert.equal(s.net, s.pairedBook - s.pairedBill);
      assert.ok(s.gross >= Math.abs(s.net));
      assert.deepEqual(source, rows.filter(r => (state === "all" || r.state === state)
        && (period === "all" || r.period === period)
        && (!exceptions || r.bill === null || r.book !== r.bill)));
    }
console.log("OK dashboard fixtures, edge cases, and 24 filter combinations");
