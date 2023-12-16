# README by RAN Group

This file has the objective to explain in detail the project for Lab of Software Project Development, made by: Anna Citon (890729), Alessio Pitteri (888551), Lorenzo Paro (889505), Natalia Babic (890577) and Rachele Suardi (890590).
The project’s aim is to allow the user to analyse Bologna's tourist traffic in main squares and other places of interest. Indeed, the bologna.csv file provides information about the number of visitors depending on:
- the area: Due Torri, Facoltà di Giurisprudenza, Palazzo Poggi, Piazza Puntoni, Piazza Rossini, Piazza
  Scaravilli, Piazza Verdi, Porta San Donato, Via Del Guasto, and Via San Giacomo;
- the day: from July 2019 to April 2021;
- the stay time length, which varies from less than one minute to more than six hours. 

# Table of Contents: 
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
    - ‘tests/’: folder that contains the main tests files for the modules.
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

This will start both the frontend and backend containers and automatically install the required libraries such as pandas and Holidays.
  
> **NOTE:** Uncomment the lines in the Dockerfiles that follow the section labelled `Command to run the application` and comment out the ones labelled `Command to keep the container running`. This will allow you to access the backend and frontend, as described in Point 3.

8.  Open your web browser and navigate to [http://localhost:8080](http://localhost:8080) to access the `frontend` and [http://localhost:8081](http://localhost:8081) to access the `backend`.

9. Use the website on the frontend to query the functions in the backend.



# Usage 

## Usage of the backend

### Cleaning

#### __Load Data__
This function loads data from a CSV file into a DataFrame.

##### Parameters
- `file_path (str)` : the path to the CSV file.

##### Returns
- `DataFrame` : the loaded data from the CSV file.

##### Example Usage
Provide the file path to your CSV file with:
```file_path = "path/to/your/file.csv"```

Load data from the CSV file with:
```python
data = load_data(file_path)
print(data.head()) 
```


#### __Save Data__
This function saves the modified DataFrame into a new CSV file.

##### Parameters
- `data (DataFrame)` : the DataFrame to be saved.
- `output_file_path (str)` : the path where to save the file.

##### Example Usage

Assuming 'data' is your modified DataFrame, select a file path:
```output_file_path = "path/to/save/your/file.csv"```

Save the modified DataFrame to a new CSV file:
```python
save_data(data, output_file_path)
print("Data saved successfully!")
```


#### __Is Holiday__
A function that determines if the passed day is a working or a non-working day with respect to the Italian calendar.

##### Parameters
- `date (datetime)` : the date as a datetime object.

#### Returns
- `bool` : true if the date is a holiday or a weekend, false otherwise.

##### Example usage
Pass a date to check if it's a holiday or weekend
```date_to_check = datetime(25, 12, 2020) ```

Check if the date is a holiday or weekend in Italy:
```python
result = is_holiday(date_to_check)
print(result)
```


#### __Preprocess Data__
Performs a data preprocessing task:
- Adding a Holiday column indicating where the date is a holiday or not.
- Shifting the Duration column to Visitors for data in the year 2021.
- Shifting Duration to 0 for data in the year 2021.

##### Parameters
- `data (DataFrame)` : the input DataFrame.

##### Returns
- `dataFrame` : the preprocessed DataFrame.

##### Example Usage
Assuming 'raw_data' is your original DataFrame:
```python
processed_data = preprocess_data(raw_data)
print(processed_data.head())
```


#### __Convert to Minutes__
A function that converts strings containing the duration into minutes.

##### Parameters
- `duration_str (str)` : the duration string.

##### Returns
- `int` : the duration in minutes.

##### Example Usage
Pass a duration string to convert to minutes
```duration = "2 hours 30 minutes" ```

Convert the duration string to minutes
```python
result_minutes = convert_to_minutes(duration)
print(result_minutes)
```


#### __Process Durata Columns__
A function that processes the Duration column to get the average duration in minutes.

##### Parameters
- `data (DataFrame)` : the input DataFrame.

##### Returns
- `DataFrame` : DataFrame with Duration column values converted to minutes.

##### Example Usage
Assuming 'data' is your DataFrame
```python
data_with_minutes = process_durata_column(data)
print(data_with_minutes.head())
```


### Function 1: What are the average stay lengths in each area? 
This backend function calculates the average number of visitors for a given area and stay time based on the provided traffic data.

#### Parameters:
- `df` (DataFrame): The input DataFrame containing traffic data.
- `area` (str): The specific area for which to calculate the average stay length.
- `stay_time` (str): The duration range for which to calculate the average stay length.

#### Returns:
- `tuple`: A tuple containing the average total visitors, average visitors on holidays, and average visitors on non-holidays. If the area or stay time is invalid, the function returns an appropriate error message.

#### Example Usage:
```python
# Import necessary libraries and modules
from your_module import calculate_average_visitors
# Load your DataFrame (df) with traffic data

# Example input
result = average_stay_length(df, “Palazzo Poggi, "From “5 to 10 min”)
print(result)

# Example output
# (avg_tot, avg_holiday, avg_non_holiday)
(383, 28, 537)
```

### Function 2 : What is the average number of visitors per area on a specific date? 
This second backend function is used to compute the average number of visitors in a specified date, as well as the maximum and minimum number of visitors from output. 
This function is composed by 3 different functions: 

#### traffic_per_area
- **Parameters**: 
    - `Traffic` (DataFrame): The input DataFrame containing traffic data.
    - `Target_date` (str): dd-mm chosen by the client 

- **Returns**: 
    - `Result` (DataFrame): DataFrame with the total visitors per area expected for the target date. 
    - `Result` (str): it returns "No data available for the given date." in case the date is not available or wrongly written. 

#### highest_affluence 
- **Parameters**: 
    - `Result` (DataFrame):  the total visitors per area Fataframe created in traffic_per_area function

- **Returns**: 
    - string with the area with the maximum amount of visitors

#### lowest_affluence
- **Parameters**: 
    - `Result` (DataFrame):  the total visitors per area Fataframe created in traffic_per_area function

- **Returns**: 
    - string with the area with the minimum amount of visitors

#### Example Usage
```python
# Import necessary libraries and modules
from your_module import traffic_per_area, highest_affluence, lowest_affluence 
# Load your DataFrame (traffic) with traffic data

# Example input
Result =  traffic_per_area (traffic, "01-10")
print (result, “\n”,highest_affluence(result), “\n”, lowest_affluence(result))
```

**Example output**
```
Area                                                       Forecasted_Visitors 
2 Torri (Inizio Portico Via Zamboni)                              1462
Facoltà di Giurisprudenza                                         1616
Palazzo Poggi                                                     1407
Piazza Puntoni (Via Zamboni)                                       679 
Piazza Rossini (Palazzo Malvezzi)                                 1834
Piazza Scaravilli                                                 1174
Piazza Verdi                                                      2071
Porta San Donato                                                  2546
Via Del Guasto                                                     821
Via San Giacomo                                                   1735
The Area with the highest tourism affluence is Porta San Donato with 2546 Forecasted Visitors 
The Area with the lowest tourism affluence is Piazza Puntoni ( Via Zamboni ) with 679 Forecasted Visitors 
```


### Function 3: what is the average number of visitors given two periods?

#### Parameters:
- `df` (DataFrame): The input DataFrame containing traffic data.
- `year1` (str): The first year for which to choose the month to select the first period.
- `month1` (str): The first month for which to compute the average number of visitors.
- `year2` (str): The second year for which to choose the month to select the second period.
- `month2` (str): The second month for which to compute the average number of visitors.

#### Returns:
- `(avg_visitors1, avg_visitors2)`: A tuple containing two integers, representing respectively the average number of visitors for the first and for the second period. 

#### Example Usage:
```python
# Import necessary libraries and modules
from your_module import avg_comparison

# Load your DataFrame (df) with traffic data

# Example usage
result = avg_comparison(df, “2019”, “07”, “2021”, “04”)
print(result)

# Example output
# (avg_visitors1, avg_visitors2)
(961, 4681)
```

##  Frontend

### Code
The main functionality of the frontend code is to create three functions that directly recall the respective functions defined in the backend, verifying first that the link is available and, if so, saving the returned data. Then, such results are passed to the HTML templates. Three of the templates are dedicated to use each of the functionalities offered by the software, i.e. `f1.html`, `f2.html`, `f3.html`, whereas `base.html` is used to define some stylesheets, to import libraries, etc. Additionally, `index.html` is used to define the core of the software, which is the homepage the user first sees when they access the website: here the weather API and the images have been added. From here linkages, through buttons, are available for the user to navigate to the pages described above. More in particular, such three templates each allow the user to access a form: each form allows to only select specific input, i.e. validates it, to limit the errors that could occur from an inappropriate input being sent. 
Bootstrap has been used to enhance the graphics and visual appeal of the website. 

### Usage of the software
Upon loading the homepage, the user receives information about the weather in the city of Bologna with temperature, description of the weather, wind speed, humidity and, in the event of rain, the mm of rain that has fallen, as well as four pictures that best represent the type of city Bologna is. The user is also able to use three buttons that specifically refer to the three functions made in the backend, and will redirect the user to a dedicated page. These buttons are:

- Average number of visitors by area and stay time
- Average number of visitors by date
- Comparison of number of visitors between two periods

In each dedicated function page, the user will be able to select, from a form selector, respectively the area and staytime, the target date, or the periods for comparison of which they want information about, and the website will provide the results immediately below the form, after communicating with the functions made in the backend.


# Backend testing
To ensure the correctness and reliability of the backend functions, a suite of tests has been developed using the ‘unittest’ and ‘pytest’ frameworks. These tests cover various scenarios and input cases to validate the functionality. 

## Tests of the cleaning process
To run the tests, navigate to the root directory of your project and execute the following command:

```bash
pytest tests/test_csv_cleaning.py
```

### Test cases:
- `test_load_data_smoke`: tests basic functionality for loading data from a CSV file into a Pandas DataFrame.
- `test_save_data_smoke`: checks the basic functionality of saving a DataFrame into a new CSV file.
- `test_is_holiday`: validates if specific dates are identified correctly as holidays or weekends.
- `test_is_italian_holiday`: verifies the identification of known Italian holidays for specific years.
- `test_is_not_holiday`: checks if provided weekdays (non-holidays) are correctly identified.
- `test_invalid_input_is_holiday`: ensures the function returns 'False' for invalid inputs to check holidays.
- `test_is_holiday_with_zero`: checks that if the value 0 is passed to the function it is properly handled.
- `test_is_holiday_with_none`: checks that if the value None is passed to the function it is properly handled.  
- `test_preprocess_data_smoke`: tests the preprocessing function to ensure the presence of required columns in the output DataFrame.   
- `test_convert_to_minutes_with_hours`: validates the conversion of duration strings in hours to minutes.   
- `test_convert_to_minutes_with_minutes`: checks the conversion of duration strings in minutes to minutes (no change).  
- `test_convert_to_minutes_with_empty_string`: tests the conversion of an empty duration string.   
- `test_convert_to_minutes_without_numbers`: verifies the behaviour of the conversion function with duration strings not containing any numbers.
- `test_process_durata_column_smoke`: validates the functionality of processing the 'Duration' column to ensure the presence and type of converted values in minutes.


## Tests of function 1
To run the tests, navigate to the root directory of your project and execute the following command:

```bash
python -m unittest test_funct1.py
```

### Test Cases:
TestAverageStayLength: this test class includes test cases for the average_stay_length function in the funct1 module.
- `test_average_stay_length_valid`: Test with a valid area and stay time.
- `test_average_stay_length_invalid_area`: Test with an invalid area.
- `test_average_stay_length_no_records`: Test with an area and stay time where no records are found.
- `test_average_stay_length_invalid_time`: Test with a valid area and an invalid duration.

TestConvertToMinutes: this test class includes test cases for the convert_to_minutes function in the csv_cleaning module.
- `test_convert_to_minutes_valid`: Test with a valid duration string.
- `test_convert_to_minutes_invalid_format`: Test with an invalid duration string format.


## Tests of function 2
To run the tests, navigate to the root directory of your project and execute the following command:

```bash
python -m unittest test_funct2.py
```

### Test Cases:
TestCall: this test class includes test cases for functions traffic_per_area, highest_affluence and lowest_affluence in the funct2 module.
- `test_traffic_per_area`: test traffic_per_area function with a valid date 
- `test _highest_affluence` : test highest_affluence with a valid date 
- `test _lowest_affluence` : test lowest_affluence with a valid date 
- `test_invalid_date` : test traffic_per_are function in case an invalid date is chosen


## Tests of function 3
To run the tests, navigate to the root directory of your project and execute the following command:

```bash
python -m unittest test_funct3.py
```

### Test Cases:
Test_avg_comparison: this test class includes all test cases for the function avg_comparison in the funct3 module.
- `test_average`: test the avg_comparison function with valid input
- `test_invalid_input`: test avg_comparison with invalid input types
- `test_years_unavailable`: test avg_comparison with both years unavailable
- `test_year1_unavailable`: test avg_comparison with the first year unavailable
- `test_year2_unavailable`: test avg_comparison with the second year unavailable
- `test_months_unavailable`: test avg_comparison with both months unavailable independently from the chosen years
- `test_month1_unavailable`: test avg_comparison with the first month unavailable independently from the chosen years
- `test_month2_unavailable`: test avg_comparison with the second month unavailable independently from the chosen years
- `test_months_not_for_years_selected`: test avg_comparison with both months not available for the chosen years
- `test_month1_not_for_year1_selected`: test avg_comparison with the first month not available for the first chosen year
- `test_month2_not_for_year2_selected`: test avg_comparison with the second month not available for the second chosen year.


## Tests of Main
To run the tests, navigate to the root directory of your project and execute the following command:

```bash
pytest tests/test_main.py
```

### Test cases:
- `test_read_main`: Tests the read_main endpoint for expected JSON response and status code.
- `test_make_average_smoke`: Validates the make_average endpoint's response with mock parameters.
- `test_forecasted_visitors_per_area_smoke`: Checks the forecasted_visitors_per_area endpoint for response status.
- `test_average_comparison_smoke`: Ensures the average_comparison endpoint responds with status code 200.
- `test_make_average`: Validates the make_average endpoint for expected output with specific parameters.
- `test_forecasted_visitors_per_area`: Checks if forecasted_visitors_per_area endpoint returns areas and 200 status.
- `test_average_comparison`: Tests average_comparison endpoint for correct average values and status code 200.
- `test_make_average_error_handling`: Verifies error handling in make_average function for raising HTTPException.
- `test_forecasted_visitors_error_handling`: Checks error handling in forecasted_visitors_per_area for HTTPException.



