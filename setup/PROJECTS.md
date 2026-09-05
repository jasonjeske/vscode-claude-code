# Set up a project for useful work

Keep the downloaded public starter separate from the approved work folder. A project is simply a
folder for one related objective, with instructions and inputs that belong together. No Git repo
or new application is required for this structure.

## Choose one instruction template

| Project | Start with | Add when useful |
| --- | --- | --- |
| General learning or document task | [PROJECT-CLAUDE.md](../templates/PROJECT-CLAUDE.md) | [Learning preferences](../templates/LEARNING-AND-WORK.md) |
| Reconciliation | [RECONCILIATION-CLAUDE.md](../templates/projects/RECONCILIATION-CLAUDE.md) | Agreed source schema, exact match rules, control expectations |
| Exemption evidence | [EXEMPTION-CLAUDE.md](../templates/projects/EXEMPTION-CLAUDE.md) | Approved evidence requirements and source matrix |
| State/local legal research | [RESEARCH-CLAUDE.md](../templates/projects/RESEARCH-CLAUDE.md) | Issue-specific source register and research memo |
| Dashboard or recurring report | [DASHBOARD-CLAUDE.md](../templates/projects/DASHBOARD-CLAUDE.md) | Approved metric dictionary and output format |

Copy **one** selected template into the work folder as `CLAUDE.md`, then adapt it locally. Merge
with an existing file after review and a verified backup. Do not paste all templates into one file.
Claude Code also offers `/init`; use its result as a draft and review it against the selected
template. Do not run it across a broad parent directory containing unrelated work.

Identify the outcome, source files, period, row grain, controls, permitted outputs, and reviewer.
Remove unused placeholders. Missing business rules remain unknown; a template does not invent them.
Add only project-specific information that policy permits Claude to process. Do not copy the filled
file back to this starter or a public issue.

## A small folder layout

For a new practice project in Windows File Explorer, create a folder in the approved location,
then copy your selected template into it. Rename that copy `CLAUDE.md` with file-name extensions
visible. In VS Code, use **File > Open Folder**, select this project, open `CLAUDE.md`, edit its
placeholders, and press **Ctrl+S**. Create any needed subfolders through File Explorer's **New > Folder**.
Reopen the saved file to check it before starting the first project prompt. No terminal is needed.

If the organization already has a workpaper layout, use it. Otherwise this is a suggested structure:

```text
approved-work-project/
  CLAUDE.md
  inputs/        approved source copies; preserve originals
  working/       reproducible scripts or queries when needed
  outputs/       newly generated workpapers and reports
  evidence/      control results, source register, reviewer notes
```

These folder names do not enforce access control. Use approved storage. Do not place database
credentials in the project instructions or copy entire mailboxes/shared drives into `inputs`.

## First project prompt

```text
Read this project's CLAUDE.md. Guided mode. My outcome is [ONE RESULT] for [PERIOD].
Use only [APPROVED INPUT REFERENCES]. The approved output is [NEW FILE OR CHAT SUMMARY].
First identify missing business rules and propose the smallest useful step. If the supplied scope
is sufficient, proceed within the authorized actions. Preserve original files and show how to
check the result. Do not load unrelated folders or start subagents.
```

Use actual approved file references through VS Code's `@` file picker where appropriate; neutral
labels are for examples and summaries, not a substitute for identifying which input is authorized.

## End the session

Record completed output, source version, checks, exceptions, and the next step in the approved
location. Keep the handoff brief. Resume the same objective with the relevant evidence; begin a
fresh conversation for unrelated work. Use [the daily guide](../guides/DAILY-USE.md) for examples.
