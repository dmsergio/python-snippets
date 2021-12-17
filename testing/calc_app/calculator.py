# calculator.py

from functools import reduce
import operator


class Calculator:
    """Calculator with four simple operations"""

    @staticmethod
    def add(*args):
        """Return the addition between x and y.

        >>> Calculator.add(2, 5)
        7

        >>> Calculator.add(-1, 2)
        1

        >>> Calculator.add(0, 0)
        0
        """
        return sum(args)

    @staticmethod
    def subtract(*args):
        """Return the subtract between x and y.

        >>> Calculator.subtract(1, -5)
        6

        >>> Calculator.subtract(10, 8)
        2

        >>> Calculator.subtract(5, 5)
        0
        """
        return reduce(operator.__sub__, args)

    @staticmethod
    def multiply(*args):
        """Return the multiply between x and y.

        >>> Calculator.multiply(5, 5)
        25

        >>> Calculator.multiply(2, -10)
        -20

        >>> Calculator.multiply(10, 0)
        0
        """
        return reduce(operator.__mul__, args)

    @staticmethod
    def divide(*args):
        """Return the division between x and y.

        >>> Calculator.divide(10, 2)
        5

        >>> Calculator.divide(2, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero

        >>> Calculator.divide(10, 10)
        1
        """
        return reduce(operator.__floordiv__, args)


if __name__ == "__main__":
    import doctest
    # doctest.testmod(verbose=True)
    # doctest.testfile("./docstring_test.txt")
    doctest.testmod()
