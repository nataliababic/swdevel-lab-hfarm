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


## Project Structure 
‘backend/’: FastAPI backend implementation 
‘App/’: folder that contains main.py and the folder for modules. 
‘tests/‘: folder that contains the main tests files for the modules.
Dockerfile: Dockerfile for building the backend image.
requirements.txt: List of Python dependencies for the backend.
‘frontend/’: folder that contains Flask frontend implementation
‘App/’: folder that contains main.py and the html templates.
Dockerfile: Dockerfile for building the frontend image. 
requirements.txt: List of Python dependencies for the frontend. 
‘Docker-compose.yml’: Docker compose configuration for running both frontend and backend. 

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

