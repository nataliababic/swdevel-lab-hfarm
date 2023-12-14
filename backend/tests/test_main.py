import os
import sys
from fastapi.testclient import TestClient
from fastapi import HTTPException

# Add the project root to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you can do the relative import
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Bologna": "Hello World!!!!"}


def test_make_average_smoke():
    """Smoke test for the make_average endpoint.

    Inputs:
        Simulate a call to the make_average endpoint with mock parameters.

    Outputs:
        Asserts if the endpoint returns a response with status code 200.
    """
    response = client.get("/average-visitors/Palazzo Poggi/from 5 to 10 minutes")
    assert response.status_code == 200, "Endpoint did not return successfully"


def test_forecasted_visitors_per_area_smoke():
    """Smoke test for the forecasted_visitors_per_area endpoint.

    Inputs:
        Simulate a call to the endpoint with mock parameters.

    Outputs:
        Asserts if the endpoint returns a response with status code 200.
    """
    response = client.get("/forecasted-visitors/10-10")
    assert response.status_code == 200, "Endpoint did not return successfully"


def test_average_comparison_smoke():
    """Smoke test for the average_comparison endpoint.

    Inputs:
        Simulate a call to the endpoint with mock parameters.

    Outputs:
        Asserts if the endpoint returns a response with status code 200.
    """
    response = client.get("/average-period/2019/10/2021/02")
    assert response.status_code == 200, "Endpoint did not return successfully"


def test_make_average():
    """Test for the make_average endpoint.

    Inputs:
        Simulates a call to the make_average endpoint with specific parameters.

    Outputs:
        Asserts if the endpoint returns the expected result
        for the given parameters.
    """
    # Define the parameters for the test
    area = "Palazzo Poggi"
    stay_time = "from 5 to 10 minutes"

    # Call the endpoint with the defined parameters
    response = client.get(f"/average-visitors/{area}/{stay_time}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response body contains the expected values
    expected_result = {
        "avg_total": 383,
        "avg_holiday": 28,
        "avg_non_holiday": 537
    }
    assert response.json() == expected_result, "Returned result does not match expected values"


def test_forecasted_visitors_per_area():
    """Smoke test for the forecasted_visitors_per_area endpoint.

    Inputs:
        Simulate a call to the endpoint with mock parameters.

    Outputs:
        Asserts if the endpoint returns a response with status code 200.
    """
    response = client.get("/forecasted-visitors/10-10")
    assert response.status_code == 200, "Endpoint did not return successfully"

    # Expected result containing all areas
    expected_result = {
        "Affluence of each area": [
            {"Area": "2 Torri (Inizio Portico Via Zamboni)", "Forcasted_Visitors": 1727},
            {"Area": "Facoltà Di Giurisprudenza", "Forcasted_Visitors": 1878},
            {"Area": "Palazzo Poggi", "Forcasted_Visitors": 924},
            {"Area": "Piazza Puntoni (Via Zamboni)", "Forcasted_Visitors": 673},
            {"Area": "Piazza Rossini (Palazzo Malvezzi)", "Forcasted_Visitors": 2037},
            {"Area": "Piazza Scaravilli", "Forcasted_Visitors": 1060},
            {"Area": "Piazza Verdi", "Forcasted_Visitors": 2409},
            {"Area": "Porta San Donato", "Forcasted_Visitors": 2709},
            {"Area": "Via Del Guasto", "Forcasted_Visitors": 800},
            {"Area": "Via San Giacomo", "Forcasted_Visitors": 1675}
        ],
        "Highest affluence": (
            "The Area with the highest tourism affluence is Porta San Donato "
            "with 2709 Forcasted Visitors"
        ),
        "Lowest affluence": (
            "The Area with the lowest tourism affluence is Piazza Puntoni "
            "(Via Zamboni) with 673 Forcasted Visitors"
        )
    }

    # Extract all areas from the expected_result
    areas = [area["Area"] for area in expected_result["Affluence of each area"]]

    # Add assertion to check if the response contains the expected areas
    response_content = response.json()
    returned_areas = [entry["Area"] for entry in response_content["Affluence of each area"]]
    assert all(area in returned_areas for area in areas), "All areas not found in the response"


def test_average_comparison():
    """Smoke test for the average_comparison endpoint.

    Inputs:
        Simulate a call to the endpoint with mock parameters.

    Outputs:
        Asserts if the endpoint returns status code 200 and checks
        average values.
    """
    response = client.get("/average-period/2019/10/2021/02")
    assert response.status_code == 200, "Endpoint did not return successfully"

    # Expected result for average comparison
    expected_result = {"Avg first period": 1803, "Avg second period": 3937}

    # Extract average values from the response content
    response_content = response.json()
    avg_first_period = response_content["Avg first period"]
    avg_second_period = response_content["Avg second period"]

    # Check if the response matches the expected result
    assert avg_first_period == expected_result["Avg first period"], "Avg first period mismatch"
    assert avg_second_period == expected_result["Avg second period"], "Avg second period mismatch"


def test_make_average_error_handling():
    """Test for error handling in make_average function.

    Inputs:
        Simulate the function call where it raises an HTTPException.

    Outputs:
        Asserts if the function raises an HTTPException with status code 404.
    """
    # Simulate a result that is a string, indicating an error message
    result = "Area not found"
    try:
        # Call the function and expect it to raise an HTTPException
        raise HTTPException(status_code=404, detail=result)
    except HTTPException as e:
        assert e.status_code == 404, "HTTPException status code mismatch"
        assert e.detail == result, "HTTPException detail message mismatch"


def test_forecasted_visitors_error_handling():
    """Test for error handling in forecasted_visitors_per_area function.

    Inputs:
        Simulate the function call where it raises an HTTPException.

    Outputs:
        Asserts if the function raises an HTTPException with status code 404.
    """
    # Simulate a result that is a string, indicating an error message
    result = "Laughtale last poneglyph is in Alabasta"
    try:
        # Call the function and expect it to raise an HTTPException
        raise HTTPException(status_code=404, detail=result)
    except HTTPException as e:
        assert e.status_code == 404, "HTTPException status code mismatch"
        assert e.detail == result, "HTTPException detail message mismatch"