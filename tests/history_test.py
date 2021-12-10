"""Testing the Calculator"""
import pytest
from calc.history.calculations import Calculations
from calc.operations.addition import Addition


# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test"""
    Calculations.clear_history()


@pytest.fixture
def setup_addition_fixture():
    """define a function that will run each time you pass it to a test"""
    nums = (2, 4)
    addition = Addition(nums)
    Calculations.add_calculation(addition)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_fixture):
    """Testing clear history returns true for success"""
    assert Calculations.count_history() == 1


def test_clear_calculation_history(clear_history_fixture, setup_addition_fixture):
    """testing clear history"""
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() is True


def test_get_calculation(clear_history_fixture, setup_addition_fixture):
    """Testing getting a specific calculation out of the history"""
    assert Calculations.get_calculation(0).get_result() == 6.0


def test_get_calc_last_result_value(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    assert Calculations.get_last_calculation_result_value() == 6.0


def test_get_calculation_first(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    assert Calculations.get_first_calculation().get_result() == 6.0


def test_history_count(clear_history_fixture, setup_addition_fixture):
    """Testing getting the count of calculations from the history"""
    assert Calculations.count_history() == 1


def test_get_calc_last_result_object(clear_history_fixture, setup_addition_fixture):
    """Testing getting the last calculation from the history"""
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Addition) is True
