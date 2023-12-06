import pandas as pd
from datetime import datetime
'''
data = pd.read_csv("/app/app/updated_bologna.csv")

years = ['2019', '2020', '2021']
dates = data['Date']

months2019=[]
months2020=[]
months2021=[]
for year in years:
    for date_str in dates:
        if date_str[-4:] == year:
            if year=='2019':
                    months2019 = months2019 + [date_str[3:5]]
            elif year=='2020':
                    months2020 = months2020 + [date_str[3:5]]
            elif year=='2021':
                months2021 = months2021 + [date_str[3:5]]
print(sorted(list(set(months2019))), sorted(list(set(months2020))), sorted(list(set(months2021))))
'''

def avg_comparison(data, year1, month1, year2, month2):
    filtered_dates=[]
    for elem in data['Date']:
        filtered_dates=filtered_dates+[elem[-7:]]
    data['filtered_dates']=pd.Series(filtered_dates)
    #print(data)
    avg_visitors1 = int(data[data['filtered_dates'] == f'{month1}/{year1}']['Visitors'].mean())
    avg_visitors2 = int(data[data['filtered_dates'] == f'{month2}/{year2}']['Visitors'].mean())
    #print(avg_visitors1)
    #print(avg_visitors2)
    return (avg_visitors1, avg_visitors2)
avg_comparison('2019', '07', '2021', '04')

