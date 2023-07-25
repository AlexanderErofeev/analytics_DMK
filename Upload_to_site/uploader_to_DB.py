import pandas as pd
from sqlalchemy import create_engine

# ENGINE = create_engine('mysql://user_for_django:%s@localhost:3306/test1' % quote('5678_@TL'))
ENGINE = create_engine('mysql://c21535_dmk_ai_info_ru:MoYzuQoxtecoh10@localhost:3306/c21535_dmk_ai_info_ru?charset=utf8mb4')  # ?charset=utf8mb4 для хостинга


dynamics_count_vacancies_to_DB = pd.read_csv('dynamics_count_vacancies_to_DB_id.csv')

dmk_countvacanciesperyear = pd.melt(dynamics_count_vacancies_to_DB, id_vars=['id'], var_name='year', value_name='count')
dmk_profession_count_vacancies = pd.concat([dmk_countvacanciesperyear['id'], pd.Series(range(1, len(dmk_countvacanciesperyear) + 1))], axis=1)
dmk_profession_count_vacancies.columns = ["profession_id", "countvacanciesperyear_id"]
dmk_countvacanciesperyear = dmk_countvacanciesperyear[['year', 'count']]
dmk_countvacanciesperyear['year'] = dmk_countvacanciesperyear['year'].apply(lambda x: int(x))

dmk_countvacanciesperyear.index += 1
dmk_profession_count_vacancies.index += 1
# dmk_countvacanciesperyear.to_csv("dmk_countvacanciesperyear.csv", index=True, index_label='id')
# dmk_profession_count_vacancies.to_csv("dmk_profession_count_vacancies.csv", index=True, index_label='id')

dmk_profession_count_vacancies.to_sql('DMK_profession_count_vacancies', if_exists="replace", con=ENGINE, index_label='id')
dmk_countvacanciesperyear.to_sql('DMK_countvacanciesperyear', if_exists="replace", con=ENGINE, index_label='id')


dynamics_salary_vacancies_to_DB = pd.read_csv('dynamics_salary_vacancies_to_DB_id.csv')

dmk_salaryperyear = pd.melt(dynamics_salary_vacancies_to_DB, id_vars=['id'], var_name='year', value_name='salary')
dmk_profession_salary = pd.concat([dmk_salaryperyear['id'], pd.Series(range(1, len(dmk_salaryperyear) + 1))], axis=1)
dmk_profession_salary.columns = ["profession_id", "salaryperyear_id"]
dmk_salaryperyear = dmk_salaryperyear[['year', 'salary']]
dmk_salaryperyear['year'] = dmk_salaryperyear['year'].apply(lambda x: int(x))

dmk_salaryperyear.index += 1
dmk_profession_salary.index += 1
# dmk_salaryperyear.to_csv("dmk_salaryperyear.csv", index=True, index_label='id')
# dmk_profession_salary.to_csv("dmk_profession_salary.csv", index=True, index_label='id')

dmk_profession_salary.to_sql('DMK_profession_salary', if_exists="replace", con=ENGINE, index_label='id')
dmk_salaryperyear.to_sql('DMK_salaryperyear', if_exists="replace", con=ENGINE, index_label='id')


soft_skill_stat_vacancies_to_DB = pd.read_csv('soft_skill_stat_vacancies_to_DB_id.csv', index_col='id')
soft_skill_ans = []
for pr_i in soft_skill_stat_vacancies_to_DB.index:
    for skill_i in soft_skill_stat_vacancies_to_DB.columns:
        soft_skill_ans.append((soft_skill_stat_vacancies_to_DB.loc[pr_i][skill_i], pr_i, skill_i))
pd.DataFrame(soft_skill_ans, index=range(1, len(soft_skill_ans) + 1), columns=['CountMentions', 'Profession_id', 'SoftSkill_id'])\
    .to_sql('DMK_countmentionsforsoftskill', if_exists="replace", con=ENGINE, index_label='id')

hard_skill_stat_vacancies_to_DB = pd.read_csv('hard_skill_stat_vacancies_to_DB_id.csv', index_col='id')
hard_skill_ans = []
for pr_i in hard_skill_stat_vacancies_to_DB.index:
    for skill_i in hard_skill_stat_vacancies_to_DB.columns:
        hard_skill_ans.append((hard_skill_stat_vacancies_to_DB.loc[pr_i][skill_i], pr_i, skill_i))
pd.DataFrame(hard_skill_ans, index=range(1, len(hard_skill_ans) + 1), columns=['CountMentions', 'Profession_id', 'Skill_id'])\
    .to_sql('DMK_countmentionsforskill', if_exists="replace", con=ENGINE, index_label='id')