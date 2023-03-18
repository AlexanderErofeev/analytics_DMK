import pandas as pd
from dict_skill import dict_skill
from global_settings_and_functions import percent, sum_mas, sum_dict


def invert_dict(input_dict):
    ans_dict = {}
    for key, values in input_dict.items():
        ans_dict.update({value: key for value in values})
    return ans_dict


def define_skill(skill, definition_dict):
    if skill in definition_dict:
        return definition_dict[skill]
    else:
        return 'Неизвестный навык'


def define_vac_skills(list_skills, definition_dict):
    ans_mas = []

    if type(list_skills).__name__ != 'list':
        return None

    for skill in list_skills:
        tr_skill = define_skill(skill, definition_dict)
        if tr_skill != 'Неизвестный навык':
            ans_mas.append(tr_skill)

    ans_mas = list(set(ans_mas))
    return '\n'.join(ans_mas)


def generate_skill_statistics(ser, bottom_line, file_name, all_count_for_percent):
    ser = ser[ser >= bottom_line]\
        .sort_values(ascending=False)
    pd.concat([ser, ser.apply(lambda x: percent(x, all_count_for_percent))], axis=1)\
        .to_csv(f"Debug data\\Skills debug\\{file_name}", index_label='skill', header=['count', 'percent'])


if __name__ == '__main__':
    vac_csv = pd.read_csv('vacancies_classified.csv', low_memory=False)
    vac_csv['key_skills'] = vac_csv['key_skills'].str.split('\n')

    lists_skill_in_vac = vac_csv['key_skills'].dropna().tolist()
    print(f"Всего вакансий с указанными скилами: {len(lists_skill_in_vac)}")

    all_key_skills = sum_mas(lists_skill_in_vac)
    global_skill_count = len(all_key_skills)
    print(f"Всего скилов: {global_skill_count}")
    print(f"Всего уникальных скилов: {len(set(all_key_skills))}")
    all_key_skills_ser = pd.Series(all_key_skills)

    solo_dict_skill = sum_dict(list(dict_skill.values()))
    invert_solo_dict_skill = invert_dict(solo_dict_skill)

    grup_dict_skill = {key: list(value.keys()) for key, value in dict_skill.items()}
    invert_grup_dict_skill = invert_dict(grup_dict_skill)

    vac_csv['key_skills'] = vac_csv['key_skills'].apply(lambda el: define_vac_skills(el, invert_solo_dict_skill))
    vac_csv['grup_skills'] = vac_csv['key_skills'].str.split('\n').apply(lambda el: define_vac_skills(el, invert_grup_dict_skill))
    vac_csv.to_csv('vacancies_and_skill_classified.csv', index=False)

    generate_skill_statistics(all_key_skills_ser.value_counts(), 0, 'skills_counts.csv', global_skill_count)

    key_skills_with_definition = pd.concat([all_key_skills_ser, all_key_skills_ser.apply(lambda el: define_skill(el, invert_solo_dict_skill))], axis='columns')
    key_skills_with_definition.columns = ['skill', 'class_skill']
    distributed_skills = key_skills_with_definition.groupby(['class_skill'])

    undefined_skills = distributed_skills.get_group('Неизвестный навык')
    print(f"Распределено скилов: {percent(global_skill_count - len(undefined_skills.index), global_skill_count)}")
    generate_skill_statistics(undefined_skills['skill'].value_counts(), 0, 'undefined_skills_counts.csv', global_skill_count)

    distributed_skills_counts = distributed_skills.apply(lambda el: len(el.index))
    generate_skill_statistics(distributed_skills_counts, 0, 'distributed_skills_counts.csv', global_skill_count)

