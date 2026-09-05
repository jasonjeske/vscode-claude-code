# Save tokens while keeping the work useful

Use concise, professional answers, narrow inputs, and the right model/effort for the task. Keep
citations, uncertainty, exceptions, control totals, and verification. The goal is a correct result
with fewer unnecessary reads and retries, not the shortest possible answer.

The [global template](../templates/GLOBAL-CLAUDE.md) already includes this behavior. No additional
token-saving skill or proxy is required. This guide is based on sources reviewed September 5, 2026
(UTC); actual savings in a managed gateway have not been measured here.

## Where usage comes from

Claude processes instructions, conversation history, supplied files, and tool results as input.
It also generates output and may use reasoning tokens. Caching changes how repeated inputs are
priced; the employer's gateway may use its own allocation and reporting rules. A smaller answer
does not necessarily mean a proportionally smaller bill or allowance deduction.

Use `/usage` for available session statistics and `/context` to inspect context composition.
Claude's dollar display is an estimate; the approved gateway/admin report determines the actual
workplace allocation. Record usage before clearing a session if you need a comparison. Current
Claude versions reset the displayed session total with `/clear`; that does not refund consumption.
[Anthropic cost and context guidance](https://code.claude.com/docs/en/costs).

## The practical habits

1. **Name one outcome.** Specify the period, files, relevant sheets/columns, rules, and output.
2. **Process data with suitable tools.** For big tables, ask approved scripts/queries to compute
   full-population controls and exception files. Inspect a bounded summary in chat. A sample is
   useful for designing a method, not for claiming the entire population reconciles.
3. **Keep related work together.** Start fresh for unrelated tasks. For long continuing work, use
   a short handoff or supported compaction that retains rules, evidence references, and unresolved
   items. Do not repeatedly clear and reload the same sources without a reason.
4. **Choose a suitable allowed model and effort.** Routine formatting needs less reasoning than
   an ambiguous multi-source reconciliation. Preserve substantive checks whichever model is used.
5. **Read one relevant skill.** Keep global instructions short and detailed procedures in invoked
   skills. Do not ask Claude to read this entire repository every morning.
6. **Stop when the result meets its checks.** Avoid repeated rewrites or extra design passes with
   no specific improvement to make. Keep subagents and long autonomous runs out of the beginner path.

Anthropic documents context management, model selection, on-demand skills, and effort as cost
controls. These are directions to evaluate, not fixed saving percentages.
[Official guidance](https://code.claude.com/docs/en/costs),
[skill loading behavior](https://code.claude.com/docs/en/skills).

## A reusable efficient-work prompt

```text
Routine mode. Produce [ONE RESULT] from [APPROVED INPUTS] for [PERIOD].
Use the smallest sufficient context. Do not scan unrelated folders or print complete datasets.
Use approved local processing for full-population counts, totals, and exceptions.
Keep the answer concise, with sources, checks, uncertainty, and the next action.
Do not start subagents or install tools. If scope needs to expand, explain why first.
```

For a new task, replace Routine with Guided and add: `Explain one concept that helps me verify it.`
Extra words that prevent a misunderstanding can save a correction round.

## Caveman: optional experiment, not the default

This review concerns [JuliusBrussee/Caveman](https://github.com/JuliusBrussee/caveman). A workplace
copy may be a different revision or fork. The original skill compresses conversational output;
the current project also offers a separate proxy and broader tooling. Those are distinct choices.

Its output-saving headline comes from coding-prompt benchmarks, not this tax workflow. The
maintainer's accounting notes acknowledge instruction overhead and possible negative savings for
already-short tasks. The percentage does not establish total input/output/reasoning cost savings.
[Maintainer's measurement notes](https://github.com/JuliusBrussee/caveman/blob/main/docs/HONEST-NUMBERS.md).

The inspected skill defaults to fragmented prose, suppresses routine progress narration, and
removes hedging, while preserving negations and providing ambiguity safeguards. For a beginner
working with conditional legal rules and complex formulas, this is a poor default tradeoff.
`lite` retains complete sentences and is the better mode to evaluate if concise style is desired.
[Skill instructions](https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md).

We recommend the small professional-style instructions already in the global template. Caveman,
its proxy, hooks, compression tools, and agent presets are not installed by this kit. A managed
gateway should not be changed to pursue an unmeasured saving.

If a reviewed skill-only copy is already approved, compare it on a few invented tasks:

- Same model, effort, inputs, deliverable, and initial instructions in fresh sessions.
- Compare the concise-template baseline with Caveman lite; record input/cache/output metrics
  actually exposed and note different cache states rather than pretending they are equivalent.
- Include clarification and correction turns. Check citations, caveats, numeric accuracy, and
  the user's ability to follow the answer. Use repeated trials if results are close.
- Keep it only if it improves total usage and usability. Do not infer a general percentage from
  a handful of tasks. This kit has not run that benchmark or the Caveman installer.

## Optional visibility, later

The [status-line guide](06-budget-aware-statusline.md) can show available session metrics after
the basic setup works. Its display is not a hard spend cap. Administrator/gateway limits remain
the place to enforce the allocation. Do not configure a guessed monthly budget as a real balance.
