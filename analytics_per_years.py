import pandas as pd


def analytics_per_years(data):
    data = data.groupby(['prof_name']).apply(lambda x: x.groupby(['year']))

    count_stat = data.apply(lambda x: x.apply(lambda y: len(y)))\
        .fillna(0)\
        .convert_dtypes()

    salary_stat = data.apply(lambda x: x.apply(lambda y: y['rub_salary'].median() if len(y['rub_salary'].dropna().index) != 0 else 0))\
        .fillna(0)\
        .apply(lambda x: x.apply(lambda y: int(y)))\
        .convert_dtypes()

    return count_stat, salary_stat


if __name__ == '__main__':
    df_vac = pd.read_csv('vacancies_classified.csv', usecols=['rub_salary', 'year', 'prof_name'])
    count_stat, salary_stat = analytics_per_years(df_vac)

    print(count_stat.sum(axis=1).sum())

    count_stat.to_csv('Results\\count_stat.csv')
    salary_stat.to_csv('Results\\salary_stat.csv')
