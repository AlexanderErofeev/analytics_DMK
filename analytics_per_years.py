import math

import pandas as pd

data = pd.read_csv('vacancies_classified.csv')

data = data.groupby(['prof_name']) \
    .apply(lambda x: x.groupby(['year']))

count_stat = data.apply(lambda x: x.apply(lambda y: len(y)))\
    .fillna(0)\
    .convert_dtypes()

count_stat.to_csv('Results\\count_stat.csv')
print(count_stat.sum(axis=1).sum())

salary_stat = data.apply(lambda x: x.apply(lambda y: y['rub_salary'].mean()))\
    .fillna(0)\
    .apply(lambda x: x.apply(lambda y: int(y)))\
    .convert_dtypes()

salary_stat.to_csv('Results\\salary_stat.csv')


