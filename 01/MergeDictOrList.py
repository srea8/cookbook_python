# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 16:05:37
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:24:40


#****************************#
#合并多个字典和映射
#****************************#


####ChainMap 类只是在内部创建了一个容纳这些字典的列表 并重新定义了一些常见的字典操作来遍历这个列表
from collections import ChainMap

a = {'x':1,'y':2}
b = {'x':3,'z':4}

c = ChainMap(a,b)
print(c)
print(len(c))
print(c['x'])
print(list(c.keys()))

del c['x']
print(a,b)

# del c['z']  字典的更新或删除操作总是影响的是列表中第一个字典,第一个字典中没有会报错

######ChainMap 对于编程语言中的作用范围变量（比如 globals , locals 等）是非常有用的
values = ChainMap()
values['x'] = 4
values = values.new_child()
values['x'] = 3
values['x'] = 1
values = values.new_child()
print(values)

values = values.parents
values['x'] = 2
print(values)

values['x'] = 5
print(values)

values = values.parents
print(values)



###合并字典:创建一个完全不同的字典对象（或者是破坏现有字典结构）。 
# 同时，如果原字典做了更新，这种改变不会反应到新的合并字典中去
a = {'x':1,'y':2}
b = {'x':3,'z':4}

merged = dict(b)
merged.update(a)
print(merged)
a['x']=16
print(a)
print(merged)

#ChainMap 使用原来的字典，它自己不创建新的字典
