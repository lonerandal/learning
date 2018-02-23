#把datetime转成字符串
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d-%H")

#把字符串转成datetime
def string_toDatetime(string):
    return datetime.strptime(string, "%Y-%m-%d-%H")

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp):
    return time.strftime("%Y-%m-%d-%H", time.localtime(stamp))

#把datetime类型转外时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())
#j将时间戳（int）转成datatime.date格式
def timestamp_datetime(stamp):
    datetime.datetime.fromtimestamp(stamp).date()

datetime.datetime.strptime('2018-02-10', "%Y-%m-%d").date()

import datetime
from dateutil.relativedelta import relativedelta
print(datetime.date.today() + relativedelta(months=1))#计算1个月后的日期

