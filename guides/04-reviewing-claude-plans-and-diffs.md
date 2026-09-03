# Guide 04: Reviewing Claude's plans and diffs

Builds on [Guide 01](01-claude-code-fundamentals.md), which introduced plan review and diff review
in sections 7 and 8. This guide is the long version of those two sections, because they are the
place where a confident-sounding wrong answer becomes a real change to a real file.

Everything in this repository is approval-gated. That design is worth nothing if approval is a
reflex. The gate only works if somebody reads what is behind it, and reading it well is a skill.

## 1. What you are actually approving

When Claude asks for approval, it is asking for one of three different things. Tell them apart,
because they carry different risk.

| You are approving | What can go wrong | How reversible |
|---|---|---|
| A plan | Wasted work, wrong direction, scope you did not intend | Fully; nothing has happened yet |
| A read | Content you did not want processed leaves your machine | Not reversible; it has been read |
| A write | A file you depend on is changed or lost | Only if a backup exists and was verified |

The read case is the one people underestimate. Approving "may I read your existing instructions
file" is not a small yes if that file contains something confidential. Stage 3 of
[START-HERE.md](../START-HERE.md) asks separately for exactly this reason.

## 2. How to read a plan before approving it

A plan is a claim about the future. Check it against five questions, in this order.

1. **Does the plan name the same outcome I asked for?** If you asked for a variance list and the
   plan proposes to correct the variances, the target has changed. Stop there.
2. **Does it name its inputs exactly?** "Review the reconciliation" is not an input. "Read the two
   CSV extracts in this folder" is.
3. **Does it say what it will not do?** A plan with no boundary is a plan that will grow.
4. **Does it name the proof?** How will you know it worked? If the plan produces an answer but no
   evidence, you cannot review the result either.
5. **Does it say where it stops for me?** Every write, every external send, every irreversible step
   should be named as a stop, not discovered later.

If any of the five is missing, the correct response is not to approve with a caveat. It is to ask
for the missing one. Caveats in chat are not constraints; they are suggestions that compete with
everything else in the context.

## 3. How to read a diff or a candidate

A diff is a claim about a specific change. Read it in this order, because the order front-loads the
cheap checks that catch the expensive mistakes.

1. **Read the file list first, before any content.** More files than you expected is the single
   loudest signal that something is wrong. One file was asked for; three files are in the diff.
2. **For each file, read the removals before the additions.** People read additions because they are
   the interesting part. Removals are where your existing work disappears.
3. **Check that unrelated content is untouched.** In a settings merge, this means your theme, your
   font, your keybindings, and anything else you did not discuss.
4. **Read the additions for things you did not ask for.** A helpful extra setting is still an
   unrequested change to a managed machine.
5. **Confirm the backup exists and was read back.** Not "a backup was created". Created and read.

For a settings candidate specifically, the merge rules are pinned in `tests/merge-spec.mjs`. If you
want to know what a correct merge looks like before you approve one, run
`node tests/merge-spec.mjs` and read the three cases. Your existing values should win every
conflict, and nothing that weakens a security control should survive.

## 4. Red flags

These are the patterns worth stopping on. None of them is proof of a problem. All of them are worth
one more question.

**Scope growth.** The plan or diff touches more than the request did. Common shapes: "while I was in
there I also", a second file that was not discussed, a refactor attached to a fix, or a settings
change bundled with an instruction change.

**Unverifiable claims.** Any sentence that asserts an outcome without naming how it was checked.
"The totals now tie" is unverifiable. "The totals tie: SOURCE-LEDGER control total matches the
exception list remainder, both shown below" is verifiable. Treat "should work", "this will fix it",
and "verified" with no named check as unfinished, not as done.

**Real identifiers appearing.** During setup and any synthetic exercise, nothing should contain a
real entity name, a real address, a real taxpayer or property identifier, an internal URL, an
absolute path with your username in it, or an actual value or total. If one appears, something read
data it should not have. Stop and find out what.

**Confidence that outruns the evidence.** Long, fluent, and specific is not the same as correct. The
question is always which tool call or which file produced that claim.

**A stop condition that quietly disappeared.** You named a stop in the request. The plan repeats it.
The diff no longer mentions it. That is worth asking about before approving.

**Approval bundling.** "Approve the plan and I will make the changes" merges two decisions into one.
Ask for them separately. The plan being right does not make the diff right.

## 5. What a good refusal looks like

Refusing is normal and should be cheap. It is not a confrontation, and it does not require you to
know what the right answer is. These are all complete, sufficient refusals.

> No. Show me the diff for that one file first.

> No. That is three files and I asked about one. Explain the other two.

> Not yet. What check produced that number?

> Stop. That path contains a real identifier. Where did it come from?

> No. Split that into the plan approval and the write approval.

> Not now. Confirm the backup was read back before you write anything else.

Two things a good refusal is not. It is not an apology, and it does not need to propose an
alternative. "No, show me X first" is a complete sentence. You are the authorized human in the loop,
and being unsure is a sufficient reason to hold.

If you are refusing the same thing repeatedly, that is a signal about the request rather than about
the answer. Go back and make the original request name its boundary, per Guide 01's prompt formula.

## 6. Practice exercise

Synthetic data only. Invent everything. Do not use a real extract, and do not use a de-identified
real extract either.

**Setup.** Create a scratch folder outside this checkout with two invented CSV files representing
two views of the same six rows for ENTITY-A, PERIOD-1. Introduce exactly two differences: one row
present in one file and missing from the other, and one row where an amount differs.

**Request.** Ask for a read-only variance list. Name SOURCE-LEDGER as authoritative. Ask for control
totals for both sides as proof. Say explicitly that nothing may be written.

**What to check in the plan.** Does it restate both differences as things to find rather than things
to fix? Does it name both files as inputs? Does it confirm that it will write nothing?

**What to check in the result.** Are both differences found? Are the control totals shown, and do
they support the conclusion? Is anything asserted that you cannot trace to one of the two files?

**Then break it on purpose.** Run it again and ask Claude to "clean up the discrepancies". Watch
what the plan proposes. This is the drill that matters: it is the one where approving is the wrong
move, and you want to have felt that once in a synthetic folder rather than for the first time on a
real reconciliation.

**Then refuse it.** Practice saying no to a plan that sounds helpful and reasonable and is not what
you asked for.

## 7. Common mistakes

- **Approving the plan and the diff in one breath.** Two decisions, two reviews.
- **Reading additions and skipping removals.** Removals are where losses hide.
- **Accepting a summary of a diff instead of the diff.** A summary is a claim about the change,
  written by the same process that made the change.
- **Treating a long explanation as evidence.** Length is not proof.
- **Approving because it is the third attempt and you are tired.** Fatigue is when the gate matters
  most and works least. Stop the session instead.
- **Assuming a backup is a rollback.** A backup that was never read back is a hope, not a rollback.
- **Reviewing a write to a managed machine the same way you would review a scratch file.** The blast
  radius is different, so the standard should be too.

## 8. Where this connects

- [Guide 01](01-claude-code-fundamentals.md) sections 7 and 8 introduce plan and diff review.
- [Guide 03](03-professional-skills-by-category.md) covers designing bounded skills, which is the
  same review discipline applied to something you keep.
- [The security boundary](../docs/SECURITY.md) explains why instructions are not enforcement, which
  is the reason review is a human job rather than a configured one.
- `tests/QA-RUNBOOK.md` procedure P3 is the rollback drill, and it is worth running once so you have
  seen a rollback actually happen.

## 9. Official references

- [Claude Code security](https://code.claude.com/docs/en/security)
- [Claude Code settings](https://code.claude.com/docs/en/settings)
- [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)
