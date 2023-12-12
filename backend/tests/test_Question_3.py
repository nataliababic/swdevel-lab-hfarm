import sys
import pandas as pd
import unittest
from fastapi.testclient import TestClient

traffic = pd.read_csv("/app/app/updated_bologna.csv")
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')

sys.path.append('/app')  # Add the path to the project's base directory

# From module funct3 import avg_comparison
from app.mymodules.funct3 import avg_comparison

class Test_avg_comparison(unittest.TestCase):

    def test_average(self):
       '''
       Test the avg_comparison function.
       Pass 2019, 07, 2021, 04, considered as valid
       '''
       result = avg_comparison(traffic, '2019', '07', '2021', '04')
       self.assertEqual(result, (961, 4681))

    def test_invalid_input(self):
        result = avg_comparison(traffic, 2019, '07', '2021', 4)
        self.assertEqual(result, "Invalid input type. All input has to be "
                         "passed as string, except for the DataFrame.")

    def test_years_unavailable(self):
        result = avg_comparison(traffic, '2023', '07', '2022', '07')
        self.assertEqual(result, "Both years not available. "
                         "Please select two other years.")

    def test_year1_unavailable(self):
        result = avg_comparison('2023', '01', '2020', '12')
        self.assertEqual(result, "First year only not available. "
                         "Please change the first year.")

    def test_year2_unavailable(self):
       result = avg_comparison(traffic, '2019', '07', '2023', '01')
       self.assertEqual(result, "Second year only not available. "
                        "Please change the second year.")
    
    def test_months_unavailable(self):
        result = avg_comparison(traffic, '2019', '05', '2020', '05')
        self.assertEqual(result, "Both months not available, independently "
                         "from year chosen. Please select two other months.")
    
    def test_month1_unavailable(self):
        result = avg_comparison(traffic, '2019', '05', '2021', '03')
        self.assertEqual(result, "First month only not available, independently "
                         "from year chosen. Please change the first month.")
        
    def test_month2_unavailable(self):
        result = avg_comparison(traffic, '2019', '07', '2021', '06')
        self.assertEqual(result, "Second month only not available, independently "
                         "from year chosen. Please change the second month.")
    
    def test_months_not_for_years_selected(self):
        result = avg_comparison(traffic, '2019', '01', '2021', '07')
        self.assertEqual(result, "Both months not available for years selected. "
                         "Please select other months or change year.")

    def test_month1_not_for_year1_selected(self):
        result = avg_comparison(traffic, '2019', '01', '2021', '04')
        self.assertEqual(result, "First month selected not available for first"
                         "year selected. Please either change the first month"
                         "or first year.")
    
    def test_month2_not_for_year2_selected(self):
        result = avg_comparison(traffic, '2019', '07', '2021', '09')
        self.assertEqual(result, "Second month selected not available for second "
                         "year selected. Please either change the second month "
                         "or second year.")
        

    
if __name__ == '__main__':
    unittest.main()