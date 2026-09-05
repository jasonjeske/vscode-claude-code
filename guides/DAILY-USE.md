# The daily desk guide

Set up once using [START-HERE](../START-HERE.md). For daily work, open the approved work project
in VS Code, not the public starter. Keep this page available as a reference; there is no need to
ask Claude to read it at the start of every conversation.

## Learn one operation while doing the work

Choose [today's useful result](../LEARN.md), rather than asking Claude to teach the whole tool.
For something new: see one example if needed, get the bounded work result, and check one source
or calculation yourself. On the next similar task, try the request and check before consulting
your saved prompt. Use Routine when you can do that; keep Guided for unfamiliar parts.

Keep a [short local task note](../templates/WORK-TASK-NOTE.md) if useful. No extra quiz chat is
required. Useful output, fewer corrections, and the ability to catch a changed condition are
better progress signals than the number of lessons or skills completed.

## Reopen the project and saved request

In VS Code choose **File > Open Recent** and select the intended project. Use **Ctrl+P** to find
`prompts/current-task.md`, edit or dictate the next bounded request, then **Ctrl+S**. Open the
Claude Code panel and select that exact file with `@`; explicitly ask it to read the saved version
and perform the allowed task. Select each approved evidence file too. Start fresh for unrelated work.
Your six personal skills stay installed. [Saved-request examples](14-prompt-files-and-dictation.md).

## Start with one outcome

Confirm the intended approved workspace/provider, choose the task, and reference only its inputs.
Keep the approved model default unless a specific task calls for a change. Check the organization's
usage website before a large task. Select **Guided** for something new or **Routine** for an
established procedure. Send one prompt at a time; use [the interface guide](00-use-vscode.md) for
waiting, partial results, usage, and a terminal exception.

```text
Guided mode. For [PERIOD], use only [APPROVED INPUTS] to produce [ONE RESULT].
Preserve originals and follow [RULES]. Show [CONTROL TOTALS / CITATIONS / CHECKS].
Put detailed output in [APPROVED NEW OUTPUT]. Ask only for material missing information.
```

The [prompt library](../prompts/PROMPT-LIBRARY.md) has more detailed variants. If you do not know
how to ask, use `/property-tax-workbench:prompt-coach`. If the assignment has many unresolved requirements, use
`/property-tax-workbench:structured-work-request` instead. You do not need both for the same straightforward task.

## Choose the tool by the job

| Today's task | Start with | Review before using the result |
| --- | --- | --- |
| Understand an unfamiliar workbook | `/property-tax-workbench:excel-workbook-review` | Sheet map, formulas/caches, hidden features, preservation limits |
| Create or edit a workbook | Approved Anthropic `xlsx` | Open a copy in Excel; check calculations, links, features, totals |
| Compare exports or books to bills | Reconciliation prompt, then `/property-tax-workbench:reconciliation-control-review` | Keys, duplicates, missing records, gross/net differences, source totals |
| Research a state/local requirement | `/property-tax-workbench:property-tax-research` | Exact provision, tax year, locality, exceptions, missing facts |
| Create a management dashboard | `/property-tax-workbench:financial-dashboard` | Metric definitions, source/as-of date, filters, chart/table totals |
| Improve a dashboard's appearance | One approved design skill | Readability, accessibility, and unchanged metric meaning |
| Draft a memo or slide deck | Approved `docx` or `pptx` | Source-backed claims and actual Word/PowerPoint rendering |

See [the catalog](../SKILLS.md) for full examples and upstream command names. The local review
skills inspect and report; they do not perform reconciliation edits or create a workbook by themselves.

## Make corrections specific

```text
The match must include jurisdiction and tax year, not just property ID. Keep the original inputs.
Revise the proposed key, identify which prior matches are affected, and rerun the control totals.
```

```text
The amount is unknown, not zero. Preserve that distinction in the table, chart, and denominator.
Show the affected results and checks.
```

```text
Explain why this citation applies to the requested tax year. If the historical version has not
been checked, mark that conclusion unresolved and identify the next source needed.
```

Specific corrections teach a reusable rule without reopening every unrelated part of the task.
When a tool fails, share only the approved relevant error. Do not paste connection strings or keys.

## Stop at a useful checkpoint

Check the source evidence and the result before relying on it. A plausible explanation, polished
chart, or lack of formula errors does not establish correctness.

```text
Summarize the completed result, inputs/versions, checks actually performed, remaining exceptions,
and next action. Keep it concise and use neutral labels. Do not change memory or instructions.
```

For the same objective, continue with the necessary evidence. For unrelated work, start a fresh
conversation or use `/clear` where available. Preserve the handoff first if needed. Clearing context
does not refund prior usage, and memory does not replace the original evidence.

## When something is unavailable

| Problem | Useful next step |
| --- | --- |
| Skill missing | [Check scope, folder, and command](../setup/SKILLS.md#troubleshooting) |
| No Excel library/engine | Request a read-only map or processing plan; route the precise runtime need to IT |
| No browsing | Supply approved official sources and keep currentness/applicability gaps visible |
| No database connection | Draft SQL from an approved schema or use approved exports |
| Low remaining allowance | Finish a bounded checkpoint; narrow the next task rather than omitting controls |
| Conflicting instructions | Preserve existing policy; resolve the affected conflict before its action |

Progress to [the work-based progression](10-four-week-learning-path.md) when the first exercise
and its checks are comfortable.
