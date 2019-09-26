# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 09:29:06
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-26 16:50:49

#****************************#
#需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节
#格式化输出单个数字的时候，可以使用内置的 format() 函数

# 需要转换或者输出使用二进制，八进制或十六进制表示的整数
# 可以分别使用 bin() , oct() 或 hex() 函数
#****************************#


x = 1234.123456


# 格式化字符串

print(format(x,'0.2f'))
print(format(x,'10.2f'))

print(format(x,'>10.2f'))
print(format(x,'<10.2f'))
print(format(x,'^10.2f'))

print(format(x,','))
print(format(x,'0,.2f'))

#大写E和小写e的区别
print(format(x,'e'))
print(format(x,'E'))
print(format(x,'0.2e'))

print('the values is {:0,.2f}'.format(x))

print('%0.2f'%x)
print('%0.3f'%x)


#######使用二进制，八进制或十六进制表示的整数
x = 123456
print(bin(x))    #2进制
print(oct(x))    #8进制
print(hex(x))    #16进制

#####如果你不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))


####负数也可以使用同样的方法
y = -123456

#这样是带符号的
print(bin(y))
print(oct(y))
print(format(y,'x'))


#这样是不带符号的
print(format(2**32+y,'b'))
print(format(2**32+y,'x'))



######其他进制转10进制
z = '4d2'
p = '10011010010'
q = '0755'
q1 = '0o775'

print(int(z,16))
print(int(p,2))
print(int(q,8))   
# print(int(q1,8))      ###答案493  错误



