# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 17:38:24
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-30 17:45:56

#****************************#
#想同时迭代多个序列，每次分别从一个序列中取一个元素
#使用 zip() 函数,zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中x来自a，y来自b,选取短列
#还可以使用 itertools.zip_longest() 函数来代替,选取长列
#****************************#

a = [1,2,3,4,5]
b = ['a','b','c','d']
c = ['一','二','三']

#选取最短序列
for x,y in zip(a,b):
	print(x,y,sep=':')

#选取最长序列
from itertools import zip_longest
for x,y in zip_longest(a,b):
	print(x,y,sep=':')

#zip可以同时打包多个字符串
for i in zip(a,b,c):
	print(i)

# 使用zip可以打包字典
dict_ab = dict(zip(a,b))
print(dict_ab)

dict_ab1 = dict(zip_longest(a,b))
print(dict_ab1)

# zip会自动创建迭代器，需要打印的话要转换为list
print(zip(a,b))
print(list(zip(a,b)))