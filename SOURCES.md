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

The learner path pairs real screenshots with selectable text and fenced prompt blocks.
The walkthrough was performed in a separate clone on a Mac Studio using VS Code's
Anthropic Claude Code extension and native Microsoft Excel, Word, PowerPoint, and Preview.
See [capture provenance](assets/walkthrough/README.md). No Windows screenshots are simulated.
The unchanged upstream reference images remain in assets/reference with their attribution.

The complete PDF is generated from README.md. Requests remain selectable text, with a
linked contents list and bookmarks. Images explain where to act; they never replace a
copyable prompt. The standalone GLOBAL-CLAUDE.md preference block matches the course.

## Checks and limits

Maintainers run:

~~~sh
node tests/validate-repo.mjs
python3 tests/state-workbook-spec.py
python3 tests/build-guide.py
python3 tests/check-guide.py
~~~

The checks verify local links, JSON manifests, six discoverable custom skills, automatic
invocation availability, and copyable prompts for all fifteen selected skills. Reviewed
walkthrough screenshots are allowed; long workbench commands are excluded from the course.
The PDF check verifies every text block and heading, source hash, bookmarks, and preferences.

The workbook test independently reads the shipped XLSX archives. It verifies text IDs,
source counts, amounts, reconciliation populations, matched net and gross differences,
and the bridge. The four-input meeting fixture is kept separate from the tiny exercises.
The checked meeting reconciliation was opened, recalculated, and saved in native Excel:
all twelve checks were OK. Its public copy removes personal author and local-path metadata while preserving
worksheet bytes and Excel's cached results.

### What the real Mac run established

- VS Code Git: Clone downloaded the public project into a separate demonstration folder.
- The official Anthropic extension was installed in a clean VS Code profile. The configured
  Claude connection was retained; a fresh account/sign-in flow was not tested.
- The property-tax marketplace already existed. Anthropic's skills marketplace was added.
  Both the workbench and document-skills plugins were installed locally to the project,
  followed by a real Reload Window.
- Plain-language requests in the extension produced the four source workbooks, the input
  Word brief and three-slide agenda, the reconciliation, and the meeting outputs.
- Excel recalculation and source totals were checked independently. Native Office review
  found a count formatted as currency and two presentation defects. The count format,
  overlapping slide text, and truncated chart axis were corrected and reviewed again.
- The final one-page Word briefing and all five PowerPoint slides were inspected in their
  native apps. The corrected briefing was exported through Word and opened in Preview.
- PDF extraction, official-source research, saving findings into a separate Research sheet,
  and creating a project review skill were run through the extension. These are actual
  saved outputs, not promises based solely on skill names.
- The PDF summary was opened and recalculated in Excel: all 24 comparisons were OK.
  The research workbook retained all twelve OK financial checks and whole-number counts.
- A new conversation selected the new project skill automatically from a request that
  did not name it. The first revision saved a backup and a 292-word checklist with a
  separate detailed check note.
- The optional Open in Terminal action launched Claude Code. A read-only request
  read MY-MEETING.md and correctly summarized the deliverables and checks. The session
  was exited and the graphical extension reopened. Personal terminal status details
  were excluded from published screenshots.
- The five optional helpers were fetched from the selected snapshots into the demo project's
  .claude/skills directory with supporting files. Nothing was installed globally. Source
  provenance and missing dependencies were reported. Installation is not a claim that every
  optional workflow or evaluation tool has been executed.

The dashboard's data and calculation logic were checked without a browser. Browser rendering,
filter interaction, empty state, print layout, and screenshots remain pending the local-preview
permission after the browser tool rejected a local file URL. This is an automation limitation,
not a reason for learners to change their security settings. Do not describe that stage as
completed until its real browser checks have passed.

### Platform and work limits

This revision was not tested in a beginner's managed Windows environment. Windows shortcuts
and file-opening differences are supplied, but company authentication, allowed tools, Office
versions, and plugin policy can differ. Macros, Power Query, PivotTables, unusual PDFs, and
employer data sources require their own native tests. A skill supplies a procedure, not an
Office license, desktop-control connection, or permission to access work systems.

The research is a worked source-review example. It is not a filing determination for any
property. The official [TCAD page](https://traviscad.org/renditions),
[Comptroller Form 50-144 (03-26)](https://comptroller.texas.gov/forms/50-144.pdf), and
[HB 9 enrolled text](https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00009F.htm)
were inspected; applicability and election timing remain review questions. No forms were
submitted, no exemption was applied to practice amounts, and no financial totals were changed
by research. Saved findings must be rechecked before real use.

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
