import os
import pandas as pd
from global_settings_and_functions import *

OUT_FILE = 'vacancies.csv'
OLD_CSV_FILES = 'old_data/old_csv_files.csv'
OLD_IDS = 'old_data/old_ids.csv'

dtype = {
    'id': 'Int64',
    'name': 'string',
    'description': 'string',
    'key_skills': 'string',
    'salary_from': 'Int64',
    'salary_to': 'Int64',
    'salary_currency': 'string',
    'area_name': 'string',
    'published_at': 'string',
}

CHUNK_SIZE = 10000


def get_chunks(chunk_size: int):
    files = sum_mas([get_all_csv_in_dir(dir_path) for dir_path in INPUT_DIRS])
    new_files = filter_new_items(files, OLD_CSV_FILES) if IS_ONLY_NEW_VACANCIES else files

    print_log(f"Reading from {', '.join(INPUT_DIRS)}")
    print_log(f"Count new files: {len(new_files)}")
    print_log(f"Chunk size {chunk_size}")

    index = 0
    for file in new_files:
        with pd.read_csv(file, usecols=dtype.keys(), chunksize=chunk_size, dtype=dtype) as reader:
            for chunk in reader:
                index += 1
                yield {
                    'chunk': chunk,
                    'index': index,
                }

    update_old_csv(new_files, OLD_CSV_FILES)


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


def crop_csv_professions(chunk):
    csv_merged = chunk.sort_values(by=['published_at']) \
        .drop_duplicates(subset=['id']) \
        .dropna(how='all')

    return csv_merged


# if __name__ == '__main__':
#     # crop_csv_professions().to_csv(OUT_FILE, index=False)
#     chancs = get_chunks(100000)
#
#     print(chancs)
#
#     p = multiprocessing.Pool(processes=32)
#
#     data = p.imap(print, chancs)
#
#     p.close()
#     p.join()