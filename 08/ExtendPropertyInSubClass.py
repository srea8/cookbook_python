# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-05 21:57:21
# @Last Modified by:   srea
# @Last Modified time: 2019-12-05 22:27:00

#****************************#
#基本的@property使用，可以把函数当做属性用,@property的set，deleter，get
#
#
#****************************#

####@property  demo1
class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    # Deleter function
    @name.deleter
    def name1(self):
        raise AttributeError("Can't delete attribute")

a = Person('11')
print(Person.name)
a.name = 'xiaoming'
print(a.name)
print(Person('lihua').name)
print(a._name)
# print(Person._name)
# print(a._name)
# del a.name


####@property  demo2
class Goods(object):
    def __init__(self):
        #原价
        self.original_price = 100
        #折扣
        self.discount = 0.8
 
    @property
    def price(self):
        #实际价格=原价*折扣
        new_price = self.original_price*self.discount
        return new_price
    @price.setter
    def price(self,value):
        self.original_price = value
    @price.deleter
    def price(self):
        del self.original_price
obj = Goods()
print(obj.price)
obj.price = 200
print(obj.price)           #调用的price.setter   设置的original_price
del obj.price
# print(obj.price)           #此处已经删除了obj.price(已屏蔽)


####property   demo3
class Foo(object):
    def get_name(self):
        print('get_name')
        return 'laowang'
 
    def set_name(self, value):
        '''必须两个参数'''
        print('set_name')
        return 'set value' + value
 
    def del_name(self):
        print('del_name')
        return 'laowang'
 
    NAME = property(get_name, set_name, del_name, 'description.')


print(Foo().NAME)
Foo().NAME = 'Alex'
print(Foo().NAME.__doc__)
print(Foo().NAME)



####property   demo4
class Person(object):
    def __init__(self, age):
        self.__age = age
 
    def set_age(self, value):
        self.__age = value
 
    def get_age(self):
        return self.__age
 
    AGE = property(get_age, set_age)
 
 
person = Person(15)
print(str(person.AGE))
person.AGE = 20
print(str(person.AGE))