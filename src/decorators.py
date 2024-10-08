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
                    result = func(*args, **kwargs)
                except Exception as e:
                    with open("log.txt", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
                    raise e
                else:
                    with open("log.txt", "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                    return result
            else:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Input: {args} {kwargs}")
                    raise e
                else:
                    print(f"{func.__name__} ok")
                    return result

        return inner

    return wrapper


@log(filename="log.txt")
def my_function_2(x: int, y: int) -> int:
    return x + y


my_function_2(2, 2)
