# First session: understand a difference and verify it

Everything on this page is wholly invented. Start in an approved practice folder outside this
public repository. The first exercise works as text, so no Excel library, database, or browsing
is needed. Use Guided mode. Do one exercise successfully before adding more tools.

## 1. Explain a tiny reconciliation

Paste the following into Claude Code. It authorizes analysis of these invented tables only.

```text
Guided mode. Reconcile these invented book and bill tables in chat. All amounts are exact USD
dollars, for STATE-A and PERIOD-1. One row means one property in that state and period.
Match exactly on Property + State + Period. Tolerance is zero. No files or external tools needed.
Do not guess matches, fill missing amounts, or hide differences. Show source counts/totals,
paired differences (bill minus book), and unmatched rows. Explain one useful verification check.

BOOK
Property | State   | Period   | Amount
P-001    | STATE-A | PERIOD-1 | 100.00
P-002    | STATE-A | PERIOD-1 | 200.00
P-003    | STATE-A | PERIOD-1 | 300.00
P-004    | STATE-A | PERIOD-1 | 400.00

BILL
Property | State   | Period   | Amount
P-001    | STATE-A | PERIOD-1 | 100.00
P-002    | STATE-A | PERIOD-1 | 210.00
P-003    | STATE-A | PERIOD-1 | 300.00
P-005    | STATE-A | PERIOD-1 | 500.00
```

### Answer key

- Book: 4 rows, **$1,000**. Bill: 4 rows, **$1,110**.
- 3 uniquely paired properties: paired book **$600**, paired bill **$610**.
- P-001 and P-003 have equal amounts. P-002 differs by **+$10**.
- Paired net difference **+$10**; paired gross absolute difference **$10**.
- P-004: book only, **$400**. P-005: bill only, **$500**.
- Whole-source bridge: **$1,110 - $1,000 = $10 + $500 - $400 = $110**.
- Every source row is accounted for. The difference is explained as comparison categories, not
  resolved as an approved accounting adjustment. No legal rule or tax treatment is established.

The useful lesson: equal paired amounts alone do not prove the complete population reconciles.
Both unmatched sides must remain visible.

## 2. Introduce one duplicate

Continue the same conversation:

```text
In the invented BILL table, append an identical second P-002 row for 210.00.
Explain what this changes before calculating a new matched result. Do not silently deduplicate.
```

Expected: bill now has 5 rows and totals **$1,320**. P-002 has a nonunique bill key, so its match
must be marked ambiguous under the unique-match rule. Claude should not duplicate the $200 book
amount through a join or discard the extra bill without an approved rule. The two unambiguous
pairs P-001/P-003 still total **$400 per side**. The duplicate population needs a decision.

If `reconciliation-control-review` is installed, ask it to review the original comparison using
the stated scope, exact keys, zero tolerance, and answer key. Controls without evidence must remain
UNVERIFIED; the existence of an explained exception does not authorize changing the books.

## 3. Try a new workbook, only after XLSX is ready

In the installed skill menu, select the reviewed Anthropic XLSX skill and use this request with
the original four-row tables above:

```text
Create a new workbook in the approved practice folder using only these invented tables. Include
Source Book, Source Bill, Comparison, Exceptions, and Controls sheets. Keep IDs as text and USD
amounts exact. Show formulas and independent control totals. Preserve unknowns for unmatched rows.
State the calculation engine actually used and checks still requiring native Excel. Do not
install tools or overwrite any existing file. Stop if required tooling is unavailable.
```

Open the result in native Excel. Check the answer-key totals, formula ranges, ID formatting,
unmatched rows, and calculated values. Do not enable macros or refresh connections. This plain
example is not proof that the tool preserves a complex production workbook's features.

## 4. Inspect a dashboard with different invented data

Open `examples/dashboard/index.html` from the downloaded starter. It uses a separate 12-row
fixture; its totals intentionally differ from this exercise. Check the
[dashboard's own answer key](../examples/dashboard/README.md), then try state, period, and exception
filters. Explain how gross differences reveal offsets that a net difference can hide.

To change its appearance, copy the complete three-file example into the practice folder, keep a
baseline copy, and request one specific improvement. Do not add real data to the public starter.

## Ready to continue?

The user can locate the skill menu, explain the unmatched rows, spot a duplicate key, and compare
output with an independent check. Record usage if available and one useful lesson. Then choose the
next task from [daily use](../guides/DAILY-USE.md) or the [learning path](../guides/10-four-week-learning-path.md).
