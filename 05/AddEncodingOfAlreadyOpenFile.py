# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 23:28:52
# @Last Modified by:   srea
# @Last Modified time: 2019-10-01 00:19:27

#****************************#
#想在不关闭一个已打开的文件前提下增加或改变它的Unicode编码
#如果你想给一个以二进制模式打开的文件添加Unicode编码/解码方式， 可以使用 io.TextIOWrapper() 对象包装它
#
#****************************#

import urllib.request
import io

u = urllib.request.urlopen('https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p16_add_change_encoding_of_already_open_file.html')
# f = io.TextIOWrapper(u, encoding='utf-8')
# texts = f.read()
# for text in texts:
# 	print(text,end='')


import sys
print(sys.stdout.encoding)
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
print(sys.stdout.encoding)