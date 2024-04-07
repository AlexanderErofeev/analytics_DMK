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


def classifying_skill(key_skills_col):
    solo_dict_skill = sum_dict(list(dict_skill.values()))
    invert_solo_dict_skill = invert_dict(solo_dict_skill)

    return key_skills_col.str.split('\n').apply(lambda el: define_vac_skills(el, invert_solo_dict_skill))


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
