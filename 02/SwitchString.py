# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 17:41:17
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 18:03:52


#****************************#
#字符串开头或结尾匹配:使用endswith和startswith
#****************************#

filename = 'test.txt'
print(filename.endswith('txt'))
print(filename.startswith('txt'))
print(filename.startswith('tes'))

url = 'http://www.python.org'
print(url.startswith('http:'))


import os

filename = os.listdir('../')
print(filename)
print(any(name for name in filename if name.endswith('.py')))
print(any(name for name in filename if name.endswith('.git')))
print(list(name for name in filename if name.endswith(('.git','.md'))))
# print(list(name for name in filename if name.endswith(['.git','.md'])))  #必须使用元组作为参数


#等价于切片匹配
filename = 'test.txt'
print(filename[-4:]=='.txt')

#等价于正则表达式匹配 
# re.match( )方法匹配的是以xxx开头的字符串，若不是开头的，尽管属于str内，则无法匹配
import re
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:',url).group())   #成功匹配可以使用group可以得到匹配的值