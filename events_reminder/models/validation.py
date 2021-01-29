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
