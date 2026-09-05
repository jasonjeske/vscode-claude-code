# State practice answer key

Use after attempting the checks in [the state workflow](../learn/STATE-WORKFLOW.md).
These expectations apply only to the supplied invented `state-practice.xlsx`.

| Control | Expected result |
| --- | --- |
| Detail rows | Book 4; Bill 4, rows 4-7 only |
| Source totals | Book $1,000; Bill $1,100 |
| Matching key | State + tax year + text property ID; unique within each side |
| Matched records | 3: 001101, 001102, 001103 |
| Matched source totals | Book $600; Bill $600 |
| Matched Bill minus Book | 001101: $0; 001102: +$10; 001103: -$10 |
| Positive / negative / net / gross matched differences | +$10 / -$10 / $0 / $20 |
| Book only | 001104, $400 |
| Bill only | 001105, $500 |
| Full-population difference | $1,100 - $1,000 = +$100 |
| Full bridge | matched net $0 + bill-only $500 - book-only $400 = +$100 |
| Causes and legal treatment | Unknown; not supplied by this workbook |

**Three matched records do not mean three equal amounts.** Only 001101 agrees exactly. The two
opposing differences cancel in the net, but both still require investigation. An absent record
is not evidence of a zero balance. Do not silently drop it with an inner join.

The source totals are `=SUM(D4:D7)` in D9 on each sheet. Property IDs are stored as text with
leading zeros; do not convert them to numeric matching keys. A six-digit display format is also
present, but display formatting alone would not establish text storage.

After revising the exception request to 001103, source cells are Book D6 = $300 and Bill D6 =
$290, giving -$10. Its cause remains unknown. The earlier +$10 note must stay unchanged.
