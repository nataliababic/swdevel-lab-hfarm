"""
Frontend module for the Flask application.

This module defines a simple Flask application that serves as
the frontend for the project.
"""

# Import the Flask module for creating a web application
from flask import Flask, render_template, request

# Import the requests library to make HTTP requests
import requests

app = Flask(__name__)


# Define a route for the root URL ('/')
@app.route('/', methods=['GET'])
def index():
    '''
    Render the index page.

    Returns:
        str: Rendered HTML content for the index page.
    '''

    # OpenWeatherMap API URL for Bologna, Italy
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Bologna&units=metric&appid=89dc412be7a253069293a9414141eb5f'

    # Send a GET request to the OpenWeatherMap API
    response = requests.get(url)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to obtain weather data
        weather_data = response.json()

        # Extract temperature and current weather description from the response
        temperature = weather_data['main']['temp']
        current_description = weather_data['weather'][0]['description']

        # Render the index.html template with weather data
        return render_template('index.html',
                               temperature=temperature,
                               current_description=current_description,
                               weather_data=weather_data)
    else:
        # If there is an error in the API response, render only 'index.html'
        return render_template('index.html')


def getF1(param1, param2):
    '''
    Get data about the average number of visitors according to
    area and stay time from the backend API.

    Args:
        param1 (str): it corresponds to the area in the backend function.
        param2 (str): it corresponds to the stay time in the backend function.

    Returns:
        tuple: A tuple containing average total visitors,
        average holiday visitors, and average non-holiday visitors.
    '''

    # Construct the backend API URL with the provided parameters
    backend_url = "http://backend/average-visitors/" + param1 + "/" + param2

    # Send a GET request to the backend API
    response = requests.get(backend_url)

    # Raise an HTTPError for bad responses
    response.raise_for_status()

    # Extract average visitor data from the JSON response,
    # providing a notification if data is not available
    avg_total = response.json().get('avg_total',
                                    'Data not available')
    avg_holiday = response.json().get('avg_holiday',
                                      'Data not available')
    avg_non_holiday = response.json().get('avg_non_holiday',
                                          'Data not available')

    # Return a tuple containing average total, holiday,
    # and non-holiday visitors
    return avg_total, avg_holiday, avg_non_holiday


@app.route('/f1', methods=['GET', 'POST'])
def f1():
    '''
    Handle requests for the 'f1' route.

    If parameters 'param1' and 'param2' are set,
    retrieve data using the getF1 function.
    Render the 'f1.html' template with the obtained data.

    Returns:
        str: Rendered HTML content for the 'f1' route.
    '''
    avg_data = None
    # Check if 'param1' and 'param2' are set
    if request.args.get('param1') and request.args.get('param2'):
        # Call the getF1 function with provided parameters
        avg_data = getF1(request.args.get('param1'),
                         request.args.get('param2'))

    # Render the 'f1.html' template with the obtained data
    return render_template('f1.html', avg_data=avg_data,
                           area=request.args.get('param1'),
                           stay_time=request.args.get('param2'))


def getF2(param1):
    '''
    Get data about the average number of visitors on a specific day
    from the backend API.

    Args:
        param1 (str): it corresponds to target date in the backend function.

    Returns:
        tuple: A tuple containing affluence data for
        each area, highest affluence, and lowest affluence.
    '''

    # Construct the backend API URL with the provided parameter
    backend_url = "http://backend/forecasted-visitors/" + param1

    # Send a GET request to the backend API
    response = requests.get(backend_url)

    # Raise an HTTPError for bad responses
    response.raise_for_status()

    # Extract forecasted affluence data from the JSON response,
    # providing a notification if data is not available
    all_areas = response.json().get('Affluence of each area',
                                    'Data not available')
    max_affluence = response.json().get('Highest affluence',
                                        'Data not available')
    min_affluence = response.json().get('Lowest affluence',
                                        'Data not available')
    error = response.json().get('error', 'Data not available')

    # Return a tuple containing affluence data for
    # each area, highest affluence, and lowest affluence
    return all_areas, max_affluence, min_affluence, error


@app.route('/f2', methods=['GET', 'POST'])
def f2():
    '''
    Handle requests for the 'f2' route.

    If 'daySelection' is set, construct a parameter 'param3'
    based on the provided day and month.
    Call the getF2 function with the constructed parameter
    and retrieve the data.
    Render the 'f2.html' template with the obtained data.

    Returns:
        str: Rendered HTML content for the 'f2' route.
    '''
    affluence = None
    param3 = None
    # Check if 'daySelection' is set (the form requires both to be compiled)
    # So, if 'daySelection' is set, 'monthSelection' is also set
    if request.args.get('daySelection'):
        # Construct 'param3' based on the provided day and month
        if (int(request.args.get('daySelection')) < 10):
            if (int(request.args.get('monthSelection')) < 10):
                param3 = '0'+request.args.get('daySelection') + '-0' + request.args.get('monthSelection')
            else:
                param3 = '0' + request.args.get('daySelection') + '-' + request.args.get('monthSelection')
        else:
            if (int(request.args.get('monthSelection')) < 10):
                param3 = request.args.get('daySelection') + '-0' + request.args.get('monthSelection')
            else:
                param3 = request.args.get('daySelection') + '-' + request.args.get('monthSelection')

        # Call the getF2 function with the constructed parameter
        affluence = getF2(param3)

    # Render the 'f2.html' template with the obtained data
    return render_template('f2.html', affluence=affluence, target_date=param3)


def getF3(param1, param2, param3, param4):
    '''
    Get data about average number of visitors in two periods
    from the backend API.

    Args:
        param1 (str): it corresponds to first year in the backend function.
        param2 (str): it corresponds to first month in the backend function.
        param3 (str): it corresponds to second year in the backend function.
        param4 (str): it corresponds to second month in the backend function.

    Returns:
        tuple: A tuple containing average number of visitors for the first
        and second periods.
    '''

    # Construct the backend API URL with the provided parameters
    backend_url = "http://backend/average-period/" + param1 + "/" + param2 + "/" + param3 + "/" + param4

    # Send a GET request to the backend API
    response = requests.get(backend_url)

    # Raise an HTTPError for bad responses
    response.raise_for_status()

    # Extract average period data from the JSON response,
    # providing a notification if data is not available
    avg_firstperiod = response.json().get('Avg first period',
                                          'Data not available')
    avg_secondperiod = response.json().get('Avg second period',
                                           'Data not available')
    error = response.json().get('error', 'Data not available')
    # Return a tuple containing average data for the first and second periods
    return avg_firstperiod, avg_secondperiod, error


@app.route('/f3', methods=['GET', 'POST'])
def f3():
    '''
    Handle requests for the 'f3' route.

    If 'param4', 'param5', 'param6', and 'param7' are set, call
    the getF3 function with these parameters.
    Render the 'f3.html' template with the obtained average visitors data.

    Returns:
        str: Rendered HTML content for the 'f3' route.
    '''
    avg_visitors = None

    # Check if 'param4', 'param5', 'param6', and 'param7' are set
    if (request.args.get('param4') and request.args.get('param5') and request.args.get('param6') and request.args.get('param7')):
        # Call the getF3 function with the provided parameters
        avg_visitors = getF3(request.args.get('param4'),
                             request.args.get('param5'),
                             request.args.get('param6'),
                             request.args.get('param7'))

    # Render the 'f3.html' template with the obtained data
    return render_template('f3.html', avg_visitors=avg_visitors,
                           year1=request.args.get('param4'),
                           month1=request.args.get('param5'),
                           year2=request.args.get('param6'),
                           month2=request.args.get('param7'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
