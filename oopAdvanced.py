#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 数据封装、继承、多态只是面向对象程序设计中最基础的3个阶段，
# 在python 中，面向对象还有很多高级特性，允许我们写出更强大的功能

print('------------多重继承，定制类，元类----------------')
from types import MethodType

class Student(object):
    pass
s=Student()
s.name="张三"     # 动态给实例绑定一个方法
print(s.name)

# 给实例绑定一个方法
def set_age(self,age):
    self.age=age


s.set_age=MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(188)  # 调用实例方法
print(s.age)

s2=Student()        # 创建一个新实例
#s2.set_age(25)      # 尝试调用新方法，可以发现绑定的方法对这个实例是不起作用的

# 为了给所有实例都绑定方法，可以给class 绑定方法

def set_score(self,score):
    self.score=score
Student.set_score=set_score

# 给 class 绑定方法后，所有实例均可使用
s.set_score(1000)
print(s.score)  # 1000
s2.set_score(666)
print(s2.score)

# 通常情况下，上面的 set_score 方法可以直接定义在class 中，但动态
# 绑定允许我们在程序运行中动态给class加上功能，这在静态中很难实现

print('-----------使用__slots__-----------------------')
# 我们想要限制实例的属性，比如只允许对 Student 实例添加 name,age属性
# 为了达到限制的目的，python 允许在定义class 的时候，定义一个特殊的 __slots__ 变量，来限制class 实例能添加的呃属性
class StudentTest(object):
    __slots__=('name','age')

ss=StudentTest()
ss.name="终端"
ss.age=219
# ss.score=99  #  AttributeError 由于score没有被放在__slots__中，所有不能绑定score属性

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__

print('------@property-------------------')
# Pythen 内置的 @property 装饰器就是负责把一个方法变成属性调用的

class StudentProperty(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('输入的参数类型不正确，请输入int类型')
        if value<0 or value>100:
            raise ValueError('输入的参数范围不正确！ 0~100')
        self._score=value
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    
    @property
    def age(self):
        return 2017-self._birth

s=StudentProperty()
s.score=60   # 实际转化为s.set_score(60)
print(s.score)      # 实际转化为 s.get_score()

# s.score=9999

# 还可以定义只读属性，只定义getter方法 ，不定义setter方法就是一个只读属性
print('----------上面birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间算出来------------')



