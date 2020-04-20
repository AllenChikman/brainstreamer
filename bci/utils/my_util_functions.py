import datetime as dt
import uuid


def milisecs_to_date(milisecs, date_format="%d/%m/%Y, %H:%M:%S:%f"):
    datetime = dt.datetime.fromtimestamp(milisecs / 1000).strftime(date_format)


def get_unique_id():
    return str(uuid.uuid4())
