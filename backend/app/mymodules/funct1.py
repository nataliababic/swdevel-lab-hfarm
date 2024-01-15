import pandas as pd
import sys
sys.path.append('/app')
from app.mymodules.csv_cleaning import convert_to_minutes


# Mapping of duration strings to minutes
duration_mapping = {
    'from 5 to 10 minutes': (5, 10),
    'from 40 to 60 minutes': (40, 60),
    'from 3 to 4 hours': (180, 240),
    'from 4 to 6 hours': (240, 360),
    'from 10 to 20 minutes': (10, 20),
    'from 20 to 40 minutes': (20, 40),
    'less 1 minute': (0, 1),
    'from 1 to 5 minutes': (1, 5),
    'from 60 to 90 minutes': (60, 90),
    'from 90 to 120 minutes': (90, 120),
    'over 6 hours': (360, float('inf')),
    'from 2 to 3 hours': (120, 180)
}


def average_stay_length(df, area, stay_time):
    '''
    Calculate the average number of visitors for a given area and stay time.

    Parameters:
    - df (DataFrame): The input DataFrame containing traffic data.
    - area (str): The specific area for which to calculate
    the average stay length.
    - stay_time (str): The duration range for which to calculate
    the average stay length.

    Returns:
    - tuple: A tuple containing the average total visitors,
        average visitors on holidays,
        and average visitors on non-holidays.
        If the area or stay time is invalid,
        returns an appropriate error message.
    '''

    # Check if both area and duration are invalid
    if area not in df['Area'].unique() and stay_time not in duration_mapping:
        return "Invalid Area and Duration"

    # Check if area is invalid
    if area not in df['Area'].unique():
        return "Invalid Area"

    # Check if duration is invalid
    if stay_time not in duration_mapping:
        return "Invalid Duration"

    # Convert the duration string to minutes
    stay_minutes = convert_to_minutes(stay_time)

    # If area and stay_time are valid, proceed with the selection of the data
    if area in df['Area'].values and stay_minutes in df['Duration'].values:
        filtered_df = df[df['Area'] == area]
        filtered_df = filtered_df[(filtered_df['Duration'] >= duration_mapping[stay_time][0]) & (filtered_df['Duration'] <= duration_mapping[stay_time][1])]

    # Calculate the averages for total, holiday, and non-holiday visitors
    avg_tot = int(filtered_df['Visitors'].mean())
    avg_holiday = int(
        filtered_df[filtered_df['Holiday'] is True]['Visitors'].mean()
    )
    avg_non_holiday = int(
        filtered_df[filtered_df['Holiday'] is False]['Visitors'].mean()
    )

    return (avg_tot, avg_holiday, avg_non_holiday)
