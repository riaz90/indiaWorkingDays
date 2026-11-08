# Pull Request Merge Guide

This document explains what each open PR is about, how to validate it, and what to check before merging.

## Open PRs

### PR #1 — Add Python MCP tool to calculate India working days by month
- **PR Link:** https://github.com/riaz90/riaz90/pull/1
- **Branch:** `feature/python-mcp-working-days-india`
- **Base branch:** `main`

#### What this PR adds
This PR adds a Python MCP tool that calculates the total working days for a given month in India.

It excludes:
- Saturdays
- Sundays
- India public/festival holidays supported by the holiday library

It also returns an explanation containing:
- total days in the month
- weekends excluded
- weekday holidays excluded
- holiday names and dates considered
- final working day count

#### Supported input examples
The tool is designed to accept month input in these formats:
- `November 2026`
- `2026-11`
- `11/2026`

#### Example usage
Input:
```text
November 2026
```

Expected response shape:
```json
{
  "month": "November 2026",
  "total_days": 30,
  "weekend_days": 9,
  "weekday_holidays": 1,
  "working_days": 20,
  "holidays": [
    {
      "date": "2026-11-XX",
      "name": "Example holiday"
    }
  ],
  "explanation": "November 2026 has 30 total days. 9 weekend days and 1 weekday holiday were excluded, leaving 20 working days."
}
```

> Note: The exact holiday list depends on the holiday dataset available for India for the requested year.

#### Validation checklist before merge
- [ ] Confirm the tool runs with Python successfully
- [ ] Confirm supported input formats work as documented
- [ ] Confirm invalid inputs return a clear validation error
- [ ] Confirm Saturdays and Sundays are excluded
- [ ] Confirm India holidays are excluded when they fall on weekdays
- [ ] Confirm README or documentation remains appropriate for a profile repository
- [ ] Confirm tests pass locally or in CI

#### Suggested manual test cases
1. Valid month name input
   - Input: `November 2026`
   - Check: returns a structured explanation and working day count

2. Valid numeric input
   - Input: `2026-11`
   - Check: same result as `November 2026`

3. Alternate numeric format
   - Input: `11/2026`
   - Check: same result as `November 2026`

4. Invalid input
   - Input: `2026/November`
   - Check: returns a clear error message

5. Holiday-sensitive month
   - Input: a month containing a festival/public holiday in India
   - Check: weekday holidays are excluded correctly

#### Merge recommendation
Merge after validation if:
- documentation is acceptable for this repository,
- tests pass,
- and the holiday-handling behavior matches expectations.

---

## Template for future PRs
Use this section format when adding more PR summaries to this file.

### PR #<number> — <title>
- **PR Link:** <url>
- **Branch:** `<branch>`
- **Base branch:** `<base>`

#### What this PR adds
Describe the change in plain language.

#### Supported input examples
- `<example 1>`
- `<example 2>`

#### Example usage
Input:
```text
<sample input>
```

Expected response shape:
```json
{
  "example": true
}
```

#### Validation checklist before merge
- [ ] Behavior matches PR description
- [ ] Edge cases reviewed
- [ ] Tests added or updated
- [ ] Documentation updated
- [ ] Safe to merge

#### Merge recommendation
State when this PR should be merged.
