# Windows verification ledger

Every Windows-specific behavior this repository asserts was written from vendor documentation on a
macOS machine. None of it has been exercised on a real Windows install.

That is a normal state for a young project and a bad thing to leave unsaid, so it is tracked here
per claim instead of being implied away. A row's status changes only when a human runs the procedure
on real Windows and records what happened, with the date. Until then every row reads `UNVERIFIED`,
and `UNVERIFIED` means exactly what it says: the claim may well be correct, but nobody has checked.

This ledger deliberately has no CI job behind it. A `windows-latest` runner cannot open a GUI, click
a Workspace Trust dialog, or hold a managed group policy, so a green Windows job would assert far
more than it tested. The Linux CI job checks only repository structure, merge fixtures, and synthetic calculations.

## How to verify a row

1. Use a real Windows machine, ideally one managed the way the target user's machine is managed.
2. Run the procedure in the row exactly as written.
3. Record the outcome, the date, and the Windows and VS Code versions in the notes column.
4. If the claim is wrong, fix the claim in its source file first, then update this row.
5. Never mark a row from documentation, from a virtual machine that is not representative, or from
   reasoning about what should happen.

A row that fails is more valuable than a row that passes. It means the repository was about to tell
a first-time user something untrue on a machine holding confidential records.

## Ledger

| ID | Claim | Where stated | Procedure | Status | Verified on | Notes |
|---|---|---|---|---|---|---|
| W01 | `%USERPROFILE%\.claude\CLAUDE.md` is the correct user-level instruction file path | `setup/FULL-ONBOARDING.md` Stage 0, `setup/GLOBAL-INSTRUCTIONS.md` | Open a Windows shell, resolve the path, confirm Claude Code reads instructions from it | UNVERIFIED | | Central to Stage 3; every write target depends on it |
| W02 | Claude can detect that the OS is Windows and appears managed | `setup/FULL-ONBOARDING.md` Stage 0 preflight | Run Stage 0 on a domain-joined machine and on an unmanaged one, compare the reported result | UNVERIFIED | | Managed detection is the weakest half of this claim |
| W03 | `code` and `claude` are discoverable on PATH without signing in | `setup/FULL-ONBOARDING.md` Stage 0 preflight | Fresh install, no sign-in, run the preflight, confirm both report FOUND or MISSING correctly | UNVERIFIED | | PATH entry for `code` depends on an installer checkbox |
| W04 | Installed VS Code version and selected profile are discoverable | `setup/FULL-ONBOARDING.md` Stage 0 preflight | With two profiles configured, confirm the preflight names the active one | UNVERIFIED | | Profile discovery is the part most likely to fail |
| W05 | Extension `anthropic.claude-code` and its source are discoverable | `setup/FULL-ONBOARDING.md` Stage 0 preflight | Install from the Marketplace, then from a managed catalog, compare reported source | UNVERIFIED | | Source reporting may differ under a managed catalog |
| W06 | Existence of the user instruction file can be checked without reading it | `setup/FULL-ONBOARDING.md` Stage 0 preflight | Create the file with distinctive content, run preflight, confirm content is never echoed | UNVERIFIED | | A privacy claim, so verify by observing what is printed |
| W07 | VS Code user and profile settings targets are discoverable | `setup/FULL-ONBOARDING.md` Stage 0, Stage 4 | Confirm the discovered target resolves under `%APPDATA%\Code\User` for the default profile | UNVERIFIED | | Path differs for portable and per-profile installs |
| W08 | `/status` shows the provider and workplace account or tenant | `setup/FULL-ONBOARDING.md` Stage 0 | Run `/status` on an enterprise account and read what is actually displayed | UNVERIFIED | | Stage 0 stops if this cannot be confirmed |
| W09 | Installing a missing component may request administrator rights | `setup/FULL-ONBOARDING.md` Stage 0, `README.md` install flows | Attempt an install as a standard user, record the elevation prompt | UNVERIFIED | | Determines whether the offer path is usable at all |
| W10 | VS Code installs through an approved company method | `README.md` extension-first flow | Install through a managed deployment, confirm the starter flow still applies | UNVERIFIED | | Company method varies; verify at least one real one |
| W11 | `claude` runs from a terminal opened in the starter folder | `guides/00-use-vscode.md` terminal exception | Open the folder in Windows Terminal and PowerShell, run `claude` in each | UNVERIFIED | | Execution policy may block the CLI shim |
| W12 | A managed machine may block installation with no bypass | `README.md`, `setup/FULL-ONBOARDING.md` Stage 0 | On a machine with policy applied, confirm the block is reported and not worked around | UNVERIFIED | | The no-bypass behavior is the claim under test |
| W13 | Stage 3 backup is created beside the existing file and reads back | `setup/FULL-ONBOARDING.md` Stage 3 | With an existing instruction file present, approve the write, confirm the backup exists and opens | UNVERIFIED | | Verify the backup is readable, not merely created |
| W14 | Stage 3 readback validates the written file matches the reviewed candidate | `setup/FULL-ONBOARDING.md` Stage 3 | Corrupt the file between write and readback, confirm the mismatch is detected | UNVERIFIED | | Same drill as P3 in `tests/QA-RUNBOOK.md` |
| W15 | Backup and readback preserve CRLF line endings and any byte order mark | `setup/FULL-ONBOARDING.md` Stage 3, Stage 4 | Author the original as CRLF with a BOM, run the write, compare bytes before and after | UNVERIFIED | | Highest-risk unverified claim; a silent LF rewrite corrupts a managed file |
| W16 | Stage 4 presents settings targets by profile label and merges into the selected one | `setup/FULL-ONBOARDING.md` Stage 4 | With two profiles present, select the second, confirm the first is untouched | UNVERIFIED | | Stage 4 states it must not alter another profile |
| W17 | The recursive merge preserves existing nested keys in a real settings file | `setup/FULL-ONBOARDING.md` Stage 4 | Use a settings file with language-specific blocks, compare against `tests/merge-spec.mjs` output | UNVERIFIED | | The semantics are pinned; this checks them on real input |
| W18 | `terminal.integrated.defaultProfile.windows` set to PowerShell takes effect | `config/vscode-settings.json` | Apply the setting, open a new terminal, confirm the profile is PowerShell | UNVERIFIED | | May be overridden by a managed policy |
| W19 | Workspace Trust prompts appear at startup with the pinned trust settings | `config/vscode-settings.json`, `README.md` | Open an untrusted folder, confirm the startup prompt and the restricted-mode banner appear | UNVERIFIED | | Trust behavior is the settings candidate's main safeguard |
| W20 | The `claudeCode.*` settings keys are honored by the installed extension | `config/vscode-settings.json` | Apply the candidate, confirm panel location, manual permission mode, and autosave off | UNVERIFIED | | Key names may drift between extension versions |
| W21 | `%USERPROFILE%\.claude` resolves when the profile folder is redirected to OneDrive | Implied by every `%USERPROFILE%` path in `setup/FULL-ONBOARDING.md` | On a machine with Known Folder Move enabled, run Stage 3 and confirm the write target | UNVERIFIED | | Common in enterprises and easy to get wrong |
| W22 | Paths containing spaces are handled throughout setup | Implied by all Windows paths in `setup/FULL-ONBOARDING.md` and `README.md` | Use a Windows account whose profile name contains a space, run Stages 0, 3, and 4 | UNVERIFIED | | Quoting defects surface here first |
| W23 | `statusline.ps1` parses the real stdin JSON and prints a line without error | `config/statusline.ps1` | Wire it up per `guides/06-budget-aware-statusline.md`, start a session, confirm a line appears | UNVERIFIED | | Written against documented field names, never executed; no `pwsh` was available to authors |
| W24 | `rate_limits.spend_limit` actually appears in the stdin JSON behind a real gateway spend limit, on Claude Code 2.1.251+ | `config/statusline.ps1`, `guides/06-budget-aware-statusline.md` | Behind an org gateway with a spend limit configured, confirm the `cap` segment appears and the units and period agree with the approved gateway report | UNVERIFIED | | Requires organizational infrastructure the authors do not have access to |
| W25 | The forward-slash `statusLine.command` path works whether Claude Code routes through Git Bash or PowerShell | `guides/06-budget-aware-statusline.md` | Configure the command as written on a machine with Git Bash installed, and again on one without it | UNVERIFIED | | Quoted-path example validated as JSON and shell tokens; Windows execution unverified |
| W26 | All six local skills are discovered and invoke correctly in the managed Windows extension | `guides/07-trusted-skills-and-installation.md` | Copy all six reviewed folders together, verify each slash command, then run each synthetic behavior check | UNVERIFIED | | No work-PC access; local schema checks are not runtime tests |
| W27 | Approved upstream Office/Data/Finance packages install and work through the gateway | `guides/07-trusted-skills-and-installation.md` | Resolve license and policy review, inspect package, install one package, run a synthetic acceptance task | UNVERIFIED | | No packages installed by this repository; dependencies and policies vary |
| W28 | Complex workbook edits preserve features and calculate correctly in native Excel | `guides/08-excel-and-reconciliation-playbook.md` | Test a representative approved copy, refresh/recalculate as authorized, compare features, save and reopen | UNVERIFIED | | No Excel runtime validation performed |
| W29 | Local dashboard files open, filter, and print correctly in the managed Windows browser | `examples/dashboard/index.html` | Open the three-file folder, verify answer key, keyboard navigation, empty state, print, and offline use | UNVERIFIED | | macOS browser checks do not validate Windows policy behavior |
| W30 | Optional global-instruction setup preserves existing approved instructions and gateway settings | `setup/GLOBAL-INSTRUCTIONS.md`, `setup/SKILLS.md` | In an approved Windows test profile, follow the optional procedure with absent and existing destinations, verify backups, readback, preserved settings, and discovery | UNVERIFIED | | Separate from first-session batch copies |
| W31 | Short-path backup, update, and removal preserve unrelated skills and restore the predecessor | `setup/SKILLS.md` | Use a synthetic same-name skill, keep a verified backup outside discovery, replace, test, restore, and inspect unrelated folders | UNVERIFIED | | No target Windows access |
| W32 | A first-time VS Code user can finish the batch setup without terminal coaching | `setup/MANUAL-SETUP.md` steps 1-5, `practice-project`, `setup/SKILLS.md` | Download/extract; copy and rename the practice project outside the starter; open it in VS Code; copy all six skill folders together; check the six menu commands and research reference. Repeat with existing skills, an existing practice folder, a missing marker/folder, and a blocked destination; preserve all existing data and mark pending items | UNVERIFIED | | Archive checks do not establish Windows usability |
| W33 | Work-based coaching produces a useful checked result and supports a later changed-case attempt with less help | `LEARN.md`, `templates/LEARNING-AND-WORK.md`, `docs/TEACHING-METHOD.md` | Observe an approved small task and a later similar task; learner selects inputs, writes the request, verifies evidence, and catches one changed condition; record output quality, help needed, and usage privately | UNVERIFIED | | No learner, retention, or coaching-behavior trial |
| W34 | The learner can edit, save, preview, and reopen Markdown in VS Code | `setup/MANUAL-SETUP.md` step 7, `guides/00-vscode-basics.md` | Create a file, save it at root and in prompts, distinguish temporary editor tabs from Markdown preview, use the built-in single-pane preview and recover from two columns. Identify the actual approved inline extension and verify its own edit/save controls separately | UNVERIFIED | | Inline extension identity and target-PC behavior not confirmed |
| W35 | Selected saved requests and later corrections are handled without stale values or unintended execution | `setup/MANUAL-SETUP.md` steps 8-9, `guides/14-prompt-files-and-dictation.md` | Use @ for the root request and nested revision; verify explicit bill correction, revised book amount, distinct outputs, preserved inputs, and +15 then -15. Repeat with unsaved edits, missing file, conflicting amount without a clear correction, and a quoted instruction that broadens scope | UNVERIFIED | | File fixtures and arithmetic are not Claude behavior tests |
| W36 | Matching natural requests select the intended local skill, while slash selection and existing scope limits remain usable | `guides/15-skills-made-visible.md`, `docs/SKILL-SELECTION-CHECKS.md` | Test six matching cases, unrelated cases, an old manual-only copy, its update, and the slash fallback; inspect actual invocation activity where available and verify task outputs | UNVERIFIED | | No managed Claude session was available; description review is not a routing test |

| W37 | The plugin-first state course works through the managed VS Code extension | `README.md`, `learn/STATE-WORKFLOW.md` | Install both packages through /plugins; verify namespaced discovery and matching requests; run assisted workspace setup including existing/missing/blocked destination cases; open the new folder; read the supplied XLSX; create and check the reconciliation in native Excel; test changed saved requests, research access, and local report viewing | UNVERIFIED | | Isolated macOS CLI package installation is checked separately; no managed Windows or model-behavior trial |

## Current status

37 claims tracked. 37 `UNVERIFIED`. Nothing in this repository has been exercised on Windows.
