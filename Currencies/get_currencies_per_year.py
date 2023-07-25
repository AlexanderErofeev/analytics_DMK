import os
import pandas as pd
from global_settings_and_functions import *
from datetime import datetime
import pathlib

TARGET_CURRENCIES = ['USD', 'RUR', 'EUR', 'KZT', 'UAH', 'BYR', 'AZN', 'UZS', 'KGS', 'GEL']
SAVE_FILE = pathlib.Path(os.path.abspath(__file__)).parent / 'currency_per_year.csv'


def get_currencies_for_month(year_month):
    print_log(f"Получение курсов валют за {year_month}")
    year_month = year_month.split('-')
    year = year_month[0]
    month = year_month[1]

    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{month}/{year}&d=0"
    df_xml = pd.read_xml(url, encoding='cp1251')[['CharCode', 'Nominal', 'Value']]

    df_xml = df_xml[df_xml['CharCode'].isin(TARGET_CURRENCIES)]
    df_xml['Value'] = df_xml['Value'].apply(lambda y: float(y.replace(',', '.')))
    return pd.Series(data=round(df_xml['Value'] / df_xml['Nominal'], 8).to_dict().values(), index=df_xml['CharCode'])


def update_currencies():
    detes = pd.period_range(
        start=datetime(2003, 1, 1),
        end=datetime.now(),
        freq='M'
    ).strftime('%Y-%m').tolist()

    if os.path.exists(SAVE_FILE):
        old_currencies_df = pd.read_csv(SAVE_FILE, index_col='date')
    else:
        old_currencies_df = pd.DataFrame()

    available_months = old_currencies_df.index.tolist()
    target_months = list(sorted(set(detes) - set(available_months)))

    if len(target_months) > 0:
        print_log(f"Не хватает месяцев: {', '.join(target_months)}")
        new_currencies_df = pd.Series(target_months).apply(get_currencies_for_month)
    else:
        new_currencies_df = pd.DataFrame()
    new_currencies_df.index = target_months

    currencies_df = pd.concat([old_currencies_df, new_currencies_df]).sort_index()
    currencies_df.to_csv(SAVE_FILE, index_label='date')
    return currencies_df


if __name__ == '__main__':
    update_currencies()
