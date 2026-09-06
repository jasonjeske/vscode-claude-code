# Meeting checklist

FICTIONAL TRAINING DATA - NOT TAX ADVICE. Invented tax year 2026 amounts in USD.

Files: `outputs/meeting-reconciliation.xlsx` (read only, unchanged), `MY-MEETING.md` for scope, source files in `practice/meeting-inputs/`. Details: `outputs/meeting-check-details.md`.

**Result:** every check ties, none reads CHECK. Totals stay UNVERIFIED until the Checks sheet is viewed in Excel.

## Four measures, kept separate

| Measure | OH | TX | Total | Cells |
| --- | --- | --- | --- | --- |
| Full difference, Bill minus Book | 2,000 | 1,200 | 3,200 | 'State totals'!B9:D9 |
| Matched net difference | 0 | 1,200 | 1,200 | 'State totals'!B19:D19 |
| Matched gross difference | 1,000 | 1,200 | 2,200 | 'State totals'!B20:D20 |
| Book-only items, count / USD | 1 / 14,000 | 0 / 0 | 1 / 14,000 | 'State totals'!B14:D14, B21:D21 |
| Bill-only items, count / USD | 1 / 16,000 | 0 / 0 | 1 / 16,000 | 'State totals'!B15:D15, B22:D22 |

Book total 190,000, Bill total 193,200 ('State totals'!D6, D8). Blank means missing record, not zero; never add the measures.

## Unresolved items (questions, not causes; owners Not provided)

1. OH 010002: book 18,000, bill 18,500 (+500). Which side is right?
2. OH 010003: book 9,000, bill 8,500 (-500). Which side is right?
3. OH 010006: book 14,000, no bill. Is a bill expected?
4. OH 010007: bill 16,000, no book row. Should it be booked?
5. TX 020003: book 24,000, bill 25,200 (+1,200). Which side is right?
6. Excel recalculation UNVERIFIED (file reader only); Excel had the workbook open, saved copy read.

## Open in Excel

1. Checks sheet: D5:D16 all read OK.
2. 'State totals'!D24 (bridge minus full difference) shows 0.
3. 'All properties'!F11 (OH 010007 Book) is blank, not 0.
