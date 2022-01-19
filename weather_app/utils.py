import datetime

def ms_to_date(ms, tz):
    mms = ms*1000 - tz*1000
    return datetime.datetime.fromtimestamp(mms/1000.0)