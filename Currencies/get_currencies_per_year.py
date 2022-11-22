import pandas as pd

mas = []
for year in range(2003, 2023):
    print(year)
    for month in range(1, 13 if year != 2022 else 10):
        url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{'{:02}'.format(month)}/{year}&d=0"
        df = pd.read_xml(url, encoding='cp1251')[['CharCode', 'Nominal', 'Value']]

        df = df[df['CharCode'].isin(['USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR', 'AZN', 'UZS', 'KGS', 'GEL'])]
        df['Value'] = df['Value'].apply(lambda y: float(y.replace(',', '.')))
        ser = pd.concat([pd.Series([f"{year}-{'{:02}'.format(month)}"]), round(df['Value'] / df['Nominal'], 8)])
        a = df['CharCode'].tolist()
        a.insert(0, 'date')
        ser.index = a
        mas.append(ser.to_frame().T)

pd.concat(mas).to_csv("currency_per_year.csv", index=False)
