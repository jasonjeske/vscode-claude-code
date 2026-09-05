# Research state and local property-tax questions

Use the optional [`property-tax-research`](../skills/property-tax-research/SKILL.md) skill for
specific legal research: property classification, exemption conditions, reporting requirements,
assessment procedures, deadlines, historical treatment, or changes between tax years. It produces
a cited research memo or comparison table for review. It does not contain a precomputed tax-law
database, provide a legal-research subscription, or grant web access.

## Add it when the first real research task arrives

Follow [the local installation instructions](07-trusted-skills-and-installation.md). Copy the
**complete** `skills/property-tax-research/` folder, including `references/`, into the approved
personal or project `.claude/skills/` folder. The personal Windows entrypoint is
`%USERPROFILE%\.claude\skills\property-tax-research\SKILL.md`.

Invoke `/property-tax-research` explicitly. After the README setup, add this skill when a law-research task needs it; it is optional.
Use existing employer-approved browsing or supplied official documents. If the gateway or managed
tools cannot access the web, it should return source-limited analysis and list missing checks.
Installation does not change those access controls.

## Start with one precise issue

Replace placeholders with a public jurisdiction and neutral facts. Never put account numbers,
internal property identifiers, privileged documents, or confidential business facts in web queries.
Real work inputs and saved results belong in an approved work location, not this public repository.

```text
/property-tax-research
Guided mode. Research whether [SPECIFIC PROPERTY CATEGORY] has an annual reporting requirement
in [STATE AND LOCAL JURISDICTION] for [TAX YEAR], using [NEUTRAL OWNERSHIP/USE FACTS]. Use approved
official sources. Explain the rule, exceptions, local requirements, and missing facts. Cite exact
provisions and their effective periods. Return a short memo in chat and teach me one research habit.
```

Use these variations after the first successful task:

| Task | Add to the prompt |
| --- | --- |
| Exemption | Separate eligibility, application, renewal, and evidence requirements; identify unknown facts without declaring approval. |
| Historical question | Compare the versions applicable to [YEAR A] and [YEAR B], including amendments and transition provisions. |
| Deadline | Identify the legal trigger, required evidence, counting rule, adjustments, and filing-method rules; calculate only when those are established. |
| State comparison | Research [NAMED JURISDICTIONS] independently at the same scope; one issue/year per row, including partial and unresolved results. |
| Rule change | Compare [OLD SOURCE] with current applicable authority and list potentially affected workpapers for review without changing them. |
| Conflicting sources | Preserve both sources, distinguish their legal force and applicable periods, and explain the unresolved question. |

Start with two jurisdictions before expanding a comparison. Review the first rows for consistent
definitions and complete citations. Larger studies need explicit coverage tracking, not a claim
that every state's law was checked because a table contains 50 rows.

## What a useful answer looks like

The [included memo format](../skills/property-tax-research/references/research-memo.md) leads with
the answer and carries a source register, pinpoint citations, effective periods, fact gaps, and
review questions. Each issue is SUPPORTED, PARTIAL, UNRESOLVED, or CONFLICT. These labels describe
evidence coverage; they do not approve a filing position.

Review whether the cited provision actually supports the claim, applies to the property and tax
year, and includes relevant exceptions. Check the local implementing authority as well as the
state. Retrieval date and effective date answer different questions. Where case law matters,
unavailable case-treatment checks must remain visible.

For exemption work, combine the skill with the
[exemption project instructions](../templates/projects/EXEMPTION-CLAUDE.md). For general task
drafting, use prompts [15 and 16 in the prompt library](../prompts/PROMPT-LIBRARY.md).

## Official starting points, not a substitute for the underlying rule

Source links reviewed September 5, 2026 (UTC):

- [Florida Property Tax Oversight](https://floridarevenue.com/property/Pages/home.aspx) links to
  statutes, rules, forms, and county officials. Florida identifies local property appraisers and
  tax collectors as resources for locally administered property-tax questions.
- [Texas Property Tax System Basics](https://comptroller.texas.gov/taxes/property-tax/basics.php)
  explains the system and links to the Tax Code, administrative rules, and research resources.

For other states, start with the official legislature and property-tax agency, then identify the
correct assessor/appraiser, collector, review board, or local legislative authority. Verify source
ownership through official links; a domain suffix alone does not establish legal authority.
An agency overview is a discovery aid. Cite the applicable provision for a substantive answer.

Before work use, run the research cases in the
[manual acceptance table](../docs/TOOLKIT-VALIDATION.md). Actual Claude Code behavior and managed
Windows access remain unverified until those trials are performed in the target environment.
