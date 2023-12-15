import pandas as pd
import os
import sys
sys.path.append('/app')
from app.mymodules.csv_cleaning import load_data, preprocess_data, process_durata_column, save_data

input_file_path = './app/bologna.csv'
output_file_path = './app/updated_bologna.csv'

def load_data():
    """Load processed data from a CSV file if it exists, else generate it.

    Returns:
    DataFrame: Processed data.
    """
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

# Load processed data from 'updated_bologna.csv' if it exists; otherwise, generate and load it from 'bologna.csv'
data = load_data()
years = ['2019', '2020', '2021']
dates = data['Date']

months2019=[]
months2020=[]
months2021=[]

for year in years:
    for date_str in dates:
        if date_str[-4:] == year:
            if year=='2019':
                    months2019 = months2019 + [date_str[3:5]]
            elif year=='2020':
                    months2020 = months2020 + [date_str[3:5]]
            elif year=='2021':
                months2021 = months2021 + [date_str[3:5]]

months2019=set(months2019)
months2020=set(months2020)
months2021=set(months2021)

mmyy={}
for month in months2019:
     mmyy[month]=['2019']

for month in months2020:
     if month in mmyy:
          mmyy[month].append('2020')  
     else:
          mmyy[month]=['2020']

for month in months2021:
     if month in mmyy:
          mmyy[month].append('2021')
     else:
        mmyy[month]=['2021']   
          
mmyy = dict(sorted(mmyy.items()))

def avg_comparison(df, year1, month1, year2, month2):
    if type(year1)!=str or type(month1)!=str or type(year2)!=str or type(month2)!=str:
        return ("Invalid input type. All input has to be passed as string, "
                "except for the DataFrame.")
    elif year1 not in years and year2 not in years:
         return "Both years not available. Please select two other years."
    elif year1 not in years and year2 in years:
        return "First year only not available. Please change the first year."
    elif year2 not in years and year2 in years:
         return "Second year only not available. Please change the second year."
    elif month1 not in mmyy and month2 not in mmyy:
         return ("Both months not available, independently from year chosen. "
                 "Please select two other months.")
    elif month1 not in mmyy and month2 in mmyy:
         return ("First month only not available, independently from year chosen. "
                 "Please change the first month.")
    elif month2 not in mmyy and month1 in mmyy:
         return ("Second month only not available, independently from year chosen. "
                 "Please change the second month.")
    elif (month1 in mmyy and year1 not in mmyy[month1]) and (month2 in mmyy and year2 not in mmyy[month2]):
         return ("Both months not available for years selected. "
                 "Please select other months or change year.")
    elif month1 in mmyy and year1 not in mmyy[month1] and month2 in mmyy and year2 in mmyy[month2]:
         return ("First month selected not available for first year selected. "
                 "Please either change the first month or first year.")
    elif month2 in mmyy and year2 not in mmyy[month2] and month1 in mmyy and year1 in mmyy[month1]:
         return ("Second month selected not available for second year selected. "
                 "Please either change the second month or second year.") 
    else:
        avg_visitors1 = int((df[(df['Date'].dt.strftime('%m') == month1) & 
                                (df['Date'].dt.strftime('%Y') == year1)]
                                ['Visitors']).mean())
        avg_visitors2 = int((df[(df['Date'].dt.strftime('%m') == month2) & 
                                (df['Date'].dt.strftime('%Y') == year2)]
                                ['Visitors']).mean())
        #diff_perc = ((avg_visitors2 - avg_visitors1) / avg_visitors1) * 100
        return (avg_visitors1, avg_visitors2)
    
