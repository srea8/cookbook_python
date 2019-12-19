# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-01 23:27:07
# @Last Modified by:   srea
# @Last Modified time: 2019-12-02 22:30:24

#****************************#
#你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数， 而是希望通过某个快捷方式以内联方式来创建这个函数
#可以使用lambda表达式来代替
#
#****************************#

add = lambda a:a+12

print(add(12))

names = ['David Beazley', 'Brian Jones','Raymond Hettinger', 'Ned Batchelder']
print(sorted(names,key=lambda name:name.split()[-1].lower()))

for name in names:
	print(name.split()[-1].lower())

#使用lambda调用函数
def lam():
	print(2)
	lambda :print(1)
lam()

mf = lambda fa:lam()
# print(mf(fa=1))

#lambda表达式中的x是一个自由变量， 在运行时绑定值，而不是定义时就绑定，这跟函数的默认值参数定义是不同的
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10),b(10))


funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
	print(f(0))


####python  switch#####
def add( a, b ):
    return a + b
def sbb( a, b ):
    return a - b
def mul( a, b ):
    return a * b
def div( a, b ):
    return a / b

oper = { '+' : add, '-' : sbb, '*' : mul, '/' : div }
def mySwitch( o, x, y ):
    #return oper[o]( x, y )
    #oper.get(o)等价于oper[0]取字典中的某一项
    return oper.get(o)( x, y )

print (mySwitch( '/', 10, 20 ))


