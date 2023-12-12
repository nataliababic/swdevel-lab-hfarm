import unittest
import pandas as pd
import os
import sys

# Add the path of the parent directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from app.mymodules.csv_cleaning import convert_to_minutes
from app.mymodules.funct1 import average_stay_length


class TestAverageStayLength(unittest.TestCase):
    def setUp(self):
        self.traffic = pd.read_csv("./app/updated_bologna.csv")

    def test_average_stay_length_valid(self):
        # Test with a valid area and stay time
        result_valid = average_stay_length(
            self.traffic, 'Palazzo Poggi', 'from 5 to 10 minutes'
        )
        expected_result = (383, 28, 537)
        self.assertEqual(
            result_valid,
            expected_result,
            "Valid area and stay time should return the expected "
            "average values"
        )

    def test_average_stay_length_invalid_area(self):
        # Test with an invalid area
        result_invalid_area = average_stay_length(
            self.traffic, 'Palazzo Chiara', 'from 5 to 10 minutes'
        )
        expected_result = "Invalid Area"
        self.assertEqual(
            result_invalid_area,
            expected_result,
            "Invalid area should return the expected result"
        )

    def test_average_stay_length_no_records(self):
        # Test with an area and stay time where no records are found
        result_no_records = average_stay_length(
            self.traffic, 'Palazzo Chiara', 'from 1 to 10 minutes'
        )
        expected_result = "Invalid Area and Duration"
        self.assertEqual(
            result_no_records,
            expected_result,
            "No records should return the expected result"
        )

    def test_average_stay_length_invalid_time(self):
        # Test with an invalid duration
        result_invalid_time = average_stay_length(
            self.traffic, 'Palazzo Poggi', 'from 1 to 10 minutes'
        )
        expected_result = "Invalid Duration"
        self.assertEqual(
            result_invalid_time,
            expected_result,
            "Invalid Duration should return the expected result"
        )

    def test_convert_to_minutes_valid(self):
        # Test with a valid duration string
        result_valid = convert_to_minutes('from 5 to 10 minutes')
        expected_result = 7.5
        self.assertEqual(
            result_valid,
            expected_result,
            "Valid duration should return the expected result"
        )

    def test_convert_to_minutes_invalid_format(self):
        # Test with an invalid duration string format
        result_invalid_format = convert_to_minutes('Ciao')
        expected_result = 0
        self.assertEqual(
            result_invalid_format,
            expected_result,
            "Invalid format should return None"
        )


if __name__ == '__main__':
    unittest.main()
