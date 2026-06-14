from typing import Any


def filter_by_state(transactions: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """
    Фильтрует список банковских операций по значению ключа 'state'.
    """
    return [txn for txn in transactions if txn.get("state") == state]


def sort_by_date(transactions: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """
    Сортирует список операций по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)