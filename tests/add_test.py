"""Testing addition"""
from calc.operations.addition import Addition


# pylint: disable=too-few-public-methods

def test_addition():
    """testing calc result"""
    nums = (3.0, 2.0)
    addition = Addition(nums)
    assert addition.get_result() == 5.0
