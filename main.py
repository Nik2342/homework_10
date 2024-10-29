from src.bank_operations_filter import get_bank_operations
from src.data_conversion import csv_data_conversion, xlsx_data_conversion
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_fin_operation
from src.widget import get_date, mask_account_card


def main():
    """Основная функция банковского приложения"""

    # Создание переменных
    result = None
    user_data = None
    user_sort_choice_direction = None
    user_search_word = None

    # Приветственные сообщения
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла\n")

    # Выбор файла пользователем
    while True:
        try:
            user_choice = int(input())
            if 1 <= user_choice <= 3:
                break
            else:
                print("Введенное число находится вне диапазона")
        except Exception:
            print("Введены некорректные данные")
    dict_for_user_choice = {1: "JSON-файл", 2: "CSV-файл", 3: "XLSX-файл"}
    if user_choice == 1:
        user_data = get_fin_operation("C:\\Users\\NikitaS\\PycharmProjects\\Homework9_1\\data\\operations.json")
    elif user_choice == 2:
        user_data = csv_data_conversion("C:\\Users\\NikitaS\\PycharmProjects\\Homework9_1\\data\\transactions.csv")
    elif user_choice == 3:
        user_data = xlsx_data_conversion(
            "C:\\Users\\NikitaS\\PycharmProjects\\Homework9_1\\data\\transactions_excel.xlsx"
        )
    print(f"Для обработки выбран {dict_for_user_choice[user_choice]}")

    # Выбор статуса операции пользователем
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    operation_status = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        try:
            user_status_choice = input()
            if user_status_choice.upper().strip() in operation_status:
                break
            else:
                print(f"Статус операции {user_status_choice} недоступен.")
        except Exception:
            print("Введены некорректные данные")
    print(f"Операции отфильтрованы по статусу {user_status_choice.upper()}")

    # Выбор параметров сортировки
    # Сортировка по дате
    print("Отсортировать операции по дате? Да/Нет")
    user_sort_choice = user_choice_convert()
    if user_sort_choice:
        print("Отсортировать по возрастанию или по убыванию? ")
        while True:
            try:
                user_sort_choice_direction = input()
                user_sort_choice_direction = user_sort_choice_direction.lower().strip()
                if user_sort_choice_direction == "по возрастанию":
                    user_sort_choice_direction = True
                    break
                elif user_sort_choice_direction == "по убыванию":
                    user_sort_choice_direction = False
                    break
                else:
                    print("Введены некорректные данные")
            except Exception:
                print("Введены некорректные данные")

    # Сортировка по валюте
    print("Выводить только рублевые тразакции? Да/Нет ")
    user_sort_choice_only_rub = user_choice_convert()

    # Сортировка по определенному слову в описании
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ")
    user_sort_choice_with_desc = user_choice_convert()
    if user_sort_choice_with_desc:
        user_search_word = input("Введите слово для фильтрации\n")
    result = user_data

    # Фильтрация списка по пользовательским условиям
    print("Распечатываю итоговый список транзакций...")
    result = filter_by_state(result, user_status_choice.upper().strip())
    if user_sort_choice:
        result = sort_by_date(user_data, user_sort_choice_direction)
    if user_sort_choice_only_rub:
        result = list(filter_by_currency(result, "RUB"))
    if user_sort_choice_with_desc:
        try:
            result = get_bank_operations(result, user_search_word)
        except Exception as ex:
            print(ex)
    if result == [] or result is None:
        print("Не найдено ни одной транзакции, подходящей под вашиусловия фильтрации")
        exit()
    else:
        print(f"Всего банковских операций в выборке: {len(result)}")

    # Вывод итоговой информации
    for el in result:
        if el == {}:
            continue
        print(f"{get_date(el.get("date"))} {el.get("description")}")
        if el.get("description") == "Открытие вклада":
            print(f"{mask_account_card(el.get("to"))}")
        else:
            print(f"{mask_account_card(el.get("from"))} -> {mask_account_card(el.get("to"))}")
        if user_choice == 1:
            print(
                f"Сумма {el.get("operationAmount").get("amount")}"
                f" {el.get("operationAmount").get("currency").get("code")}"
            )
        else:
            print(f"Сумма {el.get("amount")} {el.get("currency_code")}")


def user_choice_convert() -> bool:
    """Функция возвращающая результат ввода пользователя"""
    while True:
        try:
            user_str = input()
            if user_str.lower().strip() == "да":
                result = True
                break
            if user_str.lower().strip() == "нет":
                result = False
                break
            else:
                print("Введены некорректные данные")
        except Exception:
            print("Введены некорректные данные")
    return result
