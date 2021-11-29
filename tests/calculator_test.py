"""Testing the Calculator"""

import pytest

from calc.calculator import Calculator

@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""

    Calculator.clear_history()
    return True

def test_calculator_add(clear_history_fixture):
    """testing for addition method for calc"""
    assert Calculator.add_numbers(1.0, 2.0) == 3.0
    assert Calculator.add_numbers(1.0, 2.0, 3.0) == 6.0

def test_calculator_subtract(clear_history_fixture):
    """Testing the subtract method of the calc"""
    assert Calculator.subtract_numbers(1.0, 2.0) == -1.0

def test_calculator_multiply(clear_history_fixture):
    """Testing the multiply method of the calc"""
    assert Calculator.multiply_numbers(1.0, 2.0) == 2.0

def test_calculator_division(clear_history_fixture):
    """Testing the division method of the calc"""
    assert Calculator.divide_numbers(4.0, 2.0) == 2.0
    assert Calculator.divide_numbers(0.0, 4.0) == 0.0
    assert Calculator.divide_numbers(4.0, 0.0) == "No Zero allowed in the Denominator!"

def test_clear_history(clear_history_fixture):
    """Testing clear history """

    Calculator.add_numbers(1.0,1.0)
    Calculator.clear_history()
    assert Calculator.clear_history() == "No history"
    assert Calculator.history == []

def test_remove_1st_calculation_in_history(clear_history_fixture):
    """Testing to remove first 1st calculation and make it an object"""

    Calculator.add_numbers(*(1, 2))
    Calculator.multiply_numbers(3, 3)
    first = Calculator.history[:]
    first.pop(0)
    Calculator.remove_history(0)
    assert Calculator.history == first

def test_remove_2nd_calculations_in_history(clear_history_fixture):
    """Testing to remove first 2nd calculation and make it an object"""

    Calculator.add_numbers(*(1, 5))
    Calculator.multiply_numbers(3, 4)
    second = Calculator.history[:]
    second.pop(1)
    Calculator.remove_history(1)
    assert Calculator.history == second

def test_length_of_history(clear_history_fixture):
    """Testing the length of the history"""

    Calculator.add_numbers(*(2, 2))
    Calculator.multiply_numbers(2, 4)
    assert Calculator.length_history() == 2

def test_get_calculation(clear_history_fixture):
    """Testing getting a specific calculation out of the history"""

    Calculator.multiply_numbers(1.0,2.0)
    Calculator.subtract_numbers(3, 3, 3)
    assert Calculator.get_calculation(0).get_result() == 2.0
    assert Calculator.get_calculation(1).get_result() == -3.0

def test_get_calculation_last(clear_history_fixture):
    """Testing getting the last calculation from the history"""

    Calculator.add_numbers(2, 4, 8)
    Calculator.add_numbers(4, 4, 4)
    assert Calculator.get_calculation_last() == 12.0

def test_length():

    list = ['a', 'b', 'c', 'd', 'e']

    result = len(list)

    assert result == 5