# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 14:28:48
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:08:45


#****************************#
###从一个集合中获得最大或者最小的 N 个元素列表####
#****************************##

import heapq

nums = [1,8,2,31,3123,12,3,14,12,3,1,41,23,-3,-3123]
print (heapq.nlargest(3,nums))
print (heapq.nsmallest(3,nums))



#####
students = [
	{'name':'liming','age':12,'tail':168},
	{'name':'xiaohua','age':15,'tail':32},
	{'name':'zhijie','age':13,'tail':121},
	{'name':'tianqi','age':2,'tail':312},
	{'name':'jinmao','age':21,'tail':41},
]

ageLarge = heapq.nlargest(2,students,key=lambda s:s['age'])
ageSmall = heapq.nsmallest(2,students,key=lambda s:s['age'])
print (ageLarge)
print (ageSmall)


####headpop()
# heap = list(nums)
heapq.heapify(nums)
# print (heap)
# print(heap[0])
print (nums)
print (max(nums))
print (min(nums))


for x in range(0,len(nums)):
	print (heapq.heappop(nums))



