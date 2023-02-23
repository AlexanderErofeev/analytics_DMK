import multiprocessing
import os
import pandas as pd

path = "HH\\"
# keep_col = ['name', 'description', 'key_skills', 'experience_id', 'premium', 'employer_name', 'salary_from', 'salary_to', 'salary_gross', 'salary_currency', 'area_name', 'published_at']
keep_col = ['id', 'name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'published_at']


def opened(file):
    print(os.path.basename(file))
    return pd.read_csv(file, usecols=keep_col)


if __name__ == '__main__':
    file_list = [path + f for f in os.listdir(path) if f.endswith('.csv')]

    with multiprocessing.Pool() as p:
        csv_list = p.map(opened, file_list)

    print('Чтение завершено')

    csv_merged = pd.concat(csv_list, ignore_index=True, copy=False).reindex(columns=keep_col)
    print(f"Суммарное количество вакансий: {len(csv_merged.index)}")

    csv_merged = csv_merged.drop_duplicates(subset=['id']).dropna(how='all')
    print(f"Количество вакансий после удаления дубликатов: {len(csv_merged.index)}")

    csv_merged.drop('id', axis='columns').to_csv("vacancies.csv", index=False)
