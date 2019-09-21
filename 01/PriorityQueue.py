# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 16:24:43
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:08:55


#****************************#
#使用heapq实现优先队列
#****************************#


import heapq


##优先队列实现
class PriorityQueue():
	"""docstring for PriorityQueue"""
	def __init__(self):
		self._queue = []
		self._index = 0

	def push(self,item,priority):
		heapq.heappush(self._queue,(-priority,self._index,item))
		self._index +=1

	def pop(self):
		return heapq.heappop(self._queue)[-1]


###优先队列使用
# 第一个 pop() 操作返回优先级最高的元素。 
# 另外注意到如果两个有着相同优先级的元素（ foo 和 grok ），
# pop 操作按照它们被插入到队列的顺序返回的
q = PriorityQueue()
q.push(12,1)
q.push(212,4123)
q.push(122,4123)
q.push(8,21)
print (q.pop())
print (q.pop())


#####实现class优先队列
class Item(object):
	"""docstring for Item"""
	def __init__(self, arg):
		self.arg = arg

	def __repr__(self):
		return ('Item({!r})'.format(self.arg))

q.push(Item('foo'),3123)
print (q.pop())
		


######元组比较
#   one     error
# a = Item('foo')
# b = Item('bar')

#   two    
a = (1,Item('foo'))
b = (2,Item('bar'))
# c = (2,Item('cas'))       #error

#   three
a = (1,0,Item('foo'))
b = (2,2,Item('bar'))
c = (2,1,Item('cas'))  

print (a<b)
print (c>b)