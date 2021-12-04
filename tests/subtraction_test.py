""" testing subtraction """

import os
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


def test_subtraction():
    """ testing result"""
    value_a = CsvListMaker.csv_list_for_subtraction()[0]
    value_b = CsvListMaker.csv_list_for_subtraction()[1]
    result_difference = CsvListMaker.csv_list_for_subtraction()[2]

    num_1 = value_a[3]
    num_2 = value_b[3]

    sub_result = Calculator.subtract_numbers(num_1, num_2)

    print(result_difference[3])
    print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
    logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

    source = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2\\input_folder\\Subtraction.csv"

    destination = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2\\done_folder\\Subtraction.csv"

    try:
        if os.path.exists(destination):
            print("There is a file there already.")
        else:
            os.replace(source, destination)
            print(source + " was moved.")
    except FileNotFoundError:
        print(source + " was not found.")
