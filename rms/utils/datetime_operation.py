from datetime import datetime


def get_current_datetime():
    return datetime.now()


def get_current_datetime_in_str(date_time):
    if not date_time:
        return ""
    return datetime.strftime(date_time, "%Y-%m-%dT%H:%M:%S %p")
