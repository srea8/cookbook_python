# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 16:55:05
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:08:30


#****************************#
# 实现一个键对应多个值的字典
#****************************#


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(2)
d['a'].append(2)
d['a'].remove(1)
print (d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(12)
e['a'].add(21)
e['a'].remove(1)
print (e)


####多值字典###

k = {}
k.setdefault('a',[]).append(1)
k.setdefault('a',[]).append(2)
print (k)

pairs = {"da":'1'}

for key,value in pairs.items():
	if key not in k:
		k[key] = []
	k[key].append(value)

print (k)

