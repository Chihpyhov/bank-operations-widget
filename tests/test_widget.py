import pytest
from src.widget import mask_account_card, get_date


@pytest.fixture
def card_examples():
    return [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ]


@pytest.fixture
def account_examples():
    return [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ]


def test_mask_account_card_card(card_examples):
    for inp, expected in card_examples:
        assert mask_account_card(inp) == expected


def test_mask_account_card_account(account_examples):
    for inp, expected in account_examples:
        assert mask_account_card(inp) == expected


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("")
    with pytest.raises(ValueError):
        mask_account_card("Visa")
    with pytest.raises(ValueError):
        mask_account_card("Счет")
    with pytest.raises(ValueError):
        mask_account_card("Visa Gold 1234")


@pytest.fixture
def date_examples():
    return [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-01T00:00:00", "01.01.2023"),
    ]


def test_get_date_valid(date_examples):
    for inp, expected in date_examples:
        assert get_date(inp) == expected


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("not a date")
    with pytest.raises(ValueError):
        get_date("")
