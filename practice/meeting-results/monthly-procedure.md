# Monthly property-tax review: procedure for a new colleague

Who this is for: someone doing the monthly book-to-bill review for the first time, using the Claude Code extension in VS Code. No programming needed. You describe the work in normal language, open the results, and check them.

What you start with: the four input workbooks in `practice/meeting-inputs/`: OH-book.xlsx, OH-bills.xlsx, TX-book.xlsx, TX-bills.xlsx. What you finish with: a checked reconciliation workbook and a meeting pack (a one-page Word briefing and a short PowerPoint), all saved in `outputs/`.

Ground rules: never edit the input files; save everything new in `outputs/`; label practice data as fictional; treat a difference as a question, never as a cause; keep property IDs as text so leading zeros survive.

## 1. Inspect

Ask for a map of each input file before combining anything: sheets, how many detail rows, the file's own total, hidden content, and anything unusual.

Check: the detail rows of each file add up to that file's printed total. Note the four totals; you will tie to them later.

## 2. Reconcile

Ask for one workbook that combines the four files and matches book to bill by State, Tax year, and Property ID. Ask for these sheets: source detail rows with file, sheet, and row; one row per property; exceptions; state totals with the bridge; and a checks sheet.

Check: on the checks sheet every row reads OK. Every property has exactly one status: exact match, amount difference, book only, or bill only. A blank side is a missing record, not zero.

## 3. Verify

Ask for the monthly meeting review. It rereads the workbook, recomputes the totals from the detail rows, and writes `outputs/meeting-checklist.md` with the details in `outputs/meeting-check-details.md`.

Check: the four measures stay separate: full difference (bill total minus book total), matched net, matched gross, and missing counterparts. The bridge, matched net plus bill-only minus book-only, equals the full difference. Open the workbook in Excel yourself and confirm the checks sheet, because a file library cannot recalculate Excel formulas.

## 4. Present

Ask for a one-page Word briefing and five slides for a five-minute meeting: totals, a state comparison, the exceptions, the bridge, and the questions to resolve. Amounts must match the workbook.

Check: open both files. Compare every number with the state totals sheet. Percentages show one decimal place. Every open item is a question with an owner named or marked Not provided.

## 5. Save next steps

Ask for a short reviewer note: what was done, what was not verified, and the open questions. Keep the checklist, the details note, and the reviewer note together in `outputs/`.

Check: a colleague who opens `outputs/` cold can find the workbook, the meeting pack, and the open items without asking you.

## If something looks wrong

Say what you see and where. A check that reads CHECK, a total that does not tie, or a blank that became a zero is a stop, not a detail to smooth over. Ask for the fix, then rerun step 3 before presenting.
