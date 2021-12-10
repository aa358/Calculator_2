"""Testing division"""
from calc.operations.division import Division
# pylint: disable=too-few-public-methods


def test_division():
    """testing 3 divided by 2"""
    nums = (6, 2)
    division = Division(nums)
    assert division.get_result() == 3


def test_divide_by_zero():
    """testing 3 divided by 2"""
    nums = (6, 0)
    division = Division(nums)
    assert division.get_result() == ZeroDivisionError
