# VS Code fundamentals for working with Claude

Use the [README first session](../README.md) for setup and the first exercises. This is a desk
reference for the editor operations you will reuse. You do not need programming or terminal skills.
All keys below are Windows defaults; managed settings or extensions can change them.

## 1. Understand the window

VS Code is the application. Claude Code is one extension inside it. Your project files live on
disk; a chat is a conversation about the selected work. Closing a tab does not delete a file.

| Area | How to reach it | What belongs there |
| --- | --- | --- |
| Explorer | **View > Explorer** | The open project's files and subfolders |
| Editor | Double-click a file in Explorer | Text you want to save, such as a Markdown request |
| Command Palette | **Ctrl+Shift+P** | Search for a VS Code action such as opening Claude |
| Quick Open | **Ctrl+P** | Find a file by name within the open workspace |
| Claude Code | Command Palette > type **Claude Code** > an offered open-panel command | Requests, selected file references, and skill commands |
| Extensions | **Ctrl+Shift+X** | See installed VS Code extensions and their publishers |
| Terminal | **Terminal > New Terminal**, only for an explained exception | Shell commands, never ordinary task notes |

An extension that renders Markdown changes the editor's presentation. A Claude skill changes the
procedure Claude uses. They are installed in different places. Neither implies a database connection.
[VS Code's interface documentation](https://code.visualstudio.com/docs/getstarted/userinterface).

**Try:** open Explorer and double-click the practice project's `CLAUDE.md`. Close its tab with **X**.
Reopen it from Explorer. **Check:** closing the tab did not remove the file. Next, find a nested file.

## 2. Find a file and understand its path

1. In Explorer, click the arrow beside **prompts** to expand it.
2. Double-click **example-task.md**. The path is `prompts/example-task.md`.
3. Click the arrow again to collapse the folder. The file remains saved inside it.
4. Press **Ctrl+P**, type `example-task.md`, and select the result with the `prompts` path.

A **relative path** starts at the current project folder. An **absolute path** includes its full
location on the PC. `outputs/note.md` means “note.md inside outputs in this project.” When names
repeat, check the folder path in the result, not just the filename.

Explorer's single click can open a temporary editor tab, often shown in italics. Opening another
file can replace that tab. Double-click to keep a file open. This temporary-tab behavior is separate
from **Markdown preview**, which formats a document for reading.

**Check:** you can find the same nested file using Explorer and Ctrl+P. Neither operation sends it
to Claude. Use `@` in Claude's message box when you want to select it for a request.

### Bring one approved input into the project

For a real task, confirm that both the source and this use of it are approved. In Windows File
Explorer, find that source file, select it, and press **Ctrl+C**. Open the work project's `inputs`
folder and press **Ctrl+V**. Cancel a replacement prompt; use an agreed new copy name instead.
Return to VS Code, expand `inputs`, and confirm the copied filename. In Claude chat, select that
specific file with `@inputs/` and the picker, then state the allowed operation. A copy keeps the
original in place; it does not itself authorize processing or make a workbook reader available.
For names with spaces, use the picker instead of guessing quoting rules.

## 3. Create, edit, save, and rename

- **New file:** choose **File > New Text File**, type, then **Ctrl+Shift+S**. Select the exact project
  folder and filename, such as `my-request.md`. Save As chooses the location as well as the name.
- **New file in a subfolder:** right-click that folder in VS Code Explorer > **New File**. Type a
  name ending in `.md` and press Enter. Check where it appears, edit, then **Ctrl+S**.
- **New subfolder:** right-click the intended parent folder in Explorer > **New Folder**, name it,
  and press Enter. Check the indentation to confirm the parent.
- **Save an edit:** **Ctrl+S**. A dot on the tab normally marks unsaved changes. Save explicitly
  before Claude reads the file even if Auto Save is enabled.
- **Undo an accidental edit:** click in the text editor and press **Ctrl+Z** before making further
  edits. Read the result before saving. Undo in the editor is not a general rollback for Claude's tools.
- **Save a reusable copy:** open the file, choose **File > Save As**, and use a new name. Confirm
  the new tab's path before changing its contents; the original should remain intact.
- **Rename:** right-click the file in Explorer > **Rename**. Update the next `@` reference and any
  paths in the task. An old chat reference does not automatically become the renamed path.

If VS Code asks whether to save on closing, choose based on whether you want those edits kept.
Cancel if unsure and inspect the file first. Saving in a local folder does not publish to GitHub.
[Basic editing and saving](https://code.visualstudio.com/docs/editing/codebasics).

**Try:** save a copy of `prompts/example-task.md` as `prompts/my-next-task.md`. Change its output
filename and save. **Check:** both request files remain; no task has run. Next, read the copy comfortably.

## 4. Read and edit Markdown in one pane

Markdown is plain text with simple formatting. `# Heading`, `## Subheading`, `- list item`, and
`**important text**` are enough to start. Claude reads the saved text; fancy formatting is optional.

**Already using an approved inline Markdown extension?** Continue using it. To see which one is
installed, press **Ctrl+Shift+X**, type **`@installed markdown`** in the Extensions search box,
and open the matching extension's details. Record its exact name, publisher, and version locally.
Read its own instructions for switching editing/reading views; do not install another lookalike
or change managed defaults just to follow this guide. That Extensions search is different from
`@` in Claude chat. [Extension management](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace).

**With built-in VS Code:**

1. Open the `.md` file in the editor.
2. Press **Ctrl+Shift+V**, or right-click its tab > **Open Preview**. Read the formatted page.
   This uses the current editor group; **Open Preview to the Side** creates a second column.
3. To edit, close the preview tab and double-click the file in Explorer. If it reopens in an
   extension's reading view, right-click the tab > **Reopen Editor With… > Text Editor**, if offered.
4. Edit and press **Ctrl+S**. Preview again to check the saved result.

If two columns are confusing, close the extra preview and choose **View > Editor Layout > Single**.
Click the desired file or Claude tab afterward. A Markdown reading preview is not necessarily an
editable surface. Click in the text editor before dictating or pasting a request.
[Markdown editing and preview](https://code.visualstudio.com/docs/languages/markdown).

**Check:** you can switch between readable formatting and editable text without losing the file.
Which extension supplies inline editing is a PC-specific detail; this kit has not verified it.

## 5. Keep your workspace small and familiar

**For now, one project folder per window is enough.** **File > Open Folder** selects that workspace;
**File > Open Recent** reopens it later. Opening a single file is different: it does not select that
file's whole folder as the workspace. Confirm the project name in Explorer before each task.

For a new work objective, prepare a separate employer-approved project folder. Open it in VS Code
and start a new Claude conversation. Your personal skills remain available. Project `CLAUDE.md`
instructions belong to that project; ordinary task files become input when you select them or
explicitly authorize Claude to read them. A workspace is an organizational boundary, not an access-control sandbox.

Later, a **multi-root workspace** can hold several related folders, and **File > Save Workspace As**
can save that selection in a `.code-workspace` file. Only use it when the task needs multiple folders
and you can identify each input path. It is not necessary for this kit. Follow workplace policy
for any saved workspace file. [Workspace documentation](https://code.visualstudio.com/docs/editing/workspaces/workspaces).

**Try later:** reopen `Practice-01` through Open Recent and find yesterday's saved request without
this guide. **Check:** the expected root and output are present. If you cannot tell which project
is open, repeat the folder-selection step before giving Claude a work request.

## 6. Use the editor and Claude together

| What you intend | Action |
| --- | --- |
| Write your thoughts privately in the approved project | Edit a Markdown file and save it |
| Give Claude that request | In Claude's message box, type `@`, choose the exact saved file, and add what to do |
| Use a reusable task procedure | Select `/skill-name` in Claude's message box |
| Give Claude both a request and evidence | Select the request file and each specifically approved input with `@`; identify their roles |
| Correct a request | Save the edit, select that file again, and explicitly ask Claude to reread the current version |
| Read the result | Open the reported file under `outputs` and independently check it |

Claude may propose a file edit or tool action while you remain in its graphical panel. Review the
scope and result there; you do not need to start a terminal chat to use file tools.
If the panel shows selected editor text from an unrelated file, remove that context before sending.
[Claude Code's file-reference controls](https://code.claude.com/docs/en/vs-code#reference-files-and-folders).

Next: [saved prompt and dictation patterns](14-prompt-files-and-dictation.md), or return to the
[README exercise](../setup/MANUAL-SETUP.md#7-write-a-larger-request-as-a-markdown-file). Focus on one remaining
operation you need help with, then use it for a small checked task.
