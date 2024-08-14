# OOP
from typing import NoReturn, Union


def never_returns():
    print("I am about to an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


def handler() -> None:
    try:
        never_returns()
        print("Never executed")
    except Exception as e:
        print(f"I caught an exception: {e!r}")
    print("Executed after the exception")


def funny_division(divisor: float) -> Union[str, float]:
    try:
        return 100/divisor
    except ZeroDivisionError:
        return "Zero is not a good idea!"


def funnier_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 10 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


def funiest_division(divisor: int) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / divisor
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise


def divide_with_exception(dividend: int, divisor: int) -> None:
    try:
        print(f'{dividend / divisor=}')
    except ZeroDivisionError:
        print("You can't divide by zero")


def divide_with_if(dividend: int, divisor: int)-> None:
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print(f"{dividend / divisor=}")


if __name__ == '__main__':
    pass






































