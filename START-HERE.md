# Start here: from the ZIP to your first result in VS Code

Keep this page open in your browser. Follow steps 1-7 on the PC. **There is no installer or program
to run inside the ZIP:** it contains guides, templates, skills, and examples. You will open an
extracted folder in **Visual Studio Code (VS Code)** and use its **Claude Code extension**.
Visual Studio Code is the application used here; Microsoft Visual Studio is a different product.

This path assumes VS Code and its Claude Code extension already work through the approved workplace
gateway. Keep that configuration. No Git, cloning, terminal, GitHub account, or personal Claude
subscription is required. If the extension is missing or cannot connect, use the organization's
support process before continuing. Use only permitted local folders and invented data in this walkthrough.

## 1. Make a place for the learning files

**In Windows File Explorer:**

1. Press **Windows+E** to open File Explorer, then navigate to a location approved for learning files.
   Use the location your organization provides; do not guess that Downloads or a personal cloud folder
   is approved work storage.
2. Choose **New > Folder** (or right-click empty space and choose **New > Folder**).
3. Name the new folder `Claude-Learning` and open it. If that name already exists, choose a new
   unused name, such as `Claude-Learning-02`; do not replace an existing folder.
4. Click the address bar and copy the folder's path for your own use in the extraction dialog.

**Check:** File Explorer is inside your new learning folder. Keep that window open.
The names below are examples; use the actual folder you just created.

## 2. Download and extract the starter into that location

**In your browser, then Windows File Explorer:**

1. [Download the starter ZIP](https://github.com/jasonjeske/vscode-claude-code/archive/refs/heads/main.zip).
   Alternatively, open [the repository home page](https://github.com/jasonjeske/vscode-claude-code),
   select **Code > Download ZIP**, and wait for the download to finish.
2. Open your browser's downloads list and choose **Show in folder** for the downloaded ZIP.
3. Right-click the ZIP and select **Extract All**. In the destination field, paste the path of
   your new `Claude-Learning` folder from step 1, then select **Extract**.
4. In File Explorer, open the extracted `vscode-claude-code-main` folder. If there is an extra
   enclosing folder, keep opening until you see `README.md`, `START-HERE.md`, `setup`, `skills`,
   and `templates` together. **That is the starter folder.**

**Check:** you can open `START-HERE.md` from an ordinary extracted folder. You are not browsing
inside a file ending in `.zip`. Do not move individual files out of the starter; its folder
structure is already included. [Microsoft's extraction instructions](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/zip-and-unzip-files).

## 3. Create a separate practice folder and its subfolders

**In Windows File Explorer:**

1. Return to the `Claude-Learning` folder you created in step 1. You can paste its saved path into
   the address bar. Stay outside the extracted starter folder.
2. Choose **New > Folder**, name it `Practice-01`, and open it.
3. Inside `Practice-01`, create four folders one at a time using **New > Folder**:
   `inputs`, `working`, `outputs`, and `evidence`.

Your layout should resemble this. An extra wrapper around the extracted starter is harmless;
what matters is finding its contents and keeping practice separate:

```text
Claude-Learning/                 the location you created
  vscode-claude-code-main/       extracted reference kit; already populated
    README.md
    START-HERE.md
    setup/
    skills/
    templates/
    ...                         other downloaded files; keep them
  Practice-01/                  the separate folder you create
    inputs/                     approved source copies later
    working/                    calculations or scripts later
    outputs/                    new results
    evidence/                   checks and source notes
```

**Check:** `Practice-01` is outside the starter, and its four folders are empty. No work records
are needed yet. The starter is a reference library; the practice folder is where your exercise goes.

## 4. Open the starter in Visual Studio Code

**In the VS Code application:**

1. Open **Visual Studio Code** from Windows Start.
2. Choose **File > Open Folder**. Navigate to the extracted starter folder from step 2 and select it.
3. If a Workspace Trust question appears, read it and follow workplace policy for the reviewed
   download. Do not bypass a managed restriction.
4. Choose **View > Explorer** to see the files. Open `START-HERE.md` by clicking it in that list.

**Check:** VS Code's Explorer lists `START-HERE.md`, `setup`, `skills`, and `templates`. It should
not show your whole Downloads folder or the shared `Claude-Learning` parent. Opening one Markdown
file alone is not the same as opening its containing folder.
[VS Code interface reference](https://code.visualstudio.com/docs/getstarted/userinterface).

## 5. Open Claude Code in that same VS Code window

1. Press **Ctrl+Shift+P** to open VS Code's Command Palette. Type **Claude Code** and choose
   **Open in New Tab** if offered. Use the existing Claude Code panel if it is already open.
2. Confirm the panel is **Claude Code**, not a different chat extension. Keep the working provider
   and model. Do not switch to a personal login if an account screen unexpectedly appears.
3. Click **Claude's message box**. Type `@START-HERE.md` and select the local file from the suggestions.
4. Paste this short request into that same message and send it once:

```text
Read only the attached local START-HERE.md. In two sentences, explain what this starter is for
and which folder is for practice. Do not perform its setup steps or change any files.
```

**Check:** Claude describes the guide and separate practice folder from the file. If the file
cannot be selected or read, return to step 4. Copying a prompt from GitHub does not attach its files.
If Claude is waiting or shows an error, use [wait, respond, or stop](guides/00-use-vscode.md#5-know-whether-to-wait-respond-or-stop).
[Official Claude Code panel and file references](https://code.claude.com/docs/en/vs-code).

## 6. Switch VS Code to your practice folder and save its instructions

You have confirmed Claude can read the starter. Now switch to the folder where the exercise belongs.

1. In VS Code, choose **File > Open Folder** again. Select `Practice-01`, not the starter or their parent.
2. Check Explorer now shows `inputs`, `working`, `outputs`, and `evidence` under `Practice-01`.
3. Choose **File > New Text File**, then paste the following into the **file editor**:

```markdown
# Practice project

Use invented examples only. Help me learn Claude Code through one useful checked result.
Use only files and facts named in my request. Preserve existing files and gateway settings.
Explain one unfamiliar operation briefly and give me one check I can do myself.
Create only the new output I request. Do not overwrite an existing file, install tools,
read unrelated folders, or make filing, posting, or payment decisions.
```

4. Press **Ctrl+Shift+S** for Save As. Navigate to `Practice-01` and name the file exactly `CLAUDE.md`.
   If the dialog offers a file-type filter, select **All Files**. Do not replace an existing file.
5. Check that `CLAUDE.md` appears beside the four folders, not inside `inputs` and not as `CLAUDE.md.txt`.
   Click it in Explorer and confirm its contents. If local instruction files are blocked, skip the
   save and use the text exercise in chat within the approved scope.
6. Open the Claude Code panel using step 5's Command Palette method **in this practice window**.
   Start a fresh conversation for the exercise.

**Check:** the active workspace is `Practice-01`. The instructions were typed in the file editor;
the request in the next step belongs in Claude's message box. They are different places to type.

## 7. Make, open, and check your first result

Check your organization's usage website before the task, keeping its address and account details
private. Use the approved default model. In the practice folder's **Claude Code message box**, paste:

```text
Guided mode. Use these invented facts only: the book amount is $200 and the bill amount is $210
for the same stated property and tax year. The cause of the difference is unknown.
Create a new outputs/first-exception-note.md with the facts, Bill minus Book calculation,
unresolved cause, and one next source check. Do not overwrite an existing file. Do not decide
any payment or posting, browse, install tools, or read unrelated files.
Explain briefly what you created and tell me how to open and check it in VS Code.
If creating files is blocked, provide the note in chat and say it was not saved.
```

1. Read any proposed action or permission request. It should concern the new file in `outputs`.
   Approve only the intended action. Wait for completion; do not send the request repeatedly.
2. In VS Code's Explorer, expand `outputs` and click `first-exception-note.md` to open it.
   If Claude could only reply in chat, inspect that reply instead; do not assume a file exists.
3. Check **210 - 200 = +10** yourself. The cause must remain unknown. These invented facts do not
   establish any real tax treatment. Compare the rest of the note with the supplied facts.

**Done:** you have selected a workspace, created instructions, sent a request through the extension,
and inspected an output. No Excel engine or additional skill was required for this text task.
Check gateway usage again after its reporting delay. Continue with [today's useful work](LEARN.md),
using only employer-approved inputs and storage. Do not copy actual work into the public starter.

## What to do next

- Want help with a particular work task? Go to [LEARN.md](LEARN.md); the six task skills are optional.
- Want to reuse your preferences across projects? Use **Optional A** below.
- Want the first task skills? Use **Optional B**, or the assisted-copy alternative at the end.
- Want actual workbook editing? Read **Optional C** when that task needs the approved tools.
- Stopping here? Keep the last completed step, checks, and next action in the blank
  [setup receipt](templates/SETUP-RECEIPT.md), saved in approved storage outside the starter.

For future work folders, [project setup](setup/PROJECTS.md) explains how to adapt the structure.
The [full onboarding reference](setup/FULL-ONBOARDING.md) is for a fresh or uncertain installation;
it is not an extra required lesson. Menu names may differ by version. The Windows walkthrough
has been checked against documentation, not executed on your managed PC.

## Optional A. Add a small global instruction file

Read [GLOBAL-CLAUDE.md](templates/GLOBAL-CLAUDE.md). Its job is to set concise explanations,
teaching mode, preservation rules, and the work boundary across projects.

1. In **Windows File Explorer's** address bar, enter `%USERPROFILE%\.claude`.
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

**Check:** the saved file is named exactly `CLAUDE.md`, and any predecessor has a readable backup.
If the location is managed or blocked, leave it unchanged and continue with the text lessons.

## Optional B. Add the first local skills

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

**Check:** the skill helps draft a request. If discovery is blocked, use the same request as plain
chat and mark skill installation pending. You can still learn the workflow.

## Optional C. Add Excel tools when there is a task for them

**Optional, later.** You can finish setup and the text-based lessons without this step.

The local workbook-review skill provides an inspection procedure. For spreadsheet creation and
editing, evaluate Anthropic's **xlsx** skill. Its Office bundle is linked, not redistributed here.
Check its license, required Python/Office tooling, and approved installation route in
[the upstream setup section](setup/SKILLS.md#upstream-skills-and-plugins).

Do not promise that installing a skill enables native PivotTables, VBA, Power Query refresh, or
all formula calculations. Test a small copy in native Excel before changing a complex workbook.
Add PDF for notices, Word/PowerPoint for deliverables, and dashboard/design tools when needed.

## Prefer Claude to help with the copying?

This is an **alternative to manually copying the files in Optional A and B**. If you already completed
those optional steps, skip this section. Use it only when local instruction/skill installation is permitted.

**A prompt copied from this web page does not give Claude the repository's files.** First put the
starter on the PC and open it in VS Code. You do not need to clone a repository or use a terminal.

1. Open [this repository's home page](https://github.com/jasonjeske/vscode-claude-code) and choose
   **Code > Download ZIP**, or [download the ZIP directly](https://github.com/jasonjeske/vscode-claude-code/archive/refs/heads/main.zip).
2. In Windows File Explorer, right-click the ZIP, select **Extract All**, and open the extracted
   folders until you see `START-HERE.md` beside `README.md`, `setup`, `skills`, and `templates`.
3. In VS Code, choose **File > Open Folder** and select **that folder**, not the ZIP, its parent,
   or a work-data folder. Confirm `START-HERE.md` appears at the top level of VS Code's Explorer.
4. Open Claude Code in **that same VS Code window** and start a fresh conversation. An existing
   conversation in another project is not the place to run this setup request.
5. In Claude's message box, type `@START-HERE.md` and select the local file from the suggestions.
   Add a second reference by typing `@setup/SKILLS.md` and selecting that file. If they do not
   appear, return to step 3 of this assisted-copy list; do not paste the prompt into an unrelated project.
6. With both references selected, paste the following request into the same message and send it
   once. A typed filename alone is not confirmation that the file was attached or read.

These references point Claude at the local instructions. The folder also contains the template
and complete skill folders it needs to copy. [Official file-reference instructions](https://code.claude.com/docs/en/vs-code#reference-files-and-folders).

**Paste into the Claude Code message box, not a terminal:**

```text
I am setting up a downloaded copy of https://github.com/jasonjeske/vscode-claude-code.
The URL identifies the source; it does not mean the files are available locally.
Use the local START-HERE.md and setup/SKILLS.md references attached to this message.
Before proposing changes, confirm they are readable and identify their shared starter root.
Check these exact source paths within that root:
- templates/GLOBAL-CLAUDE.md
- skills/prompt-coach/SKILL.md
- skills/excel-workbook-review/SKILL.md
If either reference or a required source is missing, stop without changing anything. Tell me
which download/open-folder/reference step is needed. Do not search my computer, guess file
contents, fetch a replacement, or install anything to work around missing source files.

Read only the two setup documents and the selected template/skill sources needed for this task.
My workplace Claude Code and gateway already work. Help me add the global instruction template,
prompt-coach, and excel-workbook-review in personal scope. Use no work data and keep my
provider/settings unchanged.
First inspect only the selected source files and whether the exact destinations exist. If existing
instructions or same-name skills need reading, confirm their approved scope before reading.
Show the precise proposed copies/merge and backup plan together. Wait for my approval of that
batch, then perform only those changes, verify readback, and report the actual results.
Ask one question only when an unresolved choice changes the result. Do not install upstream
packages, run agents, scan my computer, or overwrite existing content without the reviewed plan.
```

**Check before approving:** Claude identifies the local starter folder, reports whether the five
named files were found, and shows the proposed destination files and backup plan. It has not copied
anything yet. A reply that merely recognizes the GitHub URL is not enough.

If file references or local copying are blocked, use the manual instructions in Optional A and B where
permitted, or leave installation pending and ask your organization's support contact. Do not change
the gateway or enable a new connection. The text exercises in [LEARN.md](LEARN.md) remain usable.

This is an instruction-guided procedure, not a tested Windows installer. Tool approval and managed
policy still apply. Approval of one reviewed batch is enough for that batch; changed scope needs a
new decision.
