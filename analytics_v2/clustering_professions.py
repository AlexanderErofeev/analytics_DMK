import pandas as pd
import dict_words
from global_settings_and_functions import *


INPUT_FILE = 'vacancies_preprocessed.csv'
OUT_FILE = 'vacancies_classified.csv'
UNKNOWN_TITLE = 'Неизвестная профессия'


def is_tuple_in_str(tuple, str):
    if type(tuple).__name__ == 'list':
        return all([word in str for word in tuple])
    else:
        return tuple in str


def define_prof(vac_name):
    for prof_name, plus_words in dict_words.plus_words.items():
        minus_words = dict_words.minus_words[prof_name]
        if any([is_tuple_in_str(plus_word, vac_name) for plus_word in plus_words]) and \
                not any([minus_word in vac_name for minus_word in minus_words]):
            return prof_name
    return UNKNOWN_TITLE


def clustering_professions(vac_names):
    unique_vac_names = vac_names.drop_duplicates().tolist()
    unique_vac_values = list(map(define_prof, unique_vac_names))
    tr_dict = dict(zip(unique_vac_names, unique_vac_values))
    vac_prof = vac_names.apply(lambda x: tr_dict[x])

    if len(vac_prof.index) > 0:
        prof_value_counts = vac_prof.value_counts()
        # print_log(f"Count professions: {len(prof_value_counts) - 1}")

        undefined_vac_count = prof_value_counts[UNKNOWN_TITLE] if UNKNOWN_TITLE in prof_value_counts else 0
        # print_log(f"Distributed vacancies: {percent(len(vac_names) - undefined_vac_count, len(vac_names))}")
        # print_log(f"Count undefined vacancies: {undefined_vac_count}")
        # print_log(f"Checksum vacancies: {prof_value_counts.sum()}")

    return vac_prof


if __name__ == '__main__':
    vac_names_csv = pd.read_csv(INPUT_FILE, low_memory=False)
    print_log(f"Count vacancies: {len(vac_names_csv.index)}")

    vac_names_csv['profession_title'] = clustering_professions(vac_names_csv['name'])
    vac_names_csv = vac_names_csv.drop('name', axis='columns')
    vac_names_csv.to_csv(OUT_FILE, index=False)
