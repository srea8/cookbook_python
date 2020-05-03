# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-21 23:07:54
# @Last Modified by:   srea
# @Last Modified time: 2019-12-23 00:33:29

#****************************#
#将代码组织成由很多分层模块构成的包
#从第九章调用第十章的包体
#****************************#
import os
import sys火箭今年
 
sys.path.append("E:\\python\\cookbook_python\\")

import _10 
print(dir(_10))

_10.graphics.formats.bar.x
print(dir(_10))




# from _10.graphics.formats import jpg as jpg

# print (dir(jpg))  ##使用dir查看方法列表

# j = jpg.JpgCC(1)
# j.getjpg('li')