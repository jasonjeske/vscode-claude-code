# Skill catalog: what to use, why, and the first prompt

Start with the next real task, then install only the skill needed for it. A skill is reusable
instructions, not a new model or an automatic grant of tool access. Claude Code's VS Code extension
can discover local skills in its supported locations; some upstream packages also need runtimes.

**Install:** [local copies and upstream packages](setup/SKILLS.md).
**Learn:** [daily use](guides/DAILY-USE.md). **More prompts:** [library](prompts/PROMPT-LIBRARY.md).

| When | Suggested choice |
| --- | --- |
| First setup | `prompt-coach`, `excel-workbook-review` |
| First tax-law question | `property-tax-research` |
| First workbook creation/edit | Reviewed Anthropic `xlsx`, with suitable runtime and Excel validation |
| First reconciliation review | `reconciliation-control-review` |
| First dashboard | `financial-dashboard`; one design skill if needed |
| Later recurring work | A specific data, document, or memory skill justified by the task |

## Seven skills included in this download

These are original local skills. Copy the complete selected folder from `skills/`. Invoke by its
slash command; none runs automatically. Use approved synthetic input for the first trial.

### 1. Prompt coach

**Does:** turns a rough request into a concise reusable prompt and teaches one prompting habit.
**Use when:** you know the task but not how to ask. It drafts text; it does not execute the task.
[Read the skill](skills/prompt-coach/SKILL.md).

```text
/prompt-coach
Help me ask for a read-only review of a synthetic workbook. I need a sheet map, formula risks,
and one verification lesson. Ask only for material missing details; do not perform the review.
```

### 2. Excel workbook review

**Does:** maps workbook structure, formulas, hidden features, data risks, and preservation needs.
**Use when:** opening an unfamiliar or complex workbook before edits. It does not save, recalculate,
refresh, run macros, or control the Excel application. [Read the skill](skills/excel-workbook-review/SKILL.md).

```text
/excel-workbook-review
Guided mode. Review only the approved synthetic workbook I selected. Map the sheets and tables,
identify formula/cache and PivotTable risks, and recommend a processing route. Do not save or
refresh anything. Mark features the available tools cannot inspect as UNVERIFIED.
```

### 3. Property-tax research

**Does:** investigates specific state/local rules with pinpoint citations, tax-year applicability,
historical versions, exceptions, and open questions. **Use when:** researching a requirement,
exemption, deadline, or change. Requires approved web access or supplied sources; it does not decide
a filing position. [Read the skill](skills/property-tax-research/SKILL.md) and [guide](guides/12-property-tax-research.md).

```text
/property-tax-research
Guided mode. Research [SPECIFIC REQUIREMENT] for [PROPERTY TYPE] in [STATE/LOCALITY] for [TAX YEAR].
Use approved official sources. Explain the rule and exceptions with exact citations, effective
periods, and missing facts. Return a short research memo for review, not a final filing decision.
```

### 4. Reconciliation control review

**Does:** checks an existing comparison against counts, totals, keys, exceptions, and reproducibility.
**Use when:** reviewing a prepared reconciliation before sign-off. Returns PASS/FAIL/UNVERIFIED;
it does not edit or repair records. [Read the skill](skills/reconciliation-control-review/SKILL.md).

```text
/reconciliation-control-review
Review the approved synthetic comparison using the supplied exact keys, control totals, and
zero tolerance. Read-only. Check duplicate/unmatched populations, gross and net differences,
and reproducibility. Preserve all missing evidence as UNVERIFIED. Use the fixed review format.
```

### 5. Financial dashboard

**Does:** builds a scoped dashboard/report with defined metrics, readable charts, and validation.
**Use when:** turning approved reconciled data into management reporting. It needs an agreed output
format and suitable tools; publication is separate. [Read the skill](skills/financial-dashboard/SKILL.md).

```text
/financial-dashboard
Build a local HTML dashboard from our approved synthetic summary in the selected practice folder.
Show totals, gross/net differences, missing amounts, and state/period filters. Use local assets,
clear units, and accessible status labels. Agree metric definitions before building, then verify
chart/table totals and empty states. Do not publish it.
```

### 6. Structured work request

**Does:** creates a fuller ten-part scope with rules, controls, deliverables, and approval boundaries.
**Use when:** a complex assignment needs requirements clarified. Use Prompt Coach for small tasks;
do not run both by default. [Read the skill](skills/structured-work-request/SKILL.md).

```text
/structured-work-request
Help me define a multistate fixed-asset reconciliation for PERIOD-1. The permitted inputs are
approved copies of EXPORT-A and MASTER-A. Produce a reviewable scope and ask one missing question
at a time. Do not open files or execute the reconciliation.
```

### 7. Work memory

**Does:** maintains small, explicitly approved, redacted cross-project notes. **Use when:** a recurring
generic lesson is worth remembering. It is optional and separate from native Claude auto memory;
it is not a storage location for records, values, or tax authority. [Read the skill](skills/work-memory/SKILL.md)
and [setup/commands](docs/WORK-MEMORY.md).

```text
/work-memory status
```

After storage is approved and initialization completed using the blank memory templates:

```text
/work-memory remember join-controls
Propose a generic note: define row grain and test key uniqueness before joining exports.
Keep company details and data out. Show the note for approval before writing it.
```

## Official upstream skills

**Not included in the download.** Review [sources, licenses, and runtimes](guides/07-trusted-skills-and-installation.md)
and use [the installation route](setup/SKILLS.md#upstream-skills-and-plugins). These are fit-based
recommendations, not workplace-tested integrations. Office skills have specific restrictive terms.

For directly invocable skills, select the actual installed command from `/`, which may be
namespaced (for example, `/document-skills:xlsx`). Then paste the example text. The four entries
labeled **supporting skill** are hidden from the slash menu upstream: ask Claude to use their
guidance in a normal request when the reviewed package is installed. Replace placeholders with approved input
references; the examples do not themselves authorize connections or installations.

| Skill | What it does / when to use it | Quick example after selecting the skill |
| --- | --- | --- |
| [xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) | Create/edit ordinary workbooks, formulas, tables, formatting | Create a new workbook from the invented practice tables with source, comparison, exceptions, and controls sheets. Preserve text keys and verify totals in native Excel. |
| [pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) | Read notices and organize page-based evidence | Extract the stated dates and assessment fields from the approved synthetic notice. Cite each page and mark unreadable fields unknown. |
| [docx](https://github.com/anthropics/skills/tree/main/skills/docx) | Create reviewer memos and structured Word documents | Turn the approved synthetic findings into a two-page memo with sources, exceptions, and reviewer questions. Verify the rendered layout. |
| [pptx](https://github.com/anthropics/skills/tree/main/skills/pptx) | Create management presentations | Build five slides from the approved summary: scope, key figures, differences, open items, next steps. Preserve units and source dates; inspect for clipping. |
| [Finance reconciliation](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance/skills/reconciliation) | Organize comparisons and reconciling items | Compare approved BOOK-A and DETAIL-A at the stated grain. Explain supported differences and keep unresolved items separate. Do not force a tie. |
| [Finance variance-analysis](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance/skills/variance-analysis) | Explain changes between periods | Bridge the two approved period totals. Separate documented drivers from hypotheses and tie the bridge back to the source totals. |
| [Data explore-data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/explore-data) | Profile unfamiliar tabular data | Profile only the approved export: schema, types, nulls, key uniqueness, period coverage, and source totals. Distinguish samples from full checks. |
| [Data validate-data](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/validate-data) | Check analytical results and assumptions | Review this synthetic analysis for duplicate joins, denominator errors, missing amounts, source freshness, and unsupported claims. |
| [Data build-dashboard](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/build-dashboard) | Build filterable analytical reporting | Build the agreed synthetic report with exception filters and a source/as-of note. Use local assets for offline use and test each filter against control totals. |
| [Data data-visualization](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/data-visualization) | **Supporting skill.** Choose and refine charts | Choose charts for jurisdiction totals and open-item aging. Explain denominators and avoid a pie chart when categories overlap. |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Improve dashboard layout, typography, and interaction | Give this synthetic dashboard a restrained professional design with readable tables and laptop-friendly filters. Preserve its metric definitions. |
| [Financial Services audit-xls](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/audit-xls) | Additional formula/model audit guidance | Review the approved workbook copy for inconsistent formulas, broken references, hardcoded overrides, and unit errors. Do not change it. |
| [Data write-query](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/write-query) | Draft a query for a defined question | Draft read-only SQL in [DIALECT] from the approved schema for [PERIOD]. Use explicit columns and typed parameters. Do not connect or execute. |
| [Data sql-queries](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/sql-queries) | **Supporting skill.** Apply SQL patterns and dialect-specific checks | Review the drafted query's join cardinality, date boundaries, null treatment, and duplicate checks before execution approval. |

Use the local `financial-dashboard` as the business/verification brief or the upstream dashboard
skill as the implementation workflow. Avoid loading every dashboard and design skill for one small
edit. A data-frame pivot summary is not a native Excel PivotTable with slicers and a refreshable cache.

### Later official additions

Use these only after a recurring task justifies the extra instructions. The same source/runtime
review and installed-menu selection apply.

| Skill and source | Purpose | First example |
| --- | --- | --- |
| [Finance close-management](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance/skills/close-management) | **Supporting skill.** Close task ownership and dependencies | Draft a close checklist from the approved procedure with owners, dependencies, and evidence; do not mark unverified tasks complete. |
| [Finance audit-support](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance/skills/audit-support) | **Supporting skill.** Organize reviewer evidence | Map each requested control to an approved evidence reference and flag gaps without inventing support. |
| [doc-coauthoring](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | Draft and refine repeatable documentation | Help document the established monthly procedure for a new reviewer; ask only for missing steps. |
| [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Develop and evaluate a recurring task skill | Draft a narrow instruction-only skill from this approved generic procedure and propose synthetic acceptance cases. Do not install or run an agent-based evaluation automatically. |
| [clean-data-xls](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls) | Spreadsheet cleaning after types/rules are agreed | Propose normalization on an approved copy; preserve source values, text identifiers, and unknown amounts. |
| [xlsx-author](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/xlsx-author) | A narrower workbook-generation candidate | Create a plain synthetic workbook with the agreed layout and checks; identify unsupported Excel features before writing. |

The Financial Services candidates do not justify installing its whole investment/agent stack.

## Six community recommendations

These are also **not bundled**. [Guide 11](guides/11-community-skills-worth-adding.md) records the
reviewed revisions, licenses, complete-folder requirements, runtime assumptions, and longer prompts.
Use the menu's actual command and review the complete package before installation.

| Skill / source | What it adds | Quick example |
| --- | --- | --- |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Dashboard design direction and chart/layout guidance | `/ui-ux-pro-max` Design an accounting dashboard for laptop use with clear exception rows, financial tables, local assets, and consistent units. Show the design before edits. |
| [Impeccable](https://github.com/pbakaus/impeccable) | Focused critique and visual refinement; includes executable tooling | `/impeccable critique` Review the synthetic dashboard in Operate mode. Identify three improvements to hierarchy, labels, accessibility, or empty states; preserve metrics. |
| [Pandas Pro](https://github.com/Jeffallan/claude-skills/tree/main/skills/pandas-pro) | Repeated joins, grouping, reshaping, and diagnostics | `/pandas-pro` Plan the exact-key join of approved exports. Preserve text IDs and exact amounts. Validate cardinality and both unmatched sides; do not impute missing evidence. |
| [SQL Pro](https://github.com/Jeffallan/claude-skills/tree/main/skills/sql-pro) | Query drafting and database-specific analysis | `/sql-pro` Draft a read-only [DIALECT] query from the approved schema, with duplicate and control-total checks. Do not connect, execute, or create indexes. |
| [K-Dense Polars](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/polars) | Larger table processing when a bottleneck is measured | `/polars` Propose a memory-conscious transformation for the approved export, retaining row provenance, exact amounts, null meaning, and source totals. |
| [K-Dense Matplotlib](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/matplotlib) | Consistent exported charts for reports and slides | `/matplotlib` Create a printable chart from the approved synthetic summary with clear units, source date, readable labels, and no invented values. |

For Excel, keep the native-workbook validation route even when pandas or Polars handles the data.
Generic library examples of interpolation, filling nulls, or converting numeric-looking IDs are not
approved tax-data rules.

## Considered, but not a default installation

- **Caveman:** try the concise professional instructions already in the global template first.
  Optional `lite` evaluation and honest measurement are described in the
  [token guide](guides/13-token-efficient-work.md). No compression proxy is part of this kit.
- **Excel Analyst Pro:** licensing and current capability limits prevent a default recommendation.
  See the [source review](guides/11-community-skills-worth-adding.md).
- **Agent teams, broad connector bundles, and automatic routers:** advanced organizational choices,
  not part of the beginner path. More installed features do not automatically improve results.

The catalog has no automatic installer. Record actual installations and tests in the
[local setup receipt](templates/SETUP-RECEIPT.md).
