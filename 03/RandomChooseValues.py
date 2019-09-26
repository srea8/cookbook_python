# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-26 21:18:15
# @Last Modified by:   srea
# @Last Modified time: 2019-09-26 23:00:48


#****************************#
#从一个序列中随机抽取若干元素，或者想生成几个随机数
#要想从一个序列中随机的抽取一个元素，可以使用 random.choice()
#为了提取出N个不同元素的样本用来做进一步的操作，可以使用 random.sample() 
#****************************#

import random

def RollScript():
	while True:	
		k = input(u"请输入：")
		if k.startswith("%roll"):
			# w = random.choice(['i love you','i miss you','i am you'])
			w = random.randint(1,100)
			print(w)
			# return(0)

# RollScript()

import numpy as np

a = np.zeros(shape = (100),dtype = int)
b = [1,2,3,4,5,6,7,8,9,10,11,12]
print(a)
print(random.choice(a))
# print(random.sample(a,10))      #报错TypeError: Population must be a sequence or set.  For dicts, use list(d).
print(random.sample(b,10))

random.shuffle(b)    ###打乱顺序
print(b)

print(random.randint(1,100))
print(random.random())
print(int(random.random()*100))

print(random.getrandbits(2))             ####二进制位随机，结果为10进制

print(random.uniform(1,100))             #####均匀分布
print(random.gauss(1,100))              ####高斯分布



# random 模块使用 Mersenne Twister 算法来计算生成随机数。这是一个确定性算法， 但是你可以通过 random.seed() 函数修改初始化种子
random.seed(1)
print(random.sample(b,2))
random.seed(1)    #种子一样
print(random.sample(b,2))    #结果相同
random.seed(2)    #种子不一样
print(random.sample(b,2))   #结果不同
# 可以看到当seed()没有参数时，每次生成的随机数是不一样的，而当seed()有参数时，每次生成的随机数是一样的，同时选择不同的参数生成的随机数也不一样