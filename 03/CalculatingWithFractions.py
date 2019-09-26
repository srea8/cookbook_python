# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 17:17:22
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-26 17:25:09

#****************************#
#fractions 模块可以被用来执行包含分数的数学运算
#****************************#

from fractions import Fraction
a = Fraction(10,19)
print(a)
b = Fraction(10,19)
print(a+b)
print(a*b)

#####获取分数的除数与被除数
c = a*b
print(c.numerator)
print(c.denominator)


print(float(c))   ###将分数转成小数
print(c.limit_denominator(360))    ###最佳近似值,限制值的分母

x = 3.75
y = Fraction(*x.as_integer_ratio())      # 将浮点数转换为分数
print(y)