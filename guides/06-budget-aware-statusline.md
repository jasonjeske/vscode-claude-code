# Optional usage status line

Start with the built-in usage/context views and [the token guide](13-token-efficient-work.md).
This optional PowerShell script displays available session data through Claude Code's status-line
interface. It is not a spend cap and is not required by the short setup. Check the interface you
actually use; do not assume a terminal status-line customization appears in VS Code's native panel
or application status bar.

## Know what the numbers mean

Source review: September 5, 2026 (UTC).

| Display | Source field | Meaning |
| --- | --- | --- |
| `ctx` | `context_window.used_percentage` | Context usage, not money; may be unavailable early in a session |
| `session` | `cost.total_cost_usd` | Client-side estimated session cost, using list or configured managed pricing |
| `cap` | `rate_limits.spend_limit.used_percentage` | Usage percentage reported by a compatible Claude apps gateway with a configured spend limit |
| `5h` | `rate_limits.five_hour.used_percentage` | Subscription-window percentage when supplied, used as a fallback by this script |

Current Claude Code resets its session estimate on `/clear`; older versions differed. The spend
field requires the documented gateway support and version, not merely any LLM gateway. Its period
is not inherently monthly. Missing fields mean unavailable, not zero consumption. The script does
not display the seven-day window even if the input includes it.
[Official status-line fields](https://code.claude.com/docs/en/statusline),
[cost reporting](https://code.claude.com/docs/en/costs).

For the actual allowance and remaining balance, use the employer's approved report. Do not infer
that a field will be absent simply because the user does not know their limit.

## Install only if this display helps

Review [statusline.ps1](../config/statusline.ps1). It uses Windows PowerShell with no additional
library. Managed script policy may still block execution; do not change execution policy to bypass it.

1. Review the selected destination and existing status-line configuration. Keep a verified backup
   before replacing anything. Obtain approval for the precise script copy and settings change.
2. Copy the script to the approved location, such as `%USERPROFILE%\.claude\statusline.ps1`.
3. Merge the following entry into the permitted Claude Code settings file. Preserve all unrelated
   settings and any managed configuration. Replace the placeholder path locally; quote it as shown
   so a path containing spaces remains one argument.

```json
{
  "statusLine": {
    "type": "command",
    "command": "powershell -NoProfile -File \"C:/Users/YOUR-USERNAME/.claude/statusline.ps1\""
  }
}
```

4. Compare the saved script/settings with the reviewed copies. Start the supported Claude session
   and check which segments actually appear. Compare them with the available usage view.
5. Record the real result in [the Windows ledger](../docs/WINDOWS-VERIFICATION.md) or a private
   setup receipt. Windows execution and shell compatibility have not been tested by this kit.

You can use the supported `/statusline` command to help configure the display after reviewing its
proposed changes. Do not replace an existing display just to follow this example.

## Optional dollar conversion for a confirmed monthly cap

The script can multiply the gateway percentage by a locally supplied monthly USD cap. Use this
only if the administrator confirms the **same** cap, currency, and monthly period represented by
that percentage. Otherwise leave the budget file absent and show the percentage alone.

For a confirmed match, copy [the blank example](../config/statusline-budget.example.json) beside
the script as `statusline-budget.json`, then replace `null` locally with the confirmed figure.
The result is arithmetic on that input, not an independently obtained balance. Update or remove
it if the cap or period changes. Keep the filled file out of this public repository.

An illustrative display without that conversion:

```text
[MODEL] | ctx 34% | session $1.42 (this session only) | cap 58% used (gateway spend limit)
```

The gateway segment is shown only when provided. The example is invented, not a real account.

## Undo

Restore the reviewed predecessor for `statusLine` or remove only the entry you added. Remove the
copied script/budget file only if they belong to this installation. Keep other Claude settings.
Verify that the previous display returns or the custom display is gone. A setup receipt should
record the backup and outcome without credentials or private account details.
