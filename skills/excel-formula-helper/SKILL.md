---
name: excel-formula-helper
description: Explain, create, or debug an Excel formula for accounting tasks and test it on small examples. Use for lookups, conditional totals, variance calculations, and missing-value checks.
---

# Explain and check one Excel formula

Explain the next useful action plainly; do not require a skill command. Identify the intended result, input columns/ranges, output cell, data types,
and material business rules. Ask for Excel version/language when function availability or syntax
matters. Keep the requested task small; do not turn a formula question into a workbook-wide audit.

Preserve originals. Explain a proposed formula before changing files; write a new practice workbook
only when requested. Use available approved spreadsheet tools and the xlsx skill when useful.
Do not install dependencies, run macros, or refresh connections without authorization.

For lookups, check exact/approximate matching, duplicate keys, unmatched items, leading-zero text
IDs, and whether the source is unique at the required grain. Do not silently choose the first
of ambiguous matches. For sums, distinguish detail from subtotal rows, inclusion rules, visible
versus all rows, and missing from zero. For differences, state direction and preserve signs.
Do not wrap every failure in IFERROR(...,0); it can conceal missing or invalid inputs.

Provide the formula, exact paste location, and plain explanation of its parts. Show how relative
and absolute references behave when filled down. Test relevant normal, zero, negative, missing,
duplicate, and boundary cases with independently derived expected results. Distinguish actual
blank cells, formula-produced empty strings, whitespace, numeric text, and errors when relevant.

If generating a practice file, keep input, expected, and calculated-result columns distinct. Check
that the workbook reopens and formulas reference the intended cells. Native Excel or a compatible
calculation engine must run before claiming calculated values were verified; writing formula text
or cached results does not prove recalculation. Label checks not run UNVERIFIED and give a manual
Excel check. State any function/separator compatibility limits without inventing a user version.

Return one usable formula or focused explanation, test evidence, unresolved assumptions, output
path if any, and the learner's next click. Do not derive tax rates or legal rules from the formula.
