# -*- coding: utf-8 -*-
# 告诉python解释器，按照UTF-8编码读取源代码。否则，输出的中文可能有乱码
print('-------------高阶函数---------')
# python 内建了map()和 reduct()函数

# map() 函数接收两个参数，一个是函数，一个是 Iterable,map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterable返回


def f(x):
    return x*x


r = map(f, [1, 2, 3, 4, 5, 67, 3, 88])
print(list(r))
# r是一个Iterator,Iterators是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list
s = map(str, [1, 2, 3, 4, 33, 5, 44, 66, 44, 7, 44])
print(list(s))

# reduce 的用法。 reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce把结果
# 继续和序列的下一个元素做累积运算。   reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


from functools import reduce


def fn(x, y):
    return x*10 + y


fni = reduce(fn, [1, 3, 4, 2, 35])
print(fni)

# 写一个str转int的function
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x*10+y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int(['2', '4', '7', '3']))

# python 内建的filter()函数用于过滤序列


def is_odd(n):
    # 如果是奇数就返回true
    return n % 2 == 1


odd = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(odd)

# 把一个空的字符串从集合中删掉


def not_empty(s):
    return s and s.strip()


empty = list(filter(not_empty, ['A', '', 'B', 'V', 'c', '', None]))
print(empty)

print('-----------排序算法 sorted----------')
# sorted 是一个高阶函。用sorted()排序的关键是在于实现一个映射函数
print(sorted([36, -22, 44, 33, -66, 88, 44]))

# 可以接收一个key实现自定义排序
print(sorted([36, -22, -44, 33, -66, 88, 44], key=abs))
# 反向排序
print(sorted([36, -22, -44, 33, -66, 88, 44], key=abs, reverse=True))

print('--------返回函数------------')
# 闭包


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

print('-----------匿名函数------------')
# 关键字lambda 表示匿名函数，冒号前面的x表示函数参数
lists=list(map(lambda x:x*x,[1,2,3,44,22,11,55]))
print(lists)

print('-----------装饰器------------')
# 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2018-2-24')
f=now
f()
print(f.__name__)

# 要增强now函数的功能，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper
# 因为log 是一个 decorator ,所以接收一个函数作为参数，并返回一个函数，
@log            # 相当于执行了 noww=log(noww)
def noww():
    print('2018-2-24')
ff=noww
ff()
print(ff.__name__)   # wrapper

# 以为返回的那个 wrapper（）函数名字就是'wrapper',所以，需要把原始函数的__name__等属性复制到
# wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错

# python 内置了 functools.wraps
import functools
def logg(funct):
    @functools.wraps(funct)
    def wrapper(*args,**kw):
        print('call %s():' % funct.__name__)
        return funct(*args,**kw)
    return wrapper
@logg            
def nowww():
    print('2018-2-24')
fff=nowww
fff()
print(fff.__name__)   # nowww

print('偏函数')
# functools 模块提供了很多功能，其中一个就是偏函数， 它可以降低调用函数的难度，就是给函数赋一个默认值
int2=functools.partial(int,base=2)      # int 默认是十进制转换的，现在改为二进制
print(int2('11110'))

# 添加默认值
max2=functools.partial(max,55)
print(max2(22,33,44,11))