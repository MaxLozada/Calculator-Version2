"""CsvCaller"""

from csv_tester.csv_reading import CsvFileReader


class CsvFileCaller:
    """ this preps csv files to be used in csvReader"""

    @staticmethod
    def csv_caller_addition():
        """ without pandas """
        add_csv = 'Addition.csv'
        csv_file = CsvFileReader('C:\\Users\\MAXLO\\PycharmProjects\\'
                                 'Calculator_Version2\\input_folder\\' + add_csv)
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_subtraction():
        """ without pandas """
        sub_csv = 'Subtraction.csv'
        csv_file = CsvFileReader('C:\\Users\\MAXLO\\PycharmProjects\\'
                                 'Calculator_Version2\\input_folder\\' + sub_csv)
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_multiplication():
        """ without pandas """
        mul_csv = 'Multiplication.csv'
        csv_file = CsvFileReader('C:\\Users\\MAXLO\\PycharmProjects\\'
                                 'Calculator_Version2\\input_folder\\' + mul_csv)
        read_content = csv_file.key_value_maker()
        return read_content

    @staticmethod
    def csv_caller_division():
        """ without pandas """
        div_csv = 'Division.csv'
        csv_file = CsvFileReader('C:\\Users\\MAXLO\\PycharmProjects\\'
                                 'Calculator_Version2\\input_folder\\' + div_csv)
        read_content = csv_file.key_value_maker()
        return read_content
