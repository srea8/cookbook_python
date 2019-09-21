# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-08 11:36:52
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:10:14


#****************************#
#现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量#
#list unpack
#****************************#



p = (4,5)
x = p
print (x)
date = ["jjj",21,9,(12,21,2,12,2)]
name,age,n,(kk,k,kkk,kkkk,kkkkk) = date
_,dd,ddd,_ = date
print (ddd)
print (age)

#string unpack
s = "hello"
a,b,c,d,e = s
print (a)