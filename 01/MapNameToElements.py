# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 15:13:30
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:10:40

#****************************#
# 你有一段通过下标访问列表或者元组中元素的代码，
# 但是这样有时候会使得你的代码难以阅读， 
# 于是你想通过名称来访问元素。
#****************************#

from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('China','2019-1-1')
print(sub)

addr,joined = sub
print(addr)

#########
records = [
	('苹果',1,20),
	('橘子',2,10),
	('香蕉',3,30),
	('鱼肉',4,29),	
]

Stock = namedtuple('Stock',['name','num','price'])
def compute_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		# s.price = 100             #不像字典那样，一个命名元组是不可更改的
		# s = s._replace(price=100)    #使用该方法可以更改
		onePrice = s.num * s.price
		total += onePrice
		print(s.name + ':\t' +str(onePrice))
	return total

total=compute_cost(records)
print('总价为：' + str(total))


#########  _replace 方法:设置初始值替代  ##########

Stock = namedtuple('Stock',['name','shares','price','date','time'])
stock_prototype = Stock('',0,0.0,None,None)
def dict_to_stack(s):
	return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
k =dict_to_stack(a)
print(k)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print (dict_to_stack(b))