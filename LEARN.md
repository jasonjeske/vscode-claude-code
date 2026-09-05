# Learn Claude Code for your work

Use this as a small workbook, one lesson at a time. Read the page on GitHub or in VS Code, copy
only the prompt you need, and compare the result with the check. You do not need to understand
programming to start. All examples are invented and can later be adapted in an approved work folder.

**If Claude Code is not ready, complete [setup](START-HERE.md) first.** If it already works, begin
with [Lesson 1](learn/01-first-conversation.md). No additional dashboard, website, or learning app
is needed to use these pages.

![A five-step learning loop: name the task, select the input, ask Claude, check the evidence, and save the next step.](assets/learning/work-loop.svg)

*Original teaching diagram. Each lesson follows the same loop; the check is part of the task.*

## Your lessons

| Lesson | You will learn | You are ready to move on when... |
| --- | --- | --- |
| [1. Your first conversation](learn/01-first-conversation.md) | Where to type, how to ask, when to clarify, and what approval means | You can get a useful explanation and improve an unclear answer |
| [2. Understand and check a spreadsheet](learn/02-spreadsheet-work.md) | Read-only inspection, formulas, comparisons, and exceptions | You can explain a difference and verify its source totals |
| [3. Research a specific rule](learn/03-source-backed-research.md) | Scope, citations, historical applicability, and unknowns | You can tell an inspected source from an unsupported claim |
| [4. Turn checked findings into a report](learn/04-reports.md) | A concise memo, useful chart brief, and reviewer handoff | Every figure and conclusion can be traced to supplied evidence |
| [5. Make the template your own](learn/05-adapt-to-your-work.md) | Global versus project instructions, reusable prompts, and gradual improvement | You can adapt one task without copying private material into this repo |

Do not install every recommended skill before learning. Lesson 1 and the text exercises work with
the existing Claude conversation. Later steps say when a particular skill, file reader, browsing,
or Office tool is required. If it is unavailable, finish the supported part and mark the gap.

## Six words that make the interface less mysterious

| Term | Plain meaning |
| --- | --- |
| Prompt | The request you send Claude, including the result and checks you want |
| Context | The messages, instructions, and source material Claude can use in this conversation |
| Skill | A reusable set of instructions for a particular task; tools may still be required |
| Model | The AI selected by the approved setup; available choices vary |
| Token | A unit used to process text and other content; more context and output can use more allowance |
| CLAUDE.md | A Markdown instruction file that Claude Code reads in its documented scope |

Markdown is plain text with headings, lists, and code blocks. You can edit it in VS Code. A prompt
in a `text` box belongs in the **Claude chat input**. Shell commands belong in a terminal only when
a guide explicitly says so. Reading a command is not a reason to execute it.

## Your reusable request

```text
Guided mode. Help me produce [ONE RESULT] for [PERIOD OR QUESTION].
Use only [APPROVED INPUTS]. Follow [RULES] and preserve originals.
Show [CHECKS OR SOURCE CITATIONS]. Put the result in [CHAT OR APPROVED NEW FILE].
Ask only for missing details that materially affect the answer. Explain one useful concept.
```

Use **Teach** for a concept, **Guided** for a new task, and **Routine** for a proven process. These
are preferences from this kit, not built-in Claude permission modes. They do not grant new access.
Never shrink the evidence or hide an exception simply to produce a shorter answer.

## Keep these nearby

- [Skill catalog](SKILLS.md): what each skill does, how to install it, and a first example.
- [Daily desk guide](guides/DAILY-USE.md): a quick reference once the lessons are familiar.
- [Prompt library](prompts/PROMPT-LIBRARY.md): task templates to copy and adapt.
- [Learning/reference index](guides/README.md): deeper Excel, research, reporting, and usage guides.

Continue: **[Lesson 1: your first conversation](learn/01-first-conversation.md)**.
