# Guide 05: After onboarding, the growth path

You have finished the onboarding, used Claude Code on real work for a while, and it is starting to
feel routine. This guide is about what comes next.

The short version: you get better by making your requests sharper, your skills more bounded, and
your review faster, not by turning on more machinery. Nothing here unlocks a capability that
onboarding withheld, because onboarding did not withhold anything on the grounds that you were new.

## 1. The exclusions were never about your skill level

This is the important idea in the guide, so it comes first.

The starter configures no MCP servers, no connectors, no hooks, no plugins, and no subagents. It is
tempting to read that as training wheels, removed once you have proven yourself. It is not.

Those exclusions come from the data environment, not from your experience:

- You work with confidential records, so every additional channel that can reach that data is a new
  place it can go.
- Your account is a metered, centrally allocated workplace seat, so anything that multiplies context
  or runs autonomously spends an allowance that is not only yours.
- Untrusted content reaches your work. Documents, exports, and web pages can carry instructions, and
  a tool with more reach turns a prompt injection into a bigger problem.

None of those three facts changes because you got good at Claude Code. **Graduation does not unlock
MCP servers, connectors, hooks, plugins, or subagents.** If anything, being experienced enough to
want them is exactly when the reasoning above matters most, because you now have enough skill to
build something that fails quietly.

What does change with experience is your judgment about scope, your ability to review a diff
quickly, and the quality of the bounded tools you build. That is the growth path, and it is real
growth, not a consolation prize.

## 2. Graduation checklist

You are ready to move past the beginner path when all of these are true. Be honest; nobody is
checking.

- You write requests that name outcome, inputs, rules, proof, and stop conditions without looking up
  the formula.
- You have refused at least one plan that sounded reasonable and was not what you asked for.
- You read the file list in a diff before the content, every time.
- You have run a rollback at least once and seen it work, rather than assuming it would.
- You know what your `/usage` looks like in a normal week, so an abnormal one is visible.
- You can say precisely what a skill can and cannot do, and you do not describe one as enforcement.
- You have caught Claude being confidently wrong on your own domain at least once, and you know
  which kinds of claim to distrust.
- You keep synthetic exercises synthetic, and you have never used a de-identified real record as
  test data.

If several of those are not true yet, the useful next step is more reps on real work, not more
configuration.

## 3. Build more bounded skills

The main way this setup grows is more small, user-invoked skills, built by the method in
[Guide 03](03-professional-skills-by-category.md).

A task earns a skill when it is repeated, when its steps are stable, and when getting it wrong is
expensive enough that you want the steps written down. Three repetitions is a reasonable threshold.
Once is a prompt, not a skill.

Keep every skill inside the same boundary the original three respect:

- `disable-model-invocation: true`, so it runs only when you invoke it by name. A skill that can
  start itself is a skill you did not decide to run.
- One job, stated in the description, with the boundary written into the body.
- Read-only unless a write is genuinely the point, and any write is approval-gated and reviewed.
- A fixed output contract where one applies, the way `reconciliation-control-review` fixes `PASS`,
  `FAIL`, and `UNVERIFIED`. A fixed contract is what makes an output reviewable at a glance.
- No real identifiers in the skill text. Placeholders only, the same as everywhere else.

Before you install a new skill, run `node tests/validate-repo.mjs`. It checks the frontmatter schema
that Stage 5 validates by hand, and catching a malformed skill locally is cheaper than discovering it
mid-task.

The failure mode to avoid is a skill that grows into a workflow. When a skill starts describing
several stages that hand off to each other, you have built an autonomous process with extra steps.
Split it, or leave the coordination to yourself.

## 4. Per-project instruction files

Once you work in more than one project, per-project instructions stop being optional overhead and
start saving real repetition.

The pattern is: run `/init` in an approved project, read what Claude generates, then improve it
against [`templates/PROJECT-CLAUDE.md`](../templates/PROJECT-CLAUDE.md) as a checklist. Do not paste
the template in wholesale. It is a list of things worth stating, not a file to copy.

Two rules that matter more than the content:

1. **Project instructions are not a second place to put confidential context.** Same standard as
   everywhere else: categories, placeholders, no identifiers, no values, no internal paths. A
   project instruction file is a file like any other, and it gets committed, backed up, and synced
   like any other.
2. **Review a generated instruction file the way you would review a diff.** `/init` writes what it
   infers, and inference is where wrong facts get stated confidently and then carried into every
   future session in that project.

More instruction files do not create an enforcement boundary. Three files saying "always require
approval" is not more binding than one. It is just more to keep current.

## 5. Usage discipline at higher volume

Doing more work makes usage a real constraint rather than a footnote. The discipline scales like
this.

- Check `/usage` on a rhythm, not on a scare. Weekly is enough to know your normal.
- Match effort to the task rather than to your anxiety. High effort for substantive analysis; lower
  for genuinely routine, low-risk work. See [`docs/MODELS-AND-USAGE.md`](../docs/MODELS-AND-USAGE.md).
- Watch context length on long sessions. A session that has drifted across four topics is both
  expensive and worse at the current one. Start a fresh session instead.
- Notice the pull toward autonomy when you are busy. "Just keep going and tell me when you are done"
  is the request that spends the most and gets reviewed the least. It is also the one this starter
  most deliberately excludes.
- Never reduce a control to save usage. If the honest work does not fit the allowance, that is a
  resourcing conversation with your manager, not something to solve by checking less.

## 6. If you think you need an MCP server or a connector

Sometimes the answer really is that a bounded tool is not enough. That is not a decision you make
alone at your desk, and it is not a decision this repository can make for you. It is an
organizational decision, and it belongs to the people who own the data and the risk.

Take it to them with answers to these questions, because they are the questions a reviewer will ask
and having them ready is the difference between a fast yes and an indefinite maybe.

**What problem does it solve that a bounded skill cannot?** If a skill can do it, this conversation
is over and the answer is a skill.

**What data can it reach?** Not what you intend to use it for. What it is technically able to read,
write, or send, including on a day when something goes wrong.

**Who publishes it, and what is the update path?** A server that auto-updates from a third party is
a standing change to your machine's trusted surface, not a one-time install.

**What untrusted content will it process?** Anything that reads documents, tickets, email, or web
pages is a prompt-injection path. Name it explicitly rather than letting it be discovered.

**Who approves it, and who reviews it later?** An approval with no review date is a permanent grant
made on one day's information.

**What is the rollback?** How do you turn it off, who notices if it misbehaves, and what evidence
would tell you it did.

**What does the organization's policy already say?** Ask before proposing. The answer may be settled.

Bring that to your security or IT function as a proposal, and let them decide. If they approve it,
the approval is theirs and it comes with their conditions. If they decline, that is a real answer,
and the bounded path in this repository still does the work.

What you should not do: install it yourself to try it out, run it against real records to build a
case, or treat a personal-account setup at home as evidence that the work setup is safe. Those are
the three shapes this goes wrong in.

## 7. Where this connects

- [Guide 03](03-professional-skills-by-category.md) is the method for designing a bounded skill.
- [Guide 04](04-reviewing-claude-plans-and-diffs.md) is the review discipline that everything above
  depends on.
- [The security boundary](../docs/SECURITY.md) explains why instructions are guidance and not
  enforcement, which is the reason the exclusions in section 1 are structural.
- [`docs/WINDOWS-VERIFICATION.md`](../docs/WINDOWS-VERIFICATION.md) is worth reading once, because
  knowing which claims are unverified is part of using this repository honestly.

## 8. Official references

- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code memory and instruction files](https://code.claude.com/docs/en/memory)
- [Claude Code security](https://code.claude.com/docs/en/security)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
