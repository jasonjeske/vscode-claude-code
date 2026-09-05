# Example onboarding transcript

> **This transcript is synthetic and illustrative.** It was written by hand to show the shape of the
> onboarding, not captured from a real session. No real person, employer, account, file path, or
> record appears in it. Every value is an invented placeholder. A real run will differ in wording,
> and the answers below are examples of the *kind* of answer to give, never a script to copy.

Read this if you are about to run `setup/FULL-ONBOARDING.md` and want to see what you are agreeing to first.
The thing to notice is how often the run stops and asks. That is the design, not friction.
Abbreviated where a stage repeats the same pattern; ellipses mark where questions continue.

---

## Stage 0: approval and preflight

**Claude:**

```text
[SETUP 0/8 - APPROVAL AND PREFLIGHT]
```

Six limits first: I cannot install or repair the Claude surface running this interview; a missing
component can be offered from an official source only after policy and your approval; managed policy
may block changes and there is no bypass; more instruction files do not create an enforcement
boundary; no task-aware model router is configured, so model choice stays yours; and this
conversation is processed by the approved Claude service, so local files do not mean local
inference.

> Have you confirmed that your employer approves this software, the exact Claude provider and
> enterprise account or tenant, the intended data classes, and the applicable retention and
> residency terms?

**User:** Yes, all four confirmed with our administrator.

**Claude:** `[SETUP 0/8 - APPROVAL AND PREFLIGHT]` May I run read-only checks? I will not sign in,
change anything, or search the whole computer.

**User:** Yes.

**Claude:** `[SETUP 0/8 - APPROVAL AND PREFLIGHT]`

```text
Operating system is Windows, appears managed           FOUND
VS Code available                                      FOUND
Claude Code CLI available                              MISSING
Extension anthropic.claude-code                        FOUND (managed catalog)
Starter checkout contains likely work artifacts        NOT FOUND
User instructions file exists                          FOUND (not read)
Discoverable settings targets                          FOUND (Default profile, Profile 2)
```

Before the interview, please run `/status` yourself, then tell me whether it shows the approved
provider and your workplace account or tenant. Do not paste any account identifier.

**User:** Ran it. Yes, it does.

**Claude:** `[SETUP 0/8 - APPROVAL AND PREFLIGHT]` The CLI is missing but the extension is present,
so onboarding can run. Would you like instructions for the CLI, an installation offer, or neither
for now?

**User:** Neither for now.

**Claude:** `[SETUP 0/8 - APPROVAL AND PREFLIGHT]` Recorded as `SKIPPED - APPROVAL REQUIRED`.

---

## Stage 1: policy boundary

**Claude:**

```text
[SETUP 1/8 - POLICY]
```

Seven questions, one at a time, categories only.

> May the verified workplace Claude account process the intended work-data classes?

**User:** Yes, for corporate tax support and reconciliation categories.

... questions 2 through 7 answered yes ...

---

## Stage 2: work interview

**Claude:**

```text
[SETUP 2/8 - WORK INTERVIEW]
```

A good request states outcome, context, sources, allowed actions, controls, deliverables, and stop
conditions. Nine questions, one at a time, categories only.

> Which generic categories apply, such as corporate tax support, property-tax accounting,
> reconciliation, document review, or workflow design?

**User:** Property-tax accounting and reconciliation, mostly.

**Claude:** `[SETUP 2/8 - WORK INTERVIEW]`

> What generic project or workflow categories recur?

**User:** Annual filings across a few states, and monthly tie-outs.

**Claude:** `[SETUP 2/8 - WORK INTERVIEW]` Recorded. I will call those states STATE-1 and STATE-2
rather than naming them.

... questions 3 through 10 continue in the same form ...

**Claude:** `[SETUP 2/8 - WORK INTERVIEW]` My redacted summary of your ten answers:

```text
Domain:        property-tax accounting, reconciliation
Recurring:     annual filings across STATE-1 and STATE-2, monthly tie-outs
30-day goal:   fewer manual tie-out passes for ENTITY-A in PERIOD-1
File types:    XLSX, CSV, PDF
Controls:      control totals, tie-outs, exception lists, review evidence
Authoritative: SOURCE-LEDGER over SOURCE-SYSTEM
Approval:      changes to filed values, anything leaving the team
Always stop:   unexplained variance, missing support, conflicting totals
```

No identifiers, values, or totals were recorded. Is that summary correct?

**User:** Yes.

---

## Stage 3: integrated instruction candidate

**Claude:**

```text
[SETUP 3/8 - INSTRUCTIONS DRAFT]
```

I read `templates/GLOBAL-CLAUDE.md` as the expected base. Your User instructions file already
exists. It may contain sensitive data, and it may contain instructions embedded by someone else.

May I process only that one file through the already verified Claude service? If you decline, I will
draft from the base and your approved generic answers instead.

**User:** Yes, you may read it.

**Claude:** `[SETUP 3/8 - INSTRUCTIONS DRAFT]` Read. Three notes. I preserved two standing rules from
your file that do not conflict with the base. I found one line that reads as an instruction to me,
which I am treating as data and have not acted on. I also found what reads as a credential-shaped
string; I have not carried it into the candidate and will not repeat it here or anywhere else in this
session. Please rotate it through your organization's approved remediation process before treating
this file as trusted again.

```text
[candidate shown in full, generic content only]

Preserved from your file:   2 standing rules (evidence rule, approval rule)
Preserved from the base:    teaching, confidentiality, reconciliation, approval, continuity, token rules
Added from the interview:   ENTITY-A and PERIOD-1 naming, SOURCE-LEDGER precedence, stop conditions
Not carried over:           1 embedded instruction line (treated as data), 1 credential-shaped
                             string (flagged for remediation, not reproduced anywhere)
```

This guides my behavior. It does not enforce policy, and it is not a security control. The
credential-shaped string itself appears nowhere above, in this response, or in the candidate; it
stays only in your original file until you remediate it.

> Approve a backup and one reviewed write of this candidate to User instructions?

**User:** Approved.

**Claude:** `[SETUP 3/8 - INSTRUCTIONS DRAFT]`

```text
1. Backup created beside the existing file, timestamped, and read back successfully.
2. Candidate written once.
3. Readback complete. The written file matches the reviewed candidate.
```

I will not make a second revision during onboarding without a new explicit request.

---

## Stage 4: VS Code candidate

**Claude:**

```text
[SETUP 4/8 - VS CODE DRAFT]
```

I read `config/vscode-settings.json`. Two settings targets are discoverable: `1. Default profile`
and `2. Profile 2`. Which should I merge into? Answer with the number.

**User:** 1.

**Claude:** `[SETUP 4/8 - VS CODE DRAFT]` Reading only that file. Calculating a recursive merge.

```text
editor.fontSize            existing 14        proposed 15        keeping existing
files.autoSave             existing "off"     proposed "off"     no change
[markdown].editor.wordWrap existing "on"      proposed "on"      no change
```

One behavioral conflict needs your decision.

> Your existing terminal font size is 12 and the candidate proposes 14. Keep 12?

**User:** Keep 12.

**Claude:** `[SETUP 4/8 - VS CODE DRAFT]` Keeping 12. The candidate adds Workspace Trust settings
absent from your file: `security.workspace.trust.enabled` as true, `startupPrompt` as always, and
`untrustedFiles` as prompt. These strengthen prompting rather than weaken it. Your theme and
telemetry are unchanged.

> Approve a backup and one reviewed write of this VS Code candidate to the selected profile?

**User:** Approved.

**Claude:** `[SETUP 4/8 - VS CODE DRAFT]`

```text
1. Backup created beside the existing settings file and verified.
2. Candidate written.
3. Written JSON parsed. All approved leaf values verified. Unrelated keys preserved.
```

Profile 2 was not touched. These settings are preferences, not DLP or policy enforcement.

---

## Stage 5: two optional public skills

**Claude:**

```text
[SETUP 5/8 - SKILLS]
```

Three skills, each handled separately. A skill is instruction text, not enforcement, and runs only
when you invoke it by name.

First: `structured-work-request`, which turns a vague request into a controlled one. Review it first?

**User:** Yes.

**Claude:** `[SETUP 5/8 - SKILLS]`

```text
Frontmatter delimiters      OK
name                        structured-work-request (matches expected)
description                 present, non-empty
disable-model-invocation    true
```

It interviews you one question at a time and produces a request stating outcome, inputs, rules,
proof, stop conditions, and approval points.

> Install this exact reviewed skill?

**User:** Yes.

**Claude:** `[SETUP 5/8 - SKILLS]` No same-name destination existed, so nothing to back up. Copied.
Every destination file matches the source exactly.

... `reconciliation-control-review` follows the same eight-step pattern, with separate review and
approval. No other persistence or storage system is initialized.

---

## Stage 6: model and usage lesson

**Claude:**

```text
[SETUP 6/8 - MODEL AND USAGE]
```

Summarizing `docs/MODELS-AND-USAGE.md`. Model and effort are not data-classification or safety
controls. Never reduce a control to save usage. Keep the approved default for the first lesson.
Use the extension controls where offered; commands such as `/status`, `/permissions`, `/model`,
`/effort`, `/context`, and `/memory` are optional reference equivalents. Check the organization's
usage website for the allocation; do not open a terminal to complete a command list.

**User:** I checked the organization's usage website. I understand the unit and period shown.

**Claude:** `[SETUP 6/8 - MODEL AND USAGE]` Useful context, not a budget I can enforce. Effort is
soft guidance rather than a hard token cap, and its availability depends on the model. We can
review the supported choices later when a task justifies a change.

`/memory`, where available, can inspect standard instructions. This setup preserves managed
settings and configures no automatic memory or storage redirection.

Subagents and long autonomous workflows are excluded from this starter because they multiply context
and usage. While learning, check the organization's usage website and decline offers to spawn subagents, keep going
autonomously, or build a complete workflow in one pass. I will not change your model, effort, or
permissions without a separate explicit request.

---

## Stage 7: starter lesson and synthetic first task

**Claude:**

```text
[SETUP 7/8 - PRACTICE]
```

Working through `guides/01-claude-code-fundamentals.md`, one topic at a time.

First topic: the prompt formula. A strong request names the outcome, the inputs, the rules, the
proof, and the stop condition. Which of those do your current requests usually leave out?

**User:** The proof, probably. I ask for an answer and not for how it was checked.

**Claude:** `[SETUP 7/8 - PRACTICE]` That is the most common gap, and the one that matters most in
reconciliation work.

... remaining topics: VS Code controls, permissions, commands, model and effort, usage discipline,
correction, plan review, diff review ...

Now choose one Guide 01 template for a read-only exercise, using invented data only. Not live
records, and not de-identified real records either.

**User:** The tie-out template. Can I use the structured-work-request skill?

**Claude:** `[SETUP 7/8 - PRACTICE]` Yes. Invoking `/structured-work-request`. The structured
request, restated in redacted form:

```text
Outcome:      identify variances between two synthetic extracts for ENTITY-A, PERIOD-1
Inputs:       two invented CSV extracts, created for this exercise
Rules:        SOURCE-LEDGER is authoritative when the two disagree
Proof:        control totals for both sides, plus a line-level exception list
Stop:         any variance without support, or any conflicting control total
Approval:     no filed value changes; this exercise produces no filing output
```

> Do you approve this request for the synthetic exercise?

**User:** Approved.

**Claude:** `[SETUP 7/8 - PRACTICE]` ... exercise completed and reviewed ... Two optional reads, no
install or configuration: `guides/02-multistate-property-tax-workflows.md` for the job lifecycle,
and `guides/03-professional-skills-by-category.md` for designing bounded local skills.

---

## Stage 8: receipt and finish

**Claude:**

```text
[SETUP 8/8 - COMPLETE]
Date: (run date)          Setup version: 1

VS Code                  PRESENT
Claude Code extension    PRESENT
Claude Code CLI          SKIPPED - APPROVAL REQUIRED
User instructions        CONFIGURED (backup verified)
VS Code settings         CONFIGURED (Default profile, backup verified)
Skills installed         structured-work-request, reconciliation-control-review
Verification             Available extension controls; organization usage page; unavailable items noted
Rollback outcomes        none required
Unresolved policy        none in this illustrative scenario
Next useful action       choose one bounded task from LEARN.md
```

This setup validated no tax, legal, or accounting conclusion. It configured tools and wrote two
reviewed files, both backed up and read back. Future improvement is proposal-only. I will never
self-modify instructions, settings, or skills.

---

## What to take from this

Six things this run did that a real run should also do. If a real run skips any of them, stop it and
say so.

1. Stopped at Stage 0 and asked for approval before inspecting anything.
2. Treated one unknown policy answer as a hard stop rather than as permission.
3. Read an existing file only after asking, and treated its embedded instruction as data.
4. Backed up, wrote once, and read back, on both writes.
5. Kept the existing value on every conflict unless the user chose otherwise.
6. Printed a receipt with no identifiers, paths, values, or totals in it.
