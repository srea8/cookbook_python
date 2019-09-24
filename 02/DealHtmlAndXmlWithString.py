# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 15:52:13
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 16:02:28

#****************************#
# 将HTML或者XML实体如 &entity; 或 &#code; 替换为对应的文本
# 如果你想替换文本字符串中的 ‘<’ 或者 ‘>’ ，使用 html.escape() 函数可以很容易的完成
# 编码使用escape()， 解码使用unescape()
#****************************#

import html

s = 'Elements are written as "<tag>text</tag>".'
print (s)
print(html.escape(s))    #escaping of quotes
print(html.escape(s,quote=False))   # Disable escaping of quotes

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))



s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

s = "Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;."
print(html.unescape(s))
a = "Elements are written as '&lt;tag&gt;text&lt;/tag&gt;'."
print(html.unescape(a))


from xml.sax.saxutils import unescape
print(unescape(a))
t = 'The prompt is &gt;&gt;&gt;'
print(unescape(t))