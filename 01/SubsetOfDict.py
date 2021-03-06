# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:17:57
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:10:00


#****************************#
##你想构造一个字典，它是另外一个字典的子集。
#****************************#


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

p1 = {key:value for key,value in prices.items() if value > 100}
print(p1)

findKey = ('AAPL','IBM')
p2 = {key:value for key,value in prices.items() if key not in findKey}
print(p2)

p3 = dict((key,value) for key,value in prices.items() if value > 100)
print(p3)

p4 = {key:prices[key] for key in prices.keys() & findKey}
print(p4)

p5 = {key:prices[key] for key in prices.keys() | findKey}
print(p5)

p6 = {key:prices[key] for key in prices.keys() ^ findKey}
print(p6)