""" testing addition """
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

def test_addition():
    """ 'testing result'"""
    value_a = CsvListMaker.csv_list_for_addition()[0]
    value_b = CsvListMaker.csv_list_for_addition()[1]
    result_sum = CsvListMaker.csv_list_for_addition()[2]

    num_1 = value_a[3]
    num_2 = value_b[3]

    add_result = Calculator.add_numbers(num_1, num_2)

    print(result_sum[3])
    print('Add: {} + {} = {}'.format(num_1, num_2, add_result))
    logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
