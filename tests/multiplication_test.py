""" testing multiplication """

from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker


def test_multiplication():
    """ testing result"""
    value_a = CsvListMaker.csv_list_for_multiplication()[0]
    value_b = CsvListMaker.csv_list_for_multiplication()[1]
    result_product = CsvListMaker.csv_list_for_multiplication()[2]

    assert Calculator.multiply_numbers(value_a[0], value_b[0]) == result_product[0]
