PROCESSOR_COUNT = 16


def percent(value_count, all_value_count):
    return str(round((value_count / all_value_count) * 100, 2)) + '%'


def sum_mas(list_lists):
    mas = []
    for el in list_lists:
        mas += el
    return mas


def sum_dict(list_dict):
    dict_ans = {}
    for el_dict in list_dict:
        dict_ans.update(el_dict)
    return dict_ans