# Use the guide and Claude side by side

[Setup](../START-HERE.md) | [Lessons](../LEARN.md) | [Daily reference](DAILY-USE.md)

Keep this GitHub guide open in your browser and do the exercise in the **Claude Code extension
inside VS Code**. The guide is your instruction book; Claude's chat is where you ask for help.
Read one section, try its prompt, check the result, then follow Next. You can pause at any check.
You do not need a personal Claude subscription, terminal experience, or every recommended skill
to follow this path with an already working, approved gateway setup.

If you have only downloaded a ZIP and have not created or opened the folders yet, follow
[the README walkthrough](../README.md) first. It shows extraction, the
starter/practice folder layout, opening VS Code, installing and trying skills, and your first output.

## 1. Find the right place to type

1. In VS Code, use **File > Open Folder** to open your approved practice folder.
2. Press **Ctrl+Shift+P**, type **Claude Code**, and choose **Open in New Tab** if offered.
   Use the installed extension's existing panel if it is already open.
3. Click Claude's message box. Paste the lesson's prompt there and send it once.
   **Shift+Enter** adds a line without sending.

The Command Palette searches VS Code actions; it is not a shell or a Claude conversation.
Menu names and controls depend on the installed version. Use the actual available choices.
[Official extension guide](https://code.claude.com/docs/en/vs-code).

| Place | What goes there | Example |
| --- | --- | --- |
| Browser showing GitHub | Read the lesson; copy a prompt | The page you are reading |
| Claude message box | Plain-English requests and offered slash commands | `Explain this formula in plain English.` |
| VS Code file editor | Contents of a file you intend to save | Your local project `CLAUDE.md` |
| Windows File Explorer | Copy files and folders; enter folder paths | `%USERPROFILE%\.claude` in its address bar |
| Integrated terminal | Only an explicitly labeled command exception | The optional procedure below |

**Check:** Lesson 1's invented $200/$210 explanation appears as a conversation. If you see a
PowerShell error or accidentally typed in a document, return to Claude's message box. Do not
save the accidental text over an existing document.

## 2. Use only the input needed now

For lessons, copy the complete example from its prompt box. For an approved file task, select
the intended file through the `@` picker. Confirm its name before sending. Selecting a workbook
does not prove a spreadsheet reader or calculation engine is available.

Read proposals before approving changes. Check the input, new output, and requested action.
Claude can run a tool or shell command from the extension; that does not require you to move your
conversation into a terminal. Review the action just as you would a proposed file change.

## 3. Check usage on the organization's website

Open the usage page supplied by your administrator in your normal browser and bookmark it locally.
Do not put its address, account details, or a filled usage record in this public repository.

Before the first exercise, note the displayed unit (tokens, money, or another allowance), period,
used/remaining amount, reset date if shown, and update time. After one completed exercise, refresh
and compare the same period and unit. Reporting can lag; a zero change is not proof of a free task.
Ask the administrator if the display or reset rules are unclear. Do not invent a conversion.

The extension's `/usage` dialog requires a claude.ai sign-in and is not offered for third-party
providers. Context fullness and session cost estimates are different from the organization's
remaining allowance. A missing `/usage` command is not a reason to change a working login.
[Account and usage documentation](https://code.claude.com/docs/en/vs-code#check-account-and-usage).

## 4. Keep the model choice simple

Keep the approved workplace default for the first lesson. If model selection is permitted, the
model control or **Switch model** command shows the offered choices; effort appears only where
supported. Do not edit connection settings to obtain a missing model.

Our suggested progression is the default or Sonnet for ordinary guided work, optional Haiku for
simple wording, and optional Opus for a specific difficult question after narrowing it. No lesson
requires an additional model family. If only one model works, reduce the size of the next step.
Higher effort can cost more and take longer; it does not replace checks. Leave it unchanged for
the first lesson. Later use [the model guide](../docs/MODELS-AND-USAGE.md) for task-based choices.

## 5. Know whether to wait, respond, or stop

A gateway alone does not establish how fast a task will run. Model, reasoning, input size, tools,
network conditions, and service limits can affect elapsed time. This guide promises no response
time. Work through one small request at a time and read the next lesson section while it runs.

| What you see | What to do |
| --- | --- |
| An approval card or question | Read it and respond to the specific request; waiting will not answer it |
| Ongoing activity with no error | Let this request continue; do not send duplicates or open parallel copies |
| More work than you intended | Use the visible Stop control, then inspect any outputs before resuming |
| A timeout or connection error | Check whether a partial output exists; do not assume failure means nothing changed |
| A rate-limit, budget, or access error | Follow the organization's reset/support instructions; do not retry in a loop or change credentials |
| No progress beyond what is normal for your setup | Check for hidden approvals and known service issues; stop if needed, preserve the last result, and seek support |

After a stopped or failed request, use this in the same conversation when the service is ready:

```text
Resume only the unfinished part of this task. First check the agreed output locations for
partial results. State what is complete and what remains unverified. Reuse completed checks
where their inputs are unchanged. Do not rerun the entire task or overwrite partial work blindly.
```

For a very large task, begin with a schema or sheet map and one clearly bounded output. A sample
can help plan the method; full-data controls are still needed for a final reconciliation.

## 6. Use the terminal only for a named exception

Reading lessons, chatting, copying local skills, and editing instruction files need no shell
commands. An optional dependency or a feature absent from the extension may require one. If you
are not comfortable, leave that optional step pending and use the supported text exercise.

Before running a command, have its provider explain the purpose, exact shell, working folder,
changes, expected result, and how to undo changes. Never paste an unexplained command.

1. In VS Code, choose **Terminal > New Terminal**.
2. Check the selected terminal profile. These guides use **PowerShell on Windows** for shell
   exceptions unless explicitly labeled otherwise. Do not translate Bash commands yourself.
3. Confirm the current folder is the intended project. `Get-Location` is a read-only PowerShell
   check. If it is wrong, stop and get the exact approved folder-switch instruction.
4. Run only the reviewed command in the stated shell. Check its output before doing another step.
5. Return to the Claude panel for the lesson. Closing the terminal panel does not undo commands.

A Claude slash command such as `/plugin` belongs inside a supported Claude session, not directly
at a `PS ...>` PowerShell prompt. The extension working does not prove the separate `claude`
terminal command is installed or inherits the same gateway. If a terminal Claude session is
required, have IT confirm both before launching it. Do not run a new installer or sign in to a
personal account to make an optional step work.
[VS Code terminal basics](https://code.visualstudio.com/docs/terminal/getting-started).

## Get help without starting over

Paste this into the extension when a guide step is confusing:

```text
Guided mode. I am following [GUIDE FILE AND STEP]. I see [NEUTRAL DESCRIPTION].
The expected result was [CHECK]. Help me with just the next action in the VS Code extension
or Windows File Explorer. Use what I already supplied; ask one question if needed.
Explain unfamiliar terms. If a terminal is necessary, explain why and identify the exact shell
and expected result before giving a command. Preserve my working provider configuration.
```

If Claude itself cannot respond, send your organization's support contact the step, versions,
time, and approved redacted error through the approved support channel. Do not publish raw logs.
At each stopping point, keep a local note: **last completed step, check result, next step**.

Next: **[First conversation](../learn/01-first-conversation.md)** or return to **[setup](../START-HERE.md)**.
