# riaz90

Python MCP server tool to calculate total working days for a given month in India.

## Features
- Accepts month input like `November 2026`, `2026-11`, or `11/2026`
- Excludes Saturdays and Sundays
- Excludes India public holidays, including year-specific holidays such as Eid, Diwali, Christmas, etc. based on the holiday library data
- Returns a structured result with a clear explanation

## Files
- `working_days_mcp.py` - FastMCP server with the `get_india_working_days` tool
- `requirements.txt` - Python dependencies

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
python working_days_mcp.py
```

## Tool
### `get_india_working_days(month_input: str)`
Example inputs:
- `November 2026`
- `2026-11`
- `11/2026`

Example result fields:
- `total_days_in_month`
- `weekend_days_excluded`
- `weekday_holidays_excluded`
- `total_working_days`
- `weekday_holidays`
- `explanation`
