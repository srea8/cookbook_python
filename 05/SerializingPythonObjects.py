# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-03 11:36:40
# @Last Modified by:   srea
# @Last Modified time: 2019-10-03 15:40:48

#****************************#
#需要将一个Python对象序列化为一个字节流，以便将它保存到一个文件、存储到数据库或者通过网络传输它
#序列化最普遍的做法就是使用 pickle 模块
#为了将一个对象转储为一个字符串，可以使用 pickle.dumps()
# 为了从字节流中恢复一个对象，使用 pickle.load() 或 pickle.loads() 函数

# 千万不要对不信任的数据使用pickle.load()。
# pickle在加载时有一个副作用就是它会自动加载相应模块并构造实例对象。
# 但是某个坏人如果知道pickle的工作原理，
# 他就可以创建一个恶意的数据导致Python执行随意指定的系统命令。
# 因此，一定要保证pickle只在相互之间可以认证对方的解析器的内部使用。
#****************************#

import pickle

data = '111222333444'

p1 = pickle.dumps(data)

print(p1)
t1 = pickle.loads(p1)
print (t1)
# 
# data = pickle.loads(f)

p2 = pickle.dumps(data,True)   #如果为 True ，则该参数指定用更快以及更小的二进制表示来创建 pickle
print(p2)
t2 = pickle.loads(p2)
print(t2)

f = open('hello.txt','wb')
p3 = pickle.dump(data,f)

f = open('hello.txt', 'rb')
t3 = pickle.load(f)
print (t3)


f = open('nofile.bin','wb')
pickle.dump([1,2,3,4],f)
pickle.dump('hello',f)
pickle.dump({'apple','pear','banana'},f)
f.close()

f = open('nofile.bin','rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))