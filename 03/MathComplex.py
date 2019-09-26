# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 16:51:42
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-26 17:11:35

#****************************#
# 学习cmath和numpy模块

#使用复数来执行一些计算操作
#复数可以用使用函数 complex(real, imag) 或者是带有后缀j的浮点数来指定
#如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
# 如果你使用 numpy ，可以很容易的构造一个复数数组并在这个数组上执行各种操作
#****************************#


###创建复数的方法
a = complex(4,6)
print(a)
b = 4-5j
print(b)

print(a.real)    #实部
print(a.imag)    #虚部
print(a.conjugate())     #共轭复数

print(a+b)
print(a*b)
print(a/b)
print(a-b)

print(abs(b))    #绝对值

# 如果要执行其他的复数函数比如正弦、余弦或平方根，使用 cmath 模块
import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.tan(a))
print(cmath.exp(a))   #指数
print(cmath.sqrt(-1))     #cmath可以产生复数


import math
# math.sin(a)    #不能计算复数的sin值
print(math.sin(math.radians(90)))
print(math.cos(-1))
# print(math.sqrt(-1))    #math不能产生复数值