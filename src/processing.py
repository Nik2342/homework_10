def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """"Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ state соответствует указанному значению."""
    result = []
    for el in list_dict:
        if el.get("state") == state:
            result.append(el)
    return result

def sort_by_date(list_dict: list, is_reverse: bool = True) -> list:
    """"Функция сортировки списка словарей по дате"""
    result = sorted(list_dict, key= lambda x: x.get("date"), reverse = is_reverse)
    return result
