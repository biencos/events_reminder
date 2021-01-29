import re
from datetime import datetime


def is_name_valid(name):
    if re.match('[a-zA-Z\s]+$', name):
        return True
    return False


def is_date_valid(day, month, year):
    try:
        d = datetime(year=year, month=month, day=day)
        return True
    except:
        return False


def is_option_valid(inp, inp_limit, inp_limit1):
    try:
        inp = int(inp)
    except:
        return False
    if inp < inp_limit or inp > inp_limit1:
        return False
    return True
