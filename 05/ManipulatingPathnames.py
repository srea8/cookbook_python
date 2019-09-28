# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-28 22:00:57
# @Last Modified by:   srea
# @Last Modified time: 2019-09-28 22:55:33

#****************************#
#需要使用路径名来获取文件名，目录名，绝对路径
#使用 os.path 模块中的函数来操作路径名
# 因为 os.path 模块知道Unix和Windows系统之间的差异并且能够可靠地处理类似 Data/data.csv 和 Data\data.csv 这样的文件名
# 使用os.listdir 模块获取指定路径下的所有文件
#****************************#

import os

####拆分文件的路径
path = 'E:/python/cookbook_python/05'

print(os.path.basename(path))     ##get the last component of the path
print(os.path.dirname(path))    ##get the directory name


print(os.path.join('04',os.path.basename(path)),'03')    #join path components together

path = '~/05/test.txt.txt'
print(os.path.expanduser(path))       ####expand the user‘s home directory


print(os.path.splitext(path))     ###split the file extension


#####判断文件是否存在  
###判断是否存在
print(os.path.exists('test.txt'))
print(os.path.exists('test1.txt'))

#判断是否为文件
print(os.path.isfile('test.txt'))
print(os.path.isfile('test1.txt'))

#判断是否为路径
print(os.path.isdir('test'))
print(os.path.isdir('05'))


#判断是否为链接
print(os.path.islink('E:/python/cookbook_python/05/test'))

#获得文件的链接
print(os.path.realpath('E:/python/cookbook_python/05/test'))


###获得文件的其他数据,这个需要注意一下被访问的文件是否有权限
#获得文件的大小
print(os.path.getsize('test.txt'))
print(os.path.getmtime('test.txt'))    #没有可读性，需要使用time翻译

import time
print(time.ctime(os.path.getmtime('test.txt')))



######获取文件夹下文件列表
print(os.listdir('.'))
path = "E:/python/cookbook_python/"
print(os.listdir(path))

filenames = [name for name in os.listdir('.') if os.path.isfile(os.path.join('.',name))]     ####获取文件夹下的所有文件
print(filenames)

dirnames = [name for name in os.listdir('.') if os.path.isdir(os.path.join('.',name))]     ####获取文件夹下的所有文件夹
print(dirnames)

pyfiles = [name for name in os.listdir('.') if name.endswith('.py')]           ##筛选特定文件
print(pyfiles)


##### 对文件名进行匹配
##方法1：使用glob
import glob
pyfiles1 = glob.glob('IoOper*.py')
print(pyfiles1)

txtfiles = glob.glob('te*.txt')
print(txtfiles)


##方法2：使用fnmatch
import fnmatch
pyfiles2 = [name for name in os.listdir('.') if fnmatch.fnmatch(name,'Io*.py')]
print(pyfiles2)

#####获得文件名后还想获得文件的大小或者修改时间等，需要配合os.path或者os.stat()使用
pyfiles1 = glob.glob('IoOper*.py')
print(pyfiles1)


###使用os.path
name_sz_date = [(name,os.path.getsize(name),time.ctime(os.path.getmtime(name))) for name in pyfiles1]
for name,filesize,filetime in name_sz_date:
	print(name,str(filesize)+' Bytes',filetime,sep = '---')

###使用os.stat
name_sz_date1 = [(name,os.stat(name)) for name in pyfiles1]
for name,meta in name_sz_date1:
	print(name,meta,sep = '---')



###获得指定文件夹下的所有文件
def FileName(filedir):
	for root,dirs,files in os.walk(filedir):
		print('root_dir:', root)    # 当前目录路径
		print('sub_dir:', dirs)     # 当前路径下所有子目录
		print('files:', files)      # 当前路径下所有非目录子文件

FileName('E:/python/cookbook_python')