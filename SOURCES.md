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


## Why these five extras

The starter list adds five specific capabilities to the existing Office package. It does not
install a whole community collection. The exact source commits and complete-folder installation
instructions are in [STARTER-SKILLS.md](practice/STARTER-SKILLS.md).

| Selected skill | Why it fits a beginner |
| --- | --- |
| [doc-coauthoring](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/doc-coauthoring) | Guided context gathering, outlining, and improving a document for its reader |
| [skill-creator](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/skill-creator) | An official method for creating and testing a reusable procedure; start with one small sample |
| [academy-guide](https://github.com/anthropics/skills/tree/41bbe19d1a1a7eaab5e7bb9050a417e5c6cffc8f/skills/academy-guide) | Matches learning questions to the current official Claude Academy catalog |
| [file-organizer](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2/file-organizer) | A practical folder-organization workflow; begin with a proposal for practice copies |
| [content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2/content-research-writer) | Combines an outline, research, citations, and draft improvements |

As checked September 6, 2026, GitHub reported about **175,000 stars** for
[Anthropic's collection](https://github.com/anthropics/skills) and **75,000** for
[Composio's collection](https://github.com/ComposioHQ/awesome-claude-skills).
Those are collection-level popularity signals, not proof of adoption or quality for each skill.
Selection also considered the actual instructions, supporting files, task fit, and beginner burden.

The community selections need judgment. The file organizer contains operating-system-specific
shell examples and a duplicate-check example that does not correctly group identical content
independently of filenames. The installation checklist requires appropriate tools and independent
content checks; the first exercise makes no file changes. The research writer contains illustrative
statistics and citations. They must never be reused as verified findings. Neither helper replaces
the tax procedure's jurisdiction, year, source, and applicability checks.

The selected community folders have no license file, and no repository-level license file was
present at the reviewed commit. This guide links to their public sources; it does not redistribute
those files or claim a reuse license. Keep any supplied upstream terms with locally fetched skills.
Anthropic's document skills have their own terms and are installed from the official marketplace.

We did not add a separate prompt optimizer or a large planning framework. Plain requests and a
saved project note cover the beginner exercises without formal prompt specifications, automatic
hooks, or repeated planning-file injection. The skill creator has more advanced evaluation tools;
the beginner preference is one small test, with an explanation before larger or parallel runs.

For browsing, see [Claude in Chrome for Claude Code](https://code.claude.com/docs/en/chrome).
For learning, see [Claude Academy's Code section](https://academy.claude.com/code) and Anthropic's
[Getting started with Claude.ai video](https://www.youtube.com/watch?v=0vZ_UVLhSQQ).
The latter demonstrates the website; it is not a VS Code extension installation video.

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

For the five extra recommendations, we fetched all 23 files in the selected upstream directories
to a temporary review folder and independently parsed all five YAML headers. Each has a matching
name, a description, and automatic invocation enabled by default. No personal skills were installed.
Claude Code 2.1.263's native validator returned an empty contents list for the staged personal-skill
layout, so its success status is **not** counted as evidence that those five files were validated.
The source review and independent format checks do not establish runtime behavior.

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
