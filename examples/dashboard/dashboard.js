/* Presentation for the fixed synthetic fixture. No input ingestion or network access. */
"use strict";
const { rows, status, select, summarize } = globalThis.TaxDemo;
const byId = id => document.getElementById(id);
const money = cents => cents === null ? "Unknown" : new Intl.NumberFormat("en-US", {
  style: "currency", currency: "USD", minimumFractionDigits: 2,
}).format(cents / 100);
const text = (id, value) => { byId(id).textContent = value; };
function node(tag, value, className) {
  const element = document.createElement(tag);
  if (value !== undefined) element.textContent = value;
  if (className) element.className = className;
  return element;
}
function render() {
  const filter = { state: byId("state").value, period: byId("period").value,
    exceptions: byId("exceptions").checked };
  const selected = select(rows, filter);
  const totals = summarize(selected);
  const absent = totals.count === 0;
  text("scope", `${filter.state === "all" ? "All states" : filter.state} / ${filter.period === "all" ? "All periods" : filter.period} / ${filter.exceptions ? "Exceptions only" : "All comparison statuses"} / ${totals.count} of ${rows.length} synthetic records`);
  for (const key of ["book", "net", "gross", "missingBook"]) text(key, absent ? "No data" : money(totals[key]));
  if (!absent && totals.equal + totals.different === 0) {
    text("net", "No pairs"); text("gross", "No pairs");
  }
  text("count", `${totals.count} selected records; periods are separate rows`);
  text("missingCount", `${totals.missing} missing ${totals.missing === 1 ? "bill" : "bills"}; no difference inferred`);
  text("rowTag", `${totals.count} records`);
  text("notice", absent ? "No records match these filters. This is not a successful reconciliation."
    : totals.different || totals.missing ? `${totals.different} paired differences and ${totals.missing} missing bills require investigation. A zero net difference can hide exceptions.`
      : "The selected amounts agree. Evidence and human review are still required before sign-off.");

  const body = byId("records"); body.replaceChildren();
  for (const row of selected) {
    const tr = node("tr");
    for (const value of [row.id, row.state, row.period]) tr.append(node("td", value));
    for (const amount of [row.book, row.bill, row.bill === null ? null : row.book - row.bill]) tr.append(node("td", money(amount), "num"));
    const td = node("td");
    td.append(node("span", status(row), `status ${row.bill === null ? "missing" : row.book === row.bill ? "equal" : "difference"}`));
    tr.append(td); body.append(tr);
  }
  if (absent) { const tr = node("tr"); const td = node("td", "No records match. Reset filters to see the full exercise.", "empty"); td.colSpan = 7; tr.append(td); body.append(tr); }
  text("controls", absent ? "Control checks: no population selected; no acceptance conclusion."
    : `Book population: ${money(totals.pairedBook)} paired + ${money(totals.missingBook)} missing-bill records = ${money(totals.book)}. Paired amounts: ${money(totals.pairedBook)} book - ${money(totals.pairedBill)} bill = ${money(totals.net)} net. Status counts: ${totals.equal} equal + ${totals.different} different + ${totals.missing} missing = ${totals.count}.`);

  const bars = byId("bars"); bars.replaceChildren();
  const groups = [...new Set(selected.map(row => row.state))].map(state => ({ state,
    amount: summarize(selected.filter(row => row.state === state)).gross }));
  const max = Math.max(1, ...groups.map(group => group.amount));
  for (const group of groups) {
    const row = node("div", undefined, "bar-row"); row.append(node("span", group.state));
    const track = node("div", undefined, "track"); track.setAttribute("aria-hidden", "true");
    const fill = node("div", undefined, "fill"); fill.style.width = `${group.amount / max * 100}%`; track.append(fill);
    row.append(track, node("span", money(group.amount), "bar-amount")); bars.append(row);
  }
  if (absent) bars.append(node("p", "No data for this selection.", "empty"));

  const categories = [["Equal amounts", totals.equal, "#006b62"], ["Difference", totals.different, "#bc792f"], ["Missing bill", totals.missing, "#af3643"]];
  const legend = byId("legend"); legend.replaceChildren();
  for (const [label, count, color] of categories) {
    const row = node("div", undefined, "legend-row"); const swatch = node("span", undefined, "swatch");
    swatch.style.background = color; swatch.setAttribute("aria-hidden", "true");
    row.append(swatch, node("span", label), node("strong", String(count))); legend.append(row);
  }
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg"); svg.setAttribute("viewBox", "0 0 120 120");
  svg.setAttribute("role", "img"); svg.setAttribute("aria-label", absent ? "No selected records" : `${totals.equal} equal, ${totals.different} different, ${totals.missing} missing bill`);
  function circle(color) { const c = document.createElementNS(ns, "circle"); for (const [name, value] of Object.entries({ cx: 60, cy: 60, r: 44, fill: "none", stroke: color, "stroke-width": 13 })) c.setAttribute(name, value); return c; }
  svg.append(circle("#edf2f1"));
  let offset = 0; const length = 2 * Math.PI * 44;
  if (!absent) for (const [, count, color] of categories) {
    const arc = circle(color); const part = count / totals.count * length;
    arc.setAttribute("stroke-dasharray", `${part} ${length - part}`);
    arc.setAttribute("stroke-dashoffset", -offset); arc.setAttribute("transform", "rotate(-90 60 60)");
    svg.append(arc); offset += part;
  }
  const center = document.createElementNS(ns, "text"); center.setAttribute("x", "60"); center.setAttribute("y", "65"); center.setAttribute("text-anchor", "middle"); center.setAttribute("font-size", "23"); center.setAttribute("fill", "#162a31"); center.textContent = String(totals.count); svg.append(center);
  byId("ring").replaceChildren(svg);
}
for (const id of ["state", "period", "exceptions"]) byId(id).addEventListener("change", render);
byId("reset").addEventListener("click", () => { byId("state").value = "all"; byId("period").value = "all"; byId("exceptions").checked = false; render(); });
byId("print").addEventListener("click", () => window.print());
render();
