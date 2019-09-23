# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 20:57:20
# @Last Modified by:   srea
# @Last Modified time: 2019-09-23 21:05:13


#****************************#
#用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹配。 而你想修改它变成查找最短的可能匹配。
#需要将匹配变成非贪婪模式，从而得到最短的匹配，可以在模式中的*操作符后面加上?修饰符
# 通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配。
#****************************#
import re

# 模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。 但是在正则表达式中*操作符是贪婪的
str_pat = re.compile(r'"(.*)"')
str1 = '"You are lady"'
str2 = '"Me" and "she"'
print(str_pat.findall(str1))
print(str_pat.findall(str2))

# 可以在模式中的*操作符后面加上?修饰符,使得匹配变成非贪婪模式，从而得到最短的匹配
str_pat1 = re.compile(r'"(.*?)"')
str1 = '"You are lady"'
str2 = '"Me" and "she"'
print(str_pat1.findall(str1))
print(str_pat1.findall(str2))

