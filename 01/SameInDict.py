# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:12:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:09:20


#****************************#
###怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

#####python3才支持
#####python2报错        print(a.keys()&b.keys())
# TypeError: unsupported operand type(s) for &: 'list' and 'list'
#****************************#



a = {1:'21',2:'22',3:'33'}
b = {1:'21',4:'24',3:'34'}


####为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作
# 尽管字典的 values() 方法也是类似，但是它并不支持这里介绍的集合操作。 某种程度上是因为值视图不能保证所有的值互不相同，这样会导致某些集合操作会出现问题。
print(a.keys()&b.keys())
print(a.keys())
print(a.values())
# print(a.values()&b.values())    #error TypeError: unsupported operand type(s) for &: 'dict_values' and 'dict_values'

###两个字典的不同点
print(a.keys()-b.keys())
print(a.items()-b.items())


####构建排除几个值的新字典
c = {key : a[key] for key in a.keys() - {1,3}}
print(c)