# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-22 23:42:01
# @Last Modified by:   srea
# @Last Modified time: 2019-12-23 00:02:03

#****************************#
#命名空间包
#包路径下不包含 __init__.py 文件
#命名空间包的一个用处就是将位于不同物理路径下的包合并到一个逻辑命名空间当中,当然所有的这些路径都必须是命名空间包，即不能包含 __init__.py 文件
#****************************#

import sys

sys.path.append("./formats/")
sys.path.append("./primitive/")
import bar

print('1',dir(bar))
###tips:在两个bar文件都不存在__init__.py时，成立！
# 如果其中一个包不是命名空间包，那么导入的命名空间包处将报错   ModuleNotFoundError: No module named 'bar.y'
# import bar.x
import bar.y    #如果在x文件夹下加了__init__.py，那么在这导入y会报错，含__init__.py的路径会被优先找到
print('2',dir(bar))   #包下的模块只有在导入之后，才会存在包的属性当中,此处才能查询到x,y
print('3',bar,bar.__path__,type(bar.__path__),len(bar.__path__))   #用来区分普通意义上包含 __init__.py 的包 --- namespace 标志
print('4',bar.__file__,type(bar.__file__))   #命名空间包的 __file__ 属性为None 


"""
#命名空间包结果
1 ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
x
y
2 ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'x', 'y']
3 <module 'bar' (namespace)> _NamespacePath(['./formats\\bar', './primitive\\bar']) <class '_frozen_importlib_external._NamespacePath'> 2
4 None <class 'NoneType'>
"""

"""
# 普通包结果
如果两个目录都是非命名空间包，即普通意义上包含 __init__.py 包，那么也是将报错。这根 import 的搜索顺序有关，由于 spam_1 在搜索路径中优先被找到，
所以 import bar 导出的将是 spam_1/bar，而此 bar 包下无 y 和 z模块，所以会报模块 bar.y 不存在的错。

#需要先屏蔽导入bar.y
1 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
x
2 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'x']
3 <module 'bar' from './formats\\bar\\__init__.py'> ['./formats\\bar'] <class 'list'> 1
4 ./formats\bar\__init__.py <class 'str'>
# """
# bar.__path__.append("./primitive/bar")
# import bar.y
# print('5',bar,bar.__path__,type(bar.__path__),len(bar.__path__))
# print('6',dir(bar))