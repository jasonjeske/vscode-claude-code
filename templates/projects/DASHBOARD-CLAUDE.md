# Dashboard and reporting project

Copy or merge into an approved project's `CLAUDE.md`. Complete locally; never publish filled facts.

## Purpose and sources

- Audience and decision: [REVIEWER / QUESTION THE REPORT ANSWERS]
- Period and scope: [PERIOD / JURISDICTIONS / POPULATION]
- Approved input versions and refresh/as-of time: [REFERENCES]
- Row grain and keys: [ONE ROW REPRESENTS / EXACT KEYS]
- Currency, units, signs, and rounding: [RULES]
- Output format/location: [EXCEL / LOCAL HTML / APPROVED BI / STATIC REPORT]
- Publishing or distribution: [SEPARATE APPROVAL / NONE]

## Metric dictionary

| Metric | Calculation | Included population / denominator | Null/zero behavior | Source / check |
| --- | --- | --- | --- | --- |
| [METRIC] | [FORMULA] | [SCOPE] | [RULE] | [REFERENCE] |

Define metrics before layout. Keep missing amounts distinct from zero. Show gross and net differences
when reconciling; equal amounts do not mean review approval. Preserve exception populations.
Every chart, total, filter, and table must use the same definitions and scoped source rows.

## Presentation and verification

Use `/financial-dashboard` when installed. Choose one design skill only when it adds useful guidance.
Use readable financial tables, consistent decimals, clear units and dates, restrained color, explicit
status labels, and accessible filters. Display empty and partially missing states honestly.
External assets/network behavior: [APPROVED LOCAL ASSETS / SPECIFIC APPROVED DEPENDENCIES].

Check source totals, filters separately and together, no-data states, keyboard navigation, narrow
layout, and print/export when applicable. Tie outputs to an independent control calculation.
Do not claim visual/browser/native-Excel checks that were not performed. Record UNVERIFIED limits.
Keep real data out of public demos, screenshots, and repositories; HTML may embed the full dataset.

Done means a useful report, metric dictionary, source/as-of notes, verified checks, remaining
exceptions, and human review. Default Guided mode: explain one chart or control choice.
