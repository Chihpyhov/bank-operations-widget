import pytest
from src.widget import mask_account_card, get_date


def test_mask_account_card_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account_card_account():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"


def test_mask_account_card_invalid():
    with pytest.raises(ValueError):
        mask_account_card("")
    with pytest.raises(ValueError):
        mask_account_card("Visa")
    with pytest.raises(ValueError):
        mask_account_card("Счет")
    with pytest.raises(ValueError):
        mask_account_card("Visa Gold 1234")  # мало цифр


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-01-01T00:00:00") == "01.01.2023"


def test_get_date_invalid():
    with pytest.raises(ValueError):
        get_date("не дата")

