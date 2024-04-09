import pandas as pd
from dict_skill import dict_skill
from global_settings_and_functions import *


INPUT_FILE = 'vacancies_classified.csv'
OUT_FILE = 'vacancies_and_skill_classified.csv'
UNKNOWN_TITLE = 'Неизвестный навык'


def invert_dict(input_dict):
    ans_dict = {}
    for key, values in input_dict.items():
        ans_dict.update({value: key for value in values})
    return ans_dict


def define_skill(skill, definition_dict):
    if skill in definition_dict:
        return definition_dict[skill]
    else:
        return UNKNOWN_TITLE


def get_description_skills(description: str, solo_dict_skill):
    if description is pd.NA:
        return pd.NA

    description_split_set = set(description.split())
    ans_skills = []

    for skill, words in solo_dict_skill.items():
        for sub_words in words:
            if sub_words.issubset(description_split_set):
                ans_skills.append(skill)
                break

    return '\n'.join(ans_skills)


def define_vac_skills(list_skills, definition_dict, drop_duplicates=True):
    ans_mas = []

    if type(list_skills) != list:
        return None

    for skill in list_skills:
        tr_skill = define_skill(skill, definition_dict)
        if tr_skill != UNKNOWN_TITLE:
            ans_mas.append(tr_skill)

    ans_mas = list(set(ans_mas)) if drop_duplicates else ans_mas
    return '\n'.join(ans_mas)


def combine_skills(ser):
    ser = ser.to_dict()
    key_skills = [] if ser['key_skills'] is None or ser['key_skills'] == '' else ser['key_skills'].split('\n')
    if '' in key_skills:
        print(key_skills)
    description_skills = [] if ser['key_skills_description'] is pd.NA or ser['key_skills_description'] == '' else ser['key_skills_description'].split('\n')
    if '' in description_skills:
        print(description_skills)
    return '\n'.join(list(set(key_skills + description_skills)))


def classifying_skill(key_skills_col, description_col):
    solo_dict_skill = sum_dict(list(dict_skill.values()))
    invert_solo_dict_skill = invert_dict(solo_dict_skill)

    key_skills = key_skills_col.str.split('\n').apply(lambda el: define_vac_skills(el, invert_solo_dict_skill))
    solo_dict_skill = {skill: [set(word.split()) for word in words] for skill, words in solo_dict_skill.items()}
    key_skills_description = description_col.apply(lambda d: get_description_skills(d, solo_dict_skill))

    df = pd.DataFrame({'key_skills': key_skills, 'key_skills_description': key_skills_description})
    return df.apply(combine_skills, axis=1)


def classifying_grup_skill(skills_col):
    grup_dict_skill = {key: list(value.keys()) for key, value in dict_skill.items()}
    invert_grup_dict_skill = invert_dict(grup_dict_skill)

    return skills_col.str.split('\n').apply(lambda el: define_vac_skills(el, invert_grup_dict_skill, False))


def print_skill_log(vac_csv):
    lists_skill_in_vac = vac_csv['key_skills'].str.split('\n').dropna().tolist()
    print_log(f"Count vacancies with skills: {len(lists_skill_in_vac)}")

    all_key_skills = sum_mas(lists_skill_in_vac)
    global_skill_count = len(all_key_skills)
    print_log(f"Count skills: {global_skill_count}")
    print_log(f"Count unique skills: {len(set(all_key_skills))}")


if __name__ == '__main__':
    vac_csv = pd.read_csv(INPUT_FILE, low_memory=False)

    print_skill_log(vac_csv)

    vac_csv['key_skills'] = classifying_skill(vac_csv['key_skills'])
    vac_csv['grup_skills'] = classifying_grup_skill(vac_csv['key_skills'])
    vac_csv.to_csv(OUT_FILE, index=False)
