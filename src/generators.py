from typing import Iterator


def filter_by_currency(list_dict: list, currency: str):
    """Функция фильтрации операций по валюте"""
    for transaction in list_dict:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction
    for transaction in list_dict:
        if transaction.get("currency_code", {}) == currency:
            yield transaction


def transaction_descriptions(list_dict: list) -> Iterator:
    """Функция описания операции"""
    if list_dict != []:
        for el in list_dict:
            yield el.get("description")


def card_number_generator(first: int, last: int) -> Iterator:
    """Функция создания номера карты"""
    for el in range(first, last + 1):
        len_el = len(str(el))
        len_0 = 16 - len_el
        result = f"{'0'*len_0}{el}"
        yield f"{result[0:4]} {result[4:8]} {result[8:12]} {result[12:16]}"
