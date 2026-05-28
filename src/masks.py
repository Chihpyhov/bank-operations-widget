def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Возвращает строку в формате "XXXX XX** **** XXXX".
    Пример: "1234567890123456" -> "1234 56** **** 3456"
    """
    clean_number = card_number.replace(" ", "")
    if len(clean_number) != 16 or not clean_number.isdigit():
        raise ValueError("Номер карты должен содержать ровно 16 цифр")
    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.
    Показывает только последние 4 цифры, добавляя перед ними "**".
    Пример: "12345678901234567890" -> "**7890"
    """
    clean_number = account_number.replace(" ", "")
    if len(clean_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{clean_number[-4:]}"
