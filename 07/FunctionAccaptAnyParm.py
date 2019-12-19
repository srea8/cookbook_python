# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-11-23 11:45:50
# @Last Modified by:   srea
# @Last Modified time: 2019-12-01 23:09:19

#****************************#
#为了能让一个函数接受任意数量的位置参数，可以使用一个*参数
# 一个*参数只能出现在函数定义中最后一个位置参数后面，
# 而 **参数只能出现在最后一个参数。 有一点要注意的是，在*参数后面仍然可以定义其他参数
#****************************#

#tips
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass


#example
def avg(first,*rest):
	return (first+sum(rest))/(1+len(rest))

def make_element(name,value,**attrs):
	keyvals = ['%s="%s"'%item for item in attrs.items()]
	print (keyvals)
	attrs_str = ''.join(keyvals)
	print (attrs_str)
	element = '<{name}{attrs}>{value}</{name}>'.format(
			name = name,
			attrs = attrs,
			value = value,
		)
	print (element)

def anyargs(*args,**attrs):
	print (args)
	print (attrs)

kk = avg(1,2,3,4,5)
print(kk)

dd = make_element('liming','12',yuwen=79,shuxue=97)
print(dd)

ff = anyargs(1,2,3,13,a=1,b=2,c=3)
print(ff)

