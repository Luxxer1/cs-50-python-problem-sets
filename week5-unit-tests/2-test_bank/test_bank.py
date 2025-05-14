from bank import value

def test_starts_with_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_starts_with_h():
    assert value("hi") == 20
    assert value("Hey you!") == 20

def test_starts_without_h():
    assert value("Can you help me?") == 100
    assert value("What's up?") == 100
