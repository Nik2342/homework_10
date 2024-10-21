import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)


def get_mask_card_number(card_number: int) -> str:
    """ "Функция маскировки номера банковской карты"""
    try:
        new_card_number = str(card_number)
        logger.info("Маскировка номера банковской карты")
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        print("Ошибка маскироки номера банковской карты")
    return f"{new_card_number[0:4]} {new_card_number[4:6]}** **** {new_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """ "Функция маскировки номера банковского счета"""
    try:
        new_account_number = str(account_number)
        logger.info("Маскировка номера банковского счета")
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        print("Ошибка маскироки номера банковского счета")
    return f"**{new_account_number[-4:]}"
