"""Subtraction class"""
from abc import abstractmethod

from calc.operations.calculation import Calculation


# pylint: disable=too-few-public-methods, missing-function-docstring

class Math(Calculation):
    """Subtracting numbers"""
    @abstractmethod
    def get_result(self):
        pass


class Subtraction(Math):
    """Subtracting numbers"""

    def get_result(self):
        """get the subtraction results"""
        result = 0.0
        for value in self.values:
            result = result - value
        return result
