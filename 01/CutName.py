# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 14:12:12
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:06:25


#****************************#
## 命名切片
# 你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码
# slice(20,23)等效于20：23
# slice(20,24,2)等效于20： 23 ： 2
#****************************#


######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'

cost = int(record[20:23])*float(record[31:37])
print(cost)

SHARES = slice(20,23)
PRICE = slice(31,37,2)
cost1 = int(record[SHARES])*float(record[PRICE])
print(PRICE.start)
print(PRICE.stop)
print(PRICE.step)
print(cost1)


#切片不合适的情况下可能出现越界情况
#你还可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上。 这个方法返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止。 这样，使用的时就不会出现 IndexError 异常
PRICEs = slice(1,213,2)
s = 'Helloworld'
print(PRICEs.indices(len(s)))