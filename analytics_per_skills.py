import pandas as pd
from global_settings_and_functions import percent, sum_mas


def gen_prof_stat(key_skills):
    key_skills = key_skills.dropna().str.split('\n').tolist()
    count_vac_with_skills = len(key_skills)
    return pd.Series(sum_mas(key_skills))\
        .value_counts()\
        .head(20)\
        .apply(lambda x: percent(x, count_vac_with_skills))\
        .to_dict()\
        .items()


data = pd.read_csv('vacancies_and_skill_classified.csv', usecols=['key_skills', 'prof_name'], low_memory=False)

data = data.groupby(['prof_name'])

skills_stat = data.apply(lambda x: pd.Series(gen_prof_stat(x['key_skills']))).T

skills_stat.apply(lambda x: x.apply(lambda y: ' - '.join(y))).to_csv('Results\\skills_stat.csv', index=False)
