from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_str: str) -> str:
    """Функция маскировки данных пользователя"""
    word = ""
    digits = ""
    result = ""
    if (user_str) == "":
        return ""
    for el in user_str:
        if el.isalpha() or el == " ":
            word += el
        if el.isdigit():
            digits += el
        else:
            continue
    if word != "Счет ":
        result = get_mask_card_number(int(digits))
    else:
        result = get_mask_account(int(digits))
    return f"{word}{result}"


def get_date(user_date: str) -> str:
    """Функция обработки времени"""
    if (user_date) == "":
        return ""
    result = user_date.replace("-", "")
    return f"{result[6:8]}.{result[4:6]}.{result[0:4]}"
