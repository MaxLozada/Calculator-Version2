""" testing division """

from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker

def test_division():
    value_a = CsvListMaker.csv_list_for_division()[0]
    value_b = CsvListMaker.csv_list_for_division()[1]
    result_quotient = CsvListMaker.csv_list_for_division()[2]
    """ testing result"""
    assert Calculator.divide_numbers(value_a[2], value_b[2]) == result_quotient[2]
    assert Calculator.divide_numbers(value_a[9], value_b[9]) == 'No Zero allowed in the Denominator!'
