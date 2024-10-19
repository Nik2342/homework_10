import os
from unittest.mock import patch

from src.external_api import currency_conversion

API_KEY = os.getenv("API_KEY")


@patch("src.external_api.requests.request")
def test_currency_conversion(mock_currency) -> None:
    mock_currency.return_value.json.return_value = 2000.0
    assert currency_conversion("USD", "RUB", 20)
