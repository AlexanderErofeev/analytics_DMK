from matplotlib import pyplot as plt
from cycler import cycler
import pandas as pd
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

GRAPH_DPI = 200
COUNT_LINES = 20
YEAR_RANGE = (2015, 2023)


def draw_graph(prof_name, group, target_col, path):
    stat_per_year_dict = group.groupby([target_col]) \
        .apply(lambda x: pd.Series(data=x['count'].tolist(), index=x['year']).to_dict()) \
        .to_dict()

    stat_per_year_dict = dict(sorted(stat_per_year_dict.items(), key=lambda el: sum(list(el[1].values())), reverse=True)[:COUNT_LINES])
    stat_per_year_dict = {key: {key_1: value_1 for key_1, value_1 in value.items() if YEAR_RANGE[0] < key_1 < YEAR_RANGE[1]} for key, value in stat_per_year_dict.items()}

    colors = ['black', 'silver', 'firebrick', 'sandybrown', 'gold',
              'olivedrab', 'chartreuse', 'green', 'cyan', 'darkblue', 'coral',
              'orange', 'yellow', 'red', 'greenyellow', 'steelblue']

    styles = ['-', '--', ':', '-.']

    prop_cycle = cycler(linestyle=styles) * cycler(color=colors)
    plt.rc('axes', prop_cycle=prop_cycle)
    plt.figure(figsize=(15, 10))
    plt.title(prof_name)
    plt.ylabel('Процент в профессии')
    plt.xlabel('Год')

    for k, v in stat_per_year_dict.items():
        plt.plot(list(v.keys()), [value * 100 for value in list(v.values())], label=k)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(f'{path}\\{prof_name.replace("/", "-")}.png', bbox_inches='tight', dpi=GRAPH_DPI)
    plt.close()


if __name__ == '__main__':
    grup_skills_stat_per_year = pd.read_csv('../Results/grup_skills_stat_per_year.csv')
    # print(grup_skills_stat_per_year['count'].sum())
    grup_skills_stat_per_year = grup_skills_stat_per_year.groupby(['prof_name'])
    for prof_name in grup_skills_stat_per_year.groups.keys():
        draw_graph(str(prof_name), grup_skills_stat_per_year.get_group(prof_name), 'grup_skills', 'grup_skills')

    skills_stat_per_year = pd.read_csv('../Results/skills_stat_per_year.csv')
    # print(skills_stat_per_year['count'].sum())
    skills_stat_per_year = skills_stat_per_year.groupby(['prof_name'])
    for prof_name in skills_stat_per_year.groups.keys():
        draw_graph(str(prof_name), skills_stat_per_year.get_group(prof_name), 'key_skills', 'skills')
