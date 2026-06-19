import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [41428829, 939719570]),
        ("CANCELED", [594226727, 615064591]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(transactions, state, expected_ids):
    result = filter_by_state(transactions, state)
    assert [txn["id"] for txn in result] == expected_ids


def test_filter_by_state_default(transactions):
    result = filter_by_state(transactions)
    assert all(txn["state"] == "EXECUTED" for txn in result)


def test_sort_by_date_descending(transactions):
    result = sort_by_date(transactions)
    dates = [txn["date"] for txn in result]
    assert dates == [
        "2019-07-03T18:35:29.512364",
        "2018-10-14T08:21:33.419441",
        "2018-09-12T21:27:25.241689",
        "2018-06-30T02:08:58.425572",
    ]


def test_sort_by_date_ascending(transactions):
    result = sort_by_date(transactions, reverse=False)
    dates = [txn["date"] for txn in result]
    assert dates == [
        "2018-06-30T02:08:58.425572",
        "2018-09-12T21:27:25.241689",
        "2018-10-14T08:21:33.419441",
        "2019-07-03T18:35:29.512364",
    ]


def test_sort_by_date_equal_dates():
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    result = sort_by_date(data)
    assert len(result) == 2