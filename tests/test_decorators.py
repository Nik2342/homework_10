from typing import Any

from src.decorators import log


def test_1() -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(2, 5)
    assert result == 7


def test_2(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(2, 2)

    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
