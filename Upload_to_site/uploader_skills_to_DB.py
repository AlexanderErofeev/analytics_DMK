import pandas as pd
from sqlalchemy import create_engine

# ENGINE = create_engine('mysql://user_for_django:%s@localhost:3306/test1' % quote('5678_@TL'))
ENGINE = create_engine('mysql://c21535_dmk_ai_info_ru:MoYzuQoxtecoh10@localhost:3306/c21535_dmk_ai_info_ru?charset=utf8mb4')  # ?charset=utf8mb4 для хостинга


DMK_softskill = pd.read_csv('DMK_softskill.csv', index_col='id')
DMK_softskill.to_sql('DMK_softskill', if_exists="replace", con=ENGINE, index_label='id')

DMK_skill = pd.read_csv('DMK_skill.csv', index_col='id')
DMK_skill.to_sql('DMK_skill', if_exists="replace", con=ENGINE, index_label='id')

DMK_skillgroup = pd.read_csv('DMK_skillgroup.csv', index_col='id')
DMK_skillgroup.to_sql('DMK_skillgroup', if_exists="replace", con=ENGINE, index_label='id')

DMK_skillgroup_child = pd.read_csv('DMK_skillgroup_child.csv', index_col='id')
DMK_skillgroup_child.to_sql('DMK_skillgroup_child', if_exists="replace", con=ENGINE, index_label='id')
