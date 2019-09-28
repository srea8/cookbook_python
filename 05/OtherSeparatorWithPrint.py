# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 15:26:20
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 15:33:22

#****************************#
#使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符
#可以使用在 print() 函数中使用 sep 和 end 关键字参数，以你想要的方式输出
#str.join() 的问题在于它仅仅适用于字符串
#****************************#

print('ACE',1,'中')
print('ACE',1,'中',sep = ',')
print('ACE',1,'中',sep = ',',end = '.')
print('ACE',1,'中',sep = ',',end = '.\n')

for i in range(5):
	# print(i)
	print(i,end=' ')


# print('.'.join())   ####报错，str instance，int found
print(','.join(str(i) for i in ('ACE',1,2)))    #join处理字符串之外的内容时需要进行转换处理