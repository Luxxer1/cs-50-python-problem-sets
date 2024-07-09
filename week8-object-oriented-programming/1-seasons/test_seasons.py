from seasons import calc_date
import pytest

def test_str_date():
    with pytest.raises(SystemExit):
        assert calc_date("January 1, 1999") == SystemExit
        assert calc_date("23/12/1995") == SystemExit

def test_normal_date():
    # Only works if you chance calc_date value to 1 year before
    # Program don't handle bissext year, so, if you're in a bissext year
    # You should pass the date from '1 year before + 1 day'
    assert calc_date("2023-07-10") == "Five hundred twenty-five thousand, six hundred minutes"
