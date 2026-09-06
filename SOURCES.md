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

## Course-format research

Reviewed September 6, 2026. The design uses short lessons, copyable requests,
a continuing work example, and observable checks. It is an original accounting course;
no upstream course text, prompt library, or paid lesson was copied.

| Source inspected | Useful structural pattern | Adaptation here |
| --- | --- | --- |
| [Anthropic Claude Code 101](https://academy.claude.com/courses/claude-code-101) | Concepts, first prompt, daily workflow, then customization | Extension setup first; reusable skills after a checked task |
| [Claude How To](https://github.com/luongnv89/claude-howto) | An ordered path with copyable examples and self-assessment | A text block for each request and a concrete output check |
| [Claude Code Ultimate Guide learning path](https://github.com/FlorianBruniaux/claude-code-ultimate-guide/tree/main/guide/learning-path) | Fundamentals separated from optional depth; practice and validation | Terminal use is optional; the main path stays in the extension |
| [Delba Oliveira's Learn Claude Code](https://github.com/delbaoliveira/learn-claude-code) | One project evolves across conversational lessons | A bill review evolves into a meeting dashboard and briefing |

GitHub metadata showed approximately **41,400 stars** for Claude How To and **5,900**
for Claude Code Ultimate Guide when checked. This supports calling them established
community references, not claiming a measured best course or verified learning outcomes.
Delba's smaller repository was selected for its continuous-project format, not popularity.
We inspected public curricula and source material; we did not complete paid courses.

The [DeepLearning.AI and Anthropic course](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)
was also located, but direct retrieval was blocked. Its unavailable lesson content was not
used as implementation evidence or a claim of full course review.

Optional video: [Anthropic's Getting started with Claude.ai](https://www.youtube.com/watch?v=0vZ_UVLhSQQ)
introduces conversation on the website, not this extension.
[Krish Naik's VS Code introduction listing](https://www.classcentral.com/course/youtube-getting-started-with-claude-code-with-vs-code-482334)
describes a short terminal-in-VS-Code tutorial. Its listing was inspected, not its full video;
it is not the authoritative source for current extension buttons. Use the official
[VS Code guide](https://code.claude.com/docs/en/vs-code) and
[terminal quickstart](https://code.claude.com/docs/en/quickstart) for current behavior.
No claim is made about video popularity, course pricing, or guaranteed access.

## Text, screenshots, and PDF

The learner path uses selectable text and fenced prompt blocks. It does not require
reading prompts from pictures. Earlier illustrations remain in Git history.
The unchanged Anthropic reference screenshots remain under assets/reference for attribution
and optional reference, not as course instructions. See [attribution](assets/reference/ATTRIBUTION.md).

The full PDF is generated from README.md. Its prompts are text, with a linked contents list
and document bookmarks. The build script wraps long lines rather than clipping them.
The standalone GLOBAL-CLAUDE.md block must match the preference prompt in the course.

## Checks and limits

Maintainers run:

~~~sh
node tests/validate-repo.mjs
python3 tests/state-workbook-spec.py
python3 tests/check-guide.py
~~~

The first checks local links, configuration, discoverable skill structure, automatic-invocation
availability, and copyable learner prompts. It rejects long workbench commands and prompt images
in the learner path. It also checks that all installed skill names are covered by the course.

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
producing every requested output. Structural checks do not establish that. The in-app success
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

To refresh the PDF after editing the course, run `python3 tests/build-guide.py`, then
`python3 tests/check-guide.py`. Maintainers need ReportLab, markdown-it-py, and pypdf;
the learner needs none of those tools. CI rebuilds the PDF and checks that the committed
copy matches, so the printable course cannot silently lag behind the Markdown.
