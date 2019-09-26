# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 23:04:22
# @Last Modified by:   srea
# @Last Modified time: 2019-09-26 23:16:13


#****************************#
#Python 四种生成一个从0到n个数字的列表
#****************************#

###方法1：###
def CreateList1(len):
	I = []
	for i in range(1,len+1):
		I = I + [i]
	return I

###方法2：###
def CreateList2(len):
	I = []
	for i in range(1,len+1):
		I.append(i)
	return I

###方法3：###
def CreateList3(len):
	I = [i for i in range(1,len+1)]
	return I


###方法4：###
def CreateList4(len):
	I = list(range(1,len+1))
	return I


import time
start_time1 = time.perf_counter()
print(CreateList1(100))
end_time1 = time.perf_counter()
print ('代码运行时长：%f'%(end_time1-start_time1))


start_time2 = time.perf_counter()
print(CreateList2(100))
end_time2 = time.perf_counter()
print ('代码运行时长：%f'%(end_time2-start_time2))

start_time3 = time.perf_counter()
print(CreateList3(100))
end_time3 = time.perf_counter()
print ('代码运行时长：%f'%(end_time3-start_time3))


start_time4 = time.perf_counter()
print(CreateList4(100))
end_time4 = time.perf_counter()
print ('代码运行时长：%f'%(end_time4-start_time4))