# Optional: reuse instructions across projects

Complete [the README setup walkthrough](../README.md) first. It creates
project instructions for practice. This page is a later option for preferences that should apply
across projects. It is not required to install skills or finish the first exercise.

## Read the template

1. Keep your work folder open in VS Code. Choose **File > Open File**.
2. Navigate to the extracted `vscode-claude-code-main` starter, open `templates`, and select
   `GLOBAL-CLAUDE.md`. Read it without editing the source. It covers concise responses, teaching,
   work boundaries, preservation, and checks.
3. Close the reference tab. Keep company-specific instructions in the approved project folder.

## Copy only when personal instructions are permitted

1. Press **Windows+E** for Windows File Explorer. Enter `%USERPROFILE%` in its address bar and
   press **Enter**. Open `.claude`; if absent and permitted, create that folder.
2. If `CLAUDE.md` already exists, leave it unchanged for now. Before merging useful additions,
   keep a dated backup outside the active instruction location, confirm it opens, and compare
   the proposed changes with existing approved rules. Do not replace managed instructions.
3. If no `CLAUDE.md` exists, open another File Explorer window and navigate to the starter's
   `templates` folder. Select `GLOBAL-CLAUDE.md`, press **Ctrl+C**, switch to `.claude`, and press
   **Ctrl+V**. Cancel any unexpected replacement prompt.
4. Select the copied `GLOBAL-CLAUDE.md`, press **F2**, and rename it `CLAUDE.md`.
5. In VS Code choose **File > Open File**, navigate to that `.claude` folder, and open the saved
   `CLAUDE.md`. Confirm its name and contents. The full filename must not end in `.txt`.
6. Close the reference tab. Start a new Claude conversation in the intended work project. Use
   `/memory`, where available, to inspect the instruction files loaded by Claude Code.

**Check:** `%USERPROFILE%\.claude\CLAUDE.md` contains only the intended approved instructions.
This is a standard Claude instruction file, not a custom persistent-memory system. Keep the
working gateway and all unrelated configuration unchanged. If personal files are blocked, leave
this optional setup pending.

[Official instruction locations](https://code.claude.com/docs/en/memory).
Return to [the learning guide](../LEARN.md) for your next useful task.
