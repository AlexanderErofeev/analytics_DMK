import os
import pandas as pd

path = "HH\\"

file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]
csv_list = []

# keep_col = ['name', 'description', 'key_skills', 'experience_id', 'premium', 'employer_name', 'salary_from', 'salary_to', 'salary_gross', 'salary_currency', 'area_name', 'published_at']
keep_col = ['name']

for file in sorted(file_list):
    print(os.path.basename(file))
    csv_list.append(pd.read_csv(file, usecols=keep_col))

csv_merged = pd.concat(csv_list, ignore_index=True)

# csv_merged = csv_merged.dropna()  # Удаляем неполностью заполненные строки, в любой колонке
# print(len(csv_merged.index))

csv_merged['name'] = csv_merged['name'].apply(lambda x: x.lower())
print(len(csv_merged.index))

csv_merged.to_csv("professions_names.csv", index=False)