import pandas as pd
import datetime

now = datetime.datetime.now()
this_year = now.year
this_month = now.month
print(this_year)
print(this_month)

mas = []
for year in range(2003, this_year + 1):
    print(year)
    for month in range(1, 13 if year != this_year else this_month + 1):
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{'{:02}'.format(month)}/{year}&d=0"
        df = pd.read_xml(url, encoding='cp1251')[['CharCode', 'Nominal', 'Value']]

        df = df[df['CharCode'].isin(['USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR', 'AZN', 'UZS', 'KGS', 'GEL'])]
        df['Value'] = df['Value'].apply(lambda y: float(y.replace(',', '.')))
        ser = pd.concat([pd.Series([f"{year}-{'{:02}'.format(month)}"]), round(df['Value'] / df['Nominal'], 8)])
        a = df['CharCode'].tolist()
        a.insert(0, 'date')
        ser.index = a
        mas.append(ser.to_frame().T)
        print(f"{year}-{month}  {ser.tolist()}")

pd.concat(mas).to_csv("currency_per_year.csv", index=False)
