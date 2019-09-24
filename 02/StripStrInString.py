# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 21:17:21
# @Last Modified by:   srea
# @Last Modified time: 2019-09-23 22:34:36


#****************************#
#去掉文本字符串开头，结尾或者中间不想要的字符，比如空白
#开头，结尾:strip() 方法能用于删除开始或结尾的字符，但是不会对字符本身造成影响
# 中间:想处理中间的空格，那么你需要求助其他技术。比如使用 replace() 方法或者是用正则表达式替换
#****************************#

s = ' Hello, world! \n'
print(s)
print(s.strip())     #从两端执行删除操作
print(s.lstrip())    #从左执行删除操作
print(s.rstrip())    #从右执行删除操作
print(s+'\n')

######可以删除特定字符
t = '-----hello====='
print(t)
print(t.strip('-'))     #从两端执行删除操作
print(t.lstrip('-'))    #从左执行删除操作
print(t.rstrip('-'))    #从右执行删除操作
print(t+'\n')

#删除开头、结尾、中间的空格或者字符
s = ' Hello,    world! \n'
print(s.replace(' ',''))

import re
print(re.sub('\s+','',s))    #匹配任意空白字符删除

# 将字符串 strip 操作和其他迭代操作相结合
# 比如从文件中读取多行数据
import os
path = os.getcwd()
# print(path)
# print(os.listdir('./'))
filename = path+"\\FindAndMatchInString.py"


# with open(filename,'rb') as f:   #需要加上'rb',否则报错UnicodeDecodeError: 'gbk' codec can't decode byte 0x80
                                 #但是进行字符操作时会报错TypeError: a bytes-like object is required, not 'str'
with open(filename,'r',encoding='utf-8') as f:    #使用该种方式打开的话，进行字符操作不会报错
	lines = (line.strip('text') for line in f)   #这种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列表中去
										 # 只是创建一个生成器，并且每次返回行之前会先执行 strip 操作
	for line in lines:
		print(line)

