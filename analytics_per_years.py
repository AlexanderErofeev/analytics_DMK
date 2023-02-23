import pandas as pd

data = pd.read_csv('vacancies_classified.csv', usecols=['rub_salary', 'year', 'prof_name'])

data = data.groupby(['prof_name']) \
    .apply(lambda x: x.groupby(['year']))


count_stat = data.apply(lambda x: x.apply(lambda y: len(y)))\
    .fillna(0)\
    .convert_dtypes()

count_stat.to_csv('Results\\count_stat.csv')
print(count_stat.sum(axis=1).sum())

salary_stat = data.apply(lambda x: x.apply(lambda y: y['rub_salary'].median() if len(y['rub_salary'].dropna().index) != 0 else 0))\
    .fillna(0)\
    .apply(lambda x: x.apply(lambda y: int(y)))\
    .convert_dtypes()

salary_stat.to_csv('Results\\salary_stat.csv')
