import os
import sys
from fastapi.testclient import TestClient
import pandas as pd
from datetime import datetime
import holidays

# Add the path of the parent directory of your project to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from app.mymodules.csv_cleaning import (
    load_data, save_data, is_holiday,
    preprocess_data, convert_to_minutes,
    process_durata_column
)


def test_load_data_smoke():
    """Test the load_data function for basic functionality.

    Inputs:
        None (Uses a predefined file path to load data)

    Outputs:
        Asserts if loaded data is not None and is a Pandas DataFrame.
    """
    # Path to the CSV file for loading data
    file_path = './app/updated_bologna.csv'
    loaded_data = load_data(file_path)
    assert loaded_data is not None, "Loading data failed"
    assert isinstance(loaded_data, pd.DataFrame), "Not a DataFrame"


def test_save_data_smoke():
    """Test the save_data function for basic functionality.

    Inputs:
        Generates a sample DataFrame and attempts to save it to a CSV file.

    Outputs:
        Asserts if the CSV file was created successfully.
    """
    # Directory for testing CSV file creation
    test_directory = './tests/'

    # Ensure the directory exists or create it if not
    os.makedirs(test_directory, exist_ok=True)

    # Create a sample DataFrame
    data = pd.DataFrame({'A': [1, 2, 3], 'B': ['x', 'y', 'z']})

    # Define the output file path for the generated CSV file
    output_file_path = os.path.join(test_directory, 'output_test.csv')

    try:
        # Attempt to save the data to a CSV file
        save_data(data, output_file_path)
    except Exception as e:
        assert False, f"Exception encountered: {e}"
    else:
        assert os.path.isfile(output_file_path), "CSV file was not created"


def test_is_holiday():
    """Test cases for the is_holiday function.

    Inputs:
        Predefined dates to check against weekends and Italian holidays.

    Outputs:
        Verifies correct identification of holidays and weekends.
    """
    # Define weekends (Saturday and Sunday)
    saturday = datetime(2019, 7, 20)
    sunday = datetime(2019, 7, 21)

    # Assertion for weekends as holidays
    assert is_holiday(saturday), "Saturday should be identified as a holiday"
    assert is_holiday(sunday), "Sunday should be identified as a holiday"


def test_is_italian_holiday():
    """Test the is_holiday function's identification of Italian holidays.

    Inputs:
        Known Italian holiday dates for the test years [2019, 2020, 2021].

    Outputs:
        Verifies if the function correctly identifies known Italian holidays.
    """
    # Create a list of known Italian holidays for the test years
    italy_holidays = holidays.Italy(years=[2019, 2020, 2021])

    # Test known Italian holidays
    test_holidays = [
        datetime(2019, 8, 15),  # Assumption: New Year's Day
        datetime(2020, 1, 1),   # Assumption: Easter Monday
        # Add more holidays as needed for your test years
    ]

    # Assertion for identification of Italian holidays
    for holiday in test_holidays:
        assert is_holiday(holiday), f"{holiday} not identified as holiday"


def test_is_not_holiday():
    """Test the is_holiday function's identification of non-holidays.

    Inputs:
        Test dates that are weekdays but not holidays.

    Outputs:
        Verifies if the function correctly identifies non-holiday weekdays.
    """
    # Test a non-holiday weekday
    non_holiday_weekday = datetime(2019, 7, 25)  # A Thursday
    assert not is_holiday(non_holiday_weekday), "Not identified as a holiday"


def test_invalid_input_is_holiday():
    """Test the is_holiday function's behavior with invalid input.

    Inputs:
        Provides a non-datetime object to check the function's handling.

    Outputs:
        Asserts that the function returns False for invalid inputs.
    """
    invalid_input = "Ciao come stai"

    # Verify handling of invalid input by is_holiday function
    result = is_holiday(invalid_input)
    assert not result, "Expected False due to invalid input type"


def test_is_holiday_attribute_error_handling():
    """Test is_holiday function's AttributeError handling.

    Verifies if the is_holiday function properly handles
    AttributeErrors for various inputs.
    """
    # Test for None input and invalid date types
    assert is_holiday(None) is False, "Expected False"

    # Test for invalid date type (string)
    assert is_holiday("2023-12-25") is False, "Expected False"

    # Test for invalid date type (integer)
    assert is_holiday(20231225) is False, "Expected False"

    # Test for valid date input causing AttributeError
    class CustomDate:
        pass  # Simulate an object that doesn't have weekday() method

    # This should result in an AttributeError in the function
    assert is_holiday(CustomDate()) is False, "Expected False - AttributeError"


def test_preprocess_data_smoke():
    """Test the preprocess_data function for basic functionality.

    Inputs:
        A sample DataFrame

    Outputs:
        Asserts if the preprocessed DataFrame contains all required columns.
    """
    # Sample DataFrame with necessary columns
    sample_data = pd.DataFrame({
        'Date': ['01/01/2021', '02/01/2021', '03/01/2021'],
        'Area': ['A', 'B', 'C'],
        'Duration': ['20', '15', '25'],
        'Visitors': [100, 150, 200],
        'Holiday': [True, False, False]  # Assuming these values
    })

    try:
        # Apply preprocess_data function on sample data
        preprocessed_data = preprocess_data(sample_data)
    except Exception as e:
        assert False, f"Exception encountered: {e}"
    else:
        # Assertion to check presence of necessary columns in preprocessed data
        required_columns = ['Date', 'Area', 'Duration', 'Visitors', 'Holiday']
        assert all(column in preprocessed_data.columns
                   for column in required_columns), \
            "Missing required columns in preprocessed data"


def test_convert_to_minutes_with_hours():
    """Test convert_to_minutes with duration strings in hours."""
    duration_1 = "More than 2 hours"
    assert convert_to_minutes(duration_1) == 120, "Conversion failed"


def test_convert_to_minutes_with_minutes():
    """Test convert_to_minutes with duration strings in minutes."""
    duration_2 = "Less than 30 minutes"
    assert convert_to_minutes(duration_2) == 30, "Conversion failed"


def test_convert_to_minutes_with_empty_string():
    """Test convert_to_minutes with an empty string."""
    empty_duration = ""
    assert convert_to_minutes(empty_duration) == 0, "Conversion failed"


def test_convert_to_minutes_without_numbers():
    """Test convert_to_minutes with a string not containing any numbers."""
    no_number_duration = "Blue Sky"
    assert convert_to_minutes(no_number_duration) == 0, "Conversion failed"


def test_process_durata_column_smoke():
    """Smoke test for the process_durata_column function.

    Checks if the 'Duration' column is added and contains
    values represented as integers or floats,
    indicating the duration in minutes.

    Inputs:
        None (Uses predefined sample DataFrame)

    Outputs:
        Verifies the presence and type of values.
    """
    # Sample DataFrame with Duration values in different formats
    sample_data = pd.DataFrame({
        'Duration': ['2 hours', '90 minutes', '1 hour']
    })

    # Apply the process_durata_column function to the sample data
    processed_data = process_durata_column(sample_data)

    # Check if 'Duration' column exists in the processed data
    assert 'Duration' in processed_data.columns, "Duration column not found"

    # Check values in 'Duration' column
    assert all(isinstance(val, (int, float))
               for val in processed_data['Duration']), \
        "Duration values are not converted"


# Run the smoke tests for loading a file
test_load_data_smoke()

# Run the smoke tests for saving a file
test_save_data_smoke()

# Run the tests for the is_holiday function
test_is_holiday()
test_is_italian_holiday()
test_is_not_holiday()
test_invalid_input_is_holiday()
test_is_holiday_attribute_error_handling()

# Run the smoke test for the preprocess_data function
test_preprocess_data_smoke()

# Run the tests with various inputs for the convert_to_minutes function
test_convert_to_minutes_with_hours()
test_convert_to_minutes_with_minutes()
test_convert_to_minutes_with_empty_string()
test_convert_to_minutes_without_numbers()

# Run the smoke test for the process_durata_columns function
test_process_durata_column_smoke()
