import pandas as pd
from csv_cleaning import convert_to_minutes

df = pd.read_csv('app/updated_bologna.csv', parse_dates=['Date'])

def average_stay_length(area, stay_time):
    if area not in df['Area'].unique():
        return "Invalid Area"

    stay_minutes = convert_to_minutes(stay_time)

    filtered_df = df[df['Area'] == area]
    filtered_df = filtered_df[filtered_df['Duration'] == stay_minutes]

    if filtered_df.empty:
        return f"No records found for {area} with a stay time around {stay_minutes} minutes."

    avg_tot = int(filtered_df['Visitors'].mean())
    
    avg_holiday = int(filtered_df[filtered_df['Holiday']== True]['Visitors'].mean())
    avg_non_holiday = int(filtered_df[filtered_df['Holiday']== False]['Visitors'].mean())



    return f"The average number of visitors for {area} with a stay time around {stay_minutes} minutes is:\n- Total: {avg_tot}\n- Holiday: {avg_holiday}\n- Non-Holiday: {avg_non_holiday}"


# Displaying the list of available areas
area_list = df['Area'].unique()
print("Available Areas:")
for area in area_list:
    print(area)

# Taking user inputs
selected_area = input("Enter the area: ")
stay_time_input = input("Enter the desired stay time (e.g., 'from 5 to 10 min'): ")

# Calculating and printing the result
result = average_stay_length(selected_area, stay_time_input)
print(result)
