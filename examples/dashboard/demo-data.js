/* Entirely invented teaching data. Amounts are USD cents. No real property records. */
(function (root) {
  "use strict";
  const rows = [
    { id: "DEMO-01", state: "STATE-A", period: "PERIOD-1", book: 120000, bill: 120000 },
    { id: "DEMO-02", state: "STATE-A", period: "PERIOD-1", book: 80000, bill: 75000 },
    { id: "DEMO-03", state: "STATE-B", period: "PERIOD-1", book: 60000, bill: 65000 },
    { id: "DEMO-04", state: "STATE-B", period: "PERIOD-1", book: 40000, bill: null },
    { id: "DEMO-05", state: "STATE-C", period: "PERIOD-1", book: 100000, bill: 100000 },
    { id: "DEMO-06", state: "STATE-C", period: "PERIOD-1", book: 50000, bill: 48000 },
    { id: "DEMO-07", state: "STATE-A", period: "PERIOD-2", book: 125000, bill: 125000 },
    { id: "DEMO-08", state: "STATE-A", period: "PERIOD-2", book: 82000, bill: 82000 },
    { id: "DEMO-09", state: "STATE-B", period: "PERIOD-2", book: 63000, bill: 63000 },
    { id: "DEMO-10", state: "STATE-B", period: "PERIOD-2", book: 42000, bill: null },
    { id: "DEMO-11", state: "STATE-C", period: "PERIOD-2", book: 101000, bill: 101000 },
    { id: "DEMO-12", state: "STATE-C", period: "PERIOD-2", book: 52000, bill: 54000 },
  ];
  function status(row) {
    return row.bill === null ? "Missing bill" : row.book === row.bill ? "Equal amounts" : "Difference";
  }
  function select(source, { state = "all", period = "all", exceptions = false } = {}) {
    return source.filter(row => (state === "all" || row.state === state)
      && (period === "all" || row.period === period)
      && (!exceptions || status(row) !== "Equal amounts"));
  }
  function summarize(source) {
    const result = { count: source.length, book: 0, pairedBook: 0, pairedBill: 0,
      net: 0, gross: 0, missingBook: 0, missing: 0, equal: 0, different: 0 };
    for (const row of source) {
      result.book += row.book;
      if (row.bill === null) {
        result.missing++;
        result.missingBook += row.book;
      } else {
        result.pairedBook += row.book;
        result.pairedBill += row.bill;
        result.net += row.book - row.bill;
        result.gross += Math.abs(row.book - row.bill);
        if (row.book === row.bill) result.equal++; else result.different++;
      }
    }
    return result;
  }
  const api = { rows, status, select, summarize };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.TaxDemo = api;
})(globalThis);
