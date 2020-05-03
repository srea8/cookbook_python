# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 16:12:10
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 16:12:29

#****************************#
#想给某个函数库增加日志功能，但是又不能影响到那些不使用日志功能的程序
#
#
#****************************#
import logging

log = logging.getLogger(__name__)   #创建一个和调用模块同名的logger模块
log.addHandler(logging.NullHandler())   #将一个空处理器绑定到刚刚已经创建好的logger对象上。 一个空处理器默认会忽略调用所有的日志消息。

# Example function (for testing)
def func():
    log.critical('A Critical Error!')
    log.debug('A debug message')