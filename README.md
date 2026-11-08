- 👋 Hi, I’m @riaz90
- 👀 I’m interested in software development, integration tooling, and automation
- 🌱 I’m currently learning and building MCP-based tools and API integrations
- 💞️ I’m looking to collaborate on practical developer tooling and backend automation
- 📫 How to reach me: via GitHub

## India Working Days MCP Tool

This repository now also includes a Python MCP server tool to calculate total working days for a given month in India.

### Features
- Accepts month input like `November 2026`, `2026-11`, `11/2026`, or `Nov 2026`
- Excludes Saturdays and Sundays
- Excludes India public holidays, including year-specific holidays such as Eid, Diwali, Christmas, etc. when available in the holiday dataset
- Returns a structured result with a clear explanation

### Files
- `working_days_mcp.py` - FastMCP server with the `get_india_working_days` tool
- `requirements.txt` - Python dependencies
- `tests/test_working_days_mcp.py` - basic test coverage for parsing and working-day calculation

### Install
```bash
pip install -r requirements.txt
```

### Run
```bash
python working_days_mcp.py
```

### Tool
#### `get_india_working_days(month_input: str)`
Example inputs:
- `November 2026`
- `2026-11`
- `11/2026`
- `Nov 2026`

Example result fields:
- `total_days_in_month`
- `weekend_days_excluded`
- `weekday_holidays_excluded`
- `total_working_days`
- `weekday_holidays`
- `explanation`

### Notes / limitations
- Holiday coverage depends on the `holidays` package data for India and the requested year.
- Some movable or festival holidays may vary year to year and are included only when present in the underlying holiday library.

<!---
riaz90/riaz90 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
