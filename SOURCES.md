# Sources and verification

[Course home](README.md). Setup references checked September 5, 2026.

| Topic | Official source |
| --- | --- |
| Windows installation | [Microsoft VS Code setup](https://code.visualstudio.com/docs/setup/windows) |
| Extension, sign-in, plugin panel, reload | [Anthropic VS Code guide](https://code.claude.com/docs/en/vs-code) |
| Skill names and discovery | [Anthropic skills guide](https://code.claude.com/docs/en/skills) |
| User and project instructions | [Anthropic CLAUDE.md guide](https://code.claude.com/docs/en/memory) |
| Office skill package and license | [Anthropic skills repository](https://github.com/anthropics/skills) |
| Exact Office package contents | [Official marketplace manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json) |
| Optional Windows shell requirements | [Claude Code setup](https://code.claude.com/docs/en/setup) |
| Optional Node.js LTS download | [Node.js downloads](https://nodejs.org/en/download) |
| Research practice starting point | [Texas Comptroller property-tax forms](https://comptroller.texas.gov/taxes/property-tax/forms/) |
| Local research practice source | [Travis Central Appraisal District renditions](https://traviscad.org/renditions) |

All numbered illustrations are original SVG teaching diagrams. They simplify controls and contain
invented examples. They are not Windows screenshots or evidence that a task ran in Claude Code.
The two real Microsoft screenshots are attributed in [assets/reference](assets/reference/ATTRIBUTION.md).

The practice workbook is synthetic, with two sheets and four detail rows per sheet. The workbook
check independently reads its XML, verifies text IDs, source totals, formulas and stored values,
unique matches, unmatched items, net/gross differences, and the full reconciliation bridge.
Stored values do not prove a native Excel recalculation.

Maintainers run `node tests/validate-repo.mjs` and `python3 tests/state-workbook-spec.py`.
The first checks local links, images, plugin discovery structure, and configuration parsing.
Neither check simulates a Windows installation, managed gateway, or Claude's response to a prompt.
The learner's in-app checks remain necessary. No state tax-law claim is supplied by this course.

The research lesson links to official starting points checked September 5, 2026. It asks the learner
to verify tax-year applicability; it does not supply a fixed deadline or assert a filing obligation.
The three additional skills need their own in-app practice checks; structural validation alone does
not establish research accuracy, formula calculation, or the quality of a generated summary.
