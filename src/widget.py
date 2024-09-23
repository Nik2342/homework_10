from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_str: str) -> str:
    word = ""
    digits = ""
    result = ""
    for el in user_str:
        if el.isalpha():
            word += el
        if el.isdigit():
            digits += el
        else:
            continue
    if word != "Счет":
        result = get_mask_card_number(int(digits))
    else:
        result = get_mask_account(int(digits))
    return f"{word} {result}"
