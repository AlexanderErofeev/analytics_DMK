import numpy as np
import pandas as pd


def sum_mas_per_el(list_lists):
    ans_mas = [0] * len(list_lists[0])
    for i in range(len(ans_mas)):
        ans_mas[i] = sum([li[i] for li in list_lists])
    return ans_mas


def multiplic_mas_per_el(list_1, list_2):
    ans_mas = [0] * len(list_1)
    for i in range(len(ans_mas)):
        ans_mas[i] = list_1[i] * list_2[i]
    return ans_mas


def del_mas_per_el(list_1, list_2):
    ans_mas = [0] * len(list_1)
    for i in range(len(ans_mas)):
        if list_1[i] == 0:
            ans_mas[i] = 0
        else:
            ans_mas[i] = list_1[i] // list_2[i]
    return ans_mas


class Profession:
    def __init__(self, name, child_professions, reference=False):
        self.name = name
        self.child_professions = child_professions
        self.reference = reference

    def is_leaf(self):
        return len(self.child_professions) == 0

    def get_count_stat(self, count_stat):
        if self.is_leaf() or self.reference:
            return count_stat.loc[self.name].tolist()
        else:
            return sum_mas_per_el([profession.get_count_stat(count_stat) for profession in professions_list if profession.name in self.child_professions])

    def get_salary_stat(self, count_stat, salary_stat):
        if self.is_leaf() or self.reference:
            return salary_stat.loc[self.name].tolist()
        else:
            ch_mas = [profession for profession in professions_list if profession.name in self.child_professions]
            return del_mas_per_el(sum_mas_per_el([multiplic_mas_per_el(profession.get_count_stat(count_stat), profession.get_salary_stat(count_stat, salary_stat)) for profession in ch_mas]), self.get_count_stat(count_stat))

    def get_skills_stat(self, skills_stat):
        if self.is_leaf() or self.reference:
            return skills_stat.T.loc[self.name].tolist()
        else:
            mas = sum_mas_per_el([profession.get_skills_stat(skills_stat) for profession in professions_list if profession.name in self.child_professions])
            return [round(el / sum(mas), 4) for el in mas]


professions_list = [
    Profession(name='IT-специалист',
               child_professions=['Специалист по автоматизации', 'Инженер-электроник', 'Инженер сетей',
                                  'Сервисный инженер', 'Инженер АСУ ТП', 'Программист-разработчик', 'ERP-инженер',
                                  'Веб-специалист', 'Интернет маркетолог', 'Системный администратор',
                                  'Специалист технической поддержки', 'Руководитель ИТ-проектов', 'Менеджер IT-проекта',
                                  'Data scientist', 'Инженер систем', 'Аналитик', 'UX/UI-дизайнер',
                                  'QA-инженер', 'Machine learning-инженер', 'Devops-инженер',
                                  'Преподаватель по программированию', 'Разработчик игр',
                                  'Специалист по информационной безопасности', 'Специалист по работе с базами данных',

                                  # Уснаследованы не прямо
                                  'IOS-разработчик', 'Android-разработчик', 'Верстальщик', 'Frontend-разработчик',
                                  'Backend-разработчик', 'Fullstack-разработчик', '1C-программист', 'SAP-консультант',
                                  'SMM-менеджер', 'SEO-специалист']
               ),

    Profession(name='Программист-разработчик',
               child_professions=['Разработчик мобильных приложений', 'Web-разработчик', 'Desktop-разработчик',
                                  'Инженер-программист', 'Программист микроконтроллеров']
               ),
    Profession(name='Разработчик мобильных приложений',
               child_professions=['IOS-разработчик', 'Android-разработчик'],
               reference=True
               ),
    Profession(name='Web-разработчик',
               child_professions=['Верстальщик', 'Frontend-разработчик', 'Backend-разработчик', 'Fullstack-разработчик'],
               reference=True
               ),
    Profession(name='ERP-инженер',
               child_professions=['1C-программист', 'SAP-консультант'],
               reference=True
               ),
    Profession(name='Веб-специалист',
               child_professions=['Web-мастер', 'Контент-менеджер']
               ),
    Profession(name='Интернет маркетолог',
               child_professions=['SMM-менеджер', 'SEO-специалист'],
               reference=True
               ),
    Profession(name='Специалист по работе с базами данных',
               child_professions=['SQL-разработчик', 'Администратор баз данных']
               ),

    Profession(name='Специалист по автоматизации',
               child_professions=[]
               ),
    Profession(name='Инженер-электроник',
               child_professions=[]
               ),
    Profession(name='Инженер сетей',
               child_professions=[]
               ),
    Profession(name='Сервисный инженер',
               child_professions=[]
               ),
    Profession(name='Инженер АСУ ТП',
               child_professions=[]
               ),
    Profession(name='IOS-разработчик',
               child_professions=[]
               ),
    Profession(name='Android-разработчик',
               child_professions=[]
               ),
    Profession(name='Верстальщик',
               child_professions=[]
               ),
    Profession(name='Frontend-разработчик',
               child_professions=[]
               ),
    Profession(name='Backend-разработчик',
               child_professions=[]
               ),
    Profession(name='Fullstack-разработчик',
               child_professions=[]
               ),
    Profession(name='Desktop-разработчик',
               child_professions=[]
               ),
    Profession(name='Инженер-программист',
               child_professions=[]
               ),
    Profession(name='Программист микроконтроллеров',
               child_professions=[]
               ),
    Profession(name='1C-программист',
               child_professions=[]
               ),
    Profession(name='SAP-консультант',
               child_professions=[]
               ),
    Profession(name='Web-мастер',
               child_professions=[]
               ),
    Profession(name='Контент-менеджер',
               child_professions=[]
               ),
    Profession(name='SMM-менеджер',
               child_professions=[]
               ),
    Profession(name='SEO-специалист',
               child_professions=[]
               ),
    Profession(name='Системный администратор',
               child_professions=[]
               ),
    Profession(name='Специалист технической поддержки',
               child_professions=[]
               ),
    Profession(name='Руководитель ИТ-проектов',
               child_professions=[]
               ),
    Profession(name='Менеджер IT-проекта',
               child_professions=[]
               ),
    Profession(name='Data scientist',
               child_professions=[]
               ),
    Profession(name='Инженер систем',
               child_professions=[]
               ),
    Profession(name='Аналитик',
               child_professions=[]
               ),
    Profession(name='UX/UI-дизайнер',
               child_professions=[]
               ),
    Profession(name='SQL-разработчик',
               child_professions=[]
               ),
    Profession(name='QA-инженер',
               child_professions=[]
               ),
    Profession(name='Machine learning-инженер',
               child_professions=[]
               ),
    Profession(name='Devops-инженер',
               child_professions=[]
               ),
    Profession(name='Преподаватель по программированию',
               child_professions=[]
               ),
    Profession(name='Разработчик игр',
               child_professions=[]
               ),
    Profession(name='Специалист по информационной безопасности',
               child_professions=[]
               ),
    Profession(name='Администратор баз данных',
               child_professions=[]
               ),
]


def get_dynamics_count(count_stat):
    mas_data = [pr.get_count_stat(count_stat) for pr in professions_list]
    return pd.DataFrame(np.array(mas_data),
                        columns=range(2003, 2003 + len(mas_data[0])),
                        index=[p.name for p in professions_list])


def get_dynamics_salary(count_stat, salary_stat):
    mas_data = [pr.get_salary_stat(count_stat, salary_stat) for pr in professions_list]
    return pd.DataFrame(np.array(mas_data),
                        columns=range(2003, 2003 + len(mas_data[0])),
                        index=[p.name for p in professions_list])


def get_skill_stat(skills_stat_file):
    mas_data = [pr.get_skills_stat(skills_stat_file) for pr in professions_list]
    return pd.DataFrame(np.array(mas_data),
                        columns=skills_stat_file.index,
                        index=[p.name for p in professions_list])


if __name__ == '__main__':
    count_stat = pd.read_csv('..\\Results\\count_stat.csv', index_col='prof_name')
    salary_stat = pd.read_csv('..\\Results\\salary_stat.csv', index_col='prof_name')
    skills_stat = pd.read_csv('..\\Results\\skills_stat.csv', index_col='Skill')

    get_dynamics_count(count_stat).to_csv('dynamics_count_vacancies_to_DB.csv', index_label='name')
    get_dynamics_salary(count_stat, salary_stat).to_csv('dynamics_salary_vacancies_to_DB.csv', index_label='name')
    get_skill_stat(skills_stat).to_csv('skill_stat_vacancies_to_DB.csv', index_label='name')
