#!/usr/bin/env python3
# 直接运行python文件，在windows不可用，在linux和max上可以
# -*- coding: utf-8 -*-
# 告诉python解释器，按照UTF-8编码读取源代码。否则，输出的中文可能有乱码


# 调用函数
print(abs(100))
abs(-20)
# abs()函数，求绝对值

# 数据类型转换
print(int('1223'))

# 函数名其实就是指向一个函数的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-222))

# 在python中，定义一个函数要使用 def语句，依次写出函数名、括号、括号中的参数和冒号（：），
# 然后，在缩进块中编写函数体、函数的返回值用return语句返回


def mu_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(mu_abs(-444))

# 如果已经把mu_abs（）的函数定义保存为demoFunction.py 文件了，那么可以在该目录下启动python解释器,
# 用 from demoFunction import mu_abs来导入mu_abs()函数

# 空函数 如果想定义一个什么也不做的空函数，可以用pass语句


def nop():
    pass

# 通常 pass做占位符，可以在不知道函数做什么的时候让代码先跑起来

# 参数检查
# 调用函数时，如果参数的个数不对，python 解释器会自动检查出来，并抛出 TypeError
# 而参数类型不对，python解释器就无法帮我们检查出来

# 数据类型的检查可以通过 内置函数 isinstance()实现


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('您传入的参数类型不正确')
    if(x > 0):
        return x
    else:
        return -x


print(my_abs(-344))

# print(my_abs('sss'))

# 返回多个值
# import math 语句表示导入math包，并允许后续代码引用 math 包里的 sin、cos 等函数

import math


def move(x, y, step, angle=0):
    nx = x+step * math.cos(angle)
    ny = y+step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi/6)
print(x, y)
z = move(33, 44, 55, math.pi/6)
# 返回值是一个tuple! 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以接收一个yuple，按位置赋给对应的值
print(z)

print('函数的参数')
print('-------位置参数-----')
# 位置参数


def power(x):
    return x*x
# 对于 power(x)函数，参数 x 就是一个位置参数


def prwer2(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s


# 对于这个修改后的power2(x,n)函数，可以计算任意 n次方，x和n都是位置参数，传入的两个值按位置分别赋给 x,n
print(prwer2(5, 111))

print('---------默认参数---------')
# 默认参数


def prwer3(x, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
# 好处：最大的好处就是降低调用函数的难度


def enroll(name, gender):
    print('name', name)
    print('gender', gender)


enroll('Sarac', 'F')

# 添加年龄、城市等信息呢 ，把年龄城市设置为默认参数


def enrollOne(name, gender, age=9, city="济南"):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)


enrollOne('田春乐', '男')
enrollOne('Bob', 'M', 7)  # 按顺序
enrollOne('Adam', 'M', city='Tianjin')  # 不按顺序

# 默认参数的坑、坑、坑


def add_end(l=[]):
    l.append("EDF")
    return(l)


print(add_end([1, 2, 3]))  # [1, 2, 3, 'EDF']
print(add_end(['x', 't']))  # ['x', 't', 'EDF']

print(add_end())  # ['EDF']
print(add_end())  # ['EDF', 'EDF'] 结果不对了
# 原因：python函数在定义的时候，默认参数L的值就被计算出来了，即[],因为默认参数L也是一个变量，它指向一个对象[],每次调用
# 该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[] 了。
# 牢记：默认参数必须指向不变对象


def add_endTrue(l=None):
    if l is None:
        l = []
    l.append("END")
    return l


print(add_endTrue())  # ['END']
print(add_endTrue())  # ['END']

print('--------可变参数---------------')
# 可变参数


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    print(sum)
    return sum


# 在调用的时候，需要先组装出一个list或者 tuple:
calc([1, 2, 3, 4, 4, 5])
calc((1, 2, 3, 4, 5, 6))

# 可变参数,在参数前面加 *


def calcll(*numbers):
    sum = 0
    for n in numbers:
        sum += n*n
    print(sum)
    return sum


# 定义可变参数和定义一个list 或 tuple参数相比，仅仅在参数前面加了一个 * 号。在函数内部，参数numbers接收到的是一个tuple
# 因此，函数代码完全不变，但是，调用该函数时，可以传入任意个参数，包括0个参数
calcll(1, 2, 3, 4, 5)
calcll()
# 如果有一个list 或者 tuple，要调用一个可变参数
nums = [11, 22, 33]
calcll(*nums)
# *nums表示把nums这个list的所有元素作为可变参数传进去

print('---------关键字参数--------')
# 关键字参数允许你传入0或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dist。


def person(name, age, **kw):
    # 检查是否有city 和job参数
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 函数person 除了必选参数name和age外，还接受关键字kw。在调用该函数时，可以只传入必选参数
person('tainchunle', 21)
# 也可以传入任意个数的关键字参数
person('tianshuo', 12, city="金乡")
extra = {'city': '济南', 'job': '程序猿'}
person('tianshuo', 12, **extra)
# **extra 表示把extra这个dist的所有key-value 用关键字传入到函数的**kw参数，kw 将获得一个dist
# 注意：kw获得的dist是extra的一份拷贝，对kw的改动不会影响到函数外的extra

print("------------命名关键字参数--------")
# 作用：限制关键字参数的名字，命名关键字需要一个特殊的分隔符*，*后面的参数被视为命名关键字参数
# 例如,只接收city和job作为关键字参数


def personName(name, age, *, city, job='设计师'):
    print(name, age, city, job)


# 调用方法
personName('六六六', 222, city='北京', job='动画设计师')

print('----参数组合----------')
# 就是把所有类型的参数组合起来用
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

print('------递归函数------------')
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身函数，这个函数就是递归函数
