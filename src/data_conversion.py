import csv

import pandas as pd


def csv_data_conversion(path):
    """Функция считывания csv-файлов"""
    csv_list = []
    try:
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                csv_list.append(row)
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as ex:
        print(ex)
    finally:
        return csv_list


def xlsx_data_conversion(path):
    """Функция считывания xlsx-файлов"""
    xlsx_list = []
    try:
        data = pd.read_excel(path)
        xlsx_list = data.to_dict(orient="records")
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as ex:
        print(ex)
    finally:
        return xlsx_list
