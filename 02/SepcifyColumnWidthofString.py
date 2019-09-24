# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 14:06:06
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 16:42:52

#****************************#
#有一些长字符串，想以指定的列宽将它们重新格式化
#使用 textwrap 模块来格式化字符串的输出
#****************************#

import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under.\
\r\n12edasd"

print(s)
print(textwrap.fill(s,20))
print(textwrap.fill(s,70))

print(textwrap.fill(s,70,initial_indent = '   13  '))    #在段首插入
print(textwrap.fill(s,70,subsequent_indent=' 12 '))     #除第一行外其他行插入


# import os
# print(os.get_terminal_size().columns)   #OSError: [WinError 6] 句柄无效
