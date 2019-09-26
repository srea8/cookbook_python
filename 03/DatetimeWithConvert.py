# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 23:18:56
# @Last Modified by:   srea
# @Last Modified time: 2019-09-27 00:11:05


#****************************#
#需要执行简单的时间转换，比如天到秒，小时到分钟等的转换
#请使用 datetime 模块
#为了表示一个时间段，可以创建一个 timedelta 实例
#****************************#
# import datetime
from datetime import timedelta
from datetime import datetime

####表示时间段
a = timedelta(days = 2,minutes = 10,hours = 6)
print(a)
print(a + timedelta(days = 10))
print(a.seconds)
print(a.days)
# print(a.minutes)   print(a.hours)    #AttributeError: 'datetime.timedelta' object has no attribute 'minutes'
print(a.seconds/3600)
print(a.total_seconds()/3600)


####指定日期和时间
c = datetime(2019,9,23)
print(c)
print(c+timedelta(days=10))
d = c + timedelta(days = 100)
print(d)
print(d - c)
print((d - c).days)


now = datetime.today()
print(now)
print(now + timedelta(minutes=10))


##datetime 自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print(a-b)
print(c-d)
print((a-b).days)


# 许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替
from dateutil.relativedelta import relativedelta
# a = datetime(2012,2,28)
# print(a+timedelta(months=1))     #报错
print(a+relativedelta(months=1))
print(a+relativedelta(months=11))

print(relativedelta(c,d))
print(relativedelta(c,d).months)
print(relativedelta(c,d).days)


# 需要查找星期中某一天最后出现的日期
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname,start_date=None):
	pass

