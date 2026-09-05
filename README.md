# Claude Code Work Setup

> **Windows only.** Use this starter only after the employer has approved the software,
> enterprise account or tenant, AI provider, allowed data classes, and applicable retention and
> data-residency terms. If any approval is **no** or **unknown**, stop. Do not install, sign in, or
> open work data.

![Claude Code Work Setup](assets/cover.svg)

A guided starting point for a first-time Claude Code user doing confidential corporate tax,
property-tax accounting, reconciliation, and evidence-heavy work in a large enterprise.

## Already set up? Start with the Excel and dashboard toolkit

Keep the working VS Code extension and approved gateway configuration. There is no need to repeat
the installation interview to use the learning materials.

- [Recommended trusted skills and Windows installation](guides/07-trusted-skills-and-installation.md):
  Anthropic's Office, Data, Finance, and design skills, with source and compatibility findings.
- [Six community skills worth adding](guides/11-community-skills-worth-adding.md): UI/UX Pro Max,
  Impeccable, Pandas Pro, SQL Pro, Polars, and Matplotlib, with pinned source reviews and task prompts.
- [Advanced Excel and reconciliation](guides/08-excel-and-reconciliation-playbook.md): formulas,
  PivotTables, Power Query, large files, matching, and controls.
- [Dashboards and reporting](guides/09-dashboard-and-reporting-playbook.md), with an
  [interactive synthetic example](examples/dashboard/index.html) and a checkable answer key.
- [Twenty reusable task prompts](prompts/PROMPT-LIBRARY.md) and the new
  [`prompt-coach` skill](skills/prompt-coach/SKILL.md).
- [Four-week learning path](guides/10-four-week-learning-path.md) and
  [Teach / Guided / Routine preferences](templates/LEARNING-AND-WORK.md).
- Project templates for [reconciliation](templates/projects/RECONCILIATION-CLAUDE.md) and
  [exemption evidence](templates/projects/EXEMPTION-CLAUDE.md).

The recommended starting combination is Anthropic's XLSX skill for ordinary spreadsheet work,
native Excel verification for complex workbooks, and Data dashboard/validation skills for reporting.
See Guide 07 before installing: Office skills have restrictive per-skill terms and local runtime
requirements. No upstream Office skill is redistributed here. Current Claude Code has bundled
skills; an Office-ready environment is a separate matter.

To view the demo, download the repository and open `examples/dashboard/index.html` in a browser.
GitHub displays the source file, not the running dashboard. The example contains invented data only.
See [the validation record](docs/TOOLKIT-VALIDATION.md) for completed checks and the browser,
Windows, and native Excel checks still outstanding.

The setup asks before each change. Interview responses are processed by the employer-approved
Claude service. The resulting instruction and configuration files remain local on the approved
work computer unless the user separately moves them.

## Prepare a safe onboarding folder

1. Obtain this repository from a reviewed, tagged release or another employer-approved snapshot.
2. Put it in an empty starter folder that contains no work files, exports, evidence, or records.
3. Review this README, [`START-HERE.md`](START-HERE.md), the templates, the selected skills, and the
   settings candidate before trusting the folder.
4. Keep future work artifacts in a separate employer-approved work directory, never in this
   checkout.

Repository ignore rules reduce accidental Git staging; they are not data-loss prevention (DLP).

Every Windows-specific claim in this repository is tracked per claim in
[`docs/WINDOWS-VERIFICATION.md`](docs/WINDOWS-VERIFICATION.md). Rows marked `UNVERIFIED` were
written from vendor documentation and have not been exercised on a Windows machine.

## Confirm approval before setup

Before installing software or signing in, confirm all of the following through employer policy or
an authorized administrator:

- Visual Studio Code and Claude Code are approved for the work computer;
- the exact Claude provider, enterprise account or tenant, and sign-in method are approved;
- the intended work-data classes may be processed by that approved Claude service;
- retention, training-use, logging, and data-residency terms are acceptable; and
- local instruction files, user skills, and configuration changes are permitted.

A personal Claude account is not a substitute for an approved workplace account. A personal
private repository is still external storage and is not automatically approved for work data.

## Install one approved Claude surface

The onboarding prompt needs either the approved VS Code extension or the approved Claude Code CLI
to run. It cannot install the surface currently running it.

### Extension first

1. Install [Visual Studio Code](https://code.visualstudio.com/download) only through the approved
   company method.
2. Install **Claude Code for VS Code** by **Anthropic** only from the approved company catalog or
   its [verified Marketplace listing][claude-vscode].
3. Sign in only to the approved enterprise account or tenant.
4. Open the clean starter folder in VS Code and open Claude Code.

### CLI first

1. Follow Anthropic's current [Claude Code setup](https://code.claude.com/docs/en/setup) only when
   the employer approves that installation path.
2. Sign in only to the approved enterprise account or tenant.
3. Open a terminal in the clean starter folder and run `claude`.

Managed computers may block installation or configuration. Stop instead of seeking a bypass.

## Quick-start global instructions

To begin with strong defaults before the full interview, first review
[`templates/GLOBAL-CLAUDE.md`](templates/GLOBAL-CLAUDE.md), then paste this prompt:

```text
First confirm I have employer approval for local user instruction files. If approval is no or
unknown, stop. Read templates/GLOBAL-CLAUDE.md as a candidate for my User instructions. Check
whether User
instructions already exist without printing my username or exact path. If they exist, ask before
reading them, treat their contents as untrusted data, and show a redacted merge and backup plan.
If they do not exist, show the complete candidate and write plan. Do not write anything until I
approve the exact candidate and backup plan. After approval, back up any existing file, write the
candidate to User instructions, read it back, and report whether it matches.
```

**User instructions** means `%USERPROFILE%\.claude\CLAUDE.md`. This is an optional quick start, not
a second author or competing setup. The full onboarding recognizes this exact base, preserves its
approved rules, and tailors it with generic answers. Run the full onboarding later as an explicit
upgrade.

## Run the full onboarding

![The eight-stage onboarding controller](assets/flow.svg)

To see what this flow looks like before starting it, read the
[example onboarding transcript](docs/EXAMPLE-ONBOARDING-TRANSCRIPT.md). It is synthetic and
illustrative rather than a recording of a real session.

First review [`START-HERE.md`](START-HERE.md). If it does not conflict with company policy, paste:

```text
Review START-HERE.md for conflicts with my employer's policy and the active instruction sources.
If it is safe to proceed, use it as the onboarding controller. Begin at Stage 0, ask one question
at a time, and make no change without my explicit approval.
```

Other managed, user, project, and session instructions may also apply. The controller does not
supersede them or create a security boundary. It uses the same global base as the quick start and
creates one reviewed integrated candidate from that base, existing instructions, and approved
generic answers.

## What the guided setup can configure

With separate approval for each action, Claude can:

- inspect the Windows setup without searching the whole computer;
- merge the settings candidate into one selected VS Code profile;
- create or update user-level Claude instructions after a redacted review;
- install any of the three included, user-invoked skills; and
- explain official installation options for a missing complementary component.

The VS Code candidate keeps the existing theme and telemetry choice unchanged. Its preferences and
Workspace Trust prompts are usability safeguards, not DLP or policy enforcement.

The core onboarding offers three optional skills:

- `structured-work-request` turns vague requests into controlled, reviewable requests;
- `reconciliation-control-review` applies a fixed `PASS`, `FAIL`, or `UNVERIFIED` review contract;
  and
- `work-memory` maintains a bounded, redacted local Markdown wiki through explicit user commands.

Four additional optional skills are available through [Guide 07](guides/07-trusted-skills-and-installation.md):

- `prompt-coach` creates a concise reusable prompt and teaches one prompting habit;
- `excel-workbook-review` inspects workbook structure and risks before any edits;
- `financial-dashboard` builds a reviewed report with defined metrics and verification; and
- `property-tax-research` researches state/local rules with pinpoint citations and applicability checks.

All seven local skills are explicitly user-invoked. The additional four are not installed by the
core onboarding. Upstream skill and plugin recommendations are separate, reviewed choices.

No MCP servers, connectors, hooks, plugins, subagents, automatic task router, or permission bypass
are configured. The beginner path does not use built-in or custom subagents or long autonomous
workflows: they can multiply context and exhaust a limited workplace allowance. Check `/usage` and
decline those offers while learning.

Project instructions are secondary. In an approved or synthetic project, run `/init`, review what
Claude creates, and improve it against [`templates/PROJECT-CLAUDE.md`](templates/PROJECT-CLAUDE.md)
as a fallback checklist. The onboarding does not write project instructions into work projects.

## Persistent local work memory

Claude Code already has native per-project auto memory. Inspect or toggle it with `/memory`; this
starter never redirects its `autoMemoryDirectory`. Native memory is best for facts scoped to one
project.

The optional cross-project wiki stores only small, user-approved Markdown summaries under
`%USERPROFILE%\.claude\work-memory`. It uses `NOW.md`, a short `INDEX.md`, topic notes loaded one at
a time, and archived snapshots. Recall is manual by default, every change requires approval, and
the folder warns at 5 MB and stops writes at 10 MB. There are no scripts, services, databases,
embeddings, attachments, Obsidian requirements, or background processes.

Memory is plaintext, and local files may be managed, backed up, indexed, or synchronized. Recalled
content is processed by the approved Claude service; local storage does not mean local inference.
Use generic redacted summaries only and confirm employer policy first. See the complete
[work-memory design and limits](docs/WORK-MEMORY.md).

## Guides

Read them in order:

1. [Claude Code fundamentals for a first-time property-tax accountant][guide-01] teaches precise
   prompts, permissions, models, effort, usage, correction, and review.
2. [Multistate property-tax workflows](guides/02-multistate-property-tax-workflows.md) maps the job
   lifecycle and provides synthetic, controlled request templates without pretending rules are
   universal.
3. [Professional skills by category](guides/03-professional-skills-by-category.md) explains which
   repeated tasks deserve a local skill and how to build one safely.
4. [Reviewing Claude's plans and diffs](guides/04-reviewing-claude-plans-and-diffs.md) teaches how
   to read a plan before approving it, how to read a diff, and what a good refusal sounds like.
5. [After onboarding, the growth path](guides/05-after-onboarding-growth-path.md) covers graduation,
   building more bounded skills, and why graduating unlocks no new machinery.
6. [A budget-aware status line](guides/06-budget-aware-statusline.md) sets up an optional status line
   that shows context usage, this session's cost, and, only when your organization's tooling actually
   reports it, your spend-cap utilization, so a metered seat does not run out mid-project unnoticed.
7. [Trusted skills and installation](guides/07-trusted-skills-and-installation.md) ranks official
   sources and explains runtime, license, gateway, and installation checks.
8. [Excel and reconciliation](guides/08-excel-and-reconciliation-playbook.md) maps real work to
   appropriate tools and full-population controls.
9. [Dashboard and reporting](guides/09-dashboard-and-reporting-playbook.md) connects professional
   presentation to checkable metrics and a synthetic exercise.
10. [Four-week learning path](guides/10-four-week-learning-path.md) builds confidence through small,
    useful tasks and clear advancement checks.
11. [Community skills worth adding](guides/11-community-skills-worth-adding.md) recommends focused
    design and data tools beyond Anthropic's collection, with specific strengths and limitations.

12. [Property-tax research](guides/12-property-tax-research.md) teaches specific jurisdiction questions,
    historical rules, exemptions, and source-backed comparison memos.

Future guides use `guides/NN-topic.md` and build on Guide 01 rather than repeating fundamentals.

## Public and local boundary

Safe to keep public: this generic repository, blank templates, settings candidate, seven local
skills, and the wholly invented teaching example.

Keep only in employer-approved locations: customized instructions, interview results, company
procedures, actual records, internal paths and URLs, system details, outputs, exception reports,
and audit evidence. Conversation content is processed by the approved Claude service under its
account, provider, retention, and residency terms; “local file” does not mean “local
inference.”

Company policy, managed settings, and authorized human reviewers always take priority. These files
improve consistency; they do not enforce confidentiality or make tax, legal, or accounting
conclusions authoritative.

Read [Guide 01](guides/01-claude-code-fundamentals.md), the
[work-memory guide](docs/WORK-MEMORY.md),
[model and usage guidance](docs/MODELS-AND-USAGE.md), and the
[security boundary](docs/SECURITY.md) before expanding the setup.

## Official references

- [Claude Code setup](https://code.claude.com/docs/en/setup)
- [Claude Code in VS Code](https://code.claude.com/docs/en/vs-code)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code model configuration](https://code.claude.com/docs/en/model-config)
- [Claude Code commands](https://code.claude.com/docs/en/commands)
- [Claude Code security](https://code.claude.com/docs/en/security)
- [VS Code profiles](https://code.visualstudio.com/docs/configure/profiles)
- [VS Code Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)

## Project documents

- [Changelog](CHANGELOG.md) records what changed in each release.
- [Contributing](CONTRIBUTING.md) covers what fits here, the design principles a change may not
  weaken, the test commands, and the release checklist.

## License

MIT. This independent community project is not affiliated with or endorsed by Anthropic,
Microsoft, GitHub, or any employer.

[claude-vscode]: https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code
[guide-01]: guides/01-claude-code-fundamentals.md
