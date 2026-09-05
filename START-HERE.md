# Set up an already working work PC

Use this path when Claude Code already works in VS Code through the approved workplace provider
or gateway. You need the downloaded repository, permission to add local instructions/skills, and
an approved practice location separate from this checkout. You do not need a GitHub account or Git.

If VS Code or Claude Code is missing, use the organization's installation process and
[Anthropic's VS Code instructions](https://code.claude.com/docs/en/vs-code). The optional
[full onboarding reference](setup/FULL-ONBOARDING.md) covers a more detailed fresh-install review.
Do not replace an existing gateway/API-key setup with a personal sign-in.

## 1. Open the starter and confirm the boundary

Extract the ZIP. Read the README before trusting the folder in VS Code. Use **File > Open Folder**
to open the extracted repository, then open the existing Claude Code extension.

Confirm that the configured provider and intended work-data use are employer-approved. Use
`/status` or the available account/settings view; do not paste account details or credentials into
chat. If an optional installation is blocked, record it as unavailable and continue with the
permitted materials. This kit does not require changes to managed settings.

## 2. Add a small global instruction file

Read [GLOBAL-CLAUDE.md](templates/GLOBAL-CLAUDE.md). Its job is to set concise explanations,
teaching mode, preservation rules, and the work boundary across projects.

1. In Explorer's address bar, enter `%USERPROFILE%\.claude`.
2. If local configuration is permitted and the folder is absent, create `.claude` under your
   user profile. Do not change a managed location.
3. If `CLAUDE.md` exists, make a dated backup and open it to confirm the backup is readable.
   Merge only the useful, nonconflicting additions in VS Code. Preserve existing approved rules.
4. If it does not exist, copy `templates/GLOBAL-CLAUDE.md` there and rename it `CLAUDE.md`.
5. Open the saved file and confirm it matches the intended text. Enable Explorer's file-name
   extensions if necessary so it is not accidentally named `CLAUDE.md.txt`.

Keep company-specific details in approved local project instructions. Do not copy the entire
library into the global file. Start a fresh Claude conversation and use `/memory`, where
available, to inspect which instruction files are loaded.
[Official instruction locations](https://code.claude.com/docs/en/memory).

## 3. Add the first local skills

Start with **prompt-coach** and **excel-workbook-review**. For immediate law research, also choose
**property-tax-research**. The [catalog](SKILLS.md) has every skill's purpose and example.

Follow [Install, verify, update, and remove skills](setup/SKILLS.md). The short version: copy each
complete selected folder from this repository's `skills/` into `%USERPROFILE%\.claude\skills\`.
Do not overwrite a same-name folder without comparing it and keeping a verified backup.

The final layout should look like this:

```text
.claude/
  CLAUDE.md
  skills/
    prompt-coach/
      SKILL.md
    excel-workbook-review/
      SKILL.md
    property-tax-research/          optional for the first session
      SKILL.md
      references/
        research-memo.md
```

Typing `/prompt-coach` should select the skill. Try:

```text
/prompt-coach
Help me ask Claude to explain an unfamiliar synthetic workbook, read-only.
I want a sheet map and one explanation of how to check a formula.
```

It should help draft the request, not open work files or start editing. If the command is missing,
use [the troubleshooting table](setup/SKILLS.md#troubleshooting).

## 4. Add Excel tools when there is a task for them

The local workbook-review skill provides an inspection procedure. For spreadsheet creation and
editing, evaluate Anthropic's **xlsx** skill. Its Office bundle is linked, not redistributed here.
Check its license, required Python/Office tooling, and approved installation route in
[the upstream setup section](setup/SKILLS.md#upstream-skills-and-plugins).

Do not promise that installing a skill enables native PivotTables, VBA, Power Query refresh, or
all formula calculations. Test a small copy in native Excel before changing a complex workbook.
Add PDF for notices, Word/PowerPoint for deliverables, and dashboard/design tools when needed.

## 5. Create a practice project and try one task

Open a new approved practice folder outside this repository. Add a project `CLAUDE.md` using
[Project setup](setup/PROJECTS.md). Use only the invented examples in the
[first-session exercise](practice/FIRST-SESSION.md).

Start in **Guided** mode. Record `/usage` before and after the task if available. Confirm that the
answer matches the answer key and that the user can explain one check. No real data is needed.

## 6. Leave a usable handoff

Complete the blank [setup receipt](templates/SETUP-RECEIPT.md) in an approved local location.
Record the reviewed snapshot, chosen skill scope, installed names, backup locations, checks that
passed, blocked features, and next task. Never commit the filled receipt here.

Bookmark the [daily desk guide](guides/DAILY-USE.md), [skill catalog](SKILLS.md), and
[prompt library](prompts/PROMPT-LIBRARY.md). Stop installing when the first useful task works.

## Prefer Claude to help with the copying?

After reviewing the above, paste this into Claude Code with the starter folder open:

```text
Read START-HERE.md and setup/SKILLS.md from this starter. My workplace Claude Code and gateway
already work. Help me add the global instruction template and prompt-coach and
excel-workbook-review in personal scope. Use no work data and keep my provider/settings unchanged.
First inspect only the selected source files and whether the exact destinations exist. If existing
instructions or same-name skills need reading, confirm their approved scope before reading.
Show the precise proposed copies/merge and backup plan together. Wait for my approval of that
batch, then perform only those changes, verify readback, and report the actual results.
Ask one question only when an unresolved choice changes the result. Do not install upstream
packages, run agents, scan my computer, or overwrite existing content without the reviewed plan.
```

This is an instruction-guided procedure, not a tested Windows installer. Tool approval and managed
policy still apply. Approval of one reviewed batch is enough for that batch; changed scope needs a
new decision.
