"""Calculation Class"""


class Calculation:
    """ Abstraction"""

    def __init__(self, values: tuple):
        """ constructor method"""
        self.values = Calculation.convert_args_to_tuple(values)

    @classmethod
    def create(cls, values: tuple):
        """ instantiate objects"""
        return cls(values)

    @staticmethod
    def convert_args_to_tuple(values):
        """ Turn values to a list of floats"""
        args_to_tuple = []
        for item in values:
            args_to_tuple.append(float(item))
        return tuple(args_to_tuple)
