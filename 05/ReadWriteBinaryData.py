# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 15:34:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 15:55:16

#****************************#
# 想读写二进制文件，比如图片，声音文件等等
# 使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据
# 在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串
# 在写入的时候，必须保证参数是以字节形式对外暴露数据的对象
#****************************#

with open('bintest.bin','wb') as f:
	data = b'Hello World!'
	f.write(data)

with open('bintest.bin','rb') as f:
	for line in f:
		print(line)

#####byte string
bindata = b'hello'
print(bindata[0])

#####text string
txtdata = 'hello' 
print(txtdata[0])


#############二进制文件中读取或者写入文本数据###########
###写入文本数据
with open('bintest.bin','wb') as f:
	text = 'Hello World'
	f.write(text.encode('utf-8'))

###读取二进制文件
with open('bintest.bin','rb') as f:
	for line in f:
		print(line)

###读取文本数据
with open('bintest.bin','rb') as f:
	data = f.read(16)
	text = data.decode('utf-8')
	print(text)


# 二进制I/O还有一个鲜为人知的特性就是数组和C结构体类型能直接被写入，而不需要中间转换为自己对象
####允许通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的内存中去
# 但是使用这种技术的时候需要格外小心，因为它通常具有平台相关性，并且可能会依赖字长和字节顺序(高位优先和低位优先)
import array
a = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
	f.write(a)

b = array.array('i',[0,0,0,0,0,0,0,0,0,0])
print(b)
with open('data.bin','rb') as f:
	f.readinto(b)
print(b)

