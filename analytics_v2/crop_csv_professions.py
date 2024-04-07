import os
import pandas as pd
from global_settings_and_functions import *

OUT_FILE = 'vacancies.csv'
OLD_CSV_FILES = 'old_data/old_csv_files.csv'
OLD_IDS = 'old_data/old_ids.csv'
KEEP_COL = ['id', 'name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at']


def open_csv(file):
    return pd.read_csv(file, usecols=KEEP_COL)


def get_all_csv_in_dir(dir_path):
    file_mas = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.csv'):
                file_mas.append(f"{root}/{file}")
    return sorted(file_mas)


def filter_new_items(items, old_csv_file):
    old_csv_files = pd.read_csv(old_csv_file).iloc[:,0].to_list() if os.path.exists(old_csv_file) else []
    old_csv_files, items = set(old_csv_files), set(items)
    return list(sorted(items.difference(old_csv_files)))


def update_old_csv(new_items, old_csv_file):
    pd.DataFrame(new_items).to_csv(old_csv_file, mode='a', index=False, header=not os.path.exists(old_csv_file))


def crop_csv_professions(is_only_new_vacancies):
    files = sum_mas([get_all_csv_in_dir(dir_path) for dir_path in INPUT_DIRS])
    new_files = filter_new_items(files, OLD_CSV_FILES) if is_only_new_vacancies else files

    print_log(f"Reading from {', '.join(INPUT_DIRS)}")
    print_log(f"Count new files: {len(new_files)}")

    if len(new_files) == 0:
        return pd.DataFrame(columns=KEEP_COL)

    csv_list = multiprocessing_map(open_csv, new_files)
    print_log('Reading completed')

    csv_merged = pd.concat(csv_list, ignore_index=True, copy=False).reindex(columns=KEEP_COL)
    print_log(f"Count vacancies: {len(csv_merged.index)}")

    csv_merged = csv_merged.sort_values(by=['published_at']) \
        .drop_duplicates(subset=['id']) \
        .dropna(how='all')
    print_log(f"Count vacancies without duplicates: {len(csv_merged.index)}")

    new_ids = filter_new_items(csv_merged['id'].tolist(), OLD_IDS) if is_only_new_vacancies else csv_merged['id'].tolist()
    csv_merged = csv_merged[csv_merged['id'].isin(new_ids)]
    print_log(f"Count new vacancies: {len(csv_merged.index)}")

    update_old_csv(new_files, OLD_CSV_FILES)
    update_old_csv(new_ids, OLD_IDS)

    return csv_merged


if __name__ == '__main__':
    crop_csv_professions(is_only_new_vacancies=True).to_csv(OUT_FILE, index=False)
