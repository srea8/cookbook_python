# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-08 18:14:22
# @Last Modified by:   srea
# @Last Modified time: 2019-12-08 22:30:18

#****************************#
#你的代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)， 并且你还需要让回调函数拥有额外的状态值，以便在它的内部使用到。
#callback函数调用
# 一部分原因是回调函数通常会跟请求执行代码断开。 因此，请求执行和处理结果之间的执行环境实际上已经丢失了。
# 如果你想让回调函数连续执行多步操作， 那你就必须去解决如何保存和恢复相关的状态信息了
#****************************#



def apply_async(func,args,*tt,callback):
	result = func(*args)
	callback(result)
##function callback
def printresult(result):
	print('Got:{}'.format(result))

def add(x,y):
	return x+y
apply_async(add,(1,2),4,callback=printresult)

##class callback
class ResultHandler:
	def __init__(self,args):
		self.args = args

	def handler(self,result):
		self.args += 1
		print('[{}] Got:{}'.format(self.args,result))

r = ResultHandler(0)
apply_async(add,(2,3),callback=r.handler)
apply_async(add,('Hello','World'),callback=r.handler)


##closefunction callback
def make_handler1():
	sequence = 0
	def handler(result):
		nonlocal sequence
		sequence += 1          #需要声明nonlocal  否则UnboundLocalError: local variable 'sequence' referenced before assignment
		print('[{}] Got:{}'.format(sequence,result))
	return handler


handler1 = make_handler1()
apply_async(add,(2,3),callback=handler1)


##coroutine callback (协程)
def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

handler2 = make_handler2() 
next(handler2)     ###需要先执行到yield
apply_async(add,(2,3),callback=handler2.send)