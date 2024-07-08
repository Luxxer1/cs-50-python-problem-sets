from numb3rs import validate


def test_string():
    assert validate("cat") == False


def test_greater_than_255():
    assert validate("512.512.512.512") == False
    assert validate("255.512.512.512") == False
    assert validate("255.255.512.512") == False
    assert validate("255.255.255.512") == False


def test_intenger():
    assert validate("255.255.255.255") == True
