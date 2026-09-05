# Synthetic dashboard exercise

Open `index.html` directly in a browser. Keep `demo-data.js` and `dashboard.js` beside it. There is
no installation, server, external library, upload, or network dependency. All twelve records are
invented. This is a learning artifact, not an accounting system or a raw-file reconciliation tool.

## Meaning of the data

Each row is one fabricated comparison record for one period. `book` and `bill` are integer USD
cents. A null bill means missing evidence, not zero liability. `STATE-A/B/C` and `PERIOD-1/2` have
no legal meaning. The two periods are separate observations; the all-period total is not a claim
about a current balance. No dates, rates, actual properties, employers, or filing requirements are
represented.

When a selection contains only missing-bill rows, the paired metrics say `No pairs`, not a zero
variance conclusion.

The fixture is already structured and paired. It does not test raw matching, many-to-many joins,
multiple currencies, bill-only rows, malicious input, or workbook feature preservation. Use a
separate approved project and expand the data contract before applying any idea to actual work.

## Answer key

| Selection | Rows | Book | Paired net difference | Paired gross difference | Book missing a bill |
| --- | ---: | ---: | ---: | ---: | ---: |
| All | 12 | $9,150.00 | $0.00 | $140.00 | $820.00 |
| PERIOD-1 | 6 | $4,500.00 | $20.00 | $120.00 | $400.00 |
| PERIOD-2 | 6 | $4,650.00 | -$20.00 | $20.00 | $420.00 |
| STATE-A / PERIOD-1 | 2 | $2,000.00 | $50.00 | $50.00 | $0.00 |
| STATE-A / PERIOD-2 / exceptions only | 0 | No data | No data | No data | No data |

Across all records, six have equal amounts, four have paired differences, and two have missing
bills. Paired book and bill totals both equal $8,330.00. The missing-bill amount is separate from
the paired variance. **Net zero does not mean no exceptions.**

Check the math with `node tests/dashboard-spec.mjs` from the repository root. The tests also cover
offsetting differences, combined filters, reset-equivalent selection, unknown bills, and an empty
result. They do not replace browser or Windows Excel testing.

## Practice

Ask Claude to explain one figure and verify it yourself from the visible rows. Change the filters
and repeat. Inspect the source code to see that all records are included in the delivered files.
Filtering does not hide data from someone who has the files.

Do not replace the fixture with work data in this public repository. For real reporting, create a
new artifact in the approved work location with its own input contract, provenance, and review.
