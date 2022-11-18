import pandas as pd
import csv
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np
from os import path
import pathlib
from pathlib import Path
import os
import glob

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
# Минус слова для профессий
exceptions_words = \
    {
        'Программист': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                        'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                        'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'backend', 'бэкэнд', 'бэкенд',
                        'c#',
                        'c sharp', 'c-sharp', 'си шарп', 'шарп', 'c#', 'c sharp', 'c-sharp', 'си шарп', 'шарп',
                        'c\+\+/с', 'c/c\+\+', 'c\\\c\+\+', 'c\+\+\\\c', 'c-plus-plus', 'c plus plus', 'си плюс плюс',
                        'delphi', 'дефи', 'frontend', 'фронтенд', 'вёрстка', 'версталь', 'fullstack', 'фуллстак',
                        'фулстак', 'фуллстэк', 'фулстэк', 'js', 'javascript', 'джаваскрипт', 'яваскрипт', 'android',
                        'андроид', 'android', 'андроид', 'ios', 'айос', 'mobile', 'мобайл', 'мобиль', 'php', 'пхп',
                        'python', 'питон', 'пайтон', 'ruby', 'руби', 'sharepoint', 'шарпоинт', 'шарепоинт', 'sql',
                        'скюл',
                        'web', 'веб', 'инженер-программист', 'engineer', 'инженер программист', 'microcontr',
                        'микроконтрол',
                        'system prog', 'системный программист', 'системный', 'c\+\+', 'game', 'unity', 'инженер',
                        '.net',
                        'java', 'рнр', 'frontеnd', 'с\+\+', 'c#', '1 c', '1 с', '1:c', '1 : c', '1:с', '1 : с', 'с#',
                        'c \+ \+', 'c\+ \+', 'c \+\+', ' си ', 'с \+ \+', 'с\+ \+', 'с \+\+', ' си,', 'баз данн',
                        '/front-end', 'front', 'оператор'],
        'Embedded-разработчик': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор',
                                                                 'репититор', 'qa', 'test', 'тест',
                                                                 'quality assurance', 'team lead', 'тимлид', 'тим лид',
                                                                 'teamlead', 'lead', 'менджер', 'manager',
                                                                 'руководитель', 'директор', 'leader', 'director', '1c',
                                                                 '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                                                                 '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Инженер-программист': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                                'quality assurance', 'микроконтрол', '1c', '1с', 'team lead', 'тимлид', 'тим лид',
                                'teamlead', 'lead', 'менджер', 'manager',
                                'руководитель', 'директор', 'leader', 'director', 'game', 'unity', '1 c', '1 с', '1:c',
                                '1 : c',
                                '1:с', '1 : с', 'баз данн', 'оператор'],
        'Системный программист': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test',
                                  'тест',
                                  'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер',
                                  'manager',
                                  'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c',
                                  '1 с',
                                  '1:c',
                                  '1 : c', '1:с', '1 : с', 'баз данн', 'оператор', 'администратор'],
        'Desktop-разработчик': ['qa', 'test', 'тест', 'quality assurance', 'препод', 'tutor', 'тьютор', 'репетитор',
                                'репититор',
                                'учитель', 'backend', 'бэкэнд', 'game', 'игр', 'unity', 'team lead', 'тимлид',
                                'тим лид', 'teamlead',
                                'lead', 'менджер', 'manager',
                                'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c',
                                '1 с', '1:c',
                                '1 : c', '1:с', '1 : с', 'баз данн', 'оператор', 'fullstack', 'фуллстак', 'фулстак',
                                'фуллстэк',
                                'фулстэк', 'full-stack', 'backend', 'бэкэнд', 'бэкенд', 'back-end', 'бэк-энд',
                                'бэк-енд'],
        'Web-разработчик': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                            'quality assurance', 'designer', 'дизайнер', 'менеджер', 'manager', 'аналитик', 'team lead',
                            'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                            'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с',
                            '1:c', '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Frontend-программист': ['game', 'препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test',
                                 'тест',
                                 'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер',
                                 'manager', 'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game',
                                 'unity',
                                 '1 c', '1 с', '1:c', '1 : c', '1:с', '1 : с', 'баз данн', 'оператор', 'преподаватель',
                                 'jsoc', 'qa', 'тест', 'test', 'тьютор'],
        'Backend-программист': ['qa', 'test', 'тест', 'quality assurance', 'game', 'препод', 'учитель', 'tutor',
                                'тьютор', 'репетитор', 'репититор', 'team lead', 'тимлид', 'тим лид', 'teamlead',
                                'lead', 'менджер', 'manager', 'руководитель', 'директор', 'leader', 'director', '1c',
                                '1с', 'game', 'unity', '1 c', '1 с', '1:c', '1 : c', '1:с', '1 : с', 'баз данн',
                                'оператор', 'sql', 'cms', 'цмс', 'game', 'unity',
                                'sdet', 'data science', 'data scientist'],
        'Fullstack-программист': ['qa', 'test', 'тест', 'quality assurance', 'препод', 'учитель', 'tutor', 'тьютор',
                                  'репетитор', 'репититор', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead',
                                  'менджер',
                                  'manager',
                                  'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c',
                                  '1 с',
                                  '1:c',
                                  '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Mobile-разработчик': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                               'quality assurance', 'ремонт', 'дизайнер', 'manager', 'owner', 'аналитик', 'animation',
                               '3d',
                               'atrist', 'бизнес', 'художник', 'аниматор',
                               'механик', 'эксплуатац', 'автомобиль', 'designer', 'java', 'маркетолог', 'python',
                               'автор',
                               'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                               'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c',
                               '1 с', '1:c',
                               '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'IOS-разработчик': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                            'quality assurance', 'ремонт', 'дизайнер', 'переквалификация', 'team lead', 'тимлид',
                            'тим лид',
                            'teamlead', 'lead', 'менджер', 'manager',
                            'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с',
                            '1:c',
                            '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Android-разработчик': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                                'quality assurance', 'ремонт', 'дизайнер', 'бизнес', 'team lead', 'тимлид', 'тим лид',
                                'teamlead',
                                'lead', 'менджер', 'manager', '1c', '1с',
                                'руководитель', 'директор', 'leader', 'director', 'game', 'unity', '1 c', '1 с', '1:c',
                                '1 : c',
                                '1:с', '1 : с', 'баз данн', 'оператор'],
        'Администратор баз данных': ['erp', 'разработчик', 'programmer', 'developer', 'программист', 'инженер', 'lead',
                                     'backend',
                                     'бэк-энд', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'руководитель',
                                     'директор',
                                     'leader', 'director', 'препод', 'учитель', 'tutor', 'тьютор', 'репетитор',
                                     'репититор', 'qa', 'test', 'тест', 'quality assurance', 'менджер', 'manager',
                                     'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity',
                                     '1 c', '1 с', '1:c',
                                     '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Devops-инженер': ['team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'руководитель', 'директор', 'leader',
                           'director',
                           'преподаватель'],
        'Специалист по анализу данных': ['team lead', 'тимлид', 'тим лид', 'teamlead', 'lead',
                                                          'руководитель', 'директор', 'leader',
                                                          'director', 'qa', 'test', 'тест', 'quality assurance'],
        'Системный администратор': ['devops', 'техподдержка', 'тех поддержка'],
        'Тестировщик (QA-инженер)': ['team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'руководитель', 'директор',
                                     'leader', 'director'],
        'Специалист техподдержки': ['1с'],
        'Инженер': ['qa', 'test', 'тест', 'quality assurance', 'devops', 'team lead', 'тимлид', 'тим лид', 'teamlead',
                    'lead', 'руководитель', 'директор', 'leader', 'director', 'java', 'php', 'front-end', 'frontend',
                    '.net', 'data', 'разработчик', 'developer', 'dev', 'toolchain', 'system', 'android', 'security',
                    'desktop', 'mobile', 'hpc', 'admin', 'ml', 'python', 'c#', 'c\+\+', 'site', 'network', 'cv',
                    'video', 'software', 'java', 'programmer', 'программист', 'информаци', 'dba', 'ios', 'rnd',
                    'backend', 'full-stack', 'поддрежк', 'framework', 'voip', 'it', 'embed', 'manager', 'js', 'oracle',
                    'support', 'compil', 'scient', 'sysop', 'micros', 'scala', 'linux', 'graph', 'бдд', 'system',
                    'систем', 'внедрен', 'лидер', 'ит', 'full stack', 'web', 'ui/ux', '1с', '1c', 'cloud'],
        'Аналитик': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                     'lead', 'руководитель', 'директор', 'leader', 'director'],
        'Специалист по информационной безопасности': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                                                      'lead', 'руководитель', 'директор', 'leader', 'director'],
        'ERP-специалист': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                           'lead', 'руководитель', 'директор', 'leader', 'director', 'game', 'препод', 'учитель',
                           'tutor', 'тьютор', 'репетитор', 'репититор', 'ic\+\+', 'qa', 'test', 'тест',
                           'quality assurance', 'менджер',
                           'manager', 'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity',
                           '1:c', '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        '1С-разработчик': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                           'lead', 'руководитель', 'директор', 'leader', 'director'],
        'SAP-разработчик': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                            'lead', 'руководитель', 'директор', 'leader', 'director'],
        'Oracle-разработчик': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                               'lead', 'руководитель', 'директор', 'leader', 'director'],
        'Разработчик игр (GameDev)': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                                      'lead', 'руководитель', 'директор', 'leader', 'director', 'design', 'дизайн',
                                      'иллюстратор',
                                      'qa', 'test', 'тест', 'quality assurance'],
        'Руководитель ИТ-проектов': [],
        'Веб-специалист': [],
        'Web-мастер': [],
        'Контент-менеджер': ['smm'],
        'UX/UI дизайнер': ['team lead', 'тимлид', 'тим лид', 'teamlead',
                           'lead', 'руководитель', 'директор', 'leader', 'director', 'linux', 'nuxt', 'копирай',
                           'писат',
                           'аналит', 'исследов', 'redux', 'ресёрчер', 'editor', 'writ', 'luxe', 'редактор', 'исслед',
                           'reasear',
                           'programmer', 'recruiter', 'builder', 'liquidit', 'gui', 'vkui', 'sapui', 'full stack',
                           'acqui',
                           'equip', 'requir', 'develop', 'программист', 'менеджер', 'разработчик', 'перподаватель',
                           'учитель'],
        'Менеджер IT-проекта': [],
        'Специалист по интернет-маркетингу': ['sap'],
        'Интернет-маркетолог': [],
        'Специалист по интернет-рекламе (Директолог)': [],
        'SEO-специалист': [],
        'SMM-специалист': [],
        'Email-маркетолог': ['аналитик', 'c\+\+', 'dev', 'верстальщик', 'front'],
        'C#': ['qa', 'test', 'тест', 'quality assurance', 'препод', 'tutor', 'тьютор', 'репетитор', 'репититор',
               'учитель', 'backend', 'бэкэнд', 'game', 'игр', 'unity', 'team lead', 'тимлид', 'тим лид', 'teamlead',
               'lead', 'менджер', 'manager',
               'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
               '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'C C++': ['game', 'препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'ic\+\+', 'qa', 'test',
                  'тест',
                  'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                  'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1:c', '1 : c',
                  '1:с', '1 : с', 'баз данн', 'оператор'],
        'Delphi': ['qa', 'test', 'тест', 'quality assurance', 'препод', 'учитель', 'tutor', 'тьютор', 'репетитор',
                   'репититор', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                   'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                   '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],

        'JavaScript': ['преподаватель', 'jsoc', 'qa', 'тест', 'test', 'тьютор', 'qa', 'test', 'тест',
                       'quality assurance',
                       'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                       'руководитель', 'директор', 'leader', 'director', '1c', '1с', '1 c', '1 с', '1:c',
                       '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Java': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                 'quality assurance', 'javascript', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead',
                 'менджер', 'manager',
                 'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                 '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],

        'PHP': ['тестировщик', 'репититор', '1c', '1с', 'ученик', 'репетитор', 'sql', 'cms', 'цмс', 'преподаватель',
                'учитель', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Python': ['тестировщик', 'qa', 'преподаватель', 'тест', 'quality assurance', 'test', 'sdet', 'учитель',
                   'репетитор', 'репититор', 'data science', 'data scientist', 'team lead', 'тимлид',
                   'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                   'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                   '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Ruby': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                 'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                 'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                 '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'Sharepoint': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                       'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                       'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с',
                       '1:c',
                       '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],
        'SQL': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'репититор', 'qa', 'test', 'тест',
                'quality assurance', 'team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'менджер', 'manager',
                'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game', 'unity', '1 c', '1 с', '1:c',
                '1 : c', '1:с', '1 : с', 'баз данн', 'оператор'],

    }
# Все профессии
prof_names = \
    {
        'Программист': ['programmer', 'программист'],
        'Embedded-разработчик': ['microcontr', 'микроконтрол', 'embedded', 'c\+\+/с',
                                                                 'c/c\+\+', 'c\\\c\+\+', 'c\+\+\\\c', 'c-plus-plus',
                                                                 'c plus plus', 'си плюс плюс',
                                                                 'с\+\+/с', 'с/с\+\+', 'с\\\с\+\+', 'с\+\+\\\с',
                                                                 'c\+\+', 'с\+\+', 'c \+\+', 'с \+\+', 'c \+ \+',
                                                                 'с \+ \+'],
        'Инженер-программист': ['инженер-программист', 'engineer', 'инженер программист'],
        'Системный программист': ['system prog', 'системный программист'],
        'Desktop-разработчик': ['desktop', 'desktop', 'десктоп', 'c#', 'c sharp', 'c-sharp', 'си шарп', 'шарп', 'с#'],
        'Web-разработчик': ['web-develoer', 'веб-разработичк', 'web-разработичк', 'web develoer', 'веб разработичк',
        'web разработичк', 'web-programmer', 'web programmer', 'web-программист', 'web программист',
        'веб-программист', 'веб программист'],
        'Frontend-программист': ['frontend', 'фронтенд', 'вёрстка', 'версталь', 'front-end', 'js', 'javascript',
                                 'джаваскрипт', 'яваскрипт'],
        'Backend-программист': ['backend', 'бэкэнд', 'бэкенд', 'back-end', 'бэк-энд', 'бэк-енд', 'php', 'пхп', 'рнр',
                                'python', 'питон', 'пайтон'],
        'Fullstack-программист': ['fullstack', 'фуллстак', 'фулстак', 'фуллстэк', 'фулстэк', 'full-stack'],
        'Mobile-разработчик': ['mobile', 'мобайл', 'мобиль'],
        'IOS-разработчик': ['ios', 'айос'],
        'Android-разработчик': ['android', 'андроид'],
        'Администратор баз данных': ['администратор баз данных', 'оператор баз данных', 'базы данных', 'oracle',
                                     'mysql',
                                     'data base', 'dba'],
        'Devops-инженер': ['devops', 'development operations'],
        'Специалист по анализу данных': ['data scientist', 'data science'],
        'Системный администратор': ['system admin', 'сисадмин', 'сис админ', 'системный админ'],
        'Тестировщик (QA-инженер)': ['qa', 'test', 'тест', 'quality assurance'],
        'Специалист техподдержки': ['техподдер', 'тех поддерж', 'тихническая поддерж', 'technical support engineer',
                                    'поддержк'],
        'Инженер': ['engineer', 'инженер'],
        'Аналитик': ['analytic', 'аналитик'],
        'Специалист по информационной безопасности': ['информационная безопасность',
                                                      'Специалист по информационной безопасности',
                                                      'информационной безопасности', 'безопасности', 'защита информ',
                                                      'information security specialist',
                                                      'information security'],
        'ERP-специалист': ['erp', 'enterprice resource planning'],
        '1С-разработчик': ['1с-разработчик', '1c-разработчик', '1с разработчик', '1c разработчик'],
        'SAP-разработчик': ['sap', 'sap-developer', 'sap-разработчик', 'sap-программист', 'sap пррограммист'],
        'Oracle-разработчик': ['oracle-developer', 'oracle developer', 'oracle разработчик', 'oracle-разработчик',
                               'oracle-программист',
                               'oracle программист'],
        'Разработчик игр (GameDev)': ['game', 'unity', 'игр'],
        'Руководитель ИТ-проектов': ['team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'руководитель', 'директор',
                                     'leader', 'director'],
        'Веб-специалист': ['web-спец', 'веб-спец', 'web спец', 'веб спец', 'web-spec', 'web spec'],
        'Web-мастер': ['web-мастер', 'web мастер', 'веб-мастер', 'веб мастер'],
        'Контент-менеджер': ['content-manager', 'content manager', 'контент-менеджер', 'контент менеджер'],
        'UX/UI дизайнер': ['design', 'ux', 'ui', 'дизайн', 'иллюстратор'],
        'Менеджер IT-проекта': ['product manager', 'менеджер проекта', 'project manager', 'менеджер продукта'],
        'Специалист по интернет-маркетингу': ['internet-marketing', 'интернет-маркетинг', 'internet marketing',
        'интернет маркетинг'],
        'Интернет-маркетолог': ['internet-market', 'internet market', 'инернет-маркетолог', 'интернет маркетолог'],
        'Специалист по интернет-рекламе (Директолог)': ['internet advisory', 'advisor', 'directologist', 'директолог',
                                                        'интернет-реклам', 'интернет реклам'],
        'SEO-специалист': ['seo'],
        'SMM-специалист': ['smm', 'social media marketing'],
        'Email-маркетолог': ['mail'],

        'C#': ['c#', 'c sharp', 'c-sharp', 'си шарп', 'шарп', 'с#'],
        'C C++': ['c\+\+/с', 'c/c\+\+', 'c\\\c\+\+', 'c\+\+\\\c', 'c-plus-plus', 'c plus plus', 'си плюс плюс',
                  'с\+\+/с', 'с/с\+\+', 'с\\\с\+\+', 'с\+\+\\\с', 'c\+\+', 'с\+\+', 'c \+\+', 'с \+\+', 'c \+ \+',
                  'с \+ \+'],
        'Delphi': ['delphi', 'делфи'],
        'JavaScript': ['js', 'javascript', 'джаваскрипт', 'яваскрипт'],
        'Java': ['java', 'ява', 'джава'],

        'PHP': ['php', 'пхп', 'рнр'],
        'Python': ['python', 'питон', 'пайтон'],
        'Ruby': ['ruby', 'руби'],
        'Sharepoint': ['sharepoint', 'шарпоинт', 'шарепоинт'],
        'SQL': ['sql', 'скюл']
    }
# Профессии для цсв
csv_professions = ['Программист',
    'Embedded-разработчик', 'Инженер-программист',
    'Системный программист', 'Desktop-разработчик',  'Web-разработчик',
    'Frontend-программист',
    'Backend-программист', 'Fullstack-программист',  'Mobile-разработчик',
    'IOS-разработчик',
    'Android-разработчик', 'Администратор баз данных', 'Devops-инженер',
    'Специалист по анализу данных',
    'Системный администратор', 'Тестировщик (QA-инженер)', 'Специалист техподдержки',
    'Инженер', 'Аналитик', 'Специалист по информационной безопасности',  'ERP-специалист',
    '1С-разработчик', 'SAP-разработчик', 'Oracle-разработчик', 'Разработчик игр (GameDev)',
    'Руководитель ИТ-проектов', 'Веб-специалист',
    'Web-мастер', 'Контент-менеджер',
    'UX/UI дизайнер', 'Менеджер IT-проекта',  'Специалист по интернет-маркетингу',
    'Интернет-маркетолог', 'Специалист по интернет-рекламе (Директолог)', 'SEO-специалист',
    'SMM-специалист', 'Email-маркетолог'
]
csv_dict = {'name': csv_professions}

# Грузим hh

PathToCsv = "D:\\Program Files (x86)\\BD DMK\\Базы HH\\dataset\\"


def load_hh(year):
    # df2017 = pd.read_csv(r"C:\Users\ahmet\YandexDisk\ДИПЛОМ\Материалы\year_2017.csv")
    # df2018 = pd.read_csv(r"C:\Users\ahmet\YandexDisk\ДИПЛОМ\Материалы\year_2018.csv")
    # df2019 = pd.read_csv(r"C:\Users\ahmet\YandexDisk\ДИПЛОМ\Материалы\year_2019.csv")
    # df2020 = pd.read_csv(r"D:\Documents\Documents\PycharmProject\dmk\Anaconda\Anaconda\dataset\year_2020.csv")
    # df2021 = pd.read_csv(r"D:\Documents\Documents\PycharmProject\dmk\Anaconda\Anaconda\dataset\year_2021.csv")
    data_frame = pd.read_csv(PathToCsv + f"year_{year}.csv")
    return data_frame


# Оставляем в вакансиях name, key_skills, description
def create_columns(data_frame):
    # dfs2017 = df2017[["name", "key_skills", "description"]]
    # dfs2017['name'] = dfs2017['name'].astype(str).str.lower()
    # dfs2018 = df2018[["name", "key_skills", "description"]]
    # dfs2018['name'] = dfs2018['name'].astype(str).str.lower()
    # dfs2019 = df2019[["name", "key_skills", "description"]]
    # dfs2019['name'] = dfs2019['name'].astype(str).str.lower()
    # dfs2020 = df2020[["name", "key_skills", "description"]]
    # dfs2020['name'] = dfs2020['name'].astype(str).str.lower()
    # dfs2021 = df2021[["name", "key_skills", "description"]]
    # dfs2021['name'] = dfs2021['name'].astype(str).str.lower()
    data_frames = data_frame[
        ["id", "name", "key_skills", "address_city", "specializations", "employer_name", "salary_from", "salary_to",
         "description"]]
    data_frames['name'] = data_frames['name'].str.lower()
    data_frames_all = pd.concat([data_frames])
    return data_frames, data_frames_all


### ПОДКЛЮЧЕНИЕ ФАЙЛА СО СКИЛЛАМИ

# Пути к справочникам-классификаторам
ProjectPath = str(Path(__file__).parents[1]) + "\\dictionary\\"
# soft = literal_eval(open(str(ProjectPath) + "soft.txt", "r", encoding='utf-8').read())
# hard = literal_eval(open(str(ProjectPath) + "hard.txt", "r", encoding='utf-8').read())
# old_group_hard = literal_eval(open(str(ProjectPath) + "group-skills.txt", "r", encoding='utf-8').read())
# new_group_hard = literal_eval(open(str(ProjectPath) + "group19042022.txt", "r", encoding='utf-8').read())
# dict_lookup = {"Soft skills": soft, "Hard skills": hard, "Старая группировка Hard": old_group_hard, "Новая группировка Hard": new_group_hard}

# Путь к справочникам профессий
pathProgrammer = ProjectPath + "\\professions_sd\\programmer"
# Путь к итоговым отчетам
path_report = ProjectPath + "\\professions_sd_report"

# Печать статистики
files = os.listdir(pathProgrammer)
txt = [i for i in files if i.endswith('.txt')]

# Печать статистики
# print("Всего вакансий: \t", dfs_all["name"].count(), "\t", dfs_all["key_skills"].count())
aggregationList = []
for x in txt:
    # Формируем путь к файлу
    p = pathProgrammer + "\\" + x
    # Читаем файл
    vac_str = literal_eval(open(p, "r", encoding='utf-8').read())
    aggregationList += vac_str

pathOther = ProjectPath + "\\professions_sd"
files = os.listdir(pathOther)
txt = [i for i in files if i.endswith('.txt')]
for x in txt:
    # Формируем путь к файлу
    p = pathOther + "\\" + x
    # Читаем файл
    vac_str = literal_eval(open(p, "r", encoding='utf-8').read())
    aggregationList += vac_str


def create_writer(year):
    writer_elem = pd.ExcelWriter(path_report + f'\\result\\{year}.ResultTemp.xlsx', engine='xlsxwriter')
    # df2 = dfs_all[dfs_all['name'].isin(aggregationList)]
    # print(dfs_all)
    return writer_elem


# print(dfs_all)


def get_data_prof(name, data_frames_all):
    global df_result_name
    profession = name
    word = name
    profession_item = []
    for elem in prof_names[profession]:
        profession_item.append(data_frames_all[data_frames_all['name'].str.contains(elem)])
    profession_item_new = pd.concat(profession_item)
    profession_item_new.drop_duplicates(keep=False)
    profession_item_clear = profession_item_new
    # deleted_prof_elem = []
    # new_elem = 'dasda'
    for elem in exceptions_words[word]:
        # temp_deleted = profession_item_clear
        # if elem != new_elem:
        #   temp_deleted = temp_deleted.loc[temp_deleted['name'].str.contains(elem)]
        #   if temp_deleted['name'].str.contains(elem).bool:
        #       deleted_prof_elem.append(temp_deleted['name'].head(1))
        #       new_elem = elem
        #   else:
        #       new_elem = elem
        profession_item_clear = profession_item_clear.loc[~profession_item_clear['name'].str.contains(elem)]
    deleted_profession = pd.concat([profession_item_new, profession_item_clear]).drop_duplicates(keep=False)
    profession_item_clear.drop_duplicates(subset=['name'], keep=False, inplace=True)
    deleted_profession.drop_duplicates(subset=['name'], keep=False, inplace=True)
    profession_item_clear = profession_item_clear[['name']]
    deleted_profession = deleted_profession[['name']]
    df_name = profession_item_clear
    df_name.columns = [profession]
    # print(share_profession)
    # profession_item_clear.to_excel(writer, sheet_name=profession + ' Clear', index=False)
    ###РАСКОМЕНТИТЬ ДЛЯ ПОКАЗА АНАЛИТИКИ!!!###
    #df_name.to_excel(writer_names, sheet_name="Вакансии по профессиям", startcol=list(prof_names)
                     #.index(profession), index=False)
    df_name.to_excel(writer, sheet_name="Первая группа", startrow=1, startcol=list(prof_names)
                     .index(profession)+4, index=False)
    df_result_name = df_name
    #deleted_profession.columns = [profession]
    #deleted_profession.to_excel(writer_names, sheet_name="Выборка удалённых", startcol=list(prof_names)
                                #.index(profession), index=False)
    # if profession != 'C#' and profession != 'C C++' and profession != 'Delphi' and profession != 'JavaScript' and profession != 'Java' and profession != 'PHP' and profession != 'Python' and profession != 'Ruby' and profession != 'Sharepoint' and profession != 'SQL':
    # df_result_name.to_excel(writer_result_xlsx, sheet_name="Вакансии по профессиям", startcol=list(prof_names)
    # .index(profession), index=False)
    ###РАСКОМЕНТИТЬ ДЛЯ ПОКАЗА АНАЛИТИКИ!!!###
    # df_deleted = pd.DataFrame(deleted_prof_elem)
    # df_deleted.columns = [profession]
    # df_deleted.to_excel(writer_names, sheet_name="Выборка удалённых", startcol=list(prof_names)
    # .index(profession), startrow=0, index=False)
    return df_name, df_result_name, deleted_profession
    # dfs_all = dfs_all[~dfs_all.index.isin(profession_item_new.index)]


csv_dir = Path(f'{path_report}\\csv')
###РАСКОМЕНТИТЬ ДЛЯ ПОКАЗА АНАЛИТИКИ!!!###

for i in range(2022, 2023):
    print(i)
    # Загружаем данные с HH
    df = load_hh(i)
    # Парсим на колонки
    dfs, dfs_all = create_columns(df)
    dfs_all = dfs_all[['name']]
    # Создаём путь хранения
    writer = create_writer(i)
    # Показываем сколько всего вакансий
    dfs_all.to_excel(writer, sheet_name='Первая группа', startcol=0, index=False)
    # Удалаяем повторные вакансии
    dfs_all = dfs_all.drop_duplicates()
    dfs_all.to_excel(writer, sheet_name='Первая группа', startcol=1, index=False)
    # Создаём массив с названиями профессий(заголовки)
    professions_arr = []
    # Создаем массив с количеством каждой вакансии за упомянутый год
    share_professions = []
    # Общий массив колличества вакансий за год
    share_profession = []
    # Создаём пути для аналитики и результата по каждой профессии
    writer_names = pd.ExcelWriter(path_report + f'\\{i}.ShareNamesVacancy.xlsx', engine='xlsxwriter')
    writer_result_xlsx = pd.ExcelWriter(path_report + f'\\{i}.ResultVacancies.xlsx', engine='xlsxwriter')
    # Создаем счетчики количества профессий
    count_clear = 0
    count_deleted = 0
    # Создаём фрейм мусорных вакансий
    df_rubbish = dfs_all
    # Бежим циклом по вакансиям и распределяем их
    for names in prof_names:
        #Получаем очищенные вакансии и удалённые
        professions_clear, clear_prof, deleted_prof = get_data_prof(names, dfs_all)
        # Заполняем мусорные вакансии
        df_rubbish = df_rubbish.append(pd.concat([professions_clear, deleted_prof]).drop_duplicates(keep=False))
        #if names != 'C#' and names != 'C C++' and names != 'Delphi' and names != 'JavaScript' and names != 'Java' and names != 'PHP' and names != 'Python' and names != 'Ruby' and names != 'Sharepoint' and names != 'SQL':
        professions_arr.append(names)
        count_clear += len(professions_clear)
        count_deleted += len(deleted_prof)
        if len(deleted_prof) == 0:
            share_profession.append(f'{100}%')
        else:
            share_profession.append(f'{round(len(professions_clear) / (len(deleted_prof) + len(professions_clear))*100)}%')

    if count_deleted == 0:
        share_professions.append(f'{100}%')
    else:
        share_professions.append(f'{round((count_clear / len(dfs_all)) * 100)}%')
    # Печатаем мусор
    df_rubbish = df_rubbish.drop_duplicates(keep=False)
    df_rubbish.to_excel(writer, sheet_name='Вторая группа', startcol=0, index=False, header=None)
    share_professions.append(f'{count_clear}/{len(dfs_all)}')
    # Создаём фрейм количества всех профессий
    df_share_professions = pd.DataFrame(share_professions)
    # Колонки для подсчёта всех профессий
    columns = ['Доля профессий(%)', 'Доля профессий']
    # Дублирую массив для цсв для одной профессии
    share_cvs_prof = share_profession
    #ЦСВ по профессиям
    csv_dict[i] = share_cvs_prof
    # Фрейм по одной из профессий
    df_share_profession = pd.DataFrame(share_profession)
    df_share_profession = df_share_profession.transpose()
    df_share_profession.columns = professions_arr
    # df_share_profession = df_share_profession.loc[:, 'Программист':'Email-маркетолог']



    df_share_professions = df_share_professions.transpose()

    df_share_professions.to_excel(writer, sheet_name='Первая группа', startcol=2, header=columns,
                                  index=False)

    df_share_profession.to_excel(writer, sheet_name='Первая группа', startrow=0, startcol=4,
                                 index=False)

    #df_csv_data = pd.DataFrame(csv_dict, columns=['name', i])
    #df_csv_data.to_csv(path_report + f'\\csv\\{i}.Result_CSV.csv', sep=',', index=False, header=True)
    ###РАСКОМЕНТИТЬ ДЛЯ ПОКАЗА АНАЛИТИКИ!!!###
    # writer_names.save()
    # writer_result_xlsx.save()
    writer.save()

###РАСКОМЕНТИТЬ ДЛЯ ПОКАЗА АНАЛИТИКИ!!!###
# result_df_csv = pd.concat([pd.read_csv(f) for f in csv_dir.glob('*.csv')], ignore_index=True)
# result_df_csv.to_csv(path_report + f'\\csv\\result\\All professions.csv', index=False)
# print(csv_dict)
# print(dfs_all)
# for elem in df_prof_names:


# print(dfs_all)
'''
php = pd.concat([dfs_all[dfs_all['name'].str.contains('php')], dfs_all[dfs_all['name'].str.contains('пхп')]]) \
    .drop_duplicates(keep=False)
php_clear = php
for i in range(len(exceptions_words['php'])):
    php_clear = php_clear.loc[~php_clear['name'].str.contains(exceptions_words['php'][i])]

deleted_php = pd.concat([php, php_clear]).drop_duplicates(keep=False)

# print(php_clear)
# print(php)
# print(deleted_php)
# temp_php = deleted_php["name"]
# php_clear.insert(2, "deleted_name", deleted_php)
# print(php_clear)

# php.to_excel(writer, sheet_name="PHP", index=False)
php_clear.to_excel(writer, sheet_name="PHP Clear", index=False)
deleted_php.to_excel(writer, sheet_name="PHP Deleted", index=False)

python = pd.concat([dfs_all[dfs_all['name'].str.contains('python')], dfs_all[dfs_all['name'].str.contains('питон')]]) \
    .drop_duplicates(keep=False)
python_clear = python
for i in range(len(exceptions_words['python'])):
    python_clear = python_clear.loc[~python_clear['name'].str.contains(exceptions_words['python'][i])]

# print(python)
# python.to_excel(writer, sheet_name="Python", index=False)
# print(python_clear)
deleted_python = pd.concat([python, python_clear]).drop_duplicates(keep=False)
# print(deleted_python)
python_clear.to_excel(writer, sheet_name="Python Clear", index=False)
deleted_python.to_excel(writer, sheet_name="Python Deleted", index=False)

js = pd.concat([dfs_all[dfs_all['name'].str.contains('js')], dfs_all[dfs_all['name'].str.contains('javascript')],
                dfs_all[dfs_all['name'].str.contains('джаваскрипт')], dfs_all[dfs_all['name'].str
               .contains('яваскрипт')]]).drop_duplicates(keep=False)
js_clear = js

for i in range(len(exceptions_words['js'])):
    js_clear = js_clear.loc[~js_clear['name'].str.contains(exceptions_words['js'][i])]
# print(js_clear)
deleted_js = pd.concat([js, js_clear]).drop_duplicates(keep=False)
# print(deleted_js)
js_clear.to_excel(writer, sheet_name="JS Clear", index=False)
deleted_js.to_excel(writer, sheet_name="JS Deleted", index=False)

backend = pd.concat([dfs_all[dfs_all['name'].str.contains('backend')], dfs_all[dfs_all['name'].str.contains('бэкэнд')],
                     dfs_all[dfs_all['name'].str.contains('бэкенд')]]).drop_duplicates(keep=False)
backend_clear = backend

# for i in range(len(exceptions_words['backend'])):
#    backend_clear = backend_clear.loc[~backend_clear['name'].str.contains(exceptions_words['backend'][i])]

# deleted_backend = pd.contact([backend, backend_clear]).drop_dublicates(keep=False)

# print(backend)
backend.to_excel(writer, sheet_name="Backend-программист", index=False)
# backend_clear.to_excel(writer, sheet_name="Backend-программист Clear", index=False)
# deleted_backend.to_excel(writer, sheet_name="Backend-программист Clear", index=False)


c_sharp = pd.concat([dfs_all[dfs_all['name'].str.contains('c#')], dfs_all[dfs_all['name'].str.contains('c-sharp')],
                     dfs_all[dfs_all['name'].str.contains('c sharp')], dfs_all[dfs_all['name'].str
                    .contains('си шарп')], dfs_all[dfs_all['name'].str.contains('шарп')]]).drop_duplicates(keep=False)
c_sharp_clear = c_sharp

for i in range(len(exceptions_words['c#'])):
    c_sharp_clear = c_sharp_clear.loc[~c_sharp_clear['name'].str.contains(exceptions_words['c#'][i])]

deleted_c_sharp = pd.concat([c_sharp, c_sharp_clear]).drop_duplicates(keep=False)

# print(c_sharp_clear)
# print(deleted_c_sharp)
c_sharp_clear.to_excel(writer, sheet_name="C# Clear", index=False)
deleted_c_sharp.to_excel(writer, sheet_name="C# Deleted", index=False)

# c_plus = dfs_all[dfs_all['name'].str.contains(r"c++")]
# c_plus_clear = c_plus

# for i in range(len(exceptions_words['c++'])):
#    c_plus_clear = c_plus_clear.loc[~c_plus_clear['name'].str.contains(exceptions_words['c++'][i])]

# deleted_c_plus = pd.concat([c_plus, c_plus_clear]).drop_duplicates(keep=False)
# print(c_plus)
# c_plus.to_excel(writer, sheet_name="C++", index=False)


dfs_all = dfs_all[~dfs_all.index.isin(php.index)]
dfs_all = dfs_all[~dfs_all.index.isin(python.index)]
'''
# print(dfs_all)
# dfs_all.iloc[0:1000].to_excel(writer, sheet_name="Совпало", index=False)
# df2 = dfs_all[~dfs_all['name'].isin(aggregationList)]
# print (df2)
# df2.iloc[0:1000].to_excel(writer, sheet_name="НеСовпало", index=False)


# # Печать статистики
# # print(filename, "\t", df2["name"].count(), "\t", df2["key_skills"].count())
# df2 = df2.filter(['key_skills'], axis=1)
# # Убираем пустые key_skills
# df2 = df2[df2['key_skills'].notna()]
# # Сплитим key_skills по \n поскольку в вакансии они идут каждый key_skill с новой строки
# df2 = df2['key_skills'].str.split("\n", expand=True).stack().to_frame()
# # Удаляем все индексы из DataFrame
# df2.columns = ['skills']
# # Формируем новые индексы с 0 для DataFrame
# df2.reset_index(drop=True, inplace=True)
# # Считаем количество уникальных значений и засовываем их в новый DataFrame
# df2 = df2.value_counts().to_frame()
# # Формируем новые индексы с 0 для текущего DataFrame
# df2.reset_index(level=0, inplace=True)
# # Делаем красивые заголовки для столбцов
# df2.columns = ['Cкиллы', 'Частотность']
# # Открываем эксельку для отчета по профессии
# writer = pd.ExcelWriter(path_report + '\\2021-22.Общая.' + filename + '.xlsx',engine='xlsxwriter')
# # Записываем все скилллы в отчет по профессии
# df2.to_excel(writer, sheet_name="Все скиллы", index=False)
# # По всем группам скиллов формируем статистику
# for key_dict_lookup in dict_lookup.keys():
#     sum_group = []
#     list_item = dict_lookup[key_dict_lookup].keys()
#     group = list(dict_lookup[key_dict_lookup])
#     for key in dict_lookup[key_dict_lookup]:
#         sum_gr = df2[df2['Cкиллы'].isin(dict_lookup[key_dict_lookup][key])]
#         sum_gr = sum_gr['Частотность'].sum()
#         sum_group.append(sum_gr)
#     # Сортируем статистику
#     df = pd.DataFrame(list(zip(group, sum_group)), columns=['Группа скиллов', 'Частотность']).sort_values(by='Частотность', ascending=False)
#     # Убираем пустые группы
#     df = df.loc[df['Частотность'] != 0]
#     # Записываем статистику по скиллам
#     # df.to_excel(writer, sheet_name=key_dict_lookup, index=False)
# writer.save()
