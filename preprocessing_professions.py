import math
import pandas as pd
import re
from global_settings_and_functions import *
from Currencies.get_currencies_per_year import update_currencies
import swifter
from swifter import set_defaults

pd.options.mode.chained_assignment = None
set_defaults(npartitions=PROCESSOR_COUNT * 2, progress_bar=False)


INPUT_FILE = 'vacancies.csv'
OUT_FILE = 'vacancies_preprocessed.csv'


def get_avg_salary(salary_from, salary_to):
    if not math.isnan(salary_from) and not math.isnan(salary_to):
        return int((float(salary_from) + float(salary_to)) / 2)
    elif not math.isnan(salary_from):
        return int(float(salary_from))
    elif not math.isnan(salary_to):
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
    print_log('Переводим в нижний регистр, удаляем лишние символы у названий')
    csv_merged['name'] = csv_merged['name']\
        .str.lower()\
        .apply(lambda x: ' '.join(re.sub(r"[^\w+#]|[_023456789]", ' ', x).split()))

    csv_merged = csv_merged[csv_merged['name'].str.len() != 0]
    print_log(f"Количество вакансий после удаления вакансий с пустыми \'name\': {len(csv_merged.index)}")

    csv_merged['key_skills'] = csv_merged['key_skills'].str.lower()
    csv_merged['published_at'] = csv_merged['published_at'].str[:7]

    print_log('Переводим зарплаты в рубли')
    df_currency = update_currencies()
    data_for_rub_salary = csv_merged[['salary_from', 'salary_to', 'salary_currency', 'published_at']]

    if IS_USES_MULTIPROCESSING:
        csv_merged['rub_salary'] = data_for_rub_salary \
            .swifter.allow_dask_on_strings().apply(lambda ser: rub_salary(ser, df_currency), axis=1)
    else:
        csv_merged['rub_salary'] = data_for_rub_salary.apply(lambda ser: rub_salary(ser, df_currency), axis=1)

    print_log(f"Количество вакансий с указанной ЗП: {csv_merged['salary_currency'].notna().sum()}")
    print_log(f"Количество вакансий с конвертированной в рубли ЗП: {csv_merged['rub_salary'].notna().sum()}")

    csv_merged['year'] = csv_merged['published_at'].str[:4]

    return csv_merged[['name', 'key_skills', 'rub_salary', 'year']]


if __name__ == '__main__':
    update_currencies()
    csv_merged = pd.read_csv(INPUT_FILE, low_memory=False)
    preprocessing_professions(csv_merged).to_csv(OUT_FILE, index=False)
