# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-23 21:05:49
# @Last Modified by:   srea
# @Last Modified time: 2019-09-23 21:14:11


#****************************#
#试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配
#用点(.)去匹配任意字符的时候，忘记了点(.)不能匹配换行符
#为了修正这个问题，你可以修改模式字符串，增加对换行的支持
#****************************#

import re


###不能跨行匹配
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */'''

print(comment.match(text1))
print(comment.match(text2))
print(comment.findall(text1))
print(comment.findall(text2))

#跨行匹配,(?:.|\n) 指定了一个非捕获组
comment = re.compile(r'/\*((?:.|\n?)*?)\*/')
print(comment.match(text1))
print(comment.match(text2))
print(comment.findall(text1))
print(comment.findall(text2))

# 或者可以使用re.DOTALL,对于简单的情况使用 re.DOTALL 标记参数工作的很好,复杂情况不适用
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.match(text1))
print(comment.match(text2))
print(comment.findall(text1))
print(comment.findall(text2))