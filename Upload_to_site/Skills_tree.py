import pandas as pd
from dict_skill import dict_skill
from global_settings_and_functions import *

soft_skills = list(dict_skill.pop('Soft').keys())
grup_skills = list(dict_skill.keys())
skills = sum_mas([list(s.keys()) for s in dict_skill.values()])

grup_skills_child = []
for k, v in dict_skill.items():
    for s in v.keys():
        grup_skills_child.append((grup_skills.index(k) + 1, skills.index(s) + 1))


pd.DataFrame(soft_skills, index=range(1, len(soft_skills) + 1), columns=['title']).to_csv('DMK_softskill.csv', index_label='id')
pd.DataFrame(grup_skills, index=range(1, len(grup_skills) + 1), columns=['title']).to_csv('DMK_skillgroup.csv', index_label='id')
skills = [[s, None] for s in skills]
pd.DataFrame(skills, index=range(1, len(skills) + 1), columns=['title', 'description']).to_csv('DMK_skill.csv', index_label='id')
pd.DataFrame(grup_skills_child, index=range(1, len(grup_skills_child) + 1), columns=['skillgroup_id', 'skill_id']).to_csv('DMK_skillgroup_child.csv', index_label='id')
