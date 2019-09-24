# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 20:29:39
# @Last Modified by:   srea
# @Last Modified time: 2019-09-23 20:54:05


#****************************#
#需要以忽略大小写的方式搜索与替换文本字符串
# re模块中使用flags=re.IGNORECASE
#****************************#

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python',text))
print(re.findall('python',text,flags=re.IGNORECASE))

print(re.sub('python','haha',text))
print(re.sub('python','haha',text,flags=re.IGNORECASE))
# 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持一致

# 使用该函数的话可以保持大小写
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()    #首字母大写
        else:
            return word
    return replace

print(re.sub('python',matchcase('haha'),text,flags=re.IGNORECASE))
