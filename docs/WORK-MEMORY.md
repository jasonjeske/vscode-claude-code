# Bounded local work memory

Claude Code already provides native auto memory. This repository adds an optional, manual
cross-project Markdown wiki for small user-approved summaries that matter across projects and days.
Neither layer is a security boundary or a substitute for authoritative work records.

## Two different memory layers

### Native Claude Code auto memory

Native auto memory is normally scoped to one project under Claude's user data. Use `/memory` to
inspect or toggle it. Claude loads the first 200 lines or 25 KB of `MEMORY.md` at startup and reads
topic files on demand. These limits and behavior may change; the current Claude Code documentation
is authoritative.

Native memory is machine-local storage, but its content is processed by the configured Claude
service when recalled. Organization policy and managed settings control whether it may be used.
This starter never changes `autoMemoryDirectory` and never redirects project memory into a shared
folder.

### Manual cross-project work wiki

The optional wiki lives only at `%USERPROFILE%\.claude\work-memory`:

```text
work-memory/
├── NOW.md                         short current handoff
├── INDEX.md                       one-line topic catalog
├── topics/<safe-slug>.md          durable topic notes
└── archive/<safe-slug>-YYYYMMDD.md preserved snapshots
```

Recall is manual by default. No file is imported automatically. The global instructions ask once
at the start of related work whether to read `NOW.md` and `INDEX.md`, then ask before one topic.
This keeps context and usage bounded and avoids mixing unrelated work.

## Fixed topic-note schema

Every topic note uses these metadata fields and sections:

```text
Title: [generic title]
Type: project | topic | procedure | preference
Status: active | proposed | superseded | contradicted | archived
Updated: YYYY-MM-DD
Source: [neutral provenance]
Confidence: high | medium | low

Purpose
Current state
Decisions
Recurring rules
Open items
Next action
Provenance
Supersedes / contradicts
```

Store outcomes and provenance, never hidden chain-of-thought. A note is a reminder, not current tax,
legal, accounting, or company authority.

## Hard bounds

| Item | Limit |
| --- | ---: |
| `NOW.md` | 100 lines and 4 KB |
| `INDEX.md` | 60 topic entries and 8 KB |
| One topic file | 300 lines and 16 KB |
| Entire work-memory folder | warning at 5 MB; hard stop at 10 MB |

No attachments, binaries, source documents, exports, generated evidence, or databases. At a file
cap, propose compaction or an archived snapshot. At 5 MB, warn before any write. At 10 MB, stop all
writes except an explicitly approved archive purge that reduces usage. Never auto-delete.

## Lifecycle verbs

The optional `/work-memory` skill supports:

- `init` - preview and create the bounded folder from blank templates;
- `status` - report neutral counts, sizes, limits, and conflicts;
- `checkpoint` - propose a redacted update to `NOW.md`;
- `remember <topic>` - preview a durable topic update and index entry;
- `recall <topic>` - read one approved topic and report freshness and conflicts;
- `compact <topic>` - preview a shorter note and archive the prior version;
- `forget <topic|NOW>` - archive first, then remove only after separate approval;
- `restore <archive>` - preview restoring an archived snapshot; and
- `purge-archive <archive>` - permanently remove one named snapshot after two confirmations.

`status` and `recall` grant read access only to the named memory scope. Every write, move, archive,
or delete requires a preview and separate explicit approval.

## Contradictions and provenance

Append dated facts rather than silently rewriting history. If a newer approved entry changes an
older one, mark the older entry `SUPERSEDED YYYY-MM-DD` or `CONTRADICTED YYYY-MM-DD`, preserve its
source, and link the newer statement. Do not resolve a conflict without evidence and human review.
Archived snapshots remain read-only until an approved restore.

## Privacy rules

Memory is plaintext. The user profile may be managed, backed up, roamed, indexed, or synchronized
by employer tooling. Confirm that this storage location is approved before initialization.

Use generic, redacted summaries only. Never store:

- credentials, tokens, secrets, or access instructions;
- names, taxpayer or property identifiers, addresses, account identifiers, or row-level data;
- actual financial values, totals, assessments, payments, or evidence;
- internal URLs, exact paths, system details, or source documents; or
- hidden chain-of-thought or copied conversation transcripts.

When memory is recalled, its content is processed by the approved Claude service. “Local” does not
mean local inference. Do not use this feature when policy is no or unknown.

## Backup, forget, and restore

Before overwriting a note, create a dated Markdown snapshot in `archive` and verify it is readable.
`forget` archives first. `purge-archive` is the only skill verb that permanently removes an archive
snapshot. It requires two confirmations naming the neutral snapshot and warning that employer
backups may retain copies. `restore` previews the destination, backs up any current note, and
requires approval before writing.

## Token-aware recall

Read `NOW.md` and `INDEX.md` only for related work, then load at most one relevant topic. Do not
scan the wiki, all native memory, or every project. Use `/context` to inspect context cost.
Compact stale notes with approval instead of loading a large history.

## Official sources

- [Claude Code memory](https://code.claude.com/docs/en/memory)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Claude Code commands](https://code.claude.com/docs/en/commands)
- [Claude Code data usage](https://code.claude.com/docs/en/data-usage)
