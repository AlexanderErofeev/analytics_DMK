import pandas as pd
from global_settings_and_functions import sum_mas
from dict_skill import dict_skill


def gen_prof_stat(key_skills, skills_list):
    key_skills = key_skills.dropna().str.split('\n').tolist()
    skills_counts = pd.Series(sum_mas(key_skills), dtype='str').value_counts().to_dict()

    a = [skills_counts[skill] if skill in skills_counts else 0 for skill in skills_list]
    a = pd.Series(a)
    a.index = skills_list
    return a


def convert_ser_to_percens(ser):
    sum = ser.sum()
    return ser.apply(lambda el: round(el / sum, 4) if el != 0 else 0)


def get_skills_stat(data):
    data = data.groupby(['prof_name'])
    skills = sum_mas([list(dict.keys()) for dict in dict_skill.values()])

    skills_stat = data.apply(lambda x: gen_prof_stat(x['key_skills'], skills)).T
    skills_stat['sum'] = skills_stat.sum(axis=1)
    skills_stat = skills_stat.sort_values(by='sum', ascending=False)
    return skills_stat.apply(convert_ser_to_percens)


def get_grups_skill_stat(data):
    data = data.groupby(['prof_name'])
    grups_skill = list(dict_skill.keys())

    skills_grup_stat = data.apply(lambda x: gen_prof_stat(x['grup_skills'], grups_skill)).T
    skills_grup_stat['sum'] = skills_grup_stat.sum(axis=1)
    skills_grup_stat = skills_grup_stat.sort_values(by='sum', ascending=False)
    return skills_grup_stat.apply(convert_ser_to_percens)


if __name__ == '__main__':
    data = pd.read_csv('vacancies_and_skill_classified.csv', usecols=['key_skills', 'grup_skills', 'prof_name', 'year'], low_memory=False)

    get_skills_stat(data).to_csv('Results\\skills_stat.csv', index_label='Skill')
    get_grups_skill_stat(data).to_csv('Results\\grup_skills_stat.csv', index_label='Группа скиллов')

    data = data.groupby(['prof_name']).apply(lambda x: x.groupby(['year']))

    data_skills = data\
        .apply(lambda x: x.apply(lambda y: convert_ser_to_percens(gen_prof_stat(y['key_skills'], skills))))\
        .apply(lambda x: pd.melt(x.reset_index(), id_vars='year', var_name='key_skills', value_name='count'))

    pd.concat(data_skills.tolist(), keys=data_skills.index.tolist())\
        .reset_index(names=['prof_name', 'level_1']).drop(['level_1'], axis=1)\
        .reindex(columns=['prof_name', 'key_skills', 'year', 'count'])\
        .to_csv('Results\\skills_stat_per_year.csv', index=False)


    data_grup_skills = data\
        .apply(lambda x: x.apply(lambda y: convert_ser_to_percens(gen_prof_stat(y['grup_skills'], grups_skill))))\
        .apply(lambda x: pd.melt(x.reset_index(), id_vars='year', var_name='grup_skills', value_name='count'))

    pd.concat(data_grup_skills.tolist(), keys=data_grup_skills.index.tolist())\
        .reset_index(names=['prof_name', 'level_1']).drop(['level_1'], axis=1)\
        .reindex(columns=['prof_name', 'grup_skills', 'year', 'count'])\
        .to_csv('Results\\grup_skills_stat_per_year.csv', index=False)
