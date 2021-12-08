""" testing multiplication """

import os
import logging
from calc.calculator import Calculator
from csv_tester.key_n_value_utilization import CsvListMaker

# Remove all handlers associated with the root logger object.
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2'
                    '\\results_folder\\csv_log_tests.log', level=logging.DEBUG,
                    format='%(created)f, %(filename)s, %(message)s')


# pylint: disable=consider-using-f-string
# pylint: disable=logging-format-interpolation


def test_multiplication():
    """ testing result"""
    value_a = CsvListMaker.csv_list_for_multiplication()[0]
    value_b = CsvListMaker.csv_list_for_multiplication()[1]
    result_product = CsvListMaker.csv_list_for_multiplication()[2]

    for record_number in range(len(result_product)):
        num_1 = value_a[record_number]
        num_2 = value_b[record_number]

        mul_result = Calculator.multiply_numbers(num_1, num_2)

        logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

    source = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2" \
             "\\input_folder\\Multiplication.csv"

    destination = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2" \
                  "\\done_folder\\Multiplication.csv"

    try:
        if os.path.exists(destination):
            print("There is a file there already.")
        else:
            os.replace(source, destination)
            print(source + " was moved.")
    except FileNotFoundError:
        print(source + " was not found.")
