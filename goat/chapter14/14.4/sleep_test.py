# coding: utf-8

import time

for i in range(10):
    print("当前时间: %s" % time.ctime())
    # 调用sleep()函数让当前线程暂停1s
    time.sleep(1)