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
import loglibTest
import logging

logging.basicConfig()
loglibTest.func()

logging.getLogger('loglibTest').level=logging.DEBUG
loglibTest.func()