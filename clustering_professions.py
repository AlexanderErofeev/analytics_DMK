import numpy as np
import pandas as pd
import dict_words

vac_names_csv = pd.read_csv('vacancies_preprocessed_original.csv')


def percent(value, all):
    return str(round((value / all) * 100, 2)) + '%'


def define_prof(vac_name):
    for prof_name, plus_words in dict_words.plus_words.items():
        minus_words = dict_words.minus_words[prof_name]
        if any([plus_word in vac_name for plus_word in plus_words]) and \
                not any([minus_word in vac_name for minus_word in minus_words]):
            return prof_name
    return 'Неизвестная профессия'


vac_names_csv['prof_name'] = vac_names_csv['name'].apply(define_prof)
vac_names_csv.to_csv('vacancies_classified.csv', index=False)
print('Общее количество вакансий: ' + str(len(vac_names_csv.index)))

prof_groups_vac = vac_names_csv.groupby(['prof_name'])
print('Количество профессий: ' + str(len(prof_groups_vac) - 1))

undefined_vac = prof_groups_vac.get_group('Неизвестная профессия')[['name']]
print('Распределено вакансий: ' + percent(len(vac_names_csv.index) - len(undefined_vac.index), len(vac_names_csv.index)))
print('Количество неопределённых вакансий: ' + str(len(undefined_vac.index)))


count_prof_names = prof_groups_vac\
    .apply(lambda x: len(x.index))\
    .sort_values(ascending=False)

count_prof_names.to_csv("count_professions_names.csv", header=False)
print('Контрольная сумма вакансий: ' + str(count_prof_names.sum()))


def dict_to_list(dict):
    list_data = []
    for key, value in dict.items():
        list_data.append(' ')
        list_data.append(key)
        list_data.append(value)
    return list_data


def undefined_vac_with_word(word):
    df_ans = undefined_vac
    df_ans['bool'] = df_ans['name'].apply(lambda x: word in x)
    df_ans = df_ans[df_ans['bool'] == True].drop(columns=['bool'], axis=1)
    ser_ans = df_ans['name'].sort_values()
    return ser_ans


def frequency_words(series):
    words = ' '.join(series.tolist()).split()
    words = list(filter(lambda x: len(str(x)) > 1, words))
    words = pd.Series(np.array(words))
    words = words \
        .groupby(words) \
        .apply(lambda x: len(x.index)) \
        .sort_values(ascending=False)
    return words


def frequency_undefined_words(count, count_extra_words):   # Функции и их вызовы для эксперементов
    undefined_words = frequency_words(undefined_vac['name'])\
        .head(count)

    new_data = pd.Series(undefined_words.index)\
        .apply(lambda x: frequency_words(undefined_vac_with_word(x)).apply(lambda y: percent(y, undefined_words[x])).head(count_extra_words).to_dict())\
        .apply(dict_to_list)\
        .apply(lambda x: pd.Series(x, copy=False))
    new_data.index = undefined_words.index

    return pd.concat([pd.DataFrame(undefined_words), new_data], axis=1)


def vac_in_prof(prof_name):
    ser_ans = prof_groups_vac.get_group(prof_name)['name']
    ser_ans = ser_ans.sort_values()
    ser_ans.to_csv("Debug data\\vac_in_prof.csv", header=False, index=False)


def efficiency_plus_minus_words_in_prof(prof_name):
    plus_words = dict_words.plus_words[prof_name]
    minus_words = dict_words.minus_words[prof_name]

    vacancies = vac_names_csv['name'].tolist()
    plus_words_dict = {plus_word: len(list(filter(lambda x: plus_word in x, vacancies))) for plus_word in plus_words}

    filtered_vacancies = list(filter(lambda x: any([plus_word in x for plus_word in plus_words]), vacancies))
    minus_words_dict = {minus_word: len(list(filter(lambda x: minus_word in x, filtered_vacancies))) for minus_word in minus_words}

    pd.Series(plus_words_dict, dtype='int64')\
        .sort_values(ascending=False)\
        .to_csv("Debug data\\plus_words_in_prof.csv", header=False)

    minus_words_ser = pd.Series(minus_words_dict, dtype='int64').sort_values(ascending=False)
    minus_words_ser = pd.concat([minus_words_ser, minus_words_ser.apply(lambda x: percent(x, len(filtered_vacancies)))], axis=1)
    minus_words_ser.to_csv("Debug data\\minus_words_in_prof.csv", header=False)


frequency_undefined_words(30, 15).to_csv("Debug data\\frequency_undefined_words.csv", header=False)
# undefined_vac_with_word('разработчик').to_csv("Debug data\\castom_frequency.csv", header=False)
# vac_in_prof('Специалист')

# efficiency_plus_minus_words_in_prof('Мусор')
