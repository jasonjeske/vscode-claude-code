# Meeting check details

FICTIONAL TRAINING DATA - NOT TAX ADVICE. Invented tax year 2026 book accruals and bills in USD. This note is a check record, not a conclusion about any real property.

Workbook checked: `outputs/meeting-reconciliation.xlsx` (read only, not changed). Run date: 2026-09-06. Scope: `MY-MEETING.md` (read for scope only). Source rows re-read from `practice/meeting-inputs/` (OH-book, OH-bills, TX-book, TX-bills). Companion checklist: `outputs/meeting-checklist.md`. This run replaces the earlier 18:10 versions of both notes.

Reader used: the SheetJS library through bun, reading formulas and cached values separately. The review used the system environment rather than the project Python environment. Excel itself was not opened by this review. Excel did have the workbook open during the run (a lock file and an open file handle were present), so the copy read is the saved file on disk; anything typed in Excel and not yet saved is not in this note.

## Workbook map

| Sheet | Used range | Rows used | Hidden | Purpose |
| --- | --- | --- | --- | --- |
| Source data | A1:J32 | 32 | No | Detail sheet: one row per source record, with file, sheet and source row (rows 5 to 28), totals at I30:I32 |
| All properties | A1:I20 | 20 | No | One row per key State + Tax year + Property ID (rows 5 to 17), totals at F19:H19, row count F20 |
| Exceptions | A1:J12 | 12 | No | Every non-exact row (rows 5 to 9), count F11, expected count F12 |
| State totals | A1:E24 | 24 | No | Totals, the four measures and the bridge, by state and total (B to D) |
| Checks | A1:E16 | 16 | No | Twelve checks, D5:D16, each OK or CHECK |

All five expected sheets are present. Detail rows: 24. Property IDs are stored as text with leading zeros (for example 010001). Formula cells: 206, all with a cached value, so none read blank.

## Source files re-read

Each source file holds six detail rows (rows 5 to 10) and a Source total at E12. In the saved files that E12 cell holds the formula `=SUM(E5:E10)` with no computed value stored, so a file reader shows nothing (or 0) there. The file totals below were therefore summed from rows 5 to 10 directly, then compared with the typed Expected values on the Checks sheet.

| File | Detail rows | Recomputed sum USD | Checks!C cell | Workbook value | Result |
| --- | --- | --- | --- | --- | --- |
| OH-book.xlsx | 6 | 90,000 | Checks!C6 | 90,000 (B6 via 'Source data') | OK |
| OH-bills.xlsx | 6 | 92,000 | Checks!C7 | 92,000 | OK |
| TX-book.xlsx | 6 | 100,000 | Checks!C8 | 100,000 | OK |
| TX-bills.xlsx | 6 | 101,200 | Checks!C9 | 101,200 | OK |

Row by row, all 24 detail rows on 'Source data' match the source files on state, tax year, property ID, name and amount. Row-level mismatches: 0.

## Checks, recomputed from detail rows and compared with the workbook

| Check | Recomputed | Workbook | Cell read | Result | What it proves |
| --- | --- | --- | --- | --- | --- |
| Detail rows copied | 24 | 24 | 'Source data'!I32, Checks!B5:C5 | OK | Only detail rows were copied, no Source total rows |
| Book total, detail sheet | 190,000 | 190,000 | 'Source data'!I30 | OK | Sum of the 12 Book rows |
| Bill total, detail sheet | 193,200 | 193,200 | 'Source data'!I31 | OK | Sum of the 12 Bill rows |
| Book total, per-key sheet | 190,000 | 190,000 | 'All properties'!F19 | OK | Every Book amount landed on one key row |
| Bill total, per-key sheet | 193,200 | 193,200 | 'All properties'!G19 | OK | Every Bill amount landed on one key row |
| Duplicate keys within a side | 0 | 0 | Checks!B14 | OK | Matching is one-to-one |
| Key rows | 13 | 13 | 'All properties'!F20, 'State totals'!D11 | OK | One row per key |
| Statuses add up to key count | 8 + 3 + 1 + 1 = 13 | 13 | 'State totals'!D12:D15, Checks!C12 | OK | Every key has exactly one status |
| Exceptions listed | 5 | 5 | Exceptions!F11, F12 | OK | Exceptions sheet is complete |
| Exception keys agree | OH 010002, 010003, 010006, 010007; TX 020003 | same | Exceptions!A5:C9 | OK | No non-exact row is missing or extra |
| OH full difference | 2,000 | 2,000 | 'State totals'!B9 | OK | Bill total minus Book total |
| TX full difference | 1,200 | 1,200 | 'State totals'!C9 | OK | Bill total minus Book total |
| Total full difference | 3,200 | 3,200 | 'State totals'!D9 | OK | Bill total minus Book total |
| Matched positive differences | 500 / 1,200 / 1,700 | same | 'State totals'!B17:D17 | OK | Bill above Book, pairs only |
| Matched negative differences | -500 / 0 / -500 | same | 'State totals'!B18:D18 | OK | Bill below Book, pairs only |
| Matched net difference | 0 / 1,200 / 1,200 | same | 'State totals'!B19:D19, 'All properties'!H19 | OK | Positive plus negative |
| Matched gross difference | 1,000 / 1,200 / 2,200 | same | 'State totals'!B20:D20 | OK | Sum of absolute differences |
| Book-only USD | 14,000 / 0 / 14,000 | same | 'State totals'!B21:D21 | OK | Book amounts with no bill |
| Bill-only USD | 16,000 / 0 / 16,000 | same | 'State totals'!B22:D22 | OK | Bill amounts with no book row |
| Bridge | 2,000 / 1,200 / 3,200 | same | 'State totals'!B23:D23 | OK | Matched net + Bill-only - Book-only |
| Bridge minus full difference | 0 / 0 / 0 | 0 / 0 / 0 | 'State totals'!B24:D24, Checks!B16 | OK | The bridge explains the whole difference |
| Checks sheet cached results | 12 OK expected | 12 OK | Checks!D5:D16 | OK | Cached values only, not a live recalculation |

Values in the three-part cells read OH / TX / Total. No check reads CHECK.

## Four measures, kept separate

| Measure | OH | TX | Total | Cells |
| --- | --- | --- | --- | --- |
| Full difference, Bill minus Book | 2,000 | 1,200 | 3,200 | 'State totals'!B9:D9 |
| Matched net difference | 0 | 1,200 | 1,200 | 'State totals'!B19:D19 |
| Matched gross difference | 1,000 | 1,200 | 2,200 | 'State totals'!B20:D20 |
| Book-only items, count | 1 | 0 | 1 | 'State totals'!B14:D14 |
| Book-only items, USD | 14,000 | 0 | 14,000 | 'State totals'!B21:D21 |
| Bill-only items, count | 1 | 0 | 1 | 'State totals'!B15:D15 |
| Bill-only items, USD | 16,000 | 0 | 16,000 | 'State totals'!B22:D22 |

These are never added together. Matched net and matched gross use the three matched pairs only. A blank Book or Bill cell is a missing record, not zero.

## Exception rows with source references

| State | Tax year | Property ID | Book USD | Bill USD | Bill minus Book | Status | Source file and row |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OH | 2026 | 010002 | 18,000 | 18,500 | +500 | Amount difference | OH-book.xlsx Book row 6; OH-bills.xlsx Bills row 6 |
| OH | 2026 | 010003 | 9,000 | 8,500 | -500 | Amount difference | OH-book.xlsx Book row 7; OH-bills.xlsx Bills row 7 |
| OH | 2026 | 010006 | 14,000 | blank | blank | Book only | OH-book.xlsx Book row 10 |
| OH | 2026 | 010007 | blank | 16,000 | blank | Bill only | OH-bills.xlsx Bills row 10 |
| TX | 2026 | 020003 | 24,000 | 25,200 | +1,200 | Amount difference | TX-book.xlsx Book row 7; TX-bills.xlsx Bills row 7 |

Workbook rows: Exceptions!A5:J9 and All properties rows 6, 7, 10, 11 and 14. No cause is supplied for any row; the inputs hold amounts only.

## Unresolved items

Questions for the meeting, not conclusions. Owners are Not provided in the inputs.

1. OH 010002: which amount is right, 18,000 or 18,500?
2. OH 010003: which amount is right, 9,000 or 8,500?
3. OH 010006: booked at 14,000 with no bill. Is a bill expected?
4. OH 010007: billed at 16,000 with no book row. Should it be booked?
5. TX 020003: which amount is right, 24,000 or 25,200?
6. Native Excel recalculation was not seen this run.

## Recalculation status

UNVERIFIED. Formulas and cached values were read with a file library, which is not a native Excel recalculation. Every recomputed figure agrees with the cached figure, and Checks!D5:D16 all cache OK, but the workbook is confirmed only when it is opened in Excel and the Checks sheet is seen. One check for the reader: open the Checks sheet and confirm D5:D16 all say OK, then confirm 'State totals'!D24 is 0.
