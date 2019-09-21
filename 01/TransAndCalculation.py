# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-21 15:47:52
# @Last Modified by:   srea
# @Last Modified time: 2019-09-21 16:01:17


#****************************#
# description：优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数
#****************************#

import time 

A = [1,21,3,13,1,23,1]
#######花费时间长########
start_time = time.perf_counter()
print(sum(x for x in A))
end_time = time.perf_counter()
print ('代码运行时长：%f'%(end_time-start_time))


#######花费时间短########
start_time = time.perf_counter()
print(sum([x for x in A]))
end_time = time.perf_counter()
print ('代码运行时长：%f'%(end_time-start_time))

print(max(x for x in A))
print(min(x for x in A))