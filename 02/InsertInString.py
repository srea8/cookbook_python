# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 10:47:59
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 14:04:57

#****************************#
# 创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉
# 通过使用字符串的 format() 方法来解决这个问题
# 要被替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
# 但是format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
#****************************#

s = "{name} has {n} message"
print(s.format(name = 'Liming',n = '12'))


# 要被替换的变量能在变量域中找到， 那么你可以结合使用 format_map() 和 vars()
# 需要提前定义变量
name = "LiHua"
n = 10
name = "Xiaoming"
print(s.format_map(vars()))


class Info:
	"""docstring for Info"""
	def __init__(self, name,n):
		self.name = name
		self.n = n


a = Info('Xiaoli','19')
print(s.format_map(vars(a)))

# print(s.format(name = 'll'))    #变量缺失报错


# 一种避免这种错误的方法是另外定义一个含有 __missing__() 方法的字典对象
class safesub(dict):
	def __missing__(self,key):
		return '{'+key+'}'

del n
del name
print(s.format_map(safesub(vars())))



# sub() 函数使用 sys._getframe(1) 返回调用者的栈帧,可以从中访问属性 f_locals 来获得局部变量,不推荐
import sys

def sub(text):
	return text.format_map(safesub(sys._getframe(1).f_locals))
name = "liming"
n = 33
print(sub('Hello,{name}'))
print(sub('Hello,{n}'))
print(sub('Hello,{age}'))