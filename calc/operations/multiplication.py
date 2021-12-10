"""Multiplication class"""
from calc.operations.calculation import Calculation


# pylint: disable=too-few-public-methods


class Multiplication(Calculation):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
            print(result)
        return result
