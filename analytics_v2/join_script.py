import multiprocessing
import pandas as pd
from crop_csv_professions import crop_csv_professions, get_chunks, filter_new_items, OLD_IDS, update_old_csv
from preprocessing_professions import preprocessing_professions
from clustering_professions import clustering_professions
from classifying_skill import classifying_skill, classifying_grup_skill
from clustering_area_name import clustering_area_name
from global_settings_and_functions import *
from upload_to_api import upload_to_api


def processing_chunk(chunk):
    print_log(f"processing finished for chank {chunk['index']}")
    df_vac = crop_csv_professions(chunk['chunk'])
    df_vac = preprocessing_professions(df_vac)

    df_vac['profession_title'] = clustering_professions(df_vac['name'])
    df_vac = df_vac.drop('name', axis='columns')

    df_vac['key_skills'] = classifying_skill(df_vac['key_skills'], df_vac['description'])
    df_vac['grup_skills'] = classifying_grup_skill(df_vac['key_skills'])
    df_vac = df_vac.drop(['description'], axis='columns')

    df_vac['area_name'] = clustering_area_name(df_vac['area_name'])

    df_vac = df_vac[~df_vac['profession_title'].isin(['Мусор', 'Неизвестная профессия'])]
    return df_vac


def main():
    chunks = get_chunks(PROCESSING_CHUNK_SIZE)

    data = []
    with multiprocessing.Pool(PROCESSOR_COUNT) as p:
        for result in p.imap_unordered(processing_chunk, chunks):
            if not result.empty:
                data.append(result)

    if len(data) == 0:
        print_log(f"No new files")
        return

    csv_merged = pd.concat(data, ignore_index=True, copy=False)
    print_log(f"Count vacancies: {len(csv_merged.index)}")

    csv_merged = csv_merged.sort_values(by=['date'])\
        .drop_duplicates(subset=['id'])
    print_log(f"Count vacancies without duplicates: {len(csv_merged.index)}")

    new_ids = filter_new_items(csv_merged['id'].tolist(), OLD_IDS) if IS_ONLY_NEW_VACANCIES else csv_merged['id'].tolist()
    csv_merged = csv_merged[csv_merged['id'].isin(new_ids)]
    print_log(f"Count new vacancies: {len(csv_merged.index)}")

    update_old_csv(new_ids, OLD_IDS)

    print_log(f'Save {len(csv_merged.index)} vacancies')
    csv_merged.to_csv('completed_analytics.csv', index=False)

    # print_log('Upload to api')
    # upload_to_api(df_vac)

    print_log('Analytics completed successfully')


if __name__ == '__main__':
    main()
