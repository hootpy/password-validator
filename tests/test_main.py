from src import validate_pw


def test_validate_password_have_less_than_8_characters():
    assert validate_pw("1234567") is False


def test_validate_password_have_no_uppercase():
    assert validate_pw("1234567a") is False


def test_validate_password_have_no_lowercase():
    assert validate_pw("1234567A") is False


def test_validate_password_have_no_digit():
    assert validate_pw("abcdefgA") is False


def test_validate_password_have_no_special_character():
    assert validate_pw("1234567Aa") is False
