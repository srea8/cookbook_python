# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 20:55:05
# @Last Modified by:   srea
# @Last Modified time: 2019-09-30 23:26:39

#****************************#
#想使用原始文件名执行文件的I/O操作
#默认情况下，所有的文件名都会根据 sys.getfilesystemencoding() 返回的文本编码来编码或解码
#如果因为某种原因你想忽略这种编码，可以使用一个原始字节字符串来指定一个文件名即可
#****************************#
import sys

# print(sys.getfilesystemencoding())
with open('jalap\xf1o.txt', mode='wt') as f:
	f.write('spicy!')

