# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 17:12:08
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-26 17:16:46

#****************************#
#创建或测试正无穷、负无穷或NaN(非数字)的浮点数
#可以使用 float() 来创建它们
#为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数
#****************************#

a = float('nan')
b = float('inf')
c = float('-inf')
d = float('nan')
print(a)
print(b)
print(c)
print(a==d)
print(a is d)

# NaN值会在所有操作中传播，而不会产生异常
print(a+45)
print(b+45)

print(b+c)
print(a+b)

import math

print(math.isinf(a))
print(math.isnan(a))
print(math.isinf(b))
print(math.isinf(c))
