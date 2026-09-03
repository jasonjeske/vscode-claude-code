# Models, thinking effort, and workplace usage

A workplace Team or Enterprise account may be limited, metered, centrally configured, or changed by
an administrator. Availability and limits vary. This guide states no fixed entitlement, price, or
token allowance.

Official references:

- [Model configuration](https://code.claude.com/docs/en/model-config)
- [Manage costs](https://code.claude.com/docs/en/costs)
- [Claude Code commands](https://code.claude.com/docs/en/commands)

## Verify the account before sensitive work

Run `/status`. Confirm on screen that the provider and account or tenant are employer-approved. Do
not paste, screenshot, or repeat account identifiers in chat or public logs. Stop if anything is
wrong or uncertain.

Model and effort choices are not data classification, privacy boundaries, or safety controls.
Approval to use a model does not imply approval to process a particular data class.

## Choose the model visibly

- **Haiku, if available:** low-risk formatting, classification, and draft wording. Do not use speed
  to bypass difficult reconciliation logic or professional review.
- **Sonnet or workplace default:** daily analysis, controlled drafting, document explanation, and
  routine workflows. Verify sources, controls, and exceptions.
- **Opus, if available:** difficult method design, ambiguous multi-source reasoning, or a demanding
  independent challenge. A human still owns tax, legal, and accounting decisions.
- **Fable, if available:** the hardest, longest, or most ambiguous work. The `fable` alias may
  resolve to a newer Fable version, so use the picker rather than assuming Fable 5.
- **Other allowed models:** select only from the current `/model` picker. Do not assume a model
  name, version, entitlement, or alias from a public example.

Claude Code documents `opusplan` as a scoped alias that uses Opus while planning and Sonnet while
executing when those models are available. It is not a general classifier for job tasks, risk, or
data sensitivity.

## Choose thinking effort separately

Run `/effort` to inspect levels supported by the current model and account. Depending on the model,
Claude Code may offer `low`, `medium`, `high`, `xhigh`, or `max`.

| Effort | Starting use |
| --- | --- |
| `low` | Quick, low-risk wording or simple formatting. |
| `medium` | Repetitive, well-defined routine work. |
| `high` | Substantive knowledge work and reconciliation planning. |
| `xhigh` | Complex multi-step or high-consequence planning, when supported. |
| `max` | Rare capability-critical work; may consume more and overthink. |

Haiku is not universally effort-capable. The picker and current account are authoritative.

Effort is soft guidance to the model, not a hard token cap, fixed budget, or correctness guarantee.
Adaptive thinking is distinct: a capable model may vary its reasoning within the chosen effort
guidance. Start at `high` for substantive professional work. Lower effort only for genuinely simple
or repetitive tasks. Use `xhigh` selectively and `max` rarely.

Never reduce evidence, controls, exceptions, or review merely to lower effort or usage.

## No general automatic router

This repository configures no model router. Choose visibly with `/model` and `/effort`, then confirm
the active choice before consequential analysis. Model choice never replaces authoritative sources,
control totals, exception queues, reproducible evidence, or human approval.

## Seven commands to learn

1. `/status` — verify the active provider and approved workplace account.
2. `/permissions` — inspect the allowed action boundary.
3. `/model` — inspect or choose an allowed model or documented alias.
4. `/effort` — inspect or choose available thinking effort.
5. `/usage` — inspect usage information exposed for the account.
6. `/context` — see what consumes the context window.
7. `/clear` — remove stale context before an unrelated objective.

Do not reproduce account identifiers from command output. Behavior can change; use Anthropic's
current [command reference](https://code.claude.com/docs/en/commands).

## Keep a limited allowance productive

1. Start with outcome, period, inputs, source hierarchy, rules, controls, deliverables, exceptions,
   and approval boundary.
2. Open only the smallest sufficient set of approved files. Never scan a drive or broad folder.
3. Use one conversation for one related objective.
4. Ask for a short plan and approve it before large analysis.
5. Request concise status focused on decisions, exceptions, and checks.
6. Reuse approved project instructions instead of repeating stable rules.
7. Check `/usage` before a long task and `/context` before adding files.
8. Stop at a clear, redacted handoff if safe completion exceeds remaining usage.

## No subagents or autonomous workflows in the starter

A **job workflow** is the human end-to-end process. A **skill** is one invoked instruction for a
bounded repeated task. A **subagent** is a separate Claude instance with its own context and usage.
They are not interchangeable.

This starter does not install, teach, or invoke subagents, agent teams, or long autonomous
workflows. Separate instances can multiply context and usage, obscure decisions, and exhaust a
limited allowance. Check `/usage` and decline beginner offers to “spawn subagents,” “keep going,” or
“build the full workflow.”

Consider a subagent only after all of these are true:

- the user understands prompts, permissions, context, model, effort, and verification;
- at least one week of controlled single-session synthetic practice is complete;
- the user understands normal usage consumption and remaining allowance;
- the employer owns and approves the cost and data-processing boundary; and
- a genuine independent review need cannot be met by a fresh, bounded human-reviewed session.

Even then, define scope, input, output, budget, stop conditions, and review before use. Never add a
subagent merely because it sounds advanced.
