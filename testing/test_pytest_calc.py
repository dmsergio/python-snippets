# test_pytest_calc.py
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
