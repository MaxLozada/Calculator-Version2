""" Multiplication class"""
from calc.operations.calculation import Calculation


class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """multiplication class"""

    def get_result(self):
        """results"""
        product_of_values = 1.0
        list_of_values = self.values[0]
        for value in list_of_values[0:]:
            product_of_values = product_of_values * float(value)
        return product_of_values
