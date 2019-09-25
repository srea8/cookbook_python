# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 21:43:24
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-25 14:31:18


#****************************#
#对浮点数执行指定精度的舍入运算
#对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可
#不要将舍入和格式化输出搞混淆了,目的只是简单的输出一定宽度的数，你不需要使用 round() 函数
# 不要试着去舍入浮点值来”修正”表面上看起来正确的问题
#****************************#

print(round(1.232,0))
print(round(1.232,1))
print(round(1.232,2))
print(round(1.232,3))
print(round(1.232,4))

print(round(-1.232,0))
print(round(-1.272,1))
print(round(-1.277,2))
print(round(-1.277,3))
print(round(-1.277,4))


# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。 也就是说，对1.5或者2.5的舍入运算都会得到2
print(round(1.5,0))
print(round(2.5,0))

# 传给 round() 函数的 ndigits 参数可以是负数,舍入运算会作用在十位、百位、千位等上面
print(round(1213123,-1))
print(round(1213123,-3))


# 格式化精度
x = 1.23456
print(x)
print(format(x,'0.2f'))
print(format(x,'0.3f'))
print(format(x,'0.9f'))
print(format(x,'f'))