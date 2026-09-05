# Lesson 1: your first conversation

[Learning home](../LEARN.md) | Next: [Spreadsheet work](02-spreadsheet-work.md)

**Goal:** ask a clear question, improve the answer, and recognize when a proposed action needs review.
**You need:** the approved Claude Code extension already working in VS Code. No extra skill or files.

## Open a small practice space

If you have not created a practice folder yet, use [the Windows first-run walkthrough](../README.md).
It includes every File Explorer and VS Code step. If you already completed its first output,
you can use this lesson as a reference and move straight to today's task.

1. Use **File > Open Folder** in VS Code to select an approved practice folder outside this public
   starter. Use the existing workplace sign-in and gateway.
2. Follow [open the Claude panel](../guides/00-use-vscode.md#1-find-the-right-place-to-type) if needed.
3. Check the approved account/provider using the available status view. Keep credentials private.
4. Begin a new conversation and paste the prompt below into Claude's input, not the terminal.

Keep the approved model default. Send once and wait for the answer or an approval question.
There is no time limit for this lesson; use [wait, respond, or stop](../guides/00-use-vscode.md#5-know-whether-to-wait-respond-or-stop)
if progress is unclear.

[Official VS Code guide](https://code.claude.com/docs/en/vs-code).

## Ask for an explanation first

```text
Teach mode. Explain what a reconciliation is using two invented amounts: the book shows $200
and the bill shows $210. Explain the $10 difference and one thing I must check before deciding
what to do. Use plain English. No files, browsing, or changes are needed.
```

**Look for:** an explanation that comparison reveals a difference but does not establish its cause.
Claude should not decide that $10 must be paid, posted, written off, or corrected. You supplied
amounts, not evidence of the correct treatment.

If the answer is too technical, continue in the same conversation:

```text
Explain that again for a first-time user. Keep the amounts unchanged and define any unfamiliar
accounting term. Give me one concrete check instead of a long list.
```

This is normal use. You can correct the scope or ask for clarification without starting over.

## Turn a vague request into a useful one

“Help with my Excel” gives little direction. A better request names the result, inputs, and check:

```text
Guided mode. I want to understand an unfamiliar workbook before changing it. I will select one
approved synthetic copy. Propose a read-only sheet map and the checks needed to understand its
formulas. Do not open unrelated folders or save the workbook. Ask for the missing input reference.
```

Here the missing file reference is a useful question. Claude should not scan the computer to guess
which workbook you meant. When you are ready, select the intended file with the available `@`
file picker. Referencing a file lets Claude process its content through the configured service.

If `/prompt-coach` is installed, it can help write the request. It is optional; a well-scoped normal
prompt works too. Type `/` to inspect the actual available commands rather than guessing names.

## Read a proposed action before approving it

Check **which input**, **which output**, and **what changes**. Approval of a reviewed new output
does not approve altering every source file. If a proposal is broader than your request, say:

```text
Limit this to the selected input and the agreed new output. Explain any additional file or tool
you need before expanding the scope. Keep the original unchanged.
```

The kit's teaching modes control explanation style. Claude's permission modes and workplace policy
control a different part of the workflow. Do not change permission settings just to remove a prompt.

## Check your understanding

You should be able to explain why the $10 difference is an exception to investigate, identify the
file you authorized, and name the output you want. If not, ask Claude to explain that one point.

For unrelated work, start a new conversation. For a correction to the same task, keep the relevant
context. Check the organization's usage website; `/context`, if offered, measures a different thing.
Never infer the employer's remaining balance from the length of the answer alone.

Next: **[Lesson 2: understand and check a spreadsheet](02-spreadsheet-work.md)**.
