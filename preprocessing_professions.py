import numpy as np
import pandas as pd
import re

csv_merged = pd.read_csv('professions_names.csv')
print(len(csv_merged.index))

csv_merged['name'] = csv_merged['name'].str.lower()  # Переводим в нижний регистр

# csv_merged['name'] = csv_merged['name'].apply(lambda x: ' '.join(re.sub(r"[-_!/:();'\".,\\\[\]023456789«»–|—?&*]", ' ', x).split()))  # Предобработка
csv_merged['name'] = csv_merged['name'].apply(lambda x: ' '.join(re.sub(r"[^\w+#]|[_023456789]", ' ', x).split()))  # Предобработка

csv_merged = csv_merged[csv_merged['name'].str.len() != 0]
print(len(csv_merged.index))

# a = list(filter(lambda x: not x.isalpha(), list(''.join(csv_merged['name'].tolist()))))
# words = pd.Series(np.array(a))
# words = words \
#     .groupby(words) \
#     .apply(lambda x: len(x.index)) \
#     .sort_values(ascending=False)
#
# words1 = pd.Series(words.index).apply(lambda x: str(x).encode('utf-8'))
#
# words1.index = words.index
# pd.concat([pd.DataFrame(words), pd.DataFrame(words1)], axis=1).to_csv("simblo.csv", header=False)

csv_merged.to_csv("preproces_professions_names.csv", index=False)
