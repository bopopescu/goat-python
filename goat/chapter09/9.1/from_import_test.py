# coding: utf-8

# 导入sys模块的argv成员
from sys import argv
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])




# 导入sys模块的argv,winver成员
from sys import argv, winver
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
print(winver)


# 导入sys模块的argv,winver成员，并为其指定别名v、wv
from sys import argv as v, winver as wv
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
print(wv)


# 导入sys模块的所有成员
from sys import *
# 使用导入成员的语法，直接使用成员的别名访问
print(argv[0])
print(winver)
