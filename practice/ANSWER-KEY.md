# Practice answer key

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
