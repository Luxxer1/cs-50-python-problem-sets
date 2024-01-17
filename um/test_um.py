from um import count

def test_between_word():
    assert count("yummy") == 0

def test_case():
    assert count("Um") == 1

def test_punctuation():
    assert count("Hey, um...") == 1
