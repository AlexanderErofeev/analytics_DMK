import multiprocessing
import pandas as pd
from dict_skill import dict_skill
from global_settings_and_functions import PROCESSOR_COUNT, percent, sum_mas, sum_dict


def invert_dict(input_dict):
    ans_dict = {}
    for key, values in input_dict.items():
        ans_dict.update({value: key for value in values})
    return ans_dict


def define_skill(skill, dict):
    if skill in dict:
        return dict[skill]
    else:
        return 'Неизвестный навык'


def define_vac_skills(list_skills):
    ans_mas = []

    if type(list_skills).__name__ != 'list':
        return None

    for skill in list_skills:
        tr_skill = define_skill(skill, tr_dict)
        if tr_skill != 'Неизвестный навык':
            ans_mas.append(tr_skill)

    ans_mas = list(set(ans_mas))
    return '\n'.join(ans_mas)


if __name__ == '__main__':
    vac_csv = pd.read_csv('vacancies_classified.csv', low_memory=False)
    vac_csv['key_skills'] = vac_csv['key_skills'].str.split('\n')

    skills = vac_csv['key_skills'].dropna().tolist()
    print(f"Всего вакансий с указанными скилами: {len(skills)}")

    skills = sum_mas(skills)
    global_skill_count = len(skills)
    print(f"Всего скилов: {global_skill_count}")

    unique_skills = list(set(skills))
    print(f"Всего уникальных скилов: {len(unique_skills)}")

    tr_dict = invert_dict(sum_dict(list(dict_skill.values())))

    vac_csv['key_skills'] = vac_csv['key_skills'].apply(define_vac_skills)
    vac_csv.to_csv('vacancies_and_skill_classified.csv', index=False)

    skills = pd.Series(skills)
    skills_counts = skills.value_counts().sort_values(ascending=False)
    pd.concat([skills_counts, skills_counts.apply(lambda x: percent(x, global_skill_count))], axis=1)\
        .to_csv('Debug data\\Skills debug\\skills_counts.csv', index_label='skill', header=['count', 'percent'])

    skills = pd.concat([skills, skills.apply(lambda el: define_skill(el, tr_dict))], axis='columns')
    skills.columns = ['skill', 'class_skill']
    skills = skills.groupby(['class_skill'])

    undefined_skills = skills.get_group('Неизвестный навык')
    undefined_skills_counts = undefined_skills['skill'].value_counts()
    undefined_skills_counts = undefined_skills_counts[undefined_skills_counts >= 100]
    pd.concat([undefined_skills_counts, undefined_skills_counts.apply(lambda x: percent(x, global_skill_count))], axis=1)\
        .to_csv('Debug data\\Skills debug\\undefined_skills_counts.csv', index_label='skill', header=['count', 'percent'])
    print(f"Распределено скилов: {percent(global_skill_count - len(undefined_skills.index), global_skill_count)}")

    skills = skills.apply(lambda el: len(el.index))
    skills = skills.sort_values(ascending=False)
    pd.concat([skills, skills.apply(lambda x: percent(x, global_skill_count))], axis=1) \
        .to_csv('Debug data\\Skills debug\\distributed_skills_counts.csv', index_label='skill', header=['count', 'percent'])
