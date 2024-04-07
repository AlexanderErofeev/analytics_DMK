from crop_csv_professions import crop_csv_professions
from preprocessing_professions import preprocessing_professions
from clustering_professions import clustering_professions
from classifying_skill import classifying_skill, classifying_grup_skill
from clustering_area_name import clustering_area_name
from global_settings_and_functions import *
from upload_to_api import upload_to_api


if __name__ == '__main__':
    print_log('Reading sources')
    df_vac = crop_csv_professions(is_only_new_vacancies=True)
    print_log('Preprocessing vacancies')
    df_vac = preprocessing_professions(df_vac)

    print_log('Classification vacancies')
    df_vac['profession_title'] = clustering_professions(df_vac['name'])
    df_vac = df_vac.drop('name', axis='columns')

    print_log('Classification skills')
    df_vac['key_skills'] = classifying_skill(df_vac['key_skills'])
    print_log('Classification grup skills')
    df_vac['grup_skills'] = classifying_grup_skill(df_vac['key_skills'])

    print_log('Classification area name')
    df_vac['area_name'] = clustering_area_name(df_vac['area_name'])

    print_log('Removing junk vacancies')
    df_vac = df_vac[~df_vac['profession_title'].isin(['Мусор', 'Неизвестная профессия'])]

    print_log(f'Save {len(df_vac.index)} vacancies')
    df_vac.to_csv('completed_analytics.csv', index=False)

    print_log('Upload to api')
    upload_to_api(df_vac)

    print_log('Analytics completed successfully')
