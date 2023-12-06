"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from anyio import Path
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Optional
from datetime import datetime
import pandas as pd

from enum import Enum
from typing import Optional
import os

import sys
sys.path.append('/app')  # Add the path to the project's base directory

from app.mymodules.csv_cleaning import load_data, preprocess_data, process_durata_column, save_data
from app.mymodules.Question_2 import traffic_per_area, highest_affluence, lowest_affluence



input_file_path = '/app/app/bologna.csv'
output_file_path = '/app/app/updated_bologna.csv'

traffic = pd.read_csv("/app/app/updated_bologna.csv")
traffic['Date'] = pd.to_datetime(traffic['Date'], format='%d/%m/%Y', errors='coerce')

# Check if the output file exists
if not os.path.exists(output_file_path):
    # Load data
    traffic = load_data(input_file_path)

    # Preprocess data
    traffic = preprocess_data(data)

    # Process Durata column
    traffic = process_durata_column(data)

    # Save the updated data
    save_data(traffic, output_file_path)

#    print("ciao")


# Create FastApi App
app = FastAPI()

#@app.get('/csv_show')
#def read_and_return_csv():
#    aux = df['Area'].values
#    return{"Area": str(aux.argmin())}

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Bologna": "Hello World!!!!"}

from pydantic import BaseModel



@app.get("/forecasted-visitors")
def forecasted_visitors_per_area(target_date: str):

    # Call the existing function to get forecasted visitors
    result = traffic_per_area(traffic, target_date)

    # Check if the result is a messa ge indicating no data
    if isinstance(result, str):
        raise HTTPException(status_code=404, detail=result)


    # Convert the result DataFrame to a dictionary
    result_dict = result.to_dict(orient='records')

    # Create the result_max function
    result_max = highest_affluence(result)

    # Create the result_min function
    result_min = lowest_affluence(result)

    return result_dict, result_max, result_min

'''
 How to use it 
.../forecasted-visitors?target_date=01-10
forcasted visitors is seen as the "branch" of our website
taget_date is seen as an input, for this reaoson is considered as a quest ( we need to put ? and the expected result )
'''


# Define the API endpoint
#@app.get ('/traffic/{target_date}')
#async def get_traffic_per_area (target_date:str):

     # Call the traffic_per_area function
 #   result = traffic_per_area(traffic, target_date)

    # Convert result DataFrame to a list of dictionaries
    #result_list = result.to_dict(orient='records')

 #   return result







# Dictionary of birthdays
#birthdays_dictionary = {
    #'Albert Einstein': '03/14/1879',
    #'Benjamin Franklin': '01/17/1706',
    #'Ada Lovelace': '12/10/1815',
    #'Donald Trump': '06/14/1946',
    #'Rowan Atkinson': '01/6/1955'
#}

#df = pd.read_csv('/app/app/employees.csv')

#@app.get('/csv_show')
#def read_and_return_csv():
   # aux = df['Age'].values
   # return{"Age": str(aux.argmin())}

#@app.get('/')
#def read_root():
   # """
    #Root endpoint for the backend.

    #Returns:
    #    dict: A simple greeting.
    #"""
    #return {"Hello": "Worldddd"}


#@app.get('/query/{person_name}')
#def read_item(person_name: str):
   #"""
    #Endpoint to query birthdays based on person_name.

    #Args:
    #    person_name (str): The name of the person.

    #Returns:
    #    dict: Birthday information for the provided person_name.
    #"""
    #person_name = person_name.title()  # Convert to title case for consistency
    #birthday = birthdays_dictionary.get(person_name)
    ##if birthday:
    #    return {"person_name": person_name, "birthday": birthday}
    #else:
    #    return {"error": "Person not found"}


#@app.get('/module/search/{person_name}')
#def read_item_from_module(person_name: str):
   # return {return_birthday(person_name)}


#@app.get('/module/all')
#def dump_all_birthdays():
    #return {print_birthdays_str()}


#@app.get('/get-date')
#def get_date():
 #   """
#    Endpoint to get the current date.

#    Returns:
#        dict: Current date in ISO format.
#    """
#    current_date = datetime.now().isoformat()
#    return JSONResponse(content={"date": current_date})
