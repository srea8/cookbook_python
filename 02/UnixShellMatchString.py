# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 18:06:04
# @Last Modified by:   srea
# @Last Modified time: 2019-09-22 12:01:57


#****************************#
#使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串

#fnmatch() 函数使用底层操作系统的大小写敏感规则(不同的系统是不一样的)来匹配模式
#fnmatchcase()完全使用你的模式大小写匹配
#****************************#

from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')]) 
print([name for name in names if fnmatch(name, 'Dat*.cSv')])#windows可以找到，mac不能找到


##fnmatch  和  fnmatchcase的区别
print(fnmatch('foo.txt','*.txt'))   #true
print(fnmatch('foo.txt','*.TXT'))	#true
print(fnmatchcase('foo.txt','*.txt'))	#true
print(fnmatchcase('foo.txt','*.TXT'))	#false


#####匹配地址
addresses = [
    '5412 N CLARK ST',
    '54L2 W CLARK ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

print([address for address in addresses if fnmatchcase(address,'* ST')])
print([address for address in addresses if fnmatchcase(address,'54[0-9][0-9] *CLARK*')])