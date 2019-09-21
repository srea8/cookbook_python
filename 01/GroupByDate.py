# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:12:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:07:52


#****************************#
##你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问
#****************************#

from operator import itemgetter
from itertools import groupby
from collections import defaultdict


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

print(rows)
# rows.sort(key=itemgetter('date'))            #groupby仅检查连续元素，需提前排序
# print(rows)

for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print('\t',i)


######使用多值字典的方式对数据进行整理
dateDict = defaultdict(list)
for row in rows:
    dateDict[row['date']].append(row)
print(dateDict)
print(dateDict['07/01/2012'])