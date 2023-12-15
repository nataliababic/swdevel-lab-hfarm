# README by RAN Group

This file has the objective to explain in detail the project for Lab of Software Project Development, made by: Anna Citon (890729), Alessio Pitteri (888551), Lorenzo Paro (889505), Natalia Babic (890577) and Rachele Suardi (890590).
The project’s aim is to allow the user to analyse Bologna's tourist traffic in main squares and other places of interest. Indeed, the bologna.csv file provides information about the number of visitors depending on:
- the area: Due Torri, Facoltà di Giurisprudenza, Palazzo Poggi, Piazza Puntoni, Piazza Rossini, Piazza
  Scaravilli, Piazza Verdi, Porta San Donato, Via Del Guasto, and Via San Giacomo;
- the day: from July 2019 to April 2021;
- the stay time length, which varies from less than one minute to more than six hours. 

# Table of Content : 
- Flask and FastAPI Dockerized Project 
    - Architecture 
    - Communication 
    - Project Structure 

- Prerequisites and Installation 
    - Prerequisites 
    - Installation and configuration 
- Usage 
    - Usage of the backend
        - Cleaning 
        - Function 1
        - Function 2
        - Function 3
- Frontend 
    - Code 
    - Usage of the software 
- Backend testing 
    - Tests of the cleaning process
    - Tests of function 1
    - Tests of function 2
    - Tests of function 3
- Contributors 

# Flask and FastAPI Dockerized Project 
This project uses Flask as the frontend and FastAPI as the backend to develop a simple web project. The front end allows the user to retrieve information about the average number of visitors in Bologna based on three different functions, which are described below.

## Architecture
The project follows a simple client-server architecture.
1. ** Frontend (Flask) : **
    - It represents the user interface, the client side of the project. 
    - base.html: used to include libraries, stylesheets, and the navbar.
    - f1.html: used to define the page for the function 1 of the backend.
    - f2.html: used to define the page for the function 2 of the backend. 
    - f3.html: used to define the page for the function 3 of the backend.
    - index.html: used to define the homepage and to allow access to all other pages, mentioned above.
    - main.py: used as bridge to make the frontend and backend communicate; here all functions from the backend are recalled and results are returned, ready to be used in the html templates.
2. ** Backend (FastAPI) : **
    - It represents the server or backend of the application.
    - csv_cleaning.py : used to clean the main dataset and to add a column named “Holiday” that tells if a day is a working or a non-working day based on saturdays and sundays and on italian holidays.
    - function_1.py : used calculates the average number of visitors for a given area and stay time based on the provided traffic data.
    - function_2.py : used to calculate the average traffic for all areas, as well as the maximum and minimum traffic; provided a date
    - function_3.py : used to compute the average number of visitors given two different months, of the same year or even two different years.
3. ** Docker Compose : **
    - It serves the purpose of managing the backend and frontend together, and it also provides a tidy and equal working environment for all developers that want to reproduce or work on the project.

## Communication 
Bidirectional communication is established between the Frontend (Flask) and Backend (FastAPI). Docker Compose facilitates this communication, allowing the components to work together seamlessly.


## Project Structure 
- ‘backend/’: FastAPI backend implementation 
    - ‘App/’: folder that contains main.py and the folder for modules. 
    - ‘tests/‘: folder that contains the main tests files for the modules.
    - Dockerfile: Dockerfile for building the backend image.
    - requirements.txt: List of Python dependencies for the backend.
- ‘frontend/’: folder that contains Flask frontend implementation
    - ‘App/’: folder that contains main.py and the html templates.
    - Dockerfile: Dockerfile for building the frontend image. 
    - requirements.txt: List of Python dependencies for the frontend. 
- ‘Docker-compose.yml’: Docker compose configuration for running both frontend and backend. 

# Prerequisites and Installation

## Prerequisites 
The user should have Docker and Visual Studio Code installed. To proceed with the installation and configuration, the user should have the URL of the remote directory and Docker open on the machine. Finally, on Visual Studio Code the user should have installed the following extensions: Python, the Docker Extension and the Remote Development Tools.

##  Installation and configuration 

1. Clone the repository and navigate in the directory:

   ```bash
   git clone REPO_URL
   cd swdevel-lab-hfarm
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```
3. Open the "Docker" view in Visual Studio Code by clicking on the Docker icon in the Activity Bar.

4. Under "Containers," you should see your running containers. Right-click on the container running your Flask or FastAPI application.

5. Select "Attach Visual Studio Code" from the context menu for both containers.

6. Open the Run view in Visual Studio Code and select the "Python: Remote Attach" configuration in each container.

7. Click the "Run" button in each container. 

This will start both the frontend and backend containers and automatically install the required libraries such as pandas, FastAPI and Holidays.
  
> **NOTE:** Uncomment the lines in the Dockerfiles that follow the section labelled `Command to run the application` and comment out the ones labelled `Command to keep the container running`. This will allow you to access the backend and frontend, as described in Point 3.

8.  Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the `frontend` and [http://localhost:8081](http://localhost:8081) to access the `backend`.

9. Use the website on the frontend to query the functions in the backend.

# Usage 

## Usage of the backend

### Cleaning

####** Load Data**


This function loads data from a CSV file into a DataFrame


#### Parameters:


    - `file_path (str)` : the path to the CSV file.


#### Returns:


    - `dataFrame` : the loaded data from the CSV file.


#### Example Usage


Provide the file path to your CSV file with:
```file_path = "path/to/your/file.csv"```


Load data from the CSV file with:
```data = load_data(file_path)
print(data.head()) 
```


####** Save Data**


This function saves the modified DataFrame into a new CSV file


#### Parameters


    - `data (dataFrame)` : the DataFrame to be saved.
    - `output_file_path (str)` : the path where to save the file.


#### Example Usage


Assuming 'data' is your modified DataFrame select a file path:
```output_file_path = "path/to/save/your/file.csv"```


Save the modified DataFrame to a new CSV file:
```save_data(data, output_file_path)
print("Data saved successfully!")
```




####** Is Holiday**


A function that determines if the passed day is a working or a non-working day with respect to the Italian calendar.


#### Parameters


    - `date (datetime)` : the date as a datetime object.


#### Returns


    - `bool` : true if the date is a holiday or a weekend, false otherwise.


#### Example usage


Pass a date to check if it's a holiday or weekend
```date_to_check = datetime(25, 12, 2020) ```


Check if the date is a holiday or weekend in Italy:
```result = is_holiday(date_to_check)
print(result)
```




####** Preprocess Data**


    - Performs data preprocessing task:
    - Adding a Holiday column indicating where the date is a holiday or not.
    - Shift the Duration column to Visitors for data in the year 2021.
    - Shift Duration to 0 for data in the year 2021.


#### Parameters


    - `data (DataFrame)` : the input DataFrame.


#### Returns


    - `dataFrame` : the preprocessed DataFrame.


#### Example Usage


Assuming 'raw_data' is your original DataFrame:
```processed_data = preprocess_data(raw_data)
print(processed_data.head())
```




####** Convert to Minutes**


A function that converts strings containing the duration into minutes.


#### Parameters


    - `duration_str (str)` : the duration string.


#### Returns


    - `int` : the duration in minutes.
#### Example Usage


Pass a duration string to convert to minutes
```duration = "2 hours 30 minutes" ```


Convert the duration string to minutes
```result_minutes = convert_to_minutes(duration)
print(result_minutes)
```




####** Process Durata Columns**


A function that processes the Duration column to get the average duration in minutes.


#### Parameters


    - `data (DataFrame)` : the input DataFrame.


#### Returns


    - `DataFrame` : DataFrame with Duration column values converted to minutes.


#### Example Usage


Assuming 'data' is your DataFrame
```data_with_minutes = process_durata_column(data)
print(data_with_minutes.head())
```


