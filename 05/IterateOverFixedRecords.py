# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 17:37:08
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 17:50:51

#****************************#
#想在一个固定长度记录或者数据块的集合上迭代，而不是在一个文件中一行一行的迭代
#通过下面这个小技巧使用 iter 和 functools.partial() 函数
#****************************#

from functools import partial

RECORD_SIZE = 32
with open('somedate.date', 'rb') as f:               #规定长度读取
	records = iter(partial(f.read,RECORD_SIZE),b'')
	for r in records:
		print(r)


with open('somedate.date', 'rb') as f:               #正常每行读取
	for r in f:
		print(r)


with open('somedate.date', 'rb') as f:               #每个字符读取
	data = f.read()
	for r in data:
		print(r,end = ' ')