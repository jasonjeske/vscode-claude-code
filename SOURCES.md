# Sources and verification

[Home](README.md). Product references checked September 6, 2026.

| What was checked | Primary source |
| --- | --- |
| Automatic skill selection, descriptions, project/user skill locations | [Anthropic skills documentation](https://code.claude.com/docs/en/skills) |
| Extension installation, graphical prompt box, clickable command menu, plugins, restart, history | [Anthropic VS Code documentation](https://code.claude.com/docs/en/vs-code) |
| Persistent global instructions | [Claude Code memory](https://code.claude.com/docs/en/memory) |
| VS Code downloads | [Microsoft download page](https://code.visualstudio.com/download) |
| Windows installation | [Microsoft setup](https://code.visualstudio.com/docs/setup/windows) |
| Anthropic's document package | [Official skills repository](https://github.com/anthropics/skills) and [marketplace manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json) |
| Texas research starting point | [Texas Comptroller forms](https://comptroller.texas.gov/taxes/property-tax/forms/) |
| Local research starting point | [Travis CAD renditions](https://traviscad.org/renditions) |

Skills can be selected automatically when the descriptions and request fit. This kit does not
disable model invocation. Explicit namespaced commands are optional and are not taught as the
learner's workflow. A skill supplies instructions; available tools and company permissions
determine what Claude can execute.

## Pictures

The **claude-** reference images are real screenshots from Anthropic's documentation, copied
unchanged. They illustrate the extension's actual interface with Anthropic's programming examples.
They are not screenshots of this course being executed. See [attribution](assets/reference/ATTRIBUTION.md).

The SVG images are original, simplified interface illustrations with property-tax examples.
They are visibly labeled **ILLUSTRATED EXAMPLE**. Replies, filenames, and dashboard arrangements
are teaching examples, not fabricated execution evidence. UI layout and button labels may differ
by version, platform, and managed configuration.

## Checks and limits

Maintainers run:

~~~sh
node tests/validate-repo.mjs
python3 tests/state-workbook-spec.py
~~~

The first checks local links, configuration, discoverable skill structure, automatic-invocation
availability, and accessible SVG markup. It rejects long workbench commands in the learner path.

The workbook check independently reads the shipped XLSX files. It checks text identifiers,
source counts and totals, formulas and stored results, reconciliation differences, and the four-row
consolidation fixture. The two new bill workbooks were authored and rendered with Artifact Tool.
Its preview renderer drops leading zeros visually; the exported XML stores all four IDs correctly
as text, which the independent check verifies. Native Excel display and recalculation remain
a separate check.

This revision was not tested end to end in a beginner's managed Windows environment.
We have not verified a live Claude session completing these prompts, selecting every skill, or
producing the illustrated replies. Structural checks do not establish that. The in-app success
checks in each lesson are therefore part of the walkthrough, and should be tried on the learner's
approved connection before introducing real work data.

The guide supplies no state tax-law conclusion or deadline. Research steps require current,
applicable official sources and human review. No source finding is treated as filing approval.

## Maintainer notes

The kit contains six procedures: workbook review, consolidation, dashboards, tax research,
formula help, and workpaper summaries. Claude chooses relevant ones; the learner describes work.
Custom procedures belong in a separate project or user skill location so plugin updates do not
overwrite personal adaptations. Claude should save and test them for the learner.

Earlier versions remain in Git history. CHANGELOG.md is historical and is not edited manually.
