from csv_tester.csvCaller import CsvFileCaller


class CsvListMaker:

    @staticmethod
    def csv_list_for_addition():
        csv_list = CsvFileCaller.csv_caller_addition()
        first_value_sum = []
        second_value_sum = []
        result_value_sum = []
        for key in csv_list:
            first_value_sum.append(key['Value_a'])
            second_value_sum.append(key['Value_b'])
            result_value_sum.append(key['Result_sum'])
        return first_value_sum, second_value_sum, result_value_sum

    @staticmethod
    def csv_list_for_subtraction():
        csv_list = CsvFileCaller.csv_caller_subtraction()
        first_value_dif = []
        second_value_dif = []
        result_value_dif = []
        for key in csv_list:
            first_value_dif.append(key['Value_a'])
            second_value_dif.append(key['Value_b'])
            result_value_dif.append(key['Result_difference'])
        return first_value_dif, second_value_dif, result_value_dif

    @staticmethod
    def csv_list_for_multiplication():
        csv_list = CsvFileCaller.csv_caller_multiplication()
        first_value_product = []
        second_value_product = []
        result_value_product = []
        for key in csv_list:
            first_value_product.append(key['Value_a'])
            second_value_product.append(key['Value_b'])
            result_value_product.append(key['Result_product'])
        return first_value_product, second_value_product, result_value_product

    @staticmethod
    def csv_list_for_division():
        csv_list = CsvFileCaller.csv_caller_division()
        first_value_quotient = []
        second_value_quotient = []
        result_value_quotient = []
        for key in csv_list:
            first_value_quotient.append(key['Value_a'])
            second_value_quotient.append(key['Value_b'])
            result_value_quotient.append(key['Result_quotient'])
        return first_value_quotient, second_value_quotient, result_value_quotient
