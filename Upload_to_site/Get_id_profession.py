import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote


# ENGINE = create_engine('mysql://user_for_django:%s@localhost:3306/test1' % quote('5678_@TL'))
ENGINE = create_engine('mysql://c21535_dmk_ai_info_ru:MoYzuQoxtecoh10@localhost:3306/c21535_dmk_ai_info_ru?charset=utf8mb4')  # ?charset=utf8mb4 for hosting


dmk_professions = pd.read_sql_table('DMK_profession', ENGINE.connect(), columns=["id"], index_col='title')["id"].to_dict()
dmk_hard_skill = pd.read_sql_table('DMK_skill', ENGINE.connect(), columns=["id"], index_col='title')["id"].to_dict()
dmk_soft_skill = pd.read_sql_table('DMK_softskill', ENGINE.connect(), columns=["id"], index_col='title')["id"].to_dict()


dynamics_count_vacancies_to_DB = pd.read_csv('dynamics_count_vacancies_to_DB.csv', index_col='name')
dynamics_count_vacancies_to_DB.index = [dmk_professions[i] for i in dynamics_count_vacancies_to_DB.index.tolist()]
dynamics_count_vacancies_to_DB.to_csv('dynamics_count_vacancies_to_DB_id.csv', index_label='id')

dynamics_salary_vacancies_to_DB = pd.read_csv('dynamics_salary_vacancies_to_DB.csv', index_col='name')
dynamics_salary_vacancies_to_DB.index = [dmk_professions[i] for i in dynamics_salary_vacancies_to_DB.index.tolist()]
dynamics_salary_vacancies_to_DB.to_csv('dynamics_salary_vacancies_to_DB_id.csv', index_label='id')


skill_stat_vacancies_to_DB = pd.read_csv('skill_stat_vacancies_to_DB.csv', index_col='name')
skill_stat_vacancies_to_DB.index = [dmk_professions[i] for i in skill_stat_vacancies_to_DB.index.tolist()]

soft_skill_stat_vacancies_to_DB = skill_stat_vacancies_to_DB[list(dmk_soft_skill.keys())]
soft_skill_stat_vacancies_to_DB.columns = [dmk_soft_skill[i] for i in soft_skill_stat_vacancies_to_DB.columns.tolist()]
soft_skill_stat_vacancies_to_DB.to_csv('soft_skill_stat_vacancies_to_DB_id.csv', index_label='id')

hard_skill_stat_vacancies_to_DB = skill_stat_vacancies_to_DB[list(dmk_hard_skill.keys())]
hard_skill_stat_vacancies_to_DB.columns = [dmk_hard_skill[i] for i in hard_skill_stat_vacancies_to_DB.columns.tolist()]
hard_skill_stat_vacancies_to_DB.to_csv('hard_skill_stat_vacancies_to_DB_id.csv', index_label='id')