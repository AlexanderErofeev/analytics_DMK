import datetime
import multiprocessing
import sys

PROCESSOR_COUNT = 16
IS_USES_MULTIPROCESSING = False


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


def print_log(log_string, is_error=False):
    text = f"[{datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {log_string}"
    print(text, file=sys.stderr if is_error else sys.stdout)


def multiprocessing_map(function, list_items):
    if IS_USES_MULTIPROCESSING:
        with multiprocessing.Pool(PROCESSOR_COUNT) as p:
            csv_list = p.map(function, list_items)
    else:
        csv_list = map(function, list_items)

    return csv_list
