# Skill selection checks

These cases are a manual protocol for Claude Code in VS Code, not an automated model benchmark.
All runtime cases remain **NOT RUN**. Static frontmatter checks establish only that the six
bundled skills permit model selection and remain user-invocable. Track target-PC results in W36.

Run in a disposable approved practice project with synthetic inputs and the updated personal
skill copies. Use a fresh conversation for each case to avoid a previously loaded skill biasing
selection. Record version, allowed model, any managed overrides, actual invocation activity where
visible, output, and unmet checks in local notes. Do not turn six cases into a daily ritual.

| Skill | Matching request | Expected task boundary | Nearby request that should not select this skill |
| --- | --- | --- | --- |
| prompt-coach | Help me write a short prompt for a read-only workbook review. Draft only. | Drafts a prompt and teaches one habit; does not open files or execute the draft | Review this selected workbook now |
| structured-work-request | Help me scope a complex reconciliation assignment through a guided interview | Reuses supplied details; asks one material gap at a time; does not perform the work | Rewrite this one-sentence prompt more clearly |
| excel-workbook-review | Review the selected synthetic workbook's sheets, formulas, and preservation risks, read-only | Identifies actual structure and coverage limits; does not save or refresh | Explain the pasted formula =210-200 without reading files |
| reconciliation-control-review | Review this prepared synthetic comparison against these exact keys and control totals | Reports PASS/FAIL/UNVERIFIED with evidence; no record edits | Build a new reconciliation from two exports |
| property-tax-research | Research a supplied official source's property-tax rule for the stated locality and year | Gives applicable citations and missing facts; uses only supplied sources when browsing is not allowed | Calculate the difference between these two invented amounts |
| financial-dashboard | Plan a local accounting dashboard using this synthetic summary and defined metrics | Defines metrics and output; respects agreed writing scope and no-publication rule | What is the sum of 200 and 210? |

For each case, verify the useful result as well as selection. A self-reported skill name is not
sufficient evidence of an invocation. If the installed extension does not expose invocation
activity, record selection as UNVERIFIED, then run the actual slash-menu command to check its
observable behavior. Do not label a normal correct answer as proof of skill loading.

Also check:

1. **No forced routing:** a simple arithmetic question does not begin an interview, research task,
   workbook scan, or dashboard build.
2. **Task change:** after Prompt Coach drafts a request, start a fresh conversation for execution.
   In a separate changed-task trial, ask for a simple calculation after a skill task; stale loaded
   instructions must not cause the former workflow to continue.
3. **Input versus procedure:** selecting `@prompts/example-task.md` is not itself a request to run
   a skill. Saving the file in the editor does not execute it.
4. **Old installation:** an old manual-only copy stays manual until replaced. Preserve and verify
   its backup outside discovery, update the complete folder, compare the installed source, then
   repeat one matching request and one slash selection.
5. **Unavailable tools:** with no XLSX reader/runtime, the skill reports the missing capability.
   It must not invent sheet contents, install tools unasked, or claim a successful workbook check.
6. **Office package:** independently test the README plugin UI route and Lesson 2 workbook
   exercise. Confirm the created file, formula bar, 10/Missing input/-200 cases, and reopening in
   native Excel. This does not validate advanced feature preservation.

A missed automatic selection can be handled with slash selection. An incorrect output or scope
violation needs correction before real use, even when the correct skill was invoked. Automatic
selection is optional model behavior, not a guarantee in the published guide.
