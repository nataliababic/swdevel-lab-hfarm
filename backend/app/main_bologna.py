"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""


from fastapi.responses import JSONResponse
from datetime import datetime
import pandas as pd
import os


from mymodules.csv_cleaning import load_data, preprocess_data, process_durata_column, save_data


input_file_path = '/app/app/bologna.csv'
output_file_path = '/app/app/updated_bologna.csv'

# Check if the output file exists
if not os.path.exists(output_file_path):
    # Load data
    data = load_data(input_file_path)

    # Preprocess data
    data = preprocess_data(data)

    # Process Durata column
    data = process_durata_column(data)

    # Save the updated data
    save_data(data, output_file_path)

    print("ciao")


data = pd.read_csv("/app/app/updated_bologna.csv")
print(data)