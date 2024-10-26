import json
import logging
import os
from typing import Optional

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
logger.addHandler(file_handler)
file_formatter = logging.Formatter("%(asctime)s %(levelname)s : %(message)s")
file_handler.setFormatter(file_formatter)


def get_fin_operation(path: Optional[str] = None) -> list:
    """Функция возвращающая список операций"""
    fin_operation = []
    try:
        logger.info("Открываем необходимый файл")
        with open(path, "r", encoding="utf-8") as file:
            logger.info("Считывание JSON строки и преобразование в Python объект")
            fin_operation = json.load(file)
            if type(fin_operation) is not list:
                logger.info("В файле содержится не список")
                fin_operation = []

    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка {ex}")
        print("Файл не найден")
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка {ex}")
        print("Ошибка декодирования файла")
    except Exception as ex:
        logger.error(f"Произошла ошибка {ex}")
        print("Cодержит не список или не найден")
    finally:
        return fin_operation


print(get_fin_operation("C:\\Users\\NikitaS\\PycharmProjects\\Homework9_1\\data\\operations.json"))
