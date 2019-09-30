# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 17:55:59
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-30 18:00:42

#****************************#
#想在多个对象执行相同的操作，但是这些对象在不同的容器中，你希望代码在不失可读性的情况下避免写重复的循环
#itertools.chain() 方法可以用来简化这个任务。 它接受一个可迭代对象列表作为输入，并返回一个迭代器，有效的屏蔽掉在多个容器中迭代细节
#itertools.chain() 接受一个或多个可迭代对象作为输入参数。 然后创建一个迭代器，依次连续的返回每个可迭代对象中的元素。 这种方式要比先将序列合并再迭代要高效的多
#****************************#

from itertools import chain

a = [1,2,3,4]
b = ['a','b','c']

for i in chain(a,b):
	print(i)

# 等价于分开执行，但是合并执行的效率更高
for i in a:
	print (i)

for i in b:
	print(i)


####列表和set都可以执行相同的操作