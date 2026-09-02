# Project instructions

> Template: copy this file into a project's root, replace every `[REPLACE]`
> section, and remove this note.

## Project

[REPLACE: Explain what this project does in one or two sentences.]

## Start here

Before changing files:

1. Read the README and the files related to the request.
2. Explain what you found in plain language.
3. Propose a small plan.
4. Wait for approval before making a broad or risky change.

## Commands

Only use commands verified from this project's files. Never invent commands.

| Task | Command |
| --- | --- |
| Install | `[REPLACE]` |
| Start | `[REPLACE]` |
| Test | `[REPLACE]` |
| Lint | `[REPLACE]` |
| Build | `[REPLACE]` |

Delete rows the project does not use.

## Project structure

- `[REPLACE: important path]`: [What belongs here.]
- `[REPLACE: important path]`: [What belongs here.]

Only document structure that is not obvious from the repository.

## Working rules

- Keep changes limited to the requested task.
- Follow existing project patterns.
- Prefer simple changes that are easy to review and undo.
- Do not change dependencies, configuration, or public interfaces unless asked.
- Add or update tests when behavior changes.
- Do not weaken tests or checks to make them pass.

## Ask before

- deleting files or data
- installing or removing dependencies
- running migrations or destructive commands
- using credentials or production systems
- committing, pushing, merging, publishing, or deploying
- changing authentication, authorization, privacy, or security behavior

Never place secrets, customer data, or private personal information in prompts,
files, logs, examples, or commits.

## Definition of done

Before reporting completion:

1. Run the smallest relevant test or check.
2. Review the complete diff for unrelated changes.
3. Explain what changed.
4. Report what passed, what was not run, and any remaining risk.
