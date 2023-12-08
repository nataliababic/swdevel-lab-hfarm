import pandas as pd
import sys
sys.path.append('/app') 
from app.mymodules.csv_cleaning import convert_to_minutes


# Mapping of duration strings to minutes
duration_mapping = {
    'From 5 to 10 min': (5, 10),
    'From 40 to 60 min': (40, 60),
    'From 3 to 4 hours': (180, 240),
    'From 4 a 6 Ore': (240, 360),
    'From 10 to 20 min': (10, 20),
    '20 40 min': (20, 40),
    'Meno di un min': (0, 1),
    'Da 1 a 5 min': (1, 5),
    'Da 60 a 90 min': (60, 90),
    '90 120 min': (90, 120),
    '+ 6 ore over 6 hours': (360, float('inf')),
    'From 2 to 3 hours': (120, 180)
}

def average_stay_length(df, area, stay_time):
    if area not in df['Area'].unique() and stay_time not in duration_mapping:
        return "Invalid Area and Duration"
    
    if area not in df['Area'].unique():
        return "Invalid Area"

    
    if stay_time not in duration_mapping:
        return "Invalid Duration"
    
    stay_minutes = convert_to_minutes(stay_time)

    filtered_df = df[df['Area'] == area]
    filtered_df = filtered_df[(filtered_df['Duration'] >= duration_mapping[stay_time][0]) & 
                               (filtered_df['Duration'] <= duration_mapping[stay_time][1])]

    if filtered_df.empty:
        return f"No records found for {area} with a stay time around {stay_minutes} minutes."

    avg_tot = int(filtered_df['Visitors'].mean())
    
    avg_holiday = int(filtered_df[filtered_df['Holiday']== True]['Visitors'].mean())
    avg_non_holiday = int(filtered_df[filtered_df['Holiday']== False]['Visitors'].mean())



    return (avg_tot, avg_holiday, avg_non_holiday)
