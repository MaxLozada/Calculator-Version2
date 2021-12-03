""" testing addition """
import logging
from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(record_number)s - %(asctime)s - %(filename)s - ')


def test_addition(): # pylint: disable=consider-using-f-string
    """ 'testing result'"""
    value_a = CsvListMaker.csv_list_for_addition()[0]
    value_b = CsvListMaker.csv_list_for_addition()[1]
    result_sum = CsvListMaker.csv_list_for_addition()[2]

    num_1 = value_a[0]
    num_2 = value_b[0]

    add_result = Calculator.add_numbers(num_1, num_2)

    print(add_result)
    print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))
