import pandas as pd
import holidays
import re

def load_data(file_path):
    """Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: Loaded data from the CSV file.
    """
    data = pd.read_csv(file_path, sep=';')
    return data

def save_data(data, output_file_path):
    """Save data to a CSV file.

    Parameters:
    data (DataFrame): The DataFrame to be saved.
    output_file_path (str): The path to save the CSV file.
    """
    data.to_csv(output_file_path, index=False)

def is_holiday(date):
    """Check if a date is a holiday.

    Parameters:
    date (str): The date in string format.

    Returns:
    bool: True if the date is a holiday or a weekend, False otherwise.
    """
    italy_holidays = holidays.Italy(years=[2019, 2020, 2021])
    try:
        date_obj = pd.to_datetime(date)
        is_weekend = date_obj.weekday() >= 5  # Saturday or Sunday
        is_official_holiday = date_obj in italy_holidays
        return is_weekend or is_official_holiday
    except ValueError:
        return False

def preprocess_data(data):
    """Preprocess the data.

    Parameters:
    data (DataFrame): The input DataFrame.

    Returns:
    DataFrame: Preprocessed DataFrame.
    """
    data['Holiday'] = data['Date'].apply(is_holiday)
    data['Date'] = pd.to_datetime(data['Date'])
    data["Visitors"] = data["Visitors"].fillna(0).astype(int)
    data = data.sort_values(by="Date", ascending=True)
    data['Date'] = data['Date'].dt.strftime('%d/%m/%Y')
    data.loc[data['Visitors'] < 0, 'Visitors'] = 0
    return data

def convert_to_minutes(duration_str):
    """Convert duration strings to minutes.

    Parameters:
    duration_str (str): The duration string.

    Returns:
    int: Duration in minutes.
    """
    pattern = r'\d+'
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
    """Process the Duration column to get average duration in minutes.

    Parameters:
    data (DataFrame): The input DataFrame.

    Returns:
    DataFrame: DataFrame with the new Duration added.
    """
    data['Duration'] = data['Duration'].apply(convert_to_minutes)
    return data
