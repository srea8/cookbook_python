# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 23:40:27
# @Last Modified by:   srea
# @Last Modified time: 2019-09-22 18:53:17


#****************************#
#匹配或者搜索特定模式的文本
#****************************#

text = 'yeah, but no, but yeah, but no, but yeah'

print(text.startswith('yeah'))
print(text.endswith('yeah'))
print(text.find('no'))

import re

def MatchString(text):
	if re.match(r'\d+/\d+/\d+',text):
		print('yes')
	else:
		print('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
MatchString(text1)
MatchString(text2)

# 想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
# 等价于re.compile(r'\d+/\d+/\d+')
dateMatch = re.compile(r'\d+/\d+/\d+')
def MatchString1(text):
	if dateMatch.match(text):
		print('yes')
	else:
		print('no')

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'		
MatchString1(text1)
MatchString1(text2)
mm = dateMatch.match(text1)
print(mm)
print(mm.group(0))
# print(mm.group(1))  #报错
print(mm.groups())   #结果为()

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.match(r'PyCon',text))      #从字符串开始去匹配
print(dateMatch.findall(text))      #全部字符串查找

# 定义正则式的时候，通常会利用括号去捕获分组
# 想精确匹配，确保你的正则表达式以$结尾
dateMatch1 = re.compile(r'(\d+)/(\d+)/(\d+)')
text1 = '11/27/2012'
m = dateMatch1.match(text1)
print('\n'+str(m))
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())

f = dateMatch1.findall(text)
print(f)

for mouth,day,year in f:
	print('{}-{}-{}'.format(year,mouth,day))

# findall() 方法会搜索文本并以列表形式返回所有的匹配。 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替
for m in dateMatch1.finditer(text):
	print(m.group())    ####11/27/2012    3/13/2013
	print(m.groups())    ####('11', '27', '2012')   ('3', '13', '2013')


