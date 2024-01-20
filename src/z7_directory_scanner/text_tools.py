from model import *


def get_size_verbose(size: int) -> str:
    n_digits = len(str(size))
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    group = min(n_digits // 3, 4)

    unit = units[group]
    unit_size = (10 ** 3) ** group

    return str(round(size / unit_size, 1)) + ' ' + unit


def get_age_in_days(date: datetime) -> int:
    # find out how many days passed between datetime.now() and date

    return (datetime.now() - date).days


def file_verbose(f: any) -> str:
    return f'{f.path:<70}\t{get_size_verbose(f.size):>8}\t{get_age_in_days(f.last_modify_time)}d'
