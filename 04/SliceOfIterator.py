# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-29 10:46:46
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-29 11:05:58

#****************************#
#想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到
# 迭代器和生成器不能使用标准的切片操作，因为它们的长度事先我们并不知道(并且也没有实现索引)
#函数 itertools.islice() 正好适用于在迭代器和生成器上做切片操作
# 这里要着重强调的一点是 islice() 会消耗掉传入的迭代器中的数据。 必须考虑到迭代器是不可逆的这个事实
#****************************#

def Count(n):
	while True:
		yield n 
		n+=1

c = Count(0)
# print(c[10:20])  #报错

import itertools
for x in itertools.islice(c,10,20):
	print(x, end='---')

for x in itertools.islice(c,None,10):
	print(x)

for x in itertools.islice(c,10,1000):
	print(x,end = '--')