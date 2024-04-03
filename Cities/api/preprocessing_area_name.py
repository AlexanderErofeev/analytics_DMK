import pandas as pd
from cities_dict import cities_dict


df = pd.read_csv('../../vacancies_and_skill_classified.csv', low_memory=False)
countries = ['Узбекистан', 'Украина', 'Казахстан', 'Азербайджан', 'Беларусь', 'Грузия', 'Другие регионы']

city_to_region = {}
for country in cities_dict:
    for region in country['areas']:
        if len(region['areas']) == 0 and country['name'] not in countries:
            city_to_region[region['name']] = region['name']
        elif len(region['areas']) == 0 and country['name'] in countries:
            city_to_region[region['name']] = country['name']
        for city in region['areas']:
            if country['name'] in countries:
                print(city['name'])
                city_to_region[city['name']] = country['name']
            else:
                city_to_region[city['name']] = region['name']
    city_to_region[country['name']] = country['name']


def preprocess_area_name(area_name):
    if area_name not in city_to_region:
        return 'Другие регионы'

    return city_to_region[area_name]


preprocessed_areas = [preprocess_area_name(area) for area in df['area_name']]

df['area_name'] = df['area_name'].apply(preprocess_area_name)

df.to_csv("vacancies_skill_and_cities_classified.csv", index=False)
