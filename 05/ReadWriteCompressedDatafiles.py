# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 16:50:46
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 16:56:39

#****************************#
#想读写一个gzip或bz2格式的压缩文件
#gzip 和 bz2 模块可以很容易的处理这些文件,两个模块都为 open() 函数提供了另外的实现来解决这个问题
#要注意的是选择一个正确的文件模式是非常重要的。 如果你不指定模式，那么默认的就是二进制模式，如果这时候程序想要接受的是文本数据，那么就会出错
#****************************#

import gzip
import bz2
with gzip.open('test.gz','wt') as g:
	g.write('hello gzip')

with gzip.open('test.gz','rt') as g:
	for line in g:
		print(g)


with bz2.open('test.bz2','wt') as b:
	b.write('hello bz2')

with bz2.open('test.bz2','rt') as b:
	for line in b:
		print(b)

