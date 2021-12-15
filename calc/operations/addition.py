"""Addition class"""
from calc.operations.calculation import Calculation


class Addition(Calculation):
    """Adding numbers"""

    def get_result(self):
        """Do the addition"""
        result = 0.0
        for value in self.values:
            result += value
        return result
