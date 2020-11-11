# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 22:04:17
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 22:12:24

#****************************#
#需要并发执行的代码创建/销毁线程
#threading 库可以在单独的线程中执行任何的在 Python 中可以调用的对象
#start() 方法时，它会调用你传递进来的函数，并把你传递进来的参数传递给该函数
# Python中的线程会在一个单独的系统级线程中执行（比如说一个 POSIX 线程或者一个 Windows 线程），这些线程将由操作系统来全权管理

# 由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。
# 所以，Python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等），而不是需要多处理器并行的计算密集型任务。

# 线程同步(event 对象最好单次使用)
# Event 对象包含一个可由线程设置的信号标志，它允许线程等待某些事件的发生。在初始情况下，event 对象中的信号标志被设置为假。
# 如果有线程等待一个 event 对象，而这个 event 对象的标志为假，那么这个线程将会被一直阻塞直至该标志为真。
# 一个线程如果将一个 event 对象的信号标志设置为真，它将唤醒所有等待这个 event 对象的线程。
# 如果一个线程等待一个已经被设置为真的 event 对象，那么它将忽略这个事件，继续执行。
#****************************#

import time
from threading import Thread,Event

def countdown(n,started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

started_evt = Event()

print('launching countdown')
t = Thread(target=countdown,args=(5,started_evt),daemon=True)
t.start()

started_evt.wait()
print('countdown is running')
# t.join()

class CountdownTask(Thread):
    def __init__(self,n):
        super(CountdownTask,self).__init__()
        self._running = True
        self.n = n

    def terminate(self):
        self._running = False

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)


c = CountdownTask(5)
# c.start()
# t1 = Thread(target=c.run,args=(10,))
# t1.start()
# c.terminate()
# t1.join()

import multiprocessing
p = multiprocessing.Process(target=c.start)
p.run()   #多进程不能用start，有tb   TypeError: can’t pickle _thread.lock objects

