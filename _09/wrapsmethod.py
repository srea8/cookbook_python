# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-04-24 23:47:22
# @Last Modified by:   srea
# @Last Modified time: 2020-04-24 23:48:01

#****************************#
#初始装饰器，完成一个函数时间的运行监控装饰器功能
#****************************#


from functools import wraps
import time


def getruntime(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        r = func(*args,**kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print('run_time:{}'.format(run_time))
        return r
    return wrapper


@getruntime
def testruntime():
    n = 10000
    while n > 1:
        # print(n)
        n -= 1

testruntime()