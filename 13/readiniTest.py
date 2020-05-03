# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 00:47:32
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 00:47:54

#****************************#
#读取普通.ini格式的配置文件
#configparser 模块能被用来读取配置文件
# 配置文件中的名字是不区分大小写的
# prefix=/usr/local 和 prefix: /usr/local 等效
#****************************#


from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini')

sections = cfg.sections()
print(sections)

#获取数据
# print(cfg.get('installation','library'))
# print(cfg.getboolean('debug','log_errors'))
# print(cfg.getint('server','port'))
# print(cfg.getint('server','nworkers'))
# print(cfg.get('server','signature'))

# 写入数据
cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)

o = open('config.ini', 'w')
cfg.write(o)
o.close()#不要忘记关闭
