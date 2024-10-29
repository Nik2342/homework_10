import re
from collections import Counter


def get_bank_operations(dict_list: list, search_str: str) -> list:
    """Функция для фильтрации списка транзакций по строке поиска"""
    result = []
    pattern = re.compile(search_str, re.IGNORECASE)
    for el in dict_list:
        description = el.get("description")
        if pattern.search(description):
            result.append(el)
    return result


def operations_counter(dict_list: list, operation_list: list) -> dict:
    """Функция для подсчета операций подходящих по списку"""
    result = []
    temp = []
    for el in dict_list:
        description = el.get("description")
        if description in operation_list:
            temp.append(el)
    result = Counter(el.get("description") for el in temp)
    result = dict(result)
    return result
