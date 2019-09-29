# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-29 10:35:32
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-29 10:46:13

#****************************#
#想反方向迭代一个序列
#使用内置的 reversed() 函数
#
#****************************#

a = [1,2,3,4]
for x in reversed(a):
	print(x)

for x in iter(a):
	print(x)

k = iter(a)
print(k)
print(next(k))