# Guide 08: Excel and reconciliation in practice

**Reconciliation means explaining why two sets of records agree or differ.** It is not forcing
their totals to match. For example, an approved tax schedule might show an amount still payable
while a ledger includes a payment posted after the schedule's cutoff. That difference needs
evidence and an owner, not a guessed correction.

A corporate property-tax role may handle real estate, business personal property, or both. Common
work includes maintaining property/asset populations, preparing returns or renditions, reviewing
assessments, monitoring bills and payments, supporting exemptions and appeals, reconciling ledger
accounts, and reporting status. The exact responsibilities and accounting policies must come from
the team. The [Finance reconciliation skill](https://github.com/anthropics/knowledge-work-plugins/blob/main/finance/skills/reconciliation/SKILL.md)
is a useful general method, not a substitute for those policies.

## Start with the actual reconciliation

| Comparison | Question | Typical cause to investigate, not assume |
| --- | --- | --- |
| Asset register to filing population | Did all in-scope assets make it into the workpaper? | Additions, disposals, location changes, duplicate assets |
| Tax schedule to general ledger | Do detail and the control account agree at the same cutoff? | Posting timing, adjustments, classification |
| Bill to assessment/support | Does the bill agree with the relevant approved basis? | Revised notice, different period, installment, disputed item |
| Payment record to payable/bill | What was paid, allocated, or remains open? | Partial payments, duplicate payments, unapplied credits |
| Current period to prior period/budget | What explains the movement? | Population, valuation, rate, timing, or unresolved drivers |

Agree on the **grain**, meaning what one row represents, before joining files. A property may have
several taxes, bills, installments, and payments. Property ID alone is often not a unique match key.
The project might require entity + jurisdiction + account + tax year + bill + installment. Those
are candidate components, not a prescribed universal key.

## Select a processing route before editing

| Workbook situation | Recommended route | Proof required |
| --- | --- | --- |
| Explain formulas or inspect a file | Read-only inventory and targeted reads | Referenced sheet/cell coverage; cached values identified |
| New, ordinary `.xlsx` report | Approved Python library such as openpyxl or XlsxWriter | Reopen, check formulas and totals, validate display in Excel |
| Existing `.xlsx` with formulas/charts | Work on a copy; choose a tool after inventory | Before/after structure and feature checks in Excel |
| `.xlsm`, `.xlsb`, Power Query, Power Pivot/Data Model, slicers, external links | Native Excel workflow, manual first; approved automation only after a pilot | Refresh, recalculation, links, pivots, and retained features checked in Excel |
| Many large exports | Approved SQL/Power Query or chunked local processing | Entire population counts and sums, bounded exception output |

openpyxl supports existing PivotTable preservation but is not a general PivotTable creation API.
Its documentation also warns that not every workbook object survives loading and saving.
XlsxWriter creates workbooks; it does not edit an existing one or calculate formula results.
[openpyxl PivotTables](https://openpyxl.readthedocs.io/en/stable/pivot.html),
[openpyxl preservation limits](https://openpyxl.readthedocs.io/en/stable/tutorial.html),
[XlsxWriter FAQ](https://xlsxwriter.readthedocs.io/faq.html).

Writing a formula is not evaluating it. A cached value is a previously saved result, possibly stale.
Excel calculation and refreshing queries or PivotTables are separate activities. An approved native
Excel automation could use its object model, but it must wait for authorized refresh work, verify
calculation and pivot outputs, save a new copy, and reopen it. `CalculateFullRebuild` recalculates
and rebuilds dependencies; it does not prove every external data refresh succeeded.
[Microsoft calculation method](https://learn.microsoft.com/en-us/office/vba/api/excel.application.calculatefullrebuild).

Do not assume `keep_vba` validates macros or preserves every feature. Never enable macros just to
inspect a workbook. Treat unsupported formats as a reason to select an appropriate reader, not
rename the extension. If native Excel is unavailable, leave the relevant checks UNVERIFIED.

## Advanced Excel work Claude can help with

- **Formulas:** explain and review SUMIFS/COUNTIFS, exact lookups, INDEX/MATCH, XLOOKUP, LET,
  dynamic arrays, structured references, and error handling against the installed Excel version.
  Confirm availability in that version. Do not replace an existing model's formulas simply to
  satisfy a different engine. `IFERROR(...,0)` can hide a missing record as a legitimate zero.
- **PivotTables:** define source grain, aggregation, filters/slicers, blank handling, grand totals,
  and the refresh process. A sum of numeric identifiers or an average of percentages may be wrong.
- **Power Query:** document types and transformations, merge on approved keys, use anti-joins to
  expose unmatched records, and check duplicate expansion before loading. Fuzzy matches are review
  candidates, not automatic evidence of identity.
- **Power Pivot/DAX:** clarify relationships and filter context; recompute ratios from numerator
  and denominator instead of averaging displayed rates. Validate in the organization's model.
- **SQL:** draft a bounded read-only query for a human to review and run through an approved tool.
  Record dialect, parameter types, cutoff, joins, null treatment, and counts. Do not infer access.

Power Query supports several join types, including full outer and anti joins.
[Microsoft merge documentation](https://learn.microsoft.com/en-us/power-query/merge-queries-overview).

## A repeatable control sequence

1. **Inventory:** source/version, extraction cutoff, row grain, currency, period, sheet/table.
2. **Baseline:** rows, distinct keys, missing keys, duplicate groups, signed sums, absolute sums.
3. **Normalize explicitly:** retain original values beside normalized keys; preserve leading zeros,
   meaningful punctuation, date conventions, negative signs, precision, and blank versus zero.
4. **Match:** validate uniqueness first. Use exact keys. Aggregate only with an approved grain
   and rule; many-to-many joins can multiply amounts while producing plausible results.
5. **Classify:** unique equal pair, unique unequal pair, source-A-only, source-B-only, ambiguous
   duplicate group, invalid/missing key. Keep these populations mutually exclusive per source row.
6. **Explain:** distinguish supported timing differences from unknown causes. Assign reviewer roles
   and follow-up status without inventing approvals or adjustment entries.
7. **Prove completeness:** each source's original rows and amounts equal its classified rows and
   amounts. Paired A minus paired B equals the sum of paired differences. Report unmatched amounts
   separately. Show absolute exceptions because equal opposite errors can net to zero.
8. **Deliver:** new workpaper, exceptions, assumptions, transformation/query, control results,
   input identity, and review status. A failed control prevents a clean completion claim.

An approved tolerance may affect triage; it does not erase the difference. Distinguish a technical
rounding tolerance from accounting materiality. Use decimal arithmetic or integer minor units for
fixed-currency calculations, with an explicit rounding policy. Do not sum across currencies.

## Large files without overwhelming the model

Ask Claude to inspect schemas and aggregate diagnostics first. Let a deterministic local tool
process all records, then provide counts, totals, and a bounded exception sample to the model.
Mark sampled review separately from full-population checks. Do not silently truncate exports or
load an entire folder into chat.

An Excel sheet has 1,048,576 rows; the header also occupies a row. Power Query capacity depends on
the operation and available memory, and 32-bit environments have tighter limits. Confirm Office
bitness, approved storage, source size, and existing IT-supported tools before choosing a route.
[Excel limits](https://support.microsoft.com/en-us/office/excel-specifications-and-limits-1672b34d-7043-467e-8e27-269d656771c3),
[Power Query limits](https://support.microsoft.com/en-us/office/power-query-specifications-and-limits-in-excel-5fb2807c-1b16-4257-aa5b-6793f051a9f4).

## State rules and exemptions

State is not always the filing unit. Track the relevant local jurisdiction, entity, property type,
tax year, valuation date, and assessment/filing/payment periods independently. Texas publishes a
business personal property rendition form; Florida publishes a tangible personal property return.
Their existence illustrates why a generic nationwide template cannot supply the applicable rule.
[Texas forms](https://comptroller.texas.gov/taxes/property-tax/forms/),
[Florida forms](https://floridarevenue.com/property/Pages/Forms.aspx).

An exemption is a distinct eligibility and evidence question, not another word for reconciliation.
Use [the exemption project template](../templates/projects/EXEMPTION-CLAUDE.md) to organize primary
authority and review. Do not preload fifty states' rates, deadlines, or eligibility rules from model
memory. An authoritative source still needs the correct effective year and applicability facts.

Next: choose a prompt from the [prompt library](../prompts/PROMPT-LIBRARY.md).
