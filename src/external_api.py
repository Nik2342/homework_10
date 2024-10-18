import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
headers = {"apikey": API_KEY}


def get_transaction_amount(transaction_list: list, transaction_id: int) -> float:
    amount = 0.0
    for transaction in transaction_list:
        if transaction.get("id") == transaction_id:
            currency = transaction.get("operationAmount").get("currency").get("code")
            amount = transaction.get("operationAmount").get("amount")
            if currency != "RUB":
                amount = currency_conversion(currency, "RUB", amount)
    return amount


def currency_conversion(cur_from: str, cur_to: str, amount: int) -> float:
    try:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={cur_to}&from={cur_from}&amount={amount}"
        response = requests.request("GET", url, headers=headers)
        return response.json()["result"]
    except Exception as e:
        print("Ошибка конвертации валюты")
        raise e