"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd

import sys
sys.path.append('/app')  # Add the path to the project's base directory

from app.mymodules.funct2 import traffic_per_area, highest_affluence, lowest_affluence
from app.mymodules.funct1 import average_stay_length
from app.mymodules.funct3 import avg_comparison

# Create FastApi App
app = FastAPI()

traffic = pd.read_csv('/app/app/updated_bologna.csv')
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')


@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Bologna": "Hello World!!!!"}


#QUESTION 1
@app.get("/average-visitors/{area}/{stay_time}")
def make_average(area: str, stay_time: str):
    print(area, stay_time)
    # Call the existing function from the module to get the average of visitors in that area for that amount of time
    result = average_stay_length(traffic,area,stay_time)
    
    if isinstance(result, str):
        # If the result is a string (indicating an error message), raise HTTPException
        raise HTTPException(status_code=404, detail=result)
    print(result)
    return  JSONResponse(content={"avg_total": result[0],"avg_holiday":result[1],"avg_non_holiday":result[2]})


#QUESTION 2
@app.get("/forecasted-visitors/{target_date}")
def forecasted_visitors_per_area(target_date: str):

    # Call the existing function to get forecasted visitors
    result = traffic_per_area(traffic, target_date)

    # Check if the result is a message indicating no data
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)


    # Convert the result DataFrame to a dictionary
    result_dict = result.to_dict(orient='records')

    # Create the result_max function
    result_max = highest_affluence(result)

    # Create the result_min function
    result_min = lowest_affluence(result)

    return  JSONResponse(content = {"Affluence of each area": result_dict,
                                  "Highest affluence":result_max,
                                  "Lowest affluence": result_min})


#QUESTION 3
@app.get("/average-period/{year1}/{month1}/{year2}/{month2}")
def average_comparison(year1:str, month1:str, year2:str, month2:str):
    result = avg_comparison(traffic, year1, month1, year2, month2)
    
    return  JSONResponse(content={"Avg first period": result[0],"Avg second period":result[1]})
'''
 How to use it 
.../forecasted-visitors/01-10
forcasted visitors is seen as the "branch" of our website
taget_date is seen as an input, for this reaoson is considered as a quest ( we need to put ? and the expected result )
'''
