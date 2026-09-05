# One state, from workbook to checked report

**Start with [README steps 1-4](../README.md).** They install the skills once, prepare
`State-Practice`, and produce the first workbook map. Keep that folder open in VS Code for
these sessions. Keep this guide in the browser. All supplied records are invented.

Each session follows **do the work, check the evidence, reuse the method**. Use one session per
useful result. You can stop and return through **File > Open Recent > State-Practice**.
Keep the existing workplace model and gateway. No agents or extra model conversations are needed.

## 2. Reconcile the state workbook

![Select the saved task, let Claude use the input workbook, then find and check the new output in Excel.](../assets/learning/state-workflow.svg)

**Result:** a new workbook comparing the Book and Bill populations, including unmatched records.
Here, reconciliation means explaining how two sets of records agree or differ, while accounting
for every record and dollar. Your actual team's controls and accounting rules take precedence.

1. In VS Code press **Ctrl+P**, type `prompts/reconcile.md`, and open it. Read the scope:
   one workbook, invented Ohio 2026 data, exact keys, Bill minus Book, new output only.
2. In the **Claude Code message box**, type `@`, then `reconcile`. Select
   **prompts/reconcile.md** from the list. After the selected file, send:

   ```text
   Perform this saved task using the installed spreadsheet capability and available approved tools.
   Preserve the input workbook. If the required reader or writer is missing, report the exact
   blocker instead of installing it or substituting a claimed workbook result.
   ```

3. Read tool requests before allowing them. Skill installation supplies instructions; runtime tools
   must also be available. If blocked, ask workplace support for the named missing dependency.
4. Find the new workbook in **Explorer > outputs**. Right-click it > **Reveal in File Explorer**,
   then open it in Excel. Review the source tabs, comparison, unmatched sides, and controls.
5. Check one matched row against the original, both source totals, and the full-population bridge.
   Check formulas in Excel's formula bar. Recalculation of a new output is separate from refreshing
   any source connections. Do not refresh external data or enable macros for this exercise.

**Try the check before [opening the answer key](../practice/STATE-ANSWER-KEY.md).** A zero net
matched difference can hide offsetting errors. Every unmatched record also needs to remain visible.
If a control fails, send Claude the precise cell, expected value, and observed value. Ask it to
correct a new output while preserving the source; do not continue to reporting on failed controls.

**Next use:** replace the practice matching rule only after confirming your actual identifiers,
period, grain, tolerance, and treatment of duplicate or missing keys.

## 3. Investigate one difference

**Result:** a short exception note with a known amount and an explicit evidence gap.

1. In VS Code's Explorer, right-click **prompts** > **New File**. Name it `investigate.md`.
2. Paste or dictate the following into the editor. Press **Ctrl+S**. This saves the request;
   it does not send it to Claude.

   ```text
   Read only inputs/state-practice.xlsx, Book and Bill detail rows 4-7.
   Investigate OH / 2026 / property 001102. Write a new outputs/exception-001102.md.
   Cite the source cells, calculate Bill minus Book, and distinguish observed facts from causes.
   The cause is unknown. Identify one source document that would help investigate it;
   do not invent that document or decide a journal entry, payment, or filing position.
   Explain one unfamiliar VS Code operation briefly. Preserve all existing files.
   ```

3. In Claude chat type **@investigate**, choose **prompts/investigate.md**, and send
   **“Perform this saved request.”**
4. Press **Ctrl+P**, type `exception-001102.md`, and open the output. To read rendered Markdown,
   use your approved inline editor or **Ctrl+Shift+V**. Return to the text tab to edit.

**Check:** Book D5 is $200; Bill D5 is $210; the difference is +$10. The source does not explain why.
“Timing” or “assessment change” would be a hypothesis, not an established cause.

**Try a change:** edit the saved request to property `001103` and output `exception-001103.md`.
Save, select the file again, and ask Claude to reread and perform the revised request. Check the
new sign yourself. This practices updating a request without reusing stale values or overwriting work.

## 4. Research one state rule

**Result:** one cited memo for a specific jurisdiction, tax type, issue, and applicable year.
The practice workbook contains no law or evidence of a tax treatment. Choose a real research
question relevant to your role; do not infer a legal question from its invented amounts.

1. Create **prompts/research.md** using the same Explorer action. Replace every bracketed field
   below before saving. Use only information permitted in this workspace and gateway.
2. If using supplied PDFs, place approved copies in **inputs**, then name their exact relative
   paths. If using the web, limit the first pass to the relevant official authority.

   ```text
   Research [SPECIFIC QUESTION] for [STATE AND COUNTY/CITY], [TAX TYPE / PROPERTY TYPE],
   applicable to [TAX YEAR AND RELEVANT DATE]. These are the known facts: [FACTS].
   Use the property-tax research skill. Search the relevant official statutes, regulations,
   and tax authority guidance, or inspect only these approved sources: [PATHS / URLs].
   Write a new evidence/rule-memo.md with pinpoint citations and links, applicable versions,
   effective dates, exceptions, unresolved facts, and the date each source was checked.
   Distinguish binding authority from explanatory guidance. Do not infer that today's rule
   applied in the earlier year. Do not decide a filing position. If access is unavailable,
   report what could not be verified and the exact source needed. Do not invent citations.
   ```

3. Select **@prompts/research.md** in Claude chat and ask it to perform the request.
   A matching normal request can select the research skill. If needed, type **/** and choose
   **property-tax-workbench:property-tax-research**, then attach the saved task.
4. Open **evidence/rule-memo.md**. Open one cited official page/PDF and find the actual passage.

**Check:** does the cited provision support the stated proposition for the specified place and
year? A correct current rule can still be inapplicable to a prior period. Keep unresolved questions
visible and route consequential interpretations through your team's review process.

**Next use:** narrow a broad multi-state question to one issue and jurisdiction, then reuse the
memo structure. [Detailed research example](03-source-backed-research.md).

## 5. Report checked results

**Result:** a small summary and chart whose numbers trace to a reconciled workbook.

1. Use the actual checked reconciliation output from session 2. If its controls failed, fix them
   before this session. In Explorer confirm its exact filename.
2. Create **prompts/report.md**, replacing the input path if a different name was produced:

   ```text
   Use only outputs/state-reconciliation.xlsx from the completed practice reconciliation.
   First check that its counts, totals, and full-population bridge agree with its source tabs.
   If they fail or cannot be checked, explain the failed control and stop before making a report.
   Create outputs/state-summary.html as a new self-contained local report with no external scripts,
   fonts, network requests, or source uploads. Audience: a reviewer of one state and period.
   Show source totals, matched differences, unmatched amounts on both sides, and unresolved causes.
   Include one clearly labeled bar chart of matched differences and an accessible data table.
   Keep zero and negative values visible. Distinguish matched net from gross differences and
   full-population difference. State the invented scope and source filename. Do not publish it.
   ```

3. Select the saved file with **@** and ask Claude to perform it. The financial-dashboard skill
   can guide presentation. No new design plugin is required for this first report.
4. Reveal the HTML file in Windows File Explorer and open it in your browser, if permitted.
   Compare its figures with Excel and try printing to preview the page. Do not upload it to a host.

**Check:** a zero matched net must not be presented as “everything reconciled.” Both unmatched
sides and the +$10/-$10 exceptions should remain visible. Avoid a pie chart for signed differences.

**Next use:** ask for one additional state or period filter only after the single-state results
are checked. Define whether totals follow the filter, then test a filter with no records.
For a Word memo or PowerPoint deck, select the installed Office capability and the same checked
source; open the output in the corresponding Microsoft app to verify layout and figures.

## 6. Repeat with a new period or state

**Result:** a reusable request you understand and can update without carrying forward stale inputs.

1. Ask Claude: **“Save the method that worked as prompts/next-reconciliation.md. Keep the control
   checks. Replace state, period, input paths, matching rules, and new output name with explicit
   placeholders. Do not execute this template.”**
2. Open that file with **Ctrl+P**. Dictate your next task into it or replace the placeholders.
   If your notes contain a correction, mark it clearly, for example “Correction: use 2027.”
3. Save with **Ctrl+S**. Read the saved state/year, filenames, key, sign, and output path yourself.
   Select it with **@** in a fresh Claude conversation and explicitly request execution.
4. Check the same controls again. Changed column names, duplicate IDs, or a different tax type
   can require a new method, not just a new date. Ask for clarification where those facts differ.

You do not reinstall personal-scope plugins for each folder. `CLAUDE.md` holds stable project
instructions; a file under `prompts` holds the current task. Neither should contain credentials.
You do not need a multi-folder `.code-workspace` file yet: one state folder opened in VS Code is
a workspace. [Saved files, dictation, and paths](../guides/14-prompt-files-and-dictation.md).

## Move to your own state project

Start after the small workbook check, whenever an approved work task is ready. Keep actual work
outside the downloaded public starter and separate from the fictional `State-Practice` folder.

In Claude chat, replace the bracketed fields and send:

```text
Prepare a new state work folder at [APPROVED FULL PATH], without overwriting existing files.
Create inputs, outputs, evidence, working, and prompts subfolders. Do not copy practice data.
Draft a short project CLAUDE.md for [STATE / LOCALITY / TAX TYPE / PERIOD]. Preserve source files,
keep evidence traceable, and mark unknown business rules as unknown. Do not assume practice keys,
tolerances, ranges, or Ohio rules. Use these actual known rules: [RULES OR NOT YET PROVIDED].
Draft prompts/first-workbook.md for a read-only map of [ONE APPROVED WORKBOOK FILENAME].
Do not access the workbook yet. Show the created full path and tell me how to open it in VS Code.
Do not install skills or change the gateway, global instructions, or other projects.
```

Then **File > Open Folder** > that new folder. Put an approved workbook copy into **inputs** using
Windows File Explorer, check its filename against the task, and run the read-only saved task.
For a huge file, first ask for sheet names, dimensions, and selected columns/ranges, not every cell
in chat. Ask for a proposed processing method before changes to complex Excel features.

**Success:** you can name the input, request the operation, locate the output, verify its evidence,
and adapt the next request yourself. Native Excel validation, business review, and actual legal
applicability remain part of the work. [Excel preservation playbook](../guides/08-excel-and-reconciliation-playbook.md).
