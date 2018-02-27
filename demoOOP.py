#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 面向对象编程--Object Oriented Programming,简称OOP，是一种程序设计思想。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

# 面向过程的程序设计把计算机程序视为一系列命令集合、即一组函数的顺序执行。
# 为了减缓程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度

# 类名通常大写
# 变量私有，加两个下划线__
class Student(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score

    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        # 在方法中可以对参数做检查，避免传入无效的参数
        if 0<=score<=100:
            self.__score=score
        else:
            raise ValueError('输入的分数有误！')

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    
        
    def print_score(self):
        return ('%s,分数:%s' %(self.__name,self.__score))
        
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

# 创建类的实例
bart=Student('滨南',18)
bart.set_score(88)

lisa=Student('蹬蹬蹬',98)


print(bart.print_score(),bart.get_grade())
print(lisa.print_score(),lisa.get_grade())

print(Student)   # <class '__main__.Student'>

print('-------------继承和多态-----------')
# 在 OOP程序设计中，当我们定义一个class的时候，可以从现有的class继承，新的class称为子类（Subclass),
# 而被继承的class称为基类、父类或超类（Base class、Super class)

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running!')


class Cat(Animal):
    def run(self):
        print('cat is running!')

animal=Animal()
dog=Dog()
dog.run()

cat=Cat()
cat.run()

a=list() # a 是list类型

print(isinstance(dog,Animal))  # True
print(isinstance(dog,Dog)) # True               dog不仅是Dog还是Animal
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是反过来就不行
# 多态，一个对象有多种状态

print(isinstance(a,list))   # True
print(isinstance(cat,Cat))      # True

print(isinstance(animal,Cat)) # False

def run_twice(animal):
    animal.run()

run_twice(dog)
run_twice(cat)
run_twice(animal)

# 新增一个Tortouse对象
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

tortoise=Tortoise()
run_twice(tortoise)         # Tortoise is running slowly...
# 多态的作用：调用方只管调用，不管细节，而当我们新增一个Animal类的子类时，只要确run()方法是正确的，不用管原来的代码是如何调用的

# 开闭原则
# 对扩展开放:允许添加Animal子类；       对修改封闭：不需要修改依赖Animal类型的run_twice()等函数


print('---------------获取对象信息---------------')
# 判断数据类型,用type（）函数
print(type(3))
print(type(animal))
print(type(dog))

# 判断一个对象是否是函数，可以使用types 模块中定义的常量：
import types
def fn():
    pass

print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)


# 使用 dir() 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(3))
print(dir(dog))
print(dir(animal))
print(dir('eee'))

print('-----普通属性和方法----------------')
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x * self.x
obj=MyObject()

# 测试该对象的属性
print(hasattr(obj,'x'))    # 是否有属性 x
print(obj.x)
print(hasattr(obj,'y'))
obj.y=199
print(hasattr(obj,'y'))
print(obj.y)

# 如果获取不存在的属性，就会抛出 AttributeError 的错误
# getattr(obj,'z')

# 可以传入一个 default 参数，如果属性不存在，就返回默认值
print(getattr(obj,'z',404))

# 也可以获得对象的方法
print(obj,'power')
p=obj.power
print(p)
print(p())

# 实例属性和类属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Human(object):
    def __init__(self,name):
        self.name=name
h=Human('tianchunle')
h.score=99

# 如果Student 类本身需要绑定一个属性呢？ 可以直接在class中定义属性，这种属性是类属性，归Human类所有
class Humans(object):
    name="Human"    # 类属性

hh=Humans()  # 创建实例
print(hh.name)          #  Human 打印实例的name属性，因为实例没有name属性，所以会继续查找class的name操作
print(Humans.name)  # Human 打印类的name属性
hh.name="nizhenbang" # 给实例绑定name属性
print(hh.name)      # nizhengbang 由于实例属性优先级比类属性高，因此，他会屏蔽掉类的name属性
print(Humans.name)  # Human   但是类的属性name并没有消失，用 Humans.name 仍可以访问
del hh.name     # 删除实例的name属性
print(hh.name)      # 再次调用hh.name，由于实例的name属性没有找到，类的name属性就显示出来了

# 在编写程序的时候，千万不要对实例的属性和类属性使用相同的名字，因为相同名称的实例实行将屏蔽掉类
# 属性，当你删除实例属性的时候，在使用相同的名称，访问到的将是类属性





