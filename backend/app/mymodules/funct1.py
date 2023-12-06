import pandas as pd
from app.mymodules.csv_cleaning import convert_to_minutes


def average_stay_length(df, area, stay_time):
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



    return (avg_tot, avg_holiday, avg_non_holiday)
