"""Testing multiplication"""
from calc.operations.multiplication import Multiplication


# pylint: disable=too-few-public-methods


def test_multiply():
    """testing 3 multiplied by 2"""
    nums = (3.0, 2.0)
    multiply = Multiplication(nums)
    assert multiply.get_result() == 6.0


def test_multiply_incorrect():
    """testing 3 multiplied by 2"""
    nums = (3.0, 3.0)
    multiply = Multiplication(nums)
    assert multiply.get_result() != 6.0
