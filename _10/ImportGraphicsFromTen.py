# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-21 23:07:54
# @Last Modified by:   srea
# @Last Modified time: 2019-12-23 23:27:23

#****************************#
#将代码组织成由很多分层模块构成的包
#从第九章调用第十章的包体
#****************************#

from graphics.formats import jpg as jpg

j = jpg.JpgCC(1)
j.getjpg('li')

import ImportModelByStr
print(dir(ImportModelByStr))