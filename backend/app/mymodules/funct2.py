# First we import all the needed datasets 
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import os
app = FastAPI()


# we start defining the traffic_per_area function linking the name of each area to the number of visotors on the input day. 

def traffic_per_area(traffic, target_date):
    
    '''
    Get the total number of visitors per area for a given date.
    Parameters:
    data (DataFrame): The input DataFrame containing date, area, and visitors.
    target_date (str): The date in 'YYYY-MM-DD' format.

    Returns:
    Result: DataFrame with the total visitors per area for the given date.
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


# Define the area with the highest affluence
def highest_affluence(result): 

    '''
    Input: Result (DataFrame), the total visitors per area Fataframe created in traffic_per_area function

    Output : the area with the maximum amount of visitors 
    '''

    max_area_row = result.loc[result['Forcasted_Visitors'].idxmax()]
    max_area = max_area_row['Area']
    mean_visitors = max_area_row['Forcasted_Visitors']

    return 'The Area with the highest tourism affluence is {} with {} Forcasted Visitors'.format(max_area, mean_visitors)


# Define the area with lowest affluence
def lowest_affluence(result):

    '''
    Input: Result (DataFrame), the total visitors per area Fataframe created in traffic_per_area function

    Output : the area with the manimum amount of visitors 
    '''

    min_area_row = result.loc[result['Forcasted_Visitors'].idxmin()]
    min_area = min_area_row['Area']
    mean_visitors = min_area_row['Forcasted_Visitors']

    return 'The Area with the lowest tourism affluence is {} with {} Forcasted Visitors'.format(min_area, mean_visitors)
