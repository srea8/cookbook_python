# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 17:21:25
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:09:33


#****************************#
####OrderedDict 内部维护着一个根据键插入顺序排序的双向链表
#****************************#

from collections import OrderedDict
import json


# d = OrderedDict()
d = {}
d['fff'] = 4
d['aaa'] = 2
d['sss'] = 3
d['aaa'] = 12

for key in d:
	print (key,d[key])

k = json.dumps(d)
print (k)


# zip  实现将key和value 调换位置
#需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
min_d = min(zip(d.values(),d.keys()))
print (min_d)
sort_d = sorted(zip(d.values(),d.keys()))
print (sort_d)


#    error   AttributeError: 'str' object has no attribute 'values'
# min_k = min(zip(k.values(),k.keys()))
# print (min_k)


min_key_d = min(d)
max_key_d = max(d)
print (min_key_d)
print (max_key_d)
print (d[min(d,key = lambda k :d[k])])