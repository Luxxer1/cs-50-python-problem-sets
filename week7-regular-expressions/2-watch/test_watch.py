from watch import parse

def test_string_none():
    assert parse("http://youtube.com/embed/xvFZjo5PgG0") == None
    assert parse("https://www.youtube.com/embed/xvFZjo5PgG0") == None

def test_valid_link():
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"