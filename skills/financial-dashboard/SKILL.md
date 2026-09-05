---
name: financial-dashboard
description: Build a professional accounting dashboard from approved validated data, with defined metrics, consistent filters, visible exceptions, and source-to-display checks.
disable-model-invocation: true
---

# Financial dashboard

Run when explicitly invoked with `/financial-dashboard`. Work within the user's approved task,
inputs, runtime, and output location. Propose the metric definitions and output before writing;
use the project's approval process. Do not connect to databases, install dependencies, publish,
send, or upload without separate authorization. Never put work records into this public starter.

## Define the report

Clarify the audience and decision. Reuse supplied details and ask one question at a time for
material gaps. Establish row grain, unique keys, period, currency, source date, and refresh status.
Define every KPI's numerator, denominator, exclusions, aggregation, and filter behavior. Missing
values remain unknown; no-data is not a successful reconciliation. Distinguish tax assessed,
book expense, liability, payments, and estimates. Do not combine different grains or currencies.

Check source counts, duplicates, join cardinality, and totals before design. Keep input exceptions
visible. If data is missing, offer a clearly labeled synthetic mockup rather than invented results.
If data is unvalidated, label the dashboard draft and report failed checks.

## Build and teach

Choose the simplest approved format that the audience can use: Excel/PivotTables for workpapers,
local HTML for an interactive snapshot, or the organization's BI platform for governed sharing.
Use the existing stack and brand standards when supplied.

For HTML, prefer local assets or native SVG, system fonts, readable tables, and a restrained palette.
Use a clear title, reporting scope, three or four purposeful metrics, useful comparisons, and an
exception table. Use bars for categories, lines for time, and a waterfall for a proved variance
bridge. Use a pie/donut only for a small, nonnegative, mutually exclusive composition with a known
whole. Include labels and a table alternative; never communicate status through color alone.

All relevant controls must update metrics, charts, and detail together. Show active filters, reset,
empty states, missing values, units, source freshness, and print behavior. A filter is not access
control. Hidden or embedded records remain part of the file. Do not embed credentials. Escape
untrusted labels; never insert source strings as executable HTML. Avoid external scripts, fonts,
analytics, or live APIs unless explicitly approved.

## Verify before delivery

- Independently total the approved source and compare it with every KPI and chart population.
- Exercise each filter alone and in combination, reset, an empty selection, missing data, and
  offsetting positive/negative differences. Show gross exceptions as well as net variance.
- Check responsive layouts, keyboard controls, label readability, scrolling, print, and console
  errors in a real browser when available. Report any browser checks not performed.
- If offline use is required, test it without network access. A CDN dependency fails that claim.
- Reopen the deliverable and document input version, transformation, checks, and refresh method.

Return the artifact location, checks with evidence, limitations, and one short lesson showing how
the user can trace a displayed number to its inputs. Human review decides accounting acceptance.
