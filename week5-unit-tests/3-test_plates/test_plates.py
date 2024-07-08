from plates import is_valid


def test_starts_alphabetical():
    assert is_valid("CS") == True
    assert is_valid("C5") == False

def test_numbers():
    assert is_valid("QWER12") == True
    assert is_valid("QW12ER") == False

def test_length():
    assert is_valid("CSQW") == True
    assert is_valid("QWERASDF") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_punctuation():
    assert is_valid("CS50!") == False
