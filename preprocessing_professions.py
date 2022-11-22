import math
import pandas as pd
import re

csv_merged = pd.read_csv('vacancies.csv')
print(len(csv_merged.index))

# a = csv_merged[['salary_currency']]\
#     .drop_duplicates(subset=['salary_currency'], keep='first')\
#     .dropna()
# a['count'] = a['salary_currency'].apply(lambda x: len(csv_merged[csv_merged['salary_currency'] == x].index))
# print(a)
# print(a['salary_currency'].tolist())


def get_avg_salary(salary_from, salary_to):
    if not math.isnan(salary_from) and not math.isnan(salary_to):
        return int((float(salary_from) + float(salary_to)) / 2)
    elif not math.isnan(salary_from):
        return int(float(salary_from))
    elif not math.isnan(salary_to):
        return int(float(salary_to))
    else:
        return None


def converter_to_rubles(value, currency, date):
    if currency not in df_currency.columns or df_currency[currency][date] is None or math.isnan(df_currency[currency][date]):
        # print(currency + ' ' + date + ' - проблемы')
        return None
    else:
        return int(value * df_currency[currency][date])


def tested(ser):
    ser = ser.to_dict()
    return ser['salary_from'], ser['salary_to'], ser['salary_currency'], ser['published_at']


def rub_salary(ser):
    salary_from, salary_to, salary_currency, date = tested(ser)
    avg_salary = get_avg_salary(salary_to, salary_from)
    if avg_salary is not None and salary_currency is not None:
        if salary_currency == 'RUR':
            return avg_salary
        else:
            return converter_to_rubles(avg_salary, salary_currency, date)
    else:
        return None


# Переводим в нижний регистр, удаляем лишние символы у названий
csv_merged['name'] = csv_merged['name']\
    .str.lower()\
    .apply(lambda x: ' '.join(re.sub(r"[^\w+#]|[_023456789]", ' ', x).split()))  # r"[-_!/:();'\".,\\\[\]023456789«»–|—?&*]"

csv_merged = csv_merged[csv_merged['name'].str.len() != 0]
print(len(csv_merged.index))

csv_merged['published_at'] = csv_merged['published_at'].apply(lambda x: x[:7])

df_currency = pd.read_csv('Currencies\\currency_per_year.csv', index_col='date')
csv_merged['rub_salary'] = csv_merged.apply(rub_salary, axis=1)

csv_merged['year'] = csv_merged['published_at'].apply(lambda x: x[:4])
csv_merged[['name', 'rub_salary', 'year']].to_csv("vacancies_preprocessed.csv", index=False)

# print(len(csv_merged[['rub_salary']].dropna().index))
