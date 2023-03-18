import pandas as pd
from global_settings_and_functions import percent
pd.options.mode.chained_assignment = None


def comparison_too_professions(prof_1, prof_2):
    skills_stat = pd.read_csv('..\\Results\\skills_stat.csv', low_memory=False, index_col='Скилл')

    df_comparison = skills_stat[[prof_1, prof_2]]
    df_comparison = df_comparison[df_comparison[prof_1] + df_comparison[prof_2] > 0]

    df_comparison['Разность'] = pd.Series.abs(df_comparison[prof_1] - df_comparison[prof_2])
    df_comparison['Приращение'] = df_comparison['Разность'] / df_comparison[[prof_1, prof_2]].max(axis=1)
    df_comparison['Разность * Приращение'] = df_comparison['Разность'] * df_comparison['Приращение']
    df_comparison = df_comparison.sort_values(by=['Разность * Приращение'], ascending=False)

    sum = df_comparison['Разность * Приращение'].sum() / 2

    df_comparison = df_comparison[df_comparison[prof_1] + df_comparison[prof_2] > 0.01]
    df_comparison = df_comparison.apply(lambda x: x.apply(lambda y: percent(y, 1)))

    return sum, df_comparison


if __name__ == '__main__':
    skills_stat = pd.read_csv('..\\Results\\skills_stat.csv', low_memory=False, index_col='Скилл')
    professions_list = skills_stat.columns.tolist()
    professions_list = professions_list[:len(professions_list) - 1]

    prof_1 = 'C#'
    prof_2 = 'Frontend-программист'

    sum, df_comparison = comparison_too_professions(prof_1, prof_2)

    # ans_mas = []
    # for i in range(len(professions_list)):
    #     print(i)
    #     for j in range(i + 1, len(professions_list)):
    #         a = comparison_too_professions(professions_list[i], professions_list[j])[0]
    #         ans_mas.append((professions_list[i], professions_list[j], a))
    #
    # ans_df = pd.DataFrame(ans_mas, columns=['prof_1', 'prof_2', 'comparison'])\
    #     .sort_values(by=['comparison'])
    # ans_df['comparison'] = ans_df['comparison'].apply(lambda x: percent(x, 1))
    # ans_df.to_csv('comparison_all_prof.csv', index=False)

    print(f"Скилы в профессиях отличаются на {percent(sum, 1)}")
    df_comparison.to_csv('comparison_per_skills.csv')
