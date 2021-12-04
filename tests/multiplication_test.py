""" testing multiplication """

import logging
from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker

# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='../results_folder/csv_log_tests.log', level=logging.DEBUG,
                    format='%(created)f, %(filename)s, %(message)s')


# pylint: disable=consider-using-f-string
# pylint: disable=logging-format-interpolation


def test_multiplication():
    """ testing result"""
    value_a = CsvListMaker.csv_list_for_multiplication()[0]
    value_b = CsvListMaker.csv_list_for_multiplication()[1]
    result_product = CsvListMaker.csv_list_for_multiplication()[2]

    num_1 = value_a[4]
    num_2 = value_b[4]

    mul_result = Calculator.multiply_numbers(num_1, num_2)

    print(result_product[4])
    print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
    logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
