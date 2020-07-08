import datetime


def datetime_to_str(date: datetime.date):
    str_date = str(date.year) + '-'
    if date.month < 10:
        str_date += '0' + str(date.month) + '-'
    else:
        str_date += str(date.month) + '-'
    if date.day < 10:
        str_date += '0' + str(date.day)
    else:
        str_date += str(date.day)
    return str_date
