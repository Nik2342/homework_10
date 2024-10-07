from typing import Any

from src.decorators import log, my_function


@log()
def test_log_1() -> None:
    result = my_function(2, 2)
    assert result == 4


@log()
def test_log_2(capsys: Any) -> None:
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "Начало работы функции\n" "Конец работы функции\n" "my_function ok\n"


@log()
def test_log_3(capsys: Any) -> None:
    my_function(2)
    captured = capsys.readouterr()
    assert (
        captured.out == "Начало работы функции\n"
        "my_function error: my_function() missing 1 required positional argument: "
        "'y'. Input: (2,) {}\n"
    )


@log()
def test_exception() -> None:
    try:
        my_function(0)
    except Exception as e:
        assert e
