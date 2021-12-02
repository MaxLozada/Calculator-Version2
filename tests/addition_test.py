""" testing addition """

from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker


def test_addition():
    """ 'testing result'"""
    value_a = CsvListMaker.csv_list_for_addition()[0]
    value_b = CsvListMaker.csv_list_for_addition()[1]
    result_sum = CsvListMaker.csv_list_for_addition()[2]

    assert Calculator.add_numbers(value_a[0], value_b[0]) == result_sum[0]
    assert Calculator.add_numbers(value_a[-1], value_b[-1]) == result_sum[-1]
