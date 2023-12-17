# Import needed library
from fastapi import FastAPI

app = FastAPI()


# Define the traffic_per_area function linking the name of each area
# to the number of visitors on the input day.
def traffic_per_area(traffic, target_date):
    '''
    Get the total number of visitors per area for a given date.

    Args:
    data (DataFrame): The input DataFrame containing date, area, and visitors.
    target_date (str): The date in 'DD-MM' format.

    Returns:
    result (DataFrame): df with total visitors per area for the given date.
    '''

    # Format dates to compare them with target date
    formatted_dates = traffic['Date'].dt.strftime('%d-%m')

    # Check whether target date is in formatted dates
    if target_date in formatted_dates.values:  # .values returns array
        filtered_traffic = traffic[formatted_dates == target_date]

        # Calculate the mean visitors per area for the given date
        result = filtered_traffic.groupby('Area')['Visitors'].mean().round(decimals=0).astype(int).reset_index()
        result.columns = ['Area', 'Forecasted_Visitors']

        return result

    # Return a message in case the target date is not available
    else:
        return "No data available for the given date."


# Define the area with the highest affluence
def highest_affluence(result):
    '''
    Get the area with the maximum number of visitors for the target date.

    Args:
    Result (DataFrame), the total visitors per area Datarame
    created in traffic_per_area function

    Returns:
    the area with the maximum amount of visitors
    '''

    max_area_row = result.loc[result['Forecasted_Visitors'].idxmax()]
    max_area = max_area_row['Area']
    mean_visitors = max_area_row['Forecasted_Visitors']

    return 'The Area with the highest tourism affluence is {} with {} Forecasted Visitors'.format(max_area, mean_visitors)


# Define the area with lowest affluence
def lowest_affluence(result):
    '''
    Get the area with the minimum number of visitors for the target date.

    Args:
    Result (DataFrame), the total visitors per area Dataframe
    created in traffic_per_area function

    Returns:
    the area with the minimum amount of visitors
    '''

    min_area_row = result.loc[result['Forecasted_Visitors'].idxmin()]
    min_area = min_area_row['Area']
    mean_visitors = min_area_row['Forecasted_Visitors']

    return 'The Area with the lowest tourism affluence is {} with {} Forecasted Visitors'.format(min_area, mean_visitors)
