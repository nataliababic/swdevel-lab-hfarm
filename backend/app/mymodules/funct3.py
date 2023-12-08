import pandas as pd

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

def avg_comparison(df, year1, month1, year2, month2):
    #df = pd.read_csv("/app/app/updated_bologna.csv")
    #df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y', errors='coerce')
    
    avg_visitors1 = int((df[(df['Date'].dt.strftime('%m') == month1) & (df['Date'].dt.strftime('%Y') == year1)]['Visitors']).mean())
    avg_visitors2 = int((df[(df['Date'].dt.strftime('%m') == month2) & (df['Date'].dt.strftime('%Y') == year2)]['Visitors']).mean())
    #diff_perc = ((avg_visitors2 - avg_visitors1) / avg_visitors1) * 100
    return (avg_visitors1, avg_visitors2)
#avg_comparison('2019', '07', '2021', '04')