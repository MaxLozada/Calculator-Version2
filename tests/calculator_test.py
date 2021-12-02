"""Testing the Calculator"""

import pytest

from calc.calculator import Calculator


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()
    return True


def test_calculator_add(clear_history_fixture):
    """testing for addition method for calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(1.0, 2.0) == 3.0


def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtract_numbers(1.0, 2.0) == -1.0


def test_calculator_multiply(clear_history_fixture):
    """Testing the multiply method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiply_numbers(1.0, 2.0) == 2.0


def test_calculator_division(clear_history_fixture):
    """Testing the division method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.divide_numbers(4, 2) == 2.0
    assert Calculator.divide_numbers(4, 0) == "No Zero allowed in the Denominator!"


def test_clear_history(clear_history_fixture):
    """Testing clear history """
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.add_numbers(1.0, 2.0)
    Calculator.clear_history()
    assert Calculator.history == []


def test_remove_1st_calculation_history(clear_history_fixture):
    """Testing to remove first 1st calculation and make it an object"""
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.add_numbers(*(1, 2))
    Calculator.multiply_numbers(3, 3)
    first = Calculator.history[:]
    first.pop(0)
    print(first)
    Calculator.remove_history(0)
    print(Calculator.history)
    assert Calculator.history == first


def test_remove_2nd_calculations_history(clear_history_fixture):
    """Testing to remove first 2nd calculation and make it an object"""
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.add_numbers(*(1, 5))
    Calculator.multiply_numbers(3, 4)
    second = Calculator.history[:]
    second.pop(1)
    print(second)
    Calculator.remove_history(1)
    print(Calculator.history)
    assert Calculator.history == second


def test_length_of_history(clear_history_fixture):
    """Testing the length of the history"""
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.add_numbers(*(2, 2))
    Calculator.add_numbers(3, 3)
    Calculator.multiply_numbers(2, 4)
    Calculator.multiply_numbers(4, 3)
    assert Calculator.length_history() == 4


def test_get_calculation(clear_history_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.multiply_numbers(1.0, 2.0)
    Calculator.add_numbers(3, 3, 3)
    Calculator.subtract_numbers(3, 3, 3)
    assert Calculator.get_calculation(0).get_result() == 2.0
    assert Calculator.get_calculation(1).get_result() == 9.0
    assert Calculator.get_calculation(2).get_result() == -3.0


def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name

    Calculator.add_numbers(2, 4, 8)
    Calculator.add_numbers(3, 3, 3)
    assert Calculator.get_calculation_last() == 9
    Calculator.clear_history()
    assert Calculator.get_calculation_last() == "Zero History Currently"
