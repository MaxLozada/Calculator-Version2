from csv import DictReader
from typing import List, Dict


class CsvFileReader:

    def __init__(self, csvName):
        self.name = csvName

    def key_value_maker(self):
        """ each line will produce the keys for the dict and the values that belong next to those keys"""
        file_handle = open(self.name, 'r', encoding="utf8")
        csv_reader = DictReader(file_handle)
        """ set up table with list of dictionaries that contain str and float """
        table: List[Dict[str, float]] = []
        """turns string to float for column that contains the numbers"""
        for row in csv_reader:
            """new dict for each row"""
            float_row: Dict[str, float] = {}
            for column in row:
                """stores value in new dict"""
                float_row[column] = float(row[column])
            table.append(float_row)
        return table

#     file_handle.close()

#    for key in float_row.keys():
#        print(key)


#    for value in float_row.values():
#        print(value)

#    for item in float_row.items():
#        print(item)

#    for item in float_row.items():
#        print(type(item))

#    print(float_row.values())

#    print(float_row['Value_a'])


