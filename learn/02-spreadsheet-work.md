# Lesson 2: understand and check a spreadsheet

[Learning home](../LEARN.md) | Previous: [First conversation](01-first-conversation.md) | Next: [Research](03-source-backed-research.md)

**Goal:** inspect before editing, understand a formula, and verify a comparison.
**You need:** Claude chat for the text exercises; an approved file reader for workbook inspection.
Workbook creation requires the approved XLSX tools and native Excel checks described in setup.

## Apply it to today's work

Choose one operation: explain a formula **or** investigate one exception. Work from an approved
copy in the separate work folder. Use the tiny example below only if that operation is new.

```text
Guided mode. Using only [APPROVED WORKBOOK/SOURCE REFERENCES], help me [EXPLAIN ONE FORMULA /
DRAFT ONE EXCEPTION NOTE] for [SHEET, CELL OR RECORD; PERIOD]. Read-only; preserve originals.
Follow [KNOWN MATCH/SIGN RULES]. Give the useful explanation or note, cite the actual input
locations, and show the calculation if supported. Explain one unfamiliar step briefly.
Identify missing evidence; do not infer a cause or claim the whole workbook reconciles.
Give me one check I can perform in Excel. Do not refresh connections or run macros.
```

**Your part:** open the cited source and trace the inputs yourself. Report any mismatch specifically.
**Keep:** the checked explanation or exception note in the approved workpaper, including gaps.
**Next similar task:** write the request and name the check before looking back. Try a blank input
or duplicate key as a changed case; a method that silently treats either as resolved needs correction.

![An invented comparison with three paired properties, one book-only property, and one bill-only property. The complete $110 difference is $10 paired difference plus $500 bill-only minus $400 book-only.](../assets/learning/reconciliation-map.svg)

*Original diagram of the [first-session exercise](../practice/FIRST-SESSION.md). All amounts are invented USD dollars.*

## First understand what you have

If `excel-workbook-review` is installed, select one approved synthetic workbook and use:

```text
/excel-workbook-review
Guided mode. Inspect only the selected synthetic workbook, read-only. Explain the purpose of each
sheet, identify the main tables and formulas, and list hidden or advanced features the tools can
actually inspect. Do not save, recalculate, refresh connections, or run macros. Explain one risk.
```

**Look for:** a sheet map, formula/cache distinctions, and explicitly unverified features. A reader
that cannot inspect Power Query should not say the workbook has no Power Query.

Without that skill, ask for the same bounded review in ordinary language. Without a file reader,
continue with the text example below; do not install software automatically to finish the lesson.

## Learn a formula on a tiny example

```text
Teach mode. In an invented sheet, A1 is Property, B1 is Book, and C1 is Bill. Row 2 contains
P-002, 200, and 210. Explain =C2-B2 in D2. What changes if C2 is blank rather than 210?
Suggest a way to make a missing input visible. Do not treat a missing bill as evidence of zero tax.
```

**Check:** with the supplied numbers the difference is **10**. Direct subtraction can treat an
empty referenced cell as zero, making the result look like **-200**. That is a formula result,
not proof that the bill is zero. For this tiny numeric example, one visible missing-input guard is:

```excel
=IF(OR(B2="",C2=""),"Missing input",C2-B2)
```

Test the formula in a practice copy in Excel with 210, an empty C2, and a numeric zero in C2.
Expected results: **10**, **Missing input**, and **-200**. This example does not validate text amounts,
errors, or every import format. For larger work, separate numeric results and exception statuses
into separate columns so charts and totals do not mix numbers with status text. Formula names and
separators can vary with Excel's language/locale.
[Microsoft: checking blank inputs](https://support.microsoft.com/en-us/excel/using-if-to-check-if-a-cell-is-blank),
[subtracting numbers](https://support.microsoft.com/en-us/excel/subtract-numbers-in-excel).

## Compare complete populations

Open the [first-session exercise](../practice/FIRST-SESSION.md). Copy its original BOOK and BILL
tables and run the first two steps, including the deliberate duplicate. Its answer key is your
independent check; the diagram above summarizes only the original unique-key case.

**Look for:** source totals, paired differences, both unmatched sides, and a visible duplicate-key
problem in the second step. Matching on property alone is insufficient if the same identifier can
appear in different jurisdictions or years. Define what one row represents before choosing keys.

## Move to a workbook only when the method is clear

Use step 3 of the exercise for a new workbook with approved XLSX tools. Open it in Excel, inspect
the formulas and answer-key totals, and check that identifiers remain text. A formatted workbook
is not proof that the formulas were calculated correctly.

An existing workbook with PivotTables, slicers, Power Query, VBA, or links needs additional feature
checks on a copy. Learn the available method in the [Excel playbook](../guides/08-excel-and-reconciliation-playbook.md).
Do not rebuild or convert a complex original just to follow this lesson.

Next: **[Lesson 3: research a specific rule](03-source-backed-research.md)**.
