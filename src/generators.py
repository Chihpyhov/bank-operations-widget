from typing import Dict, Any, Generator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> Generator[Dict[str, Any], None, None]:
    """
    Возвращает итератор транзакций с заданной валютой.
    """
    for t in transactions:
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield t


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Generator[str, None, None]:
    """
    Генерирует описания транзакций по очереди.
    """
    for t in transactions:
        yield t.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX от start до stop.
    """
    for num in range(start, stop + 1):
        raw = str(num).zfill(16)
        yield f"{raw[:4]} {raw[4:8]} {raw[8:12]} {raw[12:]}"