from twttr import shorten

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("ABACATE") == "BCT"

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("abacate") == "bct"

def test_number():
    assert shorten("1234") == "1234"
    assert shorten("19543278") == "19543278"

def test_punctuation():
    assert shorten(".;/*-") == ".;/*-"
