# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 16:25:45
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 17:40:39


#****************************#
#需要将一个字符串分割为多个字段，
#但是分隔符(还有周围的空格)并不是固定的
#****************************#

import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
print(line.split(';'))
print(re.split(r'[;,\s]\s*',line))   ###数组

fields = re.split(r'(;|,|\s)\s*',line)
print (fields)

values = fields[::2]
delimiters = fields[1::2]+['。']
print(values)
print(delimiters)

#####zip 压缩数组   合二为一
print(list(zip(values,delimiters)))
print(''.join(v+d for v,d in zip(values,delimiters)))

# 不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的话， 确保你的分组是非捕获分组
print(re.split(r'(?:;|,|\s)\s*',line))
