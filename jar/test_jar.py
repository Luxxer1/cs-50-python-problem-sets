from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    with pytest.raises(ValueError):
        assert jar.deposit(7) == ValueError


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        assert jar.withdraw(8) == ValueError
