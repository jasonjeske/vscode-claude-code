# Quick help for the Claude Code extension

[Full course](README.md) · [Restart and recovery lesson](README.md#10-restart-and-recover)

[Download the bonus cheat sheet (PDF, 6 pages)](https://raw.githubusercontent.com/jasonjeske/vscode-claude-code/main/output/pdf/claude-code-vscode-cheat-sheet.pdf)
for GUI controls, skills, short commands, and copyable Office work prompts.

## Open Claude's message box

Press **Ctrl+Shift+P** (Mac: **Cmd+Shift+P**). Type **Claude Code** and select
**Open in New Tab**. Click its message box before pasting a work request.

## Reload the window

1. Save your text files with **Ctrl+S** (Mac: **Cmd+S**).
2. Open the Command Palette with **Ctrl+Shift+P** (Mac: **Cmd+Shift+P**).
3. Copy this into the **Command Palette**, select the result, and wait:

```text
Developer: Reload Window
```

4. Reopen Claude. Start a fresh conversation to test new skills, or use Session history
   to resume earlier work. Your saved files remain in the work folder.

## Restart the whole app

Save your work, then close every VS Code window. On Mac use **Code > Quit Visual Studio Code**.
Reopen VS Code from Start or Applications, then **File > Open Recent > your work folder**.

## Ask for one clear next step

Copy into the **Claude Code message box**:

```text
I'm stuck. Ask me one question to identify where I am.
Give me one step, the exact place to click or type, and a success check.
```

If the output was not saved:

```text
Please do the task and save the finished file using available tools.
If something is missing, give me a short IT request. Do not claim success.
```

## Find and open your files

Use **View > Explorer** in VS Code. Copy input files into the open work folder using
Windows File Explorer or Mac Finder. Name the file in your request. Hold Shift while
dragging it into Claude's message box if you want to attach a reference.

Open finished **.xlsx** files in Excel, **.docx** in Word, **.pptx** in PowerPoint,
**.pdf** in a PDF reader, and **.html** in a browser through File Explorer/Finder.
Use VS Code for text and **.md** notes. Saving a note does not send it to Claude.

## If a number is wrong

Copy into Claude:

```text
Trace this number to the source rows before making more changes.
Explain the mismatch, correct it, and recheck every report that uses it.
```

## If tools, sign-in, or updates are blocked

Use your company-approved connection. Keep the error text and ask IT.
For an extension update, open Extensions, find Claude Code by Anthropic, and apply
Update if offered. For plugin and personal-skill updates, follow lesson 10.
Do not uninstall working tools, remove your adaptations, or bypass managed settings.
