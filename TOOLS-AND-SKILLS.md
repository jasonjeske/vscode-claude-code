# Tools and skills to add gradually

Do not install a large Claude setup on the first day. Start with the VS Code
extension, Manual permissions, the global instructions, and a few safe prompts.

## First: discover work without changing it

```text
Analyze this folder without changing files. Explain what each file appears to be,
how the files relate, what period or process they cover, and what information is
missing. Do not expose confidential values in your summary.
```

```text
Describe this workflow in plain language. Identify its inputs, outputs, control
totals, approval points, and possible failure modes. Do not make changes.
```

```text
Propose three small ways Claude Code could assist this process while preserving
original files and requiring human review. Do not automate anything yet.
```

## Essential built-in commands

- `/permissions`: review what Claude may do
- `/clear`: start fresh before an unrelated task
- `/context`: see what is consuming the context window
- `/doctor`: check the installation and configuration
- `/init`: draft project instructions after Claude understands a project
- `/plugin`: browse plugins only when a real need appears

## Build the real setup locally

Use [`SETUP-INTERVIEW.md`](SETUP-INTERVIEW.md) on the approved work computer.
It interviews the user without requesting confidential examples, then proposes a
custom global `CLAUDE.md`, project template, and at most three useful skills.

Likely local skills, created only after the interview, are:

1. **Workflow discovery**: maps a new folder, documents, spreadsheets, inputs,
   outputs, controls, and questions without editing anything.
2. **Reconciliation review**: applies the organization's approved matching,
   control-total, exception, and audit-trail rules.
3. **Evidence and handoff review**: verifies outputs, lists unresolved exceptions,
   and prepares a concise reviewer handoff.

These should be customized locally because real procedures, systems, fields, and
controls may be confidential. Do not publish the finished skills.

## Superpowers: useful later, not required

[Superpowers](https://github.com/obra/superpowers) provides structured
brainstorming, planning, test-driven development, debugging, and review. It is
mainly a software-development methodology.

It may help when building a script or internal tool. It is unnecessary for basic
folder discovery, document explanation, or routine accounting analysis, and it
can make small tasks feel heavier.

If company policy permits it, install from Anthropic's official marketplace:

```text
/plugin install superpowers@claude-plugins-official
```

## Optional tools, only with workplace approval

### Python and the VS Code Python extension

Python can help with repeatable CSV, spreadsheet, and reconciliation workflows,
but it should be added only when the user is ready to review scripts and the
company permits it. Begin with copies or invented sample data, never original
production files.

### GitHub CLI

If the workplace uses GitHub and permits its CLI,
[GitHub CLI](https://cli.github.com/) lets Claude read issues and pull requests.
Do not let Claude create, comment, push, or publish without explicit approval.

### Language-specific code intelligence

When a real automation project has a known language, use `/plugin` to look for a
code-intelligence plugin for that language. Do not install several language
plugins in advance.

### MCP servers

Do not configure MCP during the initial setup. MCP servers can connect Claude to
external tools and data and may run commands with granted permissions. Add one
only for a documented need after reviewing its source, publisher, requested
access, data handling, and company policy.

### Subagents

Use subagents later for independent review, not as a team of autonomous writers:

```text
Use a separate subagent to review this result against the stated controls. Do
not make changes. Report missing checks, unexplained differences, and unsupported
assumptions.
```

## A safe learning sequence

1. Ask Claude to explain a folder or workflow without changing it.
2. Learn Manual permissions, plans, file references, and diff review.
3. Perform one small task on copies or invented sample data.
4. Verify row counts, totals, exceptions, and outputs.
5. Run the local setup interview.
6. Add one local skill for a genuinely repeated workflow.
7. Add Python, Superpowers, GitHub CLI, or MCP only when there is a real need and
   workplace approval.

## Avoid initially

- permission-bypass mode
- automatic commits, pushes, emails, filings, uploads, or submissions
- unknown plugins or MCP servers
- multiple agents editing the same files
- changing original spreadsheets or source exports
- putting work data into public examples or repositories
- installing tools before confirming company policy

## Sources

- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Discover plugins](https://code.claude.com/docs/en/discover-plugins)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [Anthropic's official plugin directory](https://github.com/anthropics/claude-plugins-official)
- [Superpowers](https://github.com/obra/superpowers)
