# coding: utf-8

import time
# 获取当前时间
a = time.gmtime()
b =  time.gmtime()
print(a == b) # a和b两个时间相等，输出True
print(a is b) # a和b不是同一个对象，输出False
print(id(a))
print(id(b))