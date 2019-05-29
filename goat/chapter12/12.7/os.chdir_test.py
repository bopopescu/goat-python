# coding: utf-8

import os

# 获取当前目录
print(os.getcwd())  # G:\publish\codes\12\12.7
# 改变当前目录
os.chdir('../12.6')
# 再次获取当前目录
print(os.getcwd())  # G:\publish\codes\12\12.6
