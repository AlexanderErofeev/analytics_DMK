import pandas as pd
from dict_cities import cities_dict

INPUT_FILE = 'vacancies_and_skill_classified.csv'
OUT_FILE = 'vacancies_skill_and_cities_classified.csv'

UNKNOWN_TITLE = 'Другие регионы'
COUNTRIES = ['Узбекистан', 'Украина', 'Казахстан', 'Азербайджан', 'Беларусь', 'Грузия', UNKNOWN_TITLE]


def add_in_dict(city_dict, key, value):
    if key in city_dict:
        city_dict[key].append(value)
    else:
        city_dict[key] = [value]


def get_city_to_region_dict():
    city_to_region = {}
    for country in cities_dict:
        if country['name'] == UNKNOWN_TITLE:
            continue
        elif country['name'] == 'Россия':
            for region in country['areas']:
                city_to_region[region['name']] = region['name']
                for city in region['areas']:
                    city_to_region[city['name']] = region['name']
        else:
            for region in country['areas']:
                city_to_region[region['name']] = country['name']
                for city in region['areas']:
                    city_to_region[city['name']] = country['name']
    return city_to_region


def clustering_area_name(area_name_column):
    city_to_region_dict = get_city_to_region_dict()
    return area_name_column.apply(lambda area_name: city_to_region_dict.get(area_name, UNKNOWN_TITLE))


if __name__ == '__main__':
    df = pd.read_csv(INPUT_FILE, low_memory=False)
    df['area_name_cl'] = clustering_area_name(df['area_name'])
    df['area_name_cl'].value_counts().to_csv('area_name_counts.csv')
    df[df['area_name_cl'] == UNKNOWN_TITLE]['area_name'].value_counts().to_csv('unknown_area_name_counts.csv')
    df.to_csv(OUT_FILE, index=False)
