# Lesson 3: research a specific rule

[Learning home](../LEARN.md) | Previous: [Spreadsheet work](02-spreadsheet-work.md) | Next: [Reports](04-reports.md)

**Goal:** ask a precise research question and check the evidence supporting the answer.
**You need:** Claude chat for the invented example; approved browsing or supplied official sources
for actual legal research. The `property-tax-research` skill is helpful but does not provide access.

## Apply it to today's work

Start with one narrow provision you need to understand, not a survey of every state. Use the
real-question prompt below with approved facts and sources. The fictional counting exercise is
optional when you need practice distinguishing the rule from its application.

**Useful output:** one cited provision, the applicable year/locality, and unresolved facts for review.
**Your part:** open that citation and follow the five checks below. Identify one supporting phrase
in the source yourself. Ask Claude to correct the specific claim if the source does not support it.
**Keep:** the reviewed source note and gaps in approved work storage; a draft is not a filing position.
**Next similar task:** state the required jurisdiction, year, and evidence before reopening the prompt.
Change the tax year as a practice variation. Reuse the research method, never assume the same rule applies.

## Start with a source-reading exercise

Paste this exercise as text. It is deliberately fictional and must never enter a real calendar.

```text
Teach mode. The following is an INVENTED TRAINING RULE, not a law:
"A request must be received within 10 calendar days after the notice date. Exclude the notice
date when counting. This exercise has no weekend or holiday adjustment."
The invented notice date is April 2, 2030. No other facts apply.
Explain the conditional due date, show the counting, and identify the phrase that makes receipt
different from mailing. Do not browse or present this as a real jurisdiction's rule.
```

**Answer key:** April 3 is day 1, so April 12, 2030 is day 10. The word **received** means this
fictional instruction is not satisfied merely by mailing on day 10. This establishes no actual
filing deadline. Real questions require the applicable law, event evidence, and adjustment rules.

## Ask a real research question precisely

For a permitted research task, replace the placeholders below with a public jurisdiction and
approved neutral facts. Use generic external search terms, never internal property/account IDs.

```text
/property-tax-workbench:property-tax-research
Guided mode. Research [SPECIFIC REQUIREMENT] for [PROPERTY TYPE] in [STATE AND LOCALITY] for
[TAX YEAR]. The relevant approved facts are [NEUTRAL FACTS]. Use approved official sources.
Explain the rule, exceptions, effective period, local implementation, and missing facts. Cite
exact sections/pages. Return a short memo for reviewer use, not a final filing position.
```

If the skill is not installed, omit the slash-command line and keep the request. If browsing is
unavailable, supply approved official documents and ask for source-limited analysis. Missing
access should remain visible, not be replaced by a confident claim from memory.

## Check one citation yourself

1. Open the linked source or approved document reference.
2. Locate the cited section/subsection or page. Does it actually contain the stated rule?
3. Check whether it applies to the jurisdiction, property category, and requested tax year.
4. Read the surrounding definitions and exceptions. A headline or search snippet is insufficient.
5. Check what remains unknown: local implementation, historical version, event date, or a fact
   such as ownership/use. Ask the reviewer about a conflict rather than silently choosing a source.

Use this correction when necessary:

```text
The source you cited appears to be a different year's version. Locate the version applicable
to the requested year if approved access permits. Otherwise mark applicability unresolved.
Keep any unaffected findings and show the specific source gap.
```

## Learn what the status means

SUPPORTED, PARTIAL, UNRESOLVED, and CONFLICT describe the research evidence. They are not approval
of an exemption or filing position. “Not located” does not mean “no filing requirement.”

For historical questions, distinguish the retrieval date from the rule's effective period. For
real deadlines, confirm the trigger, counting method, holidays/extensions, and receipt/postmark
rules before calculating. The [research guide](../guides/12-property-tax-research.md) and
[memo template](../skills/property-tax-research/references/research-memo.md) provide the full method.

Next: **[Lesson 4: turn checked findings into a report](04-reports.md)**.
