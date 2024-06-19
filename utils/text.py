from datetime import datetime

def print_line(length):
    print('-'*length)

def get_current_formated_date_time():
    now = datetime.now()

    day = now.day
    month = now.month
    year = now.year
    hour = now.hour
    minute = now.minute
    second = now.second

    current_date_time = f"{day}/{month}/{year} | {hour:02d}:{minute:02d}:{second:02d}"

    return current_date_time

def isFloatable(val:str):
    try:
        val = float(val)
    except:
        return False
    return True