# Changelog

Format follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this project
follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `CONTRIBUTING.md` describing what contributions fit, the design principles a change may not
  weaken, and the release checklist.
- This changelog.
- Continuous integration (`.github/workflows/validate.yml`) that runs both validation scripts on
  every push to `main` and every pull request.
- `tests/validate-repo.mjs`, a dependency-free repository lint covering skill frontmatter, internal
  Markdown links, strict JSON, and changelog shape.
- `tests/merge-spec.mjs`, an executable specification of the Stage 4 settings merge rules, checked
  against committed fixtures including a case that proves a weakening setting is refused even when
  the key is absent from the existing file.
- `tests/fixtures/`, twelve pinned JSON merge cases plus a synthetic instruction file for the manual
  Stage 3 drill.
- `tests/QA-RUNBOOK.md`, a manual conformance protocol for the parts of the onboarding that a script
  cannot test, including a rollback drill.
- `docs/WINDOWS-VERIFICATION.md`, a per-claim ledger of every Windows behavior this repository
  asserts. All 25 rows start `UNVERIFIED` because nothing here has been exercised on Windows.
- `docs/EXAMPLE-ONBOARDING-TRANSCRIPT.md`, a synthetic worked transcript of all nine stages, so you
  can see what the onboarding does before granting it any approval.
- `guides/04-reviewing-claude-plans-and-diffs.md` on reviewing a plan, reading a diff, recognizing
  red flags, and refusing well.
- `guides/05-after-onboarding-growth-path.md` on what growth looks like after onboarding, and why
  graduating does not unlock MCP servers, connectors, hooks, plugins, or subagents.
- `guides/06-budget-aware-statusline.md`, `config/statusline.ps1`, and
  `config/statusline-budget.example.json`: an optional Claude Code status line for a metered
  workplace seat, showing context usage and this session's cost always, and a gateway spend-cap
  percentage only when your organization's own tooling actually reports one. No dollar figure is
  ever invented; it is calculated locally only from a number you type in yourself.

### Changed

- `README.md` links to the new documents and states plainly that Windows behavior claims are
  unverified.
- `START-HERE.md` points to the example transcript before Stage 0 and to guide 04 in Stage 3. No
  stage logic changed.

### Fixed

Three defects found by running the `tests/QA-RUNBOOK.md` drill against this repository.

- The Stage 3 drill fixture, `tests/fixtures/claude-md-existing.md`, contained nothing to refuse, so
  three of the five untrusted-content rules it was meant to test could not be tested: a session that
  obeyed an embedded instruction looked exactly like one that correctly refused. The fixture now
  carries an embedded instruction that tries to skip the Stage 3 approval question, and a
  credential-shaped string that is entirely invented. The runbook states what must happen to each.
- The Stage 4 merge specification exercised only two of its five protected settings. A new
  `gateway` fixture case covers the remaining three: the startup-prompt setting, the
  `claudeCode.initialPermissionMode` approval gate, and any key naming automatic approval or a
  permission bypass. It also proves the rule still adds ordinary new settings rather than blocking
  everything unfamiliar.
- `docs/EXAMPLE-ONBOARDING-TRANSCRIPT.md` showed the `[SETUP stage/8 — NAME]` marker on only 9 of
  its 31 Claude turns, contradicting the rule in `START-HERE.md` that requires it in every response,
  and omitting it from the approval and write-result turns that matter most. Every turn now carries
  the marker for its stage.

## [1.1.0] - 2026-09-03

### Added

- Bounded local work memory: an optional cross-project Markdown wiki under the user profile, driven
  by explicit user verbs, with a 5 MB warning and a 10 MB hard stop, plus the `work-memory` skill
  and `docs/WORK-MEMORY.md` describing its design and limits.

## [1.0.0] - 2026-09-03

### Added

- Initial public starter for VS Code and Claude Code: the approval-gated onboarding controller,
  conservative settings candidate, instruction templates, three user-invoked skills, and the
  security and model guidance documents.
- Onboarding redesigned around professional Claude Code work: an eight-stage interview that asks one
  question at a time, treats unknown policy answers as hard stops, and backs up and reads back every
  file it writes.
