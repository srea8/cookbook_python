# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-21 22:53:41
# @Last Modified by:   srea
# @Last Modified time: 2019-12-21 23:15:37

#****************************#
#
#
#
#****************************#

class JpgCC(object):
	"""docstring for JpgCC"""
	def __init__(self, arg):
		super(JpgCC, self).__init__()
		self.arg = arg
		print('jpg')

	def _getjpg(self,name):
		print('jpg_name:{}'.format(name))

	def getjpg(self,name):
		self._getjpg(name)