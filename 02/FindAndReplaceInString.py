# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 18:19:42
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-23 18:37:58

#****************************#
#想在字符串中搜索和匹配指定的文本模式
#****************************#


#使用replace直接进行替换
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah','yep'))
print(text)

#调用re模块中的sub（）函数
import re
text = 'Today is 11/27/2012.Python starts 11/12/2012'
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))
print(text)
print(re.sub(r'Today',r'TT',text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')   #可以提前编译
print(datepat.sub(r'\3-\2-\1',text))

####对于替换规则复杂的情况可以传递替换回调函数
from calendar import month_abbr
def change_date(m):
	mon_name = month_abbr[int(m.group(1))]
	return'{} {} {}'.format(m.group(2),mon_name,m.group(3))
print(datepat.sub(change_date,text))
newtext,n = datepat.subn(change_date,text)
print(newtext+'  n='+str(n))