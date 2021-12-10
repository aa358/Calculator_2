"""Division class"""
from calc.operations.calculation import Calculation


# pylint: disable=too-few-public-methods
# pylint: disable=unused-variable

class Division(Calculation):
    """Dividing numbers"""

    def get_result(self):
        """Do the division if not dividing by zero"""
        result = 1
        rev = self.values[::-1]

        for value in rev:
            try:
                result = value / result
                if result == 0:
                    raise ZeroDivisionError
            except ZeroDivisionError as error:
                return ZeroDivisionError
        return result
