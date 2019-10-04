# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-04 17:34:22
# @Last Modified by:   srea
# @Last Modified time: 2019-10-04 17:52:19

#****************************#
# 有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历
# heapq.merge() 函数可以帮你解决这个问题
# heapq.merge() 需要所有输入序列必须是排过序的, 它仅仅是检查所有序列的开始部分并返回最小的那个，
# 这个过程一直会持续直到所有输入序列中的元素都被遍历完
#****************************#
 
import heapq

a = [1,3,5]
b = [2,4,6]
c = [4,2,6]

for i in heapq.merge(a,b):
	print(i,end = ' ')

for i in heapq.merge(a,c):
	print(i,end = ' ')