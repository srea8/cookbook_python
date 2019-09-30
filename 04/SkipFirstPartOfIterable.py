# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-29 11:01:41
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-30 17:14:22

#****************************#
#想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们
#itertools.dropwhile() 函数可以完成这个任务
# 如果你已经明确知道了要跳过的元素的个数的话，那么可以使用 itertools.islice() 来代替
#****************************#

import os
path = os.getcwd() + '\SkipFirstPartOfIterable.py'
print(path)
# filepath = os.listdir('.')
# print(filepath)

# 假定你在读取一个开始部分是几行注释的源文件
with open(path,encoding = "utf-8") as f:
	for line in f:
		print (line)

# 跳过开始部分的注释行的话
from itertools import dropwhile
with open(path,encoding='utf-8') as f:
	for line in dropwhile(lambda line: line.startswith('#'), f):
		print (line)



# 基于根据某个测试函数跳过开始的元素。 如果你已经明确知道了要跳过的元素的个数的话
from itertools import islice
with open(path,encoding='utf-8') as f:
	for line in islice(f,7,None):
		print(line)



# 使用startswith(),可以将全部为#号开头的行去除，和预期只去除文件开头行为＃的结果不符
with open(path,encoding='utf-8') as f:
	lines = (line for line in f if not line.startswith('#'))
	for line in lines:
		print (line)  