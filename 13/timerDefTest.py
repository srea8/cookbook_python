# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 16:31:05
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 16:31:18

#****************************#
#记录程序执行多个任务所花费的时间
#通常我们会在time的基础上构造一个更高级的接口来模拟一个计时器
#这个类定义了一个可以被用户根据需要启动、停止和重置的计时器
#  它会在 elapsed 属性中记录整个消耗时间
#****************************#

import time

class Timer:
    def __init__(self, func=time.perf_counter):  #使用 time.perf_counter() 函数可以确保使用系统上面最精确的计时器
    # def __init__(self, func=time.time):  #使用 time.time() 或 time.clock() 计算的时间精度因操作系统的不同会有所不同
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already Started!')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not Started')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def countdown(n):
    while n>0:
        n -= 1

t = Timer()

#first use method
t.start()
countdown(10000000)
t.stop()
print('first elapsed:',t.elapsed)
t.reset()

#second use method
with t:
    countdown(10000000)
print('second elapsed:',t.elapsed)
t.reset()

#thrid use method
with Timer() as t2:
    countdown(10000000)
print('thrid elapsed:',t2.elapsed)

#fourth use methon
t = Timer(time.process_time)
with t:
    countdown(10000000)
print('fourth elapsed:',t.elapsed)

