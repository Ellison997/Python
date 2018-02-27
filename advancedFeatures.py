# -*- coding: utf-8 -*-
# 告诉python解释器，按照UTF-8编码读取源代码。否则，输出的中文可能有乱码
print('------切片 Slice----------')
L = ['tianchunle', 'tianshuo', 'liuhonghong', 'yanghongchun', 'liranran']
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
# 切片
s = L[0:3]
print(s)

# 倒数切片
print(L[-2:])

# 创建一个0-99的序列
num = list(range(100))
print(num)

# 后10个数
print(num[-10:])

# 前10-20个数
print(num[10:21])

# 前10个数，每2个取一个
print(num[:10:2])

# 所有数，每五个取一个
print(num[::5])

# 什么都不写，可以复制一个list
nums = num[:]
num[3] = 55
print(nums)
print(num)

print('-------迭代-----------')
# python,迭代是通过for...in..来完成的，python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

# 迭代字典 dict
di = {'a': 1, 'b': 2, 'c': 3}
for key in di:
    print(key)
# 默认情况下，dict迭代的是key。如果要迭代value。可以用 for value in d.Values(),
# 如果要同时迭代key 和 value , 可以用 for k,v in d.items()
for s, d in di.items():
    print(s+',,,'+str(d))

# 列表生成式
print('-----列表生成式------')
sss = [x*x for x in range(1, 11)]
print(sss)

# for 循环后面可以加上if判断
sse = [x*x for x in range(1, 21) if x % 2 == 0]
print(sse)

# 使用两层循环，可以生成全排列
ssw = [m+n for m in 'WER' for n in "ABC"]
print(ssw)

# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录

# 把L列表全都变成大写
print([ll.upper() for ll in L])


print('---------生成器-------------')
# 在python中， 一边循环一边计算的机制，称为生成器：generator
g = (x*x for x in range(22))  # g就是一个generator
print(g)
for gg in g:
    print(gg)

# generator 是可迭代对象，可以使用for循环迭代

# yield 关键字


def fid(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'


f = fid(11)
print(f)  # <generator object fid at 0x0000027030701E60>

# generator和函数的执行流程不一样。函数是顺序执行，遇到return 语句或者最后一行
# 函数语句就返回。而generator函数，在每次调用next（）的时候执行，遇到yield语句
# 返回，再次执行时从上次返回的yield语句处继续执行

print('---------迭代器--------')
# 可直接作用于for循环的数据类型有一下几种。
# 一类是集合数据类型，如 list、tuple、set、dist、str等
# 一类是generator,包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

# 可以使用 isinstance() 判断一个对象是否是 Iterable对象
# Iterable：可迭代的
# Iterator: 迭代器
from collections import Iterator, Iterable

print(isinstance((x for x in range(11)), Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('ssss', Iterable))
print(isinstance(1, Iterable))

# 判断一个对象是否为 Iterator对象
print(isinstance((x for x in range(11)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('ssss', Iterator))
print(isinstance(1, Iterator))

# 为什么list、dict、str等数据类型不是Iterator？
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函
# 数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数
# 据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数
# 实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
