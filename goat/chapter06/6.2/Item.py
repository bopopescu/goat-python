# coding: utf-8

class Item:
    # 直接在类空间中放置执行性质代码
    print('正在定义Item类')
    for i in range(10):
        if i % 2 == 0 :
            print('偶数:', i)
        else:
            print('奇数:', i)
