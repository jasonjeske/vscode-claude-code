# VS Code + Claude Code starter

A small Windows-friendly setup for someone learning Claude Code in VS Code while
working with confidential, regulated accounting and reconciliation workflows.
Nothing runs automatically. Everything here is generic and contains no company,
person, taxpayer, property, system, or project details.

## Files

| File | Purpose |
| --- | --- |
| `settings.json` | Safe, beginner-friendly VS Code and Claude Code settings |
| `extensions.json` | Five recommended VS Code extensions |
| `GLOBAL-CLAUDE.md` | Generic global instructions for careful regulated work |
| `CLAUDE.md` | Universal per-project instructions template |
| `SETUP-INTERVIEW.md` | Local interview prompt for safely personalizing the setup |
| `TOOLS-AND-SKILLS.md` | Gradual guide to Claude tools, plugins, and Superpowers |

## Install on a new Windows PC

### 1. Install VS Code

Download and install [Visual Studio Code](https://code.visualstudio.com/).
During installation, allow VS Code to add itself to PATH if the installer offers
that option.

### 2. Create a separate profile

1. Press `Ctrl+Shift+P`.
2. Run **Profiles: Create Profile**.
3. Choose **Create an Empty Profile**.
4. Name it **Claude Code Beginner**.

This keeps the starter settings separate from any existing VS Code setup.

### 3. Install the extensions

While the new profile is active, press `Ctrl+Shift+X` and install:

1. **Claude Code for VS Code** by Anthropic
2. **inlineMark** by 2001Y
3. **markdownlint** by David Anson
4. **Code Spell Checker** by Street Side Software
5. **GitHub Theme** by GitHub

The exact Marketplace identifiers are in [`extensions.json`](extensions.json).
Review each publisher before installing.

### 4. Copy the settings

While the **Claude Code Beginner** profile is active:

1. Press `Ctrl+Shift+P`.
2. Run **Preferences: Open User Settings (JSON)**.
3. If the file is empty, paste the contents of [`settings.json`](settings.json).
   If it already contains settings, merge the entries instead of replacing them.
4. Save with `Ctrl+S`.
5. Run **Developer: Reload Window**.

The profile uses **GitHub Dark Dimmed**, PowerShell, Manual Claude permissions,
and conservative Workspace Trust prompts. Automatic saving and dangerous
permission bypass are disabled.

The editor font is **Cascadia Code** with **Consolas** as a fallback. Windows
normally provides Consolas. Cascadia Code is optional and available from
[Microsoft's official repository](https://github.com/microsoft/cascadia-code).

### 5. Open Claude Code

1. Open a project with **File > Open Folder**.
2. Trust it only if it is a project you recognize.
3. Open any file.
4. Select the Claude spark icon.
5. Sign in and complete Claude Code's walkthrough.

Start with:

```text
Analyze this project without changing files. Explain what it does, how it is
organized, how to run it, and how to test it.
```

### 6. Add the global instructions

1. Create `%USERPROFILE%\.claude` if it does not exist.
2. Copy [`GLOBAL-CLAUDE.md`](GLOBAL-CLAUDE.md) to
   `%USERPROFILE%\.claude\CLAUDE.md`.
3. Keep it generic until the local setup interview is complete.

These global instructions teach Claude to work gradually, preserve source files,
create reconciliation evidence, protect confidential data, and require approval
for consequential actions.

### 7. Run the local setup interview

Open [`SETUP-INTERVIEW.md`](SETUP-INTERVIEW.md) and paste its prompt into Claude
Code on the approved work computer. It asks one question at a time and proposes
improvements without requesting company names, real records, credentials,
internal URLs, or actual financial values.

The completed answers and customized files stay on the work computer. Do not
commit them to this repository or a personal cloud account.

### 8. Add `CLAUDE.md` to a project

Copy [`CLAUDE.md`](CLAUDE.md) into the root of a project. Replace every
`[REPLACE]` section with approved project information and delete unused sections.

Claude reads this file when a conversation starts. Keep it short, specific, and
free of passwords, tokens, taxpayer data, company-confidential details, and
personal information.

## Markdown editing

Markdown files open in inlineMark, which displays headings, lists, tables, and
code blocks as formatted content while they remain editable.

To view the Markdown symbols:

1. Press `Ctrl+Shift+P`.
2. Run **inlineMark: Reopen with Text Editor**.
3. Press `Ctrl+K`, then `V` for a side-by-side preview.

## Claude in the VS Code terminal

The graphical extension and terminal CLI are separate installations. To use the
`claude` command in PowerShell, follow Anthropic's current
[Claude Code quickstart](https://code.claude.com/docs/en/quickstart).

The terminal CLI has separate permissions. Run `/permissions` and use Manual
mode while learning. Never use permission-bypass mode on a normal computer or
work project.

## Public repository boundary

This generic starter is suitable for a public repository. The customized global
instructions, interview answers, company procedures, actual skills, real
examples, file locations, and system information are not. Keep those only on the
approved work computer unless the employer explicitly authorizes another storage
location. A personal private GitHub repository is still external storage and is
not automatically approved for company information.

## Optional next steps

Do not install a large tool collection on day one. Read
[`TOOLS-AND-SKILLS.md`](TOOLS-AND-SKILLS.md) after learning basic project
analysis, plans, permissions, edits, tests, and diff review.

The first optional plugin recommended there is
[Superpowers](https://github.com/obra/superpowers), which adds structured
brainstorming, planning, testing, debugging, and review workflows.

## Work-computer warning

Follow the employer's AI, source-code, privacy, credential, and software-install
policies. VS Code telemetry being disabled does not make Claude local or
offline. Files and command output Claude reads can become conversation context
processed under the applicable Anthropic account and organization policies.

Do not trust an unfamiliar repository merely to activate Claude. Inspect
`CLAUDE.md`, `.claude/`, `.mcp.json`, hooks, plugins, and installation scripts
first, or use an isolated environment.

## Sources

- [Claude Code for VS Code](https://code.claude.com/docs/en/vs-code)
- [Claude Code best practices](https://code.claude.com/docs/en/best-practices)
- [VS Code profiles and settings](https://code.visualstudio.com/docs/configure/profiles)
- [VS Code Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)

## Disclaimer

This is an independent community starter configuration. It is not affiliated
with or endorsed by Microsoft, GitHub, Anthropic, or the extension publishers.
