# coding: utf-8

# 导入sys整个模块
import sys
# 使用sys模块名作为前缀来访问模块中的成员
print(sys.argv[0])


# 导入sys、os两个模块
import sys,os
# 使用模块名作为前缀来访问模块中的成员
print(sys.argv[0])
# os模块的sep变量代表平台上的路径分隔符
print(os.sep)


# 导入sys、os两个模块，并为sys指定别名s，为os指定别名o
import sys as s,os as o
# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)