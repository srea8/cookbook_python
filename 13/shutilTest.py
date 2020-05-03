# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2020-05-03 00:33:19
# @Last Modified by:   srea
# @Last Modified time: 2020-05-03 00:33:30

#****************************#
#shutil 模块有很多便捷的函数可以复制文件和目录
# 底层语义模拟了类似的Unix命令
#****************************#


import shutil

# Copy src to dst. (cp src dst)
# shutil.copy(src, dst)

# Copy files, but preserve metadata (cp -p src dst)
# shutil.copy2(src, dst)

# Copy directory tree (cp -R src dst)
# shutil.copytree(src, dst)

# 如果你想保留被复制目录中的符号链接
# shutil.copytree(src, dst, symlinks=True)

# copytree() 可以让你在复制过程中选择性的忽略某些文件或目录。 你可以提供一个忽略函数，接受一个目录名和文件名列表作为输入，返回一个忽略的名称列表
def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('.pyc')]
# print(ignore_pyc_files('12.pyc',['12.pyc','13.pyc','13.py']))
# shutil.copytree(src, dst, ignore=ignore_pyc_files)

# 由于忽略某种模式的文件名是很常见的，因此一个便捷的函数ignore_patterns()已经包含在里面了
# shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*~', '*.pyc'))

# 使用 copytree() 复制文件夹的一个棘手的问题是对于错误的处理
try:
    shutil.copytree(src, dst)
except shutil.Error as e:
    for src, dst, msg in e.args[0]:
        # src is source name
        # dst is destination name
        # msg is error message from exception
        print(dst, src, msg)

# Move src to dst (mv src dst)
# shutil.move(src, dst)