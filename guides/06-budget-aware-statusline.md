# Guide 06: A budget-aware status line

A workplace Claude Code seat is often metered, not unlimited. If your employer gave you a monthly
figure, corporate seats built on token-based usage commonly land somewhere in the tens to low
hundreds of dollars a month, and it is easy to burn through it in a day or two without noticing,
then discover mid-project that there is nothing left until next month. This guide adds a status
line: a small bar Claude Code can show at the bottom of every session with your context usage, this
session's cost, and, when your organization has the plumbing for it, your spend-cap utilization.

Read this guide before installing anything. The honesty of the numbers depends on which of two very
different situations you are in, and the status line cannot tell them apart for you.

## 1. What Claude Code actually knows about your spend

Every claim below was checked against Anthropic's own documentation before this guide was written,
not assumed. Claude Code's status line receives one JSON object per update. Three fields matter
here, and they are not the same thing:

- **`cost.total_cost_usd`** is always available once a session has made its first request. It is
  Claude Code's own client-side estimate, at list price, of what this one session has cost so far.
  It resets to zero every time you run `/clear`. It is never your monthly total and never your
  organization's real bill.
- **`rate_limits.five_hour` and `rate_limits.seven_day`** are rolling rate-limit windows. They exist
  only for Claude.ai Pro and Max subscribers, which is a personal-subscription concept, not a
  workplace-seat concept. Most corporate, token-metered seats will not see these fields at all.
- **`rate_limits.spend_limit`** is the field that actually answers "how much of my monthly cap have
  I used." It exists only when your organization runs a **Claude apps gateway** with a spend limit
  configured for you specifically, and only on Claude Code version 2.1.251 or later. When present,
  it gives a percentage, from 0 to 100 (and above 100 once you exceed the cap), plus the time the
  period resets. Claude Code deliberately reports this as a percentage. It does not report a dollar
  amount, because the gateway enforces the cap centrally and Claude Code only ever sees your
  utilization of it.

If your organization does not run that gateway, or has not set a limit for you, none of the spend
fields above exist, and the honest status line is a session-cost counter plus a reminder to check
with whoever administers your Claude Code seat. That is not a failure of this guide; it is the
actual state of what Claude Code can see from where you sit.

## 2. Find out which situation you are in

Ask whoever administers your Claude Code deployment one direct question: **does my seat have a
Claude Code spend limit configured, and if so, what is the monthly figure in dollars?**

You are looking for one of three answers:

1. **"Yes, and here is the number."** You have everything this guide's status line can use. Continue
   to section 3 and fill in the real figure.
2. **"Yes, but I do not know the exact dollar figure off the top of my head."** The status line still
   works. It shows the percentage Claude Code itself reports, with no invented dollar amount, until
   you get the real number.
3. **"No" or "I do not know."** The gateway percentage will not appear. The status line falls back to
   session cost and, on a personal Pro or Max subscription, the five-hour and weekly windows. This is
   the common case for many workplace seats today, and it is worth asking again later if your
   organization's tooling changes.

Never guess a dollar figure to make the status line show a number. A guessed cap is worse than no
cap, because it looks authoritative and is not.

## 3. Install it

The status line lives in `config/statusline.ps1` in this repository. It is PowerShell, matching the
Windows terminal profile this starter already sets, and it needs nothing beyond what Windows already
has, no Node, no additional install.

With separate approval for this specific action:

1. Copy `config/statusline.ps1` to `%USERPROFILE%\.claude\statusline.ps1`, or another location you
   prefer, keeping the file name.
2. If you have a real monthly budget figure from section 2, copy
   `config/statusline-budget.example.json` to `statusline-budget.json` in the **same folder** as
   `statusline.ps1`, and replace `null` with that number. If you do not have a figure yet, skip this
   step; the script handles a missing file by showing the percentage alone.
3. Add a `statusLine` entry to your Claude Code settings (`~/.claude/settings.json`, or your project
   settings), pointing at the script:

   ```json
   {
     "statusLine": {
       "type": "command",
       "command": "powershell -NoProfile -File C:/Users/YOUR-USERNAME/.claude/statusline.ps1"
     }
   }
   ```

   Use forward slashes in the path even though this is a Windows path; Claude Code's status line
   command can run through Git Bash, which treats backslashes as escape characters and breaks an
   unquoted Windows path silently. Replace `YOUR-USERNAME` and the folder with wherever you actually
   put the script in step 1.

4. Start a new session and confirm a line appears at the bottom.

You can also ask Claude Code to do the merge for you with `/statusline`, the same way Stage 4 of the
onboarding merges VS Code settings: review what it proposes, and never let an automatic merge
overwrite a `statusLine` entry a managed policy already set.

## 4. Read what it shows you

A line might read:

```
[Sonnet] ctx 34% | session $1.42 (this session only) | cap $46.00 of $80.00 est. (58% of gateway cap)
```

or, without a gateway spend limit configured:

```
[Sonnet] ctx 34% | session $1.42 (this session only)
```

`ctx` is your context window filling up, unrelated to money. `session` is this conversation's cost
estimate and resets on `/clear`; it is not your monthly total. `cap`, when it appears, is the one
number that reflects your actual organizational limit, reported as a percentage by Claude Code and
turned into an estimated dollar figure locally, in the script, using the number you typed into
`statusline-budget.json`. That dollar figure is arithmetic on your own input, not a second source of
truth. If your real cap changes, update the file; the script does not fetch it from anywhere.

## 5. What to do before you start a large task

If `cap` is climbing fast, or `session` alone is already a meaningful fraction of what you know your
monthly figure to be, size the task before you start it rather than after you run out. A large
project against a small remaining balance is a conversation to have with whoever owns your seat's
budget, not a reason to switch to a cheaper model mid-task and hope the reconciliation logic still
holds. See [Guide 01](01-claude-code-fundamentals.md) on model and effort choice, and
[docs/MODELS-AND-USAGE.md](../docs/MODELS-AND-USAGE.md) for the fuller usage-discipline picture this
status line is meant to support, not replace.
