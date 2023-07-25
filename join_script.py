from crop_csv_professions import crop_csv_professions
from preprocessing_professions import preprocessing_professions
from clustering_professions import clustering_professions
from classifying_skill import classifying_skill, classifying_grup_skill
from analytics_per_years import analytics_per_years
from analytics_per_skills import get_skills_stat
from Upload_to_site.Professions_tree import get_dynamics_count, get_dynamics_salary, get_skill_stat
from global_settings_and_functions import *


if __name__ == '__main__':
    print_log('Чтение исходников')
    df_vac = crop_csv_professions()
    print_log('Предобработка вакансий')
    df_vac = preprocessing_professions(df_vac)

    print_log('Классификация профессий')
    df_vac['prof_name'] = clustering_professions(df_vac['name'])
    df_vac.drop('name', axis='columns')

    print_log('Классификация скиллов')
    df_vac['key_skills'] = classifying_skill(df_vac['key_skills'])
    print_log('Классификация групп скиллов')
    df_vac['grup_skills'] = classifying_grup_skill(df_vac['key_skills'])

    print_log('Просчёт аналитики по годам')
    count_stat, salary_stat = analytics_per_years(df_vac)

    print_log('Просчёт аналитики по скиллам')
    skills_stat = get_skills_stat(df_vac)

    print_log('Оформление результатов аналитики')
    get_dynamics_count(count_stat).to_csv('Upload_to_site\\dynamics_count_vacancies_to_DB.csv', index_label='name')
    get_dynamics_salary(count_stat, salary_stat).to_csv('Upload_to_site\\dynamics_salary_vacancies_to_DB.csv', index_label='name')
    get_skill_stat(skills_stat).to_csv('Upload_to_site\\skill_stat_vacancies_to_DB.csv', index_label='name')

    print_log('Пересчёт аналитики успешно завершён')
