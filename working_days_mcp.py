from __future__ import annotations

import calendar
from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Tuple

import holidays
from dateutil import parser
from fastmcp import FastMCP

mcp = FastMCP("india-working-days")


def parse_month_input(month_input: str) -> Tuple[int, int, str]:
    """Parse values like 'November 2026', '2026-11', or '11/2026'."""
    text = month_input.strip()

    for fmt in ("%Y-%m", "%m/%Y", "%B %Y", "%b %Y"):
        try:
            dt = datetime.strptime(text, fmt)
            label = dt.strftime("%B %Y")
            return dt.year, dt.month, label
        except ValueError:
            pass

    dt = parser.parse(text, default=datetime(2000, 1, 1))
    label = dt.strftime("%B %Y")
    return dt.year, dt.month, label


def get_month_dates(year: int, month: int) -> List[date]:
    _, last_day = calendar.monthrange(year, month)
    start = date(year, month, 1)
    return [start + timedelta(days=i) for i in range(last_day)]


def get_india_holidays_for_month(year: int, month: int) -> Dict[date, str]:
    in_holidays = holidays.country_holidays("IN", years=[year])
    result: Dict[date, str] = {}
    for holiday_date, holiday_name in in_holidays.items():
        if holiday_date.year == year and holiday_date.month == month:
            result[holiday_date] = str(holiday_name)
    return result


def calculate_working_days(year: int, month: int) -> Dict[str, Any]:
    all_dates = get_month_dates(year, month)
    holidays_in_month = get_india_holidays_for_month(year, month)

    weekend_days: List[str] = []
    holiday_days: List[Dict[str, str]] = []
    overlapping_holidays: List[Dict[str, str]] = []
    working_days: List[str] = []

    for current_date in all_dates:
        weekday = current_date.weekday()  # Monday=0, Sunday=6
        is_weekend = weekday in (5, 6)
        is_holiday = current_date in holidays_in_month

        if is_weekend:
            weekend_days.append(current_date.isoformat())

        if is_holiday:
            holiday_entry = {
                "date": current_date.isoformat(),
                "name": holidays_in_month[current_date],
            }
            if is_weekend:
                overlapping_holidays.append(holiday_entry)
            else:
                holiday_days.append(holiday_entry)

        if not is_weekend and not is_holiday:
            working_days.append(current_date.isoformat())

    month_label = datetime(year, month, 1).strftime("%B %Y")
    total_days = len(all_dates)
    weekend_count = len(weekend_days)
    holiday_count_excluding_weekends = len(holiday_days)
    total_working_days = len(working_days)

    explanation = (
        f"For {month_label}, there are {total_days} total days. "
        f"{weekend_count} days are Saturdays/Sundays. "
        f"{holiday_count_excluding_weekends} India public holidays fall on weekdays and are excluded as well. "
        f"Therefore, the total number of working days is {total_working_days}."
    )

    if overlapping_holidays:
        overlap_names = ", ".join(
            f"{item['name']} ({item['date']})" for item in overlapping_holidays
        )
        explanation += (
            f" Holidays already falling on weekends were not double-counted: {overlap_names}."
        )

    return {
        "month": month_label,
        "year": year,
        "month_number": month,
        "total_days_in_month": total_days,
        "weekend_days_excluded": weekend_count,
        "weekday_holidays_excluded": holiday_count_excluding_weekends,
        "total_working_days": total_working_days,
        "weekend_dates": weekend_days,
        "weekday_holidays": holiday_days,
        "weekend_holiday_overlap": overlapping_holidays,
        "explanation": explanation,
    }


@mcp.tool()
def get_india_working_days(month_input: str) -> Dict[str, Any]:
    """
    Return the total working days in a given month for India,
    excluding Saturdays, Sundays, and India public holidays.

    Args:
        month_input: Examples: 'November 2026', '2026-11', '11/2026'
    """
    year, month, _ = parse_month_input(month_input)
    return calculate_working_days(year, month)


if __name__ == "__main__":
    mcp.run()
