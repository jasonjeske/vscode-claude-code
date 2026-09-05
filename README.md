# Set up Claude Code in VS Code, step by step

![Claude Code for property-tax work: Excel, research, and reporting, illustrated with a spreadsheet, source document, charts, and buildings.](assets/readme-banner.png)

Use this guide to set up two starter skills and make your first checked result for accounting,
Excel, property-tax research, and reporting. **Keep this page open in your browser and follow
steps 1-9 in order. All first-time setup instructions are on this page.**

You need a Windows PC with **Visual Studio Code and its Claude Code extension already connected
through your approved workplace setup**. Keep that connection and its model settings. If the
extension is missing or cannot connect, use your organization's support process before continuing.
No personal Claude subscription, GitHub account, Git, or terminal is required for this walkthrough.

The ZIP contains files to copy and read. There is no program inside it to run. We will keep the
extracted starter as a reference and create a separate practice folder for the exercise. Use
permitted local storage and invented data; keep real work and credentials out of this public kit.
Files read by Claude are processed by your configured provider.

**Your route:** open VS Code → download and extract → make a practice folder → open it in VS Code
→ save instructions → copy two skills → try a skill → create and check a result.

## 1. Open Visual Studio Code

**Where: Windows Start, then VS Code.**

1. Open Windows Start, type **Visual Studio Code**, and open that application.
2. Leave VS Code open. You will select your practice folder in step 5 after creating it.
3. Keep this guide open in your browser. Use **Alt+Tab** to switch between the guide and the
   applications named in each step.

**Check:** Visual Studio Code is open. Microsoft Visual Studio is a different application.
Do not paste anything into a terminal. **Next: step 2 below.**

## 2. Make a folder for the download and practice files

**Where: Windows File Explorer.** This is the Windows folder application, separate from the file
list called Explorer inside VS Code.

1. Press **Windows+E**. Navigate to a location approved for learning files by your organization.
2. Choose **New > Folder**, or right-click empty space and choose **New > Folder**.
3. Name it `Claude-Learning` and open it. If that name already exists, use a new unused name,
   such as `Claude-Learning-02`. Do not replace an existing folder.
4. Click the address bar at the top and copy this folder's full path. You will paste it into the
   extraction dialog in step 3. Keep this File Explorer window open.

**Check:** File Explorer is inside the new, empty learning folder. The names in this guide are
examples; use your actual location. **Next: step 3 below.**

## 3. Download the ZIP and extract its files

**Where: your browser, then Windows File Explorer.**

1. Click **[Download the starter ZIP](https://github.com/jasonjeske/vscode-claude-code/archive/refs/heads/main.zip)**.
   Wait for the download to finish.
2. Open your browser's downloads list and choose **Show in folder** for the ZIP.
3. Right-click that ZIP and select **Extract All**.
4. In the destination field, paste the learning folder path from step 2. Select **Extract**.
5. Open the extracted `vscode-claude-code-main` folder. If there is an extra enclosing folder,
   keep opening until you see `README.md`, `START-HERE.md`, `skills`, `setup`, and `templates`
   together. This is the **starter folder**. Leave all of its contents together.

**Check:** you see those files in an ordinary folder, outside the `.zip` file. Merely opening
or double-clicking the ZIP does not complete extraction. **Next: step 4 below.**

## 4. Create your practice folder

**Where: Windows File Explorer.**

1. Go back to the `Claude-Learning` folder from step 2. You can paste its path into the address bar.
2. Choose **New > Folder**, name it `Practice-01`, and open it. Use another unused name if needed.
3. Inside `Practice-01`, choose **New > Folder** four times to make these four separate folders:
   `inputs`, `working`, `outputs`, and `evidence`.

Your folders should now look like this:

```text
Claude-Learning/
  vscode-claude-code-main/      downloaded starter; leave its files together
    README.md
    START-HERE.md
    skills/
    setup/
    templates/
    ...                        keep the other downloaded files too
  Practice-01/                 your new practice folder, outside the starter
    inputs/
    working/
    outputs/
    evidence/
```

**Check:** the two folders are separate. `Practice-01` is where you will work in VS Code.
Its four subfolders are empty. **Next: step 5 below.**

## 5. Open Practice-01 in VS Code

**Where: VS Code.** Switch back to the application you opened in step 1.

1. Choose **File > Open Folder**.
2. Navigate to `Claude-Learning`, select **Practice-01**, and choose **Select Folder**.
3. If a Workspace Trust question appears, follow your organization's policy for this folder.
4. Choose **View > Explorer** to show the file list on the left.

**Check:** the file list shows `Practice-01` with `inputs`, `working`, `outputs`, and `evidence`.
If you see `skills` and `templates`, you selected the starter instead; repeat **File > Open Folder**
and select `Practice-01`. Keep this same practice folder open for the rest of the walkthrough.
**Next: step 6 below.**

## 6. Save the practice instructions in the file editor

**Where: VS Code's file editor.** This step creates a text file; it is not a message to Claude.

1. Choose **File > New Text File**.
2. Paste the following into that new file:

```markdown
# Practice project

Use invented examples only. Help me learn Claude Code through one useful checked result.
Use only files and facts named in my request. Preserve existing files and gateway settings.
Explain one unfamiliar operation briefly and give me one check I can do myself.
Create only the new output I request. Do not overwrite an existing file, install tools,
read unrelated folders, or make filing, posting, or payment decisions.
```

3. Press **Ctrl+Shift+S** for Save As. Choose your `Practice-01` folder.
4. Name the file exactly **CLAUDE.md**. If a file-type filter is offered, choose **All Files**.
   Save it. Do not replace an existing file.
5. Click `CLAUDE.md` in VS Code's Explorer to reopen it and check the text.

**Check:** `CLAUDE.md` appears beside `inputs`, `working`, `outputs`, and `evidence`. It is not
inside one of them and is not named `CLAUDE.md.txt`. Claude Code uses this file for instructions
in this project. A global instruction file is a later option; this exercise needs only this one.

If project instruction files are blocked, leave this step pending and continue only with the
permitted text exercise. **Next: step 7 below.**

## 7. Copy the two starter skills into Claude's skills folder

**What this does:** a skill supplies reusable task instructions. `prompt-coach` helps write a
clear request; `excel-workbook-review` guides inspection of a workbook before edits. These two
bundled skills require no installer. They do not provide an Excel engine or new data access.

This walkthrough uses **personal scope**, so the skills are available to your Claude Code projects
on this Windows account. Follow these copies only if that location is permitted. If it is managed
or blocked, leave installation pending; do not change permissions. Step 8 includes a plain-chat fallback.

### A. Find and read the source files

**Where: Windows File Explorer, then VS Code.**

1. In File Explorer, return to the extracted starter from step 3 and open its **skills** folder.
   You should see folders named `prompt-coach`, `excel-workbook-review`, and four others.
2. In VS Code, choose **File > Open File**. Navigate to that starter's
   `skills > prompt-coach > SKILL.md` and open it. Read the instructions.
3. Repeat **File > Open File** for `skills > excel-workbook-review > SKILL.md` and read it.
   These are reference files. Do not edit them or choose **Open Folder** here.
4. Close those two reference tabs using each tab's **X**. Your workspace remains `Practice-01`.

### B. Create the destination

**Where: Windows File Explorer.**

1. Press **Windows+E** to open another File Explorer window. Keep the source window from A open.
2. Click the new window's address bar, type **`%USERPROFILE%`**, and press **Enter**.
   Windows expands this to your user folder. This text belongs in the address bar, not in Claude.
3. Find and open the **`.claude`** folder. If it is absent and local configuration is permitted,
   use **New > Folder** to create `.claude`, including its leading dot, then open it.
4. Inside `.claude`, open **skills**. If absent, create a folder named `skills` and open it.
   Leave any other files or folders in `.claude` unchanged.

### C. Copy complete folders

**Where: the two Windows File Explorer windows.**

1. In the destination window, check whether `prompt-coach` or `excel-workbook-review` already exists.
   If either exists, do not merge or replace it. Skip that copy and check discovery in step 8.
   An existing copy may differ; updating it is a separate task after setup.
2. In the source window, click the **prompt-coach folder once**, then press **Ctrl+C**.
3. Switch to the destination window, inside `%USERPROFILE%\.claude\skills`, and press **Ctrl+V**.
4. Repeat for the complete **excel-workbook-review folder**. Do not copy the starter's entire
   `skills` folder or just a loose `SKILL.md` file. If Windows asks to replace files, cancel.
5. Open each newly copied folder in the destination. Confirm it contains `SKILL.md`.
   In VS Code, use **File > Open File** to read each destination `SKILL.md` and confirm it matches
   the source you reviewed in A. Close the reference tabs afterward.

**Check:** the destination paths have exactly this shape:

```text
%USERPROFILE%\.claude\skills\prompt-coach\SKILL.md
%USERPROFILE%\.claude\skills\excel-workbook-review\SKILL.md
```

They must not contain an extra `skills\skills` or `prompt-coach\prompt-coach` layer.
The starter's original files remain in the extracted folder. Your practice folder is still open
in VS Code. **Next: step 8 below.**

## 8. Open Claude Code in VS Code and try Prompt Coach

**Where: VS Code, with Practice-01 still open.**

1. Press **Ctrl+Shift+P**. In the Command Palette, type **Claude Code** and choose an option such
   as **Open in New Tab**. The panel should be labeled **Claude Code**.
2. Start a **new conversation** using the panel's new-session control if a previous conversation
   is displayed. Keep the approved connection and model. If an unexpected login appears, stop
   and use workplace support; do not replace the working gateway with a personal account.
3. In your browser, check the usage website supplied by your organization. Note the current usage
   privately. Return to VS Code. The exercise makes two small requests, one here and one in step 9.
4. Click **Claude's message box**, type `/excel-workbook-review`, and look for that skill in the
   suggestions. This checks discovery only. Clear the text without sending a request.
5. In the same message box, type `/prompt-coach` and select the matching skill from the suggestions.
   Add the text below to the message, then send it once. **Shift+Enter** adds a line without sending.

**Paste after selecting `/prompt-coach`:**

```text
Help me write a short request for an exception note. Use these invented facts only:
the book amount is $200 and the bill amount is $210 for the same stated property and tax year.
The cause is unknown. I want Bill minus Book, the unresolved cause, and one next source check.
Draft the request only. Do not open files, create the note, browse, or install anything.
Teach me one thing that makes this request clear.
```

**Check:** Claude returns a draft request and one brief explanation. It should not claim to have
reviewed a workbook or created the note. `excel-workbook-review` is ready for a later workbook task;
seeing it in the menu does not prove that workbook-reading tools work.

**If a skill is missing:** check the exact paths in step 7, then close and reopen VS Code, reopen
`Practice-01`, and start a fresh Claude conversation. If still missing or copying was blocked,
send the same text as an ordinary message without a slash command. Mark skill installation pending.
The text exercise can continue; a plain-chat answer is not proof the skill was installed.

**While waiting:** check whether Claude needs your answer or an action approval. Send the request
only once. If a request errors or stops, inspect what it completed before retrying. Do not change
models or connection settings to troubleshoot this exercise. **Next: step 9 below.**

## 9. Create, open, and check your first result

**Where: the same Claude Code conversation in VS Code.** Keep `Practice-01` open.
Prompt Coach wrote a request; now you will ask Claude to perform the task. Use this supplied version
for a known checkable result. **Paste into Claude's message box as a normal request, without a slash command:**

```text
Guided mode. Use these invented facts only: the book amount is $200 and the bill amount is $210
for the same stated property and tax year. The cause of the difference is unknown.
Create a new outputs/first-exception-note.md with the facts, Bill minus Book calculation,
unresolved cause, and one next source check. Do not overwrite an existing file. Do not decide
any payment or posting, browse, install tools, or read unrelated files.
Explain briefly what you created and tell me how to open and check it in VS Code.
If creating files is blocked, provide the note in chat and say it was not saved.
```

1. Send the request once. If an action approval appears, check that it concerns the intended new
   file in `outputs` before approving. Whether an approval appears depends on the managed mode.
2. When Claude finishes, choose **View > Explorer** in VS Code. Expand **outputs** and click
   **first-exception-note.md**. If the response says it was not saved, check the chat note instead.
3. Check **210 - 200 = +10** yourself. The cause must remain unknown, and the note must not tell you
   to post or pay the difference. These invented facts establish no real tax treatment.
4. Check your organization's usage website again after its reporting delay. Compare the same unit
   and reporting period. A delayed or unchanged reading does not establish that the task was free.

**Done:** you opened a work folder, saved project instructions, checked skill discovery, sent a
request in the extension, and inspected a result. If a step was blocked, keep it marked pending.
No real workbook or additional Office tools were needed for this first result.

**Next time:** open VS Code → **File > Open Folder > Practice-01** → open **Claude Code** through
**Ctrl+Shift+P** → start a conversation for your next task. Your saved file stays in `outputs`.
If you repeat this exercise, request a new filename such as `first-exception-note-02.md`.

## After setup: use this for your work

**Next recommended page: [learn by doing one useful task](LEARN.md).** It helps you apply the same
request, result, and check method to approved work. Keep real work in a separate approved project.

These are references for later; none is another prerequisite for steps 1-9:

| When you need it | Reference |
| --- | --- |
| Start an actual work project | [Project folders and instruction templates](setup/PROJECTS.md) |
| Reuse guidance across projects | [Optional global instructions](setup/GLOBAL-INSTRUCTIONS.md) |
| Understand another skill and try its example | [Skill catalog](SKILLS.md) |
| Add Excel editing, Office, or a community package | [Additional skill installation](setup/SKILLS.md#upstream-skills-and-plugins) |
| Update, remove, or troubleshoot a skill | [Skill maintenance](setup/SKILLS.md) |
| Copy a task-specific request | [Prompt library](prompts/PROMPT-LIBRARY.md) |
| Get help with the panel or usage | [VS Code desk guide](guides/00-use-vscode.md) |
| Explore the included dashboard | [Local example and answer key](examples/dashboard/README.md) |

The bundled workbook-review skill supplies a procedure. Creating or editing Excel files requires
suitable approved tools; advanced formulas, PivotTables, VBA, and Power Query need native Excel
checks. The linked Anthropic Office and community packages are separate choices with their own
licenses and runtime requirements. Install one when the task calls for it.

<details>
<summary>Sources, verification, and repository information</summary>

This is an independent public starter kit. The first-run instructions use documented
[Windows extraction](https://support.microsoft.com/en-us/windows/experience/storage-filemanagement/zip-and-unzip-files),
[VS Code file controls](https://code.visualstudio.com/docs/getstarted/userinterface),
[Claude Code extension controls](https://code.claude.com/docs/en/vs-code), and
[skill locations](https://code.claude.com/docs/en/skills).
Menu names can vary by installed version and organizational policy.

Repository links, skill frontmatter, merge fixtures, and synthetic dashboard calculations have
automated checks. Actual Windows/Claude skill operation and native Excel behavior remain unverified.
See the [validation record](docs/TOOLKIT-VALIDATION.md) and [Windows checklist](docs/WINDOWS-VERIFICATION.md).

The [full onboarding reference](setup/FULL-ONBOARDING.md) is for a fresh or uncertain installation,
not another step in this walkthrough. See [CONTRIBUTING](CONTRIBUTING.md) for maintenance and
[LICENSE](LICENSE) for terms; third-party materials retain their own licenses.

</details>
