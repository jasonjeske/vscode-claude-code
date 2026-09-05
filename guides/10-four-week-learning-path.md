# Guide 10: Learn while doing useful work

Start here if Claude Code already works in VS Code. Keep the working gateway configuration and
read only the next relevant guide. The weeks below are suggested pacing; advance when the checks
are comfortable, not because a date arrives.

## Week 1: Understand and ask

Use one short session each day, roughly 15-25 minutes. Begin with invented examples, then a small
approved work copy when permitted.

1. Review [global instructions](../templates/GLOBAL-CLAUDE.md) and merge them through the existing
   quick-start procedure. Do not replace company instructions or copy credentials.
2. Use `/prompt-coach` to describe one outcome. Notice how naming the output and proof improves it.
3. Ask for a workbook map without edits. Learn sheet, table, formula, cached value, and row grain.
4. Explain one formula and work through a tiny example by hand.
5. Review a proposed change and practice saying what is wrong or incomplete.

**Advance when:** you can explain which files Claude read, what it changed, and how you checked it.

## Week 2: Reconcile a small population

Choose one comparison, one period, and an approved exact key. Use the
[reconciliation project template](../templates/projects/RECONCILIATION-CLAUDE.md). Inventory first;
then approve a small transformation to new output files. Review duplicates, unmatched records,
net and gross differences, and source totals. Use `/reconciliation-control-review` to check evidence.

**Advance when:** every input record is accounted for and you can explain an exception without
guessing. Review the Excel runtime and skill installation only when this work needs them.

## Week 3: Turn checked results into a dashboard

Try the synthetic demo in [Guide 09](09-dashboard-and-reporting-playbook.md), then define one real
report's audience and metric dictionary. Ask for a wireframe first, approve it, then create a new
local report from the approved summary. Test filters, missing values, empty results, and print.
Draft a short management explanation from the same numbers.

**Advance when:** you can trace every figure to its source and explain what the dashboard cannot show.

For additional design help, try UI/UX Pro Max from the
[community shortlist](11-community-skills-worth-adding.md). Save deeper Impeccable refinement for
an approved installation and a specific visual problem.

## Week 4: Make one recurring task repeatable

Pick a stable task, such as combining the same approved exports each month. Record the schema,
inputs, output, match rules, and checks. Ask for a small reproducible script or Power Query plan.
Test on the same data twice, on a changed schema, and on missing/duplicate records. Keep the manual
fallback. An automation that saves time but loses records has failed.

Add Word, PowerPoint, SQL, or a source-research workflow only when there is a concrete task for it.
For specific state/local law questions, add [`property-tax-research`](12-property-tax-research.md)
and practice checking one cited provision before expanding to a multistate comparison.
Database access remains a separate organizational decision. A skill can help draft SQL without a
connection. Do not schedule unattended jobs until the workflow is owned, tested, and approved.

**Advance when:** another reviewer can reproduce the result using your instructions and identify
the exact conditions where the workflow stops.

Pandas Pro and SQL Pro are useful community additions at this stage. Evaluate Polars only when a
measured bottleneck warrants a different processing tool. Guide 11 includes scoped trial prompts.

## A daily routine

Start one conversation per related task. State the result, approved inputs, and success checks.
Use `Teach` mode for new concepts, `Guided` for unfamiliar work, and `Routine` for a known approved
method. See [the learning/work instructions](../templates/LEARNING-AND-WORK.md). Ask for a brief
summary of checks and one next action at the end. A checkpoint should record method and status,
not raw work data.

## Measure improvement honestly

Privately record the task type, hands-on time, total elapsed time, review time, corrections, missing
records, failed controls, and whether another person reproduced it. Compare similar tasks over
several runs before claiming savings. Include the time spent checking Claude's output. Do not
reward speed when quality worsens, and do not put employer results into this repository.

## A useful first prompt

```text
I am learning Claude Code and want to understand one synthetic workbook. Teach mode.
Use only the file I select. Start with a read-only map of its sheets, tables, and formulas.
Explain one unfamiliar term briefly. Identify what your tools cannot inspect.
Do not save, refresh, run macros, or change the file. Give me one check I can do myself.
```
