# README by RAN Group

This file has the objective to explain in detail the project for Lab of Software Project Development, made by: Anna Citon (890729), Alessio Pitteri (888551), Lorenzo Paro (889505), Natalia Babic (890577) and Rachele Suardi (890590).
The project’s aim is to allow the user to analyse Bologna's tourist traffic in main squares and other places of interest. Indeed, the bologna.csv file provides information about the number of visitors depending on:
the area: Due Torri, Facoltà di Giurisprudenza, Palazzo Poggi, Piazza Puntoni, Piazza Rossini, Piazza Scaravilli, Piazza Verdi, Porta San Donato, Via Del Guasto, and Via San Giacomo;
the day: from July 2019 to April 2021;
the stay time length, which varies from less than one minute to more than six hours. 

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
