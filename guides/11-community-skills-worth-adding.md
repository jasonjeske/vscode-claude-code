# Guide 11: Community skills worth adding

**Start with UI/UX Pro Max for dashboard design and Pandas Pro for repeatable data preparation.**
Add Impeccable when you want deeper visual refinement, SQL Pro when you write queries, and the
focused K-Dense skills when large-data processing or report graphics justify them.

These community recommendations complement the [official shortlist](07-trusted-skills-and-installation.md).
They are source-reviewed recommendations, not installed or bundled skills. Review date:
**September 5, 2026 (UTC)**. No recommendation here is based on a star count, and none has been
tested in the target Windows/gateway environment.

## The six picks

| Pick | Best contribution to this workflow | Add when |
| --- | --- | --- |
| **UI/UX Pro Max** | A coherent dashboard design: layout, typography, colors, charts, accessible interaction | Building the first substantial dashboard |
| **Impeccable** | Visual critique, polish, clearer labels, responsive refinement, and edge-case presentation | Improving an existing dashboard after its numbers are checked |
| **Pandas Pro** | Repeatable joins, grouping, reshaping, and diagnostics across exports | The same spreadsheet preparation keeps recurring |
| **SQL Pro** | Clear queries, window functions, query plans, and database-specific optimization | Drafting queries for an approved database workflow |
| **K-Dense Polars** | Lazy/expression-based processing for larger tabular datasets | Profiling shows a real performance or memory problem |
| **K-Dense Matplotlib** | Precisely styled charts exported for Word, PowerPoint, or PDF | Producing consistent graphics from a validated summary |

For native Excel workbooks, retain the XLSX/native-Excel guidance from Guide 08. A pandas pivot is
a summary table, not a native Excel PivotTable with a cache and slicers. A design skill is not a
calculation engine. These distinctions let the tools work together without overpromising.

## 1. UI/UX Pro Max: first choice for dashboard design

The skill uses local searchable design data and Python helpers to choose a visual system and
retrieve focused guidance. Its chart and dense-layout guidance fit accounting dashboards well.
The current entrypoint documents Windows Python fallbacks and no external Python dependencies
for its search helper. Copying only `SKILL.md` would omit the data, scripts, and references it uses.
[Reviewed skill][uipro-skill], [MIT license][uipro-license].

Give it a concrete design brief: operational dashboard, restrained professional styling, readable
numbers, clear exception status, laptop use, and print output. Preserve the company's brand and
approved metric definitions. If an offline report is required, keep fonts and other assets local.

After installation, a useful request is:

```text
/ui-ux-pro-max
Design the presentation for our synthetic reconciliation dashboard. Prioritize a clear exception
queue, readable financial tables, and a compact laptop layout. Preserve the agreed metrics and
filter behavior. Use approved local fonts/assets, visible units, and status labels beyond color.
Show the design direction before changing files. Explain one design choice I can reuse.
```

Use the installed skill's actual directory for its Python helper. The upstream example references
`CLAUDE_PLUGIN_ROOT`; that variable is specific to plugin use and must not be assumed for a manually
copied personal skill.

## 2. Impeccable: strongest visual refinement option

Impeccable provides focused commands for reviewing and improving interfaces. For this audience,
start with `/impeccable critique`, then request the specific refinements you agree with. Its
Operate mode is relevant to dashboards where clarity and completing work matter most.
[Reviewed Claude skill][impeccable-skill], [Apache-2.0 license][impeccable-license].

The current distribution includes a launcher/engine and can download a binary on first use.
Its installer also configures hooks on supported harnesses. This is a larger installation than
one Markdown file and needs the corresponding workplace review. Do not describe it as a
dependency-free, text-only add-on. [Installation behavior][impeccable-readme].

After that installation is approved:

```text
/impeccable critique
Review this synthetic accounting dashboard in Operate mode. Focus on hierarchy, table scanning,
labels, empty states, and accessibility. Identify the three most useful improvements with evidence.
Do not change metric definitions or source data. Return findings before edits.
```

Choose one main design skill for a task. UI/UX Pro Max can establish the direction; a later
Impeccable pass can refine the result. Loading both for every minor change adds little value.

## 3. Pandas Pro: the most useful data-preparation complement

Jeffallan's skill includes reference material for cleaning, joins, aggregation, and performance.
It explicitly demonstrates merge cardinality validation and an indicator column, both useful for
finding incorrect joins. Python and pandas are required for execution.
[Reviewed skill][pandas-skill], [MIT license][jeffallan-license].

Its generic examples also include forward-filling, interpolation, median filling, and converting
numeric types. Those are examples, not suitable defaults for property-tax evidence. Missing tax
amounts must not become estimated facts; identifiers must retain their text form. Avoid precision
loss when optimizing monetary fields. Define null and rounding rules in the project first.

```text
/pandas-pro
Prepare a plan to combine approved synthetic exports at [GRAIN] using [EXACT KEYS]. Preserve
original values and source-row provenance. No interpolation, fill-forward, median filling, or
replacement of missing amounts with zero. Keep identifiers as text and amounts exact.
Validate join cardinality and show counts, source totals, and both unmatched populations.
Use a new output; do not overwrite source workbooks. Explain the most important join check.
```

## 4. SQL Pro: better extraction before Excel

Jeffallan's SQL skill addresses joins, CTEs, window functions, indexing, and query optimization.
It can help draft an extraction query without a live database connection.
[Reviewed skill][sql-skill], [MIT license][jeffallan-license].

Supply the actual database dialect and approved schema description. Keep the first use to query
drafting. An index recommendation is not permission to create one, and a query skill does not
authorize connecting or executing against production.

```text
/sql-pro
Draft a read-only [DIALECT] query from [APPROVED SCHEMA] for [PERIOD] at [ROW GRAIN].
Use explicit columns and typed parameters. Explain every join's cardinality and null treatment.
Add separate duplicate and control-total queries. Do not connect, execute, create indexes,
or modify the database. Return the query and one verification lesson for the reviewer.
```

## 5. K-Dense Polars: for a demonstrated scale problem

The focused Polars skill covers lazy queries, expressions, joins, transformations, and I/O.
Consider it when the existing pandas or Power Query workflow has a measured bottleneck. It does
not make every operation stream, eliminate memory limits, or preserve a complex Excel workbook.
[Reviewed skill][polars-skill], [collection license][kdense-license].

The entrypoint includes installation/version assumptions and optional integration extras. Verify
the approved runtime rather than copying installation commands automatically. Preserve unknown
amounts even where generic examples demonstrate null filling. The skill also includes attribution
instructions; review those before using it to produce a workplace report.

```text
/polars
Profile the approved synthetic export and propose a memory-conscious transformation. Use lazy
processing where supported. Preserve text keys, monetary precision, and missing values.
Record full-population counts and totals; distinguish full checks from samples. Explain whether
the actual joins/grouping can stream. Do not install libraries or connect to external sources.
```

## 6. K-Dense Matplotlib: polished report graphics

Use this focused plotting skill when the deliverable is a chart image for a memo, slide, or PDF.
It provides styling and export guidance. Python plotting libraries must be available, and exported
charts still need visual and numerical review. For a filterable HTML report, retain the dashboard
workflow rather than treating this as a dashboard application builder.
[Reviewed skill][matplotlib-skill], [collection license][kdense-license].

```text
/matplotlib
Create a draft bar chart from [VALIDATED SYNTHETIC SUMMARY] for a management slide. Show units,
period, and source snapshot. Use the approved palette and legible labels, with no 3-D effects.
Export new SVG and PNG files after the output plan is approved. Check bar values against the
summary and inspect label clipping. State any visual checks you could not perform.
```

## A promising Excel candidate I would not install by default

**Excel Analyst Pro** has a current skill with explicit verification and preservation boundaries.
However, its license restricts commercial use without written permission. Its current skill also
excludes native PivotTables and charts, despite broader claims in the README. That makes it a poor
default for this workplace's stated need. Evaluate it only if the license and its narrower supported
scope fit a specific task. It is not evidence that a community Excel skill can replace native Excel.
[Current skill][excel-pro-skill], [tooling limits][excel-pro-tooling], [license][excel-pro-license].

## Install one complete, reviewed component

Use the [Windows installation workflow](07-trusted-skills-and-installation.md), preserving the
working gateway and existing skills. The source links below pin the reviewed revisions.

1. Download the reviewed repository revision into a separate review folder. Inspect the selected
   skill, references, executable helpers, and license. Do not install the entire collection.
2. For Pandas Pro, SQL Pro, Polars, or Matplotlib, copy the complete selected skill folder and retain
   applicable license notices. For UI/UX Pro Max, include `data`, `scripts`, and `references` from
   its skill directory. Verify its script path for the chosen personal or project installation.
3. For Impeccable, follow a reviewed upstream distribution process that accounts for the engine,
   downloads, hooks, and supporting files. A naked `SKILL.md` copy is insufficient.
4. Review same-name collisions, show the exact destination, obtain installation approval, preserve
   a verified existing copy, and verify the completed copy. Personal scope is
   `%USERPROFILE%\.claude\skills\<skill-name>\SKILL.md`; project scope is
   `<approved-project>\.claude\skills\<skill-name>\SKILL.md`.
5. Community skills may auto-trigger. If adopting the starter's explicit-only convention, add
   `disable-model-invocation: true` in a reviewed local adaptation where its license permits;
   retain notices and record the change. Do not alter managed or signed package files in place.
6. Run one synthetic task using the exact slash name shown in Claude Code. Keep runtime installation,
   network connections, and any new automation separate from copying an instruction file.

For the first Pandas Pro trial, include duplicate keys and a missing amount. Success means a visible
exception, not a filled or dropped row. For the first design trial, include a long label, missing
metric, empty filter result, and print view. Success includes preserving the original metric totals.

No third-party code was executed, installed, or copied into this repository for this recommendation.
The assessment covers the cited entrypoints, licenses, packaging, and selected references, not an
exhaustive security audit or a measured comparison of generated outputs.

## Source revisions and maintenance evidence

The date is the reviewed repository HEAD commit date, not the last change to every selected skill.
Recent activity helps identify drift; it does not guarantee quality or future support.

| Publisher / repository | Reviewed revision | HEAD commit date (UTC) | License observed |
| --- | --- | --- | --- |
| nextlevelbuilder / ui-ux-pro-max-skill | [f3ac195][uipro-commit] | 2026-09-03 | MIT |
| pbakaus / impeccable | [46ffe5c][impeccable-commit] | 2026-09-04 | Apache-2.0 |
| Jeffallan / claude-skills | [882ef55][jeffallan-commit] | 2026-08-07 | MIT |
| K-Dense-AI / scientific-agent-skills | [1e5eeff][kdense-commit] | 2026-09-02 | MIT collection; inspect selected library/license notices |
| jeremylongshore / excel-analyst-pro-skill-md | [d812e5e][excel-pro-commit] | 2026-09-01 | Proprietary; commercial permission required |

K-Dense's earlier `claude-scientific-skills` repository URL redirects to `scientific-agent-skills`.
Its reviewed skills live under `skills/`, so older `scientific-skills/` installation paths can fail.
Use the actual files, not an aggregator's cached command. [Current tree][kdense-tree].

[uipro-skill]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/f3ac195224eac1eb0dfe1a3059c2a6add78ffbe3/.claude/skills/ui-ux-pro-max/SKILL.md
[uipro-license]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/f3ac195224eac1eb0dfe1a3059c2a6add78ffbe3/LICENSE
[uipro-commit]: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/commit/f3ac195224eac1eb0dfe1a3059c2a6add78ffbe3
[impeccable-skill]: https://github.com/pbakaus/impeccable/blob/46ffe5caa2ce5a4ca34bfe9d610a938253b151ed/.claude/skills/impeccable/SKILL.md
[impeccable-license]: https://github.com/pbakaus/impeccable/blob/46ffe5caa2ce5a4ca34bfe9d610a938253b151ed/LICENSE
[impeccable-readme]: https://github.com/pbakaus/impeccable/blob/46ffe5caa2ce5a4ca34bfe9d610a938253b151ed/README.md
[impeccable-commit]: https://github.com/pbakaus/impeccable/commit/46ffe5caa2ce5a4ca34bfe9d610a938253b151ed
[pandas-skill]: https://github.com/Jeffallan/claude-skills/blob/882ef55e377dbf9a4dbe496bb41ac6ccd0e555cf/skills/pandas-pro/SKILL.md
[sql-skill]: https://github.com/Jeffallan/claude-skills/blob/882ef55e377dbf9a4dbe496bb41ac6ccd0e555cf/skills/sql-pro/SKILL.md
[jeffallan-license]: https://github.com/Jeffallan/claude-skills/blob/882ef55e377dbf9a4dbe496bb41ac6ccd0e555cf/LICENSE
[jeffallan-commit]: https://github.com/Jeffallan/claude-skills/commit/882ef55e377dbf9a4dbe496bb41ac6ccd0e555cf
[polars-skill]: https://github.com/K-Dense-AI/scientific-agent-skills/blob/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/polars/SKILL.md
[matplotlib-skill]: https://github.com/K-Dense-AI/scientific-agent-skills/blob/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills/matplotlib/SKILL.md
[kdense-license]: https://github.com/K-Dense-AI/scientific-agent-skills/blob/1e5eeffbdad3749125afe7ab48a39694e27f181c/LICENSE.md
[kdense-commit]: https://github.com/K-Dense-AI/scientific-agent-skills/commit/1e5eeffbdad3749125afe7ab48a39694e27f181c
[kdense-tree]: https://github.com/K-Dense-AI/scientific-agent-skills/tree/1e5eeffbdad3749125afe7ab48a39694e27f181c/skills
[excel-pro-skill]: https://github.com/jeremylongshore/excel-analyst-pro-skill-md/blob/d812e5e4af267439c435cced93ed319353db2de6/skills/excel-analyst-pro/SKILL.md
[excel-pro-tooling]: https://github.com/jeremylongshore/excel-analyst-pro-skill-md/blob/d812e5e4af267439c435cced93ed319353db2de6/skills/excel-analyst-pro/references/tooling.md
[excel-pro-license]: https://github.com/jeremylongshore/excel-analyst-pro-skill-md/blob/d812e5e4af267439c435cced93ed319353db2de6/LICENSE
[excel-pro-commit]: https://github.com/jeremylongshore/excel-analyst-pro-skill-md/commit/d812e5e4af267439c435cced93ed319353db2de6
