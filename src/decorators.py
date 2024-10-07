from functools import wraps
from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, для логирования функции"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                time_1 = time()
                func(*args, **kwargs)
                time_2 = time()
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
            else:
                if filename is None:
                    print(f"{func.__name__} ok. Начало работы:{time_1}. Конец работы:{time_2}.")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok. Начало работы:{time_1}. Конец работы:{time_2}.")

        return inner

    return wrapper


@log()
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
