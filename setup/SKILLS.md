# Install, verify, update, and remove skills

Use the [catalog](../SKILLS.md) to choose a task. A skill is a folder containing `SKILL.md`, sometimes
with scripts, data, or references. Putting this repository somewhere on the PC does not install its
`skills/` distribution folder. Claude Code has specific discovery locations.

## Local skills bundled here

These six original skills are explicitly invoked and require no installer. Their instructions
use the tools already available to Claude; file parsing, browsing, and Office execution still
depend on the approved environment. No local skill grants new access or automatically installs tools.

| Scope | Destination | Choose it when |
| --- | --- | --- |
| Personal | `%USERPROFILE%\.claude\skills\<name>\SKILL.md` | The same skill is useful across work projects |
| Project | `<approved-project>\.claude\skills\<name>\SKILL.md` | Local configuration is limited to that project |

Use one scope for each skill. Same-name skills can shadow one another; current Claude documentation
describes enterprise precedence over personal and personal over project. Plugin commands use their
own namespace. Check the installed source rather than assuming a project copy wins.
[Official discovery and naming rules](https://code.claude.com/docs/en/skills).

### Copy and check

1. Read the selected folder's `SKILL.md` and supporting files in this downloaded snapshot.
2. In Explorer, open the permitted destination. Create `.claude` and `skills` folders if needed.
3. Check for an existing same-name folder. If present, compare it before replacing anything.
   Preserve a dated backup **outside** the active `skills` directory and confirm its files open.
4. Copy the complete selected folder. For example, copy `skills/prompt-coach` into the destination
   `skills` folder, giving `skills/prompt-coach/SKILL.md`. Avoid doubled nesting.
   In Windows File Explorer, select the source folder, press **Ctrl+C**, open the destination
   `skills` folder, then press **Ctrl+V**. If Windows asks to replace files unexpectedly, cancel
   and return to the comparison/backup step.
5. Compare the copied files with their source, including the research skill's `references` folder.
   In VS Code, select the source for comparison, then compare with the installed file.
6. Open a fresh Claude conversation in the intended scope. Type `/` and select the installed skill.
   Use the catalog example. Record the actual command and observed result in the setup receipt.

No administrator shell, execution-policy change, shell installer, or new account is needed for
these manual file copies, assuming the destination is permitted. All six use
`disable-model-invocation: true`; they do not run merely because a task sounds relevant.

### Update or undo

Record the source snapshot before installing. For an update, compare the new version, preserve
the old installed folder outside discovery, then replace only the selected folder and repeat its
example. Keep any approved local adaptations visible in that comparison.

To undo, remove only the folder you installed, or restore its verified predecessor. Start a new
conversation and confirm discovery. Restore the global `CLAUDE.md` separately if it also changed.
Do not delete the whole `.claude` directory; it may contain unrelated configuration and credentials.

## Upstream skills and plugins

Upstream skills are **not bundled here**. The
[official-source review](../guides/07-trusted-skills-and-installation.md) and
[community-source review](../guides/11-community-skills-worth-adding.md) document versions, licenses,
runtime needs, and package behavior. Read those before choosing a route.

For each upstream choice, review the exact source/revision, license, executable files, dependencies,
network behavior, and any hooks or connector configuration. Use the employer-approved installation
method. Preserve existing configuration. Do not run a whole collection's installer to get one skill.

**Anthropic Office: optional, after the first lessons.** The marketplace route installs the Office
bundle, including Excel, PDF, Word, and PowerPoint. After reviewing the package and obtaining the
needed workplace approval, prefer the extension's plugin interface:

1. Type `/plugins` in Claude's message box if offered. Open **Marketplaces**, add
   `anthropics/skills`, then return to **Plugins**.
2. Find `document-skills` from that marketplace and inspect its contents. Choose **Install for you**
   for approved personal scope, or the specifically approved alternative scope.
3. Apply the requested restart and check the actual installed command. Run the small synthetic
   acceptance check below before using real workbooks.

If this interface is unavailable or restricted, leave the optional install pending and ask IT for
the supported route. The first text lessons still work.
[Official plugin interface](https://code.claude.com/docs/en/vs-code#manage-plugins).

**Command exception for a supported Claude session:** these equivalent commands are reference
material for an approved installation. They are not PowerShell commands. If a terminal session is
needed, follow [the terminal exception guide](../guides/00-use-vscode.md#6-use-the-terminal-only-for-a-named-exception)
and have the standalone CLI and gateway configuration verified first.

```text
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

The installed command may be namespaced, such as `/document-skills:xlsx`; use the actual `/` menu.
Check the [current manifest](https://github.com/anthropics/skills/blob/main/.claude-plugin/marketplace.json)
and [plugin documentation](https://code.claude.com/docs/en/discover-plugins) if the package changes.
The Office skills have their own restrictive terms and assume local document-processing tools.
An approved gateway does not itself establish license eligibility or install those tools.

**Data and Finance:** Guide 07 lists their marketplace route and broader package contents. These
may include connector configuration. Start with approved file exports; no new database connection
is required to draft a query or use the methodology. Select the actual installed skill command.

**Individual source folders:** where the license and package support it, copy the complete reviewed
folder using the local procedure above. Include required notices, scripts, and references, and
resolve paths intended for plugin execution before claiming the copy works. This route is useful
for reviewed community skills; it is not permission to redistribute restricted Office sources.

**UI/UX Pro Max and Impeccable:** these include supporting tooling. Guide 11 explains their actual
packaging. A single copied Markdown file is insufficient for either full workflow. Install neither
with a remote-script shortcut merely because a README suggests one.

### Verify the capability, not just the menu

| Capability | Small acceptance check |
| --- | --- |
| XLSX | Generate an invented workbook; open a copy in native Excel, check formulas/totals and save behavior |
| PDF | Extract two fields from a synthetic PDF and verify page citations against the rendered page |
| DOCX / PPTX | Produce a tiny invented memo/deck; open in Word/PowerPoint and inspect clipping and layout |
| Dashboard/design | Use invented data; check answer-key totals, filters, missing values, keyboard use, and print |
| Data/SQL | Start with a synthetic table or schema; check duplicates, join cardinality, precision, and source totals |

Do not use successful skill discovery as evidence that a Python library, Excel engine, browser,
or database connection is available. Record blocked checks as UNVERIFIED and use the supported path.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| No slash command | Correct scope; complete folder; exact `SKILL.md` filename; fresh conversation; managed restrictions |
| Wrong skill runs | Same-name personal/project/enterprise copies; installed source and plugin namespace |
| Research template missing | `references/research-memo.md` was copied with the skill |
| Library or command missing | Approved runtime inventory; request the specific dependency through IT, or use a supported task |
| No web access | Analyze supplied approved sources and label the research source-limited |
| Plugin command unavailable in the panel | Use the plugin UI above; otherwise leave the optional install pending and follow the terminal exception only with a verified setup |
| Gateway/model error | Keep existing credentials private; use the organization's support route |
| Workbook opens but results look stale | Check native Excel recalculation and feature preservation; parsing is not calculation |

Return to [setup](../START-HERE.md) or [the catalog](../SKILLS.md).
