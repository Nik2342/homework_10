from unittest.mock import mock_open, patch

from src.data_conversion import csv_data_conversion, xlsx_data_conversion


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_csv_empty_file(mock_file) -> None:

    data = csv_data_conversion("data/transactions.csv")

    assert data == []


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 3598919}')
def test_csv_not_a_list(mock_file):

    data = csv_data_conversion("data/transactions.csv")

    assert data == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_csv_file_not_found(mock_file) -> None:

    data = csv_data_conversion("data/transactions.csv")

    assert data == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_xlsx_empty_file(mock_file) -> None:

    data = xlsx_data_conversion("data/transactions_excel.xlsx")

    assert data == []


@patch("builtins.open", new_callable=mock_open, read_data='{"amount": 3598919}')
def test_xlsx_not_a_list(mock_file):

    data = xlsx_data_conversion("data/transactions_excel.xlsx")

    assert data == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_xlsx_file_not_found(mock_file) -> None:

    data = xlsx_data_conversion("data/transactions_excel.xlsx")

    assert data == []
