import os
import pandas as pd
from global_settings_and_functions import *

INPUT_FILES_DIR = 'HH'
OUT_FILE = 'vacancies.csv'

# KEEP_COL = ['name', 'description', 'key_skills', 'experience_id', 'premium', 'employer_name', 'salary_from', 'salary_to', 'salary_gross', 'salary_currency', 'area_name', 'published_at']
KEEP_COL = ['id', 'name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'published_at']


def open_csv(file):
    print_log(f"Чтение файла: {file}")
    return pd.read_csv(f"{INPUT_FILES_DIR}\\{file}", usecols=KEEP_COL)


def crop_csv_professions():
    file_list = [f for f in os.listdir(INPUT_FILES_DIR) if f.endswith('.csv')]

    csv_list = multiprocessing_map(open_csv, file_list)

    print_log('Чтение завершено')

    csv_merged = pd.concat(csv_list, ignore_index=True, copy=False).reindex(columns=KEEP_COL)
    print_log(f"Суммарное количество вакансий: {len(csv_merged.index)}")

    csv_merged = csv_merged.drop_duplicates(subset=['id']).dropna(how='all')
    print_log(f"Количество вакансий после удаления дубликатов: {len(csv_merged.index)}")

    return csv_merged.drop('id', axis='columns')


if __name__ == '__main__':
    crop_csv_professions().to_csv(OUT_FILE, index=False)

