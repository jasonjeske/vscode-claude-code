# Lesson 4: turn checked findings into a report

[Learning home](../LEARN.md) | Previous: [Research](03-source-backed-research.md) | Next: [Adapt the template](05-adapt-to-your-work.md)

**Goal:** explain what the evidence shows, what remains open, and what someone should review next.
**You need:** Claude chat for a memo draft. Word, PowerPoint, or visual reports are later options
when the corresponding approved tools are available.

## Begin with checked findings

Use the original unique-key case from the [first-session exercise](../practice/FIRST-SESSION.md),
not its later duplicate case. You can paste these invented findings into a new conversation:

```text
Guided mode. Draft a short reviewer memo in chat from these invented findings only:
STATE-A, PERIOD-1, USD. Book: 4 rows totaling $1,000. Bill: 4 rows totaling $1,110.
Three uniquely paired properties total $600 book and $610 bill. P-002 differs by +$10.
P-004 is book-only for $400; P-005 is bill-only for $500. Paired gross difference is $10.
The complete bridge is $110 = $10 + $500 - $400. Causes have not been established.
Include scope, findings, open questions, and next verification. Cite these as supplied invented
exercise findings. Do not invent causes, approvals, payments, savings, or resolved exceptions.
```

**Look for:** all figures tied to the input, the $10 paired variance kept distinct from the $110
whole-source difference, and causes listed as questions rather than facts. “Missing from the book
extract” does not automatically mean “unrecorded liability.” The extract may have a different scope.

## Improve the wording without changing meaning

```text
Make the memo easier for a reviewer to scan. Keep the amounts, scope, uncertainties, and complete
bridge unchanged. Use short professional sentences and identify the next evidence needed.
```

Compare the revision with the original. A shorter memo is useful only if the distinctions survived.
This is also a practical test of the kit's Routine mode for established reporting.

## Decide whether a chart helps

Ask for the chart brief before building anything:

```text
Propose one chart that would help explain these invented findings. State its categories, units,
source figures, and limitations. Explain why it helps a reviewer. Do not build files yet.
```

A bridge chart could explain the signed components of the $110 difference. A pie chart cannot
represent positive and negative bridge components as ordinary shares of one whole. A clear table
may be sufficient for this small case. Never manufacture more metrics to make a report look richer.

## Choose a deliverable only when needed

| Deliverable | Use | First check |
| --- | --- | --- |
| Chat memo | No additional document skill | Trace every figure and conclusion to supplied evidence |
| Word memo | Approved `docx` skill/tooling | Open in Word and inspect headings, tables, citations, and layout |
| Slide deck | Approved `pptx` skill/tooling | Check chart labels, totals, source notes, and clipping in PowerPoint |
| Financial dashboard | Existing dashboard/reporting skills, when the work calls for one | Check metric definitions, filters, missing states, and totals |

Select the actual installed skill from the menu and use:

```text
Create [FORMAT] from the reviewed memo in [APPROVED NEW OUTPUT]. Preserve facts, figures, sources,
and open questions. Use a restrained professional layout. State which content and rendering checks
were performed. Do not install tools or publish the file.
```

These are work deliverables, not an additional learning application. The existing
[reporting playbook](../guides/09-dashboard-and-reporting-playbook.md) is available when you need it.

Next: **[Lesson 5: make the template your own](05-adapt-to-your-work.md)**.
