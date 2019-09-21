# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:12:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:07:38


#****************************#
## 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
#****************************#

mylist = [1,23,41,4124,-5,15,1,-431,2,-3,123]
print([n for n in mylist if n>0 and n < 100])
pos = (n for n in mylist if n>0 and n < 100)
for tmp in pos:
    print(tmp)

######filter过滤器
values = ['1','2','3','-','312','ND']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

#######itertools.compress过滤器

from itertools import compress

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

k = list(n>5 for n in counts)   #创建一个boolean序列
print(k)
print(list(compress(addresses,k)))    #compress返回一个迭代器类型
