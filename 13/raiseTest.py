# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-02 23:04:32
# @Last Modified by:   srea
# @Last Modified time: 2020-05-02 23:32:27

#****************************#
#raise 和 assert的使用
#向标准错误打印一条消息并返回某个非零状态码来终止程序运行
#****************************#

##raise
class raisetest():
    def __init__(self):
        super(raisetest,self).__init__()

    def raisedef(self):
        print('raise')
        # raise IOError("Telnet Server Failed To Find A Usable Port To Bind!")
        raise ValueError('无法将字符串 {} 转化为物品类型'.format('12'))

#assert
def test1():
    '一堆逻辑'
    res = 1
    return 1

res1 = test1()
try:
    assert res1 == 2
except KeyError:
    print(2)
except AssertionError:
    print(1)

#raise
rt = raisetest()
try:
    rt.raisedef()
except IOError as e:
    print(e.errno,e.strerror,e.args,e.filename)
except Exception as e:
    print(e.args)