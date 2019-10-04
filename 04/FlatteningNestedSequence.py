# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-04 11:46:18
# @Last Modified by:   srea
# @Last Modified time: 2019-10-04 17:22:07

#****************************#
#想将一个多层嵌套的序列展开成一个单层列表
#可以写一个包含 yield from 语句的递归生成器来轻松解决这个问题
#isinstance(x, Iterable) 检查某个元素是否是可迭代的。 如果是的话， yield from 就会返回所有子例程的值

# 额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，
# 防止将它们再展开成单个的字符。 这样的话字符串数组就能最终返回我们所期望的结果了
#****************************#

from collections import Iterable

def flatten(items, ignore_types=(str,bytes)):
	for x in items:
		if isinstance(x,Iterable) and not isinstance(x,ignore_types):
			# yield from flatten(x)     #等价于yield表示如下,尽管只改了一点点，但是 yield from 语句看上去感觉更好，并且也使得代码更简洁清爽
			for i in flatten(x):
				yield i
		else:
			yield x

items = [1,2,[1,3,2],[1213,3123,3123],[132,11],[1]]
# for x in flatten(items):
# 	print(x)

items_1 = ['Dave', 'Paula', ['Thomas', 'Lewis']]
# for x in flatten(items_1):
# 	print(x)

from itertools import chain

# for x in chain(flatten(items),flatten(items_1)):
# 	print (x)

for x in flatten(chain(items,items_1)):
	print (x)