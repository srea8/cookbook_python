# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-21 22:53:30
# @Last Modified by:   srea
# @Last Modified time: 2019-12-21 23:02:02

#****************************#
#
#
#
#****************************#

from . import JpgCC

class PngCC(JpgCC):
	"""docstring for JpgCC"""
	def __init__(self, arg):
		super(PngCC, self).__init__()
		self.arg = arg
		print('png')

	def _getpng(self,name):
		print('png_name:{}'.format(name))

	def getpng(self,name):
		self._getjpg()