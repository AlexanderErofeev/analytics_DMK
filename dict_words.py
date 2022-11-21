minus_words = \
    {
        'Преподователь': [],
        'Embedded-разработчик': ['руководитель', 'qa', 'manager', 'lead', 'teamlead', 'тест', 'team lead', 'test',
                                 'leader'],
        'Инженер-программист': ['1с', 'manager', 'директор', 'unity', 'руководитель', 'qa', '1c', 'микроконтрол',
                                'teamlead', 'препод', 'оператор', 'lead', 'тест', 'director', 'leader',
                                'quality assurance', 'тимлид', '1 c', '1 с', 'баз данн', 'team lead', 'test', 'game'],
        'Системный программист': ['руководитель', '1с', '1c', '1 с', 'lead', 'тест', 'team lead', 'администратор'],
        'Инженер систем': ['руководитель', '1с', '1c', '1 с', 'lead', 'тест', 'team lead', 'администратор'],
        'Desktop-разработчик': ['manager', '1с', 'тьютор', 'директор', 'unity', 'руководитель', 'qa', '1c', 'teamlead',
                                'backend', 'препод', 'оператор', 'lead', 'игр', 'fullstack', 'бэкенд', 'тест',
                                'director', 'leader', 'quality assurance', 'тимлид', 'тим лид', '1 c', '1 с',
                                'баз данн', 'team lead', 'test', 'game'],
        'Web-разработчик': ['manager', '1с', 'директор', 'tutor', 'unity', 'руководитель', 'qa', '1c', 'teamlead',
                            'аналитик', 'препод', 'менеджер', 'lead', 'оператор', 'дизайнер', 'тест', 'designer',
                            'leader', 'тимлид', 'тим лид', '1 c', '1 с', 'баз данн', 'team lead', 'test', 'game'],
        'Frontend-программист': ['репетитор', 'manager', '1с', 'тьютор', 'директор', 'преподаватель', 'tutor', 'unity',
                                 'руководитель', 'qa', '1c', 'jsoc', 'teamlead', 'препод', 'оператор', 'lead', 'тест',
                                 'director', 'leader', 'quality assurance', 'тимлид', 'тим лид', '1 с', 'баз данн',
                                 'team lead', 'test', 'game'],
        'Backend-программист': ['репетитор', 'manager', '1с', 'data science', 'тьютор', 'директор', 'tutor', 'unity',
                                'руководитель', 'qa', '1c', 'sdet', 'teamlead', 'учитель', 'data scientist', 'препод',
                                'оператор', 'lead', 'sql', 'тест', 'director', 'leader', 'quality assurance', 'тимлид',
                                'cms', 'тим лид', '1 с', 'баз данн', 'team lead', 'test', 'game'],
        'Fullstack-программист': ['unity', 'тимлид', 'руководитель', 'qa', 'manager', '1c', '1с', 'game', 'препод',
                                  'директор', 'lead', 'оператор', 'teamlead', 'тест', 'team lead', 'test', 'tutor',
                                  'leader'],
        'Mobile-разработчик': ['manager', 'python', '1с', 'тьютор', 'автор', 'директор', 'механик', 'бизнес', 'unity',
                               'руководитель', 'qa', '1c', 'owner', 'teamlead', 'java', 'аналитик', 'эксплуатац',
                               'маркетолог', 'аниматор', 'препод', 'оператор', 'lead', 'дизайнер', 'тест', 'ремонт',
                               'автомобиль', 'designer', 'director', 'leader', 'quality assurance', 'тимлид',
                               'художник', 'баз данн', 'team lead', 'test', 'game'],
        'IOS-разработчик': ['manager', 'тьютор', 'директор', 'unity', 'руководитель', 'qa', 'teamlead', 'препод',
                            'оператор', 'lead', 'дизайнер', 'тест', 'ремонт', 'director', 'leader', 'тимлид', 'тим лид',
                            'team lead', 'test', 'game'],
        'Android-разработчик': ['unity', 'тимлид', 'руководитель', 'qa', 'тим лид', 'manager', 'препод', 'директор',
                                'team lead', 'lead', 'оператор', 'дизайнер', 'teamlead', 'ремонт', 'тест', 'test',
                                'game', 'leader'],
        'Администратор баз данных': ['manager', '1с', 'директор', 'tutor', 'unity',
                                     'руководитель', 'qa', '1c', 'teamlead', 'backend', 'erp', 'препод',
                                     'lead', 'тест', 'director', 'leader', 'quality assurance', 'тимлид',
                                     '1 c', '1 с', 'team lead', 'test', 'game'],
        'Devops-инженер': ['тимлид', 'руководитель', 'директор', 'lead', 'teamlead', 'преподаватель', 'team lead',
                           'director', 'leader'],
        'Специалист по анализу данных': ['руководитель', 'qa', 'директор', 'lead', 'teamlead', 'тест', 'team lead',
                                         'director', 'leader'],
        'Системный администратор': ['devops', 'тех поддержка', 'техподдержка'],
        'Тестировщик (QA-инженер)': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead',
                                     'director', 'leader'],
        'Специалист техподдержки': ['1с'],
        'Инженер': ['software', 'frontend', 'dba', 'manager', 'python', 'programmer', 'admin', 'site', 'js', 'it',
                    'data', 'voip', 'support', 'директор', 'бдд', 'ml', 'full stack', 'scala', 'framework', 'graph',
                    'devops', 'developer', 'руководитель', 'scient', 'qa', 'oracle', 'hpc', 'sysop', '1c', 'android',
                    'ит', 'dev', 'teamlead', 'linux', 'систем', 'compil', 'web', '1с', 'java', 'micros', 'backend',
                    'внедрен', 'cloud', 'network', 'security', 'desktop', 'video', 'lead', 'mobile', 'embed',
                    'информаци', 'тест', 'c#', 'director', 'leader', 'quality assurance', 'тимлид', 'toolchain', 'php',
                    'поддрежк', 'тим лид', 'лидер', 'программист', 'разработчик', 'team lead', 'test', 'ios', 'cv',
                    'system', 'rnd'],
        'Аналитик': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead', 'director',
                     'leader'],
        'Специалист по информационной безопасности': ['тимлид', 'руководитель', 'директор', 'lead', 'teamlead',
                                                      'team lead', 'director', 'leader'],
        'ERP-специалист': ['1с', 'директор', 'unity', 'руководитель', 'qa', '1c', 'teamlead', 'препод',
                           'оператор', 'lead', 'тест', 'director', 'leader', 'quality assurance', 'тимлид', 'баз данн',
                           'team lead', 'test', 'game', 'клиент', 'сайт', 'интернет магазин'],
        '1С-разработчик': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead', 'leader'],
        'Разработчик игр (GameDev)': ['quality assurance', 'тимлид', 'руководитель', 'иллюстратор', 'qa', 'дизайн',
                                      'директор', 'lead', 'teamlead', 'design', 'тест', 'team lead', 'test', 'director',
                                      'leader'],
        'Руководитель ИТ-проектов': [],
        'Web-мастер': [],
        'Контент-менеджер': ['smm'],
        'UX/UI дизайнер': ['gui', 'programmer', 'директор', 'full stack', 'аналит', 'requir', 'руководитель', 'redux',
                           'sapui', 'teamlead', 'linux', 'builder', 'исслед', 'редактор', 'equip', 'учитель',
                           'liquidit', 'nuxt', 'менеджер', 'lead', 'копирай', 'recruiter', 'director', 'leader',
                           'тимлид', 'исследов', 'luxe', 'develop', 'программист', 'team lead', 'разработчик', 'editor',
                           'писат', 'writ', 'acqui'],
        'Менеджер IT-проекта': [],

        'Менеджер по работе с клиентами': [],
        'Менеджер по работе с партнерами': [],
        'Менеджер по развитию': [],

        'Маркетолог': ['dev', 'аналитик', 'верстальщик', 'front'],
        'SEO-специалист': [],
        'SMM-специалист': [],
        'C#': ['qa', 'test', 'тест', 'quality assurance', 'препод', 'tutor', 'тьютор', 'репетитор', 'репититор',
               'учитель', 'backend', 'бэкэнд', 'game', 'игр', 'unity', 'team lead', 'тимлид', 'тим лид', 'teamlead',
               'lead', 'менджер', 'manager', 'руководитель', 'директор', 'leader', 'director', '1c', '1с', 'game',
               'unity', '1 c', '1 с', 'баз данн', 'оператор'],
        'C C++': ['quality assurance', 'тимлид', 'руководитель', 'unity', 'qa', 'manager', '1с', 'тьютор', 'препод',
                  'lead', 'teamlead', 'баз данн', 'тест', 'team lead', 'test', 'game', 'director', 'leader'],
        'Delphi': ['руководитель', 'manager', '1c', '1с', 'препод', 'lead', 'баз данн', 'тест', 'team lead', 'test',
                   'leader'],
        'JavaScript': ['manager', '1с', 'тьютор', 'преподаватель', 'руководитель', 'qa', 'jsoc', '1c', 'teamlead',
                       'lead', 'тест', 'director', 'leader', 'quality assurance', 'тимлид', '1 с', 'баз данн',
                       'team lead', 'test'],
        'Java': ['репетитор', 'manager', '1с', 'тьютор', 'директор', 'tutor', 'unity', 'руководитель', 'qa', '1c',
                 'javascript', 'teamlead', 'препод', 'lead', 'тест', 'director', 'leader', 'quality assurance',
                 'тимлид', 'тим лид', '1 с', 'баз данн', 'team lead', 'test', 'game'],
        'PHP': ['репетитор', '1с', 'manager', 'директор', 'преподаватель', 'unity', 'руководитель', '1c', 'teamlead',
                'sql', 'оператор', 'lead', 'director', 'leader', 'тимлид', 'cms', 'тим лид', 'ученик', '1 с',
                'баз данн', 'team lead', 'game', 'тестировщик'],
        'Python': ['тестировщик', 'qa', 'преподаватель', 'тест', 'quality assurance', 'test', 'sdet', 'учитель',
                   'репетитор', 'репититор', 'data science', 'data scientist', 'team lead', 'тимлид','тим лид',
                   'teamlead', 'lead', 'менджер', 'manager', 'руководитель', 'директор', 'leader', 'director', '1c',
                   '1с', 'game', 'unity', '1 c', '1 с', 'баз данн', 'оператор'],
        'Ruby': ['unity', 'тимлид', 'руководитель', 'qa', 'тим лид', 'manager', 'препод', 'директор', 'lead',
                 'оператор', 'teamlead', 'тест', 'team lead', 'test', 'leader'],
        'Sharepoint': ['unity', 'руководитель', 'qa', 'manager', '1c', '1с', 'препод', 'директор', 'lead', '1 c',
                       'teamlead', 'баз данн', 'тест', 'team lead', 'test', 'tutor', 'leader'],
        'SQL': ['manager', '1с', 'директор', 'tutor', 'unity', 'руководитель', 'qa', '1c', 'teamlead', 'препод',
                'оператор', 'lead', 'тест', 'director', 'leader', 'тимлид', 'тим лид', '1 c', '1 с', 'баз данн',
                'team lead', 'test', 'game'],
        'Программист': ['репетитор', 'frontend', 'manager', '1с', 'пхп', 'c sharp', 'js', 'python', 'тьютор', 'game',
                        'директор', 'ruby', 'мобиль', ' си ', 'питон', 'tutor', 'инженер программист', 'рнр', 'unity',
                        'руководитель', 'инженер', 'qa', '1c', 'фулстэк', 'микроконтрол', 'с#', 'android', 'javascript',
                        'front', 'версталь', 'teamlead', 'фронтенд', 'sharepoint', 'web', 'java', 'backend', 'delphi',
                        'бэкэнд', 'вёрстка', 'веб', 'препод', 'sql', 'lead', 'mobile', 'оператор', 'fullstack',
                        'бэкенд', 'engineer', 'тест', 'microcontr', 'frontеnd', 'c#', 'director', 'leader',
                        'quality assurance', 'тимлид', 'php', 'тим лид', 'системный программист', 'андроид', 'руби',
                        '1 c', '1 с', 'баз данн', 'ios', 'team lead', 'test', 'мобайл', 'системный', 'system prog'],
        'ML разработчик': [],

        'Мусор': [],
        'Оператор станков чпу': [],

        'Языки программирования': [],
        'Специалист': [],
    }

plus_words = \
    {
        'Преподователь': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'методист', 'обуч', 'тренер'],
        'Embedded-разработчик': ['microcontr', 'микроконтрол', 'embedded'],
        'Инженер-программист': ['engineer', 'инженер программист'],
        'Системный программист': ['system prog', 'системный программист'],
        'Инженер систем': ['инженер систем', 'системный инженер', 'system engineer'],
        'Desktop-разработчик': ['desktop', 'desktop', 'десктоп', 'net'],
        'Web-разработчик': ['web develop', 'веб разработ', 'web разработ', 'web programmer', 'web программист',
                            'веб программист', 'битрикс разработчик', 'bitrix разработчик', 'drupal разработчик', 'cms разработчик',
                            'wordpress разработчик', 'wp разработчик', 'joomla разработчик', 'drupal developer', 'cms developer',
                            'wordpress developer', 'wp developer', 'joomla developer'],
        'Frontend-программист': ['frontend', 'фронтенд', 'вёрстка', 'верстка', 'верста', 'front end',
                                 'angular', 'html', 'css', 'react', 'vue'],
        'Backend-программист': ['backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд', 'back end', 'бэк энд', 'бэк енд',
                                'django', 'flask', 'laravel', 'yii', 'symfony'],
        'Fullstack-программист': ['fullstack', 'фулстак', 'фуллстэк', 'фулстэк', 'full stack'],
        'Mobile-разработчик': ['mobile', 'мобайл', 'мобиль'],
        'IOS-разработчик': ['ios'],
        'Android-разработчик': ['android', 'андроид', 'andorid', 'andoroid', 'andriod', 'andrind', 'xamarin'],
        'Администратор баз данных': ['баз данных', 'оператор баз данных', 'базы данных', 'oracle',
                                     'mysql', 'data base', 'database', 'dba', 'bd', 'бд', 'базами данны'],
        'Devops-инженер': ['devops', 'development operations'],
        'Специалист по анализу данных': ['data scientist', 'data science', 'анализу данны', 'анализ данны'],
        'Системный администратор': ['system admin', 'сисадмин', 'сис админ', 'системный админ', 'cистемный админ', 'администратор систем'],
        'Тестировщик (QA-инженер)': ['qa', 'test', 'тест', 'quality assurance'],
        'Специалист техподдержки': ['техподдер', 'тех поддерж', 'technical support engineer', 'поддерж', 'support'],
        'Аналитик': ['analytic', 'аналитик', 'analyst'],
        'Специалист по информационной безопасности': ['безопасност', 'защит',
                                                      'information security specialist', 'information security'],
        'ERP-специалист': ['erp', 'enterprise resource planning', 'abap', 'crm', 'help desk', 'helpdesk',
                           'service desk', 'servicedesk', 'bi', 'sap', 'внедрен', 'сопровожден'],
        '1С-разработчик': ['1с разработчик', '1c разработчик', '1с', '1c', '1 c', '1 с'],
        'Разработчик игр (GameDev)': ['game', 'unity', 'игр'],
        'Руководитель ИТ-проектов': ['team lead', 'тимлид', 'тим лид', 'teamlead', 'lead', 'руководит', 'директор',
                                     'leader', 'director', 'начальник'],
        'Web-мастер': ['web мастер', 'веб мастер', 'администратор сайта', 'web спец', 'веб спец', 'web spec'],
        'Контент-менеджер': ['content manager', 'контент менеджер'],
        'UX/UI дизайнер': ['design', 'ux', 'ui', 'дизайн', 'иллюстратор'],
        'Менеджер IT-проекта': ['product manag', 'project manag', 'менеджер проект', 'менеджер продукт', 'менеджер по продукт',
                                'менеджер it проект', 'менеджер ит проект', 'менеджер интернет проект', 'продакт менедж',
                                'проджект менедж', 'продукт менедж', 'проект менедж', 'проектный менедж',
                                'менеджер по проект', 'менеджер по сопровождению проект', 'управление проект',
                                'управлению проект', 'project менедж', 'администратор проект'],

        'Менеджер по работе с клиентами': ['по работе с корпоративными клиентами', 'по работе с клиентами', 'по работе с заказчиками',
                                           'account manager', 'по сопровождению клиентов', 'account менеджер', 'аккаунт менеджер',
                                           'обслуживанию клиентов', 'обслуживание клиентов'],
        'Менеджер по работе с партнерами': ['по работе с партнерами'],
        'Менеджер по развитию': ['менеджер по развитию'],

        'Маркетолог': ['affiliate', 'маркет', 'market', 'advisor', 'директолог', 'реклам', 'продвижен', 'таргет'],
        'SEO-специалист': ['seo', 'sео'],
        'SMM-специалист': ['smm', 'social media marketing', 'смм'],

        'C#': ['c#', 'c sharp', 'шарп', 'с#'],
        'C C++': ['c++', 'с++'],
        'Delphi': ['delphi', 'делфи'],
        'JavaScript': ['js', 'javascript'],
        'Java': ['java', 'ява', 'джава'],
        'PHP': ['php', 'пхп', 'рнр'],
        'Python': ['python', 'питон', 'пайтон'],
        'Ruby': ['ruby', 'руби'],
        'Sharepoint': ['sharepoint'],
        'SQL': ['sql'],
        'ML разработчик': ['ml', 'machine learning', 'нейро'],

        'Мусор': ['механик', 'токарь', 'конструктор', 'монтажник', 'переводчик', 'экономист', 'журналист', 'бухгалтер',
                  'аудитор', 'строитель', 'секретарь', 'электрик', 'кассир', 'инспектор', 'курьер', 'юрист', 'бригадир',
                  'фотограф', 'режиссер', 'электроснабжен', 'фрезеровщик', 'кабельщик', 'супервайзер', 'мерчендайзер',
                  'кладовщик', 'сценарист', 'hr специалист', 'pr специалист', 'pr менеджер', 'pr manager', 'техник',
                  'ремонт', 'подбору персонал', 'доставк', 'закупк', 'тендер', 'салона связи', 'салон связи', 'развити'
                  'call center', 'колл центр', 'менеджер по продажам', 'менеджер продаж', 'специалист по продажам', 'sales', 'специалист в отдел продаж',
                                 'менеджер отдела продаж', 'специалист отдела продаж', 'менеджер в отдел продаж', 'продаж', 'продавец'],

        'Оператор станков чпу': ['чпу', 'cnc'],

        'Языки программирования': ['scala', 'go', 'vba', 'perl', 'rlang', 'swift', 'typescript', 'flash', 'cotlin', 'visual basic', 'pascal'],
        'Инженер': ['engineer', 'инженер'],
        'Программист': ['programmer', 'программист'],
        'Специалист': ['специалист'],
    }

# print(len(plus_words))  # Пропали 2 профессии
# print(len(minus_words))
