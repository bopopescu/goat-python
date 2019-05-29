# coding: utf-8

import multiprocessing
import os

def foo(q):
    print('被启动的新进程: (%s)' % os.getpid())
    q.put('Python')
if __name__ == '__main__':
    # 设置使用fork方式启动进程，并获取Context对象
    ctx = multiprocessing.get_context('fork')
    # 接下来就可用Context对象来代替mutliprocessing模块了
    q = ctx.Queue()
    # 创建进程
    mp = ctx.Process(target=foo, args=(q, ))
    # 启动进程
    mp.start()
    # 获取队列中的消息 
    print(q.get())
    mp.join()
