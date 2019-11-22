# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-11-22 23:59:25
# @Last Modified by:   srea
# @Last Modified time: 2019-11-23 00:04:24

#****************************#
#尝试将zip元组转成List
#****************************#

a = ['1','2',['3','4']]
b = ['5','6',['7','8']]
c = (1,2)

d = zip(a,b)
e = list(c)
f = list(d)
g = [list(i) for i in zip(a,b)]

print ('{d}\n{e}\n{f}\n{g}'.format(d=d,e=e,f=f,g=g))