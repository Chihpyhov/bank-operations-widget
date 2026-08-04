import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {"currency": {"code": "USD"}}
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {"currency": {"code": "RUB"}}
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {"currency": {"code": "USD"}}
        },
    ]


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in result)


def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(sample_transactions):
    descs = list(transaction_descriptions(sample_transactions))
    assert descs == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_missing_key():
    assert list(transaction_descriptions([{"id": 1}])) == [""]


@pytest.mark.parametrize(
    "start, stop, first, last",
    [
        (1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001"),
        (100, 101, "0000 0000 0000 0100", "0000 0000 0000 0101"),
    ],
)
def test_card_number_generator(start, stop, first, last):
    cards = list(card_number_generator(start, stop))
    assert cards[0] == first
    assert cards[-1] == last
    assert len(cards) == stop - start + 1
    for c in cards:
        assert len(c) == 19