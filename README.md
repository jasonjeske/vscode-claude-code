# Use Claude Code in VS Code for property-tax work

![Claude Code in VS Code. Learn by doing: Excel, research, and reporting.](assets/readme-banner.png)

**Start with one state, one workbook, and one useful result.** Install the skills through the
Claude Code extension, let Claude prepare a working folder, then inspect a workbook and check its
findings in Excel. Later lessons build toward reconciliation, state-law research, and reporting.

This guide assumes **VS Code and the Claude Code extension already connect through your approved
workplace gateway**. Keep that connection and model. No personal subscription or GitHub login is
required to read or download this public guide. Use invented practice data first; actual work and
its processing need approved storage and tools. Nothing here determines a tax filing position.

**Your first result:** a map of a small Excel workbook, saved beside it, with one finding you can
verify yourself. You will use the supplied invented Ohio 2026 file. Then repeat the method on one
approved workbook for the state you actually handle. No full-drive scan or all-state upload.

## 1. Open the starter in VS Code

**What is `README.md`?** It is this guide saved as a **Markdown** file. The `.md` ending identifies
an ordinary text document that can display headings, bold words, and lists. GitHub shows its
formatted reading view. You will use the same kind of file for saved requests to Claude.

1. [Download the ZIP](https://github.com/jasonjeske/vscode-claude-code/archive/refs/heads/main.zip).
   In your browser's downloads list choose **Show in folder**.
2. Right-click the ZIP > **Extract All**. Choose an approved learning location, then **Extract**.
   Open the extracted folders until you see `README.md`, `state-project`, `skills`, and `setup`
   together. This is the **starter folder**, not the ZIP itself.
3. Open **Visual Studio Code** from Windows Start. Choose **File > Open Folder**, select that
   starter folder, and choose **Select Folder**. Follow workplace Workspace Trust policy.
4. Press **Ctrl+Shift+P**, type **Claude Code**, and choose **Open in New Tab** or the offered
   Claude open-panel command. Click the **Claude Code message box** when sending a request.

![Microsoft's screenshot of the VS Code Command Palette, with file and folder actions.](assets/reference/vscode-command-palette.png)

*This is the real VS Code Command Palette. Search for **Claude Code** in that box to open the
extension. The screenshot shows example file commands. © Microsoft, [CC BY 3.0 US](assets/reference/ATTRIBUTION.md).*

**Check:** VS Code's Explorer shows `state-project` and `setup`, and the conversation panel says
**Claude Code**. If the gateway is disconnected, use workplace support. **Next: install the kit.**

## 2. Install the skills inside Claude Code

A **plugin** packages skills so Claude Code can install, enable, update, and remove them together.
You do not need to copy six skill folders by hand. This repository now provides that package.

In **Claude Code's message box**, type **`/plugins`** to open **Manage plugins**. These steps use
Claude's plugin panel, not VS Code's Extensions search and not a terminal.

| In the panel | What to enter or choose |
| --- | --- |
| **Marketplaces** > add source | `jasonjeske/vscode-claude-code` |
| **Plugins** > find the kit | `property-tax-workbench` from `property-tax-learning` |
| **Install** > scope | **Install for you**, when permitted by workplace policy |
| Apply changes | Use the offered restart, then open a fresh Claude conversation |

That one installation supplies **all six custom skills**: workbook review, reconciliation review,
property-tax research, financial dashboards, prompt coaching, and structured work requests.
It adds instructions; it does not install Excel libraries, connect databases, or configure agents.

**Personal scope means available across your local projects.** Claude manages the package's cache;
do not move those files into `.claude/skills`. Normal requests can select a matching skill. To
choose one explicitly, type `/` and select, for example,
**`/property-tax-workbench:excel-workbook-review`**. Check the actual menu for your installed version.

If adding the GitHub source fails because Git or network access is unavailable, the custom kit can
also use your **extracted starter's full folder path** as the marketplace source. Copy that path
from Windows File Explorer's address bar into **Marketplaces**. If plugins are restricted, keep the
step pending and use the supported workplace route. [Manual-copy fallback](setup/MANUAL-SETUP.md).

**Already copied standalone skills from an older guide?** Those are a separate installation.
Use one route, not both. Keep the existing copies or follow the
[plugin migration steps](setup/SKILLS.md#switch-from-manual-copies-to-the-plugin) before removing any.

**Check:** the plugin is installed and enabled, and its six namespaced skills appear in `/`.
A skill name appearing proves discovery, not that its Excel tools work. **Next: add Office support.**

## Add Anthropic's Office skills for Excel work

Use the same **Manage plugins** panel:

| In the panel | What to enter or choose |
| --- | --- |
| **Marketplaces** > add source | `anthropics/skills` |
| **Plugins** > find the package | `document-skills` from `anthropic-agent-skills` |
| **Install** > scope | **Install for you**, when permitted |
| Apply changes | Use the offered restart and confirm the XLSX entry in `/` |

This is Anthropic's **Excel (`xlsx`), Word (`docx`), PowerPoint (`pptx`), and PDF** package.
Our custom workbook review skill complements it. You can ask “Use the XLSX skill to create this
workbook,” or explicitly choose the actual entry, such as `/document-skills:xlsx`.

The package has specific license terms and runtime requirements. Python libraries and an Office
calculation tool may be needed; a gateway key does not install them. If a required tool is absent,
Claude must report the blocker. Use workplace support for the approved runtime, rather than
changing the gateway or installing unapproved software.
[Source/runtime details](guides/07-trusted-skills-and-installation.md#findings-that-change-the-recommendation).

**Check:** distinguish **package installed** from **file task completed and checked in Excel**.
The next task will establish which capabilities actually work on this machine.

## 3. Let Claude prepare the practice workspace

![Personal plugins stay installed while each state folder holds its own tasks, inputs, and outputs.](assets/learning/state-workflow.svg)

*Concept diagram: install the procedures once, then keep each project's files together.*

Keep the **starter folder open in VS Code**. Paste this in Claude Code:

```text
The extracted vscode-claude-code starter is open in VS Code. Read only setup/ASSISTED-SETUP.md
and follow it to create a new state practice workspace beside this starter in approved learning
storage. Use the included state-project as the source. Preserve existing files and settings.
Do not read the rest of the repository, install packages, or begin the workbook task yet.
Show the destination, verify the copied files, and tell me which folder to open next in VS Code.
```

Claude now does the folder preparation. Respond to any actual path or tool-access question;
if it reports the setup file is missing, repeat step 1 and open the extracted starter itself.
This prompt works because the named setup file is present in the currently open folder.

When Claude finishes, choose **File > Open Folder** and select the exact new path it reported,
usually the sibling **State-Practice**. Reopen Claude Code with **Ctrl+Shift+P** if needed.

```text
State-Practice/               open this folder for the exercises
  CLAUDE.md                  supplied practice instructions
  inputs/state-practice.xlsx  invented Ohio workbook, with Book and Bill sheets
  prompts/first-workbook.md   first task, ready to select
  prompts/reconcile.md        later reconciliation task
  outputs/                   where new results go
  evidence/                  checks and source notes
  working/                   intermediate work
```

**Check:** your open project is the new working copy. In **View > Explorer**, expand `inputs` and
`prompts` and confirm those files exist. The original starter remains separate. **Next: useful work.**

## 4. Inspect one workbook and check the result in Excel

### First, read the saved request: what a Markdown file looks like

In **View > Explorer**, expand **prompts** and double-click **first-workbook.md**. This document
contains the task you will give Claude. It is text, not an Excel workbook or a program to run.

Markdown has two appearances: the **source text** you edit and the **formatted view** you read.
They represent the same document:

| Text stored in the file | What the formatted view shows |
| --- | --- |
| `# Review the workbook` | A large heading saying “Review the workbook” |
| `- Preserve the original` | A bullet followed by “Preserve the original” |
| `**Check the total**` | **Check the total** |
| `Use the Book sheet.` | Use the Book sheet. |

**Using an inline Markdown editor?** It can show a formatted page while letting you edit in the
same place. In editors that reveal the active line, clicking a heading may expose its `#`, or
clicking bold words may expose `**`. That is the underlying text, sometimes called **raw Markdown**.
The file has not broken or become code. Keep those marks if you want to keep the formatting.
Moving out of the line may restore its formatted appearance; the exact behavior depends on the
installed extension. There is no need to open two panes or install a second Markdown editor.

**If you see plain text instead:** that works too. You can read and edit it directly. VS Code's
built-in **Ctrl+Shift+V** opens a formatted reading preview; return to the text editor to edit.
[Reading and editing controls](guides/00-vscode-basics.md#4-read-and-edit-markdown-in-one-pane).

Read the supplied request without changing it for this first task. When you later type or dictate
your own requests, save with **Ctrl+S** before sending them. Ordinary sentences are enough; headings
only organize your thoughts. **Opening, formatting, or saving a request does not run it.** Next,
you will select that saved file in Claude chat and explicitly ask Claude to perform the task.

### Give the saved request to Claude

1. In Claude's message box, type **`@prompts/first-workbook.md`** and choose that exact file from
   the suggestions. `@` selects a saved file for Claude to read; it is not a Windows command.
2. Add the following text and send once:

```text
Read the selected first-workbook.md as my task and perform it using the named practice workbook.
Use the installed Excel review skill if available. Give me the actual new output path and one
check to do in Excel. Keep the original workbook unchanged. Explain one unfamiliar VS Code step
briefly, but focus on completing the task. Report a missing reader instead of guessing contents.
```

3. When complete, open **Explorer > outputs > workbook-map.md** (or the new name reported).
   Read its sheet names and the cited source location. A chat reply alone is not the saved result.
4. In Explorer, right-click **inputs > state-practice.xlsx** > **Reveal in File Explorer**.
   Double-click the file there to open it in **Microsoft Excel**. Select the **Book** tab and
   check one cited row and the total. Close the original without saving changes.

![Preview of the supplied invented Book sheet, showing four detail rows and a 1000-dollar control total.](assets/learning/state-practice-book.png)

*Preview rendered from the supplied practice workbook, not a screenshot of your Excel installation.
All records are invented. The Book and Bill sheets deliberately contain different populations.*

**Check:** there are four detail rows in each sheet. Book total is **$1,000** and Bill total is
**$1,100**. Property IDs keep their leading zeros. If a tool could not read the file, do not accept
invented sheet descriptions. You can inspect the file yourself in Excel while getting the approved
reader installed. [A text-only fallback](learn/02-spreadsheet-work.md#learn-a-formula-on-a-tiny-example)
is available if tools are blocked.

You have now opened a project, selected a saved task, used Claude on an Excel file, found its
output, and checked source evidence. **Next: reconcile the two sheets in session 2 below.**

## 5. Continue from beginner toward intermediate

Keep using one state and one reporting period. Each session produces a useful workpaper and adds
one editor/Claude skill. Stop after the checked output; no need to complete a whole course in a day.

| Session | Work result | VS Code / Claude operation learned |
| --- | --- | --- |
| **1. Inspect** | Workbook map checked against the actual file | Open folder, select `@file`, find output, open in Excel |
| **[2. Reconcile](learn/STATE-WORKFLOW.md#2-reconcile-the-state-workbook)** | Matched comparison, both unmatched sides, controls | Run a saved task; let XLSX tools create a new workbook; check totals |
| **[3. Investigate](learn/STATE-WORKFLOW.md#3-investigate-one-difference)** | One evidence-backed exception note | Narrow an input range; revise a saved prompt; separate facts from causes |
| **[4. Research](learn/STATE-WORKFLOW.md#4-research-one-state-rule)** | One cited rule memo for the applicable jurisdiction/year | Select source documents or allow a scoped official-source search |
| **[5. Report](learn/STATE-WORKFLOW.md#5-report-checked-results)** | One summary with a useful chart and visible exceptions | Specify the audience, output format, and chart checks |
| **[6. Repeat](learn/STATE-WORKFLOW.md#6-repeat-with-a-new-period-or-state)** | Reusable state project and request | Edit Markdown, reuse instructions, compare periods without stale inputs |

**Bring your work in after the practice check:** choose one approved workbook for a state you
handle. Ask Claude to prepare a separate work folder at an approved path. Supply the actual
period, matching rules, and allowed operations. Start with a read-only map, not a full rewrite of
an inherited workbook. Complex PivotTables, Power Query, macros, and connections need native
Excel preservation checks before changes. [Move to your state project](learn/STATE-WORKFLOW.md#move-to-your-own-state-project).

## Know the controls when you need them

![Microsoft's labeled VS Code interface with Explorer in the left sidebar, editor tabs, lower panel, and status bar.](assets/reference/vscode-interface.png)

*Use the left file list to find inputs and outputs. Your Claude panel opens through the command
in step 1. The code and terminal pictured are Microsoft's example; this course uses workbook and
request files. © Microsoft, [CC BY 3.0 US](assets/reference/ATTRIBUTION.md).*

| Need | Action |
| --- | --- |
| Find a file yourself | **Ctrl+P**, type its name, choose the correct folder |
| Give a file to Claude | In Claude chat type **@**, choose the saved file, then add the task |
| Choose a particular skill | In Claude chat type **/**, choose its actual namespaced command |
| Write a longer request | Open a `.md` file in the editor, edit or dictate, then **Ctrl+S** before selecting it |
| Read Markdown comfortably | Use the approved inline editor; built-in fallback is **Ctrl+Shift+V** |
| Recover from split editors | **View > Editor Layout > Single** |
| Resume next time | **File > Open Recent** > your state workspace > open Claude |

Ask normally. Installed skills can be selected from a matching request; `/` is the explicit
fallback. A skill supplies a procedure, `@` supplies an input, and your request sets the allowed task.
Use focused conversations, the approved model, and the gateway's usage page. Avoid asking Claude
to read every guide or all the files for every state. A saved prompt is reusable, not token-free.

Official references: [Claude Code in VS Code](https://code.claude.com/docs/en/vs-code),
[plugin installation](https://code.claude.com/docs/en/discover-plugins),
[skill selection](https://code.claude.com/docs/en/skills).

## Explore the repository: complete navigation index

**Finished the first README task? Start with section A below**, then keep B nearby while working.
Explore C and D when a task needs them. E is for setup changes or recovery; F explains supporting
files and verification. You do not need to read everything or ask Claude to load the repository.
Each link opens a page, file, or folder on GitHub. Use your separate local work folder for exercises
and completed templates. Downloaded HTML and Excel examples open in their own applications.

**Jump to:** [A. Lessons and practice](#a-lessons-and-practice) ·
[B. Everyday references](#b-everyday-references) · [C. Skills](#c-skills-and-their-instructions) ·
[D. Templates](#d-templates-to-adapt-in-your-work-folder) · [E. Setup](#e-setup-and-recovery) ·
[F. Supporting files](#f-supporting-files-and-maintenance).

### A. Lessons and practice

Follow the state workflow first. The individual lessons are shorter alternatives when you want
to practice just one operation. All sample records are invented.

| Suggested order | Open | What you will find |
| --- | --- | --- |
| Next | [State workflow course](learn/STATE-WORKFLOW.md) | Continue the workbook through reconciliation, investigation, research, reporting, and reuse |
| Choose today's task | [Learn through useful work](LEARN.md) | A task picker, coaching prompt, and checks for growing independence |
| Practice a conversation | [Lesson 1: first conversation](learn/01-first-conversation.md) | Ask, clarify, and improve a small request |
| Practice spreadsheet work | [Lesson 2: spreadsheets](learn/02-spreadsheet-work.md) | Formula checks, workbook review, and an official XLSX skill exercise |
| Practice research | [Lesson 3: source-backed research](learn/03-source-backed-research.md) | Scope one question and check its citations |
| Practice reporting | [Lesson 4: reports](learn/04-reports.md) | Turn checked evidence into a useful reviewer draft |
| Reuse the method | [Lesson 5: adapt to your work](learn/05-adapt-to-your-work.md) | Adjust project instructions and repeat a bounded task |
| Check your attempt | [State answer key](practice/STATE-ANSWER-KEY.md) | Expected counts, amounts, differences, and reconciliation bridge |
| If Excel tools are unavailable | [Text-only first session](practice/FIRST-SESSION.md) | Work through a small reconciliation directly in chat |
| Inspect the supplied project | [State project folder](state-project/) | The complete source that Claude copies during setup |
| Inside that project | [Practice instructions](state-project/CLAUDE.md), [Excel input](state-project/inputs/state-practice.xlsx), [first task](state-project/prompts/first-workbook.md), [reconciliation task](state-project/prompts/reconcile.md) | The actual files used by the first two assignments |
| Understand its empty folders | [Outputs](state-project/outputs/), [evidence](state-project/evidence/), [working](state-project/working/) | Places for generated results, source notes, and intermediate files; `.gitkeep` only keeps an empty folder in the download |
| Explore a dashboard example | [Dashboard guide and answer key](examples/dashboard/README.md) | How to open the local example and check filters, totals, and print layout |
| Dashboard files | [HTML page](examples/dashboard/index.html), [sample data](examples/dashboard/demo-data.js), [behavior code](examples/dashboard/dashboard.js) | Keep all three together when opening the downloaded example; GitHub displays their source |

### B. Everyday references

Use the first four as desk references. Read the specialist playbooks when that work arrives.

| Open | Use it for |
| --- | --- |
| [Daily desk guide](guides/DAILY-USE.md) | Starting and finishing a focused work session |
| [VS Code basics](guides/00-vscode-basics.md) | Explorer, folders, editor tabs, saving, Markdown, and workspaces |
| [Claude Code panel guide](guides/00-use-vscode.md) | Where to type, usage views, waiting, and recovering from a blocked task |
| [Saved prompts and dictation](guides/14-prompt-files-and-dictation.md) | Collecting rough notes in a file, saving, selecting with `@`, and revising the request |
| [Prompt library](prompts/PROMPT-LIBRARY.md) | Ready-to-adapt requests for common work tasks |
| [Claude Code fundamentals](guides/01-claude-code-fundamentals.md) | Task scope, context, commands, and how to check results |
| [Review plans and changes](guides/04-reviewing-claude-plans-and-diffs.md) | Reading a proposed action or file comparison before accepting it |
| [Excel and reconciliation playbook](guides/08-excel-and-reconciliation-playbook.md) | Complex workbook preservation, keys, duplicates, differences, and controls |
| [Multistate work](guides/02-multistate-property-tax-workflows.md) | Organizing jurisdiction-specific work and evidence |
| [Property-tax research](guides/12-property-tax-research.md) | Narrow legal questions, applicable years, source quality, and memo structure |
| [Dashboards and reporting](guides/09-dashboard-and-reporting-playbook.md) | Choosing metrics, formats, charts, and reviewer checks |
| [Token-efficient work](guides/13-token-efficient-work.md) | Avoiding unnecessary reads and retries; assessing Caveman-style compression |
| [Models and workplace usage](docs/MODELS-AND-USAGE.md) | Model/effort choices within an existing managed gateway |
| [Build independence](guides/10-four-week-learning-path.md) | Capability milestones; the filename does not require four weeks of study |
| [Improve a recurring process](guides/05-after-onboarding-growth-path.md) | Deciding what to automate after the first tasks work |
| [Guide index](guides/README.md) | An alternative topic-based entrance to the guides |

### C. Skills and their instructions

The README installs the **six custom skills together**. Open their source files below to understand
their procedures, not to reinstall them. Official and community recommendations are separate packages.

| Open | What it contains |
| --- | --- |
| [Skill catalog](SKILLS.md) | What each skill does, when to choose it, and a first prompt |
| [Official skill recommendations](guides/07-trusted-skills-and-installation.md) | Anthropic Office, Data, and Finance options, sources, and runtime requirements |
| [Community skill recommendations](guides/11-community-skills-worth-adding.md) | Design, data, SQL, and graphics choices with installation considerations |
| [Skills by work category](guides/03-professional-skills-by-category.md) | How a job workflow, an agent skill, and VS Code tools fit together |
| [Workbook review skill](skills/excel-workbook-review/SKILL.md) | Read-only structure, formula, and preservation review |
| [Reconciliation review skill](skills/reconciliation-control-review/SKILL.md) | Matching and full-population control checks |
| [Property-tax research skill](skills/property-tax-research/SKILL.md) | Scoped, cited research with applicability and uncertainty checks |
| [Research memo format](skills/property-tax-research/references/research-memo.md) | The supporting memo structure used by the research skill |
| [Financial dashboard skill](skills/financial-dashboard/SKILL.md) | Useful presentation with defined metrics and traceable totals |
| [Prompt coach skill](skills/prompt-coach/SKILL.md) | Turn rough ideas into a clear request without executing it |
| [Structured request skill](skills/structured-work-request/SKILL.md) | Clarify a complicated task's scope and requirements |
| [All skill folders](skills/) | Browse the complete bundled skill sources |

### D. Templates to adapt in your work folder

These are blank starting points. They do not configure anything merely because you open them.
Keep filled versions in approved local work storage, outside this public repository.

| Open | Use it for |
| --- | --- |
| [Prompt notes](templates/PROMPT-NOTES.md) | A longer request you can type or dictate before sending |
| [Work task note](templates/WORK-TASK-NOTE.md) | Save a successful method, prompt, and verification check |
| [Project instructions](templates/PROJECT-CLAUDE.md) | Stable rules for one work folder |
| [Reconciliation project](templates/projects/RECONCILIATION-CLAUDE.md) | Matching, exceptions, and review controls |
| [Research project](templates/projects/RESEARCH-CLAUDE.md) | Jurisdiction, sources, and evidence rules |
| [Exemption project](templates/projects/EXEMPTION-CLAUDE.md) | Organize exemption facts and research without assuming eligibility |
| [Dashboard project](templates/projects/DASHBOARD-CLAUDE.md) | Audience, metrics, source data, and display checks |
| [Learning and work preferences](templates/LEARNING-AND-WORK.md) | Choose teaching, guided, or routine assistance |
| [Global instructions](templates/GLOBAL-CLAUDE.md) | Optional preferences across projects; apply using the setup guide below |
| [Setup receipt](templates/SETUP-RECEIPT.md) | Record what was installed and which checks remain pending |
| [All templates](templates/) | Browse the blank documents together |

### E. Setup and recovery

The current setup is already in this README. Return here only to maintain it, change scope,
or use an alternative route. You do not need to run onboarding again for each assignment.

| Open | When you need it |
| --- | --- |
| [Start Here](START-HERE.md) | A short signpost back to this README's ordered setup |
| [Assisted workspace setup](setup/ASSISTED-SETUP.md) | Inspect the exact bounded instructions Claude follows in step 3 |
| [Install and maintain skills](setup/SKILLS.md) | Plugin scope, updates, removal, and migration from old standalone copies |
| [Optional global instructions](setup/GLOBAL-INSTRUCTIONS.md) | Reuse preferences without overwriting existing managed instructions |
| [Project setup reference](setup/PROJECTS.md) | An alternative folder-copy method and project-specific templates; the state course also provides AI-assisted setup |
| [Manual setup fallback](setup/MANUAL-SETUP.md) | File-copy installation when plugins cannot be used, plus optional editor exercises |
| [Standalone skill files explained](guides/15-skills-made-visible.md) | Folder locations and unprefixed commands for that manual fallback |
| [Full Windows onboarding](setup/FULL-ONBOARDING.md) | A longer setup protocol for a fresh or uncertain installation, preferably with support |
| [Illustrative onboarding conversation](docs/EXAMPLE-ONBOARDING-TRANSCRIPT.md) | A fictional example of that longer protocol, not a session to execute |
| [Older text practice project](practice-project/) | Source folder used by the manual fallback; separate from the main `state-project` |
| [Its instructions](practice-project/CLAUDE.md) and [example task](practice-project/prompts/example-task.md) | The text exercise files in that alternative project |
| [Its inputs](practice-project/inputs/), [outputs](practice-project/outputs/), [evidence](practice-project/evidence/), [working](practice-project/working/) | Empty placeholders for the alternative practice route |
| [Optional usage status line](guides/06-budget-aware-statusline.md) | A later terminal customization; not required for the native Claude panel |
| [All setup references](setup/) | Browse the setup files together |

### F. Supporting files and maintenance

**You can skip this section for everyday work.** It explains the remaining folders so unfamiliar
files do not look like extra assignments. Scripts and configuration candidates are for a helper
or maintainer to review; opening their GitHub links does not run or install them.

| Open | What it is for |
| --- | --- |
| [Teaching method](docs/TEACHING-METHOD.md) | Why the lessons pair useful work with a small independent check |
| [Security and data boundaries](docs/SECURITY.md) | What the toolkit does and does not protect |
| [Validation record](docs/TOOLKIT-VALIDATION.md) | Checks performed and their limits |
| [Windows verification ledger](docs/WINDOWS-VERIFICATION.md) | Target-PC behaviors that still need hands-on verification |
| [Skill selection checks](docs/SKILL-SELECTION-CHECKS.md) | Cases for checking automatic selection and explicit commands |
| [All supporting documents](docs/) | Browse verification, usage, and design references |
| [Configuration folder](config/) | Optional candidates, not automatically applied settings |
| [VS Code settings candidate](config/vscode-settings.json) | Suggested editor settings for a reviewed merge |
| [Status-line script](config/statusline.ps1) and [budget example](config/statusline-budget.example.json) | Optional PowerShell usage display and a blank configuration example |
| [Plugin metadata](.claude-plugin/plugin.json) and [marketplace catalog](.claude-plugin/marketplace.json) | How Claude Code discovers and packages the six custom skills |
| [QA runbook](tests/QA-RUNBOOK.md) | Manual verification procedures for maintainers |
| [Repository checker](tests/validate-repo.mjs) | Checks local links, skill metadata, and configuration syntax |
| [Merge checks](tests/merge-spec.mjs) and [test fixtures](tests/fixtures/) | Invented candidate/existing/expected files for settings-merge tests |
| [Dashboard checks](tests/dashboard-spec.mjs) | Verifies synthetic calculations and filter combinations |
| [Plugin checks](tests/plugin-spec.mjs) | Verifies the complete instruction-only package |
| [Workbook checks](tests/state-workbook-spec.py) | Verifies the shipped Excel sample and reconciliation answer key |
| [All tests](tests/) and [GitHub validation workflow](.github/workflows/validate.yml) | The verification files and the automation that runs checks after changes |
| [Images and diagrams](assets/) | The README banner, earlier cover/flow artwork, and teaching illustrations |
| [Learning illustrations](assets/learning/) | Folder, prompt, skill, spreadsheet, and workflow visual examples |
| [VS Code screenshots](assets/reference/) and [their attribution](assets/reference/ATTRIBUTION.md) | Microsoft documentation images and reuse terms |
| [Contributing](CONTRIBUTING.md) | Repository structure and how to maintain the guide |
| [Change history](CHANGELOG.md) | Recorded release changes |
| [License](LICENSE) | Repository reuse terms; separately attributed materials retain their own terms |
| [Ignored-file rules](.gitignore) | Patterns reducing accidental staging of work files; not a data-protection system |

When ready to continue, return to **[the state workflow](learn/STATE-WORKFLOW.md)** and choose the
next useful result. This index is a map, not a reading assignment.
