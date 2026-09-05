# Contributing

This public kit helps a first-time property-tax/accounting user work with Claude Code in VS Code
on a managed Windows PC. Optimize for a useful first task, clear examples, correct evidence, and
small context. The default path assumes the extension and approved gateway already work.

## Structure

- `README.md`: short landing page and task navigation.
- `START-HERE.md`: recommended setup for an existing installation.
- `SKILLS.md`: every recommended skill, its purpose, example, and installation route.
- `setup/`: skill lifecycle, project setup, and the retained full onboarding reference.
- `skills/`: original, self-contained distribution folders, not auto-installed configuration.
- `templates/`: blank global, project, and handoff templates. Filled copies stay outside this repo.
- `practice/` and `examples/`: wholly invented exercises and answer keys.
- `guides/`: daily use, learning, and topic references; `guides/README.md` is the index.
- `docs/`: source/validation records, Windows checks, and deeper operational references.
- `tests/`: standard-library checks and manual QA procedures.

## Contribution rules

1. Keep the public content generic and technical. No credentials, company details, actual work data,
   customized work instructions, internal locations, or identifiable examples.
2. Keep the already-working setup path short. Do not require the full onboarding interview to add
   a local skill. The full reference retains its staged merge contract for those who need it.
   Default to the VS Code extension and Windows File Explorer. Label terminal exceptions with
   purpose, shell, working folder, expected result, and a supported fallback. Use the organization
   usage page as the allowance reference, never assume a personal subscription or extra models,
   and give each beginner step a check and a way to resume.
3. Respect approved scope. Preview configuration changes before approval; one explicit approval may
   cover a clearly listed batch. Preserve existing approved rules, verified backups, readback, and
   rollback. Silence does not authorize changes; managed policy can impose stricter requirements.
4. Do not configure connectors, proxies, hooks, subagents, or dependencies in the baseline. Document
   optional upstream packages separately, including their full contents, licenses, and runtime needs.
5. Local skills stay explicitly user-invoked with `disable-model-invocation: true`. Keep references
   inside the distributed folder where possible. Explain every local skill with a catalog example.
6. Keep specialized procedures out of global instructions. Ask only for material missing facts;
   use existing approved context without repeating the interview.
7. Verify numerical answer keys independently. Never imply that a source review, schema validator,
   or synthetic test establishes behavior in managed Windows, native Excel, or Claude Code.
8. Use American English and plain dashes. Do not edit `CHANGELOG.md` manually or modify the existing
   release cover asset. Use the maintainer's release process for changelog generation.

Useful contributions include source corrections, clearer examples, narrow skills for repeated
tasks, and actual Windows verification. Avoid overlapping skill collections and unsupported claims
of guaranteed savings or tax accuracy.

## Before pushing

Run from the repository root:

```sh
node tests/validate-repo.mjs
node tests/merge-spec.mjs
node tests/dashboard-spec.mjs
git diff --check
```

The first script checks local Markdown links, Claude skill frontmatter, JSON, and changelog shape.
The merge fixtures specify the retained full onboarding Stage 4 behavior. The dashboard tests check
synthetic calculations and filters. None requires package installation.

When changing Stage 3/4 or the global template, report the applicable manual results from
[the QA runbook](tests/QA-RUNBOOK.md). `NOT RUN` is honest; a blank or implied pass is not. For the
short setup, use W30/W31 in [the Windows ledger](docs/WINDOWS-VERIFICATION.md).

Review the public diff for work data, credentials, personal details, and accidental artifacts.
Inspect newly linked upstream entrypoints and installation behavior; URLs and package names drift.
Record source checks separately from actual runtime trials in
[the validation record](docs/TOOLKIT-VALIDATION.md).

## CI and release

The read-only GitHub Actions job runs the three scripts on Linux with Node 20 for pull requests
and main-branch pushes. It does not test a managed Windows desktop or check external links.

Before release, confirm CI, current source links, and the Windows ledger's actual statuses.
State outstanding checks in release notes. Do not claim that published instructions were installed
or tested on a work PC unless that was actually done.
