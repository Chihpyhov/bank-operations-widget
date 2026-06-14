from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по значению ключа 'state'.
    """
    return [txn for txn in transactions if txn.get("state") == state]


def sort_by_date(transactions: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=reverse)
