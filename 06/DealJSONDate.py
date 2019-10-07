# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-10-07 18:28:34
# @Last Modified by:   srea
# @Last Modified time: 2019-10-07 21:13:42

#****************************#
# JSON, 全称JavaScript Object Notation，它通过对象和数组的组合来表示数据。在JavaScript中一切都是对象，因此，任何支持的类型都可以通过JSON来表示，常用的类型有数据和对象
# 读写JSON(JavaScript Object Notation)编码格式的数据
# json 模块提供了一种很简单的方式来编码和解码JSON数据, 其中两个主要的函数是 json.dumps() 和 json.loads()
# 如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据
# JSON编码支持的基本数据类型为 None ， bool ， int ， float 和 str ， 以及包含这些类型数据的lists，tuples和dictionaries。 
# 对于dictionaries，keys需要是字符串类型(字典中任何非字符串类型的key在编码时会先转换为字符串)。
#****************************#

import json
from pprint import pprint

data = {
	'name' : 'ACME',
	'shares' : 100,
	'price' : 543.23
}

# 如果你想获得漂亮的格式化字符串后输出，可以使用 json.dumps() 的indent参数
json_str = json.dumps(data, indent=4)
print(json_str)
print(type(json_str))

k = json.loads(json_str)    #将一个JSON编码的字符串转换回一个Python数据结构
print(k)
print(type(k))

with open('json_str.json','w') as f:
	json.dump(data,f)

with open('json_str.json','r') as f:
	data = json.load(f)
	print(data)
	pprint(data)


print(json.dumps(False))   #false

d = {
	'a': True,
	'b': 'Hello',
	'c': None,
}

print(json.dumps(d))
pprint(json.dumps(d))

# JSON解码会根据提供的数据创建dicts或lists。 如果你想要创建其他类型的对象，可以给 json.loads() 传递object_pairs_hook或object_hook参数
s = '{"name": "ACME", "shares": 50, "price": 490.1}'

from collections import OrderedDict
data = json.loads(s,object_hook = OrderedDict)
print(data)

# 将一个JSON字典转换为一个Python对象例子


class JSONObject:
	def __init__(self,d):
		self.__dict__ = d

data = json.loads(s,object_hook = JSONObject)
print(data.name)




from urllib.request import urlopen
u = urlopen('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=02003390_43_hao_pg&wd=csv.writerows%E7%A9%BA%E8%A1%8C&oq=csv&rsv_pq=c009974f002212cf&rsv_t=fd01flCy8yoz%2F6HAwST0OgNgWRSEsK5G93UM98Mt0CayfDlo9PBhh8tWpj%2BMkgJxwu4zcnt8g%2FcT&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=27&rsv_sug1=3&rsv_sug7=100&bs=csv')
print(u.read().decode('utf-8'),end='')


# 对象实例通常并不是JSON可序列化的,如果你想序列化对象实例，你可以提供一个函数，它的输入是一个实例，返回一个可序列化的字典
class Point:
	def __init__(self,a,b):
		self.a = a
		self.b = b

p = Point(2,3)
# print(json.dumps(p))    #TypeError: Object of type Point is not JSON serializable

def serialize_instance(obj):
	d = {'__classname__' : type(obj).__name__ }
	d.update(vars(obj))
	return d

classes = {
	'Point': Point
}

def unserialize_object(d):
	clsname = d.pop('__classname__',None)
	if clsname:
		cls = classes[clsname]
		obj = cls.__new__(cls)
		for key,value in d.items():
			setattr(obj,key,value)
		return obj
	else:
		return d

s = json.dumps(p,default = serialize_instance)
print(s)
pprint(s)

a = json.loads(s,object_hook = unserialize_object)
print(a)
print(a.a)