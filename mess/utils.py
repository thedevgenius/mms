from datetime import datetime


def GetPrevMonth():
    prev_month = datetime.now().month - 1
    if datetime.now().month == 1:
        prev_month = 12
    else:
        prev_month = datetime.now().month - 1
    return prev_month

def GetPrevYear():
    prev_year = datetime.now().year
    if datetime.now().month == 1:
        prev_year = datetime.now().year - 1
    else:
        prev_year = datetime.now().year
    return prev_year
