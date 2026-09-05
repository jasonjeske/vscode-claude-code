# Guide 07: The recommended skill stack

Research checked **September 5, 2026 (UTC)**. This is a fit-based recommendation for enterprise
property-tax work, not a benchmark or a certification. No skill has been tested here against a
production workbook, a managed Windows installation, or an organization's gateway.

**Community skills are part of the recommendation too.** See
[Guide 11](11-community-skills-worth-adding.md) for UI/UX Pro Max, Impeccable, Pandas Pro, SQL Pro,
and focused K-Dense skills, with pinned sources, practical prompts, and installation notes.

## Start with these choices

| Need | First choice | Why it fits | Important limitation |
| --- | --- | --- | --- |
| Excel files | Anthropic **xlsx** | Official spreadsheet creation and editing skill | Requires a compatible local runtime; complex Excel features need native Excel validation |
| Interactive dashboards | Anthropic Data **build-dashboard**, with **data-visualization** and **validate-data** | Covers presentation and analytical checks | Review its external chart dependencies and embedded data before sharing |
| Visual polish | Anthropic **frontend-design** | Useful for typography, hierarchy, layout, and polished interfaces | Visual quality does not establish accounting accuracy |
| Community dashboard design | **UI/UX Pro Max**, then **Impeccable** for refinement | Strong design direction and focused visual improvements | Review the complete package; Impeccable includes executable tooling |
| Community data preparation | **Pandas Pro**, with **Polars** when scale justifies it | Reusable joins, transformations, and data diagnostics | Tax-specific null, precision, and matching rules must override generic examples |
| Reconciliation methodology | Anthropic Finance **reconciliation** | Relevant to ledger/detail comparisons and reconciling items | Generic accounting guidance, not jurisdiction-specific property-tax rules |
| Immediate learning | This repository's **prompt-coach** and **excel-workbook-review** | Small, explicit workflows that do not need Office libraries to begin | Review skill prepares findings; it does not control the Excel application |

Claude Code is **not a blank system with no skills**. Current versions have bundled skills and
tools. Installed and managed extensions vary. Those are not the same as having an Office document
toolkit ready on this particular machine. Check the installed version and the `/` menu rather than
assuming a ChatGPT, Claude web, or Cowork feature is present in VS Code.
[Claude Code skills](https://code.claude.com/docs/en/skills).

## The shortlist, in installation order

These are upstream recommendations, not copies bundled with this repository.

| Stage | Skill or package | Use it for | Source |
| --- | --- | --- | --- |
| 1 | `xlsx` | Workbooks, formulas, tables, formatting, exports | [Anthropic xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx) |
| 2 | `pdf` | Notices, source-page extraction, evidence packets | [Anthropic pdf](https://github.com/anthropics/skills/tree/main/skills/pdf) |
| 2 | Finance `reconciliation` | Balance comparisons and exception aging | [Actual skill](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance/skills/reconciliation) |
| 2 | Financial Services `audit-xls` | Focused formula and model review | [Actual audit skill](https://github.com/anthropics/financial-services/tree/main/plugins/vertical-plugins/financial-analysis/skills/audit-xls) |
| 2 | Data `explore-data`, `validate-data` | Input profiling and analysis checks | [Current Data skill tree](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills) |
| 3 | Data `build-dashboard`, `data-visualization` | Filterable reports and chart selection | [Actual dashboard skill](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/build-dashboard) |
| 3 | `frontend-design` | Improve the visual design after metrics are defined | [Anthropic frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| 3 | Finance `variance-analysis` | Explain period changes with supporting evidence | [Finance package](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance) |
| 4 | `docx`, `pptx` | Reviewer memos and management presentations | [Word](https://github.com/anthropics/skills/tree/main/skills/docx), [PowerPoint](https://github.com/anthropics/skills/tree/main/skills/pptx) |
| 4 | Data `write-query`, `sql-queries` | Draft reviewed SQL for approved exports | [Data package](https://github.com/anthropics/knowledge-work-plugins/tree/main/data) |
| Later | Finance `close-management`, `audit-support` | Close checklists and evidence organization | [Finance package](https://github.com/anthropics/knowledge-work-plugins/tree/main/finance) |
| Later | `doc-coauthoring`, `skill-creator` | Improve repeatable documentation and tested local skills | [Anthropic skill collection](https://github.com/anthropics/skills/tree/main/skills) |

The upstream `data-visualization`, `sql-queries`, `close-management`, and `audit-support` entries
are supporting skills marked `user-invocable: false`; they are not direct slash-menu commands.
Ask Claude to use their guidance in a normal request when the reviewed package is installed.

Choose the next skill from the next real task. Installing every item on day one creates more
configuration to understand without proving any benefit. The Finance and Data repositories say
they also support Claude Code, although their primary target is Cowork.
[Finance README](https://github.com/anthropics/knowledge-work-plugins/blob/main/finance/README.md),
[Data README](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/README.md).

## Findings that change the recommendation

1. **Office licensing needs a specific check.** The `xlsx`, `docx`, `pptx`, and `pdf` skills are
   source-available with per-skill terms, not ordinary MIT examples. The reviewed XLSX license
   restricts copying, modification, and redistribution. Ask the organization's reviewer to resolve
   permitted use through its Anthropic agreement and gateway before installation. This public
   repository links to them and does not redistribute them.
   [XLSX terms](https://github.com/anthropics/skills/blob/main/skills/xlsx/LICENSE.txt).
2. **The Office runtime is not included with VS Code.** The reviewed XLSX skill assumes Python
   libraries and a LibreOffice-based recalculation environment. A managed PC may have neither.
   Its assumptions must not become an instruction to install unapproved software. Native Excel
   remains the validation target for advanced Excel work.
   [XLSX implementation](https://github.com/anthropics/skills/blob/main/skills/xlsx/SKILL.md).
3. **A dashboard described as self-contained may still contact a CDN.** The inspected Data
   dashboard template includes external Chart.js scripts. For an offline requirement, use reviewed
   local assets or native SVG, then test with network disabled. Embedded data travels with the HTML.
   [Dashboard implementation](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/build-dashboard/SKILL.md).
4. **README names can lag the files.** The Data README listed `interactive-dashboard-builder` and
   `data-validation`, while the inspected skill directories were `build-dashboard` and
   `validate-data`. Select from the actual installed menu and reviewed commit.
   [Data skill tree](https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills).
5. **Official does not mean appropriate without review.** The Data package includes MCP
   configuration. Review the entire package, not just one prompt. A local-export workflow does not
   need an ERP connector, personal Microsoft login, or new database access.
   [Data connector configuration](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/.mcp.json).

The openpyxl and XlsxWriter projects are trustworthy implementation libraries, **not Claude Code
skills**. Power Query and Power BI are Microsoft products, also not skill files. A community Excel
MCP server adds a connection or execution surface; it is not a substitute for reviewing workbook
fidelity. No third-party aggregator or star count establishes enterprise suitability.

## Other official options considered

Anthropic's separate **Financial Services** repository includes `audit-xls`, `clean-data-xls`,
`xlsx-author`, and a GL Reconciler agent. The relevant narrow addition is `audit-xls`: use its
formula-review scope, with property-tax controls supplied by the project. Its investment-model
checks do not establish property-tax correctness.
[Audit skill](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/skills/audit-xls/SKILL.md).

`clean-data-xls` is useful after types and keys are agreed; a numeric-looking parcel key must not
be converted to a number. `xlsx-author` is a small file-generation fallback, not a sophisticated
Excel engine or a replacement for the Office XLSX workflow. These are candidates for a reviewed
selection under that repository's Apache-2.0 license, retaining applicable notices and dependencies.
[Cleaning skill](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/skills/clean-data-xls/SKILL.md),
[authoring skill](https://github.com/anthropics/financial-services/blob/main/plugins/vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md),
[license](https://github.com/anthropics/financial-services/blob/main/LICENSE).

Do not install the entire Financial Services stack just for these instructions: it includes
specialized investment workflows, connectors, and agent configurations. Its GL Reconciler is a
later organizational evaluation, not a beginner default. Its Microsoft 365 add-in provisioning is
an IT-admin deployment and is separate from the already working VS Code extension.
[Financial Services overview](https://github.com/anthropics/financial-services/blob/main/README.md).

Microsoft also documents **Copilot skills for Excel (preview)**. Those target the Copilot/Office
runtime and can use Office.js. They are not automatically runnable inside Claude Code's VS Code
extension, despite sharing a `SKILL.md` convention. Evaluate that separately only if the organization
already uses the required Microsoft surface.
[Microsoft runtime documentation](https://learn.microsoft.com/en-us/office/dev/add-ins/excel/excel-skills).

## Install our small local skills first

Use [the short setup](../START-HERE.md) for an already working extension. The
[skill catalog](../SKILLS.md) gives all six local skills with examples, and the
[installation guide](../setup/SKILLS.md) covers complete-folder copying, scope, backups,
discovery, updates, removal, and troubleshooting. No marketplace or runtime installer is required
for these instruction-only folders. Copy the research skill's `references/` folder too.

The optional full onboarding protocol offers two optional skills in Stage 5. It is not required
for the short setup. Keep the existing gateway configuration and install only the next useful skill.

## Install upstream skills only through the reviewed route

The following are **reference commands**, not an installer run by this repository. They belong in
an approved Claude Code terminal session, not directly in PowerShell. VS Code also has a plugin
management interface; availability varies by installed version and managed policy.
[VS Code plugins](https://code.claude.com/docs/en/vs-code),
[plugin installation](https://code.claude.com/docs/en/discover-plugins).

After source, license, dependencies, and package scope are approved:

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

That installs the Office bundle, including all four formats. For Data or Finance, review each
package and its integrations separately before choosing either installation:

```text
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install data@knowledge-work-plugins
/plugin install finance@knowledge-work-plugins
```

Do not execute the entire block as a beginner checklist. Use the interactive scope selection and
record exactly what was installed. Plugin skills use namespaced commands, typically
`/document-skills:xlsx`, `/data:build-dashboard`, or `/finance:reconciliation`; confirm in `/`.
The `example-skills` bundle contains more than design, so avoid installing it solely to obtain
`frontend-design`. A reviewer may select its complete Apache-licensed folder, retaining its license
and referenced resources, or approve a focused official package.
[Document package manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json),
[Knowledge Work manifest](https://github.com/anthropics/knowledge-work-plugins/blob/main/.claude-plugin/marketplace.json),
[design license](https://github.com/anthropics/skills/blob/main/skills/frontend-design/LICENSE.txt).

Record the source URL, resolved commit/version, license, installed folder or package, dependencies,
synthetic test result, review date, and rollback. These upstream links track `main` and may change;
they are research pointers, not pinned deployment artifacts.

## Gateway and Windows acceptance checks

- Preserve the working provider, base URL, API key mechanism, and model aliases. Skill discovery is
  local configuration; a skill does not authorize changing the gateway or enable a blocked tool.
- Verify that the gateway supports the requests used by the installed Claude Code version. If a
  tool or web capability fails, report the redacted error to IT. Do not fall back to a personal key.
- Test Python/Office libraries only if installed and approved. Discover versions before proposing
  any installation. Installing an instruction file does not install its dependencies.
- Try a tiny synthetic file, then an approved representative copy with the actual Excel features.
  Check formulas, charts, PivotTables, refresh, and output reopening before production use.
- Use the gateway's authoritative budget reporting. A missing usage field means unavailable,
  not unlimited or free.

[Gateway documentation](https://code.claude.com/docs/en/llm-gateway),
[Windows verification ledger](../docs/WINDOWS-VERIFICATION.md).
