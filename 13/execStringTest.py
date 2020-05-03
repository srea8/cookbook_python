# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 00:29:04
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 00:29:10

#****************************#
#执行一个外部命令并以Python字符串的形式获取执行结果
#使用 subprocess.check_output() 函数
#
#****************************#


import subprocess
out_bytes = subprocess.check_output(['cmd','-a'])
out_text = out_bytes.decode('utf-8')
print(out_text)


