import pytest
import sys
import pandas as pd
import unittest
from fastapi.testclient import TestClient

# Load the updated_bologna.csv file and save it in 'traffic'
traffic = pd.read_csv("/app/app/updated_bologna.csv")

# Convert the 'Date' column to datetime format
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')

# Add the path to the project's base directory to sys.path
sys.path.append('/app')

# Import the avg_comparison function from the funct3 module
from app.mymodules.funct3 import avg_comparison


class Test_avg_comparison(unittest.TestCase):
    '''
    Test cases for the avg_comparison function.
    '''
    def test_average(self):
        '''
        Test the avg_comparison function with valid input.
        '''
        # Pass '2019', '07', '2021', '04': valid input
        result = avg_comparison(traffic, '2019', '07', '2021', '04')
        self.assertEqual(result, (961, 4681))

    def test_invalid_input(self):
        '''
        Test avg_comparison with invalid input types.
        '''
        # Pass 2019 and 4 as integers: invalid type
        result = avg_comparison(traffic, 2019, '07', '2021', 4)
        self.assertEqual(result, "Invalid input type. All input has to be passed as string, except for the DataFrame.")

    def test_years_unavailable(self):
        '''
        Test avg_comparison with both years unavailable.
        '''
        # Pass '2023' and '2022': unavailable years
        result = avg_comparison(traffic, '2023', '07', '2022', '07')
        self.assertEqual(result, "Both years not available. Please select two other years.")

    def test_year1_unavailable(self):
        '''
        Test avg_comparison with the first year unavailable.
        '''
        # Pass '2023': first year unavailable
        result = avg_comparison(traffic, '2023', '01', '2020', '12')
        self.assertEqual(result, "First year only not available. Please change the first year.")

    def test_year2_unavailable(self):
        '''
        Test avg_comparison with the second year unavailable.
        '''
        # Pass '2023': second year unavailable
        result = avg_comparison(traffic, '2019', '07', '2023', '01')
        self.assertEqual(result, "Second year only not available. Please change the second year.")

    def test_months_unavailable(self):
        '''
        Test avg_comparison with both months unavailable
        independently from the chosen years.
        '''
        # Pass '05': in both cases month not available for any year selected
        result = avg_comparison(traffic, '2019', '05', '2020', '05')
        self.assertEqual(result, "Both months not available, independently from year chosen. Please select two other months.")

    def test_month1_unavailable(self):
        '''
        Test avg_comparison with the first month unavailable
        independently from the chosen years.
        '''
        # Pass '05': first month not available for any year selected
        result = avg_comparison(traffic, '2019', '05', '2021', '03')
        self.assertEqual(result, "First month only not available, independently from year chosen. Please change the first month.")

    def test_month2_unavailable(self):
        '''
        Test avg_comparison with the second month unavailable
        independently from the chosen years.
        '''
        # Pass '06': second month not available for any year selected
        result = avg_comparison(traffic, '2019', '07', '2021', '06')
        self.assertEqual(result, "Second month only not available, independently from year chosen. Please change the second month.")

    def test_months_not_for_years_selected(self):
        '''
        Test avg_comparison with both months not available
        for the chosen years.
        '''
        # Pass '01', '07': months not available for respective years selected
        result = avg_comparison(traffic, '2019', '01', '2021', '07')
        self.assertEqual(result, "Both months not available for years selected. Please select other months or change year.")

    def test_month1_not_for_year1_selected(self):
        '''
        Test avg_comparison with the first month not available
        for the first chosen year.
        '''
        # Pass '01': month not available for first year selected
        result = avg_comparison(traffic, '2019', '01', '2021', '04')
        self.assertEqual(result, "First month selected not available for first year selected. Please either change the first month or first year.")

    def test_month2_not_for_year2_selected(self):
        '''
        Test avg_comparison with the second month not available
        for the second chosen year.
        '''
        # Pass '09' : month not available for second year selected
        result = avg_comparison(traffic, '2019', '07', '2021', '09')
        self.assertEqual(result, "Second month selected not available for second year selected. Please either change the second month or second year.")


if __name__ == '__main__':
    # Run the unittests if this script is executed as the main program
    unittest.main()
