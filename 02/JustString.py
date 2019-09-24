# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 10:10:26
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 10:28:40

#****************************#
#通过某种对齐方式来格式化字符串
#对于基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center() 方法
#****************************#


text = 'Hello world'

#just的用法,使用ljust,rjust,center
print(text+'!')
print(text.ljust(20)+'!')   ##右边20个字符
print(text.rjust(20)+'!')   ##左边20个字符
print(text.center(20)+'!')  ##左右各10个字符

print(text.ljust(20,'#')+'!')   ##右边20个字符
print(text.rjust(20,'*')+'!')   ##左边20个字符
print(text.center(20,'-')+'!')  ##左右各10个字符

#format的用法,使用 <,> 或者 ^ 字符后面紧跟一个指定的宽度
print(format(text,'>20'))     ##等价于rjust
print(format(text,'<20'))     ##等价于ljust
print(format(text,'^20'))     ##等价于center

#格式
print(format(text,'#>20s'))     ##等价于rjust
print(format(text,'*<20s'))     ##等价于ljust
print(format(text,'-^20s'))     ##等价于center

# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中
print('{:>10s} {:>10s}'.format('Hello','world'))
print('{:->10s} {:#^10s}'.format('Hello','world'))


# format() 函数的一个好处是它不仅适用于字符串,可以用来格式化任何值
x = 1.213
print(format(x,'#>10'))
print(format(x,'#^10.2f'))

# 也可以使用%来格式化文本，但是format更加适用
print('%-20s' % text)
print('%20s' % text)
