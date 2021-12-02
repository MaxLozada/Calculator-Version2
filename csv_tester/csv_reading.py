"""csv reader"""
from csv import DictReader
from typing import List, Dict


class CsvFileReader:  # pylint: disable=too-few-public-methods
    """Csv File Reader"""

    def __init__(self, csvName):
        self.name = csvName

    def key_value_maker(self):
        """ each line will produce the keys for the dict and
        the values that belong next to those keys"""
        file_handle = open(self.name, 'r', encoding="utf8")  # pylint: disable=consider-using-with
        csv_reader = DictReader(file_handle)
        table: List[Dict[str, float]] = []

        for row in csv_reader:

            float_row: Dict[str, float] = {}
            for column in row:
                float_row[column] = float(row[column])
            table.append(float_row)
        return table
