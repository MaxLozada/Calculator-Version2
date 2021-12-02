""" This is the increment function"""
from calc.operations.addition import Addition
from calc.operations.division import Division
from calc.operations.multiplication import Multiplication
from calc.operations.subtraction import Subtraction


class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        """ Add calculation to history """
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        addition = Addition(args)
        Calculator.add_calculation_to_history(addition)
        result = addition.get_result()
        return result

    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        subtraction = Subtraction(args)
        Calculator.add_calculation_to_history(subtraction)
        result = subtraction.get_result()
        return result

    @staticmethod
    def multiply_numbers(*args):
        """ multiply list of numbers from result"""
        multiplication = Multiplication(args)
        Calculator.add_calculation_to_history(multiplication)
        result = multiplication.get_result()
        return result

    @staticmethod
    def divide_numbers(*args):
        """divide list of numbers from result"""
        division = Division(args)
        Calculator.add_calculation_to_history(division)
        result = division.get_result()
        return result

    @staticmethod
    def clear_history():
        """ Clear the calculation history"""
        Calculator.history.clear()
        return True

    @staticmethod
    def length_history():
        """ length of calculations in history"""
        return len(Calculator.history)

    @staticmethod
    def remove_history(num):
        """ remove a certain history"""
        Calculator.history.pop(num)
        return True

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]

    @staticmethod
    def get_calculation_last():
        """ get last calculation from history"""
        if len(Calculator.history) > 0:
            return Calculator.history[-1].get_result()
        return "Zero History Currently"
