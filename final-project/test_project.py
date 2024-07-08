from project import (
    check_item_name,
    check_valid_float,
    get_unique_item_id,
    check_item_id,
)


def test_check_item_name():
    assert check_item_name("Book") == "book"
    assert check_item_name("Book-*/") == False


def test_check_valid_float():
    assert check_valid_float("175.98") == 175.98
    assert check_valid_float("1,299.99") == False


def test_get_unique_item_id():
    database1 = [{"id": 1}, {"id": 2}, {"id": 3}]
    database2 = None
    assert get_unique_item_id(database1) == 4
    assert get_unique_item_id(database2) == 1


def test_check_item_id():
    database = [{"id": 1}, {"id": 2}, {"id": 3}]
    assert check_item_id("2", database) == 2
    assert check_item_id("abc", database) is False
