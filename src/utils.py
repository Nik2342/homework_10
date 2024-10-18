import json
from typing import Optional


def get_fin_operation(path: Optional[str] = None) -> list:
    """Функция возвращающая список операций"""
    fin_operation = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            fin_operation = json.load(file)
    except Exception as e:
        print("Cодержит не список или не найден")
    finally:
        return fin_operation


# print(get_fin_operation('C:\\Users\\NikitaS\\PycharmProjects\\Homework9_1\\data\\operations.json'))
