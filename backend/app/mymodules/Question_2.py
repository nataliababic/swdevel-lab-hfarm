# First we import all the needed datasets 
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import os
app = FastAPI()

# Now we import updated_bologna.csv as traffic
traffic = pd.read_csv('/app/app/updated_bologna.csv')

# Convert 'Date' column to datetime with appropriate format for day/month
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')

# we start defining the traffic_per_area function linking the name of each area to the number of visotors on the input day. 

def traffic_per_area(traffic, target_date):
    
    '''
    Get the total number of visitors per area for a given date.
    Parameters:
    data (DataFrame): The input DataFrame containing date, area, and visitors.
    target_date (str): The date in 'YYYY-MM-DD' format.

    Returns:
    DataFrame: DataFrame with the total visitors per area for the given date.
    '''

    # Filter data for the years 2019, 2020, and 2021
    filtered_traffic = traffic[traffic['Date'].dt.year.isin([2019, 2020, 2021]) &
                               (traffic['Date'].dt.strftime('%d-%m') == target_date)]
    
    #Return a message in case the date is not available 
    if filtered_traffic.empty:
        return "No data available for the given date."

    # Calculate the mean visitors per area for the given date
    result = filtered_traffic.groupby('Area')['Visitors'].mean().round(decimals=0).astype(int).reset_index()
    result.columns = ['Area', 'Forcasted_Visitors']

    return result

# Usage
# Replace 'your_data' with your DataFrame variable and 'desired_date' with the date you want to check
date_result = traffic_per_area (traffic, "01-10")
print(date_result)

# Define the area with the highest affluence
def highest_affluence(result): 

    '''
    Inout: date given in  traffic_per_area function
    Output : the area with the maximum amount of visitors 
    '''

    max_area_row = result.loc[result['Forcasted_Visitors'].idxmax()]
    max_area = max_area_row['Area']
    mean_visitors = max_area_row['Forcasted_Visitors']

    return 'The Area with the highest tourism affluence is {} with {} Forcasted Visitors'.format(max_area, mean_visitors)

# Example usage
date_result_max = highest_affluence (date_result)
print (date_result_max)

# Define the area with lowest affluence
def lowest_affluence(result):

    '''
    Inout: date given in  traffic_per_area function
    Output : the area with the maximum amount of visitors 
    '''

    min_area_row = result.loc[result['Forcasted_Visitors'].idxmin()]
    min_area = min_area_row['Area']
    mean_visitors = min_area_row['Forcasted_Visitors']

    return 'The Area with the lowest tourism affluence is {} with {} Forcasted Visitors'.format(min_area, mean_visitors)

# Example usage
date_result_min = lowest_affluence(date_result)
print (date_result_min)

## Possible tests 