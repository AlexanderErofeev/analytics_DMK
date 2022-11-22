import pandas as pd

csv_merged = pd.read_csv('vacancies_preprocessed.csv')
print(len(csv_merged.index))

csv_merged = csv_merged.drop_duplicates(subset=['name'], keep='first')  # Удаляем дубликаты, оставляя первое вхождение
print(len(csv_merged.index))

csv_merged.to_csv("vacancies_preprocessed_original.csv", index=False)
