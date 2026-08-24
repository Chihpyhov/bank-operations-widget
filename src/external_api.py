import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции.
    :return: Сумма в рублях (float). Для RUB возвращает исходное значение.
             Для USD/EUR обращается к API и конвертирует по текущему курсу.
    """
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return amount

    if currency_code in ("USD", "EUR"):
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?"
            f"to=RUB&from={currency_code}&amount={amount}"
        )
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json().get("result")
            if result is not None:
                return float(result)
    return 0.0
