""" division class"""
from calc.operations.calculation import Calculation

class Division(Calculation): # pylint: disable=too-few-public-methods
    """ division class"""

    def get_result(self):
        """ result """
        list_of_values = self.values[0]
        quotient_of_value = list_of_values[0]
        for value in list_of_values[1:]:
            try:
                quotient_of_value = quotient_of_value / float(value)
            except ZeroDivisionError as e:
                print(e)
                return "No Zero allowed in the Denominator!"
            return quotient_of_value

