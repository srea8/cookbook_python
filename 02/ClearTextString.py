# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 22:40:34
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 10:10:01


#****************************#
# 网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉
# 可以使用translate进行映射替换
#****************************#

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

###可以使用translate进行映射替换
rmap = {
	ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None  # Deleted
}

a = s.translate(rmap)  
print(a)

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = a.translate(cmb_chrs)
print(b)

a = unicodedata.normalize('NFD', a)    ###需要先将字符标准化,使用 unicodedata.normalize() 将原始输入标准化为分解形式字符
c = a.translate(cmb_chrs)
print(c)