def get_mask_card_number(card_number: int) -> str:
    """ "Функция маскировки номера банковской карты"""
    new_card_number = str(card_number)
    return f"{new_card_number[0:4]} {new_card_number[4:6]}** **** {new_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """ "Функция маскировки номера банковского счета"""
    new_account_number = str(account_number)
    return f"**{new_account_number[-4:]}"
