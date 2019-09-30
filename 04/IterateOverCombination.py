# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 17:15:35
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-30 17:27:02

#****************************#
#迭代遍历一个集合中元素的所有可能的排列或组合
# 1.函数 itertools.permutations() 它接受一个集合并产生一个元组序列，每个元组由集合中所有元素的一个可能排列组成。
# 2.函数 itertools.combinations() 可得到输入集合中元素的所有的组合,不考虑元素的顺序，被选择过的元素不再选择
# 3.函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次，同样也不考虑顺序
#****************************#

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
items = ['a','b','c']

print('函数 itertools.permutations()')
for item in permutations(items):
	print(item)


print('函数 itertools.combinations()')
for item in combinations(items,3):
	print(item)


print('函数 itertools.combinations_with_replacement()')
for item in combinations_with_replacement(items,2):
	print(item)

