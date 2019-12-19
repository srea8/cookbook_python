# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-02 22:35:41
# @Last Modified by:   srea
# @Last Modified time: 2019-12-02 23:07:58

#****************************#
#你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器， 但是它的参数太多了，导致调用时出错
#partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数
#****************************#

# def spam(a,b,c,d):
# 	print(a,b,c,d)

# from functools import partial
# s1 = partial(spam,1)
# s1(2,3,4)
# s2 = partial(spam,1,d=3)
# s2(2,4)


# ###sort中作为key值的应用
# points=[(1,2),(3,4),(5,6),(7,8)]
# import math
# def distance(p1,p2):
# 	x1,y1 = p1
# 	x2,y2 = p2
# 	return math.hypot(x2-x1,y2-y1)

# p = (4,3)
# positions = points.sort(key = partial(distance,p))
# print(points)


###partial() 通常被用来微调其他库函数所使用的回调函数的参数
import logging
from multiprocessing import Pool
from functools import partial

def output_result(result,log=None):
	if log is not None:
		log.debug('Got:%r',result)

def add(x,y):
	return x+y

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	log = logging.getLogger('test')
	p = Pool()
	p.apply_async(add,(3,4),callback = partial(output_result,log = log))
	p.close()
	p.join()
