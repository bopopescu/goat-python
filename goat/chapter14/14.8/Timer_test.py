# coding: utf-8

from threading import Timer

def hello():
    print("hello, world")
# 指定10秒后执行hello函数
t = Timer(10.0, hello)
t.start()