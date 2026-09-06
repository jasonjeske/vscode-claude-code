# Practice answer key

Use this after trying the exercise. Keep the two datasets separate.

## Main meeting workshop: four inputs

The README course uses **meeting-inputs**, not the tiny workbooks below.
All data is fictional, tax year 2026, USD.

| Check | Ohio | Texas | Total |
| --- | --- | --- | --- |
| Book amount | 90,000 | 100,000 | 190,000 |
| Bill amount | 92,000 | 101,200 | 193,200 |
| Full Bill minus Book | +2,000 | +1,200 | +3,200 |
| Unique State + Year + ID keys | 7 | 6 | 13 |
| Exact matches | 3 | 5 | 8 |
| Amount differences | 2 | 1 | 3 |
| Book-only keys | 1 | 0 | 1 |
| Bill-only keys | 1 | 0 | 1 |
| Matched net difference | 0 | +1,200 | +1,200 |
| Matched gross difference | 1,000 | 1,200 | 2,200 |

Every input workbook has six detail rows, starting at row 5, and a source-total
formula in E12. There are 24 source rows and 13 unique property keys in their union.
Exact matches are 8/13 = 61.5% rounded to one decimal. Five exceptions remain.

| Exception | Book | Bill | Matched difference |
| --- | --- | --- | --- |
| OH 010002 | 18,000 | 18,500 | +500 |
| OH 010003 | 9,000 | 8,500 | -500 |
| OH 010006 | 14,000 | Missing | Not applicable |
| OH 010007 | Missing | 16,000 | Not applicable |
| TX 020003 | 24,000 | 25,200 | +1,200 |

The bridge is +1,200 matched net +16,000 bill-only -14,000 book-only = +3,200.
No cause, filing status, or accounting adjustment is established by these examples.

The supplied [checked reconciliation](meeting-results/meeting-reconciliation.xlsx)
was opened, recalculated, and saved in Microsoft Excel on Mac. All twelve Checks
rows were OK. Its public copy has neutral author metadata; worksheet bytes are unchanged.

For the dashboard, test Ohio plus Amount difference: two rows, Book and Bill each
27,000, full and matched net zero, matched gross 1,000. Texas plus Book only has no
rows. Reset must restore the full population.

## Tiny exercises: original three workbooks

Check this after analyzing practice.xlsx. All records are invented Ohio 2026 examples.

| Check | Correct result |
| --- | --- |
| Detail rows | Book 4; Bill 4, rows 4-7 |
| Book total | $1,000 in Book D9 |
| Bill total | $1,100 in Bill D9 |
| Key | State + Tax Year + text Property ID; unique on each side |
| Matched records | 3 |
| Exact amount matches | 1: 001101, $100 on each side |
| Matched differences, Bill minus Book | 001102: +$10; 001103: -$10 |
| Matched net / gross difference | $0 / $20 |
| Book only | 001104: $400 |
| Bill only | 001105: $500 |
| Full-population difference | $1,100 - $1,000 = +$100 |
| Bridge | $0 matched net + $500 bill only - $400 book only = +$100 |
| Exception items | 4: two amount differences and two unmatched items |
| Causes, tax rates, legal treatment, deadlines | Unknown; not supplied |

D9 on each sheet is `=SUM(D4:D7)`. IDs in column C are text with leading zeros.
Three matched records do not mean three equal amounts. Missing is not zero.
The file's stored formula results match these inputs; check recalculation in Excel separately.

## Combining the two bill files

These files are a separate exercise from practice.xlsx. All amounts are invented USD.

| File | Detail rows | Text IDs | Bill total |
| --- | --- | --- | --- |
| OH-bills.xlsx | Bills rows 5-6 | 000101, 000102 | $300 |
| TX-bills.xlsx | Bills rows 5-6 | 000201, 000202 | $700 |
| Combined result | 4 | Four distinct IDs | $1,000 |

Each source total is in Bills D8, calculated with SUM(D5:D6).
The combined result must not count either Total row as a detail bill.
Keep source filename, sheet, and row references. The dashboard uses these same four
records: 4 bills, Ohio $300, Texas $700, total $1,000. A research addition must not
change these financial amounts.

Return to the [Excel lesson](../lessons/03-excel.md) when reading in the downloaded guide.
If you copied this folder on its own, keep the course open in your browser.
