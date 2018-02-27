#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 这是一个测试模块 '
__author__='田春乐'
import sys

# 第一行和第二行是标准注释
# 第三行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都可以视为模块的文档注释
 

# 为了编写可维护性的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
# 很多编程语言都采用这种组织代码的方式，在python中，一个 .py 文件就称之为一个模块(Module)

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello World')
    elif len(args)==2:
        print('Hello %s!' %args[1])
    else:
        print('Too mant arguments!')
if __name__=='__main__':
    test()

print('-----安装常用模块-----------')
# pip install Pillow

# 模块搜索路径
# 默认情况下，python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print(sys.path)

# 自定义路径设置，设置环境变量PYTHONPATH



