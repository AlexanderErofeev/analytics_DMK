import datetime
import sys

PROCESSOR_COUNT = 10
IS_USES_MULTIPROCESSING = True

# INPUT_DIRS = ['/home/hh-data-miner/data']
INPUT_DIRS = ['../HH']
IS_ONLY_NEW_VACANCIES = True
PROCESSING_CHUNK_SIZE = 50000

UPLOAD_URL = '...'
UPLOAD_CHUNK_SIZE = 10000


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
