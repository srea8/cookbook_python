# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-30 20:56:45
# @Last Modified by:   srea
# @Last Modified time: 2019-09-30 21:32:17

#****************************#
#检测文件的MD5码
#使用hashlib模块
#****************************#

import os
import hashlib


# path = os.getcwd() + '/test.gz'
# print(path) 


#直接使用
def GetFileMD5_0(path):
	myHash = hashlib.md5()

	f = open(path,'rb')
	while True:
		b = f.read(4096)
		if not b:
			break
		myHash.update(b)
	f.close()
	return(myHash.hexdigest())



#####使用iter

from functools import partial

def GetFileMD5(path,RECORD_SIZE = 4096):
	with open(path,'rb') as f:
		myHash = hashlib.md5()
		for i in iter(partial(f.read,RECORD_SIZE),b''):
			myHash.update(i)
	return (myHash.hexdigest())


for i in os.listdir('.'):
	path = os.getcwd()+'/'+i
	print(path)
	if os.path.isfile(path):
		print(GetFileMD5(path))
		print(GetFileMD5_0(path))