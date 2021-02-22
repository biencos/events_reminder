import os
import re
from datetime import datetime

def file_exists(filename):
    return os.path.isfile(filename)

def is_name_valid(name):
    if re.match('[a-zA-Z\s]+$', name):
        return True
    return False


def is_date_valid(d, m, y):
    try:
        d = int(d)
        m = int(m)
        y = int(y)
    except:
        return False
    try:
        d = datetime(year=y, month=m, day=d)
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
