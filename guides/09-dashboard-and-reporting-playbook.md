# Guide 09: Dashboards that earn trust

A useful dashboard helps its reader make a specific decision: which reconciliations need attention,
what explains a change, or where review is incomplete. Define that question before asking for graphs.

## Choose the deliverable

| Format | Best fit | Tradeoff |
| --- | --- | --- |
| Excel tables, PivotTables, charts | Workpaper review and analysis by accountants | Native workbook features require Excel testing |
| Local HTML snapshot | A polished, interactive report opened in a browser | The file includes its data; refresh is a deliberate new build |
| Approved Power BI environment | Shared governed reporting with scheduled refresh | Needs approved publishing, permissions, model ownership, and refresh configuration |
| PowerPoint or Word | A fixed management narrative or review memo | Numbers must tie to the same approved reporting snapshot |

This is a workflow recommendation, not a claim that Claude Code has those products installed or
can publish to them. For a new learner, start with a local synthetic HTML snapshot or an Excel chart.

## Metrics to define with the accountant

| Candidate metric | Required definition | Common mistake |
| --- | --- | --- |
| Reconciliation completion | Reviewed-complete items / all in-scope required items | Calling an exact numeric match a reviewer sign-off |
| Net difference | Signed difference across comparable paired records | Offsetting errors conceal unresolved items |
| Gross difference | Sum of absolute paired differences | Mixing unmatched exposure into a metric without defining it |
| Unmatched exposure | Amounts present only in each source, separately | Replacing absent values with zero |
| Filing status | Required filings and evidenced status at the cutoff | Treating missing status as filed or due dates as universal |
| Payment status | Approved bill/payment allocation and timing | Duplicating a bill amount across multiple payment rows |
| Exemption review | Cases by evidence and human review status | Labeling a model's suggestion as approved eligibility |
| Period movement | Comparable population plus documented additions/removals and other drivers | Attributing an unexplained change to tax rates |

Keep assessed value, tax amount, expense, accrual, and cash paid distinct. A property count and a
bill count are different metrics. Display source date, reporting period, currency, units, and scope.

## A professional visual brief

Use a quiet background, one main accent color, aligned numbers, and clear spacing. Start with three
or four important figures, a ranked comparison, a small composition or trend, and an exception
table. Use company branding when supplied. Avoid decorative gauges, 3-D pies, excessive colors,
or a chart for every column.

- Bars compare jurisdictions or exception categories accurately.
- Lines show actual time series; one snapshot does not support a trend.
- Waterfalls explain a movement only if the drivers sum to the observed change.
- Donuts/pies show a known whole with a few nonnegative categories; include counts and labels.
- Tables provide exact values and source references for review.

Anticipate 100% and 125% browser zoom, a laptop screen, keyboard use, long labels, no rows, missing
amounts, negative differences, print, and a narrow browser window. Every filter needs a visible
scope and reset. A report is not finished because its screenshot looks good.

## Try the included demonstration

Open [the synthetic dashboard](../examples/dashboard/index.html) in a browser. Keep all three files
in that folder together. No installation, network request, upload, or server is needed. Its data
is wholly invented and its geography uses neutral labels. It is a teaching snapshot, not a tax tool.

1. Compare net difference with gross difference. Opposite differences can cancel.
2. Select one state and period. Confirm the table, chart, and figures agree.
3. Turn on exceptions only, then reset. A numeric match is still not a reviewed reconciliation.
4. Select a combination with no rows. Confirm the interface says no data.
5. Inspect a missing bill. Its difference is unknown, not zero.
6. Print or save a local PDF and check that the scope and caveats remain visible.

The [exercise and expected totals](../examples/dashboard/README.md) explain the source grain and
limits. There is no input/import feature. It does not discover duplicates or reconcile raw files;
it demonstrates presentation of an already structured synthetic comparison.

For an actual work dashboard, create a separate approved project and use the
[`financial-dashboard` skill](../skills/financial-dashboard/SKILL.md). The official Anthropic
[Data dashboard skill](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/build-dashboard)
and [frontend-design skill](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
are further options after reviewing their installation and runtime requirements in Guide 07.

## Report and presentation handoff

Use one validated summary dataset for the workbook, dashboard, memo, and slides. Ask for a
source-to-statement table. Each important narrative claim needs a source, not a plausible story.
Keep unknown drivers visible. Word memos should identify the decision needed, verified evidence,
alternatives, and reviewer. Presentations should lead with the question and result, then show the
supporting comparison, exceptions, and requested decision.

Before sharing, verify totals, filters, rendering, embedded data, intended audience, and approval.
Do not use public GitHub Pages or public hosting for work dashboards. Removing a visible table
does not remove the data from HTML or JavaScript.
