# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-27 13:19:29
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-29 10:28:45

#****************************#
#遍历一个可迭代对象中的所有元素，但是却不想使用for循环
#使用 next() 函数并在代码中捕获 StopIteration 异常
#通常来讲， StopIteration 用来指示迭代的结尾。 然而，如果你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None
#****************************#


import os

path = os.listdir('.')
# path = os.path.dirname('.')
print(path)

path1 = os.getcwd()
print(path1)

filePath = path1+'\ConSumingIterator.py'
print(filePath)

def manual_iter(filePath):
	with open(filePath,encoding = 'utf-8') as f:
		try:
			while True:
				line = next(f)
				print(line)
		except StopIteration:         # StopIteration 用来指示迭代的结尾
			print('OVER!')

def manual_iter1(filePath):
	with open(filePath,encoding='utf-8') as f:
		while True:
			line = next(f,None)   #你手动使用上面演示的 next() 函数的话，你还可以通过返回一个指定值来标记结尾，比如 None
			if line == None:
				print('OVER!')
				break
			print(line)


manual_iter(filePath)
manual_iter1(filePath)

items = [1,2,3]
it = iter(items)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))   ###越界报错

its = iter(items)
for it in its:
	print(it)


####一个函数中需要有一个 yield 语句即可将其转换为一个生成器。 跟普通函数不同的是，生成器只能用于迭代操作
def CutDown(n):
	print('START')
	while n>0:
		yield n
		n -= 1
	print('DONE')

c = CutDown(2)
print(next(c))
print(next(c))
# print(next(c))   ###报错StopIteration