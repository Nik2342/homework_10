from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, для логирования функции"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            result = None
            if filename is not None:
                try:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write("Начало работы функции")
                    result = func(*args, **kwargs)
                    file.write("Конец работы функции")
                except Exception as e:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
                else:
                    file.write(f"{func.__name__} ok")
                finally:
                    return result
            else:
                try:
                    print("Начало работы функции")
                    result = func(*args, **kwargs)
                    print("Конец работы функции")
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
                else:
                    print(f"{func.__name__} ok")
                finally:
                    return result

        return inner

    return wrapper


@log(filename="log.txt")
def my_function(x: int, y: int) -> int:
    return x + y
