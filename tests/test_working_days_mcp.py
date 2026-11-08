from working_days_mcp import calculate_working_days, parse_month_input


def test_parse_month_input_supported_formats():
    assert parse_month_input("2026-11")[:2] == (2026, 11)
    assert parse_month_input("11/2026")[:2] == (2026, 11)
    assert parse_month_input("November 2026")[:2] == (2026, 11)
    assert parse_month_input("Nov 2026")[:2] == (2026, 11)


def test_parse_month_input_rejects_invalid_values():
    try:
        parse_month_input("next month please")
        assert False, "Expected ValueError for invalid input"
    except ValueError:
        pass


def test_calculate_working_days_returns_expected_shape():
    result = calculate_working_days(2026, 11)

    assert result["month"] == "November 2026"
    assert result["year"] == 2026
    assert result["month_number"] == 11
    assert result["total_days_in_month"] == 30
    assert result["weekend_days_excluded"] >= 8
    assert "total_working_days" in result
    assert "explanation" in result
