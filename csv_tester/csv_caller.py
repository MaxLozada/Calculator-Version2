"""CsvCaller"""

from csv_tester.csv_reading import CsvFileReader


class CsvFileCaller:
    """ this preps csv files to be used in csvReader"""

    @staticmethod
    def csv_caller_addition():
        """ without pandas """
        csv_file = CsvFileReader('C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2'
                               '\\input_folder\\Addition1' + '.csv')
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_subtraction():
        """ without pandas """
        csv_file = CsvFileReader(
            'C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2\\'
            'input_folder\\Subtraction.csv')
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_multiplication():
        """ without pandas """
        csv_file = CsvFileReader(
            'C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2\\'
            'input_folder\\Multiplication.csv')
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_division():
        """ without pandas """
        csv_file = CsvFileReader(
            'C:\\Users\\MAXLO\\PycharmProjects\\Calculator_Version2\\'
            'input_folder\\Division.csv')
        read_content = csv_file.key_value_maker()
        return read_content
