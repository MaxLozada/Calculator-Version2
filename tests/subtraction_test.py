""" testing subtraction """

from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker


def test_subtraction():
    """ testing result"""
    value_a = CsvListMaker.csv_list_for_subtraction()[0]
    value_b = CsvListMaker.csv_list_for_subtraction()[1]
    result_difference = CsvListMaker.csv_list_for_subtraction()[2]

    assert Calculator.subtract_numbers(value_a[0], value_b[0]) == result_difference[0]
