# Improve one established process at a time

Once the first tasks feel comfortable, focus on repeatability, better evidence, and faster review.
Use [the four-week path](10-four-week-learning-path.md) for a sequence or choose a concrete recurring
problem from the [skill catalog](../SKILLS.md).

## Ready for the next step

You can describe the input, period, exact output, and verification check; recognize an unexpected
file change; explain a failed control; and see how much usage a typical task consumes. You know how
to preserve originals and recover a verified predecessor. A polished output still gets reviewed.

If one of these is unfamiliar, practice it on a small invented example before enlarging the task.

## Choose an improvement that has a measurable result

| Repeated problem | Useful improvement | Evidence it helped |
| --- | --- | --- |
| Re-explaining the same scope | Small project `CLAUDE.md` | Fewer repeated questions without hidden assumptions |
| Combining the same exports | Reviewed script, query, or Power Query procedure | Source counts/totals tie and schema changes are caught |
| Rebuilding a report | Stable metric definitions and layout | Another reviewer can reproduce the figures |
| Repeating a complex checklist | A narrow explicitly invoked skill | Synthetic cases catch missing evidence and wrong inputs |
| Losing the next step between sessions | Short approved handoff or redacted memory | Only relevant context is recalled |

Prefer an existing focused skill to a new overlapping one. Improve the prompt or project facts
first; a new skill is justified when the repeated procedure itself needs to be reusable.

## A narrow skill contract

State its purpose, authorized input/output, business rules, evidence, stop conditions, and what it
cannot verify. Keep local skills explicitly invoked. Add a catalog entry with an example and test
it on a normal case, missing evidence, and a misleading input. Do not describe a checklist as a
security control or a guarantee of correctness.

[Guide 03](03-professional-skills-by-category.md) covers task categories, and
[skill installation](../setup/SKILLS.md) covers copying, verification, updates, and removal.
Compare performance with the original process, including correction turns and reviewer effort.

## Integrations and agents are separate decisions

Experience does not grant new system access. Database connectors, Office integrations, hooks,
proxies, or scheduled jobs need a concrete purpose, the appropriate organizational review, and a
bounded test. A skill can draft SQL without connecting to production, and a local report can work
from approved exports without a new integration.

Subagents and teams can sometimes isolate independent work, but each runs its own context and
can add cost and coordination. Keep them outside the beginner path. Consider them only when a
measured task benefits and someone owns the usage budget and review. A routine reusable prompt
or an ordinary accounting workflow does not require agents.

## A prompt for improving a routine

```text
Routine mode. The approved process is [PROCEDURE] and the recurring problem is [PROBLEM].
Propose one focused improvement. Preserve the current outputs and controls. Explain the change,
required tools, expected benefit, and how to test it on a small approved copy before adoption.
Do not install, schedule, connect, or start subagents. Keep a manual fallback and rollback route.
```

Use [the token guide](13-token-efficient-work.md) to measure total consumption, and
[plans and diffs](04-reviewing-claude-plans-and-diffs.md) to review the proposed change.
