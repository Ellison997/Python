#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('100+200=',100+200)
name=input('请输入你的名字：')
print('hello',name)
# 格式化字符串
print('%s成绩提升了：%.1f %%' % ('小明',(85-72)/72*100))
lenthx=1.75
kgx=80.5
x=(kgx/lenthx)*(kgx/lenthx)

a=100
if a>20:
    print(a)
else:
    print(-a)
print(x)
sum=0
for x in range(101):
    sum+=x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('hello %s' % l)


