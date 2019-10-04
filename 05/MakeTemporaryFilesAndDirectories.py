# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-02 23:29:17
# @Last Modified by:   srea
# @Last Modified time: 2019-10-03 11:16:20

#****************************#
# 需要在程序执行时创建一个临时文件或目录，并希望使用完之后可以自动销毁掉
# 为了创建一个匿名的临时文件，可以使用 tempfile.TemporaryFile,通常来讲文本模式使用 w+t ，二进制模式使用 w+b
# TemporaryFile() 、NamedTemporaryFile() 和 TemporaryDirectory() 函数 应该是处理临时文件目录的最简单的方式了，
# 因为它们会自动处理所有的创建和清理步骤。 在一个更低的级别，你可以使用 mkstemp() 和 mkdtemp() 来创建临时文件和目录。
# 尽可能以最安全的方式使用 tempfile 模块来创建临时文件。 包括仅给当前用户授权访问以及在文件创建过程中采取措施避免竞态条件。
#****************************#

from tempfile import TemporaryFile

with TemporaryFile('w+t') as f:
	f.write('111')
	f.write('222')
	f.write('333')
	f.seek(1)   #调整光标位置到第二个字符前，从0开始计数
	date = f.read()
	print(date)

with TemporaryFile('w+t',encoding = 'utf-8') as f:
	f.write('11中')
	f.write('222')
	f.write('333')
	f.seek(1)   #调整光标位置到第二个字符前，从0开始计数
	date = f.read()
	print(date)

####NamedTemporaryFile
from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)


####TemporaryDirectory
from tempfile import TemporaryDirectory

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)




####tempfile
import tempfile
print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())