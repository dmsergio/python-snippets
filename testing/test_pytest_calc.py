# test_pytest_calc.py

import pytest

from calc_app.calculator import Calculator


class TestCalc:

    def test_add(self):
        assert Calculator.add(2, 2) == 4, "Should be 4"

    def test_subtract(self):
        assert Calculator.subtract(10, 8) == 2, "Should be 2"

    def test_multiply(self):
        assert Calculator.multiply(3, 5) == 15, "Should be 15"

    def test_divide(self):
        assert Calculator.divide(10, 5) == 2, "Should be 2"


@pytest.mark.parametrize("adding, expected_result", [
    ((1, 1), 2),
    ((10, -1), 9),
    ((45, 4), 49),
    ((99, 1), 100),
    ((-1, -1), -2),
    ((-20, 0), -20),
])
def test_add_parametrized(adding, expected_result):
    error_info = f"Should be {expected_result}"
    assert Calculator.add(*adding) == expected_result, error_info
