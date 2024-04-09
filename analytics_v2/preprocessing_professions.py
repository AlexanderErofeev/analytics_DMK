import math
import pandas as pd
import re
from Currencies.get_currencies_per_year import update_currencies

pd.options.mode.chained_assignment = None

INPUT_FILE = 'vacancies.csv'
OUT_FILE = 'vacancies_preprocessed.csv'


def get_avg_salary(salary_from, salary_to):
    if salary_from is not pd.NA and salary_to is not pd.NA:
        return int((float(salary_from) + float(salary_to)) / 2)
    elif salary_from is not pd.NA:
        return int(float(salary_from))
    elif salary_to is not pd.NA:
        return int(float(salary_to))
    else:
        return None


def converter_to_rubles(value, currency, date, df_currency):
    if currency not in df_currency.columns or df_currency[currency][date] is None or math.isnan(df_currency[currency][date]):
        # print(currency + ' ' + date + ' - проблемы')
        return None
    else:
        return int(value * df_currency[currency][date])


def rub_salary(ser, df_currency):
    ser = ser.to_dict()
    salary_from, salary_to, salary_currency, date = ser['salary_from'], ser['salary_to'], ser['salary_currency'], ser['published_at']
    avg_salary = get_avg_salary(salary_to, salary_from)
    if avg_salary is not None and salary_currency is not None:
        if salary_currency == 'RUR':
            return avg_salary
        else:
            return converter_to_rubles(avg_salary, salary_currency, date, df_currency)
    else:
        return None


def preprocessing_professions(csv_merged):
    # print_log('Translate to lowercase and remove extra characters from names')

    csv_merged['name'] = csv_merged['name']\
        .str.lower()\
        .apply(lambda x: ' '.join(re.sub(r"[^\w+#]|[_023456789]", ' ', x).split()))

    csv_merged = csv_merged[csv_merged['name'].str.len() != 0]
    # print_log(f"Count vacancies after deleting vacancies with empty \'name\': {len(csv_merged.index)}")

    csv_merged['description'] = csv_merged['description'].str.lower()
    csv_merged['description'] = csv_merged['description'].str.replace(r"<[^>]+>", ' ', regex=True)
    csv_merged["description"] = csv_merged['description'].str.replace(r'[^\w\s+#-]|[_]', ' ', regex=True)
    csv_merged['description'] = csv_merged['description'].str.replace(r'[\s]+', ' ', regex=True)
    csv_merged['description'] = csv_merged['description'].str.strip()

    csv_merged['key_skills'] = csv_merged['key_skills'].str.lower()
    csv_merged['date'] = csv_merged['published_at'].str[:10]
    csv_merged['published_at'] = csv_merged['published_at'].str[:7]

    # print_log('Convert salary into rubles')
    df_currency = update_currencies()
    data_for_rub_salary = csv_merged[['salary_from', 'salary_to', 'salary_currency', 'published_at']]
    csv_merged['salary'] = data_for_rub_salary.apply(lambda ser: rub_salary(ser, df_currency), axis=1).astype('Int64')

    # print_log(f"Count vacancies with salary: {csv_merged['salary_currency'].notna().sum()}")
    # print_log(f"Count vacancies with salary converted into rubles: {csv_merged['salary'].notna().sum()}")

    return csv_merged.drop(['salary_from', 'salary_to', 'salary_currency', 'published_at'], axis='columns')


if __name__ == '__main__':
    csv_merged = pd.read_csv(INPUT_FILE, low_memory=False)
    preprocessing_professions(csv_merged).to_csv(OUT_FILE, index=False)
