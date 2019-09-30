# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 17:29:07
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-30 17:36:46

#****************************#
#迭代一个序列的同时跟踪正在被处理的元素索引
#内置的 enumerate() 函数可以很好的解决这个问题
#为了按传统行号输出(行号从1开始)，你可以传递一个开始参数
#****************************#

a = ['a','b','c']
for i in a:
	print(i)

#内置enumerate使用
for n,i in enumerate(a):
	print(str(n)+':'+i)

#设置开始的参数
for n,i in enumerate(a,1):
	print(str(n)+':'+i)


date = [(1,2),(3,4),(5,6)]
for n,(x,y) in enumerate(date,1):
	print(n,x,y,sep = ':')