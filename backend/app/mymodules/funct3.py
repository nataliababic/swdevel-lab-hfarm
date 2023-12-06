import pandas as pd
from datetime import datetime

def attendance():
    data = pd.read_csv("/app/app/updated_bologna.csv")
    dates2020=data[data['Date'].str.endswith('2020')]
    dates2020['Date'] = pd.to_datetime(dates2020['Date'], format='%d/%m/%Y')

    year=input("Choose 2019 or 2021 as year to compare to 2020: ")
    year=int(year)

    if year != 2019 and year != 2021:
        print("Invalid input. Please enter a valid year.")
    
    elif year==2019:
        dates2019 = data[data['Date'].str.endswith('2019')]
        dates2019['Date'] = pd.to_datetime(dates2019['Date'], format='%d/%m/%Y')
        days_months2019 = set((date.day, date.month) for date in dates2019['Date'])
        matching2020 = [date for date in dates2020['Date'] 
                           if (date.day, date.month) in days_months2019]
        dates2020 = dates2020[dates2020['Date'].isin(pd.to_datetime(matching2020))]
        avg_visitors2019 = int(dates2019['Visitors'].mean())
        avg_visitors2020 = int(dates2020['Visitors'].mean())
        diff_perc = ((avg_visitors2019 - avg_visitors2020) / avg_visitors2020) * 100

        return avg_visitors2019, avg_visitors2020, diff_perc
        '''
        return f"The average number of visitors for the dates recorded in 2019
        was {avg_visitors2019}. \n The average number of visitors for the dates
        recorded in 2020 was {avg_visitors2020}. \n Given the same period, there
        was a decrease by {diff_perc}."
        '''
    
    elif year==2021:
        dates2021 = data[data['Date'].str.endswith('2021')]
        dates2021['Date'] = pd.to_datetime(dates2021['Date'], format='%d/%m/%Y')
        days_months2021 = set((date.day, date.month) for date in dates2021['Date'])
        matching2020 = [date for date in dates2020['Date'] 
                           if (date.day, date.month) in days_months2021]
        dates2020 = dates2020[dates2020['Date'].isin(pd.to_datetime(matching2020))]
        avg_visitors2021 = int(dates2021['Visitors'].mean())
        avg_visitors2020 = int(dates2020['Visitors'].mean())
        diff_perc = ((avg_visitors2021*100) / avg_visitors2020)

        return avg_visitors2021, avg_visitors2020, diff_perc
    
        '''
        return f"The average number of visitors for the dates recorded in 2020
        was {avg_visitors2020}. \n The average number of visitors for the dates
        recorded in 2021 was {avg_visitors2021}. \n Given the same period, there
        was an increase by {diff_perc}."
        '''





