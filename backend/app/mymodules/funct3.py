import pandas as pd
import os
import sys
sys.path.append('/app')
from app.mymodules.csv_cleaning import load_data, preprocess_data, process_durata_column, save_data

input_file_path = './app/bologna.csv'
output_file_path = './app/updated_bologna.csv'


def load_data():
    '''
    Load processed data from a CSV file if it exists, else generate it.

    Returns:
    DataFrame: Processed data.
    '''
    # Check if the output file exists; if not, create it
    if not os.path.exists(output_file_path):
        # Load data
        traffic = pd.read_csv(input_file_path, sep=";")

        # Preprocess data
        traffic = preprocess_data(traffic)

        # Process Durata column
        traffic = process_durata_column(traffic)

        # Save the updated data
        save_data(traffic, output_file_path)

    # Load the processed data
    return pd.read_csv(output_file_path)


# Load processed data from 'updated_bologna.csv' if it exists;
# otherwise, generate and load it from 'bologna.csv'
data = load_data()

# Save available years in list
years = ['2019', '2020', '2021']

# Extract dates from the 'Date' column
dates = data['Date']

# Initialise lists to store the months available for each year
months2019 = []
months2020 = []
months2021 = []

# Iterate through each year and date to categorise the months
for year in years:
    for date_str in dates:
        if date_str[-4:] == year:
            # Depending on the year, append the month to the corresponding list
            if year == '2019':
                months2019 = months2019 + [date_str[3:5]]
            elif year == '2020':
                months2020 = months2020 + [date_str[3:5]]
            elif year == '2021':
                months2021 = months2021 + [date_str[3:5]]

# Convert lists to sets to get unique months per year
months2019 = set(months2019)
months2020 = set(months2020)
months2021 = set(months2021)

# Initialise a dictionary to store years for each month
mmyy = {}

# Populate the dictionary with months and years
for month in months2019:
    mmyy[month] = ['2019']

for month in months2020:
    if month in mmyy:
        mmyy[month].append('2020')
    else:
        mmyy[month] = ['2020']

for month in months2021:
    if month in mmyy:
        mmyy[month].append('2021')
    else:
        mmyy[month] = ['2021']

# Sort the dictionary by month
mmyy = dict(sorted(mmyy.items()))


def avg_comparison(df, year1, month1, year2, month2):
    '''
    Compare the average number of visitors for two different periods,
    each defined by month and year.

    Args:
        df (DataFrame): The DataFrame containing the data.
        year1 (str): The first year for comparison.
        month1 (str): The first month for comparison.
        year2 (str): The second year for comparison.
        month2 (str): The second month for comparison.

    Returns:
        String or Tuple: If there's an issue with the input, return
        an error message (str). Otherwise, return a tuple containing
          the average number of visitors for the specified months and years.
    '''
    # Check types of inputs
    if not all(isinstance(val, str) for val in [year1, month1, year2, month2]):
        return "Invalid input type. All input has to be passed as string, except for the DataFrame."

    # Check if years and months exist in the DataFrame
    elif year1 not in years and year2 not in years:
        return "Both years not available. Please select two other years."
    elif year1 not in years and year2 in years:
        return "First year only not available. Please change the first year."
    elif year2 not in years and year1 in years:
        return "Second year only not available. Please change the second year."
    elif month1 not in mmyy and month2 not in mmyy:
        return "Both months not available, independently from year chosen. Please select two other months."
    elif month1 not in mmyy and month2 in mmyy:
        return "First month only not available, independently from year chosen. Please change the first month."
    elif month2 not in mmyy and month1 in mmyy:
        return "Second month only not available, independently from year chosen. Please change the second month."

    # Check if months are available for years selected
    elif (month1 in mmyy and year1 not in mmyy[month1]) and (month2 in mmyy and year2 not in mmyy[month2]):
        return "Both months not available for years selected. Please select other months or change year."
    elif month1 in mmyy and year1 not in mmyy[month1] and month2 in mmyy and year2 in mmyy[month2]:
        return "First month selected not available for first year selected. Please either change the first month or first year."
    elif month2 in mmyy and year2 not in mmyy[month2] and month1 in mmyy and year1 in mmyy[month1]:
        return "Second month selected not available for second year selected. Please either change the second month or second year."

    # If input type is correct and years and months exists, compute and return
    # the average number of visitors for the given inputs
    else:
        avg_visitors1 = int((df[(df['Date'].dt.strftime('%m') == month1) & (df['Date'].dt.strftime('%Y') == year1)]['Visitors']).mean())
        avg_visitors2 = int((df[(df['Date'].dt.strftime('%m') == month2) & (df['Date'].dt.strftime('%Y') == year2)]['Visitors']).mean())
        # diff_perc = ((avg_visitors2 - avg_visitors1) / avg_visitors1) * 100
        return (avg_visitors1, avg_visitors2)
