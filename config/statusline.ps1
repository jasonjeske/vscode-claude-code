# Optional Claude Code status line: context usage, this session's cost, and (only
# when your organization runs a Claude apps gateway with a spend limit configured
# for you) your cap utilization.
#
# What each number actually is, verified against Anthropic's own documentation
# before this script was written (see guides/06-budget-aware-statusline.md):
#
#   - "ctx"     context_window.used_percentage. Live, always present after the
#               first response in a session.
#   - "session" cost.total_cost_usd. Claude Code's own client-side estimate at
#               list price for THIS session only. Resets to zero on /clear. This
#               is never your organization's real bill or your monthly total.
#   - "cap"     rate_limits.spend_limit.used_percentage. Present ONLY when your
#               organization runs a Claude apps gateway with a spend limit set
#               for you, and only on Claude Code v2.1.251 or later. Claude Code
#               reports this as a PERCENTAGE, never a dollar figure.
#   - "5h"      rate_limits.five_hour.used_percentage, shown as a fallback only
#               when no gateway spend limit is present. Present only for
#               Claude.ai Pro or Max subscribers.
#
# The dollar amount next to "cap" is NOT reported by Claude Code. It is
# calculated locally, in this script, as (spend limit percentage / 100) times a
# monthly budget figure YOU type into statusline-budget.json next to this
# script. If that file is absent, this script shows the percentage alone and
# invents no dollar figure. Ask your Claude Code administrator for your real
# monthly cap before filling in that file; do not guess.

try {
    $input_json = $input | Out-String | ConvertFrom-Json

    $model = $input_json.model.display_name
    $ctxPct = $input_json.context_window.used_percentage
    $sessionCost = $input_json.cost.total_cost_usd
    $spendPct = $input_json.rate_limits.spend_limit.used_percentage
    $fiveHourPct = $input_json.rate_limits.five_hour.used_percentage

    $parts = New-Object System.Collections.ArrayList

    if ($model) {
        [void]$parts.Add("[$model]")
    }

    if ($null -ne $ctxPct) {
        $ctxRounded = [math]::Round($ctxPct)
        [void]$parts.Add("ctx ${ctxRounded}%")
    }

    if ($null -ne $sessionCost) {
        $sessionRounded = [math]::Round($sessionCost, 2)
        [void]$parts.Add("session `$$sessionRounded (this session only)")
    }

    if ($null -ne $spendPct) {
        $spendRounded = [math]::Round($spendPct)
        $budgetPath = Join-Path $PSScriptRoot "statusline-budget.json"
        $budget = $null
        if (Test-Path $budgetPath) {
            try {
                $budgetData = Get-Content $budgetPath -Raw | ConvertFrom-Json
                $budget = $budgetData.monthly_budget_usd
            } catch {
                $budget = $null
            }
        }
        if ($budget) {
            $estSpent = [math]::Round(($spendPct / 100) * $budget, 2)
            [void]$parts.Add("cap `$$estSpent of `$$budget est. (${spendRounded}% of gateway cap)")
        } else {
            [void]$parts.Add("cap ${spendRounded}% used (gateway spend limit)")
        }
    } elseif ($null -ne $fiveHourPct) {
        $fiveHourRounded = [math]::Round($fiveHourPct)
        [void]$parts.Add("5h ${fiveHourRounded}%")
    }

    if ($parts.Count -eq 0) {
        Write-Host "Claude Code"
    } else {
        Write-Host ($parts -join " | ")
    }
} catch {
    # Never let a malformed input or a broken budget file take down the status
    # line. Print the minimum that is always true and stop.
    Write-Host "Claude Code"
}
