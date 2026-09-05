# Prepare the state practice workspace

This is a bounded local setup task for Claude Code with the extracted starter folder open.
The user has requested it in chat. Do not read the whole repository or launch an onboarding interview.

1. Confirm the current folder has `state-project/CLAUDE.md`,
   `state-project/inputs/state-practice.xlsx`, and `state-project/prompts/first-workbook.md`.
   If absent, stop and ask the user to open the extracted starter folder. Do not search drives.
2. Identify this starter's parent directory. Propose `State-Practice` as a sibling of the starter,
   show its full path, and use it only if this parent is approved learning storage. If that is
   unclear, ask for one permitted destination. Keep real work out of the public starter.
3. If that destination exists, do not merge or overwrite it. Offer to resume it after checking
   only `CLAUDE.md`, `inputs/state-practice.xlsx`, and `prompts/first-workbook.md` there, or use an unused sibling
   such as `State-Practice-02`. Get the user's choice if existing work makes the intent ambiguous.
4. Copy the entire `state-project` directory into the unused destination using the available
   local file tools. Preserve filenames, binary workbook bytes, and all subfolders. No downloads,
   dependency installation, configuration changes, or automatic tasks are part of this copy.
   Respect tool access prompts; do not change policy or elevation to reach a directory.
5. Compare source/destination relative file lists and file hashes. Report partial copying honestly;
   do not delete existing files to recover. The source remains unchanged.
6. Report the created full path and verified files. Tell the user exactly:
   **VS Code > File > Open Folder > choose that new folder > Select Folder**.
   Stop. Do not open the workbook or begin its task until the user requests it in the new workspace.

Plugin installation is handled by the README's Manage plugins steps, not this file. Do not copy
skills into personal discovery locations or install Office packages during this workspace task.
