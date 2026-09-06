---
name: financial-dashboard
description: Create or improve an accounting dashboard from approved spreadsheet or reconciliation data, with source totals, exception details, filters, and verification. Use for Excel dashboards or local HTML reports.
---

# Build a checked dashboard

State that you are using this skill. Use the requested audience, source, output format, and approved
location. Ask only for material missing details. Preserve originals and do not publish, upload,
install tools, or connect systems without the corresponding authorization.

Establish applicable scope: row grain, keys, jurisdiction, period, source date, and validation
status; include currency when amounts are shown.
Define metrics before building: population, exclusions, aggregation, and filter behavior. Keep
book expense, bills, assessments, payments, and estimates distinct. Identify duplicate/ambiguous
keys before joining. Mark unvalidated inputs draft; do not invent source facts or treat no data
as a passed control.

For reconciliation dashboards, distinguish full Bill minus Book from matched net and matched gross
(sum of absolute matched differences). Keep unmatched amounts and missing values visible. A
missing counterpart stays missing in detail; aggregate each source's known amounts independently
and label the resulting difference clearly. Do not show unmatched absence as a measured zero.

Use Excel for an Excel request, checking installed readers/writers and using the xlsx skill if
available. Prefer a new workbook; advanced features need native Excel checks. For a standalone
HTML request, use a self-contained file with native HTML/CSS/JS, system fonts, escaped labels, no
external requests, and no server requirement. Do not render untrusted cell text as executable HTML.

Use readable cards, labeled charts, and an exception table. Show scope, units, source, generation
date, and snapshot/refresh behavior. Relevant filters must update cards, charts, and details
together. Include reset, active-selection labels, no-data handling, keyboard-accessible controls,
and statuses conveyed with words as well as color. A filter does not protect embedded records.

Independently compare displayed counts and amounts with source records. Test filter selections,
combinations where relevant, reset, empty results, missing counterparts, and offsetting differences.
Inspect the deliverable in a browser or Excel when available; report unavailable UI, calculation,
and offline checks as UNVERIFIED. Reading code is not a browser test. Do not claim refresh from a
static snapshot. Return output location, verified results, remaining checks, and one number the
learner can trace back to its source.

For a research dashboard, count distinct finding IDs and preserve source links, jurisdiction,
property type, tax year, source/access dates, and human review metadata. Keep Needs review items
visible. Research status is not filing status. Do not apply research rules to financial rows or
change amounts without an explicit, reviewed applicability mapping. Test that added research
sections leave existing financial totals unchanged and label any unverified linkage.
