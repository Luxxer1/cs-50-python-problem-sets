from seasons import calc_date
import pytest

def test_str_date():
    with pytest.raises(SystemExit):
        assert calc_date("January 1, 1999") == SystemExit
        assert calc_date("23/12/1995") == SystemExit

def test_normal_date():
    assert calc_date("2022-12-27") == "Five hundred twenty-five thousand, six hundred minutes"
