# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 16:39:56
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 16:48:50

#****************************#
#想使用操作类文件对象的程序来操作文本或二进制字符串
#使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
#****************************#
import io

####文本文件
s = io.StringIO()
print(s.write('Hello world!!!'))
print(s.getvalue())
print('\tsss',file = s)
print(s.getvalue())

s = io.StringIO('1111111')
print(s.read(5))    #####包装文件接口存在的字符
print(s.read())


####二进制文件
s = io.BytesIO()
print(s.write(b'binary data!!!'))
print(s.getvalue())


s = io.BytesIO(b'dadadad')
# print(b'1111',file = s)
s.write(b'1111?')
print(s.read())   #####包装文件接口存在的字符