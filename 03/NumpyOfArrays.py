# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 17:26:00
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-26 18:06:11

#****************************#
# 需要在大数据集(比如数组或网格)上面执行计算
# 涉及到数组的重量级运算操作，可以使用 NumPy 库
# 需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组
#****************************#

x = [1,2,3,4]
y = [1,2,3,4]
print(x+y)    #将表二加在表一后面


# 两种方案中数组的基本数学运算结果并不相同
# NumPy 中的标量运算(比如 ax * 2 或 ax + 10 )会作用在每一个元素上
import numpy as np

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
print(a+b)
print(a*4)
print(a+10)

def f(x):
	return(x**3+1)

print(f(a))     #不需要像list一样，使用for将每个值提取出来

#np还可以像math模块一样进行计算
print(np.sqrt(a))
print(np.cos(a))

#使用numpy生成数组,shape确定数组维度和数组大小

grid = np.zeros(shape = [100, 10 ,10],dtype = int)
print(grid)
print(grid+10)
print(np.sin(grid+10))


#####numpy还有索引功能
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print(a[1])
print(a[:,1])
print(a[1:2,1:3])
print(a+[1,2,3,4])
print(a < 3,a,10)
print(np.where(a < 3,a,10))    #找到大于的数值进行替换，小于的保留


#需要执行矩阵和线性代数运算，
m = np.matrix([[1,2,3],[1,2,3],[1,2,3]])
print(m)
print(m.T)    ##np的转置
# print(m.I)   ##不存在逆

n = np.matrix([[1],[2],[3]])
print(n)
print(n.T)    #矩阵的转置
print(n.I)    #矩阵的逆

print ((n.I)*n)
print(m*n)



# 求矩阵乘法、寻找行列式、求解线性方程组

import numpy.linalg

print(numpy.linalg.det(m))           ###行列式
print(numpy.linalg.eigvals(m))         ###特征值
# x = numpy.linalg.solve(m, n)        ###求解mx=v，无解情况下报错
# print(x) 


