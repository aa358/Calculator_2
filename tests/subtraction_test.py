"""Testing subtraction"""
from calc.operations.subtraction import Subtraction
# pylint: disable=too-few-public-methods


def test_subtraction():
    """testing calc result -1"""
    nums = (2.0, 3.0)
    subtract = Subtraction(nums)
    assert subtract.get_result() == -5.0
