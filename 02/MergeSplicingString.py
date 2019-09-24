# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-09-24 10:30:21
# @Last Modified by:   shenzhijie
# @Last Modified time: 2019-09-24 10:44:46

#****************************#
#将几个小的字符串合并为一个大的字符串
#想要合并的字符串是在一个序列或者 iterable 中，那么最快的方式就是使用 join() 方法
#想在源码中将两个字面字符串合并起来，你只需要简单的将它们放到一起，不需要用加号(+)
#****************************#

parts = ['Is', 'Chicago', 'Not', 'Chicago?']

#使用join
print(parts)
print(' '.join(parts))
print(' .'.join(parts))


#使用‘+’
a = 'Is Chicago'
b = 'Not Chicago?'
print(a+' '+b)
print('{} {}'.format(a,b))
print(a,b,a)

datas = ['ACME', 50, 91.1]
print(datas)

print(' '.join(str(data) for data in datas))

#使用sep
c = ';;;'
print(a + ':' + b + ':' + c) # Ugly
print(':'.join([a, b, c])) # Still ugly
print(a, b, c, sep=':') # Better