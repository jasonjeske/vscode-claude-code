# Contributing

This is a small, deliberately conservative repository. Its audience is a first-time Claude Code user
handling confidential corporate tax and reconciliation work on a managed Windows machine. That
audience shapes every rule below.

## What contributions fit

Welcome:

- Corrections. A wrong path, a stale command, an incorrect claim about Windows or VS Code behavior.
  These are the most valuable contributions here.
- Windows verification. Running a procedure in [`docs/WINDOWS-VERIFICATION.md`](docs/WINDOWS-VERIFICATION.md)
  on real Windows and reporting what happened, whether it confirms the claim or breaks it.
- Clarity. Prose that is easier for a non-developer to follow without becoming vaguer.
- Additional guides, following the `guides/NN-topic.md` convention and building on Guide 01 rather
  than repeating it.
- Test cases. New fixtures for `tests/merge-spec.mjs` that pin a merge behavior currently untested.

Not a fit, and likely to be declined:

- Unreviewed or overlapping skill collections. Keep the three core onboarding skills stable;
  focused optional skills belong in the separately documented expansion path.
- Any dependency, package manager file, or lockfile.
- MCP servers, connectors, hooks, plugins, or subagent configuration.
- Platform ports. This repository is Windows-only on purpose; a macOS or Linux variant is a
  different project.
- Automation of anything currently gated behind human approval.

## Design principles a change may not weaken

These are not preferences. A pull request that erodes one of them will be declined regardless of how
well it is written.

1. **Approval before every write.** No change may make a write implicit, batched, or inferred from
   an earlier approval.
2. **Redaction first.** No real names, employers, credentials, taxpayer or property identifiers,
   addresses, internal URLs, absolute paths, row-level data, or actual values. Placeholders only,
   using the `ENTITY-A` and `PERIOD-1` convention.
3. **Instructions are not enforcement.** Nothing here may be described as enforcing confidentiality
   or as a security control. See [`docs/SECURITY.md`](docs/SECURITY.md).
4. **Backup, readback, rollback.** Every write path keeps all three. A backup that is not read back
   does not count.
5. **Minimal trusted surface.** No configured MCP, connectors, hooks, plugins, subagents, or package
   dependencies. Documented optional upstream recommendations are not automatic installations.
   Validation scripts use only the Node standard library; the synthetic dashboard uses browser APIs.
6. **Skills stay user-invoked.** `disable-model-invocation: true` is invariant.
7. **CI never claims more than it tested.** No job may imply a verification it did not perform. This
   is why there is no `windows-latest` job.
8. **`assets/cover.svg` is untouchable.** It ships in tagged releases.

## Before you open a pull request

Run all three checks from the repository root. Each must exit 0.

```sh
node tests/validate-repo.mjs
node tests/merge-spec.mjs
node tests/dashboard-spec.mjs
```

`node tests/validate-repo.mjs` is the lint for this repository. It checks skill frontmatter, every
relative Markdown link, strict JSON parsing, and the changelog's shape. There is no other linter and
none will be added.

`node tests/merge-spec.mjs` checks the Stage 4 merge rules against the committed fixtures. If you
change merge behavior, the fixtures are the contract: update them deliberately in the same pull
request and say why in the description.

Also:

- Describe user-visible changes in the pull request. Do not manually edit `CHANGELOG.md`; use the
  maintainer's release process.
- If your change touches Stage 3 or Stage 4 behavior, run the relevant procedure in
  [`tests/QA-RUNBOOK.md`](tests/QA-RUNBOOK.md) and paste the results block into the pull request
  description. `NOT RUN` is an acceptable entry; a blank one is not.
- Use American English spelling, and no em dashes in prose.

## Continuous integration

`.github/workflows/validate.yml` runs all three scripts on every push to `main` and on every pull
request, on `ubuntu-latest` with Node 20, with read-only permissions.

CI does not check external links, and it does not test Windows behavior. Both are deliberate. See
decisions D2 and D8 in the project's design notes.

## Release checklist

For a maintainer cutting a release:

1. CI is green on `main`.
2. All three scripts pass locally from a clean checkout.
3. Manual external-link pass: open every external URL in `README.md`, `START-HERE.md`, and the
   guides, and confirm each still resolves to the intended page. CI does not do this.
4. Windows ledger reviewed: read `docs/WINDOWS-VERIFICATION.md` and state the current status in the
   release notes, including how many rows remain `UNVERIFIED`. Do not imply verification that has
   not happened.
5. Use the maintainer's release process to generate the version's changelog; do not manually edit it.
6. Tag the release and publish it, with the generated changelog section as the release notes.

Steps 3 and 4 are the two a maintainer is most likely to skip and the two most likely to mislead a
reader if skipped.
