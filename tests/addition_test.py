""" testing addition """

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

def test_addition():
    """ 'testing result'"""
    value_a = CsvListMaker.csv_list_for_addition()[0]
    value_b = CsvListMaker.csv_list_for_addition()[1]
    result_sum = CsvListMaker.csv_list_for_addition()[2]

    for record_number in range(len(result_sum)):
        num_1 = value_a[record_number]
        num_2 = value_b[record_number]

        add_result = Calculator.add_numbers(num_1, num_2)

        logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

    source = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2" \
             "\\input_folder\\Addition.csv"

    destination = "C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2" \
                  "\\done_folder\\Addition.csv"

    try:
        if os.path.exists(destination):
            print("There is a file there already.")
        else:
            os.replace(source, destination)
            print(source + " was moved.")
    except FileNotFoundError:
        print(source + " was not found.")
