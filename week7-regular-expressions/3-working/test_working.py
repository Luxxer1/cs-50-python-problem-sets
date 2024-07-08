from working import convert
import pytest

def test_str_format():
    with pytest.raises(ValueError):
        convert("9:00 PM 9:00 AM")

def test_hours_and_minutes_off():
    assert convert("9 AM to 10 AM") == "09:00 to 10:00"

def test_out_of_range_hour_and_minutes():
    with pytest.raises(ValueError):
        convert("13 AM to 12:50 PM")
        convert("12:45 PM to 5:65 AM")
