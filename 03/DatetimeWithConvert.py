# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 23:18:56
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-27 11:30:21


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
	if start_date is None:
		start_date = datetime.today()

	day_num = start_date.weekday()      ####映射开始日期和目标日期在星期数组上的位置
	print ('day_num='+str(day_num))
	
	day_num_target = weekdays.index(dayname)    ####映射开始日期和目标日期在星期数组上的位置
	print('day_num_target='+str(day_num_target))

	days_ago = (7+ day_num - day_num_target)%7    ####进行模运算
	print ('days_ago='+str(days_ago))

	if days_ago == 0:
		days_ago = 7
	target_date = start_date - timedelta(days = days_ago)    ####得到结果日期

	return target_date


print(get_previous_byday('Monday'))
print(get_previous_byday('Friday'))

print(get_previous_byday('Friday',datetime(2019,8,20)))
print(get_previous_byday('Friday',datetime(2019,7,20)))

# 大量执行可以使用第三方包 python-deteutil
from dateutil.rrule import *
d = datetime.now()
print(d)
f = datetime.today()
print(f)

print(d+relativedelta(weekday=FR))
print(d+relativedelta(weekday=TU(2)))
print(d+relativedelta(weekday=MO))
print(d+relativedelta(weekday=MO(-1)))
print(d+relativedelta(weekday=FR(-2)))



######计算当前月份的日期范围
###方法1
import calendar

def get_month_range(start_date = None):
	if start_date == None:
		start_date = datetime.today().replace(day = 1)
	print (start_date)
	_,days_in_month = calendar.monthrange(start_date.year,start_date.month)
	print(days_in_month)
	end_date = start_date+timedelta(days = days_in_month)

	return(start_date,end_date)


start_date1,end_date1 = get_month_range()
# print(start_date1,end_date1)

a_day = timedelta(days = 1)
while start_date1<end_date1:
	print(start_date1)
	start_date1 += a_day


###方法2
def date_range(start,end,step):
	while start<end:
		print(start)
		start += step

date_range(datetime(2012,9,1),datetime(2012,10,1),timedelta(days=1))



###方法3
def date_range1(start,end,step):
	while start<end:
		yield start
		start += step

for d in date_range1(datetime(2012,9,1),datetime(2012,10,1),timedelta(days=1)):
	print(d)



#####字符串转日期
text = '2019-09-26'
y = datetime.strptime(text,'%Y-%m-%d')     #性能很差
print(y)
z = datetime.today()
print(z)

diff = z - y
print(diff)

from datetime import date
x = date(2012,1,1)
print(x)
m = date.today()
print(m)


#####日期转字符串
nice_z = datetime.strftime(z,'%A %B %d, %Y')
print(nice_z)


###自己写字符串转日期,比调用strptime快很多
def parse_ymd(s):
	year,month,day = s.split('-')
	return datetime(int(year),int(month),int(day))

print(parse_ymd('2019-09-26'))




####结合时区的时间操作
from pytz import timezone
d =  datetime(2012,2,28,9,20,12)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

###初始化时间时区后，可以得到其他时区时间
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)


######例子：由北京时间转南非时间

ch = datetime.today()
ch_timezone = timezone('Asia/Shanghai')
loc_ch = ch_timezone.localize(ch)
print(loc_ch)


import pytz
za = pytz.country_timezones['ZA']
print(za)
band_ch = loc_ch.astimezone(timezone(za[0]))
print(band_ch)