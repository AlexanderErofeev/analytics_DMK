import math
import os
import pandas as pd
import requests
from global_settings_and_functions import *


INPUT_FILE = 'completed_analytics.csv'
NOT_UPLOAD_IDS_FILE = 'not_upload_ids.csv'


def serialize_vacancy(row):
    vac = {
        'id': row['id'],
        'profession_title': row['profession_title'],
        'area_name': row['area_name'],
        'date': row['date'],
    }

    if not math.isnan(row['salary']):
        vac['salary'] = int(row['salary'])

    if type(row['key_skills']) == str and type(row['grup_skills']) == str:
        tuples_skills =  zip(row['key_skills'].split('\n'), row['grup_skills'].split('\n'))
        vac['skills'] = [{'title': title, 'group': group} for title, group in tuples_skills]

    return vac


def make_upload_request(vac_list):
    data = {
        'vacancies': vac_list
    }
    headers = {
        'Authorization': 'Bearer ...'
    }
    try:
        r = requests.post(UPLOAD_URL, json=data, headers=headers)
        if r.status_code == 200:
            print_log(f"Upload {len(vac_list)} vacancies")
            return len(vac_list)
        else:
            print_log(f"Ошибка {r.text}", is_error=True)
    except requests.exceptions.Timeout:
        print_log(f"Ошибка timeout", is_error=True)
    except requests.exceptions.ConnectionError:
        print_log(f"Ошибка connection", is_error=True)

    ids = [vac['id'] for vac in vac_list]
    pd.DataFrame(ids).to_csv(NOT_UPLOAD_IDS_FILE, mode='a', index=False, header=not os.path.exists(NOT_UPLOAD_IDS_FILE))
    return 0


def upload_to_api(df_vac):
    vac_chunks = [df_vac.iloc[i:i + UPLOAD_CHUNK_SIZE] for i in range(0, len(df_vac.index), UPLOAD_CHUNK_SIZE)]

    count_uploaded_vacancies = 0
    for vac_chunk in vac_chunks:
        vac_list = [serialize_vacancy(row) for index, row in vac_chunk.iterrows()]
        count_uploaded_vacancies += make_upload_request(vac_list)
    print_log(f"Upload finished {count_uploaded_vacancies} vacancies")


def main():
    upload_to_api(pd.read_csv(INPUT_FILE, low_memory=False))


if __name__ == '__main__':
    main()
