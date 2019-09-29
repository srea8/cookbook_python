# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-27 14:15:07
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-27 14:19:20

#****************************#
#Python os获取当前目录，上级目录，上上级目录
#****************************#

import os

print ('***获取当前目录***')
print (os.getcwd())
print (os.path.abspath(os.path.dirname(__file__)))
print (os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

print ('***获取上级目录***')
print (os.path.abspath(os.path.dirname(os.getcwd())))
print (os.path.abspath(os.path.join(os.getcwd(), "..")))

print ('***获取上上级目录***')
print (os.path.abspath(os.path.join(os.getcwd(), "../..")))

print ('***获得当前路径下所有文件名***')
print (os.listdir('.'))