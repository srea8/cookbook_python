# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-01 00:21:58
# @Last Modified by:   srea
# @Last Modified time: 2019-10-01 00:23:48

#****************************#
#想在文本模式打开的文件中写入原始的字节数据
#将字节数据直接写入文件的缓冲区即可
#能够通过读取文本文件的 buffer 属性来读取二进制数据
#****************************#

import sys

# sys.stdout.write(b'Hello!')     #TypeError: must be str, not bytes
sys.stdout.buffer.write(b'hello!')