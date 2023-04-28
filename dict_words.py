minus_words = \
    {
        'Преподаватель по программированию': [],
        'Программист микроконтроллеров': ['руководитель', 'qa', 'manager', 'lead', 'teamlead', 'тест', 'team lead', 'test',
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
        'Верстальщик': ['репетитор', 'manager', '1с', 'тьютор', 'директор', 'преподаватель', 'tutor', 'unity',
                                 'руководитель', 'qa', '1c', 'jsoc', 'teamlead', 'препод', 'оператор', 'lead', 'тест',
                                 'director', 'leader', 'quality assurance', 'тимлид', 'тим лид', '1 с', 'баз данн',
                                 'team lead', 'test', 'game', 'северсталь'],
        'Frontend-разработчик': ['репетитор', 'manager', '1с', 'тьютор', 'директор', 'преподаватель', 'tutor', 'unity',
                                 'руководитель', 'qa', '1c', 'jsoc', 'teamlead', 'препод', 'оператор', 'lead', 'тест',
                                 'director', 'leader', 'quality assurance', 'тимлид', 'тим лид', '1 с', 'баз данн',
                                 'team lead', 'test', 'game'],
        'Backend-разработчик': ['репетитор', 'manager', '1с', 'data science', 'тьютор', 'директор', 'tutor', 'unity',
                                'руководитель', 'qa', '1c', 'sdet', 'teamlead', 'учитель', 'data scientist', 'препод',
                                'оператор', 'lead', 'sql', 'тест', 'director', 'leader', 'quality assurance', 'тимлид',
                                'cms', 'тим лид', '1 с', 'баз данн', 'team lead', 'test', 'game'],
        'Fullstack-разработчик': ['unity', 'тимлид', 'руководитель', 'qa', 'manager', '1c', '1с', 'game', 'препод',
                                  'директор', 'lead', 'оператор', 'teamlead', 'тест', 'team lead', 'test', 'tutor',
                                  'leader'],
        'Разработчик мобильных приложений': ['manager', 'python', '1с', 'тьютор', 'автор', 'директор', 'механик', 'бизнес', 'unity',
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
        'SQL-разработчик': ['manager', '1с', 'директор', 'tutor', 'unity',
                                     'руководитель', 'qa', '1c', 'teamlead', 'backend', 'erp', 'препод',
                                     'lead', 'тест', 'director', 'leader', 'quality assurance', 'тимлид',
                                     '1 c', '1 с', 'team lead', 'test', 'game'],
        'Devops-инженер': ['тимлид', 'руководитель', 'директор', 'lead', 'teamlead', 'преподаватель', 'team lead',
                           'director', 'leader'],
        'Data scientist': ['руководитель', 'qa', 'директор', 'lead', 'teamlead', 'тест', 'team lead',
                                         'director', 'leader'],
        'Системный администратор': ['devops', 'тех поддержка', 'техподдержка'],
        'QA-инженер': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead',
                                     'director', 'leader'],
        'Специалист технической поддержки': ['1с'],
        # 'Инженер': ['software', 'frontend', 'dba', 'manager', 'python', 'programmer', 'admin', 'site', 'js', 'it',
        #             'data', 'voip', 'support', 'директор', 'бдд', 'ml', 'full stack', 'scala', 'framework', 'graph',
        #             'devops', 'developer', 'руководитель', 'scient', 'qa', 'oracle', 'hpc', 'sysop', '1c', 'android',
        #             'ит', 'dev', 'teamlead', 'linux', 'систем', 'compil', 'web', '1с', 'java', 'micros', 'backend',
        #             'внедрен', 'cloud', 'network', 'security', 'desktop', 'video', 'lead', 'mobile', 'embed',
        #             'информаци', 'тест', 'c#', 'director', 'leader', 'quality assurance', 'тимлид', 'toolchain', 'php',
        #             'поддрежк', 'лидер', 'программист', 'разработчик', 'team lead', 'test', 'ios', 'cv',
        #             'system', 'rnd'],
        'Аналитик': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead', 'director',
                     'leader'],
        'Специалист по информационной безопасности': ['тимлид', 'руководитель', 'директор', 'lead', 'teamlead',
                                                      'team lead', 'director', 'leader'],
        'ERP-инженер': ['1с', 'директор', 'unity', 'руководитель', 'qa', '1c', 'teamlead', 'препод',
                           'оператор', 'lead', 'тест', 'director', 'leader', 'quality assurance', 'тимлид',
                           'team lead', 'test', 'game', 'клиент', 'сайт', 'интернет магазин'],
        '1C-программист': ['тимлид', 'руководитель', 'тим лид', 'директор', 'lead', 'teamlead', 'team lead', 'leader'],
        'SAP-консультант': [],
        # 'Oracle-разработчик': [],
        'Разработчик игр': ['quality assurance', 'тимлид', 'руководитель', 'иллюстратор', 'qa', 'дизайн',
                                      'директор', 'lead', 'teamlead', 'design', 'тест', 'team lead', 'test', 'director',
                                      'leader'],
        'Руководитель ИТ-проектов': [],
        'Web-мастер': [],
        'Контент-менеджер': ['smm'],
        'Web-дизайнер': ['gui', 'programmer', 'директор', 'full stack', 'аналит', 'requir', 'руководитель', 'redux',
                           'sapui', 'teamlead', 'linux', 'builder', 'исслед', 'редактор', 'equip', 'учитель',
                           'liquidit', 'nuxt', 'менеджер', 'lead', 'копирай', 'recruiter', 'director', 'leader',
                           'тимлид', 'исследов', 'luxe', 'develop', 'программист', 'team lead', 'разработчик', 'editor',
                           'писат', 'writ', 'acqui'],
        'Менеджер IT-проекта': [],


        'Менеджер HardWare': ['csv', 'sale', 'продаж', 'develop', 'разработч', 'программист', 'seo', 'сет',
                              'клиент', 'лиц', 'hr', 'мест', 'данн', 'сайт', 'веб', 'web', 'репутац', 'отдел',
                              'бригадир', 'сервис', 'управлен', 'гибщик', 'газорез', 'риск', 'техник', 'абонент',
                              'информаци', 'качест', 'кол', 'call', 'security', 'pr manager',
                              'pr менеджер', 'токарь', 'фрезеровщик'],
        'Менеджер SoftWare': ['продаж', 'торгов', 'отдел', 'develop', 'разработч', 'программист', 'programmer',
                              'коммуник', 'communic', 'системный инж', 'system engin', 'ремонт',
                              'сервис', 'банкомат', 'компьют', 'рабочих мест', 'кадр', 'sale', 'пк',
                              'market', 'architect', 'сет', 'сист', 'оргтехник', 'оборуд', 'терминал', 'технич', 'бригадир',
                              'writer', 'hr', 'кол', 'привлеч', 'клиент', 'security', 'pr manager',
                              'pr менеджер', 'техник'],
        'Специалист по автоматизации': [],
        'Бизнес-специалист': [],
        #'Контракт-специалист': [],
        'Специалист по документации': [],
        'Инженер сетей': [],
        'Сервисный инженер': ['апк', 'пкд'],
        'Инженер-электроник': [],
        'Pre-sale инженер': [],
        'Цифровой специалист': [],
        'Менеджер по работе с клиентами': [],
        'Менеджер по работе с партнерами': [],
        'Менеджер по развитию': [],
        'Менеджер в отделы': ['pr manager', 'pr менеджер'],
        'Интернет маркетолог': ['dev', 'аналитик', 'верстальщик', 'front'],
        'SEO-специалист': [],
        'SMM-менеджер': [],
        'E-mail маркетолог': [],
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
        # 'SQL': ['manager', '1с', 'директор', 'tutor', 'unity', 'руководитель', 'qa', '1c', 'teamlead', 'препод',
        #         'оператор', 'lead', 'тест', 'director', 'leader', 'тимлид', 'тим лид', '1 c', '1 с', 'баз данн',
        #         'team lead', 'test', 'game'],
        'Программист-разработчик': ['репетитор', 'frontend', 'manager', '1с', 'пхп', 'c sharp', 'js', 'python', 'тьютор', 'game',
                        'директор', 'ruby', 'мобиль', ' си ', 'питон', 'tutor', 'инженер программист', 'рнр', 'unity',
                        'руководитель', 'инженер', 'qa', '1c', 'фулстэк', 'микроконтрол', 'с#', 'android', 'javascript',
                        'front', 'версталь', 'teamlead', 'фронтенд', 'sharepoint', 'web', 'java', 'backend', 'delphi',
                        'бэкэнд', 'вёрстка', 'веб', 'препод', 'sql', 'lead', 'mobile', 'оператор', 'fullstack',
                        'бэкенд', 'engineer', 'тест', 'microcontr', 'frontеnd', 'c#', 'director', 'leader',
                        'quality assurance', 'тимлид', 'php', 'тим лид', 'системный программист', 'андроид', 'руби',
                        '1 c', '1 с', 'баз данн', 'ios', 'team lead', 'test', 'мобайл', 'системный', 'system prog'],
        'Machine learning-инженер': [],

        'Мусор': [],
        'Инженер АСУ ТП': [],

        'Языки программирования': [],
        # 'Специалист': [],
        # 'Менеджер': []
    }

plus_words = \
    {
        'Преподаватель по программированию': ['препод', 'учитель', 'tutor', 'тьютор', 'репетитор', 'методист', 'обуч', 'тренер'], #soft

        'Программист микроконтроллеров': ['microcontr', 'микроконтрол', 'embedded'], #hard
        'Инженер-программист': [['инженер', 'программист'], ['it', 'инженер'],#soft
                                ['инженер', 'разработчик']],
        'Системный программист': [['system', 'prog'], ['систем', 'програм']],#soft
        'Специалист технической поддержки': [['тех', 'поддерж'], ['technical', 'support', 'engineer'],  # soft
                                    ['клиент', 'поддерж'], ['customer', 'support'], ['client', 'support'],
                                    ['клиент', 'support'],
                                    ['клієнт', 'підтримки'], ['contact', 'center'],
                                    ['call', 'center'], ['колл', 'центр'], ['call', 'центр']],
        'Инженер систем': [['инженер', 'систем'], ['system', 'engineer'],#soft
                           ['cистем', 'инженер'],
                           # Новинка
                           ['технич', 'специалист'], ['специалист', 'систем']],
        'Desktop-разработчик': ['desktop', 'десктоп', 'net'],#soft
        'Web-разработчик': [['web', 'develop'], ['веб', 'разработ'], ['web', 'разработ'], ['web', 'program'],#soft
                            ['web', 'програм'], ['веб', 'програм'], ['битрикс', 'разработ'],
                            ['bitrix', 'разработ'], ['drupal', 'разработ'], ['cms', 'разработ'],
                            ['wordpress', 'разработ'], ['wp', 'разработ'], ['joomla', 'разработ'],
                            ['drupal', 'develop'], ['cms', 'develop'], ['специалист', 'wp'],
                            ['wordpress', 'develop'], ['wp', 'develop'], ['joomla', 'develop'],
                            ['bitrix', 'develop'], ['bitrix', 'специалист'], ['специалист', 'drupal']],
        'Верстальщик': ['html', 'css', 'вёрстка', 'верстка', 'верста'],
        'Frontend-разработчик': ['frontend', 'фронтенд', 'front end',#soft
                                 'angular', 'react', 'vue'],
        'Backend-разработчик': ['backend', 'бэкэнд', 'бэкенд', 'бекенд', 'бекэнд', 'back end', 'бэк энд', 'бэк енд',#soft
                                'django', 'flask', 'laravel', 'yii', 'symfony'],
        'Fullstack-разработчик': ['fullstack', 'фулстак', 'фуллтак', 'фуллстэк', 'фулстэк', 'full stack'],#soft
        'Разработчик мобильных приложений': ['mobile', 'мобайл', 'мобиль', 'мобільний'],#soft
        'IOS-разработчик': ['ios'],#soft
        'Android-разработчик': ['android', 'андроид', 'andorid', 'andoroid', 'andriod', 'andrind', 'xamarin'],#soft
        'Администратор баз данных': [['data', 'base'], 'db', 'bd', 'бд',#soft
                                     ['баз', 'данн'], 'oracle', 'оракл', ],
        'SQL-разработчик': ['sql'],
        'Devops-инженер': ['devops', ['develop', 'operat'], 'devоps'],#soft
        'Data scientist': [['data', 'scien'], ['анализ', 'данн'], ['аналит', 'данн'],#soft
                                         # Посмотрим
                                         ['обработ', 'данн']],
        'Системный администратор': [['system', 'admin'], ['сис', 'админ'], ['cис', 'админ'],#soft
                                    ['сис', 'адмін'],
                                    # Новинка
                                    # ['специалист', 'админ']
                                    ],
        'QA-инженер': ['qa', 'test', 'тест', ['quality', 'assurance']],#soft
        'Аналитик': ['analytic', 'аналитик', 'analyst', 'аналітик'], #soft
        'Специалист по информационной безопасности': ['безопасност', 'защит', #soft
                                                     #['information', 'security'],
                                                     ['фахівець', 'служби', 'безпеки'], # ['cyber', 'security'],
                                                      'security',
                                                      ' иб'],
        'ERP-инженер': ['erp', ['enterprise', 'resource', 'planning'], 'abap', 'crm', 'сrm', # ['crm', 'специалист'], ['crm', 'инженер'], soft
                            # ['crm', 'менедж'], ['crm', 'special'], ['crm', 'manager'],
                           ['help', 'desk'],
                           ['service', 'desk'], ['busin', 'intell'], 'внедрен', 'сопровожден'],
        '1C-программист': ['1с', '1c', '1 c', '1 с'], #soft
        'SAP-консультант': ['sap'], #soft
        # 'Oracle-разработчик': ['oracle', 'оракл'],
        'Разработчик игр': ['game', 'unity', 'игр', 'unreal'], #soft
        'Руководитель ИТ-проектов': [['тим', 'лид'], 'lead', 'руководит', 'директор', #soft
                                     'director', 'начальник', 'лидер', ['управл', 'проект'], 'керівник',
                                     'chief'],
        'Web-мастер': [['web', 'мастер'], ['веб', 'мастер'], ['админ', 'сайт'], ['web', 'спец'], #soft
                       ['веб', 'спец'], ['web', 'spec'],
                       # Новинка
                       ['менедж', 'интернет', 'магазин']],
        'Контент-менеджер': [['content', 'manager'], ['контент', 'менеджер']], #soft
        'Web-дизайнер': ['design', 'ux', 'ui', 'дизайн', 'иллюстр'], #soft
        'Менеджер IT-проекта': [['product', 'manag'], ['project', 'manag'], #?
                                ['менеджер', 'продукт'], ['продакт', 'менедж'],
                                ['проджект', 'менедж'], ['проект', 'менедж'],
                                ['управлен', 'проект'], ['project', 'менедж'], ['админ', 'проект'],
                                ['менеджер', 'проектів'], ['менеджер', 'produc'], ['product', 'specialist'],
                                # Новинка
                                ['инженер', 'проект'], ['специалист', 'проект']],
        'Менеджер HardWare': [['технологич', 'процесс'], 'hardware', #hard
                              ['разработ', 'аппара'], 'электронщик',
                              ['management', 'engin'], ['специалист', 'управл'],
                              ['product', 'engine'], ['data', 'processing'],
                              # ['специалист', 'обработке', 'данных'],
                              ['tooling', 'engine'], ['оператор', 'эвм'],
                              'станк', 'обслуживан', 'эксплуатац', 'сопровожд', 'поддержив'
                              ],

        'Менеджер SoftWare': ['software', 'корпоративн', ['програм', 'обеспечен'], #soft
                              'wms'
                              'corporate'],
        'Специалист по автоматизации': [# Новинка hard
                                                ['инженер', 'автоматиз'], ['специалист', 'оборудования'],
                                                ['специалист', 'автоматиз'], ['automation', 'specialist'],
                                                ['обслуживан', 'оборудования'],
                                               ['обслуживан', 'систем'],
                                               ['обслуживан', 'банкоматов'],
                                               ['обслуживан', 'станций'], ['обслуживан', 'опс'],
                                               ['обслуживан', 'устройств'],
                                               ['обслуживан', 'терминалов']],
        # Новинка
        'Бизнес-специалист': [['business', 'specialist'], ['бизнес', 'специалист'], ['business', 'manager'],
                              ['business', 'менеджер'], ['бизнес', 'менеджер']], #гум
        # Новинка
        'Специалист по документации': [['specialist', 'document'], ['специалист', 'документ'], #гум
                                       ['специалист', 'document'], ['инженер', 'документ'], ['технич', 'писатель']],
        # Новинка
        'Инженер-электроник': [['инженер', 'электросвязи'], ['инженер', 'электроник'], ['специалист', 'электроник'], #hard
                                 ['специалист', 'электромонтер'], ['специалист', 'электросвязи']
                                 ],
        # Новинка
        'Инженер сетей': [['инженер', 'сет'], ['инженер', 'связ'], ['инженер', 'cisco'], ['инженер', 'cетевой'], #hard
                             ['специалист', 'связ'], ['специалист', 'сет'], ['менеджер', 'связ'],
                             ['менеджер', 'сет'], ],
        # Новинка
        'Сервисный инженер': [['инженер', 'сервис'], ['инженер', 'оборудован'], ['инженер', 'пк'], #hard
                              ['cервис', 'инженер'], ['специалист', 'сервис'], # 'ремонт'
                              ],
        # Новинка
        'Pre-sale инженер': [['pre', 'sale', 'инженер'], ['пре', 'сеил', 'инженер'], # гум
                             ['присейл', 'инженер'], ['пресэйл', 'инженер'], ['пресейл', 'инженер']],
        # Новинка
        'Цифровой специалист': [['digital', 'специалист'], ['digital', 'specia'], ['digital', 'manag'], # soft
                                ['digital', 'менедж'], ['digital', 'иженер'], ['digital', 'инженер']],
        'Менеджер по работе с клиентами': [ # Новинка  гум
                                           ['специалист', 'клиент'], ['инженер', 'клиент'],
                                           ['специалист', 'заказчик'], ['менеджер', 'заказчик'], ['менеджер', 'клиент'],
                                           ['account', 'manager'], ['account', 'менеджер'], ['инженер', 'заказчик'],
                                           ['аккаунт', 'менеджер'],
                                            ['customer', 'manag'], ['customer', 'менедж'], ['customer', 'special'],
                                            ['customer', 'специал']],
                                            # Новинка
        'Менеджер по работе с партнерами': [['специалист', 'партнер'], ['менеджер', 'партнер'], # гум
                                            ['инженер', 'партнер']],
        'Менеджер по развитию': [['менедж', 'развит']], # гум
        'Менеджер в отделы': [['инженер', 'отдел'], ['менеджер', 'отдел'], ['специалист', 'отдел']], # гум
        'Интернет маркетолог': ['affiliate', 'маркет', 'market', 'advisor', 'директолог', 'реклам', 'продвижен', 'таргет'], # гум
        'SEO-специалист': ['seo', 'sео'], # soft
        'SMM-менеджер': ['smm', 'смм', 'таргетолог', 'cmm', 'cмм', # soft
                           ['social', 'media']],
        'E-mail маркетолог': ['e mail', 'e-mail', 'email'],

        'C#': ['c#', 'c sharp', 'шарп', 'с#'], #SOFT
        'C C++': ['c++', 'с++'],
        'Delphi': ['delphi', 'делфи'],
        'JavaScript': ['js', 'javascript'],
        'Java': ['java ', 'ява', 'джава '],
        'PHP': ['php', 'пхп', 'рнр'],
        'Python': ['python', 'питон', 'пайтон'],
        'Ruby': ['ruby', 'руби'],
        'Sharepoint': ['sharepoint'],
        # 'SQL': ['sql'],
        'Machine learning-инженер': ['ml', ['machine', 'learning'], 'нейро'],

        'Мусор': ['механик', 'токарь', 'конструктор', 'монтажник', 'переводчик', 'экономист', 'журналист', 'бухгалтер',
                  'аудитор', 'строитель', 'секретарь', 'электрик', 'кассир', 'инспектор', 'курьер', 'юрист', 'бригадир',
                  'фотограф', 'режиссер', 'электроснабжен', 'фрезеровщик', 'кабельщик', 'супервайзер', 'мерчендайзер',
                  'кладовщик', 'сценарист', ['hr', 'специалист'], ['pr', 'специалист'], ['pr', 'менеджер'],
                  ['pr', 'manager'], 'техник',
                  ['подбор', 'персонал'], 'доставк', 'закупк', 'тендер', ['салон', 'связ'], 'развити',
                  ['менеджер', 'продаж'],
                  ['специалист', 'продаж'],
                  'sales', 'продаж', 'продавец', 'hr'],

        'Инженер АСУ ТП': ['чпу', 'асу', 'cnc' 'dcs', 'acs', 'apcs'], #hard

        'Языки программирования': ['scala', 'go', 'vba', 'perl', 'rlang', 'swift', 'typescript', 'flash', 'cotlin', 'visual basic', 'pascal'], #soft
        # 'Инженер': ['engineer', 'инженер', 'інженер', 'инженер'],
        'Программист-разработчик': ['programmer', 'программист', 'разработчик', 'developer'],
        # 'Специалист': ['специалист', 'specialist'],
        # 'Менеджер': ['менеджер', 'manager']
    }

hardware = ['Программист микроконтроллеров', 'Менеджер HardWare', 'Специалист по автоматизации', 'Инженер-электроник',
                 'Инженер сетей', 'Сервисный инженер', 'Инженер АСУ ТП']
humanitarian = ['Бизнес-специалист', 'Специалист по документации', 'Pre-sale инженер', 'Менеджер по работе с клиентами',
                     'Менеджер по работе с партнерами', 'Менеджер по развитию', 'Менеджер в отделы', 'Интернет маркетолог']
rubish = ['Мусор', 'Инженер', 'Программист', 'Специалист', 'Менеджер', 'Неизвестная профессия']
classification_dict = {
    'Hardware': hardware,
    'Software': [prof for prof in plus_words.keys() if prof not in hardware + humanitarian + rubish],
    'Humanitarian': humanitarian,
    'Rubish': rubish
}

# print(classification_dict)

# print(len(plus_words))  # Пропали 2 профессии
# print(len(minus_words))

rubish_list = ['Системный программист', 'Менеджер HardWare', 'Менеджер SoftWare', 'Бизнес-специалист', 'Специалист по документации', 'Pre-sale инженер', 'Цифровой специалист', 'Менеджер по работе с клиентами', 'Менеджер по работе с партнерами', 'Менеджер по развитию', 'C#', 'C C++', 'Delphi', 'JavaScript', 'Java', 'PHP', 'Python', 'Ruby', 'Sharepoint', 'E-mail маркетолог', 'Мусор', 'Менеджер в отделы', 'Инженер', 'Программист-разработчик', 'Специалист', 'Менеджер', 'Языки программирования', ]
final_prof_list = [elem for elem in list(plus_words.keys()) if elem not in rubish_list]
# print(final_prof_list)
