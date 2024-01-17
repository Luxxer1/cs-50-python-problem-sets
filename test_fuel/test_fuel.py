from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0") == ZeroDivisionError

def test_intenger():
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        assert convert("1.5/2") == ValueError

def test_string():
    with pytest.raises(ValueError):
        assert convert("three/four") == ValueError

def test_fullgauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_emptygauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"





