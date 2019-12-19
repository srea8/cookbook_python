# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-01 23:10:23
# @Last Modified by:   srea
# @Last Modified time: 2019-12-01 23:26:11

#****************************#
#函数的某些参数强制使用关键字参数传递
#将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果
#return可以返回多个值，构成一个元组
#默认参数：是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值
#特别需要注意：默认参数只在函数定义的时候运行一次，所以在默认参数值时，不要使用变量
#****************************#

def recv(maxsize,*args,block):
	#receives a message
	print (maxsize)
	print (args)

def minimum(*values,clip=None):
	m = min(values)
	if clip is not None:
		m = clip if clip>m else m
	return m,clip



# recv(1024,True,1)
# recv(block=True)
recv(1024,block=True)
print(help(recv))

print(minimum(1,212,3,213,1,23,123,-11,clip=10))
print(minimum(123,123,1,23,-12,3,-10))
