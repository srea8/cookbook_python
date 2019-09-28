# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 15:56:38
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 16:36:09

#****************************#
#想像一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。 也就是不允许覆盖已存在的文件内容
#可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题
#x模式是一个Python3对 open() 函数特有的扩展。 在Python的旧版本或者是Python实现的底层C函数库中都是没有这个模式的
#****************************#

with open('nofile.txt','xt') as f:
	f.write('File Not Exist!!!')
	print("File Not Exist!!!",file = f)

with open('nofile.bin','xb') as f:
	f.write(b'File Not Exist!!!')
	# print(b"File Not Exist!!!",file = f)   #####tips：必须使用文本模式打开，二进制模式打开的话，打印会报错