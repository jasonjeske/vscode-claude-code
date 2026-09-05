# Reconciliation project instructions

Review and merge into `CLAUDE.md` at the root of a separate approved work project. Fill bracketed
items locally. Unknown items remain unresolved; they are not permission to invent defaults.

## Objective and scope

Produce [workpaper and exception report] comparing [SOURCE-A] with [SOURCE-B] for [PERIOD].
Reviewer role: [ROLE]. Included entities/jurisdictions/property types: [SCOPE]. Exclusions: [LIST].
Reporting date, tax year, valuation date, and extraction cutoff: [DEFINE SEPARATELY].

## Data contract

- Each A row represents [GRAIN]; each B row represents [GRAIN].
- Input versions and source priority: [SOURCE LABELS, VERSION RULE, CONFLICT RULE].
- Approved exact keys: [COMPONENTS]. Required uniqueness: [PER SOURCE].
- Approved grouping or installment/payment allocation: [RULE OR NONE].
- Identifier types, date meaning, currency, unit, signs, and rounding: [RULES].
- Numeric tolerance: [VALUE AND PURPOSE OR UNRESOLVED]. Materiality: [SEPARATE POLICY].
- Input, working-copy, output, and evidence locations: [APPROVED LOCAL LABELS].

## Method

Inventory and profile before transforming. Preserve originals. Check key uniqueness before joins.
Never force matches, silently drop duplicates, replace unknowns with zero, or aggregate across
currencies. Keep original keys alongside normalized keys. Fuzzy matches require a separate rule
and human acceptance. Keep detail and subtotal populations separate.

## Controls

For each source, original rows and amounts must equal the totals in its mutually exclusive
classified populations. Report paired equal, paired unequal, A-only, B-only, ambiguous duplicates,
and invalid keys. Show paired signed and absolute differences, plus unmatched amounts separately.
Record every failed or unavailable check. A zero net difference is not sufficient for completion.

## Excel preservation

Workbook features that must survive: [FORMULAS, PIVOTS, QUERIES, MACROS, LINKS, OTHER].
Approved reader/writer and calculation engine: [TOOLS AND VERSIONS OR UNKNOWN].
Native Excel checks: [RECALCULATION, REFRESH, FEATURE COMPARISON, REOPEN].
Do not refresh external data or run macros without the relevant approval. Never save over inputs.

## Output and review

Create new outputs only within the approved plan. Deliver the comparison, exception register,
source identity, transformation/query, control results, and review status. Each exception needs
source reference, reason/evidence, status, reviewer role, and next action. Separate supported
explanations from hypotheses. Do not post journal entries, pay, file, submit, or sign off.

Teaching mode: [Guided/Teach/Routine]. Explain one new concept and one verification step when useful.
Commands: [ONLY VERIFIED PROJECT COMMANDS, OR NONE].
