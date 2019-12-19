# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-02 23:12:18
# @Last Modified by:   srea
# @Last Modified time: 2019-12-04 23:29:43

#****************************#
#将单方法的类转换为函数
#大多数情况下，可以使用闭包来将单个方法的类转换成函数
#****************************#

####单方法类
from urllib.request import urlopen

class UrlTemplate(object):
	"""docstring for UrlTemplate"""
	def __init__(self, template):
		super(UrlTemplate, self).__init__()
		self.template = template

	def open(self, **kwargs):
		return urlopen(self.template.format_map(kwargs))

# Example use. Download stock data from yahoo
yahoo = UrlTemplate('https://www.baidu.com/d/quotes.csv?s={names}&f={fields}')
with open('web.txt','w',encoding='utf-8') as f:
	for line in yahoo.open(names='FB', fields='sl1c1v'):
		f.write(line.decode('utf-8'))
		# print(line.decode('utf-8'))



###闭包方式简化单方法类
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

# Example use
yahoo = urltemplate('https://www.baidu.com/d/quotes.csv?s={names}&f={fields}')
with open('web1.txt','w',encoding='utf-8') as f:
	for line in yahoo(names='FB', fields='sl1c1v'):
		f.write(line.decode('utf-8'))