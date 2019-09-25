# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-25 14:31:53
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-25 14:48:56

#****************************#
#需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现
#可以使用 decimal 模块
#如果对精度要求不是太高，没必要使用该方法！
#****************************#


a = 4.2
b = 2.1

print(a+b)


######使用decimal ,注意数字需要用字符串表示
from decimal import Decimal

c = Decimal(4.2)
d = Decimal(2.1)

print(c+d)


e = Decimal('4.2')
f = Decimal('2.1')

print(e+f)

print((a+b)==Decimal('6.3'))
print((c+d)==Decimal('6.3'))
print((e+f)==Decimal('6.3'))

#####使用decimal，控制数字位数和四舍五入运算,先得创建一个本地上下文并更改它的设置
from decimal import localcontext
g = Decimal('4.2')
h = Decimal('1.3')
print(g/h)

with localcontext() as ctx:
	ctx.prec = 3
	print(g/h)

with localcontext() as ctx:
	ctx.prec = 30
	print(g/h)

print(g/h)

# 大数加减
nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))    #计算错误,计算精度影响

import math
print(math.fsum(nums))   #更精确计算能力来解决
