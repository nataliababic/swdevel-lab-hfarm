import pandas as pd
import holidays
import re
from datetime import datetime


def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Loaded data from the CSV file.
    """
    data = pd.read_csv(file_path, sep=';')
    return data


def save_data(data, output_file_path):
    """
    Save data to a CSV file.

    Parameters:
    data (DataFrame): The DataFrame to be saved.
    output_file_path (str): The path to save the CSV file.
    """
    data.to_csv(output_file_path, index=False)


def is_holiday(date):
    """
    Check if a date is a holiday in Italy.

    Parameters:
    date (datetime): The date as a datetime object.

    Returns:
    bool: True if the date is a holiday or a weekend, False otherwise.
    """
    if not isinstance(date, datetime):
        return False  # Return False for any input that is not a datetime

    italy_holidays = holidays.Italy(years=[2019, 2020, 2021])

    is_weekend = date.weekday() >= 5  # Saturday or Sunday
    is_official_holiday = date in italy_holidays
    return is_weekend or is_official_holiday


def preprocess_data(data):
    """
    Preprocess the data.

    Add the Holiday column.
    Shifts 'Duration' values to 'Visitors' column for the year 2021.
    Sets 'Duration' to "0" for the year 2021.

    Parameters:
    data (DataFrame): The input DataFrame.

    Returns:
    DataFrame: Preprocessed DataFrame.
    """
    data_copy = data.copy()
    data_copy['Date'] = pd.to_datetime(data_copy['Date'], dayfirst=True)
    data_copy['Holiday'] = data_copy['Date'].apply(is_holiday)

    # Shift 'Duration' to 'Visitors' column only for 2021
    mask_2021 = data_copy['Date'].dt.year == 2021
    selected_data = pd.to_numeric(data_copy.loc[mask_2021, 'Duration'])
    data_copy.loc[mask_2021, 'Visitors'] = selected_data

    # Set 'Duration' to "0" only for 2021
    data_copy.loc[mask_2021, 'Duration'] = "0"

    data_copy["Visitors"] = data_copy["Visitors"].fillna(0).astype(int)

    data_copy = data_copy.sort_values(by="Date", ascending=True)
    data_copy['Date'] = data_copy['Date'].dt.strftime('%d/%m/%Y')

    # Set 'Visitors' < "0" to "0".
    data_copy.loc[data_copy['Visitors'] < 0, 'Visitors'] = 0

    return data_copy


import re

def convert_to_minutes(duration_str):
    """
    Convert strings containing the duration to minutes.

    Parameters:
    duration_str (str): The duration string.

    Returns:
    int: Duration in minutes.
    """
    if duration_str == '0' or duration_str is None:
        return 0
    
    duration_str = duration_str.lower()  # Convert the string to lowercase
    pattern = r'\d+'  # Pattern to match consecutive digits in a string
    values = re.findall(pattern, duration_str)
    if values:
        values = [int(val) for val in values]
        avg_value = sum(values) / len(values)
        if 'hour' in duration_str:
            avg_value *= 60
        return avg_value
    else:
        return 0



def process_durata_column(data):
    """
    Process the Duration column to get average duration in minutes.

    Parameters:
    data (DataFrame): The input DataFrame.

    Returns:
    DataFrame: DataFrame with the new Duration.
    """
    data['Duration'] = data['Duration'].apply(convert_to_minutes)
    return data
