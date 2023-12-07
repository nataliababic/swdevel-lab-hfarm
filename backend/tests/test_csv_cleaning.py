import os
import sys
from fastapi.testclient import TestClient
import pandas as pd
from datetime import datetime
import holidays

# Add the path of the parent directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from app.mymodules.csv_cleaning import load_data, save_data, is_holiday, preprocess_data, convert_to_minutes, process_durata_column


# Smoke test for load_data
def test_load_data_smoke():
    file_path = './app/updated_bologna.csv'  # Adjust the path based on your directory structure
    loaded_data = load_data(file_path)
    assert loaded_data is not None, "Loading data failed"
    assert isinstance(loaded_data, pd.DataFrame), "Loaded data is not a DataFrame"


def test_is_holiday_smoke():
    # Create a list of known Italian holidays for the test years
    italy_holidays = holidays.Italy(years=[2019, 2020, 2021])

    # Test known weekends (Saturday and Sunday)
    saturday = datetime(2019, 7, 20)  # A Saturday
    sunday = datetime(2019, 7, 21)    # A Sunday

    assert is_holiday(saturday), "Saturday should be identified as a holiday/weekend"
    assert is_holiday(sunday), "Sunday should be identified as a holiday/weekend"

    # Test known Italian holidays
    # Add known Italian holidays for the test years to the italy_holidays set
    test_holidays = [
        datetime(2019, 8, 15),  # New Year's Day
        datetime(2020, 1, 1),  # Easter Monday
        #datetime(2021, 12, 25)  # Christmas Day
        # Add more holidays as needed for your test years
    ]

    for holiday in test_holidays:
        assert is_holiday(holiday), f"{holiday} not identified as an Italian holiday"

    # Test a non-holiday weekday
    non_holiday_weekday = datetime(2019, 7, 25)  # A Thursday
    assert not is_holiday(non_holiday_weekday), "Not identified as a holiday"




# Run the smoke tests
test_load_data_smoke()

# Run the smoke test
test_is_holiday_smoke()