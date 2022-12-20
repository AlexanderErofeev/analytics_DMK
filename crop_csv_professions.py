import os
import pandas as pd

path = "HH\\"

file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]
csv_list = []

# keep_col = ['name', 'description', 'key_skills', 'experience_id', 'premium', 'employer_name', 'salary_from', 'salary_to', 'salary_gross', 'salary_currency', 'area_name', 'published_at']
keep_col = ['name', 'salary_from', 'salary_to', 'salary_currency', 'published_at']

for file in sorted(file_list):
    print(os.path.basename(file))
    csv_list.append(pd.read_csv(file, usecols=keep_col))

csv_merged = pd.concat(csv_list, ignore_index=True).reindex(columns=keep_col)
print(f"Суммарное количество вакансий: {len(csv_merged.index)}")

csv_merged.to_csv("vacancies.csv", index=False)
