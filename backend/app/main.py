"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project by integrating the modules
written apart.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import sys
sys.path.append('/app')  # Add the path to the project's base directory

from app.mymodules.funct2 import traffic_per_area, highest_affluence, lowest_affluence
from app.mymodules.funct1 import average_stay_length
from app.mymodules.funct3 import avg_comparison

# Create FastAPI
app = FastAPI()

traffic = pd.read_csv('/app/app/updated_bologna.csv')
traffic['Date'] = pd.to_datetime(traffic['Date'],
                                 format='%d/%m/%Y', errors='coerce')


# Use @app.get() to associate a particular function with
# a specific URL path and HTTP method.
@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: simple notification.
    """
    return {"Bologna": "Backend reachable"}


# Call to function 1
@app.get("/average-visitors/{area}/{stay_time}")
def make_average(area: str, stay_time: str):
    """
    Calculate the average number of visitors in the specified area
    for the given stay time.

    Args:
        area (str): The area for which to calculate the average visitors.
        stay_time (str): The specified stay time.

    Returns:
        JSONResponse: A JSON response containing the calculated averages
                      for total, holiday, and non-holiday visitors.
    """
    # Call the existing function from the module to get the average of
    # visitors in that area for that amount of time.
    result = average_stay_length(traffic, area, stay_time)
    print(result)
    return JSONResponse(content={"avg_total": result[0],
                                 "avg_holiday": result[1],
                                 "avg_non_holiday": result[2]})


# Call to function 2
@app.get("/forecasted-visitors/{target_date}")
def forecasted_visitors_per_area(target_date: str):
    """
    Get forecasted visitors for each area and additional statistics
    for a given target date.

    Args:
        target_date (str): The target date in the format 'dd-mm'.

    Returns:
        JSONResponse: A JSON response containing the forecasted visitors
                      for each area, the highest affluence, the lowest
                      affluence, and an error indicator.
    """
    # Call the existing function from the module to get the forecasted visitors
    result = traffic_per_area(traffic, target_date)
    error = False

    # Check if the result is a message indicating no data
    if isinstance(result, str):
        error = True

    # If no error is raised, convert the result DataFrame to a dictionary
    result_dict = None
    result_max = None
    result_min = None
    if not error:
        result_dict = result.to_dict(orient='records')

        # Create the result_max function
        result_max = highest_affluence(result)

        # Create the result_min function
        result_min = lowest_affluence(result)

    return JSONResponse(content={"Affluence of each area": result_dict,
                                 "Highest affluence": result_max,
                                 "Lowest affluence": result_min,
                                 "error": error})


# Call to function 3
@app.get("/average-period/{year1}/{month1}/{year2}/{month2}")
def average_comparison(year1: str, month1: str, year2: str, month2: str):
    """
    Compare average number of visitors for two periods.

    Args:
        year1 (str): The year of the first period.
        month1 (str): The month of the first period.
        year2 (str): The year of the second period.
        month2 (str): The month of the second period.

    Returns:
        JSONResponse: A JSON response containing the average values for the
                      first and second periods and an error indicator.
    """
    result = avg_comparison(traffic, year1, month1, year2, month2)
    error = False

    if isinstance(result, str):
        error = True

    return JSONResponse(content={"Avg first period": result[0],
                                 "Avg second period": result[1],
                                 "error": error})
