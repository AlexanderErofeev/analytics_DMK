import pandas as pd
import re

csv_merged = pd.read_csv('preproces_professions_names.csv')
print(len(csv_merged.index))

csv_merged = csv_merged.drop_duplicates(keep='first')  # Удаляем дубликаты, оставляя первое вхождение
print(len(csv_merged.index))

csv_merged.to_csv("original_preproces_professions_names.csv", index=False)
