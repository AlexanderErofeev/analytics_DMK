import pandas as pd

csv_merged = pd.read_csv('professions_names.csv')
print(len(csv_merged.index))

csv_merged['name'] = csv_merged['name'].apply(lambda x: x.lower())  # Переводим в нижний регистр

csv_merged = csv_merged.drop_duplicates(keep='first')  # Удаляем дубликаты, оставляя первое вхождение
print(len(csv_merged.index))

csv_merged.to_csv("original_professions_names.csv", index=False)
