# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 14:38:41
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 15:24:33

#****************************#
#需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等
#使用带有 rt 模式的 open() 函数读取文本文件
#为了写入一个文本文件，使用带有 wt 模式的 open() 函数
#如果是在已存在文件中添加内容，使用模式为 at 的 open() 函数

####在确定编码的情况下，使用正确的编码，在文件编码不确定的情况下，最好使用默认的utf-8
#****************************#

#在进行文件操作前最好加上文件是否存在的判断
import os
# if not os.path.exists('test.txt'):  #其实这种方法还是有个问题，假设你想检查文件“test_data”是否存在，但是当前路径下有个叫“test_data”的文件夹，这样就可能出现误判

if not os.path.isfile("test.txt"):   #通过这个方法，如果文件”test-data”不存在将返回False，反之返回True
	with open("test.txt", mode='w', encoding='utf-8') as f:
		print(" 文件创建成功！")
else:
	print("文件存在！")

#使用os.access()方法判断文件是否可进行读写操作
# path为文件路径，mode为操作模式，有这么几种:
# os.F_OK: 检查文件是否存在;
# os.R_OK: 检查文件是否可读;
# os.W_OK: 检查文件是否可以写入;
# os.X_OK: 检查文件是否可以执行

if os.access("test.txt", os.F_OK):           #检查文件是否存在
    print ("Given file path is exist.")
 
if os.access("test.txt", os.R_OK):           #检查文件是否可读
    print ("File is accessible to read")

if os.access("test.txt", os.W_OK):            #检查文件是否可以写入
    print ("File is accessible to write") 

if os.access("test.txt", os.X_OK):           #检查文件是否可以执行
    print ("File is accessible to execute")



###在例子程序中的with语句给被使用到的文件创建了一个上下文环境， 
# 但 with 控制块结束时，文件会自动关闭。
# 你也可以不使用 with 语句，但是这时候你就必须记得手动关闭文件

###############直接打开文件####################
f = open('test.txt','rt')
date = f.read()
print(date)
f.close()

###############使用with#######################

with open('test.txt','rt') as f:           #文件不存在的时候报错
	###方法1   read the entire file as a signle string
	# date = f.read()     
	# print(date)


	#方法2  iterate over    注意回车符号
	for line in f:
		print (line)
		# print(1)



with open('test.txt','wt') as f:      ###wt 会清除文件内的内容
	date = "您 test!!!\n"
	date1 = "wt test1!!!"

	#方法1   使用write写入文件
	f.write(date)
	f.write(date1)

	#方法2   使用print，写入文件（print函数的输出重定向到文件中）    tips：必须使用文本模式打开，二进制模式打开的话，打印会报错
	print(date,file = f)
	print(date1,file = f)


with open('test.txt','at') as f:      ###at  在原有文件后面追加内容
	date = "wt test!!!\n"
	date1 = "wt test1!!!"

	#方法1   使用write写入文件
	f.write(date)
	f.write(date1)

	#方法2   使用print，写入文件
	print(date,file = f)
	print(date1,file = f)


######注意文件编码问题############
####在open过程中加入encoding编码#####
with open('test.txt','rt',encoding='latin-1') as f:
	print('#######ending########')
	print(f.read())



######如果在windows和unix中使用，需要主要换行符的问题####
# windows：\r\n
# Unix:\n
######默认处理方式：python会统一进行处理，对换行符进行替换####
# # Newline translation enabled (the default)
f = open('hello.txt', 'rt')
f.read()
# >>> 'hello world!\n'

# # Newline translation disabled
g = open('hello.txt', 'rt', newline='')
g.read()
# >>> 'hello world!\r\n'




#####读取或者写入一个文本文件时，你可能会遇到一个编码或者解码错误###
# with open('test.txt','rt',encoding='ascii') as f:     #存在中文，使用ascii编码报错
# with open('test.txt','rt',encoding='ascii',errors = 'replace') as f:     ##编码报错的时候使用未知字符替代
with open('test.txt','rt',encoding='ascii',errors = 'ignore') as f:       ##编码报错的时候直接忽视，删除报错字符
	for line in f:
		print (line)    