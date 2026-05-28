import re
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Принимает строку с типом и номером карты или счета.
    Возвращает строку с замаскированным номером.

    Пример:
        "Visa Platinum 7000792289606361" -> "Visa Platinum 7000 79** **** 6361"
        "Счет 73654108430135874305"      -> "Счет **4305"
    """
    if not info or not info.strip():
        raise ValueError("Пустая строка недопустима")

    parts = info.strip().split()
    if len(parts) < 2:
        raise ValueError("Неверный формат: ожидаются тип и номер через пробел")

    name = " ".join(parts[:-1])  # всё, кроме последнего слова — название
    number = parts[-1]          # последнее слово — номер

    # Определяем, счёт или карта
    if name.lower().startswith("счет"):
        # Проверка номера счета: минимум 4 цифры
        if not re.fullmatch(r"\d{4,}", number):
            raise ValueError("Номер счета должен содержать минимум 4 цифры")
        masked_number = get_mask_account(number)
        return f"{name} {masked_number}"
    else:
        # Считаем, что это карта
        if not re.fullmatch(r"\d{16}", number):
            raise ValueError("Номер карты должен содержать ровно 16 цифр")
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"


def get_date(iso_string: str) -> str:
    """
    Преобразует дату из ISO-формата в формат ДД.ММ.ГГГГ.

    Пример:
        "2024-03-11T02:26:18.671407" -> "11.03.2024"
    """
    try:
        # Отрезаем микросекунды, чтобы корректно парсить
        dt_part = iso_string.split(".")[0]
        dt = datetime.fromisoformat(dt_part)
        return dt.strftime("%d.%m.%Y")
    except Exception as e:
        raise ValueError(f"Некорректный формат даты: {iso_string}") from e