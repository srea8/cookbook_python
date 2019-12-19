# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Srea
# @Date:   2019-12-04 23:15:37
# @Last Modified by:   srea
# @Last Modified time: 2019-12-08 17:54:24

#****************************#
#super的用法
#类中的命名方式
#****************************#

####super的用法
class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        super(TimesFive, self).__init__(value)
        self.value *= 5


class PlusTwo(MyBaseClass):
    def __init__(self, value):
        super(PlusTwo, self).__init__(value)
        self.value += 2

###使用super继承时，在后面的先调用
class GoodWay(TimesFive, PlusTwo):
    def __init__(self, value):
        super(GoodWay, self).__init__(value)


foo = GoodWay(5)
print('Should be 5*(5+2) and is ', foo.value)
print(GoodWay.mro())


###super  example2
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print ('Parent')
    
    def bar(self,message):
        print ("%s from Parent" % message)
 
class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild,self).__init__()    
        print ('Child')
        
    def bar(self,message):
        super(FooChild, self).bar(message)
        print ('Child bar fuction')
        print (self.parent)
 
if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')


###python  类中命名方式,配合super的使用

class A(object):

    def __init__(self):#系统定义方法
        self.string='A string'
        self._string='A _string'
        self.__string='A __string'#私有变量

    def fun(self):
        return self.string + ' fun-A'

    def _fun(self):
        print(1)
        return self._string+'  _fun-A'

    def __fun(self):#私有方法
        return self.__string+' __fun-A'

    def for__fun(self):#内部调用私有方法
        return self.__fun()

class B(A):

    def __init__(self):#系统定义方法
        super().__init__()
        self.string = 'B string'

    def _fun(self):
        super()._fun()
        print('{}'.format('superB'))
        return A._fun(self)


a=A()
print (a.string)
print (a._string)
# print a.__string 不可访问

print (a.fun())
print (a._fun())
# print (a.__fun())   #不可访问
print (a._A__fun())   #可访问
print (a.for__fun())

b=B()
print (b.fun())
print (b.fun().__len__())#系统定义函数
print (b._fun())


####self和super
class FatherClass(object):
	def __init__(self):
		super().__init__()
		self.name = 'fulei'
		print(self.name)

	def A(self):
		print('我是父类')

class SubClass(FatherClass):
	"""docstring for super"""
	def __init__(self, arg):
		super(SubClass, self).__init__()
		self.arg = arg
		print(self.arg)
	
	def A(self):
		print('我是子类')

	def B(self):
		self.A()
		super().A()

sub = SubClass('zilei')
sub.B()



#####super(type,type)
class Person(object):
    def __init__(self, name):
        self.name = name
    # Getter function
    @property
    def name(self):
        print('fulei_get')
        return self._name
    # Setter function
    @name.setter
    def name(self, value):
        print('fulei_set')
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value
    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")
              
        
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)  ##??? 这种用法第一次见, 作用原理/作用流程是什么?
        #返回一个父类的实例,然后调用其方法
        #关键是: super(SubPerson, SubPerson) 如何使用的?
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)  

sp = SubPerson('liming')
print(sp._name)
print(sp.__class__.mro())
print(super(SubPerson,sp).name)
# print(super(SubPerson,self).name)
print(Person.name)
print(Person.__mro__)
print(super(SubPerson,SubPerson))     ##super(SubPerson, SubPerson) 指的是 Person (mro 中 SubPerson 的類:SubPerson 的下一個)
print(super(Person,SubPerson))       ##指的是 object (mro 中 Person 的類:Person 的下一個)

